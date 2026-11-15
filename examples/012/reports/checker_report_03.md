OK

# Independent mathematical audit

The mutation creates a substantive proof defect, its supplied primary label G1 is correct, and it is sufficiently subtle and integrated for the benchmark. An explicitly permitted repair selection produces a vector outside the stated odd-join polytope. The defect is not merely an unproved claim or a changed absorbable constant.

## Scope and reading

I read the supplied private log in full and the entire modified paper (7,270 physical source lines), including figures, bibliography, appendices, and methodology. The paper was read in bounded chunks. An initially oversized tool response truncated part of the first 900 lines; the potentially missing portion was reread in the separate 451–900 chunk. I used the original excerpts in the log for comparison. I did not inspect other experiment material, other versions, other agents, the tricker's verification program, or its output files. No delegation or formal proof assistant was used.

I independently reconstructed the witness graph, checked its connectivity by elementary finite enumeration, and computed its DFS and stars. This was fresh JavaScript executed in the tool runtime; it did not import the tricker's verifier. An attempted Python execution was unavailable and supplied no mathematical evidence.

## Exact mutation and first failure

In Appendix G, `subsec:quartic-repair-procedure`, lines 4263–4266, the unmatched demand's own connector is replaced by an arbitrary edge of its boundary set. The overview is correspondingly broadened at lines 1304–1306. The original paragraph explaining that an increased nonremovable edge must join two matched vertex demands is removed.

The first false downstream assertion is at lines 4309–4310, in `subsec:quartic-feasibility`: every degree-two vertex of H-circ has both incident values 1/4. The suppression then assigns 1/4 to each replacement edge, and Proposition `lem:quartic-reduction` applies a cut-transfer argument that needs those common values. The final-vector assertion in `prop:quartic-completed-vector` (lines 4589–4606) is actually false for an allowed execution.

The newly inserted cost sentence is correct. Every edge in these demand boundaries is a nonroot connector or a nonremovable tree-edge representative, initially valued 1/4. Its increase costs 1/4. Correct cost accounting does not imply feasibility.

## Actual assumptions and independently checked witness

The quartic section assumes a simple, 4-regular, 4-vertex-connected graph and an arbitrary fixed DFS tree. Its theorem is not restricted to the support of an extreme subtour solution. The separate sparsity and greedy-DFS hypotheses in the general-graph analysis therefore do not exclude this example.

Use vertices 0 through 12 with adjacency lists:

```
0: 1,5,9,12       1: 0,2,8,11       2: 1,3,5,9
3: 2,4,10,12      4: 3,5,10,11      5: 0,2,4,6
6: 5,7,11,12      7: 6,8,9,10       8: 1,7,9,10
9: 0,2,7,8       10: 3,4,7,8       11: 1,4,6,12
12: 0,3,6,11
```

I checked distinct neighbors, symmetric adjacency, absence of loops, and degree four at every vertex. For every deleted vertex set of sizes 0, 1, 2, and 3, I traversed the remaining graph and found it connected. The respective counts were 1, 13, 78, and 286, with no failures. Thus the exact required vertex-connectivity hypothesis holds.

Increasing-neighbor DFS rooted at 0 gives preorder 0,1,...,12 and parent array

```
[-1,0,1,2,3,4,5,6,7,8,8,6,11].
```

Using the paper's definition of I(u,v), I independently obtain these stars (pairs denote edges):

```
S0 = {0-1,0-5,0-9,0-12}
S1 = {1-2,1-8,1-11}
S2 = {2-3,2-5,2-9}
S3 = {3-4,3-10,3-12}
S4 = {4-5,4-10,4-11}
S6 = {6-11,6-12}
S7 = {7-8,7-9,7-10}
N  = {5-6,6-7,8-9,8-10,11-12}.
```

The sole member of B2 is 6. Its parent edge 5-6 is nonremovable, so U={6}. The triangle demands D are empty: their centers must belong to B2 and have a removable parent edge. There are no objective-preserving parent-edge changes, K has one isolated vertex, and its unique maximum matching is empty. Hence there is no hidden matching choice or unperformed free change affecting the example.

The unmatched demand boundary is

E6 = {rep(5-6), c6, rep(6-7)}.

The new rule expressly permits choosing rep(6-7) and increasing it from 1/4 to 1/2. It repairs the demand at 6: its boundary values become 1/4,1/4,1/2 and sum to one. The box constraints and the paid-increase budget are respected.

