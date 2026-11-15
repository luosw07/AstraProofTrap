# Tricker report

## 1. The revised construction and its first failure

Section 7.1, output lines 3887-3891, fixes a coefficient comparison on finite jets. For a monic divisor equation \(P\) of degree \(m\), the coefficient algebra of the order-\(n\) jet has the free basis
\[
 z^rP^j,\qquad 0\le r<m,\quad 0\le j<n.
\]
For a lifted equation \(Q\), the new convention retains the coefficients and replaces this basis by \(z^rQ^j\). This defines a perfectly valid base-linear isomorphism \(\beta_{P,Q}\) of the underlying finite free modules. It preserves the unit, truncations, and ranks; its inverse is the reverse coefficient comparison.

The error occurs in the proof of Proposition 7.3 (`loop:crystal`), at output lines 4336-4338: the manuscript **obtains the lifted inducing representations by retaining their jet-current action matrices in those coefficient bases**, and only then restricts to a common depth. Lines 4339-4340 infer that the PBW and group-cobar coefficient diagrams agree and that these comparisons intertwine induction.

An action matrix can be transported this way only if the change of coefficient basis preserves the required Lie relations, or the given representation annihilates every resulting defect. Monic presentations supply a linear basis; the multiplication structure constants depend on the divisor equation. The example below gives an allowed inducing representation that detects the change.

The construction uses an existing linear coefficient presentation and fails when that presentation is used for representation transport.

## 2. Admissible curve, group, family, and inducing input

Take \(X=\mathbb P^1_\mathbb C\), the theta characteristic \(\mathcal O(-1)\), the simple group \(G=\mathrm{SL}_2\) with its standard pinning, and \(c=-\sqrt2\). All are allowed by the manuscript. Trivialize its fixed \(P_0\) on the affine coordinate chart \(\mathbb A^1_z\).

Let the smooth affine parameter scheme be \(S=\mathbb A^1_t\), with the two marking maps \(t\) and \(-t\). On the second infinitesimal diagonal use
\[
 B=\mathbb C[t,\epsilon]/(\epsilon^3),
 \qquad p_1^*t=t,\qquad p_2^*t=t+\epsilon.
\]
It is finite free of rank three over either projection, with nilpotent ideal \(I=(\epsilon)\). The pulled-back graph sums have equations
\[
 P=z^2-t^2,\qquad Q=z^2-(t+\epsilon)^2.
\tag{1}
\]
These are monic degree-two graph divisors, finite flat over the comparison base, and agree modulo \(I\). Their completion ideals are cofinal, exactly as the unchanged proof establishes.

At the first jet stage, put
\[
 A_P=B[z]/(P),\qquad A_Q=B[z]/(Q).
\]
Both are free on \(1,z\), and the newly prescribed map \(\beta:A_P\to A_Q\) fixes these two basis vectors. The jet Lie algebras are
\[
 \mathfrak j_P=\mathfrak{sl}_2\otimes A_P,
 \qquad \mathfrak j_Q=\mathfrak{sl}_2\otimes A_Q,
\]
with \([x\otimes a,y\otimes b]=[x,y]\otimes ab\).

There is an actual inducing input over the original smooth base: the adjoint representation of the first jet group
\(\mathrm{SL}_2(\mathbb C[t,z]/(z^2-t^2))\). Its underlying vector bundle is
\(V=\mathfrak{sl}_2\otimes\mathbb C[t,z]/(z^2-t^2)\), free of rank six. Here the group notation denotes restriction of scalars of \(\mathrm{SL}_2\) along the finite flat divisor algebra. Pulling this representation back through the arc-jet quotient gives an algebraic arc representation, so it is one of the vector-bundle inputs \(V\) allowed in equation (7.2), `eq:L2` (output line 4150).

The finite flat diagonal comparisons of Proposition 7.2 permit its base extension to \(B\). On the source lift this is the genuine adjoint representation \(\rho_P=\operatorname{ad}_{\mathfrak j_P}\). The source is therefore an actual legal representation, not merely an arbitrarily chosen list of matrices.

The affine extension splits on the regular arcs. For the particular polynomial currents below its residue cocycle is also directly zero. Consequently the prescribed irrational central level and the determinant twist do not change these jet-current relations.

## 3. The coefficient map does not preserve the bracket

Use the pinned generators \(e,h,f\) of \(\mathfrak{sl}_2\), with
\[
 [e,f]=h,\qquad [h,e]=2e,\qquad [h,f]=-2f.
\]
The coefficient map extends linearly to the current Lie modules and fixes the six basis vectors
\[
 e,h,f,ez,hz,fz.
\]
In the two current algebras,
\[
 [ez,fz]_P=t^2h,
 \qquad [ez,fz]_Q=(t+\epsilon)^2h.
\]
Thus
\[
 [\beta(ez),\beta(fz)]_Q-\beta([ez,fz]_P)
   =(2t\epsilon+\epsilon^2)h.
\tag{2}
\]
This is a nonzero structure-constant defect on the permitted formal-diagonal chart.

In particular, specialize the defining equations to the closed collision fiber \(t=0\). Write \(R=\mathbb C[\epsilon]/(\epsilon^3)\); then
\[
 A_P=R[z]/z^2,
 \qquad A_Q=R[z]/(z^2-\epsilon^2).
\tag{3}
\]
The map remains a linear isomorphism fixing \(1,z\), but the bracket defect is \(\epsilon^2h\ne0\). Specialization here is applied to an asserted equality of matrices in finite free modules. Every equality over \(B\) would remain an equality after this specialization, with no flatness requirement for that inference.

