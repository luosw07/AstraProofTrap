# 006: Altered scaling threshold

**Area:** Analysis and PDE: nonlinear Schrodinger instability · **Labels:** CONV

**Source:** [Instability theory of stationary solutions for nonlinear Schrödinger equations](https://arxiv.org/abs/2610.39830v1) (66 pages).

[Modified paper](paper/paper.pdf) · [Original](original/paper.pdf) · [Exact patch](mutation.diff)

## Error and classification

**Location:** Section 1.2, equation (1.8); modified TeX line 369.

A one-line rational threshold changes the coefficient d(d−2) to (d+1)(d−2)/2. The one- and two-dimensional formulas and plotted qualitative behavior survive. An actual higher-dimensional ground state gives a positive scaling second derivative in the falsely admitted range.

## Agent reports

[Baseline reviewer (medium)](reports/reviewer_baseline_medium.md) · [Tricker report](reports/tricker_report.md) · [Checker 1](reports/checker_report.md) · [Classification review (Astra, max)](reports/checker_classification.md)

The classification review is a subsequent **GPT 6 Astra / max** AI-agent review prepared after the original workflow and case curation. It audits all five items—MP, G1, G2, DEF and CONV—with full Notes and supplies the current direct classification.

## Reviews of the modified paper

| Effort / record | Verdict | Target | Reviewer report |
|---|---|---|---|
| medium | ACCEPT | Missed | [reviewer_medium_01](reports/reviewer_medium_01.md) |
| max | REJECT | Detected | [reviewer_max_01](reports/reviewer_max_01.md) |
| ultra | ACCEPT | Missed | [reviewer_ultra_01](reports/reviewer_ultra_01.md) |
| xhigh | REJECT | Detected | [reviewer_xhigh_01](reports/reviewer_xhigh_01.md) |

2 ACCEPT misses, 2 REJECT detections, across 4 report records.

## Review inputs

Each reviewer receives the complete current paper and its available assets, in a fresh context. The original version, modification, tricker report and other reviews are kept outside the review input. Reviewer and checker mathematical assessments are preserved. Filenames identify the producing role.

## Source and authorship

**Authors:** Noriyoshi Fukaya, Masayuki Hayashi. **Date:** 2026-10-29. **Source group:** `paper-6`.

[Instability theory of stationary solutions for nonlinear Schrödinger equations](https://arxiv.org/abs/2610.39830v1) · [Source PDF](https://arxiv.org/pdf/2610.39830v1).

**License:** arXiv non-exclusive distribution license; author copyright retained. [Source-specific terms](LICENSE.txt).
