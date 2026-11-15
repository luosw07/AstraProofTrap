"""Offline integration tests. No model service, credentials, or network required."""
import contextlib
import csv
from http.client import IncompleteRead
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('evaluate', ROOT / 'evaluate.py')
ev = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ev)


class Reply(io.BytesIO):
    def __init__(self, data):
        super().__init__(json.dumps(data).encode())


def completion(content='VERDICT: ACCEPT\nA complete review.', finish='stop'):
    return {'model': 'returned-model', 'choices': [{'message': {'content': content},
            'finish_reason': finish}], 'usage': {'prompt_tokens': 123, 'completion_tokens': 45}}


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'repo'
        paper = self.root / 'examples/001/paper'
        paper.mkdir(parents=True)
        (paper / 'paper.tex').write_text('FIRST\n\\input{support}\nLAST-MANUSCRIPT-LINE')
        (paper / 'support.tex').write_text('SUPPORT-CONTENT')
        (paper / 'paper.pdf').write_bytes(b'PDF-NOT-SENT')
        (paper.parent / 'README.md').write_text('SECRET-ANSWER-KEY')
        (paper.parent / 'reports').mkdir()
        (paper.parent / 'reports/checker_report.md').write_text('SECRET-ANSWER-REPORT')
        (self.root / 'protocol').mkdir()
        (self.root / 'protocol/reviewer-template.txt').write_text('NEUTRAL-REVIEW-PROMPT')
        self.output = Path(self.tmp.name) / 'run'

    def args(self, *extra):
        return ev.parser().parse_args(['run', '--case', '001', '--model', 'test-model',
                                      '--output', str(self.output), *extra])

    def rows(self):
        with (self.output / 'summary.csv').open(newline='') as f:
            return list(csv.DictReader(f))

    def run_silently(self, args):
        with contextlib.redirect_stdout(io.StringIO()):
            return ev.run(args, self.root)

    def test_dry_run_is_offline_and_contains_full_paper_only(self):
        with patch.object(ev, 'request_completion', side_effect=AssertionError('Network')):
            self.assertEqual(self.run_silently(self.args('--dry-run', '--repeats', '2')), 0)
        packet = (self.output / 'inputs/001.txt').read_text()
        self.assertIn('LAST-MANUSCRIPT-LINE', packet)
        self.assertIn('SUPPORT-CONTENT', packet)
        self.assertNotIn('SECRET', packet)
        self.assertNotIn('PDF-NOT-SENT', packet)
        self.assertEqual([r['status'] for r in self.rows()], ['dry_run', 'dry_run'])
        self.assertIn('paper.pdf', (self.output / 'README.md').read_text())

    def test_wire_requests_are_independent_and_results_are_saved(self):
        requests = []

        class MockOpener:
            def open(inner, request, timeout):
                requests.append(request)
                return Reply(completion())

        with patch.dict(os.environ, {'MODEL_API_KEY': 'test-secret'}), patch.object(ev, 'build_opener', return_value=MockOpener()):
            code = self.run_silently(self.args('--base-url', 'https://model.example/v1',
                                              '--repeats', '2', '--effort', 'high',
                                              '--max-output-tokens', '1000'))
        self.assertEqual(code, 0)
        self.assertEqual(len(requests), 2)
        payloads = [json.loads(q.data) for q in requests]
        self.assertEqual(payloads[0], payloads[1])
        self.assertEqual(len(payloads[0]['messages']), 2)
        self.assertEqual(payloads[0]['reasoning_effort'], 'high')
        self.assertEqual(payloads[0]['max_completion_tokens'], 1000)
        self.assertNotIn('SECRET-ANSWER-KEY', str(payloads))
        self.assertEqual(requests[0].get_header('Authorization'), 'Bearer test-secret')
        self.assertEqual([row['report'] for row in self.rows()], [
            'reports/001/reviewer_high_01.md', 'reports/001/reviewer_high_02.md'])
        for row in self.rows():
            self.assertEqual(row['status'], 'completed')
            self.assertEqual(row['target_detected'], 'unscored')
            self.assertEqual(row['accepted_with_error'], '')
            self.assertEqual(row['prompt_tokens'], '123')
            self.assertTrue((self.output / row['report']).is_file())
        for p in self.output.rglob('*'):
            if p.is_file():
                self.assertNotIn('test-secret', p.read_text())

    def test_public_reference_text_is_complete_and_private_material_is_excluded(self):
        refs = self.root / 'examples/001/paper/references'
        refs.mkdir()
        (refs / 'source.pdf').write_bytes(b'PDF-NOT-SENT')
        (refs / 'source.txt').write_text('FULL-REFERENCE\nLAST-REFERENCE-LINE')
        (refs / 'README.md').write_text('REFERENCE-METADATA-NOT-SENT')
        with patch.object(ev, 'request_completion', side_effect=AssertionError('Network')):
            self.assertEqual(self.run_silently(self.args('--dry-run')), 0)
        packet = (self.output / 'inputs/001.txt').read_text()
        self.assertIn('FILE: references/source.txt', packet)
        self.assertIn('LAST-REFERENCE-LINE', packet)
        self.assertNotIn('SECRET', packet)
        self.assertNotIn('REFERENCE-METADATA-NOT-SENT', packet)
        self.assertEqual(self.rows()[0]['input_mode'], 'tex_text_with_references')

    def test_reference_omission_is_explicit_and_recorded(self):
        refs = self.root / 'examples/001/paper/references'
        refs.mkdir()
        (refs / 'source.pdf').write_bytes(b'PDF')
        (refs / 'source.txt').write_text('PUBLIC-REFERENCE')
        self.run_silently(self.args('--dry-run', '--references', 'omit'))
        self.assertNotIn('PUBLIC-REFERENCE', (self.output / 'inputs/001.txt').read_text())
        self.assertEqual(self.rows()[0]['input_mode'], 'tex_text')
        self.assertIn('Public reference texts: omit', (self.output / 'README.md').read_text())

    def test_missing_reference_text_fails_before_a_request(self):
        refs = self.root / 'examples/001/paper/references'
        refs.mkdir()
        (refs / 'source.pdf').write_bytes(b'PDF')
        with patch.object(ev, 'request_completion', side_effect=AssertionError('Network')):
            with self.assertRaisesRegex(ValueError, 'Missing extracted text'):
                self.run_silently(self.args('--dry-run'))
        self.assertFalse(self.output.exists())

    def test_length_failure_does_not_count_as_acceptance(self):
        with patch.object(ev, 'request_completion', return_value=completion('VERDICT: ACCEPT\nPartial', 'length')):
            self.assertEqual(self.run_silently(self.args('--base-url', 'http://localhost:8000/v1', '--no-auth')), 1)
        row = self.rows()[0]
        self.assertEqual(row['report'], 'reports/001/reviewer_provider_default_01.md')
        self.assertEqual(row['status'], 'incomplete')
        self.assertEqual(row['accepted_with_error'], '')
        score = ev.parser().parse_args(['score', str(self.output), '--case', '001', '--repeat', '1', '--detected', 'no', '--note', 'Target absent'])
        with self.assertRaises(ValueError):
            ev.score(score)

    def test_error_is_recorded_and_next_run_continues(self):
        with patch.object(ev, 'request_completion', side_effect=[ValueError('HTTP 400'), completion()]):
            self.assertEqual(self.run_silently(self.args('--base-url', 'https://model.example/v1', '--no-auth', '--repeats', '2')), 1)
        self.assertEqual([r['status'] for r in self.rows()], ['error', 'completed'])

    def test_interruption_preserves_completed_and_unstarted_requests(self):
        with patch.object(ev, 'request_completion', side_effect=[completion(), KeyboardInterrupt()]):
            with self.assertRaises(KeyboardInterrupt):
                self.run_silently(self.args('--base-url', 'https://model.example/v1', '--no-auth', '--repeats', '3'))
        rows = self.rows()
        self.assertEqual([r['status'] for r in rows], ['completed', 'interrupted', 'not_run'])
        self.assertIn('A complete review.', (self.output / rows[0]['report']).read_text())

    def test_broken_http_response_becomes_a_recorded_error(self):
        opener = unittest.mock.Mock()
        opener.open.side_effect = IncompleteRead(b'partial-private-data')
        with patch.object(ev, 'build_opener', return_value=opener):
            self.assertEqual(self.run_silently(self.args('--base-url', 'https://model.example/v1', '--no-auth')), 1)
        self.assertEqual(self.rows()[0]['status'], 'error')
        self.assertNotIn('partial-private-data', self.rows()[0]['error'])

    def test_scoring_reads_report_separately_and_keeps_verdict(self):
        with patch.object(ev, 'request_completion', return_value=completion()):
            self.run_silently(self.args('--base-url', 'https://model.example/v1', '--no-auth'))
        for detected, expected in [('yes', 'false'), ('no', 'true'), ('uncertain', '')]:
            args = ev.parser().parse_args(['score', str(self.output), '--case', '001', '--repeat', '1', '--detected', detected, '--note', 'Compared the reported composition identity with the checker report.'])
            with contextlib.redirect_stdout(io.StringIO()):
                ev.score(args)
            row = self.rows()[0]
            self.assertEqual(row['verdict'], 'ACCEPT')
            self.assertEqual(row['accepted_with_error'], expected)

    def test_rejection_that_misses_target_is_not_an_accept_miss(self):
        with patch.object(ev, 'request_completion', return_value=completion('REJECT\nAn unrelated error.')):
            self.run_silently(self.args('--base-url', 'https://model.example/v1', '--no-auth'))
        args = ev.parser().parse_args(['score', str(self.output), '--case', '001', '--repeat', '1',
                                      '--detected', 'no', '--note', 'Only an unrelated error is identified.'])
        with contextlib.redirect_stdout(io.StringIO()):
            ev.score(args)
        self.assertEqual(self.rows()[0]['accepted_with_error'], 'false')

    def test_existing_output_is_never_overwritten(self):
        self.output.mkdir()
        (self.output / 'keep.txt').write_text('keep')
        with self.assertRaises(FileExistsError):
            self.run_silently(self.args('--dry-run'))
        self.assertEqual((self.output / 'keep.txt').read_text(), 'keep')

    def test_invalid_cases_and_symlink_resources_fail_before_requests(self):
        with self.assertRaises(ValueError):
            ev.select_cases(self.root, ['../001'])
        paper = self.root / 'examples/001/paper'
        (paper / 'leak.tex').symlink_to(paper.parent / 'README.md')
        with self.assertRaises(ValueError):
            ev.manuscript(self.root, '001')

    def test_credentials_and_provider_errors_are_not_logged(self):
        class ErrorOpener:
            def open(inner, request, timeout):
                raise HTTPError(request.full_url, 401, 'secret-in-reason', {}, io.BytesIO(b'secret-in-body'))
        with patch.object(ev, 'build_opener', return_value=ErrorOpener()):
            with self.assertRaises(ValueError) as caught:
                ev.request_completion('https://model.example/v1/chat/completions', 'secret', {}, 10)
        self.assertNotIn('secret', str(caught.exception))

    def test_timeout_is_not_retried(self):
        opener = unittest.mock.Mock()
        opener.open.side_effect = URLError('private-error-detail')
        with patch.object(ev, 'build_opener', return_value=opener):
            with self.assertRaises(ValueError):
                ev.request_completion('https://model.example/v1/chat/completions', '', {}, 10)
        self.assertEqual(opener.open.call_count, 1)

    def test_parse_report_states(self):
        for body, status in [(completion('ACCEPT'), 'completed'),
                             (completion(''), 'invalid_report'),
                             (completion('VERDICT: UNCERTAIN\nUnresolved lemma.'), 'completed'),
                             (completion('VERDICT: REJECT\nIncorrect step.'), 'completed')]:
            self.assertEqual(ev.parse_response(body)[3], status)
        data = completion()
        data['choices'][0]['message']['refusal'] = 'Unable to comply'
        self.assertEqual(ev.parse_response(data)[3], 'refused')
        with self.assertRaises(ValueError):
            ev.parse_response({'choices': []})

    def test_endpoint_validation_and_no_redirect(self):
        for bad in ['https://user:key@host/v1', 'https://host/v1?key=secret',
                    'http://remote.example/v1', 'https://host/v1/chat/completions']:
            with self.assertRaises(ValueError):
                ev.endpoint_url(bad)
        self.assertEqual(ev.endpoint_url('http://127.0.0.1:8000/v1/'), 'http://127.0.0.1:8000/v1/chat/completions')
        self.assertIsNone(ev.NoRedirect().redirect_request(None, None, 302, '', {}, 'https://other.example'))


if __name__ == '__main__':
    unittest.main()
