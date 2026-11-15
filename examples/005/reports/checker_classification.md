# 005: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow. It is informed by the complete manuscript and the existing construction/checker materials, rather than being an original workflow report or a blind reviewer run. The classification below is independently reconstructed under the [classification standard](../../../protocol/classification.md).

The inputs are the [modified manuscript](../paper/paper.tex), [original manuscript](../original/paper.tex), [exact mutation](../mutation.diff), [tricker report](tricker_report.md), [original checker report](checker_report.md), and [case README](../README.md). A full source comparison confirms exactly the two recorded tilde deletions. The relevant analytic and numerical calculations in the checker report were independently repeated. The cited paper LXY25 is identified in the manuscript's bibliography but is not supplied as a separate resource. Accordingly, the audit distinguishes the implication actually required by the printed citation from a purported verbatim transcription of that external proposition.

## Target and actual assumptions

The two edits concern the same endpoint estimate:

- [Theorem 1.1, lines 334–358](../paper/paper.tex#L334-L358), specifically line 353, asserts ordinary $L^1(0,T;B^{2\alpha-1}_{\infty,\infty})$ membership for $\nabla u$ when $1/2<\alpha<1$ and $p=2$.
- [Proposition 3.2(1), equation (3.1), lines 4740–4750](../paper/paper.tex#L4740-L4750), specifically line 4748, puts that ordinary norm in an a priori bound.
- Its complete local justification is [lines 5053–5055](../paper/paper.tex#L5053-L5055): “For $\frac12<\alpha<1$, estimate [eq:u-Gam-es2] follows from [LXY25, Proposition 3.2].” There is no intervening endpoint calculation or new regularity assumption.

The spatial domain is $\mathbb R^2$, $\nu=1$, and $\varepsilon=\mathrm{Pr}^{-1}\in(0,1]$. Writing the pressure as $\pi$ to distinguish it from the integrability exponent $p$, the system is

$$
\begin{aligned}
\partial_t\theta+u\cdot\nabla\theta&=0,\\
\varepsilon(\partial_tu+u\cdot\nabla u)+\Lambda^{2\alpha}u
&=-\nabla\pi+\theta e_2,\\
\operatorname{div}u&=0,\qquad (u,\theta)|_{t=0}=(u_0,\theta_0).
\end{aligned}
$$

Here $u,u_0$ are $\mathbb R^2$-valued, $\theta,\theta_0,\pi$ are real-valued, and $\widehat{\Lambda^{2\alpha}f}(\xi)=|\xi|^{2\alpha}\widehat f(\xi)$. In the target branch the initial assumptions are exactly

$$
u_0\in H^1=W^{1,2}(\mathbb R^2),\quad
\operatorname{div}u_0=0,\quad
\theta_0\in L^1\cap L^\infty(\mathbb R^2).
$$

Proposition 3.2 is an estimate for smooth solutions; Theorem 1.1 concerns weak solutions as defined at [lines 4694–4736](../paper/paper.tex#L4694-L4736). Zero temperature is admissible. Neither a $W^{1,p}$ condition with $p>2$ nor an $\ell^1$ summability condition on initial frequency blocks belongs to this branch.

For $s=2\alpha-1\in(0,1)$, the [notation at lines 2473–2504](../paper/paper.tex#L2473-L2504) identifies $C^s$ with $B^s_{\infty,\infty}$, with equivalent spatial norms, and defines ordinary $L^1_T(X)$ as $L^1([0,T];X)$. Set

$$
\begin{aligned}
N_s(f;T)&:=\int_0^T\sup_{j\geq-1}
             2^{js}\|\Delta_jf(t)\|_\infty\,dt,\\
\widetilde N_s(f;T)&:=\sup_{j\geq-1}
             2^{js}\int_0^T\|\Delta_jf(t)\|_\infty\,dt,\\
\omega&:=\partial_1u_2-\partial_2u_1,\qquad
\mathcal R_{1-2\alpha}:=\partial_1\Lambda^{-2\alpha},\qquad
\Gamma:=\omega-\mathcal R_{1-2\alpha}\theta,\\
\mathscr E_\alpha(u,\theta;T)&:=
 \|\nabla u\|_{L^\infty_TL^2}
 +\|\Gamma\|_{L^\infty_TL^2}
 +\|\Gamma\|_{L^1_TB^1_{2,1}}
 +\|\Gamma\|_{\widetilde L^1_TB^{2\alpha}_{2,\infty}}.
\end{aligned}
$$

Thus the modified proposition asserts
$\mathscr E_\alpha+\|\nabla u\|_{L^1_TC^s}\leq Ce^{CT}$;
the [original equation](../original/paper.tex#L4745-L4750) has
$\|\nabla u\|_{\widetilde L^1_TC^s}$ instead. Replacing $C^s$ by its equivalent Besov norm only changes fixed constants, and never exchanges the two time-frequency operations.

The manuscript's [uniformity convention, lines 283–287](../paper/paper.tex#L283-L287), allows constants to depend on the fixed parameters and prescribed bounds on initial data. Consequently, a uniformly bounded set of initial $H^1$ and temperature norms must have a common bound at fixed $T,\alpha,\varepsilon$.

The full-paper dependency check finds no additional hypothesis that changes this conclusion. [Section 4, lines 5924–5932](../paper/paper.tex#L5924-L5932), uses the strict loss $\gamma<2\alpha-1$ for $p=2$, while the equality case invokes the $p>2$ estimate. The stronger velocity hypotheses in the second-order boundary and Prandtl-limit results are local to those results. Appendix A.1 uses ordinary $H^1$ approximations and supplies no uniform higher-frequency summability. The propagation of the edited claim is through [Appendix B.1, lines 9895–9896](../paper/paper.tex#L9895-L9896), [lines 10052–10057](../paper/paper.tex#L10052-L10057), and the [main theorem proof, lines 5871–5874](../paper/paper.tex#L5871-L5874).

## Five-rule audit

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | direct | Proposition 3.2(1), line 4748; its citation at lines 5054–5055; propagated to Theorem 1.1, line 353 | [Full MP Note](#mp-note): the required cited implication has a stronger consequent than the original bound and is disproved on smooth admissible solutions. |
| G1 | not_violated | downstream | Proposition 3.2(1); Theorem 1.1; proof at lines 5847–5888 | [Full G1 Note](#g1-note): the universal claims inherit the failed citation; no selected object's restriction is dropped at universal introduction. |
| G2 | not_violated | downstream | Compactness proposition, lines 9799–9839; main proof, lines 5847–5874 | [Full G2 Note](#g2-note): the subsequence and solution witnesses remain in scope or are bound on export; the missing ordinary uniform estimate is an earlier premise failure. |
| DEF | not_violated | none | Definitions at lines 2554–2631 and 1858–1871; regularization at lines 9058–9127 | [Full DEF Note](#def-note): the multipliers, norms, good unknown, and regularizations are well-defined; membership in the strengthened space is an asserted property. |
| CONV | not_violated | diagnostic | Norm definitions, lines 2597–2631; edited norm, line 4748; citation, lines 5054–5055 | [Full CONV Note](#conv-note): expansion exposes the failed estimate, but the printed target applies a cited result rather than performing a false norm-conversion equality. |

<a id="mp-note"></a>
## MP — Note

**Rule and instantiated application.** Start from

$$
\frac{\Gamma_{\mathrm{log}}\vdash A\qquad
      \Gamma_{\mathrm{log}}\vdash A\to B}
     {\Gamma_{\mathrm{log}}\vdash B}.
$$

The subscript distinguishes the logical context from the manuscript's scalar good unknown $\Gamma$.

Fix $1/2<\alpha<1$, $0<\varepsilon\leq1$, $T>0$, and finite nonnegative bounds $M_u,M_1,M_\infty$. A target object is
$$
z=(u_0,\theta_0,u,\theta,\pi),
$$
where $u_0:\mathbb R^2\to\mathbb R^2$, $\theta_0:\mathbb R^2\to\mathbb R$, and $u,\theta,\pi$ are fields on $[0,T]\times\mathbb R^2$ of the types above. Define $D_{\alpha,\varepsilon,T,M}(z)$ to be the conjunction of:

1. $u,\theta,\pi$ are a smooth solution of each of the three displayed differential equations, with $\nu=1$, and attain the displayed initial data;
2. $\operatorname{div}u_0=0$, $u_0\in H^1$, $\theta_0\in L^1\cap L^\infty$;
3. $\|u_0\|_{H^1}\leq M_u$, $\|\theta_0\|_1\leq M_1$, and $\|\theta_0\|_\infty\leq M_\infty$.

These are the actual assumptions of the target proposition on a prescribed data ball. In particular, smoothness for each selected solution is included; a common bound on its higher Sobolev norms is not assumed.

For a fixed constant $C_0>0$, define the two fully specified consequents

$$
\begin{aligned}
B_{\mathrm{old}}(z;C_0)&:\quad
 \mathscr E_\alpha(u,\theta;T)
 +\|\nabla u\|_{\widetilde L^1_TC^{2\alpha-1}}
 \leq C_0e^{C_0T},\\
B_{\mathrm{new}}(z;C_0)&:\quad
 \mathscr E_\alpha(u,\theta;T)
 +\|\nabla u\|_{L^1_TC^{2\alpha-1}}
 \leq C_0e^{C_0T}.
\end{aligned}
$$

All four terms of $\mathscr E_\alpha$, the construction of $\Gamma$, and both time norms have been expanded above. Uniformity means the constant is chosen before the smooth solution:

$$
\mathcal T_{\mathrm{new}}:\quad
\exists C_0>0\ \forall z\,
\bigl(D_{\alpha,\varepsilon,T,M}(z)
       \to B_{\mathrm{new}}(z;C_0)\bigr).
\tag{MP1}
$$

The constant has the permitted parameter/data-bound dependence and is independent of $\varepsilon$. For disproving (MP1), fixing $\varepsilon=1$ suffices.

The exact printed proof fragment is the citation at lines 5054–5055. The following is a **symbolic reconstruction of that citation**, not an additional argument present in the manuscript. Substitute the paper's $\alpha,\varepsilon,T,u_0,\theta_0,u,\theta$ directly into its claimed instance of LXY25, Proposition 3.2. For a selected smooth $z$,
$$
\Gamma_{\mathrm{log}}\vdash
A:=D_{\alpha,\varepsilon,T,M}(z),
\qquad
\Gamma_{\mathrm{log}}\overset{\text{cited, not established}}{\vdash}
A\to B_{\mathrm{new}}(z;C_0),
$$
and export
$$
C_{\mathrm{manuscript}}=B_{\mathrm{new}}(z;C_0).
\tag{MP2}
$$

Here $\Gamma_{\mathrm{log}}$ consists of the fixed parameter ranges and data bounds, the displayed PDE and Fourier/norm conventions, the definition of $\Gamma$, and the three groups of assumptions in $D(z)$. No ordinary endpoint estimate, extra velocity exponent, or uniform higher Sobolev bound is an open assumption.

The **first failed obligation is availability of the cited implication with the modified consequent**. Its antecedent really holds on the witnesses below. The [original manuscript](../original/paper.tex#L4745-L4750) records $B_{\mathrm{old}}$ with the same [citation](../original/paper.tex#L5053-L5055). If that supplied weaker estimate is the implication used, the valid MP application concludes exactly $B_{\mathrm{old}}$; the exported $C_{\mathrm{manuscript}}=B_{\mathrm{new}}$ differs from it. The external source's complete proposition is not reproduced in the inputs, so this report does not invent its wording or any additional source hypothesis. Instead, the next witness directly disproves the strengthened implication required by the printed citation under the manuscript's own hypotheses.

**Independent admissible witness.** Fix
$$
\alpha=\tfrac34,\qquad \varepsilon=1,\qquad T=1,\qquad p=2.
$$
Use $\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx$ and inverse coefficient $(2\pi)^{-2}$. The [paper's Littlewood–Paley conditions](../paper/paper.tex#L2554-L2583) force $\varphi=1$ on $4/3<|\xi|<3/2$: $\chi$ vanishes there, and every term $\varphi(2^{-j}\xi)$ with $j\geq1$ vanishes there.

Let $a=11/8$, $b=23/16$, and choose
$$
h(\xi)=K
\begin{cases}
\exp\!\left[-\dfrac1{1-(32|\xi|-45)^2}\right],
  &a<|\xi|<b,\\
0,&\text{otherwise},
\end{cases}
\qquad (2\pi)^{-2}\int h=1.
$$
The positive constant $K$ exists because the unnormalized bump has positive finite integral. Set
$$
g=\mathcal F^{-1}h,\qquad
v=\nabla^\perp\Lambda^{-2}g,\qquad
\nabla^\perp=(\partial_2,-\partial_1),\qquad
\lambda_n=16^n,\quad j_n=4n.
$$
Both $g$ and $v$ are real Schwartz functions; their spectra avoid zero. The symbol of $v$ is
$i(\xi_2,-\xi_1)|\xi|^{-2}h(\xi)$, so
$$
\operatorname{div}v=0,\qquad
\partial_1v_2-\partial_2v_1=-\Delta\Lambda^{-2}g=g.
$$
It is a radial tangential field. For any positive $(c_n)\in\ell^2$, set
$$
u_0(x)=\sum_{n\geq1}c_n v(\lambda_nx),\qquad
\theta_0=0,\qquad
u(t)=e^{-t\Lambda^{3/2}}u_0,\qquad \theta(t)=0.
\tag{W1}
$$
The annuli $\lambda_n\operatorname{supp}h$ are disjoint. Moreover $b/2<3/4$ and $2a>8/3$, so each annulus is entirely in precisely its $j_n$-block. With $A_v=\|\nabla v\|_2^2>0$ and $B_v=\|v\|_2^2>0$, Plancherel and two-dimensional scaling give
$$
\|u_0\|_{H^1,\mathrm{Hilbert}}^2
=A_v\sum_n c_n^2+B_v\sum_n c_n^2\lambda_n^{-2}.
\tag{W2}
$$
The manuscript's sum-of-derivative $H^1$ norm is equivalent to this Hilbert norm with fixed constants. Thus the data satisfy its actual $H^1$ convention.

The nonlinear equation is satisfied exactly. Rotational symmetry is preserved by the fractional heat multiplier. Write $u(t,x)=V(t,r)e_\vartheta$, where $e_\vartheta=(-x_2/r,x_1/r)$. Then
$$
(u\cdot\nabla)u=-\frac{V^2}{r}e_r,\qquad
\pi(t,r)=\int_0^r\frac{V(t,\sigma)^2}{\sigma}\,d\sigma,\qquad
\nabla\pi=\frac{V^2}{r}e_r,
$$
while $\partial_tu+\Lambda^{3/2}u=0$. Finite sums in (W1) are global smooth solutions, including at $t=0$; $V=O(r)$ makes the pressure smooth at the origin. This verifies all the equations in $D(z)$, with the correct pressure sign.

For the infinite sum, $u\in C([0,T];H^1)$ and $u$ is smooth for $t>0$. Finite sums converge in $C([0,T];H^1)$. Since $H^1(\mathbb R^2)\hookrightarrow L^4$, their quadratic terms converge in $C([0,T];L^2)$. This passes every term, including the initial term, in [Definition 3.1's pressure-free formulation](../paper/paper.tex#L4694-L4736). Its additional $L^1_TL^p$ condition holds with $p=2$.

The block estimates further give
$$
\|u\|_{L^1_TB^1_{\infty,1}}
\leq C\sum_n c_n\lambda_n^{-1/2}<\infty,\qquad
\|u\|_{\widetilde L^1_TB^{3/2}_{\infty,\infty}}
\leq C\sup_n c_n.
\tag{W3}
$$
Together with $L^\infty_TH^1$ and zero temperature, this places (W1) in the exact uniqueness class $\mathcal X_T$ of [Proposition 3.4, lines 5618–5644](../paper/paper.tex#L5618-L5644). Thus it is the solution relevant to the theorem's assertion.

As calculated in full in the [CONV Note](#conv-note), on disjoint intervals
$$
I_n=[\lambda_n^{-3/2},2\lambda_n^{-3/2}]\subset(0,1)
$$
one has
$$
\|\nabla u(t)\|_{C^{1/2}}\geq c_*c_n\lambda_n^{3/2},
\qquad
\|\nabla u\|_{L^1(0,1;C^{1/2})}\geq c_*\sum_n c_n.
\tag{W4}
$$
The constants are positive and independent of $n$ and of the number of blocks.

For finite sums, take $c_n=N^{-1/2}$, $1\leq n\leq N$. Formula (W2) gives a common bound on the initial $H^1$ norms, and the target norm grows at least as $c_*\sqrt N$. If desired the velocities can all be divided by their actual initial $H^1$ norms; those norms are bounded above and below independently of $N$, and radial swirl remains an exact solution after this rescaling. Thus (MP1) fails even for a family with identical initial velocity norm and zero initial temperature norms.

In the fully numerical parameter substitution of (MP2), take
$$
z=z_N=(u_{0,N},0,u_N,0,\pi_N),\quad
(\alpha,\varepsilon,T,M_1,M_\infty)=(3/4,1,1,0,0),
$$
and choose a single $M_u$ bounding all the initial $H^1$ norms. The established antecedent is
$A_N=D_{3/4,1,1,(M_u,0,0)}(z_N)$, including the exact smooth momentum equation verified above. The required consequent and exported claim are both
$$
B_N=C_N:\quad
\|\nabla u_N\|_{L^\infty_1L^2}
+\|\omega_N\|_{L^\infty_1L^2}
+\|\omega_N\|_{L^1_1B^1_{2,1}}
+\|\omega_N\|_{\widetilde L^1_1B^{3/2}_{2,\infty}}
+\|\nabla u_N\|_{L^1_1C^{1/2}}
\leq C_0e^{C_0}.
$$
No fixed $C_0$ makes the required implication $A_N\to B_N$ true for every $N$.

For one fixed rough datum take $c_n=1/n$. Then
$$
\sum_n c_n^2=\pi^2/6<\infty,\qquad
\sum_n c_n=\infty,
$$
so (W1) is an admissible unique weak solution and its ordinary endpoint norm is infinite. Every $T>0$ contains all sufficiently late $I_n$, proving failure of the added membership on every interval $(0,T)$.

**Downstream MP applications.** In Appendix B.1 the ordinary lower-semicontinuity application would have antecedent
$$
\begin{gathered}
\Delta_j\nabla u_{\delta_k}(t)\to\Delta_j\nabla u(t)
 \text{ in }\mathcal S'\text{ for every }j\text{ and a.e. }t,\\
\sup_kN_{1/2}(\nabla u_{\delta_k};T)\leq K_T<\infty,
\end{gathered}
$$
and consequent $N_{1/2}(\nabla u;T)\leq K_T$. The convergence and lower-semicontinuity implication are sound; the second premise is inherited from the false strengthened proposition. For the paper's actual radial mollifier/cutoff approximation of the datum $c_n=1/n$, this supremum is infinite, as checked below. The main theorem's import of “all the estimates” has the same provenance. These are downstream consequences of the direct citation error.

<a id="g1-note"></a>
## G1 — Note

**Status: not_violated; role: downstream.** The relevant rule is
$$
\frac{\Gamma_{\mathrm{log}}\vdash A\to B(x)}
     {\Gamma_{\mathrm{log}}\vdash A\to\forall x\,B(x)},
\qquad
x\notin\operatorname{FV}(\Gamma_{\mathrm{log}})
       \cup\operatorname{FV}(A).
$$

For the proposition fix $\alpha,\varepsilon,T,M_u,M_1,M_\infty$ as in the MP Note and let $x$ range over the field/data tuples $z=(u_0,\theta_0,u,\theta,\pi)$ defined there. The range predicate is exactly the expanded $D_{\alpha,\varepsilon,T,M}(z)$: smooth solution of the three PDEs with the prescribed initial traces, divergence-free $H^1$ velocity data, $L^1\cap L^\infty$ temperature data, and the three norm bounds.

Let $\Gamma_1$ consist exactly of $\nu=1$, $1/2<\alpha<1$, $0<\varepsilon\leq1$, $T>0$, the three finite nonnegative bounds $M_u,M_1,M_\infty$, the displayed PDE and definitions of $\omega,\Gamma,\Lambda,\Delta_j$, the two time-norm definitions, and the spatial $C^{2\alpha-1}$/Besov norm equivalence. It contains no selected tuple and no assumption of the target estimate. Put $A=\top$, and, for a constant $C_0$ with only the permitted dependence, put
$$
B(x)=D_{\alpha,\varepsilon,T,M}(x)\to
\left(
\begin{aligned}
&\|\nabla u_x\|_{L^\infty_TL^2}
+\|\omega_x-\partial_1\Lambda^{-2\alpha}\theta_x\|_{L^\infty_TL^2}\\
&+\|\omega_x-\partial_1\Lambda^{-2\alpha}\theta_x\|_{L^1_TB^1_{2,1}}
+\|\omega_x-\partial_1\Lambda^{-2\alpha}\theta_x\|_{\widetilde L^1_TB^{2\alpha}_{2,\infty}}\\
&+\|\nabla u_x\|_{L^1_TC^{2\alpha-1}}\leq C_0e^{C_0T}
\end{aligned}
\right),
$$
where $\omega_x=\partial_1(u_x)_2-\partial_2(u_x)_1$.

The actual pre-generalization operation is the citation already identified. Its logical reconstruction is
$$
\begin{array}{ll}
1.&[D_{\alpha,\varepsilon,T,M}(a)]\quad
      \text{for an arbitrary fresh tuple }a;\\
2.&B_{\mathrm{new}}(a;C_0)
      \quad\text{asserted using the citation at 5054–5055};\\
3.&D_{\alpha,\varepsilon,T,M}(a)\to B_{\mathrm{new}}(a;C_0)
      \quad\text{discharging line 1};\\
4.&\forall x\,
   \bigl(D_{\alpha,\varepsilon,T,M}(x)\to B_{\mathrm{new}}(x;C_0)\bigr).
\end{array}
\tag{G1a}
$$

At line 2 the necessary cited implication is unavailable, as the smooth family proves. There is no separate restriction on $a$ that is discarded between lines 3 and 4: its smoothness, initial membership, divergence condition, and norm bounds all remain in the quantified range predicate. After discharge, the free parameters are $\alpha,\varepsilon,T,M_u,M_1,M_\infty,C_0$, not the local name $a$. Neither $\Gamma_1$ nor $A=\top$ contains $a$. Introducing the universal quantifier would be legitimate if line 3 had been proved. Here the earlier MP application is the first failure; merely restating its false consequence for all tuples does not introduce another direct G1 violation.

The rough-data theorem uses a separate approximation argument rather than omitting the smoothness predicate in (G1a). For completeness, fix the admissible datum
$$
d=(u_0,\theta_0),\quad
u_0\in H^1,\quad\operatorname{div}u_0=0,\quad
\theta_0\in L^1\cap L^\infty,
$$
and $\alpha\in(1/2,1)$, $\varepsilon\in(0,1]$. Let $z=(u,\theta)$ denote the unique global solution in the retained class, once obtained by the manuscript's compactness and uniqueness steps. For auditing the last time generalization, use a distinct context $\Gamma_{\mathrm{time}}$: it contains the displayed admissibility assumptions on $d$, $1/2<\alpha<1$, $0<\varepsilon\leq1$, $\nu=1$, the PDE and norm definitions, and the fact that $z$ is the compatible global weak solution in the retained uniqueness class. It contains neither a selected time $T$ nor the ordinary endpoint claim. Define
$$
P(T,z):\quad
\nabla u\in L^\infty(0,T;L^2)
\ \land\
\int_0^T\sup_{j\geq-1}2^{j(2\alpha-1)}
             \|\Delta_j\nabla u(t)\|_\infty\,dt<\infty.
$$
The restricted time claim has the precise G1 form
$$
\Gamma_{\mathrm{time}}
\vdash \top\to\bigl(T>0\to P(T,z)\bigr)
\quad\Longrightarrow\quad
\Gamma_{\mathrm{time}}
\vdash\forall T\in\mathbb R\,(T>0\to P(T,z)).
\tag{G1b}
$$

The [printed proof](../paper/paper.tex#L5847-L5888) fixes an arbitrary interval, invokes the compactness proposition, passes the estimates, and then uses uniqueness to make solutions on different intervals compatible. The assumption $T>0$ is discharged into the range; no particular upper bound on $T$ is retained. Before compatibility, each local solution is correctly allowed to depend on $T$; on overlapping intervals uniqueness identifies the restrictions, yielding the single global $z$ used in (G1b). The remaining free quantities are $d,\alpha,\varepsilon,z$; $T$ is fresh. The fixed datum $c_n=1/n$ disproves the integral in $P(T,z)$ already for a fixed positive $T$, because of the earlier failed estimate. It does not exhibit a violation of the variable condition or a new widening of the chosen time range.

<a id="g2-note"></a>
## G2 — Note

**Status: not_violated; role: downstream.** Start from
$$
\frac{\Gamma_{\mathrm{log}}\vdash A(x)\to B}
     {\Gamma_{\mathrm{log}}\vdash(\exists x\,A(x))\to B},
\qquad
x\notin\operatorname{FV}(\Gamma_{\mathrm{log}})
       \cup\operatorname{FV}(B).
$$

The planted citation at lines 5054–5055 has no existential witness: its operation is the instance $D(z)\to B_{\mathrm{new}}(z;C_0)$ in (MP2). The relevant existential operation downstream is the choice of a convergent subsequence and limiting pair in [Appendix B.1](../paper/paper.tex#L9799-L9839), used in the [main proof](../paper/paper.tex#L5847-L5874).

Here is a concrete reconstruction of that operation. Fix $d=(u_0,\theta_0)$, $\alpha\in(1/2,1)$, $\varepsilon\in(0,1]$, and $T>0$, with the initial hypotheses just listed. Fix admissible mollifier and cutoff functions $\rho,\chi$. Their actual definitions give
$$
\rho_\delta(y)=\delta^{-2}\rho(y/\delta),\quad
\chi_\delta(y)=\chi(\delta y),\quad
u_{0,\delta}=\rho_\delta*\mathbb P(\chi_\delta u_0),\quad
\theta_{0,\delta}=\rho_\delta*\theta_0.
\tag{G2a}
$$
Let $u_\delta,\theta_\delta$ be the corresponding smooth solutions. These objects depend on $d,\rho,\chi,\alpha,\varepsilon$, and the selected time interval. Let a witness
$$
x=(\kappa,v,\eta)
$$
consist of a sequence $\kappa=(\delta_k)_{k\geq1}\subset(0,1]$ tending to zero, a vector field $v$ on $[0,T]\times\mathbb R^2$, and a scalar field $\eta$ there.

Define $A_0(x)$ by all of the following supplied compactness properties:
$$
\begin{gathered}
u_{\delta_k}\rightharpoonup^\ast v
   \text{ in }L^\infty_TH^1,\qquad
u_{\delta_k}\to v
   \text{ in }L^2(0,T;L^2(B_R))\quad\forall R>0,\\
\theta_{\delta_k}\rightharpoonup^\ast\eta
   \text{ in }L^\infty_TL^2
   \text{ and in }L^\infty((0,T)\times\mathbb R^2),\\
(v,\eta)\text{ satisfies all identities of Definition 3.1 with datum }d,\\
\eta\in L^\infty_T(L^1\cap L^\infty),\qquad
v\in L^\infty_TH^1\cap
       \widetilde L^1_TB^{2\alpha}_{\infty,\infty}.
\end{gathered}
\tag{G2b}
$$
The compactness proposition additionally **asserts** that all Proposition 3.2 estimates pass to this limit. Its claimed witness predicate therefore includes
$$
A(x):=A_0(x)\ \land\
       \bigl(\mathscr E_\alpha(v,\eta;T)
               +\|\nabla v\|_{L^1_TC^{2\alpha-1}}\leq K_T\bigr),
\tag{G2c}
$$
where $K_T=C_0e^{C_0T}$ is determined by the original data bounds and fixed parameters, not by the local witness name or the chosen subsequence.

The target after existential elimination is
$$
B:\quad\exists (u,\theta)\,
\left[
\begin{gathered}
(u,\theta)\text{ is a weak solution with datum }d,\\
\theta\in L^\infty_T(L^1\cap L^\infty),\
u\in L^\infty_TH^1\cap\widetilde L^1_TB^{2\alpha}_{\infty,\infty},\\
\mathscr E_\alpha(u,\theta;T)
   +\|\nabla u\|_{L^1_TC^{2\alpha-1}}\leq K_T
\end{gathered}
\right].
\tag{G2d}
$$
Every solution variable in $B$ is bound. The actual elimination has the explicit scope
$$
\begin{array}{ll}
1.&[\exists x\,A(x)]^h;\\
2.&\quad[A(a)]^k,\quad
 a=(\kappa_a,v_a,\eta_a)\text{ a fresh witness};\\
3.&\quad(v_a,\eta_a)\text{ has the weak-solution and norm properties in }B,
       \quad\land\text{-elimination from }A(a);\\
4.&\quad B,\quad\exists\text{-introduction with }(v_a,\eta_a);\\
5.&B,\quad\exists\text{-elimination, discharging }k;\\
6.&(\exists x\,A(x))\to B,\quad\text{discharging }h.
\end{array}
\tag{G2e}
$$
The open background $\Gamma_2$ contains $d,\alpha,\varepsilon,T,\rho,\chi$, the formulas (G2a), the smooth family, the definitions of the norms and equations, and the fixed permitted data-bound constants. Its free parameters do not include $a,\kappa_a,v_a,\eta_a$; none occurs free in $B$. All dependence of the selected limit on the subsequence remains inside (G2c) and is bound before export. Thus this is a valid G2 elimination from the existential assertion actually supplied by the cited compactness proposition.

The earlier assertion $\exists x\,A(x)$ is where the strengthened estimate fails. If only the verified properties $A_0(x)$ are retained, the proof needs the additional premise
$$
U:\quad \sup_{0<\delta\leq1}
       \|\nabla u_\delta\|_{L^1_TC^{2\alpha-1}}\leq K_T
\tag{G2f}
$$
to establish the extra conjunct in (G2c). At [lines 9895–9896](../paper/paper.tex#L9895-L9896), $U$ is claimed for the entire approximation family by reference to Proposition 3.2; it is not a new property secretly demanded of a specially selected subsequence. For the fixed witness datum in (W1), the [calculation below](#conv-note) gives
$\liminf_{\delta\to0}\|\nabla u_\delta\|_{L^1_TC^{1/2}}=\infty$.
The conditional $A_0(x)\to$ the additional bound therefore lacks its earlier uniform-estimate premise. The source of that failure is the audited MP application, not a fresh-witness condition in (G2e).

The quantifier orders are also explicit. Compactness supplies
$$
\forall T>0\ \exists(\kappa_T,v_T,\eta_T)\ A_{0,T}(\kappa_T,v_T,\eta_T);
$$
the paper does not assert a single unconstructed subsequence works for all $T$. Its global solution is obtained using compatibility from uniqueness, which identifies local limits on overlaps. The erroneous ordinary membership is already false before that global passage, on any one fixed interval.

<a id="def-note"></a>
## DEF — Note

**Status: not_violated; role: none.** The edits introduce stronger assertions about existing objects, not a new prescription for the objects. The relevant definition checks are concrete.

**Dyadic operators and time norms.** The paper fixes $\chi,\varphi\in C_c^\infty$ satisfying its partition of unity and defines
$$
\Delta_{-1}f=\mathcal F^{-1}(\chi\widehat f),\qquad
\Delta_jf=\mathcal F^{-1}(\varphi(2^{-j}\cdot)\widehat f)\quad(j\geq0).
$$
These are continuous linear maps $\mathcal S'(\mathbb R^2)\to\mathcal S'(\mathbb R^2)$, with smooth convolution representatives. On the $H^1$ velocities used here, each $\Delta_j\nabla u$ is a bounded smooth function by Bernstein's inequality. For a measurable time-dependent field in these domains, $N_s$ and $\widetilde N_s$ above are extended nonnegative functionals with codomain $[0,\infty]$. The supremum is over the countable set $j\geq-1$, so the integrand is measurable whenever its block norms are measurable. The spaces consist of the elements where the corresponding functional is finite. Distributional derivatives, Fourier multipliers and essential norms depend on the distribution or almost-everywhere class, not a chosen function representative. The partition reconstructs $f$, so a vanishing norm identifies the zero distribution; there is no quotient representative choice or recursion at the target.

The counterexample solution is smooth and continuous into $C^{1/2}$ on every $[\tau,T]$, $\tau>0$, so its ordinary time norm has no measurability ambiguity. Its value $+\infty$ is a valid value of the extended functional. The assertion that this value is finite is the false theorem property.

**Vorticity and good unknown.** The exact defining formulas are
$$
\omega=\partial_1u_2-\partial_2u_1,\qquad
\mathcal R_{1-2\alpha}\theta
 =\mathcal F^{-1}\!\left(i\xi_1|\xi|^{-2\alpha}\widehat\theta\right),
\qquad
\Gamma=\omega-\mathcal R_{1-2\alpha}\theta
$$
at [lines 1858–1871](../paper/paper.tex#L1858-L1871). On the target domain $1/2<\alpha<1$, the kernel of $\mathcal R_{1-2\alpha}$ has magnitude bounded by $C|y|^{2\alpha-3}$. For $\theta\in L^1\cap L^\infty$,
$$
\int_{|y|\leq1}|y|^{2\alpha-3}\,dy
=2\pi\int_0^1r^{2\alpha-2}\,dr
=\frac{2\pi}{2\alpha-1}<\infty,
$$
and the kernel is bounded on $|y|\geq1$. Thus the convolution exists absolutely and gives a unique bounded function. Also $\theta\in L^{1/\alpha}$, and the fractional integration estimate of order $2\alpha-1$, with
$$
\frac12=\alpha-\frac{2\alpha-1}{2},
$$
puts $\mathcal R_{1-2\alpha}\theta$ in $L^2$. Hence for $u\in H^1$, $\omega$ and $\Gamma$ are well-defined $L^2$ scalar fields. In the witness $\theta=0$, this reduces exactly to $\Gamma=\omega$; no low-frequency inverse ambiguity arises.

**Actual approximation objects.** Appendix A.1 defines precisely (G2a), with $0<\delta\leq1$, $\rho\geq0$, $\int\rho=1$, and $0\leq\chi\leq1$, $\chi=1$ on $B_1$, $\operatorname{supp}\chi\subset B_2$. For $u_0\in H^1$, multiplication by the smooth cutoff maps into compactly supported $H^1$; $\mathbb P$ is the unique bounded Leray projection on $L^2$ and commutes with derivatives; convolution then gives
$$
u_{0,\delta},\theta_{0,\delta}\in\bigcap_{m\geq0}H^m,\qquad
\operatorname{div}u_{0,\delta}=0.
$$
For example,
$$
\|\nabla\chi_\delta\,u_0\|_2
\leq\delta\|\nabla\chi\|_\infty\|u_0\|_2,
\quad
\|u_{0,\delta}\|_{H^1}\leq C\|u_0\|_{H^1}.
$$
The cutoff tends to one and the convolution is an approximate identity, giving $u_{0,\delta}\to u_0$ in $H^1$. Temperature convolution is unique, preserves its integral, is contractive on $L^1$ and $L^\infty$, and converges in every finite $L^r$ available here. These are the stated defining requirements, verified in [lines 9058–9127](../paper/paper.tex#L9058-L9127).

For the radial witness choose the permitted $\rho,\chi$ radial. Then
$$
\operatorname{div}(\chi_\delta u_0)
=\nabla\chi_\delta\cdot u_0+\chi_\delta\operatorname{div}u_0=0,
$$
because the first field is radial and the second tangential. Thus $\mathbb P(\chi_\delta u_0)=\chi_\delta u_0$. Radial convolution preserves tangential swirl, and $u_\delta(t)=e^{-t\Lambda^{3/2}}u_{0,\delta}$, $\theta_\delta=0$, gives the actual smooth solution. These objects exist and meet their construction contract. Failure of a later claimed uniform $L^1_TC^{1/2}$ estimate is not failure to define or regularize them.

<a id="conv-note"></a>
## CONV — Note

**Status: not_violated; role: diagnostic.** At the target the manuscript starts with the norm
$\|\nabla u\|_{L^1_T(C^{2\alpha-1})}$ as the last term in (3.1) and claims the endpoint
$$
\mathscr E_\alpha(u,\theta;T)
+\|\nabla u\|_{L^1_T(C^{2\alpha-1})}\leq Ce^{CT}.
$$
The justification at lines 5054–5055 is an application of a separate cited proposition. It prints no equality exchanging an integral and a supremum. The exact definitional expansions are
$$
\begin{aligned}
\|\nabla u\|_{L^1_T(C^s)}
&=\int_0^T\|\nabla u(t)\|_{C^s}\,dt\\
&\asymp\int_0^T\sup_{j\geq-1}
     2^{js}\|\Delta_j\nabla u(t)\|_\infty\,dt
 =N_s(\nabla u;T),\\
\|\nabla u\|_{\widetilde L^1_T(C^s)}
&\asymp
 \sup_{j\geq-1}2^{js}\|\Delta_j\nabla u\|_{L^1(0,T;L^\infty)}\\
&=\sup_{j\geq-1}2^{js}
      \int_0^T\|\Delta_j\nabla u(t)\|_\infty\,dt
 =\widetilde N_s(\nabla u;T).
\end{aligned}
\tag{C1}
$$
The equivalence signs concern only the spatial Hölder/Besov convention. Setting $f_j(t)=2^{js}\|\Delta_j\nabla u(t)\|_\infty\geq0$, the correct calculation is
$$
\int_0^T f_j(t)\,dt
\leq\int_0^T\sup_\ell f_\ell(t)\,dt
\quad\text{for each }j,
\qquad
\sup_j\int_0^T f_j(t)\,dt
\leq\int_0^T\sup_jf_j(t)\,dt.
\tag{C2}
$$
There is no converse supplied by this calculation.

The [printed embedding at lines 2624–2631](../paper/paper.tex#L2624-L2631) does supply
$$
\widetilde L^\rho_TB^{s+\delta}_{q,r}
\hookrightarrow L^\rho_TB^s_{q,r}
\quad\text{if }\delta>0,\text{ or if }\delta=0\text{ and }r\leq\rho.
$$
At the target the parameters would be $q=r=\infty$, $\rho=1$, $\delta=0$, $s=2\alpha-1$, so neither alternative holds. This is a precise diagnosis of why the strengthening is unavailable; the manuscript does not explicitly apply this embedding with these bad parameters or print a reversed version of (C2).

**Full witness calculation.** Use $h,g,v,\lambda_n,j_n,c_n$ from (W1). Fourier scaling and differentiation give
$$
\begin{aligned}
\widehat{c_nv(\lambda_n\cdot)}(\xi)
   &=c_n\lambda_n^{-2}\widehat v(\xi/\lambda_n),\\
\operatorname{curl}[c_nv(\lambda_nx)]
   &=c_n\lambda_ng(\lambda_nx),\\
\widehat{\operatorname{curl}[c_nv(\lambda_n\cdot)]}(\xi)
   &=c_n\lambda_n^{-1}h(\xi/\lambda_n).
\end{aligned}
$$
The heat multiplier multiplies this last expression by $e^{-t|\xi|^{3/2}}$. Exact frequency isolation and the substitution $\xi=\lambda_n\eta$, $d\xi=\lambda_n^2d\eta$, therefore yield
$$
\begin{aligned}
\Delta_{j_n}\omega(t,0)
&=(2\pi)^{-2}\int
  \varphi(\xi/\lambda_n)e^{-t|\xi|^{3/2}}
  c_n\lambda_n^{-1}h(\xi/\lambda_n)\,d\xi\\
&=c_n\lambda_n(2\pi)^{-2}\int
  h(\eta)e^{-t\lambda_n^{3/2}|\eta|^{3/2}}\,d\eta\\
&=c_n\lambda_n F(t\lambda_n^{3/2}),\\
F(\tau)&:=(2\pi)^{-2}\int h(\eta)e^{-\tau|\eta|^{3/2}}\,d\eta.
\end{aligned}
\tag{C3}
$$
Here $\varphi=1$ on $\operatorname{supp}h$. Since $h\geq0$ and $(2\pi)^{-2}\int h=1$,
$$
F(\tau)\geq e^{-2b^{3/2}}=:c_0>0\quad(1\leq\tau\leq2).
$$
The intervals $I_n=[2^{-6n},2^{1-6n}]$ have length $\lambda_n^{-3/2}$, and
$\sup I_{n+1}=(1/32)\inf I_n$, so they are pairwise disjoint in $(0,1)$.
For $t\in I_n$, curl is a difference of two gradient components, hence
$$
\begin{aligned}
\|\nabla u(t)\|_{C^{1/2}}
&\geq c\sup_j 2^{j/2}\|\Delta_j\nabla u(t)\|_\infty\\
&\geq c\,2^{j_n/2}|\Delta_{j_n}\omega(t,0)|\\
&=c\,c_n\lambda_n^{3/2}F(t\lambda_n^{3/2})\\
&\geq c\,c_0c_n\lambda_n^{3/2}.
\end{aligned}
$$
Integrating over the disjoint windows gives
$$
\begin{aligned}
\int_0^1\|\nabla u(t)\|_{C^{1/2}}\,dt
&\geq c\sum_n c_n\lambda_n^{3/2}
     \int_{\lambda_n^{-3/2}}^{2\lambda_n^{-3/2}}
           F(t\lambda_n^{3/2})\,dt\\
&=c\left(\int_1^2F(\tau)\,d\tau\right)\sum_n c_n
\geq c\,c_0\sum_n c_n.
\end{aligned}
\tag{C4}
$$
For $c_n=1/n$ this is infinite; for the finite smooth family it grows at least as $\sqrt N$.

The blockwise norm has a different, finite result. Fourier inversion of the gradient and the support lower bound $|\eta|\geq a$ give
$$
\|\Delta_{j_n}\nabla u(t)\|_\infty
\leq Cc_n\lambda_ne^{-a^{3/2}t\lambda_n^{3/2}}.
$$
All other blocks vanish. Consequently
$$
\begin{aligned}
\widetilde N_{1/2}(\nabla u;T)
&\leq C\sup_n c_n\lambda_n^{3/2}
  \int_0^Te^{-a^{3/2}t\lambda_n^{3/2}}\,dt\\
&=\frac{C}{a^{3/2}}\sup_n c_n
       (1-e^{-a^{3/2}T\lambda_n^{3/2}})\\
&\leq \frac{C}{a^{3/2}}\sup_n c_n<\infty.
\end{aligned}
\tag{C5}
$$
With $\Gamma=\omega$, the remaining terms are finite as well:
$$
\begin{aligned}
\|\nabla u\|_{L^\infty_TL^2}+\|\Gamma\|_{L^\infty_TL^2}
 &\leq C\|(c_n)\|_{\ell^2},\\
\|\Gamma\|_{\widetilde L^1_TB^{3/2}_{2,\infty}}
 &\leq C\sup_n c_n,\\
\|\Gamma\|_{L^1_TB^1_{2,1}}
 &\leq C\sum_n c_n\lambda_n^{-1/2}.
\end{aligned}
\tag{C6}
$$
Indeed a vorticity block has $L^2$ norm at most
$Cc_ne^{-a^{3/2}t\lambda_n^{3/2}}$; multiplying by $\lambda_n^{3/2}$ and integrating yields the second bound, whereas multiplying by $\lambda_n$, summing and integrating yields the third. For $c_n=1/n$, the last sum is
$\sum_{n\geq1}4^{-n}/n=-\log(1-1/4)=\log(4/3)$.

The checker report's numerical constants were also independently recomputed from the one-dimensional radial integrals
$$
F(\tau)=
\frac{\int_a^b r\,\exp[-1/(1-(32r-45)^2)]\,e^{-\tau r^{3/2}}\,dr}
     {\int_a^b r\,\exp[-1/(1-(32r-45)^2)]\,dr}.
$$
Composite Simpson evaluation with 4096 and 8192 subintervals gave, to the displayed digits,
$$
F(1)=0.188698035050,\quad F(2)=0.035624343703,\quad
\int_1^2F(\tau)\,d\tau=0.091815730898.
$$
The analytic lower bound is $c_0=0.031840891871$ to the displayed digits. These computations agree with the [existing checker calculation](checker_report.md); positivity and divergence in (C4) follow analytically, independently of numerical quadrature.

**Actual approximation and lower semicontinuity.** For the radial approximation verified in the DEF Note,
$$
\|u_\delta-u\|_{C([0,T];H^1)}
\leq\|u_{0,\delta}-u_0\|_{H^1}\to0.
$$
For each fixed $j$, Bernstein's inequality gives
$$
\|\Delta_j\nabla(u_\delta-u)\|_{L^\infty_TL^\infty}
\leq C2^j\|u_\delta-u\|_{L^\infty_TH^1}\to0.
$$
For any fixed $M$, all the first $M$ interval lower bounds in (C4) therefore survive with half the constant once $\delta$ is sufficiently small. Thus
$$
\liminf_{\delta\to0}
\|\nabla u_\delta\|_{L^1(0,1;C^{1/2})}
\geq \frac{cc_0}{2}\sum_{n=1}^M\frac1n
\quad\text{for every }M,
$$
and the liminf is infinite.

In general the correct lower-semicontinuity calculation for the ordinary norm, once blockwise distributional convergence is available almost everywhere, is
$$
\begin{aligned}
N_s(\nabla u;T)
&\leq\int_0^T\sup_j
        \liminf_k\bigl(2^{js}\|\Delta_j\nabla u_{\delta_k}(t)\|_\infty\bigr)\,dt\\
&\leq\int_0^T\liminf_k
        \sup_j 2^{js}\|\Delta_j\nabla u_{\delta_k}(t)\|_\infty\,dt\\
&\leq\liminf_k N_s(\nabla u_{\delta_k};T).
\end{aligned}
\tag{C7}
$$
Both inequalities involving supremum and Fatou have the correct direction. The actual approximation makes the right side infinite; the missing finite upper bound is precisely (G2f).

Therefore the concrete computations diagnose the strengthened citation's failure and its downstream uniform-estimate failure. There is no first incorrect printed equality or definitional transformation at the planted step to certify as CONV. Calling the mechanism a reversal of integration and frequency supremum describes why the estimate is false; it does not change the printed citation into a computation that the manuscript never performs.

## Final direct labels

**MP only.** This agrees with the existing label in the [case README](../README.md). No direct G1, G2, DEF, or CONV label is added. The direct failed obligation is the attribution of the strengthened ordinary endpoint estimate to an established proposition at lines 5054–5055. The universal formulation, compactness witnesses, uniform approximation claims, and main-theorem membership propagate that failure; the norm expansions and radial-swirl calculation provide its certificate.

The verified witness consists of exact zero-temperature radial swirl solutions at $\alpha=3/4$, $\varepsilon=1$, with $\lambda_n=16^n$. The coefficients $N^{-1/2}$ on $N$ blocks disprove the uniform smooth a priori bound, while the single datum $c_n=1/n$ has finite initial $H^1$ norm and infinite ordinary critical time norm. The original Chemin–Lerner norm and the other terms remain finite. No mathematical issue needed for this direct classification remains unresolved.
