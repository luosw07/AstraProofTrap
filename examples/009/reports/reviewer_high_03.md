REJECT

I found a substantive algebraic error in the proof of the constraint compatibility theorem. An asserted covariant-derivative identity drops a connection term. The identity fails even on smooth compact initial data satisfying all the supersymmetry constraints, and the proof explicitly uses it to deduce the transverse momentum identity. This is a defect in the supplied proof, not a counterexample to the theorem's final statement: the missing term may be repairable, but the inference as written is unjustified.

## Scope of review

I read the complete supplied `paper.tex`, lines 1–5440, including the introduction, all statements and proofs, examples, and bibliography. I used only this version of the paper and direct mathematical calculations. I did not inspect other versions, reports, logs, or external mathematical sources, and did not use a formal proof assistant. The TeX supplied sufficiently explicit formulas for this review; I did not need to inspect the rendered PDF.

The review covered the spinor/coframe correspondence and exterior system; the reduction and explicit integration of the skew-torsion Cauchy problem; uniqueness and the time-independent development; contact and integrable constraint branches; the gerbe and Neveu–Schwarz reductions; the supersymmetry constraints and their developments; the constraint compatibility and propagation arguments; and the leafwise averaging and compact rigidity argument. I checked the principal transformations and selected component calculations rather than independently recomputing every displayed curvature component. Results imported by citation were assessed as stated and used in this paper, without consulting their original sources.

## Substantive issue: a missing connection term in the compatibility proof

**Location:** Theorem `thm:compatibilityflows`, proof, TeX lines 3749–3752, in the displayed equation immediately following the sentence beginning “Taking its … component and using the symmetry of …”. The erroneous identity is subsequently used in the deduction at line 3769. The theorem's claimed conclusion is equation `eq:constraintidentities0`, lines 3660–3663.

Fix the time and abbreviate

\[
U=e_{tu}^{\sharp},\qquad L=e_{tl}^{\sharp},\qquad
c=\iota_U\widehat c_t,\qquad \nabla=\nabla^{h_t},\qquad \Theta=\Theta_t.
\]

The paper correctly obtains

\[
d\bigl(\Theta(U,\cdot)\bigr)=\tfrac12 dc.
\]

It then asserts

