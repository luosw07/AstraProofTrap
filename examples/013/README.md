# 013: A fixed quadrature grid loses parameter dependence

**Area:** Optimization and dynamical systems · **Primary label:** G2 (G) · **Secondary label:** MP

**Source:** Dmitry Pasechnyuk-Vilensky, Martin Takáč, [Exact (Non-)Accelerations of Heavy-Ball Discretizations](https://arxiv.org/abs/2611.13584v1), submitted 10 November 2026, 63 pages. **Source group:** `arxiv-2611.13584v1`.

[Modified paper](paper/paper.pdf) · [Original](original/paper.pdf) · [Exact patch](mutation.diff)

## Error and classification

**Location:** proof of `lem:spreadwit`, [TeX lines 4332–4336](paper/paper.tex#L4332), PDF page 53. The lost dependency occurs in `lem:spreadhalf`, [line 3573](paper/paper.tex#L3573).

The finite-atom argument chooses a lag cutoff $n_2=\lceil |t|^{-1}\log(8/\eta)\rceil$ before choosing the quadrature resolution. With $t=\log(1-c\varepsilon)$, this cutoff grows without bound. The mutation fixes one midpoint grid before the subsequent construction for each epsilon, then treats its transported wave data as feasible at every lag. Strict minimizer slack alone does not establish those lag constraints.

For the admissible TMM family $\mu=\varepsilon^2$, $L=1$, $\beta=(1-\varepsilon)^2/(1+\varepsilon)$, $h=2-\varepsilon$, $\tau=\beta/h$, set $c=9/8$ and a permitted rational-width band around $2\pi/3$. Any fixed grid of $2J$ cells has common phase period $P=6qJ$. At lag $n=P-1$, cosine phases repeat the lag-one phases while sine phases reverse.

The exact factor identities yield $D_\varepsilon/\varepsilon\to D_*=-\sum_j\nu_{0,j}\xi_j(3-7\xi_j/4)<0$, with $1<\xi_j<12/7$. The positive combination $[\sinh(nt)/\sinh(t)]\ell_1+\upsilon_n$ cancels the value constant and, divided by epsilon, tends to $(n+1)D_*<0$. Thus every fixed resolution fails for sufficiently small positive epsilon, even allowing a different value constant.

**G2** identifies the lost dependence of the existential witness on epsilon. The grid and weights are legitimate objects and use the correct formula; their claimed all-lag feasibility is unsupported and false. Allowing the resolution to depend on epsilon repairs this inference. The checker verifies all tuning and band assumptions. The checker calculation checks the exact first-order polynomial identities, strict sign and common-period formula.

**MP:** the explicit application of `lem:startup` at [line 4335](paper/paper.tex#L4335) requires a finite feasible pair (see [its hypotheses](paper/paper.tex#L3146)). The selected fixed-grid pair violates a lag inequality. Strict minimizer slack, which the paragraph does establish, supplies only part of the antecedent. This failed application is a secondary label alongside the G2 witness-dependence error.

Run `python3 examples/013/reports/checker_calculation.py`. The linked checker report gives the full admissibility argument.

## Agent reports

[Baseline reviewer (medium)](reports/reviewer_baseline_medium.md) · [Tricker report](reports/tricker_report.md) · [Checker 1](reports/checker_report.md) · [Classification review (Astra, max)](reports/checker_classification.md)

The classification review is a subsequent **GPT 6 Astra / max** AI-agent review prepared after the original workflow and case curation. It audits all five items—MP, G1, G2, DEF and CONV—with full Notes and supplies the current direct classification.

## Reviews of the modified paper

| Effort / record | Verdict | Target | Reviewer report |
|---|---|---|---|
| medium | ACCEPT | Missed | [reviewer_medium_01](reports/reviewer_medium_01.md) |
| high | ACCEPT | Missed | [reviewer_high_01](reports/reviewer_high_01.md) |
| high | ACCEPT | Missed | [reviewer_high_02](reports/reviewer_high_02.md) |
| xhigh | ACCEPT | Missed | [reviewer_xhigh_01](reports/reviewer_xhigh_01.md) |
| xhigh | ACCEPT | Missed | [reviewer_xhigh_02](reports/reviewer_xhigh_02.md) |
| ultra | ACCEPT | Missed | [reviewer_ultra_01](reports/reviewer_ultra_01.md) |
| ultra | ACCEPT | Missed | [reviewer_ultra_02](reports/reviewer_ultra_02.md) |

7 ACCEPT misses, across 7 report records.

All seven reports miss the fixed grid’s lost epsilon dependence. Reviewer 3012’s correction concerns a separate QHM degenerate case.

## Review inputs

Each reviewer receives the complete current paper and its available assets, in a fresh context. The original version, modification, tricker report and other reviews are kept outside the review input. Reviewer and checker mathematical assessments are preserved. Filenames identify the producing role.

## Source and authorship

The byline lists **2 human author(s)**. The Use of AI tools statement credits Claude Opus 5.5 and ChatGPT-6.1 Sol with exposition, formal proof verification and literature checks; the human authors state that they verified the results. See the [original statement](original/paper.tex#L2123).

The arXiv metadata specifies [arXiv non-exclusive distribution license; original rights remain with the authors](https://arxiv.org/licenses/nonexclusive-distrib/1.0/). Attribution and benchmark changes are recorded in [LICENSE.txt](LICENSE.txt). The planted defect is a benchmark modification.
