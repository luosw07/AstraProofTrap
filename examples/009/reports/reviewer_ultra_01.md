REJECT

I found a substantive algebraic error in the proof of Theorem 4.30 (the constraint compatibility identity). An equality used in the proof drops a generally nonzero covariant-product-rule term. I give both the corrected formula and an explicit supersymmetry flow satisfying the hypotheses on which the printed equality fails. This is a rejection of the argument as written, not a claim that the theorem's final identity, the existence results, or compact rigidity are false.

Reviewed source: paper.tex in run_20261114/blind/r8p6, 5,440 lines. All line references below refer to that exact source.

1. Substantive error: the covariant differentiation of Theta(e_u) in Theorem 4.30.

Location: Theorem 4.30, label thm:compatibilityflows, proof at TeX lines 3749–3752, specifically the unnumbered displayed equality at line 3751. Its use in the final deduction is at lines 3762–3769. The relevant formula for the covariant derivative of e_u appears at line 3542 in Remark 4.28.

Fix a time, and abbreviate
\[
U=e_{tu}^{\sharp},\qquad L=e_{tl}^{\sharp},\qquad
T=\Theta_t,\qquad \gamma=\widehat c_t(U,-).
\]
The equation for the scale function gives
\[
d(T(U,-))=\tfrac12 d\gamma.
\]
The paper then asserts
\[
(\nabla_U T)(U,L)-(\nabla_L T)(U,U)
=\tfrac12 d\gamma(U,L). \tag{printed}
\]
This does not follow by differentiating the contraction: U is a variable vector field, and its covariant derivatives must be included.

Indeed, the paper's own formula at line 3542 gives
\[
\nabla_U U=-T(U,-)^\sharp+T(U,U)U-\tfrac12\gamma^\sharp,
\qquad
\nabla_L U=-T(L,-)^\sharp+T(U,L)U.
\]
Consequently, by the product rule and symmetry of T,
\[
\begin{aligned}
d(T(U,-))(U,L)
&=(\nabla_U T)(U,L)-(\nabla_L T)(U,U)\\
&\quad+T(\nabla_U U,L)-T(\nabla_L U,U)\\
&=(\nabla_U T)(U,L)-(\nabla_L T)(U,U)
-\tfrac12T(\gamma^\sharp,L).
\end{aligned}
\]
The correct equality therefore is
\[
(\nabla_U T)(U,L)-(\nabla_L T)(U,U)
=\tfrac12 d\gamma(U,L)+\tfrac12 T(\gamma^\sharp,L). \tag{corrected}
\]
Neither symmetry of T nor any of the stated supersymmetry conditions makes the last term vanish in general.

An explicit test within the theorem's hypotheses.

Take the three-torus with angular coordinates x,y,z and initial data
\[
e_u=e^{\sin y}dx,\qquad e_l=e^{\sin x}dy,\qquad e_n=dz,
\qquad \mathfrak f=0,
\]
\[
\phi=e^{i\sin y},\qquad \varphi_\phi=\cos y\,dy,\qquad
b=0,\qquad \mathfrak c=e_u\wedge\varphi_\phi
\]
on the trivial gerbe. Here H_b=f_b=0. Directly,
\[
de_u=\varphi_\phi\wedge e_u,\qquad
de_l\wedge e_u=de_n\wedge e_u=0.
\]
The antisymmetric screen Lie-derivative expression in the last supersymmetry constraint is zero. Thus these data satisfy equations (NSNSsusyconstraintsI)–(NSNSsusyconstraintsII), at lines 3849–3851.

For additional explicitness, this is not just a test on arbitrary tensors. Set
\[
X=e^{-\sin y}\partial_x,\qquad
\Phi_t(x,y,z)=(x+t e^{-\sin y},y,z),
\]
and take
\[
\lambda_t=1,\quad\mathfrak f_t=0,\quad
\mathfrak e_t=\Phi_t^*\mathfrak e,\quad
\phi_t=\phi,\quad a_t=0,\quad b_t=t\mathfrak c.
\]
Since d\mathfrak c=0 and \Phi_t^*\mathfrak c=\mathfrak c, the derived two-form is \widehat c_t=\mathfrak c and f_{b_t}=0. The evolution equations and spatial constraints of Lemma 4.31, lines 3800–3812, hold directly: the coframe evolves by Lie transport, the dilaton is invariant under X, and all spatial constraints are pullbacks of their initial versions. This provides a smooth supersymmetry flow. Its metric -dt^2+h_{\mathfrak e_t} is globally hyperbolic on R times the compact torus; a causal curve cannot escape through a bounded time interval because the spatial metrics are uniformly comparable on every such interval.

At t=0,
\[
h=e^{2\sin y}dx^2+e^{2\sin x}dy^2+dz^2,\qquad
T=-\tfrac12\mathcal L_Uh.
\]
The nonzero coordinate coefficients of T are
\[
T_{xy}=T_{yx}=\tfrac12\cos y\,e^{\sin y},
\qquad
T_{yy}=-\cos x\,e^{2\sin x-\sin y}.
\]
Also \gamma=\widehat c(U,-)=\cos y\,dy, so d\gamma=0 identically.

At p=(0,0,0), the coframe is (dx,dy,dz), U=\partial_x, L=\partial_y, and
\[
T(p)=
\begin{pmatrix}
0&1/2&0\\
1/2&-1&0\\
0&0&0
\end{pmatrix}.
\]
The relevant Christoffel coefficients there are
\[
\Gamma^x_{xy}=1,\quad \Gamma^x_{yy}=-1,\quad
\Gamma^y_{xx}=-1,\quad \Gamma^y_{xy}=1.
\]
The coordinate derivatives of T give
\[
(\nabla_U T)(U,L)=-\tfrac32,\qquad
(\nabla_L T)(U,U)=-1.
\]
Thus the left side of the printed equality is -1/2, whereas its right side is zero. The omitted term is exactly
\[
\tfrac12T(\gamma^\sharp,L)=-\tfrac12.
\]

