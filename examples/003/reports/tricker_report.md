# Tricker report

## 1. Sole modification and its actual meaning

Modified §13.5, line 8694, changes the central-translation convention

\[
[qz,x]=[q,zx]
\]

to

\[
[qz,x]=[q,z^{-1}x]. \tag{*}
\]

The new convention itself defines valid central translation: translation by the inverse torsor \(Q^{-1}\) under the original convention. It still preserves the adjoint bundle and adjoint determinant line. The error is that later comparisons retain the original central-arc action, finite pairing, and transgression without inverting this action.

In particular, lines 8779–8781 still say “A change of lift by \(z\) changes the translated frame by \(z\)”; (*) actually gives \(z^{-1}\). The localization comparison at line 8784 and Theorem 13.5's `eq:G7` use this change.

## 2. Shortest geometric test

Take the trivial central torsor \(Q=X\times Z\) with unit section \(q_0\). For a fixed bundle \(E\), trivialize by

\[
t_{q_0}:E\longrightarrow\tau_Q(E),\qquad x\longmapsto[q_0,x]
\]

The torsor automorphism \(a_z:q\mapsto qz\) gives under the new convention

\[
[q_0,x]\longmapsto[q_0z,x]=[q_0,z^{-1}x]. \tag{1}
\]

It therefore induces the bundle's central automorphism \(z^{-1}\). Equivalently, changing section \(q_0\mapsto q_0z\) gives

\[
t_{q_0z}=t_{q_0}\circ z^{-1}. \tag{2}
\]

This reverses the equality used at line 8780. Both conventions give identity translation on the trivial torsor as an **object**, but differ on its **automorphisms**. Centers of exponent at most two hide the difference; an order-three center detects it.

The following nonzero object satisfies the paper's hypotheses and turns this distinction into an impossible natural isomorphism, beyond a mere frame-notation difference.

## 3. Allowed group, curve, and level

Take

\[
G=\mathrm{SL}_3(\mathbb C),\quad
G^\vee=\mathrm{PGL}_3(\mathbb C),\quad
Z_G=\mu_3,\quad r=1,\quad h^\vee=3.
\]

Let \(X\) be any smooth projective connected complex genus-two curve, with a fixed theta characteristic. Set

\[
c=-\sqrt2,\quad a=-c=\sqrt2,\quad
 d=1/\sqrt2,\quad
 s=-\frac{a-3}{6}=\frac{3-\sqrt2}{6}\notin\mathbb Q.
\]

These are the actual parameters of the main theorem, `foundations:levels`, and `foundations:four-categories`. Put

\[
Q=X\times\mu_3,\qquad
\zeta^2+\zeta+1=0,\quad\zeta\ne1,
\qquad \eta(\zeta)=\zeta.
\]

The paper retains the actual group's central characters, and `equivalence:central` explicitly requires naturality for the full torsor groupoid, so \(a_\zeta\) must be tested.

## 4. Explicit nonzero \(\eta\)-character sector

### 4.1 A stable \(\mathrm{SL}_3\)-bundle

Consider

\[
A=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},
\qquad
B=\operatorname{diag}(1,\zeta,\zeta^2).
\]

They satisfy

\[
\det A=\det B=1,\qquad A^3=B^3=I,
\qquad [A,B]=\zeta^2I.
\]

and generate the finite Heisenberg group of order 27,

\[
H=\{\zeta^k A^iB^j:0\le i,j,k<3\}\subset\mathrm{SL}_3.
\]

The representation is irreducible: \(B\) has three distinct eigenvalues, so invariant subspaces are sums of its eigenlines; \(A\) permutes all three transitively, leaving only zero and the whole space invariant under both.

The genus-two surface fundamental group has relation \([a_1,b_1][a_2,b_2]=1\). The assignment

\[
a_1\mapsto A,\quad b_1\mapsto B,\quad
 a_2\mapsto B,\quad b_2\mapsto A
\]

satisfies it and surjects onto \(H\). Riemann existence for finite coverings gives a connected finite étale Galois cover \(\pi:Y\to X\) with group \(H\). The associated algebraic vector bundle

\[
E=(Y\times\mathbb C^3)/H
\]

has fixed trivial determinant and \(\pi^*E\simeq\mathcal O_Y^3\).

Stability follows directly. Any proper nonzero saturated subbundle \(F\subset E\) pulls back to a subbundle of a trivial bundle. A nonzero Plücker component of its determinant gives \(\deg\pi^*F\le0\), hence \(\deg F\le0\). Equality would make the map \(Y\to\operatorname{Gr}(\operatorname{rk}F,3)\) pull back the Plücker ample line bundle to degree zero, forcing it to be constant. Then \(\pi^*F=\mathcal O_Y\otimes W\) for a fixed proper nonzero subspace \(W\subset\mathbb C^3\); descent makes \(W\) invariant under \(H\), contradicting irreducibility. Every proper saturated subbundle thus has strictly negative degree, so \(E\) is stable.

Stability gives \(\operatorname{Aut}_{\mathrm{GL}_3}(E)=\mathbb C^\times\). Preserving the determinant trivialization gives \(\operatorname{Aut}_{\mathrm{SL}_3}(E)=\mu_3\).

### 4.2 A nonzero twisted \(D\)-module

Inside the stable-bundle open, the residual gerbe of \(E\) is the closed fiber over its stable coarse-moduli point:

