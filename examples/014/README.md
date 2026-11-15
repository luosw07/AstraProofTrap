# 014: The shortest projective arc loses the signed-cone restriction

**Area:** Dynamical systems and fractal geometry · **Primary label:** G1 (G) · **Secondary label:** DEF

**Source:** Roberto De Leo, [The Levitt–Yoccoz gasket: dynamics, Hausdorff dimension and norm exponent](https://arxiv.org/abs/2611.15996v1), submitted 11 November 2026, 80 pages. **Source group:** `arxiv-2611.15996v1`.

[Modified paper](paper/paper.pdf) · [Original](original/paper.pdf) · [Exact patch](mutation.diff)

## Error and classification

**Location:** the direction-enclosure instruction at [TeX line 2315](paper/paper.tex#L2315), PDF page 37, in “Values at the vertices.” The signed derivative formulas are at lines 2301–2305 and the projective coordinate is at line 2169.

The actual tail vectors satisfy $V_k=V_K+(k-K)U$. The original rule projects the cone spanned by signed representatives in a common open half-plane. The mutation instead takes the shortest projective arc containing the endpoint directions. A signed angle below pi can exceed pi/2; its cone then projects to the longer arc. Identifying opposite directions loses the sign restriction required by the positive-combination argument.

For any $K\ge1$, take $x=(0,1/2,1/2)$, $j=2$ and $w=(4K+3,-4K-4,1)$. The paper's formulas give $U=(-1,0,1)$ and $V_k=(4K+3-k,-4K-4,k+1)$. The endpoints pass the open-half-plane test. Their direction coordinates are $4/9$ and $4/3$, yet the actual run $k=2K+1$ has direction zero, outside the shortest arc. The signed endpoint-angle cosine is $-1/\sqrt{13}$.

After the required transposition, the false arc is $[3,4]\cup[0,5/6]$ while the actual direction is 1. A permitted positive symmetric test function with a peak around 1 can therefore exceed the value bounded over that arc. The exact check includes the actual tail threshold $K=2^{28}+1$.

**G1** identifies extension of a positive-cone inclusion after its signed-representative restriction is lost. **DEF** identifies the prescribed directional enclosure failing its defining containment requirement: an admissible image lies outside the constructed set, and the resulting test-function value hull can omit the actual value. The [post-workflow classification review](reports/checker_classification.md) verifies both obligations. The coordinate formulas and vectors remain correct. Retaining the projected signed cone, or using the whole projective line when needed, repairs the inference.

Run `python3 examples/014/reports/checker_calculation.py`. The linked checker report gives the full admissibility argument.

## Agent reports

[Baseline reviewer (medium)](reports/reviewer_baseline_medium.md) · [Tricker report](reports/tricker_report.md) · [Checker 1](reports/checker_report.md) · [Checker 2](reports/checker_report_02.md) · [Checker 3](reports/checker_report_03.md) · [Classification review (Astra, max)](reports/checker_classification.md)

The classification review is a subsequent **GPT 6 Astra / max** AI-agent review prepared after the original workflow and case curation. It audits all five items—MP, G1, G2, DEF and CONV—with full Notes and supplies the current direct classification.

## Reviews of the modified paper

| Effort / record | Verdict | Target | Reviewer report |
|---|---|---|---|
| medium | ACCEPT | Missed | [reviewer_medium_01](reports/reviewer_medium_01.md) |
| high | ACCEPT | Missed | [reviewer_high_01](reports/reviewer_high_01.md) |
| high | REJECT | Detected | [reviewer_high_02](reports/reviewer_high_02.md) |
| xhigh | ACCEPT | Missed | [reviewer_xhigh_01](reports/reviewer_xhigh_01.md) |
| xhigh | REJECT | Detected | [reviewer_xhigh_02](reports/reviewer_xhigh_02.md) |
| ultra | ACCEPT | Missed | [reviewer_ultra_01](reports/reviewer_ultra_01.md) |
| ultra | REJECT | Detected | [reviewer_ultra_02](reports/reviewer_ultra_02.md) |

4 ACCEPT misses, 3 REJECT detections, across 7 report records.

Reviewers 4104, 4106 and 4108 identify the shortest-arc failure and provide actual-run counterexamples. The other four reports miss this target.

## Review inputs

Each reviewer receives the complete current paper and its available assets, in a fresh context. The original version, modification, tricker report and other reviews are kept outside the review input. Reviewer and checker mathematical assessments are preserved. Filenames identify the producing role.

## Source and authorship

The byline lists **1 human author(s)**. The Tools use statement credits Claude (Anthropic) and ChatGPT (OpenAI) with certificate programs and drafts of parts of the proofs and text. Roberto De Leo retains responsibility for the article. See the [original statement](original/paper.tex#L3707).

The arXiv metadata specifies [CC BY-NC-SA 4.0; the adapted manuscript retains these terms](https://creativecommons.org/licenses/by-nc-sa/4.0/). Attribution and benchmark changes are recorded in [LICENSE.txt](LICENSE.txt). The planted defect is a benchmark modification.
