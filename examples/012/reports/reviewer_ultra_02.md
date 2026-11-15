ACCEPT

I found no substantive mathematical error in the arguments reviewed. In particular, the paper's fully presented proofs support the claimed 89/64 bound for general graphic TSP, the 13/10 bound for simple 4-regular 4-vertex-connected graphs, and the 4/3 bound for simple k-vertex-connected graphs with maximum degree at most k+1. This is an independent mathematical review, not formal verification or a confirmation of the external formalizations mentioned in the paper.

## Scope and method

I read the complete supplied `paper.tex`, lines 1–7270, in bounded chunks, including all appendices, the bibliography, the numerical example, and the final discussion of further improvements. I inspected the mathematical content of the TeX figures as well as the prose and displayed formulas. I did not consult another version, external mathematical sources, other workspace documents, other reviewers, or a proof assistant. I did not separately inspect the rendered PDF. Standard matching, flow, and laminar-cut results cited by the paper were assessed as mathematical prerequisites; I did not audit the cited publications or their bibliographic details.

The main review concentrated on the actual deductions: the auxiliary-graph parity formulations, the two tour-recovery bounds, the DFS star system, the circulation comparisons, the quartic correction procedure, and the general-graph certificate. I also performed finite calculations on the explicitly supplied 23-vertex example. The supplementary stronger ratios advertised as externally formalized have a separate limitation noted below.

## Findings on the main arguments

### Degree bounds, parity, and tour recovery

Theorem `thm:bounded-T-join`, lines 1774–1830, has a sound reduction to the b-factor description stated in Theorem `thm:b-factor`. Rounding the degree bound to the required parity is essential and is handled by beta. The added slack loops provide exactly the missing even degree; the singleton blossom inequality supplies the necessary lower bound when the demanded parity is odd. Loops do not alter any cut inequality. Consequently the projection and integrality conclusions used later are justified.

The projected parity argument for the StarDeletionLP, lines 2057–2109, is valid. For the StarReconnectionLP, lines 2273–2338, a fully selected star forces its loop to be absent, giving the stated upper bound on saturation probability. Restoring two copies of one edge in every fully selected star preserves parity and leaves at least one edge per star, which is sufficient for connectivity. Optimizing the loops independently, lines 2376–2399, gives exactly the stated maximum-of-two-terms objective. In particular, the nonlinear projected objective is justified through the integral linear formulation; its minimization is not incorrectly justified merely by integrality of the projection.

The introductory matroid-join identity at lines 501–506 is also consistent: deleting a cographically independent subset of doubled join edges preserves connectivity and parity, and an optimal graphic tour can be taken to have edge multiplicities at most two, yielding the converse representation.

### DFS removability and circulation comparisons

The cycle argument in Lemma `lem:DFS-removability`, lines 2851–2969, is valid. Choosing a back edge whose upper endpoint has minimum depth forces the second crossing of the indicated subtree cut to lie in the same star. Keeping one edge per star therefore gives an acyclic graph with n−1 edges, proving the spanning-tree conclusion.

The support restoration and lifting arguments, lines 3170–3471, preserve the required parities and star constraints. The root restoration's accounting is consistent with the additional root back edge when one is needed. In Lemma `lem:reconnection-MS-parity`, lines 3474–3537, every fully selected star is charged to a distinct unpaired selected tree edge, and the two-unit saving from changing that edge's treatment pays its reconnection charge. The comparison statements distinguish the optimized circulation estimate from the optimized parity correction in the way required by their proofs.

### Highly connected graph bounds

For the quartic analysis, I checked the reduction to Q, the classification of cuts of size at most three, the singleton and triangle repairs, and the correction count. In Lemma `lem:quartic-small-cuts`, lines 4431–4475, deleting the centers of crossing connectors and the remaining crossing edges leaves a connected graph by 4-vertex-connectivity. This bounds the smaller surviving cut shore by three vertices. Simplicity and minimum degree three then give exactly the singleton/triangle possibilities claimed.

The three cases in Lemma `lem:quartic-repair-forest`, lines 4639–4921, exhaust the possible shared demand boundaries and give at most one predecessor. The subsequent independent-set estimate and the two disjoint counting arguments, lines 4997–5188, establish the paid-increase budget (n−2)/5. Combining this with the initial cost 5n/4−1/2 gives 13n/10−3/5 as stated.

For Theorem `thm:k-connected-four-thirds`, lines 5244–5432, the assigned coordinates satisfy the auxiliary degree bounds exactly. The blossom verification correctly reduces to a singleton complement. If only one expanded-tree edge crosses, the required k−1 back edges follow respectively from edge-connectivity of G or of G−u. The resulting objective calculation gives 4n/3−2/3.

