REJECT

I found a substantive, explicitly testable error in the written proof of Theorem 4.30: a covariant differentiation formula omits a generally nonzero term. The omitted term occurs in the argument for the transverse momentum/Maxwell constraint identity, which is subsequently used in the compatibility theorem. This is a repairable proof error; my example disproves the displayed intermediate identity, not the final statement of Theorem 4.30 or the compact rigidity theorem.

## Scope and method

The mathematical inputs to this review were exclusively the assigned `run_20261114/blind/r8p6/paper.tex` and its accompanying `paper.pdf`. I read the entire TeX file, including all statements, proofs, examples, and bibliography, in bounded chunks (lines 1-5440). I also consulted the 65-page PDF, including visual checks of the main existence/uniqueness argument, the erroneous calculation on page 46, and the complete leafwise averaging and compact rigidity argument on pages 55-61. The error below is present in both the source and the rendered PDF.

I did not inspect another version, other reviews, logs, or experiment files, consult another agent, or use a formal proof assistant. I used an elementary exact rational tensor calculation to check the numerical evaluation below. I did not retrieve or independently verify the external works cited by the paper. In particular, my review of arguments invoking the spinor-square correspondence and the classification of locally free R^2 actions is conditional on the cited results having their stated hypotheses and conclusions. This is a mathematical review, not formal verification of every component calculation.

## 1. Missing frame-derivative term in Theorem 4.30

**Location:** Proof of Theorem 4.30 (`thm:compatibilityflows`), TeX lines 3749-3752, especially line 3751; PDF page 46, first displayed equation. The subsequent use is at TeX line 3769. The theorem's claimed vector identity is equation (66), `eq:constraintidentities0`, at TeX lines 3660-3663.

Fix a time and abbreviate

\[
U=e_{tu}^{\sharp},\qquad L=e_{tl}^{\sharp},\qquad
B=\Theta_t,\qquad c=\widehat c_t(e_{tu}),\qquad C=c^{\sharp}.
\]

The paper correctly has

\[
d(B(U,\cdot))=\tfrac12 dc.
\]

It then asserts

\[
(\nabla_U B)(U,L)-(\nabla_L B)(U,U)
=\tfrac12 dc(U,L).
\tag{*}
\]

This inference does not account for differentiation of the vector field U inside the contracted one-form B(U,·). The actual differentiation formula is

\[
\begin{aligned}
d(B(U,\cdot))(U,L)
={}&(\nabla_U B)(U,L)-(\nabla_L B)(U,U)\\
&+B(\nabla_U U,L)-B(\nabla_L U,U).
\end{aligned}
\]

The paper's own connection formula in Remark 4.28 (`remark:covariantevolution`), TeX line 3542, gives

\[
\nabla_X U=-B^{\sharp}X+B(U,X)U-\tfrac12 e_{tu}(X)C.
\]

Using symmetry of B, one obtains

\[
B(\nabla_U U,L)-B(\nabla_L U,U)
=-\tfrac12 B(C,L).
\]

Consequently, the correct version of (*) is

\[
\boxed{
(\nabla_U B)(U,L)-(\nabla_L B)(U,U)
=\tfrac12 dc(U,L)+\tfrac12 B(C,L).
}
\]

The extra term is not constrained to vanish by supersymmetry. In particular, neither symmetry of B nor closedness of the dilaton curvature removes it.

### An explicit admissible example

On a coordinate three-manifold with coordinates (z,x,y), choose

\[
e_u=dz,\qquad e_l=e^z dx,\qquad e_n=dy,
\qquad \mathfrak f=-x,
\]

and take a flat initial curving, together with

\[
f_b=0,\qquad \phi=e^{ix},\qquad
\varphi_\phi=dx,\qquad \mathfrak c=dz\wedge dx.
\]

These data satisfy the supersymmetry constraints (74)-(75), `eq:NSNSsusyconstraintsI` and `eq:NSNSsusyconstraintsII`:

\[
d(e^{-\mathfrak f}e_u)=d(e^x dz)
=dx\wedge e^x dz,
\qquad
de_l=e^z dz\wedge dx,\qquad de_n=0,
\]

