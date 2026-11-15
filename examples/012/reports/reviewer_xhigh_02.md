ACCEPT

I found no substantive mathematical error in the paper's fully presented proofs. The arguments support the stated 89/64 guarantee, the 13/10 guarantee for 4-regular 4-vertex-connected graphs, and the 4/3 guarantee for k-vertex-connected graphs of maximum degree at most k+1. This is an independent mathematical review, not formal verification. The stronger numerical guarantees mentioned as externally formalized results have a specific limitation described below.

## Coverage and method

I read the entire supplied `paper.tex`, lines 1–7270, in bounded, consecutive chunks, including the bibliography, figure specifications and captions, all appendices, the further-improvements section, and the methodology statement. I used only this paper as mathematical input. I did not consult another version, external references, other workspace files, other reports, other agents, or a formal proof assistant. I reviewed the TeX directly rather than separately inspecting the rendered PDF.

I checked the combinatorial constructions, parity and integrality arguments, cut inequalities, local numerical inequalities, and aggregation of costs. I also performed independent finite calculations on the 23-vertex example specified in the paper. Standard cited background results, including the b-factor polytope theorem, subtour support sparsity, the box-constrained optimum reduction, and the standard block reduction, were treated as background inputs; I did not independently inspect their cited sources.

## Main mathematical checks

1. **DFS removable systems.** The proof of Lemma `lem:DFS-removability`, lines 2851–2969, correctly finds two edges of the same star on every cycle. Keeping exactly one edge of each star therefore leaves an acyclic graph with n−1 edges. This establishes simultaneous removability, rather than merely removability of each star in isolation.

2. **The parity polytopes and tour recovery.** The slack-loop reduction in Theorem `thm:bounded-T-join`, lines 1774–1831, correctly accounts for the parity-adjusted degree bounds. Loops contribute twice to degree and never to cuts. The lift and contraction parity calculations used by both LPs are consistent. The reconnection proof, lines 2273–2339, charges at most two for each fully selected star and preserves both connectivity and even degrees. Eliminating loop variables, lines 2363–2399, gives the displayed maximum expression with the correct sign and constant. For DFS systems, its constant is n−1.

3. **Comparison with the MS construction.** The restoration argument, lines 3170–3225, and the mapping of omitted edges into joins, lines 3386–3471, preserve the relevant parity and star restrictions. The separate proof comparing the reconnection LP with optimized MS parity correction, lines 3474–3537, correctly offsets the reconnection charge by the savings on newly removable tree edges. I distinguish this stronger parity comparison for the second LP from the circulation-value comparison proved for the first LP.

4. **The quartic result.** In the proof of Theorem `thm:quartic-thirteen-tenths`, I checked the degree-two suppression/root reduction, the classification of cuts of size at most three, the singleton and triangle repairs, and the correction forest. In particular, the mixed vertex/edge deletion argument in Lemma `lem:quartic-small-cuts`, lines 4431–4476, leaves a connected graph and forces one small shore to have at most three vertices. The forest and independent-set counts in lines 4630–5189 give rho ≤ (n−2)/5. Together with the initial value 5n/4−1/2 and a cost of 1/4 per paid increase, this gives 13n/10−3/5 as claimed.

5. **The k-connected result.** For Theorem `thm:k-connected-four-thirds`, lines 5244–5432, the prescribed values meet the auxiliary degree bounds with equality. A cut with at least two expanded-tree edges has enough complement mass. A cut with exactly one such edge has at least k−1 crossing back edges, including the connector case obtained by deleting its original center. The cost calculation then gives 4n/3−2/3.

6. **Feasibility of the general-graph certificate.** In Lemma `s12pair:connector-completion`, lines 5655–5985, the minimum-cut completion and cut exchange handle simultaneous connector increases. A witness for a connector with value greater than 1/3 has capacity below 2/3, so it contains no other connector. The distinguished violating edge cannot belong to that witness cut, and symmetric difference preserves the violation while reducing the number of crossing connectors. These are the key facts needed to avoid a circular feasibility argument.

7. **The local and global numerical estimates.** I checked the split-cut bounds defining tau in lines 5990–6312, the lift of the half-subtour point and its connector bounds in lines 6320–6445, and both branches of the local-charge proof in lines 6450–6798. The scalar inequality follows from the nonnegative square (t−7)^2. In the consecutive-star case, the remaining charge is at most 1/64, which is at most t_S/64 even when the successor star is not positive. The proof also bounds the sum of chi at a center by its degree excess; it does not incorrectly charge the full excess once per star. Finally, the root excess cancels correctly in lines 6803–6897, leaving 89n/64 + 9(L−n)/8 − 13/16 ≤ 89L/64. The specialization to L=n, lines 6920–7011, is consistent with the main-text formulas.

## Independent check of the separating example

I reconstructed the graph, weights, DFS tree, stars, and retained MS support from lines 2458–2700. The calculations gave:

| Quantity | Independently checked value |
| --- | ---: |
| Displayed subtour-vector cost | 26 |
| Minimum cut under the displayed weights | 2 |
| Number of tight cuts, counting one shore of each cut | 35 |
| Rank of their cut vectors on the 30 edges | 30 |
| Subtour optimum, certified by a nonnegative tight-cut dual combination | 26 |
| StarDeletionLP optimum | 28 |
| StarReconnectionLP optimum | 27 |
| Optimized MS parity value on the specified support and pairing | 29 |
| Minimum MS circulation cost for the specified tree | 1 |

The join calculations enumerated all 256 odd joins using the eight-dimensional cycle space. The dual certificate used only multipliers 1/2 and 1, with every edge covered to total weight exactly one and dual objective 26. Thus the example's feasibility, extremality, optimality, and strict numerical separation agree with the paper. These finite checks support this example; they are not a substitute for the general proofs.

## Minor wording issue; no effect on a claimed bound

**Location:** Main-text discussion following `proc:repair-polytope`, line 756, together with its footnote.

The sentence saying that when the loop is unselected the reconnection cost is “exactly 2 units” is too strong if read as an assertion about the actual reconnection required by every feasible integral point. An unselected loop does not force every star edge to be selected: a join may leave a star edge unselected and still omit the loop. Such a star need not require any reconnection. The quantity 2(1−y_loop) is an upper-bound charge, not always the actual cost. The footnote on that same line states the correct “at most” interpretation, and the detailed proof at lines 2301–2332 uses the correct inequality. This is a harmless wording imprecision, not a substantive mathematical error, and it does not affect the tour bounds.

## Limits concerning the further improvements

The discussion at lines 1339–1376 reports stronger ratios of 14524/10481, 9/7, and 41944/31181 and attributes complete proofs to external Lean material. Appendix `sec:further-improvements` explicitly says at lines 7024–7026 that the proofs and their combined approximation analysis are not presented in full. I did not treat the external-verification claim, authorship, or provenance as evidence of correctness and did not inspect that material.

Within the supplied appendix, the laminar-family counting argument, lines 7182–7226, and the partitionable-center estimate at lines 7228–7232 are mathematically consistent on inspection. The circulation refinement and its final cost bound, lines 7036–7176, are presented as a sketch. I did not obtain an independent full verification of that refinement or of the three stronger numerical ratios from the supplied text alone. Accordingly, this ACCEPT verdict records that no substantive error was found in this review; it should not be read as certification of those externally proved stronger results or as formal verification of the paper.
