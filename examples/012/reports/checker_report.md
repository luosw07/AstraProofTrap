OK

Independent checker report — checker_3301

Verdict

The planted change is a substantive mathematical defect. Its primary G1 classification is justified: a feasibility argument valid for a restricted family of repair selections is extended to an explicitly larger arbitrary-choice family without preserving its essential endpoint restriction. The resulting constructed vector can violate an actual defining Blossom inequality by 1/4 on a graph satisfying all of the quartic theorem's hypotheses. The mutation is sufficiently subtle and integrated for this benchmark. This verdict concerns the modified construction and proof, not falsity of the ultimate tour-length theorem.

Inputs and full-paper coverage

I read the entire supplied paper.tex, lines 1–7270, including the preamble, main text, bibliography, every appendix, all figure definitions/captions, and AI methodology. Reads were bounded and untruncated: 1–600, 601–1300, 1301–2100, 2101–2900, 2901–3700, 3701–4400, 4401–5208, 5209–5900, 5901–6600, and 6601–7270. I also read the complete supplied tricker_log.md, including both original excerpts and the proposed witness. I did not inspect another paper version, other experiment material, another agent's work, a blind-review outcome, or the tricker's verification program/output. I did not delegate or use a formal proof assistant. The original wording is available to me only through the designated log; I do not independently certify its provenance or a byte-for-byte comparison with another version.

Exact mutation and dependencies

At paper lines 1304–1306 the overview changes an unmatched-cut connector correction to a boundary-edge correction. The operative change is lines 4263–4266, in subsec:quartic-repair-procedure: every unmatched demand may choose an arbitrary edge of its boundary E_u. The log's original excerpt instead increases its own connector c_{S_u}. The original subsequent paragraph explains that increased nonremovable edges must join two matched vertex demands, and therefore cannot be parent edges of vertices with one DFS child. That restriction and explanation have been replaced by the true cost statement at 4271–4273.

The first false downstream invariant is at 4309–4310: both incident edges at every degree-two vertex of H^circ are asserted to have value 1/4. Lines 4314–4316 assign 1/4 to suppression replacement edges. Proposition lem:quartic-reduction, lines 4365–4397, relies on common incident values to transfer cut inequalities. Lemma lem:quartic-vertex-cuts, especially 4498–4503, also assumes the paid corrections survive in the reduced vector. Proposition prop:quartic-completed-vector, lines 4589–4606, asserts feasibility for the completed vector. Lines 5194–5207 use this membership to invoke the tour certificate bound.

Actual assumptions and quantifiers

The independent quartic section fixes a simple, 4-regular, 4-vertex-connected graph G and an arbitrary rooted DFS tree T (1120–1123, 3630–3636, 3744–3755). Its stars are the prescribed DFS stars S(u,v)={uv} union I(u,v), with I nonempty. This part does not assume that G is the support of an extreme subtour solution, impose the general-section sparsity hypothesis m<=2n-3, or require the greedy DFS construction from the general approximation algorithm. In particular, the witness with m=2n is admissible. The general section's support assumptions are scoped to that other analysis and are explicitly restated there.

For each admissible G,T, let K be the prescribed demand graph, let M range over maximum matchings of K, and let c encode all repair choices. Define C_old(G,T,M) by the original excerpt: increase removable parent edges only for the indicated B_2 vertices; choose shared boundary edges for matched pairs; use c_{S_u} for each unmatched demand. The valid pre-generalization implication at issue is

  c in C_old(G,T,M) => every degree-two vertex of H^circ has both incident values 1/4 => the common-value suppression argument applies.

Combined with the subsequent small-cut proof, the original selected-family conclusion is xbar^(c) in P^circ. These statements hold uniformly over admissible G,T,M and the choices still free inside C_old. For a degree-two original vertex, its star has size three and it has one DFS child. Free parent changes are confined to B_2. Paid nonremovable changes for matched pairs have both endpoints in U, hence both endpoints have two DFS children. The vertex's own size-three-star connector is in no demand boundary. Both incident coordinates therefore remain 1/4 under the original rules.

C_new replaces the unmatched connector restriction by e_u in E_u, with every such edge explicitly allowed. The actual target range is every output obtained by this broadened procedure, not just the original outputs and not arbitrary box-constrained vectors. For each target output the asserted membership requires every shore X subset W and every F subset delta(X) with |delta(X) minus F| odd to satisfy the displayed inequality (2344–2356 and 4299–4307). The witness below fixes admissible G,T and the unique maximum matching, then selects one of the newly allowed edges. Thus it attacks precisely this quantified claim.

Independent admissible witness

Use V={0,...,12} and the following adjacency lists:

  0: 1,5,9,12
  1: 0,2,8,11
  2: 1,3,5,9
  3: 2,4,10,12
  4: 3,5,10,11
  5: 0,2,4,6
  6: 5,7,11,12
  7: 6,8,9,10
  8: 1,7,9,10
  9: 0,2,7,8
  10: 3,4,7,8
  11: 1,4,6,12
  12: 0,3,6,11

These lists are symmetric, have four distinct neighbors each, and have no loops. I independently enumerated every vertex-deletion subset of size at most three and performed graph traversal on the survivors. The counts were [1,13,78,286]; all 378 survivor graphs were connected. This verifies 4-vertex-connectivity, not merely edge connectivity. My independent computation used elementary JavaScript in the tool runtime and the adjacency lists above, not the tricker's checker or mathematical libraries. An initial attempt to run Python was unavailable and supplied no evidence; the successful JavaScript check supplied the reported results.

I independently reconstructed increasing-neighbor DFS rooted at 0. Its preorder is 0,1,...,12 and its parent array is

  [-1,0,1,2,3,4,5,6,7,8,8,6,11].

