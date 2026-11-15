REJECT

I found an incorrect tensor identity in the proof of the constraint-compatibility theorem. It is used in the derivation of the transverse momentum identities, and it fails on smooth, compact, admissible supersymmetric initial data. This is an error in the argument, rather than a counterexample to the theorem's final statement. A corrected derivation is needed before I can accept the complete paper as mathematically justified.

## Substantive issue: a missing term in the compatibility proof

**Location:** Theorem `thm:compatibilityflows`, proof, the displayed equation at TeX lines **3749–3752**, specifically line **3751**. Its subsequent use is at lines **3762–3769**. All line numbers refer to the supplied `blind/r8p6/paper.tex`.

Suppress the time index and write

\[
U=e_u^\sharp,\qquad L=e_l^\sharp,\qquad c=\widehat c(U,\cdot).
\]

The displayed equation asserts

\[
(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12\,dc(U,L).
\tag{*}
\]

The equation preceding it, namely
\(d(\Theta(U,\cdot))=\tfrac12dc\), does not imply (*), because differentiation must also act on the vector field inserted into \(\Theta\). In fact,

\[
\begin{aligned}
d(\Theta(U,\cdot))(U,L)
={}&(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)\\
&+\Theta(\nabla_UU,L)-\Theta(\nabla_LU,U).
\end{aligned}
\]

The paper's own covariant derivative formula at line **3542** gives

\[
\nabla_X U=-\Theta(X,\cdot)^\sharp+\Theta(U,X)U
-\tfrac12 e_u(X)c^\sharp.
\]

Using the symmetry of \(\Theta\), the last two terms in the preceding exterior-derivative calculation combine to
\(-\tfrac12\Theta(c^\sharp,L)\). Consequently the correct identity is

\[
(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12dc(U,L)+\tfrac12\Theta(c^\sharp,L).
\tag{**}
\]

There is no condition in the theorem requiring the additional term to vanish.

### Explicit admissible example demonstrating the failure

Let \(\Sigma=(\mathbb R/2\pi\mathbb Z)^3\), with coordinates \((x,y,z)\), and take

\[
e_u=e^{\sin x}dz,\qquad e_l=e^{\sin z}dx,\qquad e_n=dy,
\qquad \mathfrak f=0,
\]

\[
\phi=e^{i\sin x},\qquad \varphi_\phi=\cos x\,dx,
\qquad b=0,\quad H_b=0,\quad f_b=0,
\qquad \mathfrak c=e_u\wedge\varphi_\phi.
\]

Here (b=0) can be taken on the trivial gerbe. These data satisfy every supersymmetry constraint in `eq:NSNSsusyconstraintsI` and `eq:NSNSsusyconstraintsII`:

* \(de_u=\varphi_\phi\wedge e_u\).
* \(de_l\wedge e_u=de_n\wedge e_u=0\).
* The required formula for \(\mathfrak c\) holds by definition.
* \(\mathcal L_Ue_n=0\) and \(\mathcal L_Ue_l\) is proportional to \(e_l\), so the scalar rotation constraint is zero, as required by \(f_b=0\).

The vector field \(U=e^{-\sin x}\partial_z\) is complete. Its flow is
\(\Phi_t(x,y,z)=(x,y,z+t e^{-\sin x})\). With \(\lambda_t=1\), \(\mathfrak f_t=0\), \(\mathfrak e_t=\Phi_t^*\mathfrak e\), \(\phi_t=\phi\), and
\(b_t=\int_0^t\Phi_s^*\mathfrak c\,ds\), the specialized evolution and constraint equations of the paper are satisfied directly. In particular \(d\mathfrak c=0\), so \(H_{b_t}=0\) and \(\widehat c_t=\Phi_t^*\mathfrak c\). This supplies an actual supersymmetry flow, not merely arbitrary choices of tensors. The metric \(-dt^2+\Phi_t^*h\) is globally hyperbolic with compact spatial slices: on every bounded time interval its spatial metrics are uniformly equivalent to a fixed metric on the compact torus.

At time zero put

\[
q=\cos x\,e^{-\sin z},\qquad A=\cos z\,e^{-\sin x}.
\]

Then \(c=\varphi_\phi=q e_l\), so \(dc=0\). The second fundamental form and relevant connection coefficients are

\[
\Theta=\tfrac12 e_u\odot\varphi_\phi-Ae_l\otimes e_l,
\]

\[
\nabla_UU=-qL,\qquad \nabla_UL=qU,\qquad
\nabla_LU=AL.
\]

Thus \(\Theta(U,U)=0\), \(\Theta(U,L)=q/2\), \(\Theta(L,L)=-A\), and \(U(q)=-Aq\). It follows that

\[
(\nabla_U\Theta)(U,L)=-\tfrac32Aq,\qquad
(\nabla_L\Theta)(U,U)=-Aq.
\]

The left side of (*) is therefore \(-Aq/2\), while its right side is zero. At \(x=z=0\), these values are \(-1/2\) and \(0\), respectively. The missing term in (**) is precisely \(-Aq/2\).

### Effect on the claimed conclusions

Line **3769** explicitly uses this identity when deriving the transverse component of `eq:constraintidentities`, and thus the proof as written contains a substantive unjustified inference. The constraint-compatibility theorem is then used in the propagation theorem `thm:susyflowcompatibility` and the subsequent characterization of supersymmetric solutions.

I do **not** claim that those theorem statements are false. Indeed, in the example above the final transverse identity itself remains consistent: \(\mathcal W(L)=-Aq/2\) and \((*\mathcal M)(L)=Aq\). This distinguishes the demonstrated error from a counterexample to the final conclusion. It also means that simply calling the omitted summand zero cannot repair the proof; the calculation leading to line 3769 must be revisited and the cancellations checked with (**).

## Lesser presentation issues

These do not independently determine the verdict.

* Line **1162** has exterior derivatives in places where the coframe one-forms themselves are needed in the Lie derivative of the metric. The next lines give the intended expansion, so this appears to be a typesetting error.
* Line **1251** says that exact rank-one invariants allow the connection to preserve a “conformal transformation” of every representative. The transformation supplied by `eq:kapparhogauge` is a null-frame gauge transformation, not a conformal rescaling. The asserted triviality of holonomy follows from that gauge transformation; the wording should be corrected.
* The final sentence of the compact rigidity theorem at line **4777** reverses the proportionality stated and proved later. The proved conclusion is \(\varphi_{\bar\phi}=c u\), including \(c=0\), rather than \(u=c\varphi_{\bar\phi}\). The latter literal formulation fails for a constant dilaton and a nonzero Dirac current. Lines **5210–5228** make the intended conclusion clear.

## Coverage and limitations

I read the entire supplied standalone TeX source, lines 1–5440, including the introduction, all theorem statements and proofs, examples, and bibliography. The initially truncated portion of a tool output was reread in a bounded chunk. I did not inspect another version, other reports, private records, or external mathematical sources, and did not consult other agents or use a formal proof assistant.

The review covered the spinor/parallelism translation, the constrained evolution and its explicit integration, the uniqueness and stationary-development arguments, the contact and integrable branches, the gerbe reduction, the bosonic and supersymmetry flows, constraint compatibility and propagation, and the leafwise averaging and compact rigidity arguments. In particular, the leafwise averaging proof uses an orthogonal projection onto a closed subspace and smoothing by the commuting measure-preserving flows; I did not find the dense-leaf issue itself to invalidate that proof.

The source was my mathematical representation; I did not separately inspect the rendered PDF. I treated cited external results as stated in the paper and did not verify those sources. This was a mathematical review, not a complete independent recomputation of every lengthy curvature expansion. The rejection rests on the explicit, locally checkable incorrect identity above.
