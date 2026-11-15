# 008: Prime-power completion loses pair-codegree control

**Area:** Combinatorics and random hypergraph matchings · **Primary label:** MP · **Secondary label:** DEF

**Source:** Hyunwoo Lee, [Matching statistics in regular hypergraphs and applications](https://arxiv.org/abs/2611.17197v1), submitted 12 November 2026, 67 pages. **Source group:** `arxiv-2611.17197v1`.

[Modified paper](paper/paper.pdf) · [Original](original/paper.pdf) · [Exact patch](mutation.diff)

## Error and classification

**Location:** printed page 30, proof of Theorem 4.1, validity of the completed stages; source line 1866. The invoked construction is Lemma 4.2 on page 21, and the failed completed-codegree assertion is (4.10).

The modified invocation selects the least prime power at least max{D_(i+1), k−1}, while the lemma's displayed construction uses a prime field and integer multipliers j = 0,...,k−2. In characteristic two with k = 4, the coordinates indexed by 0 and 2 coincide as field scalars. For fixed b, all D slopes a give auxiliary edges containing {(0,b),(2,b)}, so this pair has codegree D instead of at most one.

The checker supplies an admissible asymptotic family that reaches a power-of-two target degree at an actual completion stage. Positive deficits force the faulty auxiliary edges. The resulting pair codegree has order n while the stage budget is O((log n)^4); the next random-greedy application loses a required hypothesis. MP identifies the unsupported application of Lemma 4.2. DEF identifies the failure of the prescribed completion to meet its claimed codegree specification. The original source is unmodified in `original/`; this error was introduced for the benchmark.

Run `python3 examples/008/reports/checker_calculation.py` from the repository root. This finite-field calculation demonstrates the characteristic-two collision and checks the corresponding prime-field construction. The full admissible stage witness and downstream failure are in the checker report.

## Agent reports

[Baseline reviewer (medium)](reports/reviewer_baseline_medium.md) · [Tricker report](reports/tricker_report.md) · [Checker 1](reports/checker_report.md) · [Classification review (Astra, max)](reports/checker_classification.md)

The classification review is a subsequent **GPT 6 Astra / max** AI-agent review prepared after the original workflow and case curation. It audits all five items—MP, G1, G2, DEF and CONV—with full Notes and supplies the current direct classification.

## Reviews of the modified paper

| Effort / record | Verdict | Target | Reviewer report |
|---|---|---|---|
| medium initial | UNCERTAIN | Missed | [reviewer_medium_01](reports/reviewer_medium_01.md) |
| medium supplemented | ACCEPT | Missed | [reviewer_medium_02](reports/reviewer_medium_02.md) |
| high 1 | ACCEPT | Missed | [reviewer_high_01](reports/reviewer_high_01.md) |
| high 2 | ACCEPT | Missed | [reviewer_high_02](reports/reviewer_high_02.md) |
| xhigh 1 | ACCEPT | Detected | [reviewer_xhigh_01](reports/reviewer_xhigh_01.md) |
| xhigh 2 | ACCEPT | Detected | [reviewer_xhigh_02](reports/reviewer_xhigh_02.md) |
| ultra 1 | ACCEPT | Detected | [reviewer_ultra_01](reports/reviewer_ultra_01.md) |
| ultra 2 | ACCEPT | Detected | [reviewer_ultra_02](reports/reviewer_ultra_02.md) |

1 UNCERTAIN miss, 3 ACCEPT misses, 4 ACCEPT detections, across 8 report records from seven contexts.

The two medium records are one reviewer context, before and after supplying the complete cited Bennett–Bohman paper. High and higher repetitions each use a fresh context with that same public reference. The four ACCEPT detections explicitly identify the target, even though the reports describe its repair as local.

## Review inputs

The complete current paper is supplied as PDF and extracted text. The supplemented medium review and all six higher-effort reviews also receive the full [Bennett–Bohman reference](paper/references/README.md). The original version, modification, tricker report and other reviews are kept outside the review input. Reviewer and checker mathematical assessments are preserved. Filenames identify the producing role.

## Source and authorship

The paper is a **human–AI collaboration**, with Hyunwoo Lee as its sole listed author. The disclosure on page 58 assigns the questions, main results and overall strategy to the human author and describes substantial AI proof contributions, including Section 4's technical calculations. The author states that the mathematical results were independently verified and takes responsibility. This benchmark's planted error is separate from that source authorship.

The arXiv record links the source to the arXiv non-exclusive distribution license; see [source terms](LICENSE.txt). The complete public supporting reference is Patrick Bennett and Tom Bohman, [A natural barrier in random greedy hypergraph matching](https://arxiv.org/abs/1210.3581v2), 12 pages; its provenance is recorded in `paper/references/README.md`. Original rights remain with their holders.
