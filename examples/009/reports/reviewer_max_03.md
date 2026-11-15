REJECT

I found a false intermediate identity in the proof of Theorem 4.30. It omits a generally nonzero term from differentiating the vector field inserted into the second fundamental form. This is used in the derivation of the transverse momentum-constraint identity, so the proof is not correct as printed. I give an explicit admissible local example below. The error appears repairable, and I am not claiming that Theorem 4.30, the subsequent compatibility theorem, or the compact rigidity theorem is false.

**Material and scope.** I read the complete supplied `blind/r8p6/paper.tex`, lines 1-5440, in bounded chunks, including the bibliography, and consulted its supplied 65-page `paper.pdf`. I visually checked PDF pages 22, 29, 45-46, and 55-61, including the problematic display and the complete leafwise averaging and compact rigidity arguments. No other manuscript version, external mathematical source, other review, experiment file, or agent's work was consulted. I did not delegate or use a formal proof assistant.

**1. Substantive computational error in the proof of Theorem 4.30.**

Location: TeX lines 3749-3752, especially line 3751; the first displayed equation on PDF page 46, in the proof of Theorem 4.30. The affected conclusion is the second identity in equation (67), used to establish equation (66). The subsequent invocation of the faulty display is at TeX line 3769.

Fix a time and suppress its index. Put

\[
U=e_u^\sharp,\qquad L=e_l^\sharp,\qquad
w=\widehat c(e_u)=\iota_U\widehat c.
\]

The paper correctly has

\[
d\bigl(\Theta(U,-)\bigr)=\tfrac12dw.
\]

It then asserts