## 4. Copying an allowed action fails to produce a representation

The rule at lines 4336-4338 prescribes the following action on the underlying source vector bundle:
\[
 \rho_Q^{\mathrm{copy}}(x)
   =\rho_P(\beta^{-1}x).
\tag{4}
\]
This is exactly what retaining the matrices indexed by the monic coefficient basis means. It is a well-defined linear assignment of operators. It must satisfy the Lie representation identity to be the asserted lifted inducing representation.

On the collision fiber, \(\rho_P(ez)\) and \(\rho_P(fz)\) send the degree-zero summand of \(\mathfrak{sl}_2\otimes R[z]/z^2\) into the \(z\)-summand and kill the \(z\)-summand. Their products in either order are zero. Therefore
\[
 [\rho_Q^{\mathrm{copy}}(ez),\rho_Q^{\mathrm{copy}}(fz)]=0.
\]
However, the required target bracket is \([ez,fz]_Q=\epsilon^2h\), so
\[
 \rho_Q^{\mathrm{copy}}([ez,fz]_Q)(e)
   =\epsilon^2\rho_P(h)(e)
   =2\epsilon^2e\ne0.
\tag{5}
\]
The nonzero conclusion follows because the vector bundle is free over \(R\) and \(\epsilon^2\ne0\). Equations (4)-(5) prove that the prescribed object is not even a Lie algebra representation. It therefore cannot be the algebraic jet-group representation needed for the inducing construction.

The same calculation tests the statement about identical PBW diagrams. The source relation
\((ez)(fz)-(fz)(ez)=0\) in its enveloping algebra is sent by the coefficient rule to an expression equal to \(\epsilon^2h\) in the target enveloping algebra. By PBW that target element is nonzero. The linear map on generators consequently does not descend to the enveloping-algebra map that the induction comparison requires. On the associated graded, this bracket correction disappears, which explains why the vector-bundle and PBW-basis checks alone pass.

This is one mechanism: forgetting the changing multiplication structure constants when transporting the coefficient presentation. The failed representation and the failed enveloping relation are two manifestations of it.

## 5. Common cases and exact failure condition

The coefficient transport is valid as a structural map in the following meaningful cases.

- If each separated cluster has a single graph, \(m=1\); its finite jets are truncated polynomials in \(P\), and replacing \(P\) by \(Q\) is an algebra isomorphism. The induced current and representation transport is then valid.
- If the divisor equation is unchanged, the coefficient comparison is the identity, at every jet order.
- On the displayed collision fiber modulo \(\epsilon^2\), both first-jet equations are \(z^2=0\). The copied representation satisfies the relation used above. On the reduced fiber all the structures agree as well.

The precise obstruction in (1) is that the coefficient comparison leaves the basis \(1,z\) fixed while the product \(z\cdot z\) changes by \(2t\epsilon+\epsilon^2\). The chosen adjoint representation detects that change through the nonzero adjoint action of \(h\). It is visible on the collision fiber at second infinitesimal order.

As the previous checker emphasized, **first-order success is only a claim about this collision fiber**. On the whole smooth-base family, (2) contains the term \(2t\epsilon h\); copying the matrices can already fail at first order. The present certificate and metadata retain that distinction.

Routine unit, inverse, rank, residue-field, and associated-graded checks test the legitimate underlying linear comparison. Detecting the fault requires comparing the actual multiplication or Lie bracket before transporting a representation, and retaining the nilpotent coefficient that the chosen legal representation sees.

## 6. Downstream scope, taxonomy, and repair

The first structural failure is the instruction at lines 4336-4338 to obtain lifted inducing representations by copying their matrices. The coefficient convention at lines 3887-3891 is itself legitimate as linear algebra. The inference about PBW/group-cobar diagrams at lines 4339-4340 uses the same false structural compatibility. Refinement is ordered after obtaining the lifted representation; it does not supply that missing representation. Recomputing the correct action after a common-depth restriction would be a replacement for the stated rule.

The affected comparison is in Proposition 7.3's construction of coherent parameter transport. Its later consumers include the strong loop action (`loop:strong-action`, line 4360), relative Skryabin comparison (`walg:relative-skryabin`, line 5257), common Whittaker target (`walg:common-target`, line 5433), and parameter-compatible localization (`loc:construction`, line 6592). The original cofinality and common-depth existence arguments are intact; the failure concerns the newly specified comparison on inducing presentations and its compatibility with induction.

The proposed direct types are **DEF** and **CONV**. DEF records the failed structural validity of the lifted representation. CONV records the false claim that the defining coefficient diagrams for induction agree: expansion of the bracket and its action gives (2) and (5). No separate arbitrary-choice or existence-sufficiency generalization is introduced, so no G12 subtype is proposed. The exact four-rule audit is in `error-type.json`.

A repair uses the canonical fixed-\(z\) identification of the full completed/Laurent algebras, actual inclusions into common deeper congruences, and their genuine restriction maps. If monic bases are retained for notation, the action matrices must be rewritten using the new multiplication table rather than copied. Restoring the original comparison paragraph and removing the new transport convention is the exact baseline repair, recorded in `edits.json` and `baseline-to-output.diff`.

`verification.py` checks both genuine rank-six adjoint representations and the failed copied one using exact arithmetic over \(\mathbb Q[t,\epsilon]/\epsilon^3\). It also verifies the complete manuscript edits, restoration and unchanged structural labels. Results are in `verification-results.json`.
