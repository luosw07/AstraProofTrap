REJECT

I found a substantive tensor-calculus error in the proof of Theorem 4.30 (the constraint compatibility theorem). The displayed identity at TeX line 3751 omits a generally nonzero contraction of the second fundamental form with the transverse dilaton curvature. The missing term cannot be discarded under the hypotheses of that theorem. An explicit smooth example below makes the left-hand side nonzero while the printed right-hand side is zero.

This finding invalidates a step in the supplied proof; it does not by itself disprove the statement of Theorem 4.30. In fact, the theorem's final constraint identity holds in the example below when calculated directly. The verdict is based on the substantive erroneous inference in the proof, rather than a claim that the central existence or compact rigidity statements have been disproved.

1. Incorrect covariant differentiation in Theorem 4.30.

Location: proof of Theorem 4.30, label `thm:compatibilityflows`, specifically the paragraph at lines 3748–3753 and the displayed equation at line 3751. The error is used in the concluding computation at line 3769. Write

\[
U=e_{tu}^{\sharp},\qquad L=e_{tl}^{\sharp},\qquad
q=\widehat c_t(U,-),\qquad \nabla=\nabla^{h_t},\qquad \Theta=\Theta_t.
\]

The manuscript correctly has \(d(\Theta(U,-))=\tfrac12dq\). It then asserts