\[
(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12 dc(U,L).
\tag{*}
\]

Symmetry of \(\Theta\) does not justify this step: the contracted vector field \(U\) varies. The product rule gives instead

\[
\begin{aligned}
d\bigl(\Theta(U,\cdot)\bigr)(U,L)
={}&(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)\\
&+\Theta(\nabla_UU,L)-\Theta(\nabla_LU,U).
\end{aligned}
\]

The first covariant-derivative formula in Remark `remark:covariantevolution` (line 3542), already used in this proof, implies

\[
\nabla_UU=\Theta(U,U)U-\Theta(U,\cdot)^\sharp-\tfrac12c^\sharp,
\qquad
\nabla_LU=\Theta(U,L)U-\Theta(L,\cdot)^\sharp.
\]

Consequently the two extra terms combine to

\[
\Theta(\nabla_UU,L)-\Theta(\nabla_LU,U)
=-\tfrac12\Theta(c^\sharp,L).
\]

Thus the corrected identity is

\[
\boxed{
(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12 dc(U,L)+\tfrac12\Theta(c^\sharp,L).
}
\]

The omitted term need not vanish under the stated hypotheses.

### Explicit admissible data for which (*) fails

Take a three-torus with angular coordinates \((x,y,z)\), oriented by \(dz\wedge dx\wedge dy\), and put

\[
F(x)=\sin x,\qquad B(z)=\sin z,
\qquad
e_u=e^{F(x)}dz,\quad e_l=e^{B(z)}dx,\quad e_n=dy.
\]

Choose

\[
\mathfrak f=0,\qquad b=0,\qquad f_b=0,
\qquad \phi=e^{iF(x)},\qquad
\varphi_\phi=dF,\qquad \mathfrak c=e_u\wedge dF,
\]

on the trivial bundle gerbe. These satisfy the supersymmetry initial constraints `eq:NSNSsusyconstraintsI` and `eq:NSNSsusyconstraintsII`:

* \(de_u=dF\wedge e_u\).
* \(de_l=e^B B'\,dz\wedge dx\) and \(de_n=0\), so both required wedge products with \(e_u\) vanish.
* \(\mathfrak c=f_b*_\mathfrak e e_u+e_u\wedge\varphi_\phi\).
* The two cross terms in the scalar rotation constraint vanish, so its value is \(f_b=0\).

These are genuine supersymmetry-flow data, not arbitrary tensors. In the paper's explicit evolution, the complete vector field is \(U=e^{-F}\partial_z\), with flow

\[
\Phi_t(x,y,z)=(x,y,z+t e^{-F(x)}).
\]

One can take \(\mathfrak f_t=0\), \(\lambda_t=1\), \(\mathfrak e_t=\Phi_t^*\mathfrak e\), \(\phi_t=\phi\), \(a_t=0\), and \(b_t=t\mathfrak c\). Indeed \(d\mathfrak c=0\) and \(\Phi_t^*\mathfrak c=\mathfrak c\). This is precisely the construction of `eq:NSNSexplicitdevelopment`; its compact initial hypersurface gives the globally hyperbolic development considered by the paper. The following calculation takes place at its initial slice.

Write

\[
U=e^{-F}\partial_z,\qquad L=e^{-B}\partial_x,\qquad N=\partial_y,
\qquad C=F'e^{-B},\qquad K=B'e^{-F}.
\]

The second fundamental form prescribed by the flow is

\[
\Theta=-\tfrac12\mathcal L_U h,
\qquad
[\Theta]_{(U,L,N)}=
\begin{pmatrix}
0&C/2&0\\
C/2&-K&0\\
0&0&0
\end{pmatrix}.
\]

Furthermore \(c=\iota_U\mathfrak c=dF\), so \(dc=0\). The intrinsic connection has

\[
\nabla_UU=-CL,\quad \nabla_UL=CU,
\quad \nabla_LU=KL,\quad \nabla_LL=-KU.
\]

Since \(U(C)=-KC\), direct evaluation yields

\[
(\nabla_U\Theta)(U,L)=-\tfrac32 KC,
\qquad
(\nabla_L\Theta)(U,U)=-KC.
\]

At \(x=z=0\), \(C=K=1\). Thus the left-hand side of (*) is \(-1/2\), whereas its right-hand side is zero. The missing term is exactly \(\tfrac12\Theta(c^\sharp,L)=-1/2\).

### Effect on the claimed conclusions

This is not merely a misspelled symbol or an imprecise explanatory sentence. It is a false mathematical equality used between the two Ricci-component calculations and the final transverse constraint deduction. In particular, the final “direct computation” at line 3769 does not follow from the displayed identities as written. The compatibility theorem in turn is invoked in the evolution-defect and constraint-propagation argument, including lines 4247–4258 and 4324–4328, and underlies the asserted characterization of supersymmetric solutions by combined initial constraints.

I have not shown those final conclusions false. In fact, the example above is consistent with the theorem's final transverse identity: at the indicated point, \(\mathcal W(L)=-1/2\) and \((*\mathcal M)(L)=1\). This distinction matters. The required correction is to retain the missing connection term and recheck the subsequent component algebra and downstream uses, rather than to discard the theorem on the strength of this example. My REJECT verdict concerns the mathematical proof supplied in the current paper.

## Other observations and limitations

The leafwise averaging proof was a particular focus of review. Its use of the closure of leafwise exact forms, orthogonal projection, and convolution by the commuting measure-preserving flows avoids assuming compact leaves or a closed range for the leafwise differential. I found no substantive error in that lemma. I also found the separation into compact-leaf and dense-leaf cases, the choice of a positive basic weight, and the two determinant arguments in the compact rigidity proof mathematically coherent on their stated hypotheses. This does not independently certify all earlier compatibility formulas on which the surrounding results rely.

There are several evident notation slips that I do not count as substantive reasons for rejection: for example, the mismatched curvature symbol in line 910, the undefined \(\beta_t\) in line 3083 where the formula concerns \(\varphi_{\phi_t}\), and the capital \(T\) in the dilaton expression at line 5329 where the time coordinate was introduced as \(t\). The missing connection term identified above is different: it changes the value of a central identity on admissible data.

No additional substantive error is asserted in this report. This is an independent mathematical review, not formal verification of the entire article.
