REJECT

Independent mathematical review of the complete current paper

Reviewed source: run_20261114/blind/r8p6/paper.tex, all 5,440 lines, including the introduction, every statement and proof, examples, and bibliography. The locations below refer to this source. I did not consult another version, another report, external mathematical sources, or another agent.

Verdict and principal finding

There is a false covariant-derivative identity in the proof of Theorem 4.30 (label thm:compatibilityflows). It omits a generally nonzero contraction with the second fundamental form. This is an algebraic proof error on data satisfying the paper's hypotheses, not merely an undefined symbol. The displayed proof therefore requires correction. The error is localized and appears repairable; I have not established that the theorem's final compatibility identity, or the paper's principal existence and rigidity conclusions, are false.

1. Missing tensor term in the proof of Theorem 4.30

Exact location: paper.tex lines 3749–3752, specifically the unnumbered display at line 3751. It is used in the final combination of identities at line 3769.

Fix a time, suppress its subscript, and write
\[
 U=e_u^\sharp,\qquad L=e_l^\sharp,\qquad
 \gamma=\widehat c(U,-).
\]
The equation for \(d_\Sigma\mathfrak a\) does indeed imply
\[
 d_\Sigma(\Theta(U,-))=\tfrac12d_\Sigma\gamma.
\]
However, line 3751 claims
\[
 (\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
 =\tfrac12d_\Sigma\gamma(U,L).
\]
This does not follow: differentiating the contraction \(\Theta(U,-)\) also differentiates \(U\).

The connection formula given in Remark 4.28 (label remark:covariantevolution; lines 3541–3544) implies
\[
 \nabla_XU
 =-\Theta(X,-)^\sharp+\Theta(U,X)U
   -\tfrac12e_u(X)\gamma^\sharp.
\]
Consequently,
\[
\begin{aligned}
 d(\Theta(U,-))(U,L)
 ={}&(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)\\
 &+\Theta(\nabla_UU,L)-\Theta(\nabla_LU,U)\\
 ={}&(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
       -\tfrac12\Theta(\gamma^\sharp,L).
\end{aligned}
\]
The correct identity is therefore
\[
 \boxed{
 (\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
 =\tfrac12d\gamma(U,L)+\tfrac12\Theta(\gamma^\sharp,L).
 }
\]
The omitted term is not forced to vanish by supersymmetry or by closedness of the dilaton curvature.

An explicit admissible example

Take \(\Sigma=\mathbb R^3\), with coordinates \(x,y,z\), and let
\[
 F(y)=\tanh y,\qquad G(x)=\tanh x.
\]
Use the trivial bundle gerbe with initial curving \(b=0\), and set
\[
\begin{gathered}
 e_u=e^{F(y)}dx,\qquad e_l=e^{G(x)}dy,\qquad e_n=dz,
 \qquad \mathfrak f=0,\\
 \phi=e^{iF(y)},\qquad \varphi_\phi=dF,\qquad
 f_b=0,\qquad \mathfrak c=e_u\wedge dF .
\end{gathered}
\]
These satisfy both sets of supersymmetry initial constraints at lines 3849–3851:
\(de_u=dF\wedge e_u\);
\(de_l\wedge e_u=de_n\wedge e_u=0\);
the required formula for \(\mathfrak c\) holds; and the antisymmetric screen Lie-derivative expression is zero, equal to \(f_b\). The initial Riemannian metric is complete because \(F,G\) are bounded, so its coefficients are uniformly bounded above and below by positive constants.

For completeness, an actual flow realizing the example is
\[
\begin{gathered}
 \Phi_t(x,y,z)=(x+t e^{-F(y)},y,z),\qquad
 \lambda_t=1,\quad \mathfrak f_t=0,\\
 e_{tu}=e^{F(y)}dx-tF'(y)dy,\qquad
 e_{tl}=e^{G(x+t e^{-F(y)})}dy,\qquad e_{tn}=dz,\\
 \phi_t=e^{iF(y)},\qquad a_t=0,\qquad
 b_t=t\,e^{F(y)}F'(y)\,dx\wedge dy.
\end{gathered}
\]
It satisfies the evolution and constraint equations in
eq:NSNSspecializedevolution and eq:NSNSspecializedconstraints directly.
Its metric \(-dt^2+h_{\mathfrak e_t}\) has Cauchy slices: on every bounded time interval the spatial metrics are uniformly equivalent to the Euclidean metric, which prevents a causal curve from escaping spatially at finite time. Thus the example can meet the global-hyperbolicity hypothesis as well as the local equations.

At \(t=0\), write
\[
 w=F'(y)e^{-G(x)},\qquad A=-G'(x)e^{-F(y)}.
\]
The second fundamental form specified by the paper is
\[
 \Theta=\frac{w}{2}(e_u\otimes e_l+e_l\otimes e_u)
          +A\,e_l\otimes e_l.
\]
Here \(\gamma=dF=w e_l\) is closed. Direct covariant differentiation gives
\[
 (\nabla_U\Theta)(U,L)=\frac32Aw,\qquad
 (\nabla_L\Theta)(U,U)=Aw.
\]
At \(x=y=z=0\), \(w=1\), \(A=-1\). Thus the left-hand side of line 3751 is \(-1/2\), whereas its right-hand side is zero. The missing term is exactly
\(\tfrac12\Theta(\gamma^\sharp,L)=-1/2\).

Effect on conclusions

This invalidates the displayed inference at line 3751 and the derivation at line 3769 as written. In particular, that derivation cannot discard this term when equating the two Ricci-tensor expressions. Inserting the corrected identity supplies the missing contraction and should be followed through the remaining algebra.

This is not a counterexample to equation eq:constraintidentities0, the final statement of Theorem 4.30. Indeed, the final identity is consistent with this example when the calculation is done correctly. The finding concerns the validity of the submitted proof. Theorem 4.35 (label thm:susyflowcompatibility) subsequently uses Theorem 4.30; its justification inherits the need to repair this proof, although no counterexample to that theorem was found.

2. Incorrect description of the zero rank-one invariant

Exact location: paper.tex line 1251, the paragraph after Corollary cor:torsionflat.

The statement that \([\kappa]=[\rho]=0\) makes the connection preserve “a conformal transformation of every representative” is not correct if “conformal transformation” has its usual meaning of multiplying the coframe by a common nonzero function. Equation eq:kapparhogauge instead supplies a null-rotation gauge change that makes both connection forms vanish.

For example, start with a constant null coframe \((u,v,l,n)\) and its flat Levi-Civita connection. For a nonconstant function \(a\), replace it by
\[
 u'=u,\qquad v'=v-\tfrac12a^2u+a l,\qquad
 l'=l-a u,\qquad n'=n.
\]
Then \(\kappa'=-da\), \(\rho'=0\), so both cohomology classes vanish. If a common rescaling \(s(u',v',l',n')\) were parallel, parallelity of \(su'\) would force \(ds=0\); parallelity of \(sl'\) would then fail wherever \(da\ne0\). A gauge change, not a common conformal rescaling, restores a parallel coframe.

This is a noncentral, readily corrected assertion. The ensuing conclusion of trivial holonomy is correct after using the gauge change, and this correction does not affect the main development or rigidity results.

Harmless notation and transcription errors

These are distinct from the nonzero missing term above:

- At line 1162, the first two terms in the displayed formula for \(\mathcal L_u g\) contain extra exterior-derivative symbols on the coframe factors. The intended terms are \((\iota_Udu)\odot v+u\odot(\iota_Udv)\), as is clear from the following expansion.
- At line 3083, the undefined \(\beta_t\) in \(\Theta_t(\beta_t^\sharp)\) should be \(\varphi_{\phi_t}\).
- At line 5329, the dilaton uses \(T+z\), although the time coordinate in that example is \(t\).
- The last sentence of Theorem 4.41, line 4777, reverses the direction of proportionality if read literally. The proof establishes \(\varphi_{\bar\phi}=c\,u\), allowing \(c=0\); a nowhere-vanishing \(u\) cannot be a multiple of a zero dilaton curvature.

Review coverage and limitations

I read the entire source and assessed the argument from the spinor/coframe correspondence through the two Cauchy problems and the final examples. Particular attention was given to the normalized evolution, the constancy obstruction, arbitrary-lapse uniqueness, the time-independent development, the constraint compatibility calculations, and all six steps of the compact rigidity proof.

The leafwise averaging argument in Lemma 4.38 was examined including its weak derivatives, closure of exact forms, smoothing by the commuting measure-preserving flows, and the weighted pairing. I did not find a substantive error in that argument. I also checked the compact-leaf/dense-leaf distinction, the positive weighting in Step 4 of Theorem 4.41, and the symmetric trace-free curvature-matrix argument in Step 5; no additional substantive error was found there.

The global-hyperbolicity assertion in Corollary 3.27 would benefit from an explicit justification before its maximality argument. The missing short argument is available: for
\(g=h-e^{-\mathfrak f}dt\odot e_u\) and
\(q=e^{2\mathfrak f}h\), any causal tangent \((\dot t,v)\) satisfies
\(|v|_q\le2|\dot t|\). Completeness of \(q\) then excludes spatial escape at finite \(t\) and proves that the slices are Cauchy. I do not regard this readily supplied step as a separate substantive counterexample.

I did not independently reprove every cited background theorem or every lengthy component expansion. References were read as part of the paper's bibliography, not retrieved. This was an ordinary mathematical review with direct calculations, not formal verification. The verdict rests on the explicit false identity and invalid inference identified in item 1, with the limits on its consequences stated above.