and the scalar screen-rotation expression is zero. Also
\(\mathfrak c=e_u\wedge\varphi_\phi\), as required when \(f_b=0\).
The explicit evolution uses \(\mathcal X=e^x\partial_z\) and
\(\Phi_s(z,x,y)=(z+s e^x,x,y)\); thus this is not an arbitrary tensor assignment unrelated to the supersymmetry equations. The issue is local and remains on a globally hyperbolic restriction of the constructed development.

The initial metric and second fundamental form are

\[
h=dz^2+e^{2z}dx^2+dy^2,
\qquad
B=-e^{2z}dx\otimes dx-\tfrac12(dx\otimes dz+dz\otimes dx).
\]

Here \(U=\partial_z\), \(L=e^{-z}\partial_x\), and

\[
c=\iota_U\mathfrak c=dx,\qquad dc=0,
\qquad B(U,\cdot)=-\tfrac12 dx.
\]

In particular, the premise \(d(B(U,\cdot))=\tfrac12dc\) holds exactly. But at z=0 the nonzero Christoffel symbols needed for (*) are

\[
\Gamma^z_{xx}=-1,\qquad
\Gamma^x_{zx}=\Gamma^x_{xz}=1.
\]

They give

\[
(\nabla_U B)(U,L)=\tfrac12,
\qquad
(\nabla_L B)(U,U)=1.
\]

The printed left-hand side is therefore \(-\tfrac12\), while its printed right-hand side is zero. The missing term is precisely

\[
\tfrac12 B(C,L)=-\tfrac12
\]

at that point.

### Effect on the argument

This is a mathematical failure in a calculation used to prove the transverse part of (66), rather than an undefined symbol or harmless relabeling. The two Ricci expressions immediately preceding it are equated and this identity is substituted to obtain
\(\mathcal W_t(e_{tl}^{\sharp})=-\tfrac12(*\mathcal M_t)(e_{tl}^{\sharp})\).
With the printed identity, that substitution is invalid. Theorem 4.35 subsequently invokes Theorem 4.30 in its passage from the evolution defects to vanishing constraints (for example TeX lines 4247-4258 and 4324-4328).

The correct additional term supplies a plausible local repair, and the final compatibility identity itself is consistent with the explicit example above. I therefore do **not** claim a counterexample to equation (66), the existence theorems, or compact rigidity. The verdict concerns the current paper's proof: the omitted term and the dependent algebra need correction and verification before that proof can be accepted as written.

## 2. A global-hyperbolicity step that should be made explicit

**Location:** Corollary 3.27 (`cor:timeindependentdevelopment`), item (3), TeX line 2441; its proof, TeX lines 2537-2573, especially the transition at line 2541.

The proof establishes completeness of the spatial flow from completeness of
\(q=e^{2\mathfrak f}h_{\mathfrak e}\), then proceeds to maximality without explicitly showing that the entire stationary product is globally hyperbolic. Maximality is not a substitute for this prerequisite. However, this omission has a short direct completion, so I do not count it as a separate substantive error.

For

\[
g=h_{\mathfrak e}-e^{-\mathfrak f}dt\odot e_u,
\qquad \vartheta=e^{\mathfrak f}e_u,
\]

we have \(|\vartheta|_q=1\) and

\[
e^{2\mathfrak f}g=q-dt\odot\vartheta.
\]

The covector dt is timelike. A causal curve parameterized by increasing t satisfies

\[
|\dot p|_q^2\le 2\vartheta(\dot p)\le 2|\dot p|_q,
\]

so \(|\dot p|_q\le2\). If t had a finite endpoint along an inextendible causal curve, completeness of q would give a limit for p and hence an endpoint in the product, a contradiction. Every inextendible causal curve therefore crosses each t-slice exactly once. This establishes the missing global hyperbolicity assertion and permits the subsequent maximality argument to proceed.

## 3. Minor errors, distinct from the substantive finding

