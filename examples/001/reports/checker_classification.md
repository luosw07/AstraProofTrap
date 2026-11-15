# 001: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow. It is informed by the manuscript and the existing construction/checker materials; it is neither an original workflow report nor a blind reviewer run.

## Target, sources, and actual assumptions

The exact target is the definition and immediately following assertion in [§8.5, lines 5545–5547](../paper/paper.tex#L5545-L5547):

> Let $H_k$ be the degree-$d$ truncation of the total primary change preceded by $h_k$. It has the required center derivative and inverse jet, and (8.3) follows.

The claimed equation (8.3) is

$$
J_d(H_{k+1}\circ F_k)=J_d(G_k\circ H_k).
\tag{T}
$$

It is the conclusion of [Proposition 8.1, lines 5034–5069](../paper/paper.tex#L5034-L5069), not an additional assumption available to its proof. The [original sentence](../original/paper.tex#L5545-L5547) says “followed.” Comparison of the complete original and modified TeX confirms that the [mutation](../mutation.diff) consists of precisely this one-word replacement, with every other manuscript byte unchanged.

I read the complete manuscript, traced its definitions and later uses, and examined the [case README](../README.md), [tricker report](tricker_report.md), [original checker report](checker_report.md), and [classification standard](../../../protocol/classification.md). Its displayed calculations were checked afresh, including independent exact rational polynomial calculations through degree eight. Reviewer verdicts and detection counts play no part in this classification.

Here is the common mathematical context used in the five Notes.

1. The geometric input is a connected noncompact complex manifold $M$ of dimension $n\geq1$, with a smooth complete Kähler metric $g$ of pointwise strictly positive holomorphic bisectional curvature. The normalization is $\partial_t h_t=-\operatorname{Ric}(h_t)$, $\operatorname{Ric}(h)=-\partial\bar\partial\log\det h$. See [Theorem 1.1](../paper/paper.tex#L194-L204) and [the conventions](../paper/paper.tex#L412-L434). The volume clock is $s=\rho(o,t)$, and $q(s)=tR(o,t)$. Section 8 explicitly retains $q$ nondecreasing, $q\geq c>0$, $\liminf q(s)/s\leq2$, and $\lambda_{\min}(t\operatorname{Ric})(o)\geq b_0q(a_0s)$, for fixed $0<a_0<1$, $b_0>0$.
2. [Proposition 7.7](../paper/paper.tex#L4806-L4849) supplies centered holomorphic charts $\Phi_s:B(r_0)\to M$, unitary center derivatives, uniformly comparable pullback metrics, and nonsingular bounded transition maps $F_{s,u}=\Phi_u^{-1}\Phi_s:B(r_1)\to\mathbb C^n$. They fix zero, compose as germs, and satisfy
   $$
   \|F_{s,u}'(0)\|\leq1,\quad
   |\det F_{s,u}'(0)|=e^{-(u-s)/2},\quad
   \|F_{s,u}'(0)^{-1}\|\leq e^{(u-s)/2}.
   $$
   The continued inverse charts satisfy $\sup_K|f_s|\leq e^{-\sigma s}$ eventually for each compact $K$. The transition-jet and small-ball estimates are exactly those in lines 4835–4845.
3. Fix $d\in\mathbb N$, $d\geq2$, and the macro width $h\in(0,1)$, before constructing the grid. Its indices are $k\in\mathbb N_0$, after a sufficiently late starting point has been relabeled zero. The grid tends to infinity and obeys
   $$
   c_h\sqrt{s_k}\leq s_{k+1}-s_k\leq(e^h-1)s_k.
   $$
   Set $F_k=F_{s_k,s_{k+1}}$. Regular and bad steps, rate weights, and the endpoint linear changes are those of §§8.3–8.4.
4. Introduce the review notation $C_k$ for the total change from raw chart coordinates to primary coordinates. This avoids confusing it with the manuscript's scalar logarithmic Jacobian $P_k$. Explicitly $C_k=M_k\circ A_k$, where $A_k$ is the volume correction of [lines 5128–5138](../paper/paper.tex#L5128-L5138) and $M_k\in\operatorname{GL}_n(\mathbb C)$ is the chosen endpoint linear change. At a regular step, [lines 5450–5472](../paper/paper.tex#L5450-L5472) give
   $$
   C_{k+1}\circ F_k\circ C_k^{-1}=J_k\circ\widehat F_k,\qquad
   G_k=J_k\circ g_k,
   $$
   $$
   J_d(g_k\circ h_k)
   =J_d(J_k^{-1}\circ h_{k+1}\circ J_k\circ\widehat F_k).
   \tag{H}
   $$
   The corrections $h_k$ are tangent to the identity and solve the finite-terminal backward recursion followed by a coefficientwise limit. They equal the identity at nonregular starts. The regular $g_k$ are triangular polynomial automorphisms; bad-step models realize the corrected primary jet using Lemma 8.2.
5. All local maps fix zero. $J_d u$ is the Taylor polynomial through total degree $d$ at zero, as defined at [lines 4806–4807](../paper/paper.tex#L4806-L4807). Equivalently, work in the finite-dimensional space of $\mathbb C^n$-valued polynomials with no constant term, modulo terms of degree $>d$, with composition
   $$
   [u]\star[v]=J_d(u\circ v).
   $$
   This operation is associative; a jet is invertible exactly when its linear part is invertible. It is generally noncommutative. The following formalizations use this actual jet convention, not a different coordinate convention.

Under the modified wording, the prescribed polynomial is

$$
\widetilde H_k=J_d(C_k\circ h_k).
\tag{W}
$$

Here $\widetilde H_k$ denotes the manuscript's current $H_k$. For comparison only, write $H_k^*=J_d(h_k\circ C_k)$. This comparison is used to locate the error, not to replace the submitted definition. The full manuscript contains no second operative definition of $H_k$, no commutation condition on $C_k,h_k$, and no subsequent adjustment of $G_k$ to the reversed composition. In particular, [§9.1](../paper/paper.tex#L5695-L5708) uses (T) with the raw transitions $F_k$.

## Five-item audit summary

“Downstream” below records the inherited failure of a later application, separately from a direct error at the planted step.

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | downstream | §9.1, lines 5695–5708; source of the failed premise: §8.5, lines 5545–5547 | The Cauchy-remainder application lacks its vanishing-jet antecedent. The reassembly error itself is a composition calculation. [Full MP Note](#mp-note) |
| G1 | not_violated | none | Proposition 8.1 and §8.5, lines 5034–5049, 5450–5547 | The step index is arbitrary, with the same assumptions at every index; the failed computation already occurs before universal introduction. [Full G1 Note](#g1-note) |
| G2 | not_violated | none | §8.5, lines 5540–5547; Lemma 8.2, lines 5144–5150 | Realization witnesses can be discharged with all dependencies correctly bound. The target definition is an explicit composition of already fixed maps. [Full G2 Note](#g2-note) |
| DEF | not_violated | none | §§8.1, 8.5, especially lines 5128–5138, 5464–5538, 5545–5547 | The reversed polynomial exists, is locally invertible, and has a unique inverse jet. The false claim is its subsequent compatibility identity. [Full DEF Note](#def-note) |
| CONV | violated | direct | §8.5, lines 5545–5547, compared with (8.21) at lines 5468–5472 | Composition in primary coordinates yields $h_k\circ C_k$; the submitted definition uses $C_k\circ h_k$. An admissible example has defect $(2a_k(1-a_k)z_2^2,0)$. [Full CONV Note](#conv-note) |

<a id="mp-note"></a>
## MP — Note

**Status: violated; role: downstream.** The failed application identified here is the subsequent Cauchy-remainder argument. There is no independently demonstrated theorem-application error in the unchanged primary-coordinate homological construction.

The rule is

$$
\frac{\Gamma\vdash A\qquad\Gamma\vdash A\to B}{\Gamma\vdash B}.
$$

### The local algebra, formalized without inventing a cited theorem

Fix an index $k$ and the data in the common context. Let $\Gamma_0$ consist of their domains and zero-center conditions, invertibility of $C_k,C_{k+1},J_k$, the definitions $G_k=J_kg_k$ and $C_{k+1}F_kC_k^{-1}=J_k\widehat F_k$, and equation (H). For a bad step replace (H) by the jet realization of its corrected primary transition. These are precisely the local dependencies; geometric and grid assumptions are the fixed background establishing them.

In the jet space define

$$
U=J_d(h_{k+1}C_{k+1}F_kC_k^{-1}),\quad
V=J_d(G_kh_k),\quad W=J_dC_k.
$$

A symbolic reconstruction of equality congruence is

$$
\forall u,v,w\quad (u=v\ \longrightarrow\ u\star w=v\star w).
$$

Substitute $u=U,v=V,w=W$. The antecedent $A_0$ is the full equality

$$
J_d(h_{k+1}C_{k+1}F_kC_k^{-1})=J_d(G_kh_k),
$$

which follows from (H) and the two stated definitions. The instantiated consequent $B_0$, after associative composition and inverse cancellation, is

$$
J_d(h_{k+1}C_{k+1}F_k)=J_d(G_kh_kC_k).
\tag{MP-valid}
$$

Thus $\Gamma_0\vdash A_0$, $\Gamma_0\vdash A_0\to B_0$, and $\Gamma_0\vdash B_0$ are a valid application. The conclusion $C_0$ actually asserted after (W) is instead

$$
J_d(C_{k+1}h_{k+1}F_k)=J_d(G_kC_kh_k).
\tag{MP-claimed}
$$

The first failing bridge is the replacement of the composed expressions in (MP-valid) by those in (MP-claimed). The manuscript does not cite a separate implication granting that replacement. Packaging equality congruence into an implication above is explicitly a reconstruction of its algebra: its MP application is valid, and the incorrect identification of its resulting expressions is the CONV failure expanded below. This is different from applying a cited theorem with an additional unproved hypothesis or strengthening that theorem's conclusion.

The actual nearby theorem application is sound. At [lines 5540–5544](../paper/paper.tex#L5540-L5544), for a bad index $k$, set

$$
Q_k=J_d(h_{k+1}C_{k+1}F_kC_k^{-1}h_k^{-1}).
$$

Lemma 8.2 is instantiated with dimension $n$, order $d$, and input jet $Q_k$. Its antecedent is

$$
A_{\mathrm{vol}}:\quad
Q_k(0)=0,\quad \det Q_k'(0)\ne0,\quad
J_{d-1}\det Q_k'=\det Q_k'(0).
$$

Its consequent $B_{\mathrm{vol}}$ is the existence of a polynomial automorphism $p:\mathbb C^n\to\mathbb C^n$ fixing zero with $J_dp=Q_k$, degree and inverse degree at most $D_d$, and coefficients and inverse coefficients bounded by the fixed polynomial supplied by Lemma 8.2 in $\|Q_k\|$ and $\|Q_k'(0)^{-1}\|$. In the corresponding context $\Gamma_{\mathrm{vol}}$, $C_{k+1}F_kC_k^{-1}$ has constant-volume jet by [lines 5135–5142](../paper/paper.tex#L5135-L5142), $h_k,h_{k+1}$ preserve volume through degree $d-1$ by [lines 5530–5538](../paper/paper.tex#L5530-L5538), and all their linear parts are invertible. The chain rule establishes every component of $A_{\mathrm{vol}}$. The conclusion claimed at this application is exactly $B_{\mathrm{vol}}$. Reversing the later definition of $H_k$ changes none of these hypotheses.

### The downstream application with a false antecedent

At [lines 5695–5708](../paper/paper.tex#L5695-L5708), define the actual holomorphic error on a fixed raw transition ball:

$$
E_k(z)=\widetilde H_{k+1}(F_k(z))-G_k(\widetilde H_k(z)).
$$

Fix radii $0<r=R/2<R$ inside that ball. The Cauchy/Taylor implication, with $E:B(R)\to\mathbb C^n$ and $L>0$, is

$$
\begin{aligned}
&\bigl[
E\text{ holomorphic on }B(R),\
\sup_{B(R)}|E|\leq L,\
\forall\alpha\in\mathbb N_0^n,\ |\alpha|\leq d:
\partial^\alpha E(0)=0
\bigr]\\
&\hspace{2em}\Longrightarrow
\bigl[
\forall z\in B(R/2),\
|E(z)|\leq K_{n,d,R}L|z|^{d+1}
\bigr].
\end{aligned}
\tag{Cauchy}
$$

The substitution is $E=E_k$, with $L=L_k$ bounded by $\exp(A_d\Delta s_k+o(s_k))$, absorbing the fixed Cauchy constant. Let $\Gamma_R$ contain the fixed $n,d,k,R$, the actual polynomial definitions, the holomorphic bounded transition $F_k$, and the coefficient bounds in Proposition 8.1; do not insert (T) as an independently proved fact. The antecedent $A_R$ is the complete bracket on the first two lines of (Cauchy). Its holomorphicity and size components hold. Its derivative-vanishing component is the first unestablished obligation: it is precisely (T), obtained earlier by the failed conversion. The consequent $B_R$ is the displayed remainder estimate, and the manuscript's conclusion $C_R$ is that same estimate (9.3).

For the admissible example below,

$$
E_k(z)=(2a_k(1-a_k)z_2^2,0),\qquad
\partial_{z_2}^2(E_k)_1(0)=4a_k(1-a_k)\ne0.
$$

Consequently $\Gamma_R\nvdash A_R$. This is an inherited antecedent failure in a correctly stated implication, so its role is downstream. It contributes no additional direct label.

<a id="g1-note"></a>
## G1 — Note

**Status: not_violated; role: none.**

Use the rule

$$
\frac{\Gamma\vdash A\to B(x)}
{\Gamma\vdash A\to\forall x\,B(x)},
\qquad x\notin FV(\Gamma)\cup FV(A).
$$

Here the relevant quantified variable is the step index, not a coordinate vector secretly chosen to commute with a map. For a precise reconstruction take $x$ to range over $\mathbb N_0$, with $D(x)$ the predicate that $x$ belongs to the retained grid tail. After the manuscript relabels its sufficiently late start as zero, $D(x)$ holds for every $x\in\mathbb N_0$. The range predicate is retained in the formulas to make its discharge explicit; all sequence evaluations have their stated domains.

Let $\Gamma_1$ contain the fixed geometric/chart/grid data in the common context, the domains of the sequences $F,C,h,G$, the zero-center and inverse conditions, and the explicit definition $\widetilde H_i=J_d(C_i h_i)$ for every $i\in\mathbb N_0$. It contains no statement specializing a free index $x$. Put

$$
A_1=
\forall i\in\mathbb N_0\
J_d(h_{i+1}C_{i+1}F_iC_i^{-1})=J_d(G_i h_i),
$$

$$
B_1(x)=
D(x)\ \longrightarrow\
J_d(\widetilde H_{x+1}F_x)=J_d(G_x\widetilde H_x).
$$

The formula $A_1$ records the actually established primary identity, regular or realized on a bad step. It does not add the sought raw-coordinate identity. The asserted universal conclusion is

$$
A_1\ \longrightarrow\
\forall x\in\mathbb N_0\
\left(D(x)\longrightarrow
J_d(\widetilde H_{x+1}F_x)=J_d(G_x\widetilde H_x)\right).
\tag{G1-claimed}
$$

The pre-generalization proof for a fresh natural-number parameter $a$ has this exact shape:

$$
\begin{array}{ll}
1.&[A_1]\quad\text{open assumption},\\
2.&[D(a)]\quad\text{temporary range assumption},\\
3.&J_d(h_{a+1}C_{a+1}F_aC_a^{-1})=J_d(G_a h_a)
       \quad\text{by 1},\\
4.&J_d(h_{a+1}C_{a+1}F_a)=J_d(G_a h_aC_a)
       \quad\text{by composition on the right with }C_a,\\
5.&J_d(C_{a+1}h_{a+1}F_a)=J_d(G_aC_a h_a)
       \quad\text{the failing conversion},\\
6.&D(a)\to J_d(\widetilde H_{a+1}F_a)=J_d(G_a\widetilde H_a)
       \quad\text{intended discharge of 2}.
\end{array}
$$

Line 4 is a valid derivation under the actual assumptions. Line 5 fails at this fixed index, as the quadratic calculation below proves. The intended final introductions would discharge the range assumption, universally quantify the fresh $a$, and discharge $A_1$.

The free parameters in $\Gamma_1,A_1$ are the fixed $n,d,h$, geometric objects, chart and map sequences, grid and rate constants. The index $i$ in $A_1$ is bound. The fresh $a$ occurs only in the temporary range assumption and the indexed formulas, and that assumption is discharged into the restricted conclusion. No assumption that $a$ is a special favorable step is exported. Splitting into regular and bad cases also preserves the stated range: the primary identity is supplied by (H) in one case and realization in the other.

Thus the first failure is line 5, before the G1 rule. There is no additional choice-specific assumption or free-variable violation. In the witness, every step is regular and the defect is nonzero at each individual index; quantifying over indices does not create it. The statement's quantifier order also remains the manuscript's

$$
\forall d\geq2\ \forall h\in(0,1)\
\exists(\text{late grid},H,G)\
\forall k\in\mathbb N_0\ (\text{the stated model properties}),
$$

with the grid and maps chosen after $d,h$. There is no passage to a single grid or correction working independently of those parameters. The invalid ground computation is classified under CONV, rather than adding G1 solely because (T) is asserted for all steps.

<a id="g2-note"></a>
## G2 — Note

**Status: not_violated; role: none.**

The rule is

$$
\frac{\Gamma\vdash A(x)\to B}
{\Gamma\vdash(\exists x\,A(x))\to B},
\qquad x\notin FV(\Gamma)\cup FV(B).
$$

The planted operation itself is the deterministic assignment (W), followed by a claimed equality. At that point $C_k,h_k,G_k,F_k$ are already fixed. No existential premise is used to select a map having an unmentioned commuting property.

The nearest actual existential operation is the bad-step use of Lemma 8.2. Its full witness structure is as follows. Fix a bad index $k$, $n,d$, the maps $C_k,C_{k+1},h_k,h_{k+1},F_k$, and

$$
Q_k=J_d(h_{k+1}C_{k+1}F_kC_k^{-1}h_k^{-1}).
$$

Let $\Gamma_2$ contain these fixed data and definitions; invertibility and the constant-volume conditions on $Q_k$; the identities for inverse jets; and constants $D_d$ and the coefficient-bound polynomial $\mathcal P_{n,d}$ furnished by Lemma 8.2. Set

$$
L_Q=\mathcal P_{n,d}\bigl(\|Q_k\|,\|Q_k'(0)^{-1}\|\bigr).
$$

The witness variable $x$, and the output variable $u$ below, range over polynomial automorphisms of $\mathbb C^n$, so their inverses are defined. Its actual supplied properties are

$$
\begin{aligned}
A_2(x):={}&x\in\operatorname{Aut}_{\rm poly}(\mathbb C^n)
\ \land\ x(0)=0
\ \land\ J_dx=Q_k\\
&{}\land\deg x\leq D_d
\ \land\deg x^{-1}\leq D_d\\
&{}\land\bigl(\|x\|_{\rm coeff}+
\|x^{-1}\|_{\rm coeff}\leq L_Q\bigr).
\end{aligned}
$$

The required primary-coordinate output can be expressed without the witness name:

$$
\begin{aligned}
B_2:=\exists u\ \bigl[&
u\in\operatorname{Aut}_{\rm poly}(\mathbb C^n),\quad u(0)=0,\\
&J_d(u h_k)=J_d(h_{k+1}C_{k+1}F_kC_k^{-1}),\\
&\deg u,\deg u^{-1}\leq D_d,\quad
\|u\|_{\rm coeff}+\|u^{-1}\|_{\rm coeff}\leq L_Q
\bigr].
\end{aligned}
$$

Here commas inside the bracket mean conjunction. An explicit fresh-witness subderivation is

$$
\begin{array}{ll}
1.&\exists x\,A_2(x),\\
2.&\quad[A_2(p)]\quad p\text{ fresh, local to this scope},\\
3.&\quad J_dp=Q_k,\\
4.&\quad J_d(p h_k)=J_d(Q_k h_k)
 =J_d(h_{k+1}C_{k+1}F_kC_k^{-1}),\\
5.&\quad B_2\quad\text{by existential introduction with }u=p,
       \text{ retaining all bounds from 2},\\
6.&B_2\quad\text{by existential elimination, discharging 2}.
\end{array}
$$

The cancellation in line 4 uses the already fixed inverse jet $h_k^{-1}$. The subsequently named model $G_k=p$ depends on the witness within that scope. Exporting the model uses the existentially bound $u$, and all its bounds depend only on $Q_k,n,d$, which are in $\Gamma_2$. Thus $p\notin FV(\Gamma_2)\cup FV(B_2)$. Equivalently, $\Gamma_2\vdash A_2(p)\to B_2$ legitimately yields $\Gamma_2\vdash(\exists p\,A_2(p))\to B_2$.

The raw-coordinate compatibility of the explicit $\widetilde H_k=C_kh_k$ would require the separate, false reordering calculated in the CONV Note. It is not obtained by overlooking a property of the realization witness: the displayed existential derivation remains valid for every realization supplied by the lemma. In particular, the counterexample has no bad steps and uses $G_k=a_kI$ throughout, so the defect occurs without any such realization witness. The manuscript also constructs entire correction sequences before using their individual terms; it does not exchange $\forall k\,\exists h_k$ with a claim that one fixed map works for all $k$.

<a id="def-note"></a>
## DEF — Note

**Status: not_violated; role: none.**

The relevant introduced objects have the following explicit definitions and obligations.

First, [§8.1](../paper/paper.tex#L5094-L5142) defines scalar holomorphic germs

$$
P_k(z)=\log\frac{\det F_k'(z)}{\det F_k'(0)},\quad P_k(0)=0,
\qquad
\ell_k=\sum_{l\geq k}J_{d-1}(P_l\circ F_{s_k,s_l}),
$$

$$
E_k=J_{d-1}e^{\ell_k},\qquad
A_k(z)=
\left(z_1,\ldots,z_{n-1},
\int_0^{z_n}E_k(z_1,\ldots,z_{n-1},\zeta)\,d\zeta\right).
$$

The logarithm exists uniquely as a germ because its argument is holomorphic, nonzero, and equals one at zero. The zero normalization fixes its branch. The series converges coefficientwise by the transition estimate stated in the common context and the summability argument at lines 5111–5122. Since $\ell_k(0)=0$, $E_k(0)=1$. The integral is the unique polynomial primitive in $z_n$ vanishing on $z_n=0$; hence $A_k:\mathbb C^n\to\mathbb C^n$ is a polynomial of degree at most $d$ with $A_k(0)=0$, $A_k'(0)=I$. It is required to be a local change, not a global polynomial automorphism.

Next $C_k=M_kA_k$ is a polynomial map, with $M_k$ an invertible complex matrix. It therefore has a holomorphic inverse germ at zero. The $h_k:\mathbb C^n\to\mathbb C^n$ are polynomial representatives of tangent-to-identity jets. Their degree-by-degree backward recursion is explicitly [lines 5474–5522](../paper/paper.tex#L5474-L5522): lower homogeneous degrees are already fixed before forming $B_k^{(m)}$, forbidden coefficients are solved backward with identity terminal correction, and the uniform envelopes allow a coefficientwise subsequential limit. The construction calls for a chosen limit with those equations and bounds, rather than a unique choice of terminal subsequence. The mutation does not alter that recursion. In the witness it reduces to the scalar recurrence solved exactly below, with a definite limit $h_k=\theta$.

The regular $G_k=J_kg_k$ are global polynomial automorphisms because $g_k$ is triangular with nonzero diagonal linear part; inversion is successive substitution. The bad-step $G_k$ are supplied by the well-instantiated realization lemma formalized in the MP and G2 Notes.

Finally the actual target object is the explicit polynomial

$$
\widetilde H_k(z)=
\sum_{1\leq|\alpha|\leq d}
\frac{\partial^\alpha(C_k\circ h_k)(0)}{\alpha!}\,z^\alpha
:\mathbb C^n\longrightarrow\mathbb C^n.
$$

For fixed $C_k,h_k$ this formula exists and specifies a unique polynomial of degree at most $d$. On sufficiently small neighborhoods the germs compose, and

$$
\widetilde H_k(0)=0,\quad
\widetilde H_k'(0)=C_k'(0)h_k'(0)=M_k,\quad
\det M_k\ne0,
$$

$$
J_d\widetilde H_k^{-1}=J_d(h_k^{-1}\circ C_k^{-1}).
$$

The inverse jet is unique because the linear term is invertible. Composition through degree $d$ depends only on the two input $d$-jets: changing a representative by terms of degree $>d$ cannot create a term of degree at most $d$ when the other map fixes zero. Thus representative independence holds. Its coefficient bounds follow from finite polynomial operations on the polynomially bounded $C_k$ and the $\exp(o(s_k))$ corrections; the same applies to the inverse jet. The center-derivative assertion and the calculation in [lines 5558–5560](../paper/paper.tex#L5558-L5560) survive the reversal.

For a concrete check, in the quadratic witness

$$
C_k=P:(z_1,z_2)\mapsto(-z_1,z_2),\qquad
h_k=\theta:(z_1,z_2)\mapsto(z_1+z_2^2,z_2),
$$

$$
\widetilde H_k=(-z_1-z_2^2,z_2),\qquad
\widetilde H_k^{-1}=\widetilde H_k,\qquad
\det\widetilde H_k'=-1.
$$

Even global invertibility holds in this example. In the nonlinear-primary witness below, $C_k(z)=(z_1,(1+z_1)z_2)$ has local inverse $(w_1,w_2/(1+w_1))$; the reversed map has determinant $1+z_1+z_2^2$, which is nonzero near zero, so its required local inverse also exists.

The defining expression at lines 5545–5546 is not an implicit specification of a solution to (T). It defines an ordinary polynomial local coordinate change, and the next clause asserts (T) as a property to be proved. The explicit object meets its definition and local-coordinate requirements while failing that property. Treating every failed theorem property of an explicitly defined object as an invalid definition would erase the standard's DEF/CONV distinction. Here there is no failed existence, uniqueness, representative-independence, or recursion obligation at the planted definition.

<a id="conv-note"></a>
## CONV — Note

**Status: violated; role: direct.**

### Exact conversion and first incorrect step

Start from the manuscript's equation (8.21), namely (H), and the primary-coordinate transition relation. Every equality below is an equality of $d$-jets:

$$
\begin{aligned}
J_d(G_kh_k)
&=J_d(J_kg_kh_k)\\
&=J_d\!\left(J_kJ_k^{-1}h_{k+1}J_k\widehat F_k\right)\\
&=J_d(h_{k+1}J_k\widehat F_k)\\
&=J_d(h_{k+1}C_{k+1}F_kC_k^{-1}).
\end{aligned}
$$

Composing on the right with $C_k$ gives

$$
\begin{aligned}
J_d(G_kh_kC_k)
&=J_d(h_{k+1}C_{k+1}F_kC_k^{-1}C_k)\\
&=J_d(h_{k+1}C_{k+1}F_k).
\end{aligned}
\tag{correct expansion}
$$

Because every map fixes zero, intermediate truncations do not affect this calculation. Its endpoint is the equality for $H_k^*=J_d(h_kC_k)$.

The actual definition (W) instead expands the claimed endpoint (T) to

$$
J_d(C_{k+1}h_{k+1}F_k)=J_d(G_kC_kh_k).
\tag{wrong endpoint}
$$

This is the first incorrect transformation: it replaces the successive action “$C_k$, then $h_k$” by “$h_k$, then $C_k$” at both endpoints. Associativity allows the parentheses to move; it does not permit this order change. The word “preceded” at line 5546 is therefore material.

Noncommutation alone is not a complete general failure criterion. If

$$
\mathcal E_k=J_d(\widetilde H_k(H_k^*)^{-1}),
$$

then, using the valid correct-order identity, the wrong order satisfies (T) exactly when

$$
J_d(\mathcal E_{k+1}G_k)=J_d(G_k\mathcal E_k).
$$

The [original checker, §2](checker_report.md#2-independently-determining-composition-order-from-the-manuscript), correctly refines the tricker's more general wording on this point. The witnesses below calculate the actual failure of this compatibility, rather than inferring it only from a nonzero commutator.

### An admissible geometric realization

The geometric realization in the existing reports can be verified directly. On $M=\mathbb C^2$, put $x=|z|^2$ and define $\phi(x)\geq0$ by

$$
\int_0^{\phi(x)}u e^u\,du
=(\phi-1)e^\phi+1=\frac{x^2}{2}.
$$

The left side is strictly increasing for $\phi>0$; near zero its expansion gives $\phi=x-x^2/3+O(x^3)$. Put

$$
\Phi(x)=\int_0^x\frac{\phi(v)}v\,dv,\qquad
g=\partial\bar\partial\Phi(|z|^2),\qquad r=\log x.
$$

Differentiating the defining equation yields

$$
p(\phi)=\frac{d\phi}{dr}
=\frac{x^2}{\phi e^\phi}
=2\frac{\phi-1+e^{-\phi}}{\phi}
=2\int_0^1(1-e^{-\phi u})\,du.
$$

The radial and tangential metric eigenvalues are $b=p/x$ and $f=\phi/x$, both positive and tending to one at zero. The radial length is $\sqrt p\,dr/2$, with $p\to2$ at infinity. Radial variation bounds the length of any escaping curve below, proving completeness.

For completeness of the curvature check, inserting $g_{i\bar j}=f\delta_{ij}+f'\bar z_i z_j$ into the Kähler curvature formula on the radial axis gives the unitary components

$$
\begin{aligned}
\mathcal A
&=\frac{-(b'+xb'')+x(b')^2/b}{b^2}=-p''(\phi),\\
\mathcal B
&=\frac{-(f'+xf'')+x(f')^2/f}{bf}
=\frac{p-\phi p'}{\phi^2},\\
\mathcal C
&=-\frac{2f'}{f^2}=\frac{2(\phi-p)}{\phi^2}.
\end{aligned}
$$

Primes on $b,f$ differentiate $x$, and primes on $p$ differentiate $\phi$. The integral representation gives

$$
\mathcal A=2\int_0^1u^2e^{-\phi u}\,du>0,\qquad
p-\phi p'=2\int_0^1[1-(1+\phi u)e^{-\phi u}]\,du>0,
$$

and $0<p<\phi$ from $1-e^{-y}<y$. Their limits at zero are $2/3,1/3,2/3$. For any two nonzero complex tangent vectors $v,w$,

$$
R(v,\bar v,w,\bar w)
=\mathcal A|v_1w_1|^2
+\mathcal B|v_1w_2+v_2w_1|^2
+\mathcal C|v_2w_2|^2>0:
$$

the three squared expressions cannot all vanish unless one vector is zero. This verifies the manuscript's strict bisectional hypothesis.

Also $\det g=\phi p/x^2=e^{-\phi}$. For $D_t(z)=e^{-t/2}z$, the complete metrics

$$
h_t=D_t^*g=\partial\bar\partial\Phi(e^{-t}|z|^2)
$$

satisfy

$$
\partial_t h_t
=-\partial\bar\partial\phi(e^{-t}|z|^2)
=-\operatorname{Ric}(h_t).
$$

Their central values are $h_t(0)=e^{-t}I$, $R(0,t)=2$, hence $s=2t$, $q(s)=s$, and $\lambda_{\min}(t\operatorname{Ric})(0)=s/2$. The rate input holds with $b_0a_0\leq1/2$. Ricci eigenvalues are $p'(\phi),p(\phi)/\phi\in(0,1]$, so $e^{-t}g\leq h_t\leq g$. The full logarithmic volume loss is $2t+\phi(e^{-t}x)-\phi(x)$, between zero and $2t$, and divided by $s$ tends to one on each fixed compact.

For either fixed local biholomorphism $\mathscr R$ used below, with $\mathscr R'(0)$ unitary, take

$$
\Phi_s(z)=e^{s/4}\mathscr R(z),\quad
f_s(X)=\mathscr R^{-1}(e^{-s/4}X),\quad
F_{s,u}=\mathscr R^{-1}\circ(aI)\circ\mathscr R,\quad
a=e^{-(u-s)/4}.
$$

On a sufficiently small fixed chart ball, $\Phi_s^*h_{s/2}=\mathscr R^*g$. Thus the metric and derivative bounds are uniform. The inverse branches are defined on each physical compact for all sufficiently large $s$, with size $O_K(e^{-s/4})$; choose $\sigma<1/4$. The transitions obey $|F_{s,u}(z)|\leq Ca|z|$, $\|J_dF_{s,u}\|\leq C_da$, and $F_{s,u}'(0)=aI$. These give all the center estimates, the transition-jet estimate, and the small-ball estimate: for $\gamma\leq1/4$,

$$
Ca e^{-\gamma s}\leq C e^{-\gamma u},
$$

and a late starting threshold absorbs $C$ after reducing the small-ball exponent.

Here $Q_j=q(e^{hj})=e^{hj}$, so every flag expression is $h(N+1)$. The actual choice $M>3(2N+1)h$ in [lines 5574–5580](../paper/paper.tex#L5574-L5580) leaves every macro interval regular. Both singular rates equal $\Delta s_k/(2\log(s_{k+1}/s_k))$, hence both propagated weights at each step coincide and are positive. A nonlinear monomial of degree $m\geq2$ has input weight $mw_k>w_k$; all such monomials are forbidden. Thus $g_k$ is linear, and equal weights force $L_k^\pm=I$. These facts verify the example against the actual grid and homological algorithm.

### Exact quadratic defect, including the prescribed correction

Choose

$$
\theta(z_1,z_2)=(z_1+z_2^2,z_2),\quad
P(z_1,z_2)=(-z_1,z_2),\quad
\mathscr R=\theta P=(-z_1+z_2^2,z_2).
$$

These are global polynomial automorphisms, $\mathscr R^{-1}=\mathscr R$, and $\mathscr R'(0)=P$ is unitary. At any actual grid step put $a=a_k=e^{-\Delta s_k/4}\in(0,1)$. Substitution gives

$$
F_k=\mathscr R^{-1}(a\mathscr R)
=(az_1+(a^2-a)z_2^2,az_2),\qquad
\det F_k'=a^2.
$$

Consequently $P_k=\ell_k=0$, $E_k=1$, and $A_k=I$ in the volume algorithm. Since $F_k'(0)=aI$, taking the same unitary $P$ at all SVD endpoints is permitted; there is no fixed-phase restriction. Then $C_k=P$, $J_k=I$, and

$$
\widehat F_k=PF_kP^{-1}
=(az_1+(a-a^2)z_2^2,az_2),\qquad G_k=g_k=aI.
$$

To check the correction actually produced, at terminal horizon $l$ put

$$
h_k^{[l]}=(z_1+c_k^{[l]}z_2^2,z_2),\qquad c_l^{[l]}=0.
$$

Equation (H) becomes

$$
ac_k^{[l]}=a-a^2+a^2c_{k+1}^{[l]},\quad
c_k^{[l]}=1-a_k+a_kc_{k+1}^{[l]}
=1-\prod_{i=k}^{l-1}a_i.
$$

The product is $e^{-(s_l-s_k)/4}\to0$, so the prescribed limit is $h_k=\theta$. Composition of these triangular quadratic maps generates no higher homogeneous forcing. This establishes the stated correction for every $d\geq2$, not merely a freely chosen conjugacy.

The submitted definition gives $\widetilde H_k=P\theta=(-z_1-z_2^2,z_2)$. Its claimed zero defect expands as

$$
\begin{aligned}
\widetilde H_{k+1}(F_k(z))
&=\bigl(-[az_1+(a^2-a)z_2^2]-(az_2)^2,\ az_2\bigr)\\
&=(-az_1+(a-2a^2)z_2^2,\ az_2),\\
G_k(\widetilde H_k(z))
&=(-az_1-az_2^2,\ az_2),\\
\widetilde H_{k+1}F_k-G_k\widetilde H_k
&=(2a(1-a)z_2^2,0)\ne0.
\end{aligned}
\tag{verified defect}
$$

The first nonzero term has degree two, so $J_d$ retains it for every allowed $d$. In the same data $H_k^*=\theta P=\mathscr R$ gives exact equality $\mathscr R F_k=a\mathscr R$. This comparison isolates the effect of the changed composition order.

### Nonlinear primary change and the absence of a hidden basis remedy

The second example in the construction/checker materials also checks out independently. With the same flow and chart formula, use

$$
A(z)=(z_1,(1+z_1)z_2),\qquad \mathscr R=\theta A.
$$

The map $A$ is biholomorphic near zero. Its determinant is $1+z_1$, so for $F_k=\mathscr R^{-1}a_k\mathscr R$,

$$
P_k=\log(1+z_1)-\log(1+(F_k)_1).
$$

The finite volume sum telescopes to

$$
J_{d-1}\bigl[\log(1+z_1)-\log(1+(F_{s_k,s_l})_1)\bigr].
$$

The second jet tends coefficientwise to zero as $l\to\infty$. Thus

$$
\ell_k=J_{d-1}\log(1+z_1),\qquad
E_k=J_{d-1}e^{\ell_k}=1+z_1,\qquad A_k=A.
$$

With identity unitary bases, $C_k=A$, $\widehat F_k=\theta^{-1}a_k\theta$, $h_k=\theta$, and $G_k=a_kI$. For $d\geq4$ no truncation changes either polynomial:

$$
\begin{aligned}
H^*=\mathscr R=\theta A
&=(z_1+z_2^2+2z_1z_2^2+z_1^2z_2^2,\ z_2+z_1z_2),\\
\widetilde H=A\theta
&=(z_1+z_2^2,\ z_2+z_1z_2+z_2^3).
\end{aligned}
$$

The lowest layer of $\widetilde H-\mathscr R$ is
$E_3=(-2z_1z_2^2,z_2^3)$. Since $\mathscr R F_k=a_k\mathscr R$ and $F_k=a_kz+O(|z|^2)$,

$$
J_3(\widetilde H F_k-a_k\widetilde H)
=E_3(a_kz)-a_kE_3(z)
=(a_k^3-a_k)(-2z_1z_2^2,z_2^3)\ne0.
$$

The explicit transition used in the independent expansion was

$$
(F_k)_1=a_kz_1+a_k(1-a_k)(1+z_1)^2z_2^2,\qquad
(F_k)_2=\frac{a_k(1+z_1)z_2}{1+(F_k)_1}.
$$

Exact rational jet expansion through degree eight verifies this cubic term, the correct-order conjugacy, and the volume exponential and cocycle. The displayed lowest-degree argument proves the failure for every relevant larger $d$. Section 9 actually imposes $(d+1)\nu>30$ and $\nu<1/10$, so its chosen order is well above four.

Even arbitrary unitary choices $U_k$ do not supply a missing premise in this example. Equal weights leave alignment trivial, and the primary construction gives

$$
C_k=U_kA,\quad h_k=U_k\theta U_k^{-1},\quad
G_k=a_kU_{k+1}U_k^{-1}.
$$

The finite-terminal recursion still gives these $h_k$ in the limit. If the wrong-order conjugacy held, putting
$K_k=U_k^{-1}\widetilde H_k=A\,U_k\theta U_k^{-1}$ and
$Q_k=J_d(K_k\mathscr R^{-1})$ would give

$$
J_d(Q_{k+1}(a_kz))=J_d(a_kQ_k(z)).
$$

The maps $Q_k$ are tangent to the identity and have uniformly bounded coefficients, since $U_k$ is unitary and $d$ is fixed. Every degree-$m\geq2$ coefficient therefore satisfies

$$
q_{k,m}=a_k^{m-1}q_{k+1,m}
=\left(\prod_{i=k}^{l-1}a_i\right)^{m-1}q_{l,m}\longrightarrow0.
$$

Hence $J_dK_k=J_d\mathscr R$. Comparing degree two forces the sole nonlinear homogeneous layer of $U_k\theta U_k^{-1}$ to equal that of $\theta$, so these two maps are equal. Then $K_k=A\theta$, whose cubic layer differs from $\mathscr R=\theta A$ by $E_3$, a contradiction. Thus the nonlinear part of the primary change forced by the volume algorithm also produces a verified defect.

### Actual downstream use

For the quadratic example, along $z=(0,r)$,

$$
\frac{|E_k(0,r)|}{|r|^{d+1}}
=2a_k(1-a_k)|r|^{1-d}\longrightarrow\infty.
$$

This directly falsifies the order-$d+1$ remainder used in (9.3). It also affects the actual compact-orbit regime, not just a formal jet. For $X=(0,1)\in M$, let $b_k=e^{-s_k/4}$. Then

$$
f_{s_k}(X)=(b_k^2,b_k),\qquad
\zeta_k=\widetilde H_kf_{s_k}(X)=(-2b_k^2,b_k),
$$

$$
|r_k|=|\zeta_{k+1}-G_k\zeta_k|
=2a_k(1-a_k)b_k^2.
$$

The actual grid has $\Delta s_k\to\infty$, $\Delta s_k\leq\delta s_k$, and $\delta<1/10$. Eventually $2(1-a_k)\geq1$, whence

$$
|r_k|\geq e^{-s_k/2-\Delta s_k/4}
\geq e^{-21s_k/40}>e^{-10s_k}.
$$

This contradicts [equation (9.6)](../paper/paper.tex#L5738-L5745). Moreover $G_{k,l}=(b_l/b_k)I$, so

$$
\xi_k=\lim_{l\to\infty}G_{k,l}^{-1}\zeta_l=(0,b_k),\qquad
|\xi_k-\zeta_k|=2e^{-s_k/2}>e^{-6s_k}.
$$

Thus the quantitative shadow estimate in [Lemma 9.1](../paper/paper.tex#L5774-L5788) also fails. Its later uses for point separation, derivative nondegeneracy, and inverse-ball inclusion are at [lines 5866–5898](../paper/paper.tex#L5866-L5898), [5902–5928](../paper/paper.tex#L5902-L5928), and [5941–5984](../paper/paper.tex#L5941-L5984). These are downstream effects of the same conversion error.

## Final direct labels and comparison

**Final direct labels: CONV.**

This agrees with the existing direct label in the [case README](../README.md#error-and-classification). The review adds an explicit five-rule audit: MP has a demonstrated downstream antecedent failure at the Cauchy-remainder application; G1 and G2 introduce no separate quantifier-rule failure; DEF's actual object-introduction obligations hold. None of these observations adds a direct label.

The verified witness is an actual complete positively bisectionally curved flow with admissible charts, the manuscript's all-regular grid, and the correction produced by its finite-terminal algorithm. It yields the exact quadratic defect $(2a_k(1-a_k)z_2^2,0)$; the forced nonlinear-primary example independently yields a cubic defect. No unresolved mathematical issue remains for this classification.
