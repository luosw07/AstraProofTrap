# 002: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow, informed by the manuscript and existing construction/checker materials. It is neither an original workflow report nor a blind reviewer run. The audit follows the [classification standard](../../../protocol/classification.md) and [classification-review instructions](../../../protocol/checker-classification-template.txt).

## Target, assumptions, and reading scope

The modification replaces the definition of the correction field in the proof of Lemma 8.2, “Realization of constant-volume jets,” at [modified source lines 5154–5158](../paper/paper.tex#L5154). The first false claim is the assertion that decomposing these fields gives shears “correcting degree $m$” and that their induction proves realization, at [lines 5185–5188](../paper/paper.tex#L5185). The [original paragraph](../original/paper.tex#L5154) used the first discrepancy of the current model; the [patch](../mutation.diff) replaces it with the homogeneous terms of one fixed logarithm of the target.

I read the complete 6,473-line modified source, the original target paragraph and the full-source comparison, the patch, the [tricker report](tricker_report.md), the [existing checker report](checker_report.md), and the [case README](../README.md). The full comparison has exactly one changed range, lines 5154–5158; all other source lines agree. The supplied auxiliary TeX files are identical and provide glyph mappings. I rechecked the polynomial witness independently, including 70 exact-rational assertions. Reviewer verdicts and detection counts play no part in this assessment.

The relevant actual assumptions are as follows.

* The main theorem permits complex dimension $n\ge1$, with a connected, noncompact complex manifold carrying a smooth complete Kähler metric of strictly positive holomorphic bisectional curvature; see [lines 194–199](../paper/paper.tex#L194). The target lemma is a finite-dimensional statement for **every** jet in its stated algebraic domain. Its hypotheses impose no mesh, curvature-rate, or commutativity restriction on nonlinear jet coefficients.
* $J_dF$ is the Taylor jet at zero through total degree $d$, with fixed coefficient norms; see [the jet convention](../paper/paper.tex#L4806). Every map and jet in Section 8 fixes zero. For a polynomial representative $t$ of a $d$-jet, the exact domain predicate is

  $$
  \mathsf D_{n,d}(t):\quad
  t\in(\mathbb C[z_1,\ldots,z_n]_{\le d})^n,
  \quad t(0)=0,\quad L_t:=t'(0)\in GL_n(\mathbb C),
  \quad J_{d-1}\det t'(z)=\det L_t.
  $$

  This is the manuscript's [constant-volume definition and lemma](../paper/paper.tex#L5141). Changing a germ representative by $O(|z|^{d+1})$ leaves this condition unchanged.
* Normalize by $\widehat t=J_d(L_t^{-1}\circ t)$. It is tangent to the identity and preserves $dz_1\wedge\cdots\wedge dz_n$ through the required order. The replacement defines

  $$
  X(t)=\log(\widehat t)=\sum_{m=2}^dX_m(t),
  \qquad X_m(t)\in\mathcal V_{n,m},
  $$

  where $\mathcal V_{n,m}$ is the complex vector space of homogeneous degree-$m$ polynomial vector fields with zero divergence. The logarithm is the infinitesimal vector field of the substitution operator, as made explicit below.
* For each degree, the manuscript selects a finite shear list and a fixed linear decomposition, independent of the input jet. The intended construction is a finite product of the resulting shear maps, followed by $L_t$. Its required output has the **same full $d$-jet** as $t$, as well as bounded degree, inverse degree, and coefficients. A polynomial automorphism with only the correct determinant and linear part does not fulfill that construction specification.

For precise formulas below, fix an ordered list

$$
W_{m,j}(z)=\ell_{m,j}(z)^m v_{m,j},\qquad
\ell_{m,j}\in(\mathbb C^n)^*,\quad v_{m,j}\in\mathbb C^n,
\quad\ell_{m,j}(v_{m,j})=0,
$$

for $1\le j\le N_m$, spanning $\mathcal V_{n,m}$. Let

$$
E_m:\mathbb C^{N_m}\longrightarrow\mathcal V_{n,m},\qquad
E_m(c)=\sum_jc_jW_{m,j},
\quad
\Lambda_m:\mathcal V_{n,m}\longrightarrow\mathbb C^{N_m},
\quad E_m\Lambda_m=\operatorname{Id}.
$$

Here $\Lambda_m$ is the fixed linear decomposition. Write

$$
\begin{aligned}
 c_{m,j}(t)&=(\Lambda_mX_m(t))_j,\\
 \phi_{m,j,t}(z)&=z+c_{m,j}(t)\ell_{m,j}(z)^mv_{m,j},\\
 U_m(t)&=\phi_{m,N_m,t}\circ\cdots\circ\phi_{m,1,t},\\
 P_1(t)&=\operatorname{Id},\qquad
 P_m(t)=U_m(t)\circ P_{m-1}(t),\\
 \mathcal A(t)&=L_t\circ P_d(t).
\end{aligned}
\tag{1}
$$

These symbols reconstruct the printed algorithm; they are not extra assumptions or a replacement proof. The source does not specify which side receives a new layer. Equation (1) fixes left composition for calculation, and the opposite direction is checked explicitly below.

For use in the logical Notes, define the full realization predicate

$$
\begin{aligned}
\mathsf R(t,G;D,Q):\quad &G:\mathbb C^n\to\mathbb C^n
  \text{ is a polynomial automorphism},\quad G(0)=0,\\
 &J_dG=t,\qquad \det G'\equiv\det L_t,\\
 &\deg G,\deg G^{-1}\le D,\\
 &\|G\|_{\mathrm{coeff}}+\|G^{-1}\|_{\mathrm{coeff}}
 \le Q(\|t\|_{\mathrm{coeff}},\|L_t^{-1}\|).
\end{aligned}
\tag{2}
$$

$D$ is a positive integer; $Q$ is a real polynomial in two nonnegative real arguments with nonnegative coefficients. The lemma requires choices depending only on $n,d$. For a fixed list and decomposition, the product construction really supplies a degree bound
$D_w=\prod_{m=2}^d m^{N_m}$ and a polynomial coefficient bound $Q_w$; the failed part of (2) is its jet equality.

## Five-item audit summary

“Violated / downstream” in the logical rows records a failed premise derivation inherited from the earlier construction/composition error. It contributes no additional direct label.

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | downstream | Lemma invocation at [5540–5547](../paper/paper.tex#L5540); Taylor implication at [5695–5708](../paper/paper.tex#L5695), dependent on 5185–5188 | The local shear theorem is instantiated correctly. Later applications lack the established realization/jet-agreement premise. [Full MP Note](#mp--note) |
| G1 | violated | downstream | Universal realization statement at [5145–5150](../paper/paper.tex#L5145), purported arbitrary-input induction at [5185–5188](../paper/paper.tex#L5185) | The generic-input conditional fails at its fourth-order calculation; its parameter conditions are correct. [Full G1 Note](#g1--note) |
| G2 | violated | downstream | Selection of a finite spanning list and linear decomposition at [5181–5188](../paper/paper.tex#L5181) | The witness supplies all shear/decomposition properties claimed for it. The conditional proof of full realization then inherits the same false composition step; no witness escapes its scope. [Full G2 Note](#g2--note) |
| DEF | violated | direct | Fixed-log prescription at [5154–5158](../paper/paper.tex#L5154), used as a realizing construction at [5185–5194](../paper/paper.tex#L5185) | The explicit output exists as an automorphism but fails its defining realization requirement $J_d\mathcal A(t)=t$. [Full DEF Note](#def--note) |
| CONV | violated | direct | “Correcting degree $m$” and completion of the induction at [5185–5188](../paper/paper.tex#L5185) | Expanding the prescribed product leaves a nonzero quartic term although $X_4=0$. [Full CONV Note](#conv--note) |

## MP — Note

### The local theorem application is valid

Start with implication elimination:

$$
\Gamma\vdash A,\qquad\Gamma\vdash A\to B
\quad\Longrightarrow\quad\Gamma\vdash B.
$$

For the application of the shear-spanning statement at [lines 5160–5185](../paper/paper.tex#L5160), take $n,d$ as above, an integer $m$ with $2\le m\le d$, and a jet $t$ satisfying $\mathsf D_{n,d}(t)$. The background $\Gamma_{\mathrm{sh}}$ consists of these domain assumptions; the definition of $\widehat t$, its formal logarithm and its homogeneous components; the already established zero-divergence conclusion; the finite-dimensional shear-spanning statement proved in lines 5169–5179; the fixed ordered list and right inverse $E_m,\Lambda_m$; and polynomial composition and differentiation over $\mathbb C$. It contains no assumption that $X_m(t)$ is a current residual.

The relevant quantified theorem and its substitution are

$$
\forall Y\in\mathcal H_{n,m}\quad
 \left(\operatorname{div}Y=0\ \longrightarrow\quad
 \exists c\in\mathbb C^{N_m}\quad
 Y(z)=\sum_{j=1}^{N_m}c_j\ell_{m,j}(z)^mv_{m,j}\right),
\qquad Y\leftarrow X_m(t),
\tag{3}
$$

where $\mathcal H_{n,m}$ is the space of all homogeneous degree-$m$ polynomial vector fields $\mathbb C^n\to\mathbb C^n$. Thus

$$
\begin{aligned}
A_{\mathrm{sh}}&=X_m(t)\in\mathcal H_{n,m}
                 \ \land\ \operatorname{div}X_m(t)=0,\\
B_{\mathrm{sh}}&=\exists c\in\mathbb C^{N_m}\quad
 X_m(t)=\sum_jc_j\ell_{m,j}^mv_{m,j}.
\end{aligned}
$$

Both the implication and the antecedent are available. Choosing $c=\Lambda_mX_m(t)$ makes the conclusion concrete. For each $j$, $\ell_{m,j}(v_{m,j})=0$ implies that $\ell_{m,j}$ is constant along its flow; therefore the claimed time-$c_j$ map, inverse, and determinant are correct. Composing the factors gives exactly

$$
J_mU_m(t)=\operatorname{Id}+X_m(t),
\qquad J_{m-1}U_m(t)=\operatorname{Id}.
\tag{4}
$$

The application of (3), and the computation of (4), preserve their antecedents and consequents.

The manuscript's additional conclusion is

$$
C_m:\quad J_m\bigl(U_m(t)\circ P_{m-1}(t)\bigr)
                  =J_m\widehat t.
\tag{5}
$$

Equation (4) alone does not give (5). To expose the exact obligation, under
$J_{m-1}P_{m-1}(t)=J_{m-1}\widehat t$, substitution gives

$$
[U_m(t)\circ P_{m-1}(t)-\widehat t]_m
 =[P_{m-1}(t)-\widehat t]_m+X_m(t).
\tag{6}
$$

Here $[\cdot]_m$ denotes the homogeneous vector part of total degree $m$. The cancellation required by (5) is

$$
X_m(t)=[\widehat t-P_{m-1}(t)]_m.
\tag{7}
$$

For the admissible witness in the CONV Note, at $m=4$, the left side of (7) is zero and the right side is
$(x^3y,-\tfrac32x^2y^2)$. If (5) is recast as an application of a residual-correction implication, (7) is its first unestablished antecedent. That recasting is a reconstruction: the modified manuscript has removed the residual definition and does not cite such a theorem at this point. Its actual local claim is the result of composing the prescribed formulas. Accordingly, this first error is classified directly as CONV and as a failed construction contract, not as an additional misuse of the correctly invoked shear-spanning theorem.

### The later invocation has an unavailable proved implication

The statement of Lemma 8.2 has the form

$$
\exists D\,\exists Q\,\forall t\quad
\bigl(\mathsf D_{n,d}(t)\to\exists G\,\mathsf R(t,G;D,Q)\bigr).
\tag{8}
$$

At a fixed bad macro index $k$, define the actual input jet

$$
q_k=J_d(H_{k+1}\circ F_k\circ H_k^{-1}),
\tag{9}
$$

where $F_k$ is the holomorphic transition germ and $H_k,H_{k+1}$ are the endpoint polynomial local changes, all fixing zero with invertible center derivative. The inverse in (9) is a local inverse jet, as permitted by the manuscript.

The checked background $\Gamma_k$ contains $n,d,k$; these domains and local invertibility facts; the volume-cocycle identity and coordinate changes of [lines 5103–5142](../paper/paper.tex#L5103); the determinant identities for the primary linear changes and endpoint $h_k$ corrections in [lines 5530–5538](../paper/paper.tex#L5530); the bounds on input coefficients and inverse linear part in [lines 5549–5551](../paper/paper.tex#L5549); and the definitions of jet composition and (9). Expanding its volume conclusion gives

$$
q_k(0)=0,\quad L_k=q_k'(0)\in GL_n(\mathbb C),
\quad J_{d-1}\det q_k'=\det L_k.
$$

Consequently $\Gamma_k\vdash A_k:=\mathsf D_{n,d}(q_k)$.

The intended substitution in (8) is $t\leftarrow q_k$; for its fixed $D,Q$, the consequent is

$$
B_k:=\exists G\left[
G\in\operatorname{Aut}_{\mathrm{poly}}(\mathbb C^n),\ G(0)=0,
\ J_dG=q_k,\ \det G'\equiv\det L_k,
\ \deg G,\deg G^{-1}\le D,
\ \|G\|_{\mathrm{coeff}}+\|G^{-1}\|_{\mathrm{coeff}}
 \le Q(\|q_k\|,\|L_k^{-1}\|)\right].
$$

After selecting its realizing witness $G_k$, the claimed conclusion is

$$
C_k:\quad J_d(H_{k+1}\circ F_k)=J_d(G_k\circ H_k).
\tag{10}
$$

The conversion from $J_dG_k=q_k$ to (10) by right composition with $H_k$ is valid. The first failed MP obligation is the availability of a proved implication $A_k\to B_k$: the submitted proof of (8) has failed at (5). If the algorithm's candidate is used as $G_k$, its required witness property $J_dG_k=q_k$ is exactly the unproved, and in the explicit local example false, property. This is the provenance of the downstream MP finding. The antecedent's constant-volume requirement is not the defective part.

The same distinction applies at [lines 5695–5708](../paper/paper.tex#L5695). The valid Taylor implication is: for holomorphic maps $f,g:B(R)\to\mathbb C^n$, bounded there by a finite $M$, if every coefficient of $f-g$ through degree $d$ vanishes, then on a fixed smaller ball

$$
|f(z)-g(z)|\le C_{n,d,R}M|z|^{d+1}.
$$

Substitute $f=H_{k+1}\circ F_k$, $g=G_k\circ H_k$, with the coefficient bounds supplying $M$. Holomorphicity and boundedness hold on the stated ball. The missing antecedent is their jet equality (10), inherited from the failed realization construction. The Taylor theorem's consequent is used with its correct order; it is not itself misstated.

## G1 — Note

Use the specified rule

$$
\frac{\Gamma\vdash A\to B(x)}
     {\Gamma\vdash A\to\forall x\,B(x)},
\qquad x\notin FV(\Gamma)\cup FV(A).
$$

The target variable here is the input jet, denoted $t$, rather than a spatial coordinate. Its ambient domain is
$\mathcal J_{n,d}=\{t\in(\mathbb C[z]_{\le d})^n:t(0)=0\}$, and its restricted range is the fully specified predicate $\mathsf D_{n,d}(t)$ above.

Let $\Gamma_{\forall}$ contain: fixed integers $n\ge1,d\ge2$; fixed coefficient norms; the ordered shear lists and linear right inverses for degrees $2,\ldots,d$, selected depending only on $n,d$; their shear and spanning identities; the formal logarithm identities for arbitrary tangent-to-identity jets; and the definitions (1), the degree bound $D_w$, and its coefficient polynomial $Q_w$. These formulas have free parameters $n,d,w,D_w,Q_w$ and the chosen norms. They have no free input jet. Spatial coordinates in polynomial identities are bound universally, and each degree index in the list of identities is bound or fixed before the input is selected.

Take $A=\top$ and

$$
B(t)=\mathsf D_{n,d}(t)
       \longrightarrow\mathsf R(t,\mathcal A(t);D_w,Q_w).
\tag{11}
$$

A reconstruction of the actual pre-generalization argument, with a fresh arbitrary $a\in\mathcal J_{n,d}$, is

$$
\begin{array}{ll}
[\mathsf D_{n,d}(a)] &\text{open range assumption},\\
\widehat a=J_d(L_a^{-1}a),\quad
 X(a)=\sum_{m=2}^dX_m(a)
 &\text{definitions},\\
\operatorname{div}X_m(a)=0\quad(2\le m\le d)
 &\text{volume and homogeneous grading},\\
P_1(a)=\operatorname{Id},\quad J_1P_1(a)=J_1\widehat a
 &\text{valid base case},\\
[J_{m-1}P_{m-1}(a)=J_{m-1}\widehat a]
 &\text{local induction assumption},\\
J_mU_m(a)=\operatorname{Id}+X_m(a)
 &\text{valid shear calculation},\\
\boxed{J_mP_m(a)=J_m\widehat a}
 &\text{asserted at 5186; fails by (6)–(7)},\\
J_d\mathcal A(a)=a
 &\text{purported result after restoring }L_a,\\
\mathsf R(a,\mathcal A(a);D_w,Q_w)
 &\text{purported constructed realization}.
\end{array}
\tag{12}
$$

The local induction assumption would be discharged in establishing the step from degree $m-1$ to $m$. The range assumption $\mathsf D_{n,d}(a)$ would then be discharged to obtain (11) for $a$. The asserted quantified conclusion of this construction is

$$
\forall t\in\mathcal J_{n,d}\quad
\bigl(\mathsf D_{n,d}(t)\to
      \mathsf R(t,\mathcal A(t);D_w,Q_w)\bigr),
\tag{13}
$$

which would imply the lemma's stated, weaker conclusion with
$\exists G\,\mathsf R(t,G;D_w,Q_w)$.

The relevant free-variable conditions are satisfied: $a$ is fresh for $\Gamma_{\forall}$, $FV(\top)=\varnothing$, the only assumption involving $a$ is discharged into the restricted formula, and the temporary $m$-induction assumption is also discharged. The selected jet has no special assumption beyond fixing zero, having an invertible derivative, and the stated constant-volume condition. In particular, the proof does not first select a commuting, one-dimensional, or single-shear input and then illegally erase that restriction. The fixed shear lists are independent of $a$ exactly as required for (13).

The failed obligation is the derivation of $B(a)$ before generalization: the boxed step in (12) is already false for the perfectly admissible fixed jet
$a=J_d(S_{1/2}\circ R_1\circ S_{1/2})$, with $n=2,d\ge4$. Its degree-four calculation fails before any universal quantifier is introduced. Thus G1 is recorded as **downstream**, rather than a new direct error inferred merely from a false universal algorithmic assertion.

The other explicit universal claim in the changed paragraph is valid. Since $\operatorname{div}X_m$ has homogeneous degree $m-1$,

$$
\sum_{m=2}^d\operatorname{div}X_m=0
\quad\Longrightarrow\quad
\forall m\in\mathbb Z\,
(2\le m\le d\to\operatorname{div}X_m=0).
$$

It follows by uniqueness of homogeneous components, with the range retained in the formula. It neither supplies (7) nor causes a separate quantifier error.

## G2 — Note

Use

$$
\frac{\Gamma\vdash A(x)\to B}
     {\Gamma\vdash(\exists x\,A(x))\to B},
\qquad x\notin FV(\Gamma)\cup FV(B).
$$

There is a concrete existential selection in the target: [lines 5181–5185](../paper/paper.tex#L5181) select finite spanning lists and fixed linear decompositions. Formalize its witness as the finite data tuple

$$
w=\bigl(N_m,(\ell_{m,j},v_{m,j})_{j=1}^{N_m},\Lambda_m\bigr)_{m=2}^d.
$$

Its domain is the disjoint union, over all finite list lengths, of the indicated covectors, vectors, and complex-linear maps. Its supplied property $A(w)$ is the conjunction, for every $m=2,\ldots,d$, of

$$
\begin{gathered}
N_m\in\mathbb N_0,\quad
\ell_{m,j}\in(\mathbb C^n)^*,\quad v_{m,j}\in\mathbb C^n,
\quad \ell_{m,j}(v_{m,j})=0,\\
E_m(c)=\sum_{j=1}^{N_m}c_j\ell_{m,j}^mv_{m,j},\quad
\operatorname{im}E_m=\mathcal V_{n,m},\\
\Lambda_m:\mathcal V_{n,m}\to\mathbb C^{N_m}
\text{ is complex-linear},\qquad
E_m\Lambda_m=\operatorname{Id}_{\mathcal V_{n,m}}.
\end{gathered}
\tag{14}
$$

No condition in (14) identifies a fixed-log field with a current residual. The shear-spanning result and elementary linear algebra establish $\exists w\,A(w)$.

Let $\Gamma_{\exists}$ contain only the fixed $n,d$, coefficient norms, the definitions of the jet domain and realization predicate, polynomial/finite-jet algebra and the formal-logarithm identities, and the just proved existence of a tuple satisfying (14). It contains no particular such tuple. The full intended target, including the uniformity of the bounds, is

$$
B=\exists D\in\mathbb N_{\ge1}\ \exists Q\in\mathbb R_{\ge0}[u,v]\quad
\forall t\in\mathcal J_{n,d}\quad
\bigl(\mathsf D_{n,d}(t)\to\exists G\,\mathsf R(t,G;D,Q)\bigr).
\tag{15}
$$

Here $\mathbb R_{\ge0}[u,v]$ means polynomials with nonnegative real coefficients, evaluated on nonnegative norms. Both $D,Q$ are quantified before $t$, as required by the lemma; $G$ may depend on $t$.

The existential-elimination subderivation with fresh witness $w_0$ has the following scope. Broken lines are explicitly identified rather than treated as established sequents:

$$
\begin{array}{ll}
\exists w\,A(w)&\text{available premise},\\
\quad[A(w_0)]&\text{fresh witness assumption},\\
\quad D_{w_0}=\prod_{m=2}^dm^{N_m},\quad Q_{w_0}
 &\text{bounds constructed from its finite list},\\
\quad\text{fix arbitrary }a\in\mathcal J_{n,d},\ [\mathsf D_{n,d}(a)]
 &\text{inner range assumption},\\
\quad c_m=\Lambda_mX_m(a),\quad
G_{w_0,a}=L_a\circ U_d(a)\circ\cdots\circ U_2(a)
 &\text{witness-dependent constructions},\\
\quad G_{w_0,a}\in\operatorname{Aut}_{\mathrm{poly}},\quad
G_{w_0,a}(0)=0,\quad\det G_{w_0,a}'\equiv\det L_a
 &\text{valid},\\
\quad\deg G_{w_0,a},\deg G_{w_0,a}^{-1}\le D_{w_0}
 &\text{valid},\\
\quad\|G_{w_0,a}\|+\|G_{w_0,a}^{-1}\|
 \le Q_{w_0}(\|a\|,\|L_a^{-1}\|)
 &\text{valid},\\
\quad\boxed{J_dG_{w_0,a}=a}
 &\text{fails at the earlier composition claim},\\
\quad\mathsf R(a,G_{w_0,a};D_{w_0},Q_{w_0})
 &\text{therefore unavailable},\\
\quad\exists G\,\mathsf R(a,G;D_{w_0},Q_{w_0})
 &\text{would bind the constructed map},\\
\quad\forall t\,\bigl(\mathsf D_{n,d}(t)\to
             \exists G\,\mathsf R(t,G;D_{w_0},Q_{w_0})\bigr)
 &\text{would discharge the range assumption and }a,\\
\quad B&\text{would bind }D_{w_0},Q_{w_0},\\
B&\text{would discharge }A(w_0)\text{ by }\exists\text{-elimination}.
\end{array}
\tag{16}
$$

This displays all hidden dependencies: $c_m,U_m,G_{w_0,a},D_{w_0},Q_{w_0}$ depend on $w_0$; the map and coefficients also depend on $a$. Their occurrence inside the witness scope is permitted. In (15) the bounds and map are existentially bound, the input is universally bound, and $w_0$ is absent. Thus
$w_0\notin FV(\Gamma_{\exists})\cup FV(B)$. No particular shear list, decomposition, or map is exported as a free existential witness.

For an entirely valid elimination, omit the boxed jet-equality line and replace $\mathsf R$ in (15)–(16) by the predicate consisting of all its clauses **except** $J_dG=t$. The remaining lines then follow from (14), and existential elimination closes. This isolates the actual failed conditional for the full target: having a shear decomposition is sufficient to form an automorphism with the listed bounds, but the prescribed coefficients have already failed the jet-matching calculation.

There is also no exchange of
$\forall t\exists w$ with $\exists w\forall t$. The manuscript deliberately selects lists and right inverses once, before the input-dependent coefficients; finite-dimensional linear algebra supplies this fixed choice. The stronger algorithmic assertion

$$
\exists w\left(A(w)\ \land\quad
\forall t\,[\mathsf D_{n,d}(t)\to J_d\mathcal A_w(t)=t]\right)
$$

fails for the calculation explained in the DEF Note, not because an input-dependent witness was silently made uniform. Consequently the failure of the full conditional in (16) is **downstream** of CONV/DEF, with no independent direct G2 label or eigenvariable violation.

## DEF — Note

### Which objects are well-defined

The modified first paragraph does define a legitimate logarithm. Work in the finite jet algebra

$$
\mathcal R_d=\mathbb C[z_1,\ldots,z_n]/(z_1,\ldots,z_n)^{d+1}.
$$

For a tangent-to-identity input $\widehat t$, let
$\widehat t^*f=f\circ\widehat t$, and put
$\Delta=\widehat t^*-\operatorname{Id}$. On positive-degree polynomials, $\Delta$ raises degree by at least one; it annihilates constants. Thus

$$
\log(\widehat t^*)
 =\sum_{r\ge1}\frac{(-1)^{r+1}}r\Delta^r
\tag{17}
$$

is a finite sum at each order. It depends only on the input jet, and the usual inverse finite exponential makes it unique among derivations raising degree.

To check the derivation requirement, the truncated operator

$$
(\operatorname{Id}+\Delta)^a=\sum_r\binom ar\Delta^r
$$

has coefficients polynomial in $a$. For every nonnegative integer $a$, it is the pullback by an iterate, hence multiplicative. Polynomial identity extends multiplicativity to every $a\in\mathbb C$. Differentiation at $a=0$ proves the Leibniz rule for (17). Its values on coordinate classes specify a unique polynomial vector field through degree $d$, and homogeneous projection specifies each $X_m$ uniquely.

For the volume statement, use the same finite-order action on forms, retaining total degree with $\deg dz_i=1$. The condition $J_{d-1}\det\widehat t'=1$ says that the volume form is fixed through coefficient degree $d-1$. Its integer iterates have the same property, so the polynomial-in-$a$ argument and differentiation give

$$
\mathcal L_X(dz_1\wedge\cdots\wedge dz_n)
 =(\operatorname{div}X)\,dz_1\wedge\cdots\wedge dz_n=0
$$

to that order. Distinct homogeneous degrees then give $\operatorname{div}X_m=0$. No logarithm branch or convergence assumption is involved in this formal construction.

The finite lists and $\Lambda_m$ in (14) exist because their spanning maps are surjective between finite-dimensional complex vector spaces. A right inverse can be fixed once; uniqueness of a decomposition is not required. With this choice fixed, every coefficient and map in (1) is specified uniquely. For a shear, $\ell(v)=0$ yields

$$
\ell(z+c\ell(z)^mv)=\ell(z),\qquad
\phi_c^{-1}=\phi_{-c},\qquad
\det\phi_c'=1+cm\ell(z)^{m-1}\ell(v)=1.
$$

Thus $\phi_{m,j,t}:\mathbb C^n\to\mathbb C^n$, each $U_m$, and each $P_m$ are genuine polynomial automorphisms; restoring $L_t$ is meaningful. The recursion is finite and has no existence or circularity problem. Its inverse is obtained by reversing the finite factor order and changing shear signs, followed by $L_t^{-1}$. At fixed $n,d$, log coefficients, decomposition coefficients, composition coefficients, and inverse coefficients are polynomial expressions in the input coefficients and inverse linear entries. These facts establish the stated coarse bounds.

### The construction contract fails on an admissible input

The object being offered at [lines 5185–5194](../paper/paper.tex#L5185) is a **realizing automorphism for the supplied jet**, not merely an unspecified automorphism. Its required codomain is the fiber

$$
\{G\in\operatorname{Aut}_{\mathrm{poly}}(\mathbb C^n):J_dG=t\},
$$

with the additional determinant and quantitative requirements in (2). The finite recursive specification claims to maintain
$J_mP_m(t)=J_m\widehat t$. This defining construction requirement, as opposed to the existence of the underlying polynomial expression, fails.

Take $n=2$, coordinates $(x,y)\in\mathbb C^2$, and any $d\ge4$. Define

$$
S_a(x,y)=(x+ay^2,y),\qquad
R_b(x,y)=(x,y+bx^3),\qquad
T=S_{1/2}\circ R_1\circ S_{1/2},\qquad t=J_dT.
\tag{18}
$$

Every factor fixes zero, has derivative $I$ at zero, has Jacobian identically one, and has inverse $S_{-a}$ or $R_{-b}$. In particular,

$$
T^{-1}=S_{-1/2}\circ R_{-1}\circ S_{-1/2},
$$

so $\mathsf D_{2,d}(t)$ holds to all required orders. The target itself realizes its jet; the failure is in the submitted construction, not in the existence of this fiber.

One permitted fixed list, for every $m$, is

$$
W_{m,\infty}=y^m\partial_x,\qquad
W_{m,r}=(x+ry)^m(-r\partial_x+\partial_y),
\quad r=0,1,\ldots,m.
\tag{19}
$$

All of these are shears with $\ell(v)=0$. Divergence maps the $2(m+1)$-dimensional space of homogeneous vector fields onto the $m$-dimensional space of homogeneous degree-$m-1$ polynomials: an antiderivative in $x$ already gives a preimage of every such polynomial. Its kernel therefore has dimension $m+2$. Under the injective homogeneous Hamiltonian map
$H\mapsto(-\partial_yH,\partial_xH)$, the fields in (19) correspond to

$$
-\frac{y^{m+1}}{m+1},\qquad
\frac{(x+ry)^{m+1}}{m+1}.
$$

Comparing coefficients with $y$-exponents $0,\ldots,m$ in a relation gives the Vandermonde matrix at $r=0,\ldots,m$, forcing every finite-node coefficient to vanish; the remaining coefficient also vanishes. Thus (19) is a basis. Its coordinate map is a fixed linear decomposition with finite norm depending only on $m$.

The calculation below gives

$$
X_2=y^2\partial_x,
\qquad X_3=x^3\partial_y,
\qquad X_4=0.
$$

For (19), each of the first two fields has just one nonzero coefficient. Hence

$$
U_2=S_1,\qquad U_3=R_1,\qquad U_4=\operatorname{Id},
$$

and

$$
J_4(P_4-T)=\left(-x^3y,\frac32x^2y^2\right)\ne0.
\tag{20}
$$

The proposed map remains invertible and volume-preserving; it does not belong to the required realization fiber. This is a direct DEF failure of a construction contract. It is not a claim that the formal logarithm, shear formula, or ambient polynomial automorphism is undefined, and it is not based on a separate later theorem about an otherwise correctly realized jet.

Nor can the unspecified choice of fixed decomposition supply the missing property. For any such choice let $U_m(Y)$ denote its layer output on field $Y$. Linearity gives $U_m(0)=\operatorname{Id}$. If it realizes the single-shear input $S_1$ correctly through degree four, then, since that input has only $X_2=y^2\partial_x$,

$$
J_4U_2(y^2\partial_x)=J_4S_1.
$$

For (18) it receives exactly the same quadratic field. Every cubic shear product has
$U_3(x^3\partial_y)=\operatorname{Id}+(0,x^3)+O_5$, because interaction between two cubic fields begins in degree five. Its quartic layer is again $U_4(0)=\operatorname{Id}$. Thus the same discrepancy (20) follows. If its quadratic output does not have the displayed jet, the single-shear input already fails. This proves that no permitted fixed linear decomposition makes the algorithm work for every input. It addresses the actual unspecified choice without assuming a favorable decomposition not supplied by the paper.

## CONV — Note

The exact starting data are the fixed $X_m$ at [lines 5154–5158](../paper/paper.tex#L5154) and the shear flow formula at [lines 5183–5185](../paper/paper.tex#L5183). The claimed endpoint is “correcting degree $m$” followed by realization at [lines 5186–5188](../paper/paper.tex#L5186). In the notation of (1), the corresponding reconstructed equality is

$$
J_d\bigl(U_d(t)\circ\cdots\circ U_2(t)\bigr)
 =\widehat t,
\quad\text{and at each stage}\quad
J_mP_m(t)=J_m\widehat t.
\tag{21}
$$

This is an equality of explicit substituted polynomials. It is not a consequence supplied by the cited shear-spanning theorem.

### Expand the admissible target and its fixed logarithm

For (18), put

$$
u=x+\tfrac12y^2,\qquad v=y+u^3,\qquad T=(u+\tfrac12v^2,v).
$$

Here $O_j$ denotes terms of total degree at least $j$. Direct multiplication gives

$$
\begin{aligned}
u^3&=x^3+\tfrac32x^2y^2+\tfrac34xy^4+\tfrac18y^6,\\
v&=y+x^3+\tfrac32x^2y^2+O_5,\\
v^2&=y^2+2x^3y+O_5,\\
T&=\left(x+y^2+x^3y,\ y+x^3+\tfrac32x^2y^2\right)+O_5.
\end{aligned}
\tag{22}
$$

Now $T^*f=f\circ T$ and $\Delta=T^*-\operatorname{Id}$. In $\mathcal R_4$,

$$
\begin{aligned}
\Delta x&=y^2+x^3y+O_5,\\
\Delta(y^2)&=(y+x^3+\tfrac32x^2y^2+O_5)^2-y^2
             =2x^3y+O_5,\\
\Delta(x^3y)&=O_5,\\
\Delta^2x&=2x^3y+O_5,\qquad \Delta^3x=O_5;\\[2pt]
\Delta y&=x^3+\tfrac32x^2y^2+O_5,\\
\Delta(x^3)&=(x+y^2+x^3y+O_5)^3-x^3
             =3x^2y^2+O_5,\\
\Delta(x^2y^2)&=O_5,\\
\Delta^2y&=3x^2y^2+O_5,\qquad \Delta^3y=O_5.
\end{aligned}
$$

Using (17), all further powers contribute only $O_5$, so

$$
\begin{aligned}
(\log T^*)x&=y^2+x^3y-\tfrac12(2x^3y)+O_5=y^2+O_5,\\
(\log T^*)y&=x^3+\tfrac32x^2y^2
              -\tfrac12(3x^2y^2)+O_5=x^3+O_5.
\end{aligned}
$$

Thus the replacement paragraph correctly supplies

$$
Y:=X_2=y^2\partial_x,\qquad
Z:=X_3=x^3\partial_y,\qquad X_4=0.
\tag{23}
$$

Both nonzero fields have zero divergence. The vanished quartic term is an exact cancellation in the logarithm.

For another direct check of the intended endpoint, the exponential of the derivation $Y+Z$ acts on coordinates as

$$
\begin{aligned}
(Y+Z)x&=y^2,&(Y+Z)^2x&=2x^3y,&(Y+Z)^3x&=O_5,\\
(Y+Z)y&=x^3,&(Y+Z)^2y&=3x^2y^2,&(Y+Z)^3y&=O_5.
\end{aligned}
$$

Hence the exponential through degree four is exactly (22). A product of the separate flows has a different fourth jet, as follows.

### Expand the prescribed layer product

For the allowed decomposition (19), applying the quadratic and then cubic layers gives

$$
\begin{aligned}
P_2(x,y)&=S_1(x,y)=(x+y^2,y),\\
P_3(x,y)&=R_1(S_1(x,y))
 =\left(x+y^2,\ y+(x+y^2)^3\right),\\
(x+y^2)^3&=x^3+3x^2y^2+3xy^4+y^6,\\
J_4P_3&=\left(x+y^2,\ y+x^3+3x^2y^2\right),\\
P_4&=U_4\circ P_3=\operatorname{Id}\circ P_3=P_3.
\end{aligned}
\tag{24}
$$

All terms through degree three agree with the target. The **first incorrect equality in the claimed induction**, for this witness, is

$$
J_4(U_4\circ P_3)=J_4T.
$$

Its correct difference is

$$
\boxed{J_4(P_4-T)=\left(-x^3y,\frac32x^2y^2\right).}
\tag{25}
$$

Equivalently, the current residual is

$$
T\circ P_3^{-1}
 =\operatorname{Id}+\left(x^3y,-\frac32x^2y^2\right)+O_5,
$$

and its leading field has divergence
$3x^2y-3x^2y=0$. It is different from the prescribed $X_4=0$. This calculation identifies the failed substitution in (7); it does not replace the submitted algorithm with a residual algorithm.

With the vector-field bracket
$[Y,Z]=(Y\cdot\nabla)Z-(Z\cdot\nabla)Y$,

$$
[Y,Z]=(-2x^3y,3x^2y^2),
$$

so (25) is half this nonzero bracket. This identity is a diagnostic interpretation of the explicit multiplication above, not an assumed Baker–Campbell–Hausdorff theorem.

If a new layer is put on the other side instead, its fourth jet is

$$
\begin{aligned}
S_1(R_1(x,y))&=(x+(y+x^3)^2,y+x^3),\\
J_4(S_1\circ R_1)&=(x+y^2+2x^3y,y+x^3),\\
J_4(S_1\circ R_1-T)&=(x^3y,-\tfrac32x^2y^2).
\end{aligned}
$$

It fails with the opposite sign. Every subsequent layer of degree $m\ge5$ is $\operatorname{Id}+O_5$; composing it on either side preserves the fourth jet. Thus the error survives for every $d\ge4$, including the large $d$ required by [lines 5674–5687](../paper/paper.tex#L5674).

### Trace the use of the failed identity

The volume correction at [lines 5128–5142](../paper/paper.tex#L5128) controls the determinant jet and does not impose (7). Both $T$ and the erroneous $P_4$ have determinant identically one. The regular-step construction in Section 8.5 solves separate homological equations using lower-order data; [the bad-step passage](../paper/paper.tex#L5540) instead invokes Lemma 8.2. Neither that passage nor the remainder of the manuscript recomputes this lemma's residual or adds compensation for (25).

Restoring an arbitrary invertible linear part $L$ turns the discrepancy into $L(-x^3y,\tfrac32x^2y^2)$, which is nonzero. Along $(x,y)=(r,r)$, its leading value is

$$
r^4L(-1,\tfrac32).
$$

For any fixed finite constant, a nonzero term of this order fails an $O(|z|^{d+1})$ estimate when $d\ge4$: division by $|(r,r)|^{d+1}$ produces a positive constant times $|r|^{3-d}$. This explains precisely the missing input to [the remainder estimate](../paper/paper.tex#L5695), and thence to the orbit-defect and backward-convergence estimates in Section 9. It is downstream use of the incorrect jet, whereas the direct CONV violation is already (24)–(25).

The algebraic witness meets every hypothesis of the universal realization lemma. The reports also discuss realizing such normalized jets by a change of local atlas charts. They do not determine a final bad macro interval for that particular radial-flow geometry; that additional global example is not used as a premise of this classification. The failed universal construction and its actual later invocation are established directly by the supplied source and the finite polynomial calculation.

## Final direct classification

**Final direct labels: DEF, CONV.** These agree with the labels in the [case README](../README.md). There is no change to the direct label set.

* **DEF:** the fixed-log algorithm is presented as a construction of an automorphism realizing the prescribed jet, but its output fails that required jet condition on (18).
* **CONV:** actual expansion of its layer product gives (25), contradicting the claimed degree-four correction.

The proof-availability failures recorded under MP, G1, and G2 arise after this same fixed-input error. Their instantiated theorem hypotheses, quantifier scopes, and witness dependencies have been displayed above; they supply no further direct label. The formal logarithm, its divergence-free components, the shear-spanning result, and the individual shear maps all pass their own concrete checks.

There is no unresolved mathematical issue affecting these two direct labels. The independently verified witness has correct input domains, an explicit polynomial inverse, exact unit Jacobian, agreement through degree three, a nonzero degree-four defect in either composition direction, and a defect that persists at every higher jet order.
