# 009: Missing moving-frame derivative in a constraint identity

**Area:** Differential geometry and supergravity · **Primary label:** CONV

**Source:** C. S. Shahbazi, [The Cauchy problem for skew-torsion-parallel spinors with applications to supergravity](https://arxiv.org/abs/2611.17319v1), submitted 12 November 2026, 65 pages. **Source group:** `arxiv-2611.17319v1`.

[Modified paper](paper/paper.pdf) · [Original](original/paper.pdf) · [Exact patch](mutation.diff)

## Error and classification

**Location:** page 46, first display, in the proof of Theorem 4.30 (`thm:compatibilityflows`); [TeX lines 3749–3752](paper/paper.tex#L3749). Its later use is at line 3769 in the derivation of the transverse constraint identity (67).

Fix a time, put $U=e_u^\sharp$, $L=e_l^\sharp$, $w=\iota_U\widehat c$, and $q=\Theta(U,-)$. The spatial constraint gives $dq=\frac12dw$. The modified proof then asserts

$$
D:=(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)=\tfrac12dw(U,L).
$$

Differentiating the contracted one-form also differentiates the moving field $U$. The covariant product rule and the unchanged coframe connection formula give

$$
D=\tfrac12dw(U,L)-\Theta(\nabla_UU,L)+\Theta(\nabla_LU,U)
=\tfrac12dw(U,L)+\tfrac12\Theta(w^\sharp,L).
$$

Symmetry cancels the other terms, but the final contraction remains. The mutation deletes precisely this contribution and changes the accompanying justification. **CONV** records the false expansion of a contracted exterior derivative. The tensor fields are well-defined and the required differentiation rule is available; the failed obligation is the calculation itself.

The checker constructs an actual smooth supersymmetry flow with initial coframe $e_u=e^x dz$, $e_l=e^z dx$, $e_n=dy$, flat initial gerbe curving, and dilaton $e^{ix}$. At $x=z=0$, the left side is $-1/2$ while the modified right side is zero. The deleted correction is exactly $-1/2$. The full constraint and flow checks are in the [checker report](reports/checker_report.md); several rejecting reviews also supply compact torus witnesses. Restoring the omitted term repairs this step of the proof.

Run `python3 examples/009/reports/checker_calculation.py` from the repository root. Using exact rational arithmetic and Koszul's formula, it independently computes the frame connection, the two covariant derivatives, and the omitted term at the checker's witness point. It produces **actual -1/2; modified 0; corrected -1/2**. The checker supplies the full geometric admissibility argument.

## Agent reports

[Baseline reviewer (medium)](reports/reviewer_baseline_medium.md) · [Tricker report](reports/tricker_report.md) · [Checker 1](reports/checker_report.md) · [Classification review (Astra, max)](reports/checker_classification.md)

The classification review is a subsequent **GPT 6 Astra / max** AI-agent review prepared after the original workflow and case curation. It audits all five items—MP, G1, G2, DEF and CONV—with full Notes and supplies the current direct classification.

## Reviews of the modified paper

| Effort / record | Verdict | Target | Reviewer report |
|---|---|---|---|
| medium | ACCEPT | Missed | [reviewer_medium_01](reports/reviewer_medium_01.md) |
| high | REJECT | Detected | [reviewer_high_01](reports/reviewer_high_01.md) |
| high | REJECT | Detected | [reviewer_high_02](reports/reviewer_high_02.md) |
| xhigh | REJECT | Detected | [reviewer_xhigh_01](reports/reviewer_xhigh_01.md) |
| xhigh | REJECT | Detected | [reviewer_xhigh_02](reports/reviewer_xhigh_02.md) |
| ultra | REJECT | Detected | [reviewer_ultra_01](reports/reviewer_ultra_01.md) |
| ultra | REJECT | Detected | [reviewer_ultra_02](reports/reviewer_ultra_02.md) |
| medium | ACCEPT | Missed | [reviewer_medium_02](reports/reviewer_medium_02.md) |
| medium | ACCEPT | Missed | [reviewer_medium_03](reports/reviewer_medium_03.md) |
| high | REJECT | Detected | [reviewer_high_03](reports/reviewer_high_03.md) |
| high | REJECT | Detected | [reviewer_high_04](reports/reviewer_high_04.md) |
| xhigh | REJECT | Detected | [reviewer_xhigh_03](reports/reviewer_xhigh_03.md) |
| xhigh | REJECT | Detected | [reviewer_xhigh_04](reports/reviewer_xhigh_04.md) |
| ultra | ACCEPT | Missed | [reviewer_ultra_03](reports/reviewer_ultra_03.md) |
| ultra | REJECT | Detected | [reviewer_ultra_04](reports/reviewer_ultra_04.md) |
| max | REJECT | Detected | [reviewer_max_01](reports/reviewer_max_01.md) |
| max | REJECT | Detected | [reviewer_max_02](reports/reviewer_max_02.md) |
| max | REJECT | Detected | [reviewer_max_03](reports/reviewer_max_03.md) |
| max | REJECT | Detected | [reviewer_max_04](reports/reviewer_max_04.md) |

4 ACCEPT misses, 15 REJECT detections, across 19 report records.

## Review inputs

Each reviewer receives the complete current paper and its available assets, in a fresh context. The original version, modification, tricker report and other reviews are kept outside the review input. Reviewer and checker mathematical assessments are preserved. Filenames identify the producing role.

## Source and authorship

The source has one listed human author, **C. S. Shahbazi**. No AI-collaboration disclosure was found in the supplied source, including its acknowledgments. The artificial proof error is a benchmark modification.

The arXiv record identifies the source license as [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution, the source link and the benchmark changes are recorded in [LICENSE.txt](LICENSE.txt).
