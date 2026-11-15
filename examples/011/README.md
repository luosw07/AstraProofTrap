# 011: Base-field trace agreement loses extension-field control

**Area:** Number theory and algebraic geometry · **Primary label:** G (G2) · **Secondary label:** MP

**Source:** Dante Bonolis, Tim Browning, Jakob Glas and Victor Y. Wang, [The Artin-Davenport conjecture on cubic forms](https://arxiv.org/abs/2610.08226v2), 14 October 2026, 66 pages. **Source group:** `arxiv-2610.08226v2`.

[Modified paper](paper/paper.pdf) · [Original](original/paper.pdf) · [Exact patch](mutation.diff)

## Error and classification

**Location:** Proposition 9.5, printed pages 37–38; the selection paragraph at source lines 4340–4345 and the subsequent use of Lemma 9.1 at line 4386.

The modified proof selects any uniformly bounded-rank mixed-lisse realization agreeing with the exponential sum on base-field points. It then reuses the notation for that realization's traces over every finite extension and applies a second-moment estimate proved for the canonical exponential sums. Agreement at degree one supplies no agreement at higher extension degrees.

Let K be the canonical complex on a smooth dense open U in a rational (n−2)-plane. Add a geometrically constant rank-two sheaf with Frobenius eigenvalues p^(n−1) and −p^(n−1), in even cohomological degree 2n−2. It contributes zero on every base-field point and 2q^(n−1) on every even extension, q=p^a. The new realization retains mixed lissity, uniform rank, integer weights and the recorded weight envelope. Its second moment is at least q^(3n−4)/2 for sufficiently large even a, by reverse triangle and the canonical moment bound. The canonical bound is only O(q^(2n−3)). After normalization by q^(2n−2), the new moment grows at least as q^(n−2)/2.

The degree-one cone has r=d=1. Xu's moment dichotomy applies to the selected realization, but its large-moment alternative cannot be eliminated by Lemma 9.1. The repair is to select the canonical realization or require trace agreement over every finite extension. G2 identifies the unsupported sufficiency of the selected witness; MP identifies the later misapplication of Lemma 9.1 to traces outside its proved scope. This directly violates the theorem-application obligation, alongside the G2 failure of witness sufficiency. The conditional construction works for every canonical object under the proof's standing contradiction assumptions; the checker separately verifies its geometric and sheaf-theoretic admissibility.

The original theorem's statement and the original source are retained. This benchmark introduces the proof defect.

Run `python3 examples/011/reports/checker_calculation.py` from the repository root. It checks the zero degree-one trace, nonzero even-extension trace, preserved weight/degree, and exact moment-exponent and reverse-triangle calculations. The full existence, admissibility and infinite-extension arguments are in the [checker report](reports/checker_report.md).

## Agent reports

[Baseline reviewer (medium)](reports/reviewer_baseline_medium.md) · [Tricker report](reports/tricker_report.md) · [Checker 1](reports/checker_report.md) · [Classification review (Astra, max)](reports/checker_classification.md)

The classification review is a subsequent **GPT 6 Astra / max** AI-agent review prepared after the original workflow and case curation. It audits all five items—MP, G1, G2, DEF and CONV—with full Notes and supplies the current direct classification.

## Reviews of the modified paper

| Effort / record | Verdict | Target | Reviewer report |
|---|---|---|---|
| medium | ACCEPT | Missed | [reviewer_medium_01](reports/reviewer_medium_01.md) |
| high 1 | ACCEPT | Missed | [reviewer_high_01](reports/reviewer_high_01.md) |
| high 2 | ACCEPT | Missed | [reviewer_high_02](reports/reviewer_high_02.md) |
| xhigh 1 | ACCEPT | Missed | [reviewer_xhigh_01](reports/reviewer_xhigh_01.md) |
| xhigh 2 | ACCEPT | Missed | [reviewer_xhigh_02](reports/reviewer_xhigh_02.md) |
| ultra 1 | ACCEPT | Missed | [reviewer_ultra_01](reports/reviewer_ultra_01.md) |
| ultra 2 | ACCEPT | Missed | [reviewer_ultra_02](reports/reviewer_ultra_02.md) |

7 ACCEPT misses, across 7 report records.

All seven reports endorse the moment-transfer argument without diagnosing the degree-one-only trace agreement or requiring agreement over every extension. Their comments at other locations do not identify this target.

## Review inputs

The baseline, medium review and six repetitions receive the complete current paper and the same [five public references](paper/references/README.md): Bei16, FK01, HY18, RS22 and Xu20. The medium review finishes in one continued context. The original version, modification, tricker report and other reviews are kept outside the review input. Reviewer and checker mathematical assessments are preserved. Filenames identify the producing role.

## Source and authorship

The source is **human-authored with disclosed substantive AI assistance**. Its four listed authors attribute the proof structure and most new ideas to their own work. The [AI statement](original/paper.tex#L559) credits ChatGPT 6.0 with the improved incidence-dimension bound and a rational Hilbert–Mumford approach, and several OpenAI models with estimates, proofreading and Lean auto-formalization. That formalization was not used in this benchmark workflow.

The arXiv source uses [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); attribution and modification notice are in [source terms](LICENSE.txt). The five supporting papers and their exact versions are listed in [reference provenance](paper/references/README.md).