Why this is substantive and what it affects.

Line 3769 explicitly uses this incorrect identity when equating the two Ricci expressions to deduce the tangential momentum/Maxwell relation. The omission is not merely an undefined symbol, a mislabeled reference, or a term that happens to vanish on the objects under consideration. The displayed equality is false on a smooth supersymmetry flow covered by the theorem. The deduction using the printed identities therefore needs correction.

This does not disprove the final identity \mathcal H e_u=2\mathcal W+*\mathcal M. In the example, at p, direct evaluation gives
\[
\mathcal H=-4,\qquad
\mathcal W=-\tfrac32 dx-\tfrac12dy,\qquad
*\mathcal M=-dx+dy,
\]
which satisfy that final identity. Replacing line 3751 with the corrected product-rule formula is a natural possible repair; the subsequent Ricci substitution should then be checked and written consistently. Theorem 4.35 explicitly uses Theorem 4.30's compatibility identity at lines 4247–4258 and 4324–4328, so the proof dependency should also be checked after that repair. I do not claim this calculation produces a counterexample to Theorem 4.35 or Theorem 4.41.

2. A small proof omission that is readily supplied: global hyperbolicity in the corollary on the time-independent development.

Location: Corollary labeled cor:timeindependentdevelopment, item (3), line 2441; proof at lines 2537–2573.

The proof shows completeness of X and then proceeds to maximality and the universal property, without explicitly establishing that the full product metric is globally hyperbolic with the stated initial slice Cauchy. This is a missing explanatory step rather than a counterexample, and I do not use it as an independent reason for rejection.

Here is a direct completion of that step. For
\[
g=h_{\mathfrak e}-e^{-\mathfrak f}dt\odot e_u,\qquad
q=e^{2\mathfrak f}h_{\mathfrak e},
\]
dt is timelike. Parametrize a causal curve by t and write its spatial velocity as v. Causality gives
\[
|v|_h^2\le 2e^{-\mathfrak f}e_u(v)
\le 2e^{-\mathfrak f}|v|_h,
\qquad |v|_q\le2.
\]
If its t-coordinate has a finite endpoint, completeness of q makes the spatial path converge. The causal curve then has an endpoint in the full product and can be extended. Hence every inextendible causal curve has full t-range and intersects every slice exactly once. This establishes the Cauchy property needed before the maximality argument.

3. Harmless wording and notation errors, distinguished from issue 1.

At line 910, the curvature expansion uses \mathcal R^o_{x,y}, while its context and the following sentence identify the term as the Levi-Civita curvature \mathcal R^g_{X,Y}. This is a notation typo and does not change the argument.

At line 1162, the first displayed line for \mathcal L_u g contains exterior derivatives in places where the undifferentiated coframe factors must occur; as written the tensor degrees do not match. The intended Cartan-formula expression is
\[
(\iota_Udu)\odot v+u\odot(\iota_Udv)
+l\odot(\iota_Udl)+n\odot(\iota_Udn).
\]
The following expanded lines and the usual uniqueness of the metric connection with prescribed torsion make the intended calculation clear. I treat this as a typographical formula error, not the basis for rejection.

At line 4777, Theorem 4.41 says that the Dirac current is proportional by a real constant to the dilaton curvature. The proof at lines 5216–5222 establishes the reverse wording, \varphi_{\bar\phi}=c u, allowing c=0. The examples also allow zero dilaton curvature and a nonzero current. The statement should say that the dilaton curvature is a constant multiple of the Dirac current. The intended assertion is clear from the proof; this is a wording reversal.

At line 5329, the final example uses T in e^{im(T+z)}, although the spacetime coordinate is t. It should read t. This has no effect on the curvature calculation or example.

Coverage and limitations.

I read the entire standalone TeX source, lines 1–5440, in bounded chunks, including the complete mathematical text and bibliography. I did not consult another version, external mathematical sources, any other workspace paper, or another review. I did not use a formal proof assistant. The rendered PDF was not needed to resolve notation; locations in this report are source locations.

I examined the algebraic/coframe setup, its conversion to a Cartan exterior system, the spatial/time splitting, the explicit rotated flow, the null-current uniqueness argument, the stationary model and completeness claim, the contact/integrable branches, the gerbe and curvature reduction, the supergravity evolution/constraint equations, their compatibility and propagation arguments, and the entire compact-rigidity proof and examples.

In particular, I checked the essential logic of Lemma 4.38's L2 projection argument: the volume-preserving commuting flows, regularization by their R2 action, application of the integrated flat Weitzenbock identity, convergence to the weak remainder, and the weighted pairing. I found no substantive defect in that argument. I also followed the compact-versus-dense leaf distinction and both determinant-averaging applications in Theorem 4.41; the dense-leaf part does not simply assume that an arbitrary measurable function constant along a dense leaf is constant, but supplies the needed period-group argument.

The review includes independent product-rule and coordinate calculations for the error above and spot checks of other geometric formulas. It is not exhaustive symbolic verification of every lengthy component calculation. Results imported by citation, including the spinor-square correspondence and the classification theorem for locally free R2 actions, were assessed for the way they are used but were not independently re-proved or externally checked. I found a defensible specific mathematical failure in the submitted argument, so the overall verdict is REJECT rather than INCONCLUSIVE. The report does not assert that the paper's principal conclusions cannot be repaired.