Vertex 7 has one child, 8, and two entering back edges, 7-9 and 7-10. Its size-three star moves all three of those incidences to z7. The original vertex 7 consequently has exactly the two incident edges rep(6-7) and c7 in H-circ. The chosen repair changes only the former. Its two values are now 1/2 and 1/4.

## Decisive Blossom calculation

Set X={7}, C=delta(X)={rep(6-7),c7}, and F={rep(6-7)}. Then |C minus F|=1 is odd, exactly as required by `eq:repair-nonloop-polytope`. Its left-hand side is

```
x(C minus F) + |F| - x(F)
= x(c7) + 1 - x(rep(6-7))
= 1/4 + 1 - 1/2
= 3/4 < 1.
```

This is a violated inequality of the actual formulation, not a substitute condition. Generally the two Blossom inequalities of a two-edge cut {a,b} are y(a)+1-y(b)>=1 and y(b)+1-y(a)>=1; together they require equality of the two coordinates. Thus no omitted argument can establish feasibility of this particular vector.

The original rule instead raises c6. It leaves the two edges at 7 equal to 1/4. More generally, in the original excerpt a paid increase of a nonremovable edge joins two matched vertex demands, both in U and therefore both with two DFS children. Such an increase cannot change the parent edge of a one-child vertex. Free parent-edge increases are also confined to B2. Demand connectors belong to size-two stars, whereas the degree-two original centers come from size-three stars. These restrictions justify the invariant needed for the original suppression step.

## G1 classification and quantifiers

Fix admissible G and T; these determine the stars, H-circ, demands and K. Fix any maximum matching M. A selection c consists of the shared edge for each matched pair and the edge for each unmatched demand; free changes are fixed by G and T. Write x(c) for its resulting vector.

Let Cold(G,T,M) restrict every unmatched choice to its own connector, and let Cnew(G,T,M) allow any edge of the corresponding demand boundary. Both families retain the shared-boundary restriction for matched pairs and the prescribed free changes. Cold is a subset of Cnew, strictly so in the example.

The pre-generalization implication used by the original proof is:

```
admissible(G,T), maximum_matching(M,K), c in Cold(G,T,M)
    => all suppressed incident pairs have values (1/4,1/4)
       and x(c) satisfies every required Blossom inequality.
```

The universally quantified variables are G, T, M, and the permitted selection c; within the feasibility conclusion they also include every shore X subset W and every F subset delta(X) with the required parity. The modified procedure enlarges c's range to Cnew while retaining the same invariant and feasibility conclusions. It does not supply the extra argument needed to discharge the old selection restriction. The witness fixes G,T,M and a particular c in Cnew minus Cold, then fixes an allowed X,F falsifying the conclusion.

Thus the supplied G1 label accurately identifies an illicit generalization from a restricted family of selected objects to a larger family. No scalar parameter, asymptotic constant, or parameter dependency can absorb the 1/4 violation. This is not primarily an algebraic conversion or an existential-witness substitution.

## Possible interpretations, downstream significance, and subtlety

The ultimate tour theorem asserts existence and may still be true. The old connector selection remains available. Nevertheless the submitted proof explicitly says to choose an arbitrary boundary edge and defines its final vector from those corrections; the subsequent proposition asserts that vector's feasibility. Reading the selection existentially and quietly choosing the old connector rule changes the stated allowable construction and its universal correctness claim. It is a substantive repair, not an interpretation that makes the current arbitrary-choice argument valid. The unchanged figure caption shows the old selection as an illustrative special case; it does not override the explicit algorithmic rule.

Numerically, the witness has initial objective 63/4 and one paid increase, giving 16. The budget is rho=1 <= 11/5, and 16 <= 163/10, the claimed bound at n=13. These correct inequalities cannot justify the tour-certificate invocation for a vector outside P-circ. Suppression also discards the changed value at 6-7, so the surviving cut at 6 again has three 1/4 values, contradicting the later reduced vertex-cut assertion.

Prospectively, the defect is sufficiently subtle: any boundary edge repairs the local deficient cut at the same cost, the matching and counting arguments survive, and the lost restriction matters at another endpoint in a subsequent graph reduction. A careful reader tracking degree-two cuts can detect it fairly quickly once prompted; it is not maximally concealed. But it is mathematically integrated and plausibly missed in a review focused on demand satisfaction and cost. I use no blind-review outcome in this assessment.

There is no unresolved issue material to this verdict. I did not independently enumerate every Blossom inequality of the original vector; that stronger claim in the log is unnecessary for the decisive modified-vector disproof and is not treated as independently verified here.
