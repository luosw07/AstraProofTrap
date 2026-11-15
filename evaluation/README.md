# Evaluate a model

`evaluate.py` is the evaluation entry point. It runs independent blind reviews through a Chat Completions compatible endpoint, saves each complete response, and records the overall verdict separately from manual target detection. It requires **Python 3.10+**, with no third-party packages.

The reviewer uses the same [prompt](../protocol/reviewer-template.txt) as the [agent workflow](../protocol/README.md). The input is the complete manuscript source plus supplied public reference texts. PDFs, images and tool access belong to the agent review setting; this runner uses text messages. [Case notes](case-notes.md) describe the published examples with special input conditions.

## 1. Preview the input

Run from the repository root:

```sh
python3 evaluation/evaluate.py run \
  --case 001 --model YOUR_MODEL --effort high \
  --dry-run --output runs/preview
```

Open `runs/preview/prompt.txt` and `runs/preview/inputs/001.txt` to inspect the exact messages. This command works offline. Every output directory must be new.

The runner reads only `examples/NNN/paper/`: all `.tex`, `.sty`, `.cls`, `.bib`, `.bbl` and `.tikz` resources, plus any `references/*.txt` files. It sends these files in full and excludes case descriptions, originals, patches and reports. Each request starts with the same saved prompt and case input, without conversation history. Inputs are never shortened automatically.

## 2. Run independent reviews

Set `MODEL_API_KEY` in your environment, then choose the endpoint, model and effort supported by your provider:

```sh
python3 evaluation/evaluate.py run \
  --base-url https://YOUR_PROVIDER/v1 \
  --model YOUR_MODEL --effort high \
  --case 001 007 --repeats 2 \
  --output runs/my-model
```

The endpoint must implement `POST /chat/completions`. `MODEL_BASE_URL` can supply the base URL. Use `--api-key-env NAME` to read a different key variable, or `--no-auth` for an unauthenticated local server. Requests run sequentially with no automatic retries.

| Option | Purpose |
|---|---|
| `--case all` | Review all examples; this is the default. |
| `--repeats 2` | Make two independent requests per case. |
| `--effort high` | Forward the chosen reasoning effort; an omitted value is recorded as `provider_default`. |
| `--references omit` | Use manuscript resources alone; supplied reference texts are included by default. |
| `--max-output-tokens 32000` | Set the output budget. |
| `--token-limit-field max_tokens` | Use this field instead of the default `max_completion_tokens`. |
| `--instruction-role developer` | Use a developer message instead of the default system message. |
| `--timeout 900` | Set the per-request timeout in seconds; default 900. |

The model needs enough context for the full input and output budget. Endpoint errors, context-limit errors, refusals and truncated responses are recorded separately from completed reviews. No parameter is silently changed to obtain a successful response.

## 3. Judge target detection

Read the saved reviewer report alongside the case's error description, `tricker_report.md` and `checker_report.md`. Determine whether it correctly identifies the planted invalid step or missing necessary hypothesis. A correction of the target counts as detection, even when the reviewer calls it minor or returns ACCEPT.

```sh
python3 evaluation/evaluate.py score runs/my-model \
  --case 001 --repeat 1 --detected yes \
  --note "The report identifies the reversed composition in Proposition 8.1."
```

`score` records a manual judgment and makes no model request. Use `yes`, `no`, or `uncertain`; supply the location and reason in the note. It updates the selected row while preserving the model's verdict. Repeating the command replaces that row's judgment.

| Verdict | Target detected | `accepted_with_error` |
|---|---|---|
| ACCEPT | no | true |
| ACCEPT | yes | false |
| REJECT or UNCERTAIN | yes or no | false |
| Any | uncertain or unscored | empty |

Only completed reports can receive a target judgment. For comparisons, report completed, failed and unscored request counts alongside the results; distinguish independent contexts from continuations. The [protocol](../protocol/README.md#reading-the-results) gives the detection criteria.

## Saved output

```text
runs/my-model/
  README.md                           Model, settings and input conditions
  prompt.txt                          Exact reviewer instruction
  inputs/001.txt                      Exact case input
  reports/001/reviewer_high_01.md      First high-effort review of case 001
  reports/001/reviewer_high_02.md      Second independent review
  summary.csv                         Verdict, detection, status and usage
```

`summary.csv` records `tex_text_with_references` when public reference text is included, and `tex_text` otherwise. The run description lists omitted files. Reports keep the full returned text, including incomplete responses. The API key is read from the environment and is not saved. `runs/` is ignored by Git.

A completed response must end normally and start with `ACCEPT`, `REJECT` or `UNCERTAIN`; `VERDICT:` is also accepted as a prefix. Exit codes are 0 for completed runs or offline previews, 1 for response/request failures, 2 for configuration/file errors, and 130 for interruption. Completed reports remain saved after interruption.

## Test the evaluator

```sh
python3 -m unittest discover -s evaluation/tests -v
```

`tests/test_evaluate.py` contains offline tests for input isolation, complete reference inclusion, independent requests, report naming, failure handling and target adjudication. It is a test suite; `evaluate.py` is the sole evaluation entry point.
