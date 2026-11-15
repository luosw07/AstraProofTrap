# 005: Strengthened endpoint time norm

**Area:** Analysis and PDE: Boussinesq temperature patches · **Labels:** MP

**Source:** [Global regularity and infinite Prandtl-number limit for 2D Boussinesq temperature patches in W^{k,infinity} and C^{k,gamma}: lower-order case](https://arxiv.org/abs/2610.12253v1) (70 pages).

[Modified paper](paper/paper.pdf) · [Original](original/paper.pdf) · [Exact patch](mutation.diff)

## Error and classification

**Location:** Theorem 1.1 and Proposition 3.2(1); modified TeX lines 353 and 4748.

Two Chemin–Lerner tildes are removed, strengthening the endpoint estimate to an ordinary time-integrated Besov norm. Exact radial swirl solutions with separated frequencies have square-summable initial energy and a divergent ordinary critical time norm.

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

**Authors:** Omar Lazar, Liutang Xue, Jiakun Yang. **Date:** 2026-10-08. **Source group:** `paper-5`.

[Global regularity and infinite Prandtl-number limit for 2D Boussinesq temperature patches in W^{k,infinity} and C^{k,gamma}: lower-order case](https://arxiv.org/abs/2610.12253v1) · [Source PDF](https://arxiv.org/pdf/2610.12253v1).

**License:** CC BY-NC-ND 4.0. [Source-specific terms](LICENSE.txt).
