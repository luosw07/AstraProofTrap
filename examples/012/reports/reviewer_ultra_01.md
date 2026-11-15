REJECT

I found a substantive, explicit counterexample to the feasibility assertion for the quartic-graph correction procedure. The procedure permits a paid increase on an edge incident to a degree-two vertex of the auxiliary graph, without increasing that vertex's other incident edge. The resulting vector violates a Blossom inequality. This is a failure of a stated intermediate proposition and of the prescribed construction, not a counterexample to the numerical approximation bound itself. I did not find a separate substantive error in the detailed general-graph proof of the 89/64 bound.

## 1. A permitted paid increase makes the final vector infeasible

**Locations.** Appendix `sec:quartic-framework-2`, subsection `subsec:quartic-repair-procedure`, TeX lines 4260–4269, especially the instruction at 4263–4265 to choose an arbitrary edge of an unmatched demand's boundary; the assertion at lines 4309–4315 that both edges at every degree-two vertex still have value 1/4; Proposition `prop:quartic-completed-vector`, lines 4589–4606. The proof of Theorem `thm:quartic-thirteen-tenths` uses this proposition at lines 5193–5212.

The issue is that an unmatched vertex demand at u can have a nonremovable child edge uv, where v centers a three-edge star. In H° the original copy of v then has degree two: its incident edges are rep(uv) and the connector of that three-edge star. The procedure allows rep(uv) to be increased from 1/4 to 1/2, while the connector remains 1/4. A point of the odd(H°)-join polytope must have equal coordinates on the two edges of any degree-two cut; this permitted correction therefore destroys feasibility.

### Explicit graph satisfying the theorem's assumptions

Let the vertices be 0,1,…,19 and let the edge set consist of the following 40 unordered pairs:

```text
(0,1)   (0,10)  (0,12)  (0,19)
(1,2)   (1,3)   (1,6)
(2,3)   (2,8)   (2,10)
(3,4)   (3,18)
(4,5)   (4,6)   (4,15)
(5,6)   (5,13)  (5,15)
(6,7)
(7,8)   (7,14)  (7,17)
(8,9)   (8,19)
(9,10)  (9,12)  (9,17)
(10,11)
(11,12) (11,14) (11,16)
(12,13)
(13,14) (13,15)
(14,15)
(16,17) (16,18) (16,19)
(17,18)
(18,19)
```

This graph is simple and every vertex has degree four. I checked 4-vertex-connectivity directly by deleting each of the C(20,3)=1140 triples and running a graph traversal: every resulting graph had all 17 surviving vertices reachable. Checking every triple also excludes a separator with fewer than three vertices. This is a finite graph calculation, not an appeal to another paper or to a proof assistant.

Use the DFS tree rooted at 0 whose edges are the path

```text
0–1–2–3–4–5–6–7–8–9–10–11–12–13–14–15
```

together with the second branch

```text
11–16–17–18–19.
```

Visit the branch starting at 12 before the branch starting at 16. Every nontree edge in the displayed graph joins an ancestor to a descendant, and visiting unvisited neighbors in increasing numerical order gives exactly this DFS tree. Thus this is a valid fixed DFS tree of the kind allowed by the quartic theorem.

Vertex 11 is the only nonroot vertex with two DFS children. Its children are 12 and 16, its parent is 10, and its unique entering back edge is (11,14). Hence

```text
B₂ = {11},
S₁₁ = {(11,12), (11,14)}.
```

There is no back edge ending at 10 from the subtree of 11, so (10,11) belongs to N. There is no back edge from the subtree of 16 ending at 11, so (11,16) also belongs to N. Consequently U={11}. There are no triangle demands: D is a subset of B₂, but 11 cannot be a triangle-demand center because its parent edge is nonremovable. Thus the correction graph K has one isolated vertex, its maximum matching is empty, and there are no objective-preserving parent-edge changes.

The unmatched demand boundary is exactly

```text
E₁₁ = {rep(10,11), c_S₁₁, rep(11,16)}.
```

The explicit instruction at lines 4263–4265 permits choosing rep(11,16). Make that choice, increasing its coordinate to 1/2.

Vertex 16 has exactly one DFS child, 17, and two entering back edges, (16,18) and (16,19). It therefore centers the three-edge star

```text
S₁₆ = {(16,17), (16,18), (16,19)}.
```

After the star splitting, the original vertex 16 in H° has precisely the two incident edges

```text
C = δ_H°({16}) = {rep(11,16), c_S₁₆}.
```

No step of this correction changes c_S₁₆, so the final values are

```text
x̄_rep(11,16) = 1/2,       x̄_c_S₁₆ = 1/4.
```

Take F={rep(11,16)}. Then |C\F|=1 is odd, so this is one of the paper's required Blossom inequalities. Its left side is

```text
x̄(C\F) + |F| − x̄(F) = 1/4 + 1 − 1/2 = 3/4 < 1.
```

Therefore the vector produced by this expressly permitted run of the procedure does not belong to P°. This directly contradicts Proposition `prop:quartic-completed-vector`. It also disproves the blanket assertion at lines 4309–4310 on which the suppression argument relies.

### Effect and possible repair

This is substantive rather than a harmless typographical error: an allowed algorithmic choice produces a vector outside the claimed feasible polytope, so the tour-bound theorem cannot be applied to that vector. The proof as written does not justify its claimed feasibility guarantee for the stated procedure or the ensuing quartic certificate construction.

The numerical 13/10 theorem may nevertheless be repairable. In particular, choosing an unmatched demand's own connector, instead of an arbitrary boundary edge, avoids this specific problem. The caption at lines 4961–4964 in fact says that unmatched demands use their own connectors, whereas the operative procedure says to choose arbitrarily. The latter freedom must be removed or otherwise controlled, and the degree-two-vertex assertion must then be proved for the resulting rule. I have not treated the counterexample as a disproof of the existential 13/10 tour bound. The general 89/64 construction in Appendix `sec:general-L` does not depend on this quartic correction procedure and is not invalidated by this finding.

## 2. Review coverage and limitations

I read all 7270 lines of the supplied standalone TeX in bounded, nontruncated chunks, including its bibliography, figure definitions, all appendices, the further-improvements discussion, and the methodology statement. I used the TeX as the complete paper; I did not separately inspect the rendered PDF. I did not consult another version, any other workspace source, another review, external literature, or Lean artifacts, and did not use a formal proof assistant.

I examined the degree-bounded join polytope reduction, the two LP formulations and tour recovery, the DFS removable-system proof, the circulation comparison, the quartic small-cut classification and counting argument, the k-connected degree-bounded construction, and the general-graph fractional constructions and aggregation. In particular, I checked the connector minimum-cut completion argument, the connector estimates, the half-subtour lift, the scalar inequality using (t−7)², the local star charge, and the final coefficient calculations for 89/64. Apart from the quartic correction flaw above, I did not identify a substantive failure in these written arguments.

The bibliography's external results were not independently rederived or checked against their cited originals. I did not independently certify every numerical optimum in the 23-vertex comparison example. The stronger ratios advertised as Lean-verified are explicitly not proved in full in the supplied paper (lines 1339–1340, 1348, and 7024–7026); I cannot verify those advertised formalizations from this paper alone. This review's finding is the explicit mathematical counterexample above, and its favorable observations on other portions are not claims of formal verification.
