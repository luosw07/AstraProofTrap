REJECT

The manuscript contains a false covariant-derivative identity in the proof of the constraint-compatibility theorem. This is a missing product-rule term, not a change of notation or a harmless index typo. I give the correct identity and an explicit admissible example below. This finding concerns the proof as written; it does not establish that the compatibility theorem or the compact rigidity theorem is false. The error appears repairable, but the affected calculation must be corrected and checked.

## Material and coverage

I read the entire assigned standalone source, `run_20261114/blind/r8p6/paper.tex`, lines 1–5440, including the introduction, all statements and proofs, examples, and bibliography, in bounded sequential chunks. I used no other paper version, external mathematical source, private record, or other review. The TeX source supplied all mathematical content needed for this review; I did not independently inspect the rendered PDF.

The review covered the contorsion and isotropic-coframe formulation; the globally hyperbolic reduction; the explicit rotated pullback development and its uniqueness; the contact and integrable branches; the bundle-gerbe and Neveu–Schwarz reductions; the supersymmetry flow; the compatibility and propagation arguments; and the leafwise averaging and compact rigidity proof. I checked the main structural transitions and selected tensor calculations, rather than independently expanding every long component calculation. Results quoted from the bibliography were assessed as stated in this manuscript, not verified against their sources. This is not formal verification.

## Substantive issue: a missing covariant product-rule term

**Location.** Proof of Theorem `thm:compatibilityflows`, specifically the paragraph and display at TeX lines 3749–3752, followed by the substitution claimed at lines 3769–3772. The theorem's asserted identity is `eq:constraintidentities0`, lines 3657–3667.

Fix the time and abbreviate

\[
U=e_{tu}^{\sharp},\qquad L=e_{tl}^{\sharp},\qquad
T=\Theta_t,\qquad v=\widehat c_t(e_{tu}).
\]

The equation for the spinor-scale function does indeed give

\[
d(T(U,\cdot))=\tfrac12\,dv.
\]

However, line 3751 concludes from this that

\[
(\nabla_U T)(U,L)-(\nabla_L T)(U,U)
=\tfrac12\,dv(U,L).
\tag{*}
\]

This conclusion neglects the derivative of the vector field inserted into the first argument of (T). The covariant product rule gives

\[
\begin{aligned}
d(T(U,\cdot))(U,L)
={}&(\nabla_U T)(U,L)-(\nabla_L T)(U,U)\\
&+T(\nabla_UU,L)-T(\nabla_LU,U).
\end{aligned}
\]

The manuscript's own formula for \(\nabla^{h_t}e_{tu}\), in Remark `remark:covariantevolution` at line 3542, gives

\[
\nabla_UU=-T(U,\cdot)^{\sharp}+T(U,U)U-\tfrac12v^{\sharp},
\qquad
\nabla_LU=-T(L,\cdot)^{\sharp}+T(U,L)U.
\]

By symmetry of (T), their contribution is

\[
T(\nabla_UU,L)-T(\nabla_LU,U)
=-\tfrac12T(v^{\sharp},L).
\]

Consequently the correct replacement for (*) is

\[
\boxed{
(\nabla_U T)(U,L)-(\nabla_L T)(U,U)
=\tfrac12dv(U,L)+\tfrac12T(v^{\sharp},L).
}
\]

There is no hypothesis in Theorem `thm:compatibilityflows` forcing the additional term to vanish.

### Explicit admissible data exhibiting the discrepancy

On an oriented coordinate domain in \(\mathbb R^3\), take

\[
e_u=e^y\,dx,\qquad e_l=e^x\,dy,\qquad e_n=dz,
\qquad \mathfrak f=0,
\]

and take a trivial gerbe with zero initial curving (b), so (H_b=f_b=0). Set

\[
\phi=e^{iy},\qquad \varphi_\phi=dy,
\qquad \mathfrak c=e_u\wedge dy.
\]

These are admissible supersymmetry data for the equations `eq:NSNSsusyconstraintsI` and `eq:NSNSsusyconstraintsII` (lines 3847–3852):

\[
de_u=dy\wedge e_u,\qquad
de_l\wedge e_u=de_n\wedge e_u=0,
\qquad
\mathfrak c=e_u\wedge\varphi_\phi,
\]

and

\[
(\mathcal L_Ue_n)(L)-(\mathcal L_Ue_l)(e_n^{\sharp})=0=f_b.
\]

They therefore occur at the initial slice of the manuscript's explicit local supersymmetry flow. No equations of motion or Maxwell constraint are required in the hypothesis of the compatibility theorem.

Here

