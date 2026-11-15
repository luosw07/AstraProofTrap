REJECT

I found a substantive, explicitly falsifiable intermediate identity in the proof of the constraint-compatibility theorem. The missing term is generally nonzero even for a smooth supersymmetry flow on a compact three-torus. This is a defect in the written proof, not a counterexample to the final constraint identity or to the compact rigidity theorem. The defect appears repairable, but the present derivation is not correct as printed.

## Review scope

I read the complete supplied `paper.tex`, lines 1–5440, in bounded, numbered chunks, including all proofs, examples, and the bibliography. I reviewed the spinorial/coframe reduction, the skew-torsion evolution and constraint system, local uniqueness and the stationary development, the contact/integrable branches, the gerbe reduction, the Neveu–Schwarz reduction, the supersymmetry compatibility arguments, and the leafwise averaging and compact rigidity proof. I used only this paper as mathematical input; I did not consult other versions, other workspace files, other reviewers, or outside references. No formal proof assistant was used. The review is of the TeX mathematical content; I did not separately inspect the rendered PDF.

## 1. Substantive algebraic omission in the proof of Theorem `thm:compatibilityflows`

**Location:** TeX lines 3749–3752, particularly the displayed equation at line 3751; its use in the conclusion at line 3769. The theorem itself is stated at lines 3657–3667, with main equation `eq:constraintidentities0`.

Fix a time and abbreviate

\[
U=e_{tu}^{\sharp},\quad L=e_{tl}^{\sharp},\quad
T=\Theta_t,\quad q=\widehat c_t(U,-).
\]

The preceding constraint does imply

\[
d(T(U,-))=\tfrac12dq.
\]

The paper then claims

\[
(\nabla_U T)(U,L)-(\nabla_L T)(U,U)
=\tfrac12dq(U,L).
\tag{printed line 3751}
\]

This drops the derivatives of the vector field in the contraction `T(U,-)`. In fact the product rule gives

\[
\begin{aligned}
d(T(U,-))(U,L)
={}&(\nabla_U T)(U,L)-(\nabla_L T)(U,U)\\
&+T(\nabla_UU,L)-T(\nabla_LU,U).
\end{aligned}
\]

The covariant coframe formula at line 3542 gives

\[
\nabla_XU=-T(X,-)^{\sharp}+T(U,X)U-\tfrac12 e_{tu}(X)q^{\sharp}.
\]

Since `T` is symmetric, its contributions to the last two terms cancel except for

\[
T(\nabla_UU,L)-T(\nabla_LU,U)=-\tfrac12T(q^{\sharp},L).
\]

Consequently the correct formula is

\[
\boxed{
(\nabla_U T)(U,L)-(\nabla_L T)(U,U)
=\tfrac12dq(U,L)+\tfrac12T(q^{\sharp},L).
}
\]

There is no hypothesis in this theorem forcing the extra contraction to vanish.

### Explicit admissible periodic example

Here is a check entirely within the paper's systems. Take the three-torus with angular coordinates `(x,y,z)`, orientation `dz∧dx∧dy`, and put

\[
a=\sin x,\quad b=\sin z,\qquad
e_u=e^a dz,\quad e_l=e^b dx,\quad e_n=dy,
\]

\[
\mathfrak f=0,\quad \phi=e^{i\sin x},\quad
\varphi_\phi=da,\quad H_{b_0}=0,\quad
\mathfrak c=e_u\wedge da.
\]

Choose the trivial gerbe and the zero initial curving. The symbol `b` in the first display is only the scalar `sin z`; `b_0` denotes the initial curving.

These data satisfy the supersymmetry constraints: `de_u=da∧e_u`, `de_l∧e_u=de_n∧e_u=0`, and the scalar rotation constraint is zero, so `f_{b_0}=0`. Also `d𝔠=0`. The vector field

\[
U=e^{-a}\partial_z
\]

has the complete flow

\[
\Phi_t(x,y,z)=(x,y,z+t e^{-a(x)}).
\]

One can verify a full supersymmetry flow, independently of the disputed compatibility identity, by taking

\[
\lambda_t=1,\quad\mathfrak f_t=0,\quad
\mathfrak e_t=\Phi_t^*\mathfrak e,\quad
\phi_t=\phi,\quad a_t=0,\quad b_t=t\mathfrak c.
\]

Here `Φ_t*𝔠=𝔠`, `H_{b_t}=0`, `ĉ_t=𝔠`, and `p_t=0`. The temporal and spatial equations `eq:susyevol` hold; they can also be checked directly from

\[
e_{tu}=e^{\sin x}dz-t\cos x\,dx,\quad
e_{tl}=e^{\sin(z+t e^{-\sin x})}dx,\quad e_{tn}=dy.
\]

The metric `-dt²+h_{𝔢_t}` is globally hyperbolic with these compact slices: on every bounded time interval the smooth slice metrics have uniform positive lower bounds, so an inextendible causal curve cannot stop at a finite time.

At `t=0`, let

\[
L=e^{-b}\partial_x,\quad N=\partial_y,\qquad
s=e^{-b}\cos x,\quad B=-e^{-a}\cos z.
\]

Then `[U,L]=sU+BL`, and the Levi–Civita connection is

\[
\nabla_UU=-sL,\quad \nabla_UL=sU,\quad
\nabla_LU=-BL,\quad \nabla_LL=BU,
\]