The DFS stars, indexed by center, are

  0: {0-1,0-5,0-9,0-12}
  1: {1-2,1-8,1-11}
  2: {2-3,2-5,2-9}
  3: {3-4,3-10,3-12}
  4: {4-5,4-10,4-11}
  6: {6-11,6-12}
  7: {7-8,7-9,7-10}.

The remaining edges are N={5-6,6-7,8-9,8-10,11-12}. The DFS/star reconstruction independently agrees with these sets. Vertex 6 has two children, 7 and 11, and exactly one entering back edge, 6-12, from the 11 subtree. Vertex 8 has two children but no entering back edge. Thus B_2={6}, and because 5-6 is nonremovable, U={6}. Triangle demands are a subset of B_2 outside U, so D is empty. No free parent-edge increase occurs. K has exactly one isolated vertex, and its unique maximum matching is empty.

The sole demand boundary is E_6={rep(5-6),c_6,rep(6-7)}. Each coordinate starts at 1/4. Choose rep(6-7) under the new arbitrary-edge rule and increase it to 1/2. This is a fully permitted execution. Its demand boundary sum becomes 1, it respects all box constraints, and it uses one paid increase of cost 1/4.

At vertex 7, the size-three star moves all incidences 7-8,7-9,7-10 to z_7. The original copy of 7 is therefore incident only to rep(6-7) and c_7. The connector c_7 is unchanged at 1/4. Set

  X={7}, C=delta_Hcirc(X)={rep(6-7),c_7}, F={rep(6-7)}.

Then |C minus F|=1 is odd, and the actual defining inequality has left side

  xbar(C minus F)+|F|-xbar(F)
  = 1/4 + 1 - 1/2
  = 3/4 < 1.

This exact two-edge calculation decisively disproves xbar in P^circ. More generally, the two Blossom inequalities on a degree-two cut {a,b} force y_a=y_b. A scalar cost explanation cannot replace this equality.

The original unmatched repair raises c_6 instead. It leaves the two coordinates at vertex 7 both equal to 1/4 and avoids this violation. I did not independently exhaustively enumerate all Blossom cuts for the original vector, and do not rely on the log's claim to have done so. That is unnecessary to the disproof; the original endpoint restriction independently establishes the invariant that the mutation loses.

Classification and competing interpretations

G1 is the substantive mechanism: a restricted selected-object argument is generalized to a larger family of selections. The relevant restriction is structural, not merely syntactic: an increased nonremovable edge was allowed only when both endpoints are demands. Newly allowing an unmatched demand to select its nonremovable child edge loses this condition at a one-child child. The universally quantified cut verification is then reused on a vector outside the family for which its suppression premise was established.

There is a downstream failed modus-ponens application in the broad sense that common-value suppression needs a premise which is now false. That does not displace G1 as the primary planted mechanism: the mutation is the enlarged choice family, and the omitted endpoint invariant is the precise dependency it violates. There is no G2-type exchange of quantifier order required for this witness: G,T,M are fixed and the newly free selection is concretely instantiated. There is no definition mismatch (DEF): E_6, rep, the connector, P^circ and the odd-complement parity condition all have their literal declared meanings. Nor is there a faulty algebraic conversion (CONV): the cost identity, the repair count, and the inequality calculation are correct. The subsequent suppression is unjustified specifically because its equality premise has been lost.

The word 'arbitrary' cannot validly be read as 'choose only a connector' while leaving this procedural claim intact. The overview agrees with the broader scope; the feasibility subsection explicitly refers to the corrections just defined. The unchanged caption at 4961–4964 illustrates the original connector selection, which remains one permitted execution; it does not override the operative arbitrary-edge instruction. Likewise, the existential theorem could be recovered by deliberately choosing the old connectors, but that would substantively narrow the construction. It does not make the assertion about outputs of the stated procedure true.

Consequences, repair, and subtlety

The numerical budget is unaffected. Here the baseline expression is 5*13/4-1/2=63/4, and the new execution gives 16 after one paid increase. Also rho=1<=11/5 and 16<=163/10. Thus no harmless rounding, constant adjustment, or omitted cost calculation explains the failure. The number 16 is only the objective expression at an infeasible vector; the certificate theorem requires membership. Under the paper's specified suppression, the increased 6-7 edge is replaced with value 1/4, so the reduced singleton cut at 6 again has sum 3/4. This also explains directly why the reduced vertex-cut argument cannot rescue the proof.

Restoring the original own-connector choice for unmatched demands, and its endpoint invariant, repairs this planted defect. A genuinely broader rule would require additional proved restrictions or coordinated changes preserving degree-two equalities and the cost budget. Adding prose asserting feasibility, changing parity notation, or invoking the existing cost count cannot repair the current arbitrary-choice procedure.

The change is subtle enough: all allowed boundary edges have the same immediate local repair effect and cost, the maximum matching remains legitimate, and the substantial counting argument stays intact. The failure depends on tracing the opposite endpoint of an unmatched edge into the later suppression step. The altered overview and detailed rule agree, while a later familiar-looking invariant silently retains the original restriction. It is integrated into a fully presented 13/10 argument rather than placed in an unrelated or externally formalized claim.

Limitations

This is a targeted independent mathematical audit informed by the designated private log, not a blind review. I certify the explicit admissible counterexample and the selected-family failure; I do not claim the ultimate 13/10 theorem is false or that every widened-rule execution fails. Whole-paper reading was used to check scope, definitions, dependencies, and possible rescuing assumptions; it is not a certification of every unrelated theorem or cited result. No external sources or formalization were needed for the finite disproof, and no PDF compilation or visual audit was performed.