\[
h=e^{2y}dx^2+e^{2x}dy^2+dz^2,
\qquad U=e^{-y}\partial_x,\qquad L=e^{-x}\partial_y,
\]

and the second fundamental form prescribed by the explicit development is

\[
T=-\tfrac12\mathcal L_Uh
=\tfrac12e^y(dx\otimes dy+dy\otimes dx)
-e^{2x-y}dy\otimes dy.
\]

In particular,

\[
T(U,\cdot)=\tfrac12dy,\qquad v=\iota_U\mathfrak c=dy,
\qquad d(T(U,\cdot))=dv=0,
\]

but

\[
T(v^{\sharp},L)=-e^{-x-y}.
\]

Thus the left side of (*) equals \(-\tfrac12e^{-x-y}\), while its printed right side is zero. At (x=y=0), the disagreement is (-1/2=0). For an entirely coordinate-level check at that point, the relevant Christoffel symbols are

\[
\Gamma^y_{xx}=-1,\quad \Gamma^x_{xy}=1,
\quad\Gamma^y_{xy}=1,\quad\Gamma^x_{yy}=-1,
\]

and the displayed (T) gives

\[
(\nabla_{\partial_x}T)_{xy}=-\tfrac32,
\qquad (\nabla_{\partial_y}T)_{xx}=-1.
\]

Their difference is indeed (-1/2).

### Effect on the claimed conclusions

Line 3769 explicitly substitutes the erroneous identity into the comparison of the two mixed Ricci expressions to obtain the transverse momentum–Maxwell relation. The missing term is generally nonzero even on admissible supersymmetry data, so that displayed derivation is invalid as written. The relation is subsequently used in Theorem `thm:susyflowcompatibility`, notably lines 4247–4258 and 4324–4334, and in the resulting initial-data characterization.

This is a substantive error in a proof of a principal result, although it is localized and has an explicit candidate correction. I have not found a counterexample to the theorem's final constraint identity: the counterexample above targets its printed intermediate equality. Correcting the product-rule step and recomputing the final cancellation may restore the theorem. The report should therefore not be read as a claim that the final rigidity conclusion has been disproved.

## Other observations, distinguished from the substantive issue

1. **Global hyperbolicity verification omitted in the maximal-development proof.** In Corollary `cor:timeindependentdevelopment`, item (3), lines 2537–2573, completeness of (q=e^{2\mathfrak f}h_{\mathfrak e}) is used to prove completeness of \(\mathcal X\), and the proof then establishes the maximality/universal property without explicitly first proving that the full product is globally hyperbolic. This is readily supplied: for a causal tangent (a\partial_t+V) of (g=h-e^{-\mathfrak f}dt\odot e_u), with (a>0), the causal inequality gives \(|V|_q\le 2a\). Since (dt) is timelike and (q) is complete, an inextendible causal curve cannot terminate at finite (t); consequently every (t)-slice is Cauchy. I regard this as an omitted short justification, not an additional reason for rejection.

2. **“Conformal transformation” at line 1251.** The assertion that vanishing rank-one class makes the connection preserve a “conformal transformation of every representative” should refer to the null-rotation gauge transformation `eq:equivalencerelation`, with potentials supplied by `eq:kapparhogauge`. A conformal rescaling is generally insufficient: preserving a rescaled parallel (u) already forces its scalar factor to be constant, and cannot remove a nonzero exact \(\kappa\). The intended gauge argument and trivial-holonomy conclusion are clear from the surrounding formulas. This is a terminology correction, not the principal proof error above.

3. **Harmless notation slips.** Examples include \(\mathcal R^o_{x,y}\) where \(\mathcal R^g_{X,Y}\) is intended at line 910, the degree-inconsistent first line of the Lie-derivative expansion at line 1162 (the following lines make the intended expansion clear), and (T+z) instead of (t+z) in the final example at line 5329. These do not underpin my verdict.

## Assessment of the remaining main arguments

The explicit flow integration and null-current straightening give a coherent mechanism for the germ's uniqueness, including nonuniform flow neighborhoods. The contact/integrable branching and reconstruction formulas are consistent with the bracket description. The leafwise averaging proof does not require compact individual leaves: its (L^2) projection and leafwise smoothing argument address that difficulty directly. In the compact rigidity proof, the distinction between compact fibers and dense leaves, the choice of positive basic weight, and the determinant pairing for the final trace-free curvature matrix form a coherent argument. I found no separate substantive error in those portions during this review.

My verdict is nevertheless REJECT for the current mathematical text because the false identity at line 3751 is actually used in proving a principal compatibility result. A revised proof should include the missing term and verify its cancellation before the downstream claims can be accepted on the basis of the written argument.
