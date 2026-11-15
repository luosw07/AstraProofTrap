REJECT

I found a substantive error in a covariant-derivative identity used in the proof of the constraint compatibility theorem. The error is a missing, generally nonzero quadratic term. I give its correction and an explicit admissible example below. This is a rejection of the argument as written, not a claim that the main theorem or the compact rigidity conclusion is false: the identified calculation appears repairable.

## Scope and input

I read the complete supplied `paper.tex`, lines 1–5440, including its introduction, all mathematical sections, proofs, examples, and bibliography. My mathematical input was only this supplied version. I did not consult other versions, external mathematical sources, other reports, or other agents, and did not use a formal proof assistant. Locations below refer to the supplied TeX source; theorem labels are included to avoid ambiguity about numbering.

## Substantive error: a moving-frame term is omitted

**Location:** Theorem `thm:compatibilityflows`, proof, lines 3749–3752, specifically the displayed equality at line 3751. The surrounding claim is that the spatial constraints imply

\[
(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12\,dC(U,L),
\]

where, at a fixed time, \(U=e_{tu}^{\sharp}\), \(L=e_{tl}^{\sharp}\), and \(C=\widehat c_t(U,\cdot)\). I suppress the time subscripts and write \(\nabla=\nabla^{h_t}\).

This equality is false. The equation for \(d\mathfrak a_t\) gives

\[
d(\Theta(U,\cdot))=\tfrac12 dC.
\]

However, \(U\) is a variable vector field. Differentiating the one-form \(\Theta(U,\cdot)\) therefore gives

\[
\begin{aligned}
d(\Theta(U,\cdot))(U,L)
={}&(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)\\
&+\Theta(\nabla_U U,L)-\Theta(\nabla_L U,U).
\end{aligned}
\]

The paper's own covariant formula in Remark `remark:covariantevolution`, line 3542, implies

\[
\nabla_XU=-\Theta(X,\cdot)^{\sharp}
+\Theta(U,X)U-\tfrac12 e_{tu}(X)C^{\sharp}.
\]

Using the symmetry of \(\Theta\), the last two terms in the differentiated expression combine to

\[
\Theta(\nabla_U U,L)-\Theta(\nabla_L U,U)
=-\tfrac12\Theta(C^{\sharp},L).
\]

Thus the correct identity is

\[
\boxed{
(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12 dC(U,L)+\tfrac12\Theta(C^{\sharp},L).
}
\]

The added term is not forced to vanish by the supersymmetry constraints.

### Explicit admissible example

On an open subset of \(\mathbb R^3\), with coordinates \((x,y,z)\), take

\[
e_u=e^x dz,\qquad e_l=e^z dx,\qquad e_n=dy,
\qquad \mathfrak f=0,
\]

and use the trivial gerbe with initial curving \(b=0\), circle-valued dilaton \(\phi=e^{ix}\), and

\[
\varphi_\phi=dx,\qquad f_b=0,\qquad
\mathfrak c=e^x dz\wedge dx.
\]

These satisfy all supersymmetric initial constraints `eq:NSNSsusyconstraintsI` and `eq:NSNSsusyconstraintsII`:

* \(de_u=dx\wedge e_u=\varphi_\phi\wedge e_u\).
* \(de_l\wedge e_u=de_n\wedge e_u=0\).
* \(\mathfrak c=e_u\wedge\varphi_\phi\).
* With \(U=e^{-x}\partial_z\), both mixed evaluations in the scalar screen-rotation condition vanish, so their difference is \(0=f_b\).

Consequently this example is within the class used by the compatibility argument; it also has the explicit local supersymmetry development supplied earlier in the paper. No field equations or Maxwell constraint are required by Theorem `thm:compatibilityflows`.

At the initial slice, put \(a=e^{-x}\), \(c=e^{-z}\). The orthonormal frame is

\[
U=a\partial_z,\qquad L=c\partial_x,\qquad N=\partial_y,
\]

and

\[
h=e^{2x}dz^2+e^{2z}dx^2+dy^2,\qquad
\Theta=-\tfrac12\mathcal L_Uh.
\]

Its relevant components are

\[
\Theta(U,U)=0,\qquad \Theta(U,L)=\tfrac c2,
\qquad \Theta(L,L)=-a,
\]

with all components involving \(N\) zero. Moreover,

\[
C=\iota_U\mathfrak c=dx=c e_l,\qquad dC=0,
\qquad \Theta(C^{\sharp},L)=-ac.
\]

For a direct check, the frame connection is

\[
\nabla_UU=-cL,\quad \nabla_UL=cU,
\quad \nabla_LU=aL,\quad \nabla_LL=-aU.
\]

It gives

\[
(\nabla_U\Theta)(U,L)=-\tfrac32 ac,
\qquad
(\nabla_L\Theta)(U,U)=-ac.
\]

The left-hand side of line 3751 is therefore
\(-\tfrac12ac=-\tfrac12e^{-x-z}\), whereas its printed right-hand side is zero. This is a nonzero discrepancy on the entire coordinate domain.

### Effect on the claimed conclusions

The omitted term is used immediately afterwards: line 3769 says that substituting the preceding identities gives the transverse momentum/Maxwell compatibility relation. That substitution is invalid with the printed line 3751. In particular, the right-hand Ricci formula at lines 3744–3745 already contains \(\tfrac12\Theta(C^{\sharp},L)\); it is the additional term in the corrected derivative identity that cancels it. It cannot simply be discarded.

The compatibility identity `eq:constraintidentities0` is then used in Theorem `thm:susyflowcompatibility` to reduce the evolution defects and propagate the remaining constraints. Thus this is an error in a central proof, rather than an irrelevant numerical typo.

I do **not** infer that `eq:constraintidentities0` is false. In fact, retaining the missing term restores the relevant cancellation, and the example above satisfies the final transverse compatibility identity. The necessary repair is to replace line 3751 by the corrected formula and carry out the subsequent substitution with that term included. The report's negative verdict concerns the supplied proof as written; it does not provide a counterexample to either compatibility theorem or compact rigidity.

## Other observations, distinguished from the substantive finding

The following are readily interpretable notation/typography slips and are not independent grounds for rejection:

* Line 1162, in the proof of `thm:existencenullcoframeII`, writes products involving \(du\) and \(dv\) where the Cartan calculation should involve \((\iota_u du)\odot v+u\odot(\iota_u dv)\). The next expanded line makes the intended calculation identifiable.
* Line 3083, in `lemma:hyperbolicderivatives`, contains an undefined \(\beta_t\) in the formula for \(\nabla^g\varphi_{\phi_t}\); the intended argument of \(\Theta_t\) is \(\varphi_{\phi_t}^{\sharp}\).
* Line 5329 uses \(T\) in the last example's dilaton although the specified time coordinate is \(t\).

The proof of item (3) of `cor:timeindependentdevelopment` would also benefit from explicitly establishing global hyperbolicity before proving maximality. This omission has a short repair under the stated hypothesis: for \(g=h_{\mathfrak e}-e^{-\mathfrak f}dt\odot e_u\), a causal curve parametrized by \(t\) has spatial speed at most 2 in \(q=e^{2\mathfrak f}h_{\mathfrak e}\). Completeness of \(q\) prevents spatial escape in bounded time, while \(dt\) is timelike. Thus every inextendible causal curve meets every time slice. I do not regard this easily supplied step as a counterexample or a separate substantive error.

## Coverage and limitations

I checked the structure of the torsion/coframe correspondence, the reduction to evolution and constraint equations, the normalized pullback evolution and constant-rotation obstruction, local uniqueness through the null-current flow, the time-independent developments, and the contact/integrable initial-data descriptions. I followed the gerbe reduction, the bosonic constraint formulation, supersymmetric specialization, compatibility and propagation arguments, and the entire compact rigidity proof.

In particular, I examined the leafwise averaging lemma's use of the closure of exact forms, its unitary leafwise smoothing argument, and the weighted integral identities and curvature matrix in compact rigidity. I found no independent substantive error in those arguments. The proof works with ambient \(L^2\) integration and does not incorrectly assume compact leaves. The compact-leaf versus dense-leaf discussion supplies the smooth basic projection needed later in the proof.

This was a mathematical review, not a formal verification. I did not independently rederive every long curvature-component expansion, and I did not verify the contents of externally cited results. Their applications were assessed from the hypotheses and descriptions in the supplied manuscript. The explicit contradiction to line 3751, however, is a local calculation using only the paper's own definitions and does not depend on those external results.
