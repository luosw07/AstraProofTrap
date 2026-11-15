ACCEPT

I found no substantive mathematical error in the supplied current paper. This is an independent mathematical review, not a claim of formal verification.

## Scope and method

I read the entire supplied `paper.tex`, lines 1–7270, in bounded, consecutively numbered chunks, including the main text, every appendix, figure specifications and captions, and bibliography. I used this document alone as mathematical input. I did not inspect another version, another workspace document, another reviewer’s report, or the cited Lean development. I did not use a proof assistant or delegate the review. The TeX contains the mathematical arguments and the diagrams’ source descriptions; I did not separately inspect the PDF rendering.

The review concentrated on the actual arguments establishing the three main guarantees, rather than the paper’s authorship, provenance, or statements concerning formal verification. I also independently enumerated the parity corrections in the worked separation example.

## Main mathematical checks

### 1. Degree-bounded joins and recovery of tours

The reduction in Theorem `thm:bounded-T-join` (lines 1774–1831) is sound. The parity-adjusted bound beta has the required parity; adding slack loops converts the degree inequalities to factor equations. For a vertex in T, the singleton blossom inequality supplies the lower bound needed to ensure that the available slack loops suffice. Loops do not change the cut inequalities. The projection argument therefore supports the integrality used later, subject to the cited standard factor-polytope theorem.

The lift and contraction parity arguments are consistent (lines 2057–2087, 2288–2338, and 3282–3320). In the reconnection formulation, a fully selected star has its loop absent. Deleting its selected removable edges and then restoring two copies of one edge preserves parity and permits connectivity to be restored using the defining removable-system property. The expected-cost argument charges an upper bound, which is the correct direction.

Eliminating the loop variables gives exactly the maximum expression in equation `eq:repair-nonloop-cost` (lines 2363–2399). The general constant is m minus the sum of k_S−1; its replacement by n−1 for DFS stars is justified by the DFS counting identity. There is no reliance here on the false general principle that minimizing a convex function over an integral polytope must yield an integral minimizer: the paper retains an integral linear extended formulation and uses that formulation for recovery.

### 2. DFS removable systems and circulation comparisons

The cycle argument in Lemma `lem:DFS-removability` (lines 2851–2969) correctly shows that every cycle has two edges in one star. Keeping one edge per star consequently gives an acyclic graph with n−1 edges, hence a spanning tree. The use of the DFS ancestor property in identifying the second crossing edge is valid.

The support-restoration accounting (lines 3195–3225) and the extension of joins by omitted back edges (lines 3401–3467) preserve the intended parity and objective. I also checked the distinct comparison with optimized MS parity correction in Lemma `lem:reconnection-MS-parity` (lines 3474–3537): fully selected stars can be charged injectively to selected tree edges that the MS construction leaves unpaired. The resulting two-unit savings pay for the reconnection charges.

The LPone comparison proved by the paper is with the circulation certificate; the stronger comparison with optimized parity correction is explicitly proved for LPtwo. I read the overview language in light of these precise statements.

### 3. The quartic 13/10 bound

I checked the classification of nonroot vertex types, the initial assignments, and the objective calculation (lines 3645–3691 and 3761–3877). A parent-edge increase at a B_2 vertex has zero objective cost exactly when that edge is removable. The remaining singleton and triangle demands use paid edges.

The degree-two suppression and removal of the root connector (Proposition `lem:quartic-reduction`, lines 4309–4397) preserve the relevant cut verification. In the reduced graph, the small-cut proof (Lemma `lem:quartic-small-cuts`, lines 4416–4476) uses 4-vertex-connectivity in the right way: deleting s centers leaves enough edge connectivity to delete at most 3−s additional edges. This forces one shore to have at most three vertices. Simplicity and minimum degree three then give precisely a singleton or a triangle.

The triangle classification (lines 4518–4588) follows from the tree/back-edge incidence counts at degree-three vertices. The correction procedure satisfies both kinds of three-edge blossom inequalities, and cuts of size at least four are covered by the coordinate lower bound.

I checked all three shared-correction cases and the forest argument (lines 4630–4921). The forest’s predecessor and successor restrictions justify the independent-set inequalities. The counts
n−2 = 2|N| + n_1 + |B_2|,
|N| >= |U| + |D| + c_U,
and n_1 + |B_2| >= |U| + 2|D| + c_D
are supported by the disjoint objects identified in the text (lines 5059–5188). Combined with the independent-set calculation, they give at most (n−2)/5 paid increases. Substitution yields 13n/10−3/5 as claimed.

### 4. The degree-bounded k-connected 4/3 result

