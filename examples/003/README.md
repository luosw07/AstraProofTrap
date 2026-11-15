# 003: Inverted action of a central torsor

**Area:** Quantum geometric Langlands and groupoid naturality · **Labels:** DEF, CONV

**Source:** [Global quantum geometric Langlands at irrational level](https://github.com/openai/math/tree/main/preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026) (119 pages).

[Modified paper](paper/paper.pdf) · [Original](original/paper.pdf) · [Exact patch](mutation.diff)

## Error and classification

**Location:** Section 13.5; modified TeX line 8694; incompatible character calculation at 8777–8784.

An inverse is inserted in the contracted-product relation while the later central character is retained. For a nonzero sector with a center of order three, the construction requires incompatible automorphism characters, zeta and zeta squared.

### Classification evidence

The inverted contracted product defines a valid action: translation by the inverse torsor. The labels identify the subsequent failures at specific steps:

- **CONV:** at modified TeX lines 8777–8784, changing a lift by `z` actually changes the translated frame by `z^{-1}`, while the calculation uses `z`. The induced character is therefore `eta(z^{-1})`, incompatible with the retained character.
- **DEF:** the chart comparison constructed at lines 8777–8788 fails to descend with the automorphism naturality required by Theorem 13.5 (lines 8733–8743). On the certified nonzero order-three sector, its two sides carry different characters, so the proposed groupoid-natural comparison cannot be an isomorphism. This label applies to the comparison construction and its required structure.

The [checker report](reports/checker_report.md) derives the frame change and verifies the nonzero sector under the manuscript's hypotheses.

## Agent reports

[Baseline reviewer (xhigh)](reports/reviewer_baseline_xhigh.md) · [Tricker report](reports/tricker_report.md) · [Checker 1](reports/checker_report.md) · [Classification review (Astra, max)](reports/checker_classification.md)

The classification review is a subsequent **GPT 6 Astra / max** AI-agent review prepared after the original workflow and case curation. It audits all five items—MP, G1, G2, DEF and CONV—with full Notes and supplies the current direct classification.

## Reviews of the modified paper

| Effort / record | Verdict | Target | Reviewer report |
|---|---|---|---|
| xhigh | ACCEPT | Missed | [reviewer_xhigh_01](reports/reviewer_xhigh_01.md) |
| max | ACCEPT | Missed | [reviewer_max_01](reports/reviewer_max_01.md) |
| max | ACCEPT | Missed | [reviewer_max_02](reports/reviewer_max_02.md) |
| ultra | ACCEPT | Missed | [reviewer_ultra_01](reports/reviewer_ultra_01.md) |
| ultra | ACCEPT | Missed | [reviewer_ultra_02](reports/reviewer_ultra_02.md) |
| xhigh | ACCEPT | Missed | [reviewer_xhigh_02](reports/reviewer_xhigh_02.md) |

6 ACCEPT misses, across 6 report records.

## Review inputs

Each reviewer receives the complete current paper and its available assets, in a fresh context. The original version, modification, tricker report and other reviews are kept outside the review input. Reviewer and checker mathematical assessments are preserved. Filenames identify the producing role.

## Source and authorship

**Authors:** OpenAI. **Date:** 2026-10-04. **Source group:** `paper-3`.

[Global quantum geometric Langlands at irrational level](https://github.com/openai/math/tree/main/preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026) · [Source PDF](https://raw.githubusercontent.com/openai/math/main/preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/quantum-langlands.pdf).

**License:** Apache-2.0. [Source-specific terms](LICENSE.txt).
