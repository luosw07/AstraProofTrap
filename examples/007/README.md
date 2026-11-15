# 007: Copying jet-action matrices across moving divisors

**Area:** Quantum geometric Langlands and deformation of Lie algebra representations · **Labels:** DEF, CONV

**Source:** [Global quantum geometric Langlands at irrational level](https://github.com/openai/math/tree/main/preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026) (119 pages).

[Modified paper](paper/paper.pdf) · [Original](original/paper.pdf) · [Exact patch](mutation.diff)

## Error and classification

**Location:** paper.tex, Proposition 7.3 (loop:crystal), lines 4336-4338: obtain lifted inducing representations by retaining jet-current action matrices in the monic coefficient bases; the linear convention itself is at lines 3887-3891.

A base-linear identification of monic jet coefficient bases is used to copy the matrices of a genuine inducing representation. The coefficient multiplication table changes with the divisor, so the prescribed target matrices fail its Lie bracket, and the asserted identical PBW/cobar coefficient diagrams fail.

Run the exact algebra certificate from the repository root:

```sh
python3 examples/007/reports/checker_calculation.py
```

The script uses only the Python standard library. It verifies the genuine source/target relations and asserts the exact nonzero defect of the copied action, then prints the results. It requires no local configuration and writes no files.

## Agent reports

[Baseline reviewer (xhigh)](reports/reviewer_baseline_xhigh.md) · [Tricker report](reports/tricker_report.md) · [Checker 1](reports/checker_report.md) · [Classification review (Astra, max)](reports/checker_classification.md)

The classification review is a subsequent **GPT 6 Astra / max** AI-agent review prepared after the original workflow and case curation. It audits all five items—MP, G1, G2, DEF and CONV—with full Notes and supplies the current direct classification.

## Reviews of the modified paper

| Effort / record | Verdict | Target | Reviewer report |
|---|---|---|---|
| medium | UNCERTAIN | Missed | [reviewer_medium_01](reports/reviewer_medium_01.md) |
| high | REJECT | Detected | [reviewer_high_01](reports/reviewer_high_01.md) |
| xhigh | ACCEPT | Missed | [reviewer_xhigh_01](reports/reviewer_xhigh_01.md) |
| max | REJECT | Detected | [reviewer_max_01](reports/reviewer_max_01.md) |
| ultra | ACCEPT | Missed | [reviewer_ultra_01](reports/reviewer_ultra_01.md) |

1 UNCERTAIN miss, 2 REJECT detections, 2 ACCEPT misses, across 5 report records.

## Review inputs

Each reviewer receives the complete current paper and its available assets, in a fresh context. The original version, modification, tricker report and other reviews are kept outside the review input. Reviewer and checker mathematical assessments are preserved. Filenames identify the producing role.

## Source and authorship

**Authors:** OpenAI. **Date:** 2026-10-04. **Source group:** `paper-3`.

[Global quantum geometric Langlands at irrational level](https://github.com/openai/math/tree/main/preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026) · [Source PDF](https://raw.githubusercontent.com/openai/math/main/preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/quantum-langlands.pdf).

**License:** Apache-2.0. [Source-specific terms](LICENSE.txt).
