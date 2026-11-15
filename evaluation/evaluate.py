#!/usr/bin/env python3
"""Blind text-only evaluation through a Chat Completions compatible endpoint."""
import argparse
import csv
from datetime import datetime, timezone
from http.client import HTTPException
import json
import os
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {'.tex', '.sty', '.cls', '.bib', '.bbl', '.tikz'}
FIELDS = ['case', 'repeat', 'model', 'returned_model', 'effort', 'input_mode',
          'status', 'verdict', 'finish_reason', 'target_detected',
          'accepted_with_error', 'scoring_note', 'prompt_tokens',
          'completion_tokens', 'elapsed_seconds', 'report', 'error']


def positive(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError('Must be a positive integer.')
    return number


def endpoint_url(base):
    url = urlsplit(base)
    if (url.scheme not in {'https', 'http'} or not url.hostname
            or url.username or url.password or url.query or url.fragment):
        raise ValueError('Use a base URL without credentials, query, or fragment.')
    if url.scheme == 'http' and url.hostname not in {'localhost', '127.0.0.1', '::1'}:
        raise ValueError('Use HTTPS, except for a local model server.')
    if url.path.rstrip('/').endswith('/chat/completions'):
        raise ValueError('Supply the base URL (usually ending in /v1), not /chat/completions.')
    return base.rstrip('/') + '/chat/completions'


def select_cases(root, requested):
    available = sorted(p.name for p in (root / 'examples').iterdir()
                       if re.fullmatch(r'\d{3}', p.name) and (p / 'paper/paper.tex').is_file())
    selected = available if requested == ['all'] else list(dict.fromkeys(requested))
    if not selected or any(c not in available for c in selected):
        raise ValueError('Select case IDs from: ' + ', '.join(available) + ', or all.')
    return selected


def manuscript(root, case, references='include'):
    """Read only paper/, never case cards, originals, diffs, or reports."""
    folder = root / 'examples' / case / 'paper'
    if folder.is_symlink():
        raise ValueError('Symlinked paper directories are not supported.')
    files = sorted(folder.rglob('*'), key=lambda p: (p.name != 'paper.tex', str(p)))
    text, omitted = [], []
    for p in files:
        if p.is_symlink():
            raise ValueError('Symlinked manuscript resources are not supported.')
        if not p.is_file():
            continue
        name = p.relative_to(folder).as_posix()
        is_reference = name.startswith('references/')
        if is_reference and references == 'omit':
            omitted.append(name)
            continue
        if is_reference and p.suffix.lower() == '.pdf' and not p.with_suffix('.txt').is_file():
            raise ValueError(f'Missing extracted text for public reference: {name}')
        if p.suffix.lower() in TEXT_SUFFIXES or (is_reference and p.suffix.lower() == '.txt'):
            text.append(f'===== FILE: {name} =====\n{p.read_text(encoding="utf-8")}\n===== END FILE =====')
        else:
            omitted.append(name)
    if not text:
        raise ValueError('No manuscript text found.')
    return '\n\n'.join(text), omitted


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Do not forward a credential to a redirect target.
        return None


def request_completion(endpoint, key, payload, timeout):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    if key:
        headers['Authorization'] = 'Bearer ' + key
    request = Request(endpoint, data=json.dumps(payload).encode('utf-8'), headers=headers)
    try:
        with build_opener(NoRedirect()).open(request, timeout=timeout) as response:
            data = json.loads(response.read().decode('utf-8'))
    except HTTPError as exc:
        # Provider bodies can echo inputs or credentials; do not persist them.
        raise ValueError(f'HTTP {exc.code}; check endpoint, model, credentials, parameters, and context limit.') from None
    except (URLError, TimeoutError, OSError, HTTPException):
        raise ValueError('Connection failed or timed out; no automatic retry was sent.') from None
    except (UnicodeError, json.JSONDecodeError):
        raise ValueError('The endpoint returned an invalid JSON response.') from None
    if not isinstance(data, dict):
        raise ValueError('Expected a Chat Completions response object.')
    return data


def parse_response(data):
    try:
        choice = data['choices'][0]
        message = choice['message']
        finish = choice.get('finish_reason') or ''
        content = message.get('content') or ''
        if isinstance(content, list):
            content = '\n'.join(p['text'] for p in content
                                if p.get('type') == 'text' and isinstance(p.get('text'), str))
        if not isinstance(content, str):
            raise ValueError()
    except (KeyError, IndexError, TypeError, AttributeError, ValueError):
        raise ValueError('Malformed choices/message in response.') from None
    first = next((line.strip() for line in content.splitlines() if line.strip()), '')
    match = re.fullmatch(r'(?:VERDICT:\s*)?(ACCEPT|REJECT|UNCERTAIN)', first)
    verdict = match.group(1) if match else ''
    if message.get('refusal'):
        status = 'refused'
    elif finish != 'stop':
        status = 'incomplete'
    elif not content.strip() or not verdict:
        status = 'invalid_report'
    else:
        status = 'completed'
    return content, verdict, finish, status


def write_csv(path, rows):
    temp = path.with_suffix('.tmp')
    with temp.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(path)


def run(args, root=ROOT):
    cases = select_cases(root, args.case)
    if not args.dry_run and not args.base_url:
        raise ValueError('Set --base-url or MODEL_BASE_URL.')
    endpoint = endpoint_url(args.base_url) if args.base_url else '(dry run: no endpoint)'
    key = '' if args.dry_run or args.no_auth else os.environ.get(args.api_key_env, '')
    if not args.dry_run and not args.no_auth and not key.strip():
        raise ValueError(f'Set the {args.api_key_env} environment variable, or use --no-auth for an unauthenticated server.')
    prompt = (root / 'protocol/reviewer-template.txt').read_text(encoding='utf-8')
    packets = {case: manuscript(root, case, args.references) for case in cases}
    output = (args.output or root / 'runs' /
              (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid4().hex[:8]))
    output = output.resolve()
    # Refuse replacement of an existing run, including a score or partial result.
    output.mkdir(parents=True, exist_ok=False)
    (output / 'inputs').mkdir()
    (output / 'reports').mkdir()
    (output / 'prompt.txt').write_text(prompt, encoding='utf-8')
    rows = [{**dict.fromkeys(FIELDS, ''), 'case': case, 'repeat': str(repeat),
             'model': args.model, 'effort': args.effort or 'provider_default',
             'input_mode': ('tex_text_with_references' if args.references == 'include'
                            and any((root / 'examples' / case / 'paper/references').rglob('*.txt'))
                            else 'tex_text'),
             'status': 'not_run', 'target_detected': 'unscored'}
            for case in cases for repeat in range(1, args.repeats + 1)]
    summary = output / 'summary.csv'
    write_csv(summary, rows)
    notes = ['# Evaluation run', f'Started (UTC): {datetime.now(timezone.utc).isoformat()}',
             f'Dry run: {args.dry_run}', f'Model: {args.model}', f'Endpoint: {endpoint}',
             f'Instruction role: {args.instruction_role}',
             f'Effort: {args.effort or "provider default"}',
             f'Output limit: {args.max_output_tokens or "provider default"} ({args.token_limit_field})',
             f'Timeout per request: {args.timeout} seconds',
             f'Planned requests: {len(rows)}',
             f'Public reference texts: {args.references}',
             'Mode: complete TeX/text resources; no PDF, images, tools, or browsing.',
             'Each request contains only the neutral prompt and one paper packet. No conversation history.',
             'No automatic retries. Token usage is recorded when supplied by the endpoint.',
             'Target detection starts unscored; use the score command after reading the reviewer, tricker and checker reports.']
    for case, (text, omitted) in packets.items():
        (output / 'inputs' / f'{case}.txt').write_text(text, encoding='utf-8')
        notes.append(f'Case {case}: {len(text)} characters. Files not sent: {", ".join(omitted) or "none"}.')
    (output / 'README.md').write_text('\n\n'.join(notes) + '\n', encoding='utf-8')
    print(f'Output: {output}', flush=True)
    for row in rows:
        if args.dry_run:
            row['status'] = 'dry_run'
            continue
        payload = {'model': args.model, 'messages': [
            {'role': args.instruction_role, 'content': prompt},
            {'role': 'user', 'content': packets[row['case']][0]}], 'stream': False}
        if args.effort:
            payload['reasoning_effort'] = args.effort
        if args.max_output_tokens:
            payload[args.token_limit_field] = args.max_output_tokens
        row['status'] = 'running'
        write_csv(summary, rows)
        start = time.monotonic()
        try:
            data = request_completion(endpoint, key, payload, args.timeout)
            content, verdict, finish, status = parse_response(data)
            # The model should never see the key; also redact a provider echo.
            if key:
                content = content.replace(key, '[REDACTED]')
            effort_name = re.sub(r'[^A-Za-z0-9_-]', '_', row['effort'])
            name = f"reports/{row['case']}/reviewer_{effort_name}_{int(row['repeat']):02}.md"
            (output / name).parent.mkdir(parents=True, exist_ok=True)
            (output / name).write_text(content, encoding='utf-8')
            returned_model = str(data.get('model', ''))
            if key:
                returned_model = returned_model.replace(key, '[REDACTED]')
            usage = data.get('usage') if isinstance(data.get('usage'), dict) else {}
            row.update(status=status, verdict=verdict, finish_reason=finish, report=name,
                       returned_model=returned_model,
                       prompt_tokens=usage.get('prompt_tokens', ''),
                       completion_tokens=usage.get('completion_tokens', ''))
        except ValueError as exc:
            row.update(status='error', error=str(exc))
        except KeyboardInterrupt:
            row['status'] = 'interrupted'
            write_csv(summary, rows)
            raise
        finally:
            row['elapsed_seconds'] = f'{time.monotonic() - start:.3f}'
            write_csv(summary, rows)
        print(f"{row['case']} / {row['repeat']}: {row['status']} {row['verdict']}", flush=True)
    write_csv(summary, rows)
    return 0 if all(r['status'] in {'completed', 'dry_run'} for r in rows) else 1


def score(args):
    path = args.run_dir / 'summary.csv'
    with path.open(encoding='utf-8', newline='') as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != FIELDS:
            raise ValueError('Not an evaluate.py summary.csv file.')
        rows = list(reader)
    found = [r for r in rows if r['case'] == args.case and r['repeat'] == str(args.repeat)]
    if len(found) != 1:
        raise ValueError('No unique case/repeat row found.')
    row = found[0]
    if row['status'] != 'completed':
        raise ValueError('Only a completed, correctly formatted report can be scored.')
    if not args.note.strip():
        raise ValueError('Supply a scoring note with the matching location/reason.')
    row.update(target_detected=args.detected, scoring_note=args.note.strip(),
               accepted_with_error=('' if args.detected == 'uncertain' else
                                    str(args.detected == 'no' and row['verdict'] == 'ACCEPT').lower()))
    write_csv(path, rows)
    print(f"Scored {args.case} / {args.repeat}: target detected = {args.detected}")
    return 0


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    q = sub.add_parser('run', help='Run independent blind reviews, or prepare inputs offline.')
    q.add_argument('--case', nargs='+', default=['all'], help='Case IDs, e.g. 001 007; default: all.')
    q.add_argument('--model', required=True, help='Exact model ID accepted by your endpoint.')
    q.add_argument('--base-url', default=os.environ.get('MODEL_BASE_URL'))
    q.add_argument('--api-key-env', default='MODEL_API_KEY', help='Name of an environment variable, never the key itself.')
    q.add_argument('--no-auth', action='store_true', help='For an unauthenticated model server.')
    q.add_argument('--repeats', type=positive, default=1)
    q.add_argument('--effort', help='Forwarded unchanged as reasoning_effort; omitted by default.')
    q.add_argument('--references', choices=['include', 'omit'], default='include',
                   help='Include supplied public reference texts by default; omit for a manuscript-only run.')
    q.add_argument('--max-output-tokens', type=positive)
    q.add_argument('--token-limit-field', choices=['max_completion_tokens', 'max_tokens'], default='max_completion_tokens')
    q.add_argument('--instruction-role', choices=['system', 'developer'], default='system')
    q.add_argument('--timeout', type=positive, default=900)
    q.add_argument('--output', type=Path, help='New output directory; existing directories are refused.')
    q.add_argument('--dry-run', action='store_true', help='Save inputs and a plan; no key or network request.')
    q = sub.add_parser('score', help='Record manual target adjudication, separately from the model verdict.')
    q.add_argument('run_dir', type=Path)
    q.add_argument('--case', required=True)
    q.add_argument('--repeat', type=positive, required=True)
    q.add_argument('--detected', choices=['yes', 'no', 'uncertain'], required=True)
    q.add_argument('--note', required=True)
    return p


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        return run(args) if args.command == 'run' else score(args)
    except KeyboardInterrupt:
        print('Interrupted. Completed reports and current status are saved.', file=sys.stderr)
        return 130
    except (ValueError, OSError) as exc:
        # Filesystem errors can contain local paths, but never API request bodies.
        print(f'Error: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
