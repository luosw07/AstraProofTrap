VERDICT: REJECT

The manuscript presents an ambitious proof of the unramified quantum geometric Langlands equivalence at every irrational complex level, for the actual global forms. Its final categorical assembly is logically consistent assuming the stated localization, period, and Plancherel inputs. I found a concrete error in the construction of infinitesimal transport of jet representations, at the point where the manuscript claims compatibility with induction and higher crystal coherences. I also found a false global identification in the finite Whittaker test. The first issue concerns a structure used throughout the moving-point argument; the second has a fairly direct local repair.

**Scope and checks.** I read the complete current `paper.tex`, including all proofs and the bibliography (lines 1–9178). I used only the supplied manuscript and local mathematical calculations. External references were not consulted; statements imported from those references were assessed in the form and scope specified by the manuscript. The principal checks included the shifted-level and determinant conventions, the inertia/HN cutoff and its use with Levi subgroups, the pseudo-identity induction, the distinction between finite-stage and filtered-colimit deformation, the logarithm/weight argument, the collision extension using the degree-three unit gap, the finite-level period normalizations, the Ran insertion comparisons, and the domains and compositions in the final two-inverse argument. In particular, the determinant cancellation in (T9)–(T10) and the formal inverse calculations in the last section check out. The following objections are mathematical issues in the supplied arguments, rather than objections to the scale or novelty of the theorem.

**1. The prescribed transport of jet-current action matrices does not preserve the Lie relations at collisions.**

Location: Section 7, “Loop categories over moving divisors,” the initial finite-jet convention at TeX lines 3887–3891 and Proposition `loop:crystal`, specifically lines 4333–4342. The locating passages are:

> “coefficient transport is base-linear: it retains the \(a_{rj}\) and uses the lifted divisor equation for \(u\)”

and, in the proof of the proposition,

> “Obtain the lifted inducing representations … by retaining their jet-current action matrices in the monic coefficient bases, and then restrict to the common depth. The PBW and group-cobar constructions therefore use identical coefficient diagrams … This supplies the higher cocycle compatibilities.”

The monic-basis correspondence is a correspondence of underlying modules, not of jet algebras. Consequently, retaining action matrices through that correspondence need not even produce a representation. This problem occurs for two infinitesimally close *tuples*, including precisely the collision situation allowed in the proposition.

Let \(R=\mathbb C[\epsilon]/(\epsilon^2)\). Compare the two marked tuples \((0,0)\) and \((0,\epsilon)\) on the affine line. Their divisor equations are

\[
 P(z)=z^2,\qquad Q(z)=z(z-\epsilon)=z^2-\epsilon z.
\]

At jet order one, the two coefficient algebras have the common free module basis \(1,z\), but different multiplication:

\[
 A_P=R[z]/(z^2),\qquad A_Q=R[z]/(z^2-\epsilon z).
\]

The prescribed coefficient correspondence fixes \(1,z\). It cannot be an algebra homomorphism: \(z^2=0\) on the first side, whereas \(z^2=\epsilon z\ne0\) on the second.

For an explicit permitted inducing representation, take \(\mathfrak g=\mathfrak{sl}_2\), with \([e,f]=h\), and the adjoint representation

\[
 V=\mathfrak{sl}_2\otimes A_P
\]

of the algebraic jet group \(\mathrm{SL}_2(A_P)\). It is a vector bundle over \(R\), as required for the generators in (L2). Write \(N_x\) for the matrix of \(x\otimes z\) in this representation. Then

\[
 [N_e,N_f]=0,
 \qquad N_h(e\otimes1)=2e\otimes z.
\]

If the matrices are retained in the \(Q\)-monic basis, the new Lie relation instead requires

\[
 [N_e,N_f]
   =\rho([e\otimes z,f\otimes z])
   =\epsilon N_h.
\]

The right-hand side is nonzero, since it sends \(e\otimes1\) to \(2\epsilon e\otimes z\). Thus this assignment violates the representation relations. The central extension causes no modification of this example: these are regular arc currents, where the stated splitting applies.

Passing to a deeper jet quotient does not make the *retained-matrix prescription* valid. A correct pullback of the old action through the identity on the common completed ring must, for example, assign to the new current \(xQ\) the matrix

\[
 \rho(xQ)=\rho(xz^2-\epsilon xz)=-\epsilon N_x,
\]

rather than the zero matrix of the old current \(xP\). These are exactly the nilpotent correction terms discarded by retaining the monic-basis matrices. They remain necessary at a common deeper depth.

