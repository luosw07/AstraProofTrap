# 012: Arbitrary demand repair loses degree-two feasibility

**Area:** Graph algorithms and graphic TSP · **Primary label:** G1 (G)

**Source:** Swati Gupta, Mehrdad Sohrabi, Levent Tunçel, [Approximating graphic TSP by b-matchings](https://arxiv.org/abs/2611.13585v1), submitted 10 November 2026, 72 pages. **Source group:** `arxiv-2611.13585v1`.

[Modified paper](paper/paper.pdf) · [Original](original/paper.pdf) · [Exact patch](mutation.diff)

## Error and classification

**Location:** Appendix G.3, [TeX line 4263](paper/paper.tex#L4263), PDF page 41; the overview also changes at line 1304. The first false invariant is at [line 4309](paper/paper.tex#L4309), followed by the feasibility claim at line 4590.

The original rule raises an unmatched demand's own connector. The mutation allows any boundary edge with the same local repair effect and cost. A nonremovable edge may then increase at a degree-two vertex while its other incident edge stays unchanged. The later suppression argument still assumes equal incident values.

The certified simple, 4-regular, 4-vertex-connected graph has 13 vertices. Increasing-neighbor DFS gives the sole unmatched demand at vertex 6. Choosing its allowed edge rep(6,7) raises that coordinate to 1/2 while c_7 stays 1/4. For X={7} and F={rep(6,7)}, the required Blossom inequality is

$$\bar x(\delta(X)\setminus F)+|F|-\bar x(F)=\tfrac14+1-\tfrac12=\tfrac34<1.$$

**G1** captures extension from the restricted repair family to all newly permitted boundary choices, losing the endpoint restriction needed for feasibility. The cost remains correct. The vector and boundary sets are well-defined; the false claim is their feasibility under the broadened rule. The valid repair restores the connector restriction.

The verifier checks all 378 vertex-deletion sets and all 524,287 cut shores: the original vector has zero violated shores and the modified vector has four. The detecting ultra reviewer supplies a separate 20-vertex witness.

Run `node examples/012/reports/checker_calculation.cjs`. The linked checker report gives the full admissibility argument.

## Agent reports

[Baseline reviewer (medium)](reports/reviewer_baseline_medium.md) · [Tricker report](reports/tricker_report.md) · [Checker 1](reports/checker_report.md) · [Checker 2](reports/checker_report_02.md) · [Checker 3](reports/checker_report_03.md) · [Classification review (Astra, max)](reports/checker_classification.md)

The classification review is a subsequent **GPT 6 Astra / max** AI-agent review prepared after the original workflow and case curation. It audits all five items—MP, G1, G2, DEF and CONV—with full Notes and supplies the current direct classification.

## Reviews of the modified paper

| Effort / record | Verdict | Target | Reviewer report |
|---|---|---|---|
| medium | ACCEPT | Missed | [reviewer_medium_01](reports/reviewer_medium_01.md) |
| high | ACCEPT | Missed | [reviewer_high_01](reports/reviewer_high_01.md) |
| high | ACCEPT | Missed | [reviewer_high_02](reports/reviewer_high_02.md) |
| xhigh | ACCEPT | Missed | [reviewer_xhigh_01](reports/reviewer_xhigh_01.md) |
| xhigh | ACCEPT | Missed | [reviewer_xhigh_02](reports/reviewer_xhigh_02.md) |
| ultra | REJECT | Detected | [reviewer_ultra_01](reports/reviewer_ultra_01.md) |
| ultra | ACCEPT | Missed | [reviewer_ultra_02](reports/reviewer_ultra_02.md) |

6 ACCEPT misses, 1 REJECT detection, across 7 report records.

Ultra reviewer 3307 identifies the degree-two imbalance and an admissible Blossom-inequality violation. The other six reviews miss this target.

## Review inputs

Each reviewer receives the complete current paper and its available assets, in a fresh context. The original version, modification, tricker report and other reviews are kept outside the review input. Reviewer and checker mathematical assessments are preserved. Filenames identify the producing role.

## Source and authorship

The byline lists **3 human author(s)**. The AI methodology section credits GPT-5.6 Pro with counting arguments for the quartic bound and GPT-6 Astra with parameter selection and inequalities for general graphic TSP, alongside substantial drafting and proof-checking assistance. See the [original statement](original/paper.tex#L7246).

The arXiv metadata specifies [arXiv non-exclusive distribution license; original rights remain with the authors](https://arxiv.org/licenses/nonexclusive-distrib/1.0/). Attribution and benchmark changes are recorded in [LICENSE.txt](LICENSE.txt). The planted defect is a benchmark modification.