\[
(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12dq(U,L).
\]

This treats the vector field inserted into \(\Theta\) as though its covariant derivative contributed nothing. The product rule actually gives

\[
\begin{aligned}
d(\Theta(U,-))(U,L)
={}&(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)\\
&+\Theta(\nabla_UU,L)-\Theta(\nabla_LU,U).
\end{aligned}
\]

Using the manuscript's own connection formula in Remark 4.28, line 3542,

\[
\nabla_XU=-\Theta(X,-)^{\sharp}+\Theta(U,X)U
-\tfrac12 h_t(U,X)q^{\sharp},
\]

the last two terms in this product rule sum to \(-\tfrac12\Theta(q^{\sharp},L)\). Thus the correct identity is

\[
(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12dq(U,L)+\tfrac12\Theta(q^{\sharp},L).
\tag{R1}
\]

Symmetry of \(\Theta\), cited in the manuscript at this step, cancels the other quadratic terms, but does not cancel the last term in (R1).

Here is an example satisfying the supersymmetry constraints where that term is nonzero. On a coordinate domain with coordinates \((z,x,y)\), take

\[
e_u=e^x dz,\qquad e_l=e^z dx,\qquad e_n=dy,
\qquad \mathfrak f=0,
\]

and use a trivial gerbe with initial curving \(b=0\), dilaton \(\phi=e^{ix}\), and

\[
\varphi_\phi=dx,\qquad f_b=0,\qquad
\mathfrak c=e^x dz\wedge dx=e_u\wedge\varphi_\phi.
\]

The orientation is \(e_u\wedge e_l\wedge e_n\). Directly,

\[
de_u=dx\wedge e_u,\quad
de_l=e^z dz\wedge dx,\quad de_n=0.
\]

Consequently both equations `NSNSsusyconstraintsI` and `NSNSsusyconstraintsII` hold: the two wedge constraints vanish, the dilaton constraint holds, and the scalar rotation expression is zero because
\(\mathcal L_Ue_n=0\) and \(\mathcal L_Ue_l=e^{-x}e_l\), where \(U=e^{-x}\partial_z\). Also \(d\mathfrak c=0\).

These data can be put into an explicit supersymmetry flow using

\[
\Phi_t(z,x,y)=(z+t e^{-x},x,y),\quad
\lambda_t=1,\quad \mathfrak f_t=0,\quad
\mathfrak e_t=\Phi_t^*\mathfrak e,\quad
\phi_t=e^{ix},\quad a_t=0,\quad b_t=t\mathfrak c.
\]

Here \(\Phi_t^*\mathfrak c=\mathfrak c\), \(H_{b_t}=0\), and the supersymmetry equations are preserved by these pullbacks. One may restrict to a globally hyperbolic neighborhood of a spacelike initial patch. The disputed equation is pointwise, so this restriction does not alter the calculation.

At time zero,

\[
h=e^{2x}dz^2+e^{2z}dx^2+dy^2,
\qquad U=e^{-x}\partial_z,\quad L=e^{-z}\partial_x.
\]

Put \(a=e^{-z}\) and \(b_*=e^{-x}\), where \(b_*\) is just a scalar used in this calculation, not the gerbe curving. The second fundamental form prescribed by the paper is
\(\Theta=-\tfrac12\mathcal L_Uh\), with frame components

\[
\Theta(U,U)=0,\qquad \Theta(U,L)=\tfrac12a,
\qquad \Theta(L,L)=-b_*,
\]

and all components involving \(e_n^{\sharp}\) zero. The Levi-Civita connection gives

\[
\nabla_UU=-aL,\quad \nabla_UL=aU,
\quad \nabla_LU=b_*L,\quad \nabla_LL=-b_*U.
\]

Therefore

\[
(\nabla_U\Theta)(U,L)=-\tfrac32ab_*,\qquad
(\nabla_L\Theta)(U,U)=-ab_*.
\]

The left-hand side at line 3751 is thus \(-\tfrac12e^{-x-z}\). On the other hand,
\(q=\iota_U\mathfrak c=dx\), so \(dq=0\) and its printed right-hand side is zero. The missing term in (R1) is exactly
\(\tfrac12\Theta(q^{\sharp},L)=-\tfrac12e^{-x-z}\). In particular, at \(x=z=0\), the printed equality reads \(-1/2=0\).

This is a genuine omitted tensor contribution, rather than a notational ambiguity or an incorrect choice of sign convention. It affects the presented proof of the transverse part of equation `constraintidentities`, which is then used in Theorem 4.35 and the initial-data characterization. Those derivations need to be checked with (R1) restored. The example is not a counterexample to the final identity `constraintidentities0`: a separate direct calculation of the constraints gives \(\mathcal H e_u-2\mathcal W-*\mathcal M=0\) in this example. Thus I am not asserting that a corrected proof is impossible or that compact rigidity is false.

2. Editorial errors distinguished from the substantive finding.

Several other discrepancies have evident intended readings and are not grounds for the verdict. At line 910, the Levi-Civita curvature is written `R^o_{x,y}` instead of `R^g_{X,Y}`. The first line of the calculation at line 1162 has exterior derivatives in tensor factors where Cartan's formula requires the coframe forms themselves, making that line ill-typed as printed; its intended form is clear from the following line. At line 3083, the undefined `beta_t` should be the one-form `varphi_{phi_t}` being differentiated. At line 5329, the coordinate `T` should be `t`. These differ from line 3751, where the displayed, well-typed identity is mathematically false and a nonzero term must be restored.

Review coverage and limitations: I read the entire supplied standalone TeX file, all 5,440 lines, including the introductory claims, all statements and proofs in Sections 2–4, every example, and the bibliography. I followed the exterior-system reduction, explicit transport construction, null-current uniqueness argument, time-independent development and maximality argument, the contact/integrable classification, gerbe reduction, Neveu–Schwarz reduction, supersymmetry and constraint propagation, and the compact rigidity proof. I checked the leafwise averaging argument, including the weak remainder, leafwise regularization, weighted projection pairing, compact/dense leaf alternatives, and its two determinant applications. I found no separate substantive objection to that averaging argument or to the subsequent rigidity argument conditional on the earlier identities.

I performed independent exact calculations for the local example above. No external mathematical source, alternative paper version, private log, experiment record, or other review was consulted, and I did not delegate or use a formal proof assistant. The TeX itself was the reviewed mathematical representation; I did not need the PDF to resolve its formulas. Results imported by citation, such as the global spinor-square correspondence and the classification of compact three-manifolds carrying the specified action, were assessed through the statements and uses in this paper, not independently verified from their sources. This is a mathematical review, not formal verification of every component calculation.