The cofinality of the ideals, and the resulting identification of the *full* completed rings at fixed \(z\), are valid observations. They provide a promising alternative construction. They do not justify the subsequent assertion that the proposed lifted representations and their PBW/cobar coefficient diagrams are identical. Likewise, equality of essential images after restriction, established earlier in the proof, does not by itself establish the claimed compatibility of the particular induction functors and their higher comparison maps.

**Consequence.** Proposition `loop:crystal` has not established the stated induction-compatible crystal coherences by the construction given. Those coherences are subsequently used in the strong loop action, the relative Skryabin comparison, the common target, the collision comparison, and the crystalline period map. Fibrewise equivalences do not supply this missing comparison of functors on infinitesimal multiple diagonals.

**Possible repair.** Replace the coefficient-retention construction by actual algebra maps between cofinal jet presentations induced by the identity of the absolute completed curve. Transport representations through these maps, retaining all nilpotent correction terms. Then prove, on those corrected diagrams, the comparisons of PBW induction and group-cobar complexes, their independence of common depth, and their composition on multiple infinitesimal diagonals. The two-point example above is a necessary elementary check for such a replacement. Merely describing the original coefficient correspondence as base-linear is insufficient for transporting Lie or group representations.

**2. The diagonal coefficient of the finite Whittaker-test composite is not generally a constant complex on the flag variety.**

Location: Section 6, Proposition `planch:finite-test`, the final diagonal calculation, TeX lines 3259–3277. The locating passage is:

> “After fixing a flag and a representative of it, the remaining integral is the de Rham integral of the dualizing object on \(N\times B^-\). Its cohomology is nonzero and varies constantly along the diagonal. The composite therefore acts as the identity tensored with a nonzero complex of vector spaces …”

This inference loses the gluing of the representatives of the flag. Even with constant cohomology local systems, the derived direct image can have a nontrivial extension between them.

Work in the manuscript's local model over \(Y(K^d)\), and put \(p:H\to H/B^-\). On the diagonal, the two unipotent coordinates coincide, and the phases and twists cancel, as the manuscript says. The remaining incidence is parametrized by \((v,n)\in H\times N\), with flag \(vnB^-\). The change of variables \((v,n)\mapsto(vn,n)\) identifies its map to the flag variety with \(p\) times the projection from \(N\). Consequently its diagonal coefficient is, up to the fixed normalization, \(p_*\omega_H\) tensored with the cohomology of the contractible unipotent factor. It is not in general the constant complex having the fibre cohomology of \(B^-\).

There is an elementary counterexample with \(H=\mathrm{SL}_2\). In ordinary constructible normalization, a splitting

\[
 Rp_*\mathbb C_{\mathrm{SL}_2}
 \simeq \mathbb C_{\mathbb P^1}\otimes R\Gamma(B^-,\mathbb C)
\]

would imply

\[
 H^*(\mathrm{SL}_2,\mathbb C)
 \simeq H^*(\mathbb P^1,\mathbb C)\otimes H^*(\mathbb G_m,\mathbb C).
\]

The left side is one-dimensional in degrees 0 and 3 and zero otherwise. The right side is one-dimensional in each of degrees 0, 1, 2, and 3. In the actual pushforward, the nonzero Chern/transgression class of the torus torsor accounts for the missing two classes. Shifts, dualizing normalization, and the contractible \(N\) factor do not remove this contradiction to the asserted global splitting.

**Consequence and repair.** The quoted identity for the composite kernel is false. The intended conservativity conclusion can nevertheless be recovered locally: trivialize \(H\to H/B^-\) on a flag-variety open cover, where the diagonal coefficient really is the constant fibre complex, and use its nonzero cohomology to detect vanishing there. This also works with arbitrary D-module inputs and spectators. The proof should make this local argument and keep the actual globally glued diagonal coefficient, rather than assert a global tensor-by-a-vector-space identity.

**Typographical issues.** Neither objection above is typographical or a matter of an overall sign or shift. I have not included ordinary typographical corrections as grounds for the verdict.

The manuscript carefully separates several genuine difficulties—especially finite versus filtered deformation and pointwise versus family comparisons—and the final formal quotient argument is clear. The present verdict rests on the explicit failures above, principally the representation-transport step used to claim the required crystal coherences. A corrected manuscript needs to supply that coherent construction before the moving-point and global conclusions are established.