\[
(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12dw(U,L).
\tag{printed}
\]

This does not follow. The argument of the tensor, namely $U$, is a varying vector field. The product rule gives

\[
\begin{aligned}
d\bigl(\Theta(U,-)\bigr)(U,L)
={}&(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)\\
&+\Theta(\nabla_UU,L)-\Theta(\nabla_LU,U).
\end{aligned}
\]

The covariant-derivative formula in the paper's own Remark 4.28, TeX line 3542, implies

\[
\nabla_UU=-\Theta(U,-)^\sharp+\Theta(U,U)U-\tfrac12w^\sharp,
\qquad
\nabla_LU=-\Theta(L,-)^\sharp+\Theta(U,L)U.
\]

By symmetry of $\Theta$, their contributions cancel except for

\[
\Theta(\nabla_UU,L)-\Theta(\nabla_LU,U)
=-\tfrac12\Theta(w^\sharp,L).
\]

Thus the correct identity is

\[
\boxed{
(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12dw(U,L)+\tfrac12\Theta(w^\sharp,L).
}
\tag{corrected}
\]

There is no hypothesis in Theorem 4.30 making the added term vanish. In particular, the theorem concerns general supersymmetric configurations, before imposing the Maxwell and momentum constraints of the equations of motion. One cannot use the later compact-solution argument to set $w=0$ here.

Here is a concrete local check within the paper's spatial supersymmetry constraints. On a coordinate domain with coordinates $(z,y,x)$, orient it by the coframe

\[
e_u=e^y dz,\qquad e_l=e^zdy,\qquad e_n=dx,
\qquad \mathfrak f=0.
\]

Take $\phi=e^{iy}$, so $\varphi_\phi=dy$, a flat initial curving with $H_b=0$, and

\[
f_b=0,\qquad \mathfrak c=e_u\wedge dy.
\]

These satisfy (74)-(75):

\[
de_u=dy\wedge e_u,
\quad de_l=e^{-y}e_u\wedge e_l,
\quad de_n=0,
\]

and the antisymmetric screen-rotation expression is zero. In particular $de_l\wedge e_u=de_n\wedge e_u=0$, and the prescribed initial three-form is indeed zero. The second fundamental form prescribed by the paper is

\[
\Theta=-\tfrac12\mathcal L_Uh
=-e^{-y}e_l\otimes e_l
+\tfrac12e^{-z}e_u\odot e_l,
\qquad
U=e^{-y}\partial_z,\quad L=e^{-z}\partial_y.
\]

Here $\odot$ has the manuscript's convention, the sum of the two tensor products. We have

\[
w=\iota_U\mathfrak c=dy=e^{-z}e_l,
\qquad \Theta(U,-)=\tfrac12dy,
\qquad dw=0.
\]

The spatial connection satisfies

\[
\nabla_UU=-e^{-z}L,\quad
\nabla_UL=e^{-z}U,\quad
\nabla_LU=e^{-y}L,\quad
\nabla_LL=-e^{-y}U.
\]

Consequently,

\[
(\nabla_U\Theta)(U,L)=-\tfrac32e^{-(y+z)},
\qquad
(\nabla_L\Theta)(U,U)=-e^{-(y+z)}.
\]

The left side of the printed identity is therefore $-\tfrac12e^{-(y+z)}$, whereas its right side is zero. The omitted term is precisely

\[
\tfrac12\Theta(w^\sharp,L)=-\tfrac12e^{-(y+z)}.
\]

This is a failure of a pointwise tensor identity, rather than an issue about global topology, completeness, or differentiability. The proof explicitly says at line 3677 that this part uses only the spatial constraints, all of which the example satisfies.

**Effect and repair.** The term is needed when equating the two Ricci expressions at TeX lines 3737-3745. With the corrected formula it cancels the $\tfrac12\Theta(w^\sharp,L)$ in the second Ricci expression, and the intended identity

\[
\mathcal W(L)=-\tfrac12(*\mathcal M)(L)
\]

can then be recovered using the remaining displayed relations. With the printed formula, that cancellation is unavailable; following the stated substitution leaves an additional $\tfrac12\Theta(w^\sharp,L)$. Thus line 3769 is not a justified consequence of the displayed calculation as written.

This is the basis of the verdict. It is a substantive algebraic omission in a central proof, not merely a misspelled symbol: the missing term is nonzero on admissible data and changes the inference. Nevertheless, the corrected identity appears to repair this part of Theorem 4.30 without changing its statement. The dependent uses in Theorem 4.35 and the initial-data corollaries should be checked against the corrected calculation. I found no counterexample to those statements.

**2. A missing but readily supplied global-hyperbolicity argument.**

Location: Corollary 3.27(3), TeX line 2441, and its proof at lines 2537-2573, especially the transition at line 2541; PDF pages 28-29.

The proof shows completeness of $\mathcal X$ from completeness of $q=e^{2\mathfrak f}h$, and then proceeds to maximality. It does not actually establish that the whole constructed product is globally hyperbolic with the stated Cauchy hypersurface. Flow completeness alone would not prove that assertion.

For this particular metric the omitted argument is short and valid. Write $\lambda=e^{-\mathfrak f}$, $U=e_u^\sharp$, and $\mathcal X=\lambda U$. Then $q=\lambda^{-2}h$, $|\mathcal X|_q=1$, $dt$ is timelike, and a causal curve parametrized by $t$, with spatial velocity $v$, satisfies

\[
0\geq\lambda^{-2}g(\partial_t+v,\partial_t+v)
=|v|_q^2-2q(\mathcal X,v),
\]

so $|v-\mathcal X|_q\leq1$ and $|v|_q\leq2$. Completeness of $q$ prevents a causal curve from escaping spatially at a finite value of $t$. Such a curve would have an endpoint and could be extended. Hence every inextendible causal curve has the full time range and meets each slice exactly once. This supplies the Cauchy property before the maximality argument.

I regard this as an omitted elementary justification, not a counterexample and not an independent basis for rejection. The later completeness-based uses can be retained after adding it.

**3. Minor mathematical wording and notation corrections.**

- TeX line 1251, the paragraph following Corollary 2.16: triviality of $[\kappa]\oplus[\rho]$ allows a *null-rotation gauge change* of the coframe, using (7), to produce a parallel representative. It does not generally allow a conformal rescaling of every representative to become parallel. For example, apply a nonconstant null rotation to a constant Minkowski coframe. The resulting exact, nonzero $\kappa$ can be eliminated by the inverse null rotation, but a scalar rescaling cannot do it: parallelity of the rescaled, already parallel $u$ forces the scalar to be constant. The claimed trivial-holonomy consequence is correct; replace the phrase about a conformal transformation. This does not affect the later principal results.

- TeX line 4777, Theorem 4.41: the final statement should say that the **dilaton curvature is a constant multiple of the Dirac current**, namely $\varphi_{\bar\phi}=c u$, as proved at lines 5216-5228. Saying that the nonvanishing Dirac current is a constant multiple of the dilaton curvature would wrongly exclude constant dilatons, including the $m=0$ case of Example 4.43. The intended statement and proof are clear, so this is a direction-of-proportionality wording correction, not a defect in the rigidity argument.

- TeX line 5329 in the final example uses $T$ in $e^{im(T+z)}$, although the spacetime coordinate is $t$. This is a harmless typo; the computations use $e^{im(t+z)}$.

**Coverage and checks of the remaining arguments.**

I followed the entire chain of results, not only the location reported above:

- In Section 2 I checked the torsion/contorsion alternation, the null-coframe gauge formulas, the passage between covariant and exterior systems, and the curvature formula in terms of $d\kappa,d\rho$. The reconstruction of the global real spinor relies on cited results; those external proofs were not independently consulted.

- In Section 3 I checked the lapse and coframe reduction, the spatial cohomological condition, the integration in the gauge $\lambda_t=e^{-\mathfrak f_t}$, the derivation of constancy of the rotation rate, and the null-current argument for uniqueness independently of lapse. I checked the treatment of nonuniform flow domains and the need to restrict to a domain of dependence. The contact-branch construction from a trivialized contact plane field and the explicit mapping-torus construction in the integrable branch are consistent. The global classification uses the stated external contact and rank-two-action theorems, whose proofs were outside the permitted input.

- In Sections 4.1-4.5 I followed the gerbe and curvature decompositions, the Einstein/Maxwell/dilaton splitting, the dilatino reduction, and the explicit evolution of the curving and circle-valued dilaton. I checked that the asserted uniqueness concerns the metric, flux curvature, dilaton, and spinor up to sign, rather than incorrectly claiming uniqueness of all flat gerbe data.

- In Section 4.6 I checked the roles of the constraint identities and the homogeneous transport equations, including the use of the Cauchy property to reach the initial hypersurface along every characteristic. The defect and curvature calculations are long; I did not reproduce every component computation independently. The product-rule error above was found by doing such a computation rather than accepting the concluding phrase that a direct calculation suffices.

- I examined Lemma 4.38 and Theorem 4.41 in detail. The leafwise smoothing uses the commuting, volume-preserving $\mathbb R^2$-action and legitimately extends the integrated identity to the weak $L^2$ remainder. The argument uses closure of leafwise exact forms, so it does not improperly assume the range is closed or impose a spectral gap. The weighted pairing is justified because the weight is basic. In the rigidity proof I checked the positive Maxwell integral, the scalar constraint, the compact/dense-leaf description of the projection, the choice of positive weight, and both determinant-pairing applications. In particular, the proof does not incorrectly infer $A=0$ from $\Pi(A)=0$; it separately proves vanishing of the symmetric trace-free curvature matrix $C$. I found no independent substantive error in those steps.

- I checked the concluding examples, including the nonzero-flux configuration that fails the scalar constraint, the circle-valued dilaton with nonzero period, and the curved spacelike graph in flat spacetime.

I also made a small exact-arithmetic curvature check on an admissible contact-branch example when assessing the separate algebraic-speciality claim. That check did not produce an additional issue. Such a check supports only the example tested, not the universal assertion.

This is a mathematical review, not formal verification. The verdict concerns the current manuscript's demonstrably false intermediate identity and the inference that uses it. It should not be read as a claim that the principal existence, compatibility, or rigidity statements cannot be repaired or are disproved.
