ACCEPT

I found no substantive mathematical error in the arguments I reviewed. In particular, the included proofs of the main bounds—89/64 for general graphic TSP, 13/10 for simple 4-regular 4-vertex-connected graphs, and 4/3 for simple k-vertex-connected graphs with maximum degree at most k+1—are internally consistent. This is a mathematical review, not formal verification.

## Input and coverage

The sole mathematical input was the supplied standalone `paper.tex`, lines 1–7270, in `run_20261114/blind/q7m2v8`. I read the entire source in consecutive bounded chunks, including the introductory claims, all main sections, the bibliography, every appendix, figure definitions and captions, the further-improvements section, and the methodology statement. I did not search for another version, read other workspace material or agent reports, consult the linked formalization, use a proof assistant, or delegate the review. I used elementary calculations and small independent programs to check the supplied comparison example. I did not separately compare the rendered PDF against the TeX.

The most detailed scrutiny was of the polyhedral formulations, their tour recovery, the DFS star construction, both highly connected graph proofs, and the full general-subtour-value proof. I also examined the mathematical content of the supplementary refinements. Limitations concerning the latter and externally cited results are stated below.

## Findings

### No substantive error found in the principal arguments

1. **Degree-bounded joins and the two LPs.** The degree-bounded T-join theorem (`thm:bounded-T-join`, lines 1774–1831) uses an appropriate parity-adjusted degree bound. The slack-loop reduction works: the singleton blossom inequalities provide the lower degree needed at odd-demand vertices, the added loops supply the remaining even degree, and the blossom parity condition is unchanged. The degree bounds at star auxiliary vertices in both formulations have the required parity. The parity projection and connectivity arguments for the deletion LP (lines 2057–2110) and reconnection LP (lines 2273–2339) correctly give tours. In particular, repairing each fully selected star with two copies of one of its edges both preserves even degrees and restores the removable-system connectivity condition.

   The elimination of loop variables in `eq:repair-nonloop-cost` (lines 2363–2399) is algebraically correct. The resulting convex, piecewise-linear objective is not being rounded by an unsupported claim about minimizing a convex function over an integral polytope: it is the projection of the stated *linear* optimization problem over the integral lifted polytope. This distinction makes the fractional certificates legitimate.

2. **DFS removable stars.** The cycle argument in `lem:DFS-removability` (lines 2851–2969) is valid. Choosing a cycle back edge with shallowest upper endpoint forces another edge of that cycle to belong to the same star. Thus a selection keeping exactly one edge per star is acyclic; the edge count then makes it a spanning tree. This establishes the simultaneous-deletion property, not merely separate removability of each star.

3. **Comparison with circulation methods.** I checked the support-restoration accounting (lines 3195–3225), join lifting (lines 3292–3320), and the two distinct comparison arguments (lines 3386–3471 and 3488–3537). The distinction is important: the deletion LP is bounded by the optimized circulation *estimate*, while the reconnection LP also dominates optimized MS parity correction. In the latter argument, every fully selected star is charged to a distinct selected tree edge in the set U; changing such an edge from an MS nonremovable edge to a removable edge saves the two units needed for its possible reconnection. The displayed inequalities follow.

4. **The quartic bound.** I checked `thm:quartic-thirteen-tenths` and its proof, lines 3630–5213. The degree-two suppression is consistent with the correction procedure: neither incident value at a suppressed vertex is changed from 1/4. After suppression and deletion of the root leaf, the graph is the original graph with only the size-two stars split. The mixed vertex-and-edge deletion argument in `lem:quartic-small-cuts` (lines 4431–4476) correctly uses 4-vertex-connectivity to restrict cuts of size at most three to the listed singletons and triangles. The triangle classification and the subsequent repairs cover those cuts; cuts of size at least four have sufficient contribution regardless of the blossom sign choices.

   I also checked the correction-forest cases and the counting argument, including the disjointness of the vertex sets A1, A2, and A3. The inequalities

   `5 alpha(K) <= 3|U| + 4|D| + 2c_U + c_D <= n-2`

   follow from the stated predecessor/successor restrictions and the DFS counts. The resulting paid increase of at most `(n-2)/20` gives exactly `13n/10 - 3/5`.

5. **The bounded-degree, highly connected bound.** The proof of `thm:k-connected-four-thirds` (lines 5244–5432) checks out. For a cut crossed by a single expanded-tree edge, a representative tree edge is handled by k-edge-connectivity of G, and a connector is handled by (k-1)-edge-connectivity of G-u. Both shores of the latter cut are nonempty because the connector is nonroot. The lower bound on the complements of back-edge coordinates then supplies 4/3 in the required cut calculation. The auxiliary degree equalities and the final objective count are correct.

