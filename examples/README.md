# Example overview

[Project](../README.md) · [Error classification](../protocol/classification.md) · [Evaluation](../evaluation/README.md) · [Case notes](../evaluation/case-notes.md)

**14 examples · 103 review contexts · 71 target misses.** Original-paper bylines comprise **9 human-authored examples and 5 OpenAI-authored examples**.

Reviewer cells show **target misses / total reviews**; a dash means no recorded review at that effort. Baseline reviews are excluded.

| Example | Authorship | Lean | Error type | Area | medium reviewer | high reviewer | xhigh reviewer | max reviewer | ultra reviewer |
|---|---|---|---|---|---:|---:|---:|---:|---:|
| [001](001/README.md) | [OpenAI](001/README.md#source-and-authorship) | [NO](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md#L8249) | [CONV](001/reports/checker_classification.md) | Complex geometry | — | 2 / 2 | 3 / 3 | 3 / 3 | 3 / 3 |
| [002](002/README.md) | [OpenAI](002/README.md#source-and-authorship) | [NO](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md#L8249) | [DEF, CONV](002/reports/checker_classification.md) | Polynomial automorphisms | — | — | 1 / 1 | 2 / 2 | 2 / 2 |
| [003](003/README.md) | [OpenAI](003/README.md#source-and-authorship) | [NO](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md#L1765) | [DEF, CONV](003/reports/checker_classification.md) | Quantum geometric Langlands | — | — | 2 / 2 | 2 / 2 | 2 / 2 |
| [004](004/README.md) | [OpenAI](004/README.md#source-and-authorship) | [NO](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md#L332) | [DEF, CONV](004/reports/checker_classification.md) | Arithmetic geometry | — | — | 1 / 1 | 2 / 2 | 2 / 2 |
| [005](005/README.md) | [Human](005/README.md#source-and-authorship) | NO | [MP](005/reports/checker_classification.md) | Boussinesq PDE | 1 / 1 | — | 0 / 1 | 0 / 1 | 1 / 1 |
| [006](006/README.md) | [Human](006/README.md#source-and-authorship) | NO | [CONV](006/reports/checker_classification.md) | Nonlinear Schrödinger PDE | 1 / 1 | — | 0 / 1 | 0 / 1 | 1 / 1 |
| [007](007/README.md) | [OpenAI](007/README.md#source-and-authorship) | [NO](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md#L1765) | [DEF, CONV](007/reports/checker_classification.md) | Quantum geometric Langlands | 1 / 1 | 0 / 1 | 1 / 1 | 0 / 1 | 1 / 1 |
| [008](008/README.md) | [Human†](008/README.md#source-and-authorship) | NO | [MP, DEF](008/reports/checker_classification.md) | Hypergraph matchings | 1 / 1 | 2 / 2 | 0 / 2 | — | 0 / 2 |
| [009](009/README.md) | [Human](009/README.md#source-and-authorship) | NO | [CONV](009/reports/checker_classification.md) | Differential geometry and supergravity | 3 / 3 | 0 / 4 | 0 / 4 | 0 / 4 | 1 / 4 |
| [010](010/README.md) | [Human](010/README.md#source-and-authorship) | NO | [G2, MP](010/reports/checker_classification.md) | Dynamical systems and discrepancy | 1 / 1 | 2 / 2 | 1 / 2 | 2 / 2 | 0 / 2 |
| [011](011/README.md) | [Human†](011/README.md#source-and-authorship) | [YES](011/original/paper.tex#L547) | [G2, MP](011/reports/checker_classification.md) | Number theory and algebraic geometry | 1 / 1 | 2 / 2 | 2 / 2 | — | 2 / 2 |
| [012](012/README.md) | [Human†](012/README.md#source-and-authorship) | [YES](012/original/paper.tex#L1339) | [G1](012/reports/checker_classification.md) | Graph algorithms and graphic TSP | 1 / 1 | 2 / 2 | 2 / 2 | — | 1 / 2 |
| [013](013/README.md) | [Human†](013/README.md#source-and-authorship) | [YES](013/original/paper.tex#L333) | [G2, MP](013/reports/checker_classification.md) | Optimization and dynamical systems | 1 / 1 | 2 / 2 | 2 / 2 | — | 2 / 2 |
| [014](014/README.md) | [Human†](014/README.md#source-and-authorship) | NO | [G1, DEF](014/reports/checker_classification.md) | Dynamical systems and fractal geometry | 1 / 1 | 1 / 2 | 1 / 2 | — | 1 / 2 |
| **Total** |  |  |  |  | **12 / 12** | **13 / 19** | **16 / 26** | **11 / 18** | **19 / 28** |

**Authorship** follows the original-paper byline; † marks disclosed AI assistance. **Lean** records whether the original paper or its official source repository lists accompanying Lean formalizations (`YES` / `NO`).

A **miss** means the report did not correctly identify the planted error, regardless of its overall verdict. **Identifying the error or explicitly correcting it counts as detection**, including an ACCEPT report that calls it minor or repairable. Authorship links lead to the source attribution and disclosures; example links lead to the error explanation and all reviewer reports. Lean links lead to the original papers' formalization statements or the official manuscript map. The OpenAI cases were also checked against the [upstream Lean formalization catalogue](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/formalization.yaml).

[Example 008](008/README.md#reviews-of-the-modified-paper) has two medium report files from one continued context. Counts use its final supplemented report once, giving 103 contexts from 104 report files. The [case notes](../evaluation/case-notes.md) describe the supplied-reference and reviewer-instruction differences.

## Post-workflow classification review

The error-type links in the main table open each example's `checker_classification.md`. These reports were produced **after the original workflow and case curation by GPT 6 Astra at max effort**, using the recorded [prompt](../protocol/checker-classification-template.txt). Every report audits MP, G1, G2, DEF and CONV, with fully instantiated logical Notes for MP/G, concrete object and computation checks for DEF/CONV, and reasons for negative findings. The table uses the verified direct labels from these reviews; reviewer counts come from the original recorded reviews above.

## Verdict breakdown

Cells use the same **target misses / total reviews** format, grouped by the report's overall verdict. Across all efforts, 68 of 72 ACCEPT reviews, 2 of 30 REJECT reviews and 1 of 1 UNCERTAIN review missed the target.

### By example

| Example | ACCEPT | REJECT | UNCERTAIN | All verdicts |
|---|---:|---:|---:|---:|
| [001](001/README.md#reviews-of-the-modified-paper) | 11 / 11 | — | — | 11 / 11 |
| [002](002/README.md#reviews-of-the-modified-paper) | 5 / 5 | — | — | 5 / 5 |
| [003](003/README.md#reviews-of-the-modified-paper) | 6 / 6 | — | — | 6 / 6 |
| [004](004/README.md#reviews-of-the-modified-paper) | 5 / 5 | — | — | 5 / 5 |
| [005](005/README.md#reviews-of-the-modified-paper) | 2 / 2 | 0 / 2 | — | 2 / 4 |
| [006](006/README.md#reviews-of-the-modified-paper) | 2 / 2 | 0 / 2 | — | 2 / 4 |
| [007](007/README.md#reviews-of-the-modified-paper) | 2 / 2 | 0 / 2 | 1 / 1 | 3 / 5 |
| [008](008/README.md#reviews-of-the-modified-paper) | 3 / 7 | — | — | 3 / 7 |
| [009](009/README.md#reviews-of-the-modified-paper) | 4 / 4 | 0 / 15 | — | 4 / 19 |
| [010](010/README.md#reviews-of-the-modified-paper) | 4 / 4 | 2 / 5 | — | 6 / 9 |
| [011](011/README.md#reviews-of-the-modified-paper) | 7 / 7 | — | — | 7 / 7 |
| [012](012/README.md#reviews-of-the-modified-paper) | 6 / 6 | 0 / 1 | — | 6 / 7 |
| [013](013/README.md#reviews-of-the-modified-paper) | 7 / 7 | — | — | 7 / 7 |
| [014](014/README.md#reviews-of-the-modified-paper) | 4 / 4 | 0 / 3 | — | 4 / 7 |
| **Total** | **68 / 72** | **2 / 30** | **1 / 1** | **71 / 103** |

### By reviewer effort

| Reviewer effort | ACCEPT | REJECT | UNCERTAIN | All verdicts |
|---|---:|---:|---:|---:|
| medium | 11 / 11 | — | 1 / 1 | 12 / 12 |
| high | 13 / 13 | 0 / 6 | — | 13 / 19 |
| xhigh | 16 / 18 | 0 / 8 | — | 16 / 26 |
| max | 9 / 9 | 2 / 9 | — | 11 / 18 |
| ultra | 19 / 21 | 0 / 7 | — | 19 / 28 |
| Total | 68 / 72 | 2 / 30 | 1 / 1 | 71 / 103 |

## Error descriptions

| Example | Planted error |
|---|---|
| [001](001/README.md) | Reversed coordinate composition |
| [002](002/README.md) | Fixed logarithm in residual recursion |
| [003](003/README.md) | Inverted central torsor action |
| [004](004/README.md) | Missing transpose in Koszul duality |
| [005](005/README.md) | Strengthened endpoint time norm |
| [006](006/README.md) | Altered scaling threshold |
| [007](007/README.md) | Copied jet matrices across moving divisors |
| [008](008/README.md) | Prime-power completion loses pair-codegree control |
| [009](009/README.md) | Missing moving-frame derivative in a constraint identity |
| [010](010/README.md) | Retaining a finite-horizon witness after enlarging the horizon |
| [011](011/README.md) | Base-field trace agreement loses extension-field control |
| [012](012/README.md) | Arbitrary demand repair loses degree-two feasibility |
| [013](013/README.md) | A fixed quadrature grid loses parameter dependence |
| [014](014/README.md) | The shortest projective arc loses the signed-cone restriction |