with all contributions involving `N` zero. From `T=-½𝓛_Uh` one gets

\[
[T]_{(U,L,N)}=
\begin{pmatrix}
0&s/2&0\\
s/2&B&0\\
0&0&0
\end{pmatrix}.
\]

Moreover `q=da=s e_l` is closed and `U(s)=Bs`. Thus

\[
(\nabla_U T)(U,L)=\tfrac32 Bs,
\qquad (\nabla_L T)(U,U)=Bs.
\]

The left side of line 3751 is therefore `Bs/2`, while its printed right side is zero. At `x=z=0`, these values are `-1/2` and `0`, respectively. The omitted term `½T(q♯,L)` is exactly `-1/2` there.

**Effect on conclusions.** Line 3769 explicitly uses this identity to infer the transverse momentum/Maxwell relation. The omitted contraction changes the coefficient of an actual nonzero tensor term, so this is more than a notation or index typo. The displayed chain of reasoning does not establish that conclusion as written. Restoring the contraction is compatible with the claimed final formula: in the example, direct calculation gives `𝓦(L)=Bs/2` and `(*𝓜)(L)=-Bs`, so the theorem's final identity itself is not contradicted. A corrected substitution can plausibly repair this proof. My rejection concerns the false intermediate assertion and its use, not a demonstrated counterexample to Theorem `thm:compatibilityflows`, Theorem `thm:susyflowcompatibility`, or compact rigidity.

## 2. Nonessential but literally incorrect use of “conformal transformation”

**Location:** TeX line 1251, the paragraph immediately after Corollary `cor:torsionflat`.

The paragraph says that when the rank-one invariant vanishes, the connection “preserves a conformal transformation of every representative.” Exact `κ,ρ` allow a **null-rotation gauge change** using `eq:kapparhogauge`; they do not generally allow a conformal rescaling of the representative to be parallel.

For example, start with a constant null coframe `(u,v,l,n)` in flat Minkowski space and choose a nonconstant function `f`. The same isotropic parallelism has representative

\[
(u,\ v-\tfrac12f^2u+fl,\ l-fu,\ n).
\]

Its auxiliary forms are `κ'=-df, ρ'=0`, so the invariant vanishes. If multiplication of this coframe by a common nonzero conformal factor `Ω` made it parallel, the `u` equation would force `dΩ=0`; the `l-fu` equation would then still contain `-Ω df⊗u` and would not vanish.

**Effect on conclusions.** The intended conclusion of trivial holonomy is correct: undo the null rotation. This is a correctable terminology/assertion error in an explanatory paragraph and is not the basis for rejecting the main results.

## 3. A short global-hyperbolicity justification should be supplied

**Location:** Corollary `cor:timeindependentdevelopment`, item (3), lines 2441 and 2537–2573.

The proof establishes completeness of the spatial flow from completeness of `q=e^{2𝔣}h_𝔢`, and then proceeds directly to maximality among globally hyperbolic developments. It does not explicitly show global hyperbolicity of the stationary product itself. This omission is readily repairable and is not a substantive obstruction to the result.

Indeed, conformally rescale its metric to

\[
\widetilde g=q-dt\odot\vartheta,
\qquad \vartheta=e^{\mathfrak f}e_u,
\qquad |\vartheta|_q=1.
\]

For a causal tangent `(\dot t,\dot x)`,

\[
|\dot x|_q^2\le 2|\dot t|\,|\dot x|_q,
\qquad\text{hence}\qquad
|dx/dt|_q\le2.
\]

The slices are spacelike and `dt` is timelike. Completeness of `q` implies that any causal curve with finite limiting time has a spatial limit and can be extended. Thus every inextendible causal curve crosses every time slice. This supplies the needed global-hyperbolicity step before the subsequent complete-null-current maximality argument.

## Other checks and limitations

The main flow construction and its obstruction are coherent: Lie transport fixes the metric and current up to pullback, the complex screen phase yields `dr=0`, and straightening the null Killing current gives the stated local uniqueness and stationary form. The contact-branch reconstruction and the explicit torus-bundle construction are internally consistent. The use of external classification/existence theorems is identifiable, but I did not verify those references outside the supplied paper.

The leafwise averaging lemma at lines 4547–4768 addresses the dense-leaf difficulty rather than silently integrating over a noncompact leaf. The volume-preserving commuting flows, projection onto the closure of leafwise gradients, weak closed/coclosed remainder, flow convolution, and the integrated flat identity give the required parallel remainder. I found no substantive error in that argument. I also checked the compact rigidity proof's positive weighted integral, the determinant pairing, and the symmetric trace-free curvature-matrix argument; these are consistent with the stated constraints.

There are ordinary presentation slips, such as the undefined `β_t` in line 3083 where the differentiated one-form is `varphi_{phi_t}`, the ill-typed first line at 1162 before its correctly typed expansion, and the uppercase `T` in the last example's `e^{im(T+z)}` at line 5329 despite the coordinate being `t`. These can be corrected locally and do not independently undermine their surrounding conclusions.

I have not recomputed every lengthy curvature component independently or proved the cited spinor-square and topology results from first principles. This is a full-paper mathematical review with a concrete proof defect, not a formal verification or a claim that every principal theorem is false.