6. **General graphic TSP.** I checked the chain of lemmas proving `s12pair:theorem`, especially:

   - `s12pair:connector-completion`, lines 5655–5985: the simultaneous minimum-cut connector assignment is justified. In the exchange case, the witnessing cut contains no other connector because every connector had capacity 2/3 and the witness capacity is strictly smaller. The violated edge f cannot belong to that witness cut. Symmetric difference therefore preserves the violation while decreasing the number of crossing connectors, as required.
   - `s12pair:connector-estimate`, lines 5990–6312: the three cut cases exhaust the possibilities after contracting the other connectors. The two ordinary subtour cuts supply the two terms `2-q-a` and `q+a-eta`; the singleton cases give the separate predecessor contribution. When eta is zero, the claimed equality for the specialized connector formula follows from the available singleton witness.
   - The construction and connector bounds for Q^(2), lines 6320–6445: every cut expression in G is at least x(C)/2, and integral join lifting preserves the required parity. The stronger connector inequality uses an odd number of remaining incident tree edges exactly when the center's tree degree is even.
   - `s11p:scalar`, lines 6450–6486: greedy DFS gives `1+bar_e <= t(1-bar_e)`. The subsequent scalar inequality has the nonnegative difference `(t-7)^2/[64(t+1)]`, with the constants as printed.
   - `s12pair:local-charge`, lines 6542–6798: both branches of the star maximum are bounded. In the predecessor case, substituting the degree equation cancels the predecessor q term and leaves the scalar bound plus nonpositive terms. For multiple positive chi terms at a center, subtracting at least two from their disjoint star weights correctly bounds their sum by eta.
   - The aggregation, lines 6800–6898: the nonroot edge partition, support sparsity, and root-star calculation are compatible. The root eta terms cancel with the nonroot charge budget, leaving `89n/64 + 9(L-n)/8 - 13/16`. Since L >= n, the asserted 89L/64 bound follows. The specialization to L=n, lines 6920–7011, is consistent with the main-text construction.

   I found no reversed inequality, missing cut case, unjustified rounding step, or lost positive term in these arguments.

### Harmless wording issue

**Location:** Section “The StarReconnectionLP,” TeX line 756, immediately following the explanation of the loop variable.

The sentence says that when the loop is not selected, the reconnection cost is “exactly 2 units.” As a statement about actual necessary reconnection, this is too strong. A loop can be unselected while the star is not fully selected, in which case no reconnection is needed.

For a concrete example within the formulation, take a triangle r-a-b-r, its DFS path r-a-b, and root star S={ra,rb}. In the split graph, select only the root connector and select no representative edges and no loop. This is a feasible integral degree-bounded odd join: r and z_S have the correct odd parity, and the auxiliary selected degree is 1 <= 3. Its projection is the empty join, so the original triangle already supplies a connected even graph and the actual reconnection cost is zero.

The footnote on the same line correctly describes the cost as **at most** `2(1-y_loop)`, and the later proof uses the correct inequality (`eq:saturation-probability`, lines 2301–2312). Thus this is an expositional imprecision, not a substantive error, and it does not affect any claimed approximation conclusion. Suggested correction: “we charge two units, which upper-bounds the reconnection cost.”

## Independent checks of the numerical example

For the graph specified in lines 2458–2699, I reconstructed its 22 tree edges, eight back edges, and five stars directly from the text and figure definitions.

- All 4,194,303 nontrivial cuts, counted once up to complementation, have x-weight at least 2. The displayed vector has cost 26. Its 35 tight cuts have rank 30 over the field of order 1,000,003, certifying full column rank for the 30 positive edge variables and hence extremality over the rationals.
- I also obtained an exact half-integral dual certificate of value 26. Give weight 1 to the singleton cuts at 2, 11, 13, 15, 19, 20, and 22; give weight 1/2 to the singleton cuts at 4, 6, 8, 12, 14, 16, 17, and 21, and to the cuts with shores {4,12}, {6,14}, {16,17}, and {8,21}. Each edge has total dual load at most 1, and twice the sum of these weights is 26. This independently verifies subtour optimality.
- Enumerating the 256 joins through the graph's fundamental cycle basis gives deletion-LP optimum 28 and reconnection-LP optimum 27, using the paper's star constraints and saturation charges.
- Enumerating the 32 joins on the displayed MS support gives optimized MS parity-correction value 29 for the stated pairs.
- A separate numerical solution of the explicitly described circulation gives minimum cost 1 and an integral optimum, consistent with the claimed circulation estimate 92/3. This last calculation is numerical corroboration, unlike the exact half-integral dual and finite join enumerations above.

These checks corroborate the comparison example; they are not the justification for the general theorems.

## Limitations and supplementary claims

The standard externally cited facts—including the b-factor polytope theorem, polynomial-time matching and circulation optimization, the sparse-support fact, the box-constrained optimal-solution reduction, and block reduction—were assessed for correct formulation and application. I did not independently consult or reconstruct every cited external proof. Bibliographic priority claims and assertions about what earlier papers contain were not independently verified.

I read the further-improvements section, lines 7017–7235. Its laminar counting argument and the partitionable-center estimate are consistent: if the partition containing the child edge contains p back edges and the other partition contains t-p, then the excess is at most both p q and (t-p-1)q, yielding the printed floor bound. For the laminar tree, a node with k >= 3 children can account for at most k unpartitionable singleton children and incurs deficit k-2; the inequality k <= 3(k-2) supplies the stated ceiling loss.

The additional ratios 14524/10481, 9/7, and 41944/31181 in the discussion are explicitly accompanied only by sketches and references to external formalizations. The supplied text does not contain the complete derivations of those ratios or the complete combined use of the Z-circulation refinement. I have not independently verified those stronger results. Statements about Lean verification, authorship, or AI assistance were not used as evidence of correctness. This limitation does not reveal a contradiction in the supplied argument, but the supplementary ratios should not be treated as independently checked by this report.

Subject to these stated limits, the verdict is ACCEPT: no substantive mathematical error was found in the current paper's reviewed arguments, and the fully presented main approximation proofs withstand the checks described above.