\[
i:B\mu_3\hookrightarrow\operatorname{Bun}_{\mathrm{SL}_3}^{\mathrm{st}}.
\]

The center acts trivially on the adjoint representation \(\mathfrak{sl}_3\), hence on \(L_G|_E=\det R\Gamma(X,\operatorname{ad}E)\), exactly the convention at original lines 344–347 and 8632–8633. Thus the \(L_G^s\) twist on \(B\mu_3\) is trivial, and its \(D\)-module category contains the one-dimensional representation \(k_\eta\).

Let \(j\) embed the stable open in the whole bundle stack, and set

\[
\mathcal F=j_*i_*k_\eta\in A=D(L_G^s).
\]

Kashiwara full faithfulness for the closed image and \(j^!j_*\simeq\mathrm{Id}\) show \(\mathcal F\ne0\), with central character \(\eta\). The required sector thus contains a nonzero object in the actual irrationally twisted category.

## 5. Rigorous contradiction in subsequent natural comparisons

### 5.1 The localization comparison already fails

Original `equivalence:localization` and lines 8670–8673 state that \(L\) is essentially surjective and preserves central characters, so there is \(V\) in KL's \(\eta\)-sector with \(L(V)\simeq\mathcal F\).

At lines 8751–8754, `V[Q]` still descends through the unchanged central-arc action. The torsor automorphism \(a_\zeta\) acts on the right side \(L(V[Q])\) by \(\eta(\zeta)=\zeta\). By (1), it acts on the left side \(\tau_Q^!L(V)\) by \(\eta(\zeta^{-1})=\zeta^2\), using the paper's fixed central-character and pullback conventions. The groupoid-natural comparison required at line 8784 would intertwine distinct scalars on a nonzero object.

### 5.2 The first identity of Theorem 13.5 is actually false

\(\Phi\) is constructed before line 8694; its definition, equivalence proof, and central-character/component formula `eq:G6` are unchanged. Since \(\pi_1(\mathrm{SL}_3)=0\), that formula gives

\[
\Phi(\mathcal F)\text{ lies in component }-\eta
\text{ of }\pi_1(\mathrm{PGL}_3)=X^*(\mu_3),
\qquad \Phi(\mathcal F)\ne0.
\]

Transgression is still defined by

\[
[u_Q]=\int_X\langle[Q]\cup\operatorname{obs}\rangle,
\]

with component and automorphism conventions fixed at original lines 8705–8708 and 8722–8730. For \(a_\zeta\) of trivial \(Q\), the automorphism of \(u_Q\) on component \(-\eta\) is

\[
(-\eta)(\zeta)=\zeta^{-1}.
\]

Thus the automorphism on \(u_Q^{-1}\otimes\Phi(\mathcal F)\) is \(\zeta\), while that on newly defined \(\Phi\tau_Q^!(\mathcal F)\) is \(\zeta^{-1}=\zeta^2\).

A natural isomorphism \(\theta\) as claimed in the first `eq:G7` identity would require

\[
\theta\,\zeta^2=\zeta\,\theta,
\qquad\text{equivalently}\qquad (\zeta^2-\zeta)\theta=0. \tag{3}
\]

In \(\mathbb Q(\zeta)\),

\[
\zeta^2-\zeta=-1-2\zeta,
\qquad (\zeta^2-\zeta)^2=-3.
\]

The scalar is invertible, so (3) forces \(\theta=0\), impossible for an isomorphism on a nonzero object. This directly refutes the full-groupoid naturality conclusion in `equivalence:central`, formula (13.7).

Changing an objectwise trivialization or multiplying the comparison by a nonzero scalar preserves the distinction between central characters. Changing only the contracted-product convention while retaining transgression and character labels is not a uniform renaming of all data.

## 6. Why local checks still pass

- (*) is a valid central action; the center acts trivially on the adjoint bundle, so adjacent twist-preservation remains true.
- The adjoint Lie algebra, determinant, local differential operators, and all infinitesimal-parameter formulas are unchanged. The finite center has zero Lie-algebra differential.
- On the trivial torsor as an object, both translations are identity functors; its automorphisms must be retained to detect the difference.
- For trivial or exponent-two centers, \(z=z^{-1}\). In particular, ordinary small \(\mathrm{SL}_2\) examples pass; repeated-mark and collision examples are unaffected too.
- Earlier `eq:G6` and later finite pairing and transgression remain individually unchanged; character matching fails when they are connected to the new contracted-product action.

The shortest detector is one order-three central automorphism; the nonzero-sector certificate places it in the actual category.

## 7. Minimal repair and reproducible data

Delete the five inserted TeX characters `^{-1}` at line 8694, restoring \([qz,x]=[q,zx]\). Retaining the new action instead requires jointly adjusting localization comparison, central-torsor tensor directions on both sides of `eq:G7`, and the associated groupoid descent.

`verification.py` checks over the exact field \(\mathbb Q(\zeta)=\mathbb Q[t]/(t^2+t+1)\): both scalars, the nonzero defect and its square; matrix determinants and order-three relations; the order-27 group, genus-two surface relation, and irreducibility tests. It also verifies complete restoration of the previous target, a sole difference at line 8694, inverse-patch recovery of the specified baseline, and unchanged sections and labels. See `verification-results.json`.