The construction in Theorem `thm:k-connected-four-thirds` (lines 5244–5432) satisfies each auxiliary degree bound with equality. In the blossom verification, a cut with one edge outside F reduces to a complement-capacity inequality. Two expanded-tree edges already suffice. If exactly one expanded-tree edge crosses, the original cut or the cut in G−u supplies at least k−1 back edges. This validates the use of vertex connectivity at the connector case. The objective aggregation gives 4n/3−2/3.

### 5. The general 89/64 result

I scrutinized the minimum-cut connector completion in Lemma `s12pair:connector-completion` (lines 5655–5985). The admissibility bound d_S <= 1−q_S is used to obtain
1−Q(d)_rep(e) >= 2x_e/3.
Because every coordinate is at least 1/3, only the blossom cases with exactly one edge outside F remain. The cut-exchange argument in Case 3 is valid: a raised connector has a witness cut whose other edges contain no connectors, and a violating edge f cannot lie in that witness cut. Taking the symmetric difference removes the connector without losing f or increasing the opposing complement sum.

The connector estimate (lines 6000–6312) covers all cuts after other connectors are contracted. For a cut with two nonempty original shores, the two subtour inequalities give the two stated bounds. The singleton cases are also correctly separated. For L=n, tau vanishes and the claimed explicit connector formula follows.

The half-subtour point and its lift (lines 6320–6445) are feasible: each edge contributes at least x_e/2 to any relevant cut expression before lifting, and the connector bounds follow from valid local blossom inequalities with the stated parity.

I checked the scalar calculation in Lemma `s11p:scalar` (lines 6450–6486), including the identity involving (t_S−7)^2. In Lemma `s12pair:local-charge` (lines 6542–6798), the excess truncation, the successor-connector calculation, and the charge sum at a vertex all have the correct signs and constants. In particular, Case 2 uses the predecessor’s t-value in the subtraction and then converts the remaining bound to 1/64 <= t_S/64; it does not require the successor star to be positive.

Finally, the root-star charge and the nonroot charges cancel the root excess in the stated way (lines 6803–6898). The aggregation yields
89n/64 + 9(L−n)/8 − 13/16
and hence at most 89L/64. The L=n specialization in lines 6920–7011 is consistent with that analysis.

## Independent calculation of the example

I reconstructed the 23-vertex, 30-edge example directly from the edge lists and drawing source in lines 2463–2470 and 2551–2600.

Using the eight fundamental cycles of its displayed spanning tree, I enumerated all 256 odd(G)-joins. Evaluating the two integral star objectives gives:

- LPone optimum: 28.
- LPtwo optimum: 27.

For the displayed MS support and pairing, I enumerated its 32 joins and obtained optimized parity-correction length 29. These agree with lines 2485–2492.

I also enumerated all 4,194,303 nonempty vertex subsets excluding one fixed vertex for the displayed half-integral x. The minimum cut weight was 2 and the total weight was 26. There were 35 tight cuts; ordinary numerical row reduction of their incidence vectors gave rank 30, consistent with the claimed extremality. This calculation did not independently construct an optimal dual certificate for the value 26, nor solve the circulation optimization. It should not be represented as a complete computational certification of every assertion about the example.

## Minor wording issues, without effect on the conclusions

1. **Line 756, paragraph after `proc:repair-polytope`:** The phrase saying that the cost is “exactly 2 units” when the loop is not selected is stronger than the actual recovery implication. A loop can be absent without the star being fully selected, in which case no reconnection need be performed. The footnote on the same line correctly uses “at most,” and Theorem `thm:framework-2-bound` uses the correct inequality at lines 2305–2311. This is a harmless wording inconsistency, not an error in the bound.

2. **Algorithm line 826:** Z is called “Eulerian” before its components are reconnected. At that stage its degrees are even but it may be disconnected. Under a convention requiring an Eulerian graph to be connected, “an even-degree multigraph” would be more precise. The following step explicitly reconnects Z, so this terminology does not invalidate the algorithm.

## Limitations

The main arguments use standard cited results about factor polytopes, circulation integrality, sparse extreme subtour supports, box-constrained optimal subtour solutions, and block reduction. I checked their roles and compatibility with the deductions in this paper, but did not consult the cited sources under the single-document review restriction.

The stronger numerical guarantees described as Lean-verified in the Discussion and Table `tab:discussion-results` (lines 1338–1377) are not proved in full in this document. The Further Improvements appendix explicitly identifies its discussion as partial (lines 7020–7028). I read its circulation construction, laminar counting argument, and stated estimates, but have not independently established the omitted combined analyses or the external formalizations. Those claims are therefore outside the strength of my verification; I did not treat the references to Lean as mathematical evidence. They are not needed for the three fully presented main approximation guarantees reviewed above.

I found no substantive error requiring rejection in the supplied arguments. ACCEPT records that review finding, with the preceding coverage and limitations.