- **TeX line 961:** the kernel distribution of a one-form is written as a subset of \(T^*M\); it should be a subset of \(TM\). The intended screen quotient is clear and the later calculations use the intended object.
- **TeX line 1162:** the first line of the Lie-derivative computation inserts extra exterior derivatives in the u,v terms, producing expressions of incompatible tensor degree. Replacing that line by the standard Leibniz/Cartan expansion gives the calculation displayed immediately afterward. I regard this as a transcription error, not a reason to reject the exterior-system characterization.
- **TeX line 3083:** \(\beta_t\) appears in the formula for \(\nabla^g\varphi_{\phi_t}\) without being the named input; the intended form is \(\varphi_{\phi_t}\).
- **Theorem 4.41 statement, TeX line 4777, PDF page 57:** the direction of the phrase “Dirac current ... proportional ... to the dilaton curvature” should be reversed or written as \(\varphi_{\bar\phi}=c u\). The proven statement allows c=0, while u never vanishes. The proof at lines 5216-5228 and the examples make the intended statement unambiguous.
- **Final example, TeX line 5329:** the dilaton uses an undefined capital T although the time coordinate throughout the example is t. The subsequent calculation clearly requires \(e^{im(t+z)}\).

These items do not, with the indicated interpretations, change the intended principal conclusions.

## Review coverage and assessment of the remaining arguments

**Section 2.** I followed the contorsion decomposition, the null-frame gauge transformations, the equivalence of the covariant and exterior systems, and the curvature expression in terms of dκ and dρ. The converse exterior-system characterization can also be justified by uniqueness of a metric connection with specified torsion. I found no additional substantive obstruction there. The reconstruction of spinors and their spin structure uses external results that I did not re-prove.

**Section 3.** I checked the adapted globally hyperbolic coframe, the evolution/constraint reduction, the choice of lapse, the transport solution, and the derivation of the constant rotation parameter r. In particular, the argument from \(dr=f e_u\) to \(d(r^2)=0\), followed by connectedness, is valid, including at r=0. I checked the distinction between a point-dependent flow tube and a globally hyperbolic development, and the null-current straightening argument for local uniqueness. The stationary torsion formula and the contact/integrable branch reconstructions are consistent. The global classification uses a cited classification theorem, which I did not verify externally. The short global-hyperbolicity completion is given above.

**Section 4 before the final rigidity argument.** I read the gerbe reduction, the dilaton conventions, the second-order reduced equations, the supersymmetry reduction, explicit existence construction, and uniqueness at the stated level of metric, dilaton, curvature, and spinor. I checked that the explicit curving construction has the prescribed curvature and that its closure follows from the spatial constraints. I examined the compatibility and defect-propagation calculations and independently checked representative scalar and mixed components, leading to the concrete missing-term finding above. I did not independently rederive every lengthy curvature component in this section. The transport argument's use of the Cauchy property is appropriate once the preceding defect identities hold.

**Lemma 4.38 and Theorem 4.41.** I scrutinized the entire weak leafwise averaging proof and its use in compact rigidity. I found no additional substantive error in these arguments. In particular, the proof projects onto the closure of leafwise exact forms rather than assuming a closed range; smoothing by the commuting, measure-preserving R^2 action justifies use of the integrated Bochner identity on the weak remainder. The weighted wedge-pairing argument then follows from integration by parts. In the rigidity proof, the connected level sets on the universal cover justify the compact-leaf/dense-leaf description of the invariant functions. The choice of positive basic weight, the determinant averaging for A, and the subsequent symmetric trace-free curvature-matrix argument were checked. The argument does not require integration over a dense individual leaf. The transfer to the original development uses the global null-current flow and is compatible with the earlier universal-property argument.

**Examples and bibliography.** I read all examples, including the incomplete flow-tube example, the compact configuration that fails the scalar constraint, the circle-valued dilaton example, and the non-flat spacelike graph in flat spacetime. Their intended calculations are consistent with the stated conventions, apart from the notation issue listed above. I read the bibliography but did not use publication status or authorship as evidence of correctness.

The decisive finding is the false intermediate equality in the proof of Theorem 4.30. It is specifically localized, independently derived, and contradicted by admissible data. The rest of this report should not be read as formal certification of the remaining calculations or of results imported by citation.
