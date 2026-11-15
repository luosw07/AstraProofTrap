REJECT

I found a substantive calculation error in the proof of Theorem \(\ref{thm:compatibilityflows}\): the unnumbered identity at TeX line 3751 omits a term which need not vanish. The identity is explicitly used to obtain the transverse momentum–Maxwell compatibility relation at line 3769. The stated compatibility theorem may nevertheless be correct; the finding below is a counterexample to an essential displayed step of its proof, not a counterexample to the theorem itself.

The input reviewed was the complete current paper at \`run_20261114/blind/r8p6/paper.tex\`, lines 1–5440, including its bibliography. All line references below refer to that file.

1. Missing contraction term in the compatibility proof

Location: proof of Theorem \(\ref{thm:compatibilityflows}\), paragraph beginning “On the other hand, the equation for…” at lines 3749–3752, especially the display at line 3751; its subsequent use is stated at line 3769.

Fix a time and abbreviate
\[
U=e_{tu}^{\sharp},\qquad L=e_{tl}^{\sharp},
\qquad C=\widehat c_t(e_{tu})=\iota_U\widehat c_t,\qquad
B=\Theta_t(U,\cdot).
\]
The equation for \(\dd_\Sigma\mathfrak a_t\) does imply
\[
\dd_\Sigma B=\tfrac12\dd_\Sigma C.
\]
However, \(B\) is obtained by contracting \(\Theta_t\) with a nonparallel vector field. Consequently,
\[
\begin{aligned}
\dd_\Sigma B(U,L)
={}&(\nabla_U\Theta_t)(U,L)
-(\nabla_L\Theta_t)(U,U)\\
&+\Theta_t(\nabla_U U,L)
-\Theta_t(\nabla_L U,U).
\end{aligned}
\]
The paper's own covariant derivative formula at line 3542 gives
\[
\nabla_XU=-\Theta_t(X,\cdot)^\sharp
+\Theta_t(U,X)U-\tfrac12 e_{tu}(X)C^\sharp.
\]
Using symmetry of \(\Theta_t\), the last two terms in the preceding expression combine to
\[
-\tfrac12\Theta_t(C^\sharp,L),
\]
rather than zero. Thus the correct identity is
\[
\boxed{
(\nabla_U\Theta_t)(U,L)-(\nabla_L\Theta_t)(U,U)
=\tfrac12\dd_\Sigma C(U,L)
+\tfrac12\Theta_t(C^\sharp,L).
}
\]
The last summand is absent from line 3751. Symmetry of \(\Theta_t\), cited in the surrounding sentence, does not remove it.

Here is an explicit example showing that this is a real failure under the relevant hypotheses. On the oriented torus
\(\Sigma=(\mathbb R/2\pi\mathbb Z)^3\), with coordinates \(x,y,z\), set
\[
F=\sin x,\qquad G=\sin y,\qquad
e_u=e^G\dd x,\qquad e_l=e^F\dd y,\qquad e_n=\dd z,
\]
and choose
\[
\mathfrak f=0,\quad
\phi=e^{iG},\quad
\varphi_\phi=\dd G,\quad
b=0,\quad H_b=0,\quad f_b=0,\quad
\mathfrak c=e_u\wedge\dd G.
\]
Take the trivial gerbe with its trivial connective structure and curving.

These data satisfy all the supersymmetry constraints at lines 3849–3851:
\[
\dd e_u=\dd G\wedge e_u,\qquad
\dd e_l\wedge e_u=\dd e_n\wedge e_u=0,
\]
the formula for \(\mathfrak c\) holds by definition, and
\[
(\mathcal L_{e_u^\sharp}e_n)(e_l^\sharp)
-(\mathcal L_{e_u^\sharp}e_l)(e_n^\sharp)=0=f_b.
\]
Their explicit supersymmetry evolution is the paper's pullback construction with the complete vector field
\[
U=e^{-G}\partial_x,\qquad
\Phi_t(x,y,z)=(x+t e^{-G(y)},y,z).
\]
In particular, this example lies in the class to which the compatibility proof applies; it is not arbitrary data violating its supersymmetry assumptions. It need not satisfy the equations of motion, which are not hypotheses of that compatibility theorem.

At the initial time put
\[
q=G'e^{-F},\qquad r=F'e^{-G}.
\]
Here \(r\) is merely a local abbreviation, not the paper's constant screen-rotation parameter, which is zero for these data. The metric and second fundamental form are
\[
h=e^{2G}\dd x^2+e^{2F}\dd y^2+\dd z^2,\qquad
\Theta=-r\,e_l\otimes e_l+\tfrac q2\,e_u\odot e_l.
\]
Moreover,
\[
C=\iota_U\mathfrak c=\dd G,\qquad \dd C=0.
\]
The frame connection satisfies
\[
\nabla_UU=-qL,\quad \nabla_UL=qU,\quad
\nabla_LU=rL,\quad \nabla_LL=-rU,
\]
and \(U(q)=-rq\). Hence
\[
(\nabla_U\Theta)(U,L)=-\tfrac32rq,\qquad
(\nabla_L\Theta)(U,U)=-rq.
\]
At \(x=y=0\), \(q=r=1\), so the left side of line 3751 is \(-1/2\), while its printed right side is \(0\). The omitted term is exactly
\[
\tfrac12\Theta(C^\sharp,L)=-\tfrac12.
\]
I also checked these values directly from the coordinate metric and its Christoffel coefficients; the discrepancy is independent of frame notation.

Impact: line 3769 explicitly substitutes the false identity into the two Ricci expressions to conclude
\[
\mathcal W_t(e_{tl}^{\sharp})
=-\tfrac12(*_{h_t}\mathcal M_t)(e_{tl}^{\sharp}).
\]
That inference is not justified by the calculation as printed. This is a missing nonzero tensor term in a proof of a principal result, rather than a harmless symbol or typographical error. The transverse relation is subsequently used in Theorem \(\ref{thm:susyflowcompatibility}\), notably lines 4247–4258.

Restoring the missing term and rechecking the subsequent cancellation appears to be a localized route to repair. I am not asserting that either compatibility theorem is false. Indeed, in the example above, at the indicated point one obtains
\(\mathcal H=-4\), \(\mathcal W=-\tfrac32e_u-\tfrac12e_l\), and
\(*\mathcal M=-e_u+e_l\), which do satisfy the theorem's final identity
\(\mathcal H e_u=2\mathcal W+*\mathcal M\). This distinction does not make the false intermediate identity valid.

2. Minor notation defects

These do not drive the verdict.

- In Lemma \(\ref{lemma:hyperbolicderivatives}\), line 3083, the symbol \(\beta_t\) in the term \(\Theta_t(\beta_t^\sharp)\) is undefined in that statement; the surrounding calculation indicates \(\varphi_{\phi_t}\).
- In the last example, line 5329 uses \(T\) in \(e^{im(T+z)}\), although the time coordinate introduced there is \(t\). Reading this as \(t\) gives the subsequent stated curvature \(m\,u\).

Review coverage and limitations

I read the whole TeX document in bounded, consecutive chunks. The review included the spinorial-form framework, torsion exterior system, all stages of the Cauchy reduction, the explicit rotated pullback solution, the null-current uniqueness argument, the contact and integrable branches, the gerbe reduction, the bosonic evolution and constraint equations, both compatibility arguments, the supersymmetric development, the entire leafwise averaging lemma, all six steps of compact rigidity, and the final examples.

I checked the main algebraic reconstruction and transport mechanisms, the zero/constant screen-rotation obstruction, the weighted determinant argument, and the curvature-matrix argument. In particular, I found no additional substantive problem in the leafwise averaging proof: its use of the closure of leafwise exact forms, regularization by the commuting measure-preserving action, and integration by parts does address the possibility of noncompact or dense leaves. I also checked how the closed one-form in the compact rigidity proof permits the stated distinction between compact fibers and dense leaves, and how the positive basic weight is constructed in each case.

The global hyperbolicity claim under completeness of \(e^{2\mathfrak f}h_{\mathfrak e}\) can be supported directly: a causal curve in the stationary metric, parametrized by its temporal coordinate, has spatial speed at most \(2\) in that complete Riemannian metric. Thus I do not regard the brevity of that portion of the proof as a separate substantive objection.

This was an independent mathematical review, not formal verification. I did not independently recompute every lengthy curvature expansion. I treated the external results cited by the paper as cited inputs and did not inspect those sources, other paper versions, other reports, or experiment records. The current TeX was sufficient for the mathematical review; I did not separately inspect the PDF. No formal proof assistant was used.

