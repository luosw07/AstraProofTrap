REJECT

I found an incorrect tensor-differentiation identity in the proof of the constraint compatibility theorem. The omitted term can be nonzero on a smooth, globally defined supersymmetry flow with compact Cauchy hypersurface. Thus this is a mathematical error in the supplied argument, not merely a notational typo. It does not by itself disprove the theorem's final statement: the indicated correction appears to repair this part of the calculation.

## Substantive finding

**Location:** Theorem with TeX label `thm:compatibilityflows`, proof, unnumbered display at **TeX lines 3749–3752, specifically line 3751**, and its subsequent use in the concluding calculation at **line 3769**. All line references in this report refer to the supplied `paper.tex`.

Fix a time and abbreviate

\[
U=e_{tu}^{\sharp},\qquad L=e_{tl}^{\sharp},\qquad
c=\widehat c_t(U,\cdot),\qquad \Theta=\Theta_t,\qquad \nabla=\nabla^{h_t}.
\]

The displayed identity at line 3751 is

\[
(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12\,dc(U,L).
\]

It is asserted to follow from
\(d(\Theta(U,\cdot))=\tfrac12dc\). But differentiating the contraction with the varying field \(U\) gives

\[
\begin{aligned}
d(\Theta(U,\cdot))(U,L)
={}&(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)\\
&+\Theta(\nabla_UU,L)-\Theta(\nabla_LU,U).
\end{aligned}
\]

The paper's own connection formula in Remark `remark:covariantevolution` (lines 3541–3544) implies

\[
\nabla_UU=-\Theta(U,\cdot)^\sharp+\Theta(U,U)U-\tfrac12c^\sharp,
\quad
\nabla_LU=-\Theta(L,\cdot)^\sharp+\Theta(U,L)U.
\]

By symmetry of \(\Theta\), the quadratic terms cancel, leaving

\[
\Theta(\nabla_UU,L)-\Theta(\nabla_LU,U)
=-\tfrac12\Theta(c^\sharp,L).
\]

Consequently, the correct identity is

\[
\boxed{
(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12dc(U,L)+\tfrac12\Theta(c^\sharp,L).
}
\]

There is no hypothesis in this theorem forcing the last term to vanish. The theorem concerns supersymmetry flows before imposing the bosonic constraint equations, so vanishing cannot be supplied by those equations either.

### Explicit example showing the omission is nonzero

Take the three-torus with angular coordinates \((s,x,y)\), each of period \(2\pi\), and set

\[
e_u=e^{\sin x}\,ds,\qquad e_l=e^{\sin s}\,dx,\qquad e_n=dy,
\qquad \mathfrak f=0.
\]

On a trivial gerbe take initial curving \(b=0\), and choose

\[
\phi=e^{i\sin x},\qquad \varphi_\phi=\cos x\,dx,
\qquad \mathfrak c=e_u\wedge\varphi_\phi,
\qquad f_b=0.
\]

These satisfy the supersymmetry initial constraints in lines 3849–3851:

* \(de_u=\varphi_\phi\wedge e_u\).
* \(de_l\wedge e_u=de_n\wedge e_u=0\).
* \(\mathfrak c=f_b*e_u+e_u\wedge\varphi_\phi\).
* Both screen-mixing terms in the scalar rotation constraint vanish, as does \(f_b\).

One can exhibit the whole flow, rather than merely relying on a formal initial jet. Let

\[
X=e^{-\sin x}\partial_s,\qquad
\Phi_t(s,x,y)=(s+t e^{-\sin x},x,y),
\]

and take

\[
\lambda_t=1,\quad \mathfrak f_t=0,\quad
\mathfrak e_t=\Phi_t^*\mathfrak e,\quad
\phi_t=\phi,\quad a_t=0,\quad b_t=t\mathfrak c.
\]

Here \(d\mathfrak c=0\) and \(\Phi_t^*\mathfrak c=\mathfrak c\), so the derived two-form is \(\widehat c_t=\mathfrak c\) and the spatial gerbe curvature stays zero. The evolution and spatial constraints in `eq:NSNSspecializedevolution` and `eq:NSNSspecializedconstraints` hold. The resulting smooth metric \(-dt^2+h_{\mathfrak e_t}\) on \(\mathbb R\times T^3\) has Cauchy slices: on each bounded time interval its spatial metrics are uniformly comparable to a fixed metric on the compact torus. Thus this is an admissible globally hyperbolic supersymmetry flow of the type used in the theorem.

At time zero, put

\[
U=e^{-\sin x}\partial_s,\quad L=e^{-\sin s}\partial_x,
\quad B=e^{-\sin s}\cos x,\quad K=e^{-\sin x}\cos s.
\]

Then

\[
[U,L]=BU-KL,
\quad \nabla_UU=-BL,\quad \nabla_UL=BU,
\quad \nabla_LU=KL,
\]

and, from \(\Theta=-\tfrac12\mathcal L_Xh\),

\[
\Theta(U,U)=0,\qquad \Theta(U,L)=B/2,
\qquad \Theta(L,L)=-K.
\]

Also \(c=\iota_U\mathfrak c=\cos x\,dx\), so \(dc=0\). At \(s=x=0\), one has \(B=K=1\) and

\[
(\nabla_U\Theta)(U,L)=-\tfrac32,
\qquad (\nabla_L\Theta)(U,U)=-1.
\]

The left-hand side of the printed identity is therefore \(-1/2\), while its right-hand side is zero. The missing term is exactly
\(\tfrac12\Theta(c^\sharp,L)=-1/2\).

### Effect on the conclusions

This identity is explicitly used to derive the transverse momentum/Maxwell compatibility relation at line 3769, which is part of the theorem's claimed identity
\(\mathcal H_t e_{tu}=2\mathcal W_t+*\mathcal M_t\).
The proof as printed loses a nonzero term in the comparison of the two Ricci expressions. In particular, the \(\tfrac12\Theta(c^\sharp,L)\) appearing in the second Ricci expression (line 3744) is cancelled by the omitted term when the differentiation is done correctly. It cannot be discarded using the printed line 3751.

Adding the missing term restores that cancellation, and the stated compatibility relation is consistent with the example above. I therefore **do not claim a counterexample to the final compatibility identity**, to the development theorems, or to compact rigidity. The finding is a concrete algebraic failure in a central proof and the associated unjustified inference as currently written. The later compatibility/propagation theorem uses this result, so its presented chain of justification requires this repair as well.

## Minor typographical issues, distinguished from the finding above

These do not supply the reason for the verdict:

* **Line 1162**, in the proof of `thm:existencenullcoframeII`, writes terms such as \(du(u)\odot dv\) in a formula for a symmetric two-tensor. The intended terms are \((\iota_u du)\odot v+u\odot(\iota_u dv)\), as the next lines make clear. This is a type/notation typo in the displayed expansion.
* **Line 3083**, Lemma `lemma:hyperbolicderivatives`, contains \(\Theta_t(\beta_t^\sharp)\) although \(\beta_t\) is not defined in that statement. The intended argument is the spatial one-form \(\varphi_{\phi_t}\); the subsequent calculations use it that way.
* **Line 5329**, in the final example, uses \(T\) in \(e^{im(T+z)}\) although the time coordinate is \(t\). The following curvature statement and the remainder of the example identify the intended expression.

## Review coverage and limitations

I read the complete supplied TeX source, **lines 1–5440**, including the introduction, all four sections, all proofs and examples, and the bibliography. I did not inspect other workspace material, other reports, or other versions of the paper, and did not consult external sources or agents. The TeX, rather than a separate PDF inspection, was the reviewed representation.

I followed the full logical chain: spinorial forms and the torsion exterior system; hypersurface reduction; the normalized pullback/rotation construction and null-current uniqueness; stationary developments and the two branches of initial data; gerbe and dilaton reduction; bosonic and supersymmetry constraints; compatibility and propagation; and the compact rigidity argument. I checked key signs and contractions and scrutinized the global parts of the flow arguments. For example, the claimed global hyperbolicity under completeness of \(q=e^{2\mathfrak f}h\) has the direct supporting estimate \(|dx/dt|_q\leq2\) for causal curves in the stationary metric, although that estimate is not written out in the corollary's proof.

I examined the leafwise averaging lemma in detail. Its use of the closure of leafwise gradients, weak closedness and coclosedness, regularization by the commuting measure-preserving flows, and the integrated flat Weitzenböck identity does not require compact individual leaves. I found no substantive failure in that lemma or in the subsequent weighted determinant argument for compact rigidity. In particular, I did not treat dense leaves as compact leaves or assume an unjustified leafwise normalized integral.

This was an ordinary mathematical review, not formal verification. I did not independently reproduce every long component expansion in the scalar curvature and Einstein-defect computations. Results invoked from the bibliography were assessed in their stated role; their original proofs were not checked. Apart from the explicit proof error documented above and the noted typos, I did not establish another substantive error or a counterexample to a principal theorem.