### General-graph certificate and constant

I checked Lemma `s12pair:connector-completion`, lines 5655–5985, especially the simultaneous connector assignment. The potentially delicate cut-exchange step is valid: a minimum cut witnessing an increased connector has capacity below 2/3, so it contains no other connector under the initial capacities. The distinguished violating edge cannot belong to that witness cut. Symmetric difference then preserves the violation while strictly decreasing the number of crossing connectors, yielding the required contradiction.

The connector estimate in Lemma `s12pair:connector-estimate`, lines 6000–6302, covers cuts with both original shores nonempty and the two singleton cases. Its use of the two subtour inequalities and the local degree surplus is correct. The lift of the half-subtour point and both local connector estimates, lines 6320–6445, have the appropriate parity conditions.

The scalar inequality in Lemma `s11p:scalar`, lines 6450–6486, follows from greedy DFS and the cap on the increase; the square (t−7)^2 in its proof has the correct coefficient. I checked both branches of Lemma `s12pair:local-charge`, lines 6542–6798, including the predecessor-star charge, the degree identity at a one-child center, and the bound on the sum of chi at one center. The successor need not be positive, but t_S≥1 is sufficient for the step at lines 6697–6705.

Finally, the aggregation at lines 6803–6897 correctly partitions E outside the root star, applies the support-size bound, and cancels the root surplus. It gives

`Phi(Y) <= (89/64)n + (9/8)(L−n) − 13/16 <= (89/64)L`.

The L=n specialization, lines 6920–7011, is consistent with the main-body construction and with the root star's contribution. The initial use of a box-constrained optimum on the same support and the reduction through blocks are cited prerequisites; I found no contradiction in their subsequent use.

## Independent check of the numerical separation example

I reconstructed the 30 edges, five stars, edge weights, and displayed MS support directly from lines 2463–2470 and 2551–2699.

- Enumerating all 2^22−1 nontrivial cuts with one vertex fixed outside the shore gives minimum x-cut weight 2 and 35 tight cuts. The proposed point is feasible and has objective 26.
- The tight-cut matrix has rank 30 modulo the prime 1,000,003, which certifies rank 30 over the rationals. Together with positivity, this certifies extremality.
- I found nonnegative half-integral weights on tight cuts whose edge coverage is exactly one. Their dual objective is exactly 26, independently certifying optimality.
- Enumerating all 256 odd(G)-joins through the eight-dimensional cycle space gives StarDeletionLP optimum 28 and StarReconnectionLP optimum 27.
- On the displayed 27-edge MS support, enumerating its 32 odd joins with the three specified pair restrictions gives optimized length 29.

The displayed circulation cost 1 is also consistent: the back edges from the degree-two leaves 16 and 20 are forced to carry at least one unit, both entering the same star at 0, so zero cost is impossible; the displayed circulation attains cost one.

## Minor wording issue, without an effect on the conclusions

**Location:** lines 754–756, the sentence asserting that when the loop is unselected the reconnection cost is “exactly 2 units.”

An unselected loop does not by itself imply that its star is fully selected. Thus the actual reconnection cost can be zero even though the objective charges two. For example, in a triangle with its two-edge DFS root star, select only the root connector and no loop. This is a feasible integral odd(H)-join; its projection selects no original edge, and the original triangle already needs no reconnection.

The correct general wording is that two units are charged, or that the required reconnection cost is at most two. The accompanying footnote already says this, and the formal proof uses the correct inequality at lines 2307–2312. This is a harmless explanatory overstatement, not a substantive defect in a theorem or bound.

## Limitations concerning the supplementary improvements

The discussion at lines 1338–1362 advertises stronger ratios, including 14524/10481, 9/7, and 41944/31181, as results of external formalizations. Appendix `sec:further-improvements`, lines 7017–7235, explicitly supplies constructions and estimates without their complete proofs or the combined analysis producing those ratios. I did not inspect external formalizations, and I did not treat the assertions of verification as evidence of correctness.

I checked the supplied laminar-count argument and the partitionable-center estimate in that appendix; they are consistent. I have not independently established the full supplementary circulation assertion and its global combination into the three stronger numerical ratios. Those supplementary claims are therefore outside what this report independently confirms. Their acknowledged abbreviated presentation does not supply a counterexample to, or a failure in, the fully presented main proofs reviewed above.

The verdict means no substantive mathematical error was found in this review. It does not claim exhaustive verification of every unstated prerequisite or of results whose full proofs are outside the supplied paper.
