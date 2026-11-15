# 010: Retaining a finite-horizon witness after enlarging the horizon

**Area:** Dynamical systems, discrepancy and election methods · **Primary label:** G2 (G) · **Secondary label:** MP

**Source:** Jean-Pierre Conze, Svante Janson and Anders Öberg, [Frege's election method: discrepancy, invariant polygons and Farey geometry](https://arxiv.org/abs/2611.13996v1), submitted 10 November 2026, 96 pages. **Source group:** `arxiv-2611.13996v1`.

[Modified paper](paper/paper.pdf) · [Original](original/paper.pdf) · [Exact patch](mutation.diff)

## Error and classification

**Location:** proof of Theorem 7.12 (`TB`), PDF pages 40–41; TeX lines [4218–4220](paper/paper.tex#L4218) select the block, [4232–4233](paper/paper.tex#L4232) enlarge the horizon, and [4257–4258](paper/paper.tex#L4257) reuse its earlier guarantee.

The original proof chooses a block B with widths jointly rationally independent of the vote coordinates. Lemma 7.11 then guarantees that **every iterate** of this one B is a finite union of good blocks. A later finite covering horizon may depend on B.

The mutation instead chooses **any** block whose iterates are good only through an initial horizon N0. It then increases the horizon to M(B), keeping B fixed, and asserts goodness through M(B) by the original choice. Existence of a witness satisfying F(B,N0), followed by existence of a covering horizon M(B), does not supply F(B,M(B)) for that witness.

**G2** identifies the unsupported property used after an existential witness is selected. **MP** identifies the final application of the selected finite certificate: its implication requires $n\le N_0$, while the proof establishes only $n\le M(B)$. The initial existence claim and the later cover are each valid; their required compatibility fails. The [post-workflow classification review](reports/checker_classification.md) verifies both obligations. The tricker report traces the dependencies through Theorem 7.5, Lemma 7.11, the two covers in Theorem 7.12 and the two-party dynamics.

For an explicit admissible example, let $\epsilon=\sqrt2/1000$, $p_1=1/4+\epsilon$, $p_2=3/4-\epsilon$, $N_0=1$ and $B=[-2\epsilon,2\epsilon]$. In the paper's two-party multivalued map,

$$
TB=[1/4-\epsilon,1/4+3\epsilon],\qquad
T^2B=[-1/2,-1/2+4\epsilon]\cup\{1/2\}.
$$

B and TB are good blocks, but the isolated point in the second image prevents it from being a finite union of nondegenerate intervals. Every cover by translates of the projected interior of B needs M at least 176, since $176(4\epsilon)<1$. Thus every later covering horizon includes the bad second iterate. Restoring the original all-iterate witness selection repairs this proof step.

Run `python3 examples/010/reports/checker_calculation.py`. Exact arithmetic in $\mathbb Q(\sqrt2)$ reproduces both images, preserves both branches at a tie, identifies the isolated point and verifies the necessary covering lower bound. The checker supplies the full admissibility and downstream argument.

## Agent reports

[Baseline reviewer (medium)](reports/reviewer_baseline_medium.md) · [Tricker report](reports/tricker_report.md) · [Checker 1](reports/checker_report.md) · [Classification review (Astra, max)](reports/checker_classification.md)

The classification review is a subsequent **GPT 6 Astra / max** AI-agent review prepared after the original workflow and case curation. It audits all five items—MP, G1, G2, DEF and CONV—with full Notes and supplies the current direct classification.

## Reviews of the modified paper

| Effort / record | Verdict | Target | Reviewer report |
|---|---|---|---|
| medium | ACCEPT | Missed | [reviewer_medium_01](reports/reviewer_medium_01.md) |
| high-1 | ACCEPT | Missed | [reviewer_high_01](reports/reviewer_high_01.md) |
| high-2 | ACCEPT | Missed | [reviewer_high_02](reports/reviewer_high_02.md) |
| xhigh-1 | ACCEPT | Missed | [reviewer_xhigh_01](reports/reviewer_xhigh_01.md) |
| xhigh-2 | REJECT | Detected | [reviewer_xhigh_02](reports/reviewer_xhigh_02.md) |
| ultra-1 | REJECT | Detected | [reviewer_ultra_01](reports/reviewer_ultra_01.md) |
| ultra-2 | REJECT | Detected | [reviewer_ultra_02](reports/reviewer_ultra_02.md) |
| max-1 | REJECT | Missed | [reviewer_max_01](reports/reviewer_max_01.md) |
| max-2 | REJECT | Missed | [reviewer_max_02](reports/reviewer_max_02.md) |

4 ACCEPT misses, 3 REJECT detections, 2 REJECT misses, across 9 report records.

High-2, xhigh-2, ultra-1, ultra-2, max-1 and max-2 use the explicit instruction to assess the proof as printed, without adding arguments, strengthening assumptions or providing a repaired proof. The medium, high-1 and xhigh-1 reports use the original review instruction. Each row is a fresh context. The two max rejections concern other errors and miss the target in Theorem 7.12.

## Review inputs

Each reviewer receives the complete current paper and its available assets, in a fresh context. The original version, modification, tricker report and other reviews are kept outside the review input. Reviewer and checker mathematical assessments are preserved. Filenames identify the producing role.

## Source and authorship

The source lists three human authors: **Jean-Pierre Conze, Svante Janson and Anders Öberg**. No AI-collaboration disclosure was found in the supplied source, including its acknowledgments. This adds one human-authored case and one distinct source paper. The synthetic error is a benchmark modification.

The arXiv record identifies [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) as the source license. See [LICENSE.txt](LICENSE.txt) for attribution and changes.
