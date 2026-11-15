# 013: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow, informed by the manuscript and the existing construction and checker materials. It is a classification review rather than an original workflow report or a blind reviewer run.

## Target and actual assumptions

The target is the last paragraph of the proof of `lem:spreadwit`, specifically [modified TeX lines 4332–4336](../paper/paper.tex#L4332): “Fix a sufficiently fine uniform midpoint partition” is followed by “For each $\varepsilon$,” the prescribed transported weights, and the invocation of `lem:startup`. The [original passage](../original/paper.tex#L4332) takes a finite feasible pair for the current exponent directly from `lem:spreadhalf`; the [mutation](../mutation.diff) changes precisely this selection. The full original and modified manuscripts agree outside that replacement.

The class $\mathcal F_{\mu,L}(H)$ consists of real-valued differentiable $\mu$-strongly convex functions with $L$-Lipschitz gradient on the real Hilbert space $H$. As in the manuscript, $\mathbb C^m$ denotes a real space of dimension $2m$, with inner product $\operatorname{Re}\sum_j z_j\overline w_j$.

The hypotheses of [`lem:spreadwit`](../paper/paper.tex#L4290) are as follows. A sequence of positive parameters tends to zero; write $E\subset(0,1)$ for its set of parameter values. At parameter $\varepsilon\in E$,

$$
L=1,\qquad \mu=\varepsilon^2,\qquad
\beta_\varepsilon=1-\theta_\varepsilon\varepsilon,\qquad
h_\varepsilon=y_\varepsilon,
\qquad
(\theta_\varepsilon,y_\varepsilon,\tau_\varepsilon)
\longrightarrow(\theta,y,\tau),\quad \theta,y,\tau>0.
$$

Each tuning has $0\le\beta_\varepsilon<1$, $\tau_\varepsilon\ge0$, $h_\varepsilon>0$ and is quadratically stable. By [`lem:qstab`](../paper/paper.tex#L364), stability is

$$
y_\varepsilon(1+2\tau_\varepsilon)<2(1+\beta_\varepsilon).
$$

Fix $0<c<\theta/2$ and $0<\mathsf s\le\mathsf s_1$. For sufficiently small $\varepsilon$, put

$$
r_\varepsilon=1-c\varepsilon\in(0,1),\qquad
 t_\varepsilon=\log r_\varepsilon<0.
$$

The band is allowed to depend on $\varepsilon$: $K_\varepsilon\in\mathbb N$, $K_\varepsilon\ge3$, $\omega_{0,\varepsilon}=2\pi/K_\varepsilon$, $\mathsf w_\varepsilon=\mathsf s\omega_{0,\varepsilon}$ and

$$
B_\varepsilon=[\omega_{0,\varepsilon}-\mathsf w_\varepsilon,
\omega_{0,\varepsilon}+\mathsf w_\varepsilon]\subset(0,\pi).
$$

With $z=r_\varepsilon e^{i\omega}$, the actual method and normalized symbols are

$$
\begin{aligned}
u_\varepsilon(z)&=(1+\tau_\varepsilon)z-\tau_\varepsilon,\qquad
v_\varepsilon(z)=-h_\varepsilon^{-1}(z-1)(z-\beta_\varepsilon),\\
p_\varepsilon(z)&=\frac{(1+\varepsilon^2)u_\varepsilon(z)-2v_\varepsilon(z)}{1-\varepsilon^2},\\
g_\varepsilon(\omega)&=|u_\varepsilon(z)|^2-|p_\varepsilon(z)|^2,\qquad
s_\varepsilon(\omega)=\operatorname{Im}(p_\varepsilon(z)\overline{u_\varepsilon(z)}),\\
\chi_\lambda(z)&=(z-1)(z-\beta_\varepsilon)+h_\varepsilon\lambda u_\varepsilon(z),\\
X_\varepsilon(\omega)&=\chi_\mu(z)\overline{\chi_L(z)},\qquad
\mathfrak c_\varepsilon=\frac4{y_\varepsilon^2(1-\varepsilon^2)^2},\\
g_\varepsilon-2is_\varepsilon&=-\mathfrak c_\varepsilon X_\varepsilon.
\end{aligned}
$$

The polynomials $u_\varepsilon,v_\varepsilon,p_\varepsilon$ have real coefficients and are evaluated at complex $z$; spectral measures are denoted by $\nu$. The definitions are in [the stationary-method normalization](../paper/paper.tex#L807), [the factor identity](../paper/paper.tex#L832), and [the wave symbols](../paper/paper.tex#L887). Define

$$
\begin{aligned}
\xi&=1-\cos\omega,\qquad
\xi_{\max,\varepsilon}=1-\cos((1+\mathsf s)\omega_{0,\varepsilon}),\\
\Xi_{B,\varepsilon}&=\max_{\omega\in B_\varepsilon}|X_\varepsilon(\omega)|,\\
H_{r_\varepsilon}(\omega)&=\operatorname{Re}[(1-r_\varepsilon e^{i\omega})X_\varepsilon(\omega)],\\
\xi\mathsf M_{r_\varepsilon}(\xi)&=\operatorname{Re}[(1-e^{i\omega})X_\varepsilon(\omega)].
\end{aligned}
$$

The remaining assumptions are

$$
\varepsilon=o(\xi_{\max,\varepsilon}^{3/2}),\qquad
\max_{B_\varepsilon}|\mathsf M_{r_\varepsilon}|=o(\xi_{\max,\varepsilon}^{3/2}),\qquad
H_{r_\varepsilon}\le-\lambda_0\varepsilon\Xi_{B,\varepsilon}
\quad\text{on }B_\varepsilon,
$$

for a fixed $\lambda_0>0$. The unchanged proof establishes $g_\varepsilon,s_\varepsilon>0$ on the band, a continuous phase

$$
g_\varepsilon-2is_\varepsilon=R_\varepsilon e^{-i\Theta_\varepsilon},\qquad R_\varepsilon>0,
$$

and the small-defect hypotheses of `lem:spreadhalf`. The lag-one integrand used below is

$$
\Phi^{(1)}_{t_\varepsilon}(\omega)
=\operatorname{Re}[(1-r_\varepsilon e^{i\omega})(g_\varepsilon-2is_\varepsilon)]
=-\mathfrak c_\varepsilon H_{r_\varepsilon}(\omega).
$$

The proof chooses

$$
\eta=\min\left(\frac12,\frac{\lambda_0}{2c}\right)\in(0,1).
$$

All member-indexed quantities below are taken on a sufficiently small tail of $E$ where $c\varepsilon<1$ and these local sign and phase prerequisites hold; this tail still has zero as an accumulation point.

The smooth kernel $\mathsf k=\mathsf b*\mathsf b$ is fixed as prescribed at [lines 3484–3485](../paper/paper.tex#L3484).

For a probability measure $\nu$ on $B_\varepsilon$, write $G_\varepsilon(\nu)=\int g_\varepsilon\,d\nu$. The exact feasibility requirements in [`def:feas`](../paper/paper.tex#L899) are

$$
\begin{aligned}
|C|&\le G_\varepsilon(\nu),\\
\ell_{n,\varepsilon}(\nu,C)
&=\int\!\left[g_\varepsilon(\cosh(nt_\varepsilon)-\cos(n\omega))
-2s_\varepsilon\sin(n\omega)\right]d\nu+C\sinh(nt_\varepsilon)\ge0,\\
\upsilon_{n,\varepsilon}(\nu,C)
&=\int\!\left[g_\varepsilon(\cosh(nt_\varepsilon)-\cos(n\omega))
+2s_\varepsilon\sin(n\omega)\right]d\nu-C\sinh(nt_\varepsilon)\ge0
\quad(n\in\mathbb N).
\end{aligned}
$$

The edited construction uses one integer $J$ and, for $1\le j\le2J$, sets

$$
\begin{aligned}
a_j&=-1+\frac{j-1/2}{J},\qquad
\omega_{\varepsilon,j}=\omega_{0,\varepsilon}+\mathsf w_\varepsilon a_j,\\
Z_{\varepsilon,J}&=\sum_{l=1}^{2J}\frac{\mathsf k(a_l)}{R_\varepsilon(\omega_{\varepsilon,l})},\qquad
\nu_{\varepsilon,J,j}=\frac{\mathsf k(a_j)/R_\varepsilon(\omega_{\varepsilon,j})}{Z_{\varepsilon,J}},\\
\nu_{\varepsilon,J}&=\sum_j\nu_{\varepsilon,J,j}\delta_{\omega_{\varepsilon,j}},\qquad
G_{\varepsilon,J}=G_\varepsilon(\nu_{\varepsilon,J}),\qquad
C_{\varepsilon,J}=-(1-\eta)G_{\varepsilon,J}.
\end{aligned}
$$

Denote this pair by $Q_\varepsilon(J)$. Write $F_\varepsilon(J)$ for the conjunction that these formulas define a finite probability measure on $B_\varepsilon$, that $|C_{\varepsilon,J}|<G_{\varepsilon,J}$, and that **both displayed lag inequalities hold for every $n\in\mathbb N$**. The adjective “feasible” always includes the lag inequalities.

The finite-atom proof in [`lem:spreadhalf`, lines 3573–3580](../paper/paper.tex#L3573) fixes $t_\varepsilon$ first, sets

$$
n_2(\varepsilon)=\left\lceil\frac{\log(8/\eta)}{|t_\varepsilon|}\right\rceil,
$$

and then chooses a quadrature fine enough to preserve the finitely many strict inequalities with $n<n_2(\varepsilon)$. Since $n_2(\varepsilon)\to\infty$, this supplies a resolution depending on $\varepsilon$. The submitted lemma itself explicitly permits $J=J_\varepsilon$ at [line 4299](../paper/paper.tex#L4299).

The separate uniform finite-dimensional result in [`lem:flowspirals`](../paper/paper.tex#L3725) does not supply the missing premise. It uses frequencies $\omega_j=\varepsilon\gamma_j$, the flow margin, and $\theta/3<c<c_Q(\theta,y)$. The present construction uses the half-step bands and only $0<c<\theta/2$. In the counterfamily below its band remains around $2\pi/3$, and $c_Q(3,2)=\theta/3=1$, so that flow interval is empty. The later invocations in the [wall-layer proof](../paper/paper.tex#L4683), [corner proof](../paper/paper.tex#L4895), and [optimal-tuning proof](../paper/paper.tex#L5129) inherit the unsupported use of `lem:spreadwit`; they do not prove uniform feasibility of the selected grid.

## Five-item audit

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | direct | [4335–4336](../paper/paper.tex#L4335), applying [3146–3154](../paper/paper.tex#L3146) | [Full MP Note](#mp-note): the selected pair fails an upper-lag antecedent of startup. |
| G1 | not_violated | none | [4330–4336](../paper/paper.tex#L4330), with [3573–3580](../paper/paper.tex#L3573) | [Full G1 Note](#g1-note): the universal introductions have the proper parameter scope; their unavailable uniform premise is the G2 defect. |
| G2 | violated | direct | [4332–4334](../paper/paper.tex#L4332), versus [3573–3580](../paper/paper.tex#L3573) | [Full G2 Note](#g2-note): the witness supplied for one parameter is used with an additional false uniform-feasibility property. |
| DEF | not_violated | none | [4332–4334](../paper/paper.tex#L4332), [3484–3485](../paper/paper.tex#L3484) | [Full DEF Note](#def-note): the grid, weights, measure and scalar meet their definition requirements. |
| CONV | not_violated | diagnostic | [4330–4334](../paper/paper.tex#L4330), [899–909](../paper/paper.tex#L899) | [Full CONV Note](#conv-note): the printed computations are correct; an exact slack computation certifies the missing premise. |

<a id="mp-note"></a>

## MP — Note

**Status: violated. Role: direct.** The rule being audited is

$$
\frac{\Gamma\vdash A\qquad\Gamma\vdash A\Rightarrow B}{\Gamma\vdash B}.
$$

Here $\Gamma_{\mathrm{MP}}$ consists of the family, tuning, band, asymptotic, and symbol assumptions specified above; a sufficiently small fixed $\varepsilon\in E$ with $0<\varepsilon<\min(1,1/c)$; the fixed kernel and constants $c,\mathsf s,\lambda_0,\eta$; the chosen finite integer $J$ and the displayed midpoint definitions; and the cited startup implication. Its established local facts are:

- $0<\mu=\varepsilon^2<L=1$, $0\le\beta_\varepsilon<1$, $\tau_\varepsilon\ge0$, $h_\varepsilon>0$, and $h_\varepsilon(1+2\tau_\varepsilon)<2(1+\beta_\varepsilon)$;
- $t_\varepsilon=\log(1-c\varepsilon)<0$, $K_\varepsilon\ge3$, $B_\varepsilon\subset(0,\pi)$, and $g_\varepsilon,s_\varepsilon,R_\varepsilon>0$ on that band;
- the phase-defect bounds $\mathsf d_\varepsilon\le\mathsf m_\varepsilon/2$ and $C_{\mathsf k}(|t_\varepsilon|/(\mathsf m_\varepsilon\mathsf w_\varepsilon))^2+\mathsf d_\varepsilon<\sqrt\eta/8$, where $\mathsf d_\varepsilon=\max_{B_\varepsilon}|\omega-2\Theta_\varepsilon(\omega)|$ and $\mathsf m_\varepsilon=\min(1/4,\omega_{0,\varepsilon}^2/6,c_{\mathsf k}\mathsf s^2)$; and $\int\Phi^{(1)}_{t_\varepsilon}d\nu>\eta r_\varepsilon\sinh|t_\varepsilon|G_\varepsilon(\nu)$ for every probability measure $\nu$ on the band, from [lines 4324–4332](../paper/paper.tex#L4324);
- a finite probability measure $\nu_{\varepsilon,J}$ with $G_{\varepsilon,J}>0$ and $C_{\varepsilon,J}=-(1-\eta)G_{\varepsilon,J}$, hence $|C_{\varepsilon,J}|<G_{\varepsilon,J}$.

In particular, $\Gamma_{\mathrm{MP}}$ does not contain an independently established assertion of all-lag feasibility for this fixed-grid pair. The proof's claim that the selection is sufficient is the obligation under review.

To instantiate [`lem:startup`](../paper/paper.tex#L3146), discard zero-weight atoms and enumerate the remaining distinct frequencies by $1\le j\le m$, where $m\le J$ as checked in the DEF Note. Its universally quantified objects have types

$$
\mu,L,h\in\mathbb R,\quad \beta,\tau,t,C\in\mathbb R,\quad
m\in\mathbb N,\quad (\omega_j)\in[0,\pi]^m,
\quad (\nu_j)\in(0,\infty)^m.
$$

The substitution is

$$
(\mu,L,h,\beta,\tau,t,\nu,C)
=(\varepsilon^2,1,y_\varepsilon,\beta_\varepsilon,
\tau_\varepsilon,t_\varepsilon,\nu_{\varepsilon,J},C_{\varepsilon,J}).
$$

The instantiated antecedent $A$ is the conjunction

$$
\begin{gathered}
0<\varepsilon^2<1,\quad 0\le\beta_\varepsilon<1,\quad
\tau_\varepsilon\ge0,\quad y_\varepsilon>0,\quad
 y_\varepsilon(1+2\tau_\varepsilon)<2(1+\beta_\varepsilon),\\
m\in\mathbb N,\quad \omega_{\varepsilon,j}\in[0,\pi],\quad
\nu_{\varepsilon,J,j}>0,\quad\sum_{j=1}^m\nu_{\varepsilon,J,j}=1,\\
|C_{\varepsilon,J}|\le G_{\varepsilon,J},\\
\forall n\in\mathbb N:\quad
\sum_{j=1}^m\nu_{\varepsilon,J,j}
[g_\varepsilon(\omega_{\varepsilon,j})(\cosh(nt_\varepsilon)-\cos(n\omega_{\varepsilon,j}))
-2s_\varepsilon(\omega_{\varepsilon,j})\sin(n\omega_{\varepsilon,j})]
+C_{\varepsilon,J}\sinh(nt_\varepsilon)\ge0,\\
\forall n\in\mathbb N:\quad
\sum_{j=1}^m\nu_{\varepsilon,J,j}
[g_\varepsilon(\omega_{\varepsilon,j})(\cosh(nt_\varepsilon)-\cos(n\omega_{\varepsilon,j}))
+2s_\varepsilon(\omega_{\varepsilon,j})\sin(n\omega_{\varepsilon,j})]
-C_{\varepsilon,J}\sinh(nt_\varepsilon)\ge0,\\
t_\varepsilon>0\ \Rightarrow\ |C_{\varepsilon,J}|<G_{\varepsilon,J}.
\end{gathered}
$$

The last conditional is vacuous here because $t_\varepsilon<0$. Thus even the stronger strict minimizer check supplies only one part of the needed antecedent.

The consequent $B$ is the existence of an objective $f\in\mathcal F_{\varepsilon^2,1}(\mathbb C^m\oplus\mathbb R)$, normalized to have minimizer $0$, a point $a\ne0$, and a number $c_0>0$, such that the uniquely defined recurrence

$$
\begin{aligned}
x_{-1}=x_0&=a,\qquad \widetilde x_k=(1+\tau_\varepsilon)x_k-\tau_\varepsilon x_{k-1},\\
x_{k+1}&=(1+\beta_\varepsilon)x_k-\beta_\varepsilon x_{k-1}
-y_\varepsilon\nabla f(\widetilde x_k)
\end{aligned}
$$

has

$$
\forall N\in\mathbb N\cup\{0\}:\quad
\|x_N\|\ge c_0r_\varepsilon^N\|a\|.
$$

Startup further specifies that $x_k$ has wave coordinates
$\sqrt{\nu_{\varepsilon,J,j}}z_j^{k+1}$, where $z_j=r_\varepsilon e^{i\omega_{\varepsilon,j}}$, and one scalar coordinate tending to zero. All of these objects may depend on the fixed parameter and on the input pair.

The manuscript's exported conclusion $C_{\mathrm{claim}}$ is the displayed existence and distance bound in $\mathbb C^J\oplus\mathbb R$, followed by $\rho_{\mathcal F}^0\ge r_\varepsilon$. Passing from $m\le J$ to $J$ by unused quadratic coordinates preserves the bound. The rate consequence also follows correctly from $B$: for each $N$, the supremum in [`def:rate`](../paper/paper.tex#L371) is at least $c_0r_\varepsilon^N$, and $(c_0r_\varepsilon^N)^{1/N}\to r_\varepsilon$.

The actual fragment is therefore

$$
\Gamma_{\mathrm{MP}}\vdash |C_{\varepsilon,J}|<G_{\varepsilon,J},
\qquad
\Gamma_{\mathrm{MP}}\vdash A\Rightarrow B,
\qquad
\text{the text concludes }B\text{ and then }C_{\mathrm{claim}}.
$$

The **first failed MP obligation is $\Gamma_{\mathrm{MP}}\vdash A$**: a complete set of lag inequalities has not been established. The CONV Note verifies admissible data for which, for every fixed sufficiently fine $J$ and all sufficiently small positive $\varepsilon$, $\upsilon_{6qJ-1,\varepsilon}<0$. The cited implication is correctly stated; its consequent has not been reversed or strengthened. Its instantiated antecedent is false for the selected pair.

The G2 dependency mistake explains how this pair was selected, while [line 4335](../paper/paper.tex#L4335) is a separate explicit theorem application requiring that pair's feasibility. This is a direct MP violation. Later uses of the lemma merely propagate the unsupported realization and are downstream consequences.

<a id="g1-note"></a>

## G1 — Note

**Status: not_violated. Role: none.** The rule is

$$
\frac{\Gamma\vdash A\Rightarrow B(x)}
{\Gamma\vdash A\Rightarrow\forall x\,B(x)},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(A).
$$

There are three concrete universal structures to distinguish: the valid “every probability measure” lag-one calculation, the all-lag property required of the grid, and the family conclusion “for each $\varepsilon$.”

First fix one member $\varepsilon$. Let $\Gamma_\nu$ consist of its tuning and band, the defined functions $g_\varepsilon,\Phi^{(1)}_{t_\varepsilon}$, and the inequalities

$$
\Phi^{(1)}_{t_\varepsilon}(\omega)\ge\mathfrak c_\varepsilon\lambda_0\varepsilon\Xi_{B,\varepsilon}>0,
\quad g_\varepsilon(\omega)\le\mathfrak c_\varepsilon\Xi_{B,\varepsilon}
\quad(\omega\in B_\varepsilon),
\quad
\eta r_\varepsilon\sinh|t_\varepsilon|\le\lambda_0\varepsilon/2.
$$

The quantified variable $x$ is a finite Borel measure $\nu$ on $[0,\pi]$. Put $A=\top$ and

$$
\begin{aligned}
D_\nu(\nu)&\equiv
\nu\ge0\ \land\ \nu([0,\pi])=1\ \land\ \nu([0,\pi]\setminus B_\varepsilon)=0,\\
B(\nu)&\equiv D_\nu(\nu)\Rightarrow
\left[\int\Phi^{(1)}_{t_\varepsilon}\,d\nu>
\eta r_\varepsilon\sinh|t_\varepsilon|\int g_\varepsilon\,d\nu\right].
\end{aligned}
$$

For an arbitrary fresh $\nu_*$, assume $D_\nu(\nu_*)$. Integration of the two pointwise bounds gives

$$
\int\Phi^{(1)}_{t_\varepsilon}\,d\nu_*
\ge\mathfrak c_\varepsilon\lambda_0\varepsilon\Xi_{B,\varepsilon}
>\tfrac12\mathfrak c_\varepsilon\lambda_0\varepsilon\Xi_{B,\varepsilon}
\ge\eta r_\varepsilon\sinh|t_\varepsilon|\int g_\varepsilon\,d\nu_*.
$$

Discharge $D_\nu(\nu_*)$, then universally quantify $\nu_*$. The only open assumption involving $\nu_*$ was discharged. The free parameters remaining in $\Gamma_\nu$ are $\varepsilon,c,\lambda_0,\eta$ and the method, kernel and band data; none is $\nu_*$. Thus [lines 4330–4332](../paper/paper.tex#L4330) validly establish the claim for every probability measure on that band, including the selected atomic measure. No special choice of the measure is generalized away.

For the family conclusion, the following is a **symbolic reconstruction of the dependency used by the printed passage**, not an additional premise granted to it. Fix a tail bound $\delta>0$ and a resolution $J$. Let

$$
D_\delta(x)\equiv 0<x<\delta\quad(x\in E),\qquad
U_J\equiv\forall a\in E\,[D_\delta(a)\Rightarrow F_a(J)].
$$

Here $U_J$ is precisely the unestablished uniform-feasibility assertion examined in the G2 Note. Let $\mathcal R_x(J)$ mean that there exist $f\in\mathcal F_{x^2,1}(\mathbb C^J\oplus\mathbb R)$ with minimizer zero, $a\ne0$, and $c_0>0$ whose from-rest trajectory satisfies $\|x_N\|\ge c_0(1-cx)^N\|a\|$ for every $N\ge0$. The recurrence is the one in the MP Note with the parameter set to $x$. In the G1 schema take

$$
A=U_J,\qquad B(x)=D_\delta(x)\Rightarrow\mathcal R_x(J),\qquad x\in E.
$$

The background $\Gamma_1$ fixes $E$, the family functions and their stated asymptotic assumptions, $c,\mathsf s,\lambda_0,\eta,\mathsf k,J,\delta$, the formula for $Q_x(J)$, and the startup implication. The tail bound is chosen so the already proved local sign, phase and lag-one conclusions hold on $D_\delta$. The relevant conditional derivation is

$$
\begin{array}{ll}
[U_J]&\text{open conditional assumption},\\
x\text{ arbitrary in }E,&[D_\delta(x)]\text{ open range assumption},\\
F_x(J)&\text{from }U_J\text{ and }D_\delta(x),\\
\mathcal R_x(J)&\text{from feasibility and startup},\\
D_\delta(x)\Rightarrow\mathcal R_x(J)&\text{discharge the range assumption},\\
\forall x\in E\,[D_\delta(x)\Rightarrow\mathcal R_x(J)]&\text{universal introduction},\\
U_J\Rightarrow\forall x\in E\,[D_\delta(x)\Rightarrow\mathcal R_x(J)]&\text{discharge }U_J.
\end{array}
$$

Neither $\Gamma_1$ nor $U_J$ has $x$ free: the parameter in $U_J$ is bound, and $J$ is fixed. The objective, initialization and positive constant are existentially bound separately inside $\mathcal R_x(J)$, so their dependence on $x$ is retained. No property special to a selected $x$ is omitted from the range predicate.

This conditional use of G1 is sound. What the submission lacks is $U_J$ itself; and, at a fixed member, the startup step lacks the corresponding feasible antecedent. These are the demonstrated G2 and MP failures. Treating an unsupported family conclusion alone as a further G1 violation would conflate the acquisition of its premise with universal introduction.

Finally, the original finite-atom paragraph does not generalize from “$n$ below a fixed cutoff” to all $n$. At a fixed $\varepsilon$, it proves the range-restricted statements

$$
\forall n\in\mathbb N\,[n<n_2(\varepsilon)\Rightarrow
(\ell_n\ge0\land\upsilon_n\ge0)],\qquad
\forall n\in\mathbb N\,[n\ge n_2(\varepsilon)\Rightarrow
(\ell_n\ge0\land\upsilon_n\ge0)]
$$

by, respectively, finite approximation and a separate hyperbolic tail bound. Their ranges cover $\mathbb N$. The mutation changes the parameter dependence of the chosen quadrature; it does not insert a distinct finite-to-infinite G1 inference. The quantifier over iteration horizons $N$ is already part of startup's consequent.

<a id="g2-note"></a>

## G2 — Note

**Status: violated. Role: direct.** The rule is

$$
\frac{\Gamma\vdash A(x)\Rightarrow B}
{\Gamma\vdash(\exists x\,A(x))\Rightarrow B},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(B).
$$

The witness here is the finite quadrature resolution. The following explicit reconstruction expresses the choice in [lines 4332–4334](../paper/paper.tex#L4332) and preserves the supplied properties of that witness.

Let $\Gamma_2$ fix the sequence $E$, the entire tuning family, its positive limiting parameters, the constants $c,\mathsf s,\lambda_0,\eta$, the fixed kernel, the member bands and the symbol formulas, with all the actual hypotheses stated above. It includes the cited half-step and startup implications. Choose a fixed $\varepsilon_*\in E$ sufficiently small for the half-step lemma. At this member the supplied hypotheses are:

$$
\begin{gathered}
t_{\varepsilon_*}<0,\quad K_{\varepsilon_*}\ge3,\quad
0<\mathsf s\le\mathsf s_1,\quad
B_{\varepsilon_*}=[(1-\mathsf s)\omega_{0,\varepsilon_*},(1+\mathsf s)\omega_{0,\varepsilon_*}],\\
g-2is=Re^{-i\Theta}\text{ on }B_{\varepsilon_*},\quad R>0,\quad \Theta\text{ continuous},\quad 0<\eta<1,\\
\mathsf d=\max_{B_{\varepsilon_*}}|\omega-2\Theta(\omega)|,\quad
\mathsf m=\min(1/4,\omega_{0,\varepsilon_*}^2/6,c_{\mathsf k}\mathsf s^2),\\
\mathsf d\le\mathsf m/2,\qquad
C_{\mathsf k}\left(\frac{|t_{\varepsilon_*}|}{\mathsf m\mathsf w_{\varepsilon_*}}\right)^2+\mathsf d<\sqrt\eta/8,\\
d\nu^{\mathrm{cont}}_{\varepsilon_*}\text{ proportional to }
\frac{\mathsf k((\omega-\omega_{0,\varepsilon_*})/\mathsf w_{\varepsilon_*})}{R(\omega)}\,d\omega,\\
\int\Phi^{(1)}_{t_{\varepsilon_*}}\,d\nu^{\mathrm{cont}}_{\varepsilon_*}
>\eta r_{\varepsilon_*}\sinh|t_{\varepsilon_*}|
G_{\varepsilon_*}(\nu^{\mathrm{cont}}_{\varepsilon_*}).
\end{gathered}
$$

These are the concrete antecedents of [`lem:spreadhalf`](../paper/paper.tex#L3487). Its finite-atom proof applies to normalized midpoint Riemann sums, because their continuous positive denominator and continuous test functions converge at this fixed member. Accordingly it supplies

$$
\exists j\in\mathbb N\ A(j),\qquad
A(j)\equiv j\ge3\ \land\ F_{\varepsilon_*}(j).
$$

The predicate $F_{\varepsilon_*}(j)$ has been expanded above: its measure has the transported midpoint frequencies, its weights are normalized $\mathsf k/R$ weights, its scalar is $-(1-\eta)G$, its minimizer slack is strict, and both lag inequalities hold at **$t_{\varepsilon_*}$**. The proof obtains these properties after choosing $n_2(\varepsilon_*)$ and then a fine enough resolution. No constraint involving a different member is supplied by $A(j)$.

For precision about the exported conclusion, write $H_m=\mathbb C^m\oplus\mathbb R$. For quantified vectors $\boldsymbol\omega=(\omega_l)_{l=1}^m$ and $\boldsymbol v=(v_l)_{l=1}^m$, abbreviate $\nu_{\boldsymbol\omega,\boldsymbol v}=\sum_{l=1}^m v_l\delta_{\omega_l}$. This vector $\boldsymbol v$ is a weight vector, distinct from the method polynomial $v_\varepsilon$. Write $x^{\varepsilon,f,a}$ for the uniquely defined from-rest recurrence in the MP Note. Then let $\mathcal W_\varepsilon$ mean the following fully quantified statement:

$$
\begin{aligned}
&\exists m\in\mathbb N\ \exists\boldsymbol\omega\in B_\varepsilon^m\quad
\exists\boldsymbol v\in(0,\infty)^m\ \exists C\in\mathbb R\\
&\exists f\in\mathcal F_{\varepsilon^2,1}(H_m)\quad
\exists a\in H_m\setminus\{0\}\ \exists c_0\in(0,\infty):\\
&\quad \sum_{l=1}^m v_l=1
\ \land\ |C|<G_\varepsilon(\nu_{\boldsymbol\omega,\boldsymbol v})\\
&\quad {}\land\ \forall n\in\mathbb N\quad
[\ell_{n,\varepsilon}(\nu_{\boldsymbol\omega,\boldsymbol v},C)\ge0
\land\upsilon_{n,\varepsilon}(\nu_{\boldsymbol\omega,\boldsymbol v},C)\ge0]\\
&\quad {}\land\ \operatorname{argmin}f=\{0\}\\
&\quad {}\land\ \forall N\in\mathbb N\cup\{0\}\quad
[\|x_N^{\varepsilon,f,a}\|\ge c_0r_\varepsilon^N\|a\|].
\end{aligned}
$$

Startup also supplies the wave realization specified in the MP Note. The displayed formula records the actual existential pair-and-distance conclusion of `lem:spreadwit`. Set

$$
B\equiv\exists\delta>0\ \forall\varepsilon\in E
\,[0<\varepsilon<\delta\Rightarrow\mathcal W_\varepsilon].
$$

All dimension, spectrum, objective, initial-point and bound constants are bound inside $\mathcal W_\varepsilon$. Thus the grid witness $j$ is not free in $B$.

The legitimate existential elimination for a **single member** has the following scope. From $\exists j\,A(j)$, open a subderivation with fresh $j_*$ and assumption $A(j_*)$. At $\varepsilon_*$, this gives the fully feasible pair $Q_{\varepsilon_*}(j_*)$. Startup yields the objective and trajectory, and existential introduction packages the pair and realization into $\mathcal W_{\varepsilon_*}$. Discharge $A(j_*)$ and its fresh name. The conclusion $\mathcal W_{\varepsilon_*}$ has no free occurrence of $j_*$. This local G2 application is valid.

The edited selection instead requires the following family subderivation:

$$
\begin{array}{ll}
[\exists j\,A(j)]&\text{existential premise at }\varepsilon_*,\\
\quad[j_*\text{ fresh};\ A(j_*)]&\text{witness scope begins},\\
\quad\varepsilon\in E,\ 0<\varepsilon<\delta&\text{arbitrary subsequent member},\\
\quad Q_\varepsilon(j_*)&\text{defined by the transported-node and weight formulas},\\
\quad |C_{\varepsilon,j_*}|<G_{\varepsilon,j_*},\quad\ell_{1,\varepsilon}>0
&\text{valid local checks},\\
\quad F_\varepsilon(j_*)&\textbf{not supplied by }A(j_*)\textbf{ and not established},\\
\quad\mathcal W_\varepsilon&\text{claimed by startup using this very pair},\\
\quad B&\text{claimed after quantifying the member and tail},\\
B&\text{would require discharging the witness scope}.
\end{array}
$$

The hidden dependencies are explicit: $a_l=a_l(j_*)$; $\omega_{\varepsilon,l}=\omega_{0,\varepsilon}+\mathsf w_\varepsilon a_l(j_*)$; $Z_{\varepsilon,j_*}$ and $\nu_{\varepsilon,j_*,l}$ depend on both the member and that same resolution; $C_{\varepsilon,j_*}$ depends on those weights; and startup's wave coordinates and prescribed normalized values depend on all of these. For example, at wave index $k$ the value is

$$
\psi_k=\frac14\left(C_{\varepsilon,j_*}
+2\sum_l\nu_{\varepsilon,j_*,l}\operatorname{Re}(p_\varepsilon(z_l)\overline{u_\varepsilon(z_l)})\right)e^{2kt_\varepsilon}.
$$

Merely binding the eventual objective and dimension in $B$ does not supply the interpolation inequalities for these particular data.

The actual quantifier difference is

$$
\boxed{\exists\delta_0>0\ \forall\varepsilon\in E\cap(0,\delta_0)\quad
\exists J\in\mathbb N\ F_\varepsilon(J)}
$$

versus the property's order required by the edited construction,

$$
\boxed{\exists J\in\mathbb N\ \exists\delta>0\quad
\forall\varepsilon\in E\cap(0,\delta)\ F_\varepsilon(J)}.
$$

The missing implication inside the witness scope is from $A(j_*)$ to eventual feasibility of $Q_\varepsilon(j_*)$ for every subsequent member. It is a failure of the **conditional derivation required before G2**, through an additional unproved witness property. With the existential conclusions properly written, $j_*\notin\operatorname{FV}(\Gamma_2)\cup\operatorname{FV}(B)$; there is no need to assert a separate eigenvariable-name violation.

The verified counterfamily below establishes, for every fixed sufficiently fine $J$,

$$
\exists\delta_J>0\ \forall\varepsilon\in E\cap(0,\delta_J)\quad
\forall C\in\mathbb R:\quad
(\nu_{\varepsilon,J},C)\text{ is infeasible at }t_\varepsilon.
$$

In particular, a resolution that works at $\varepsilon_*$ fails later on the sequence. This refutes the extra property used in the conditional derivation. It directly certifies G2 without asserting that the unchanged existential conclusion $B$ is itself false.

<a id="def-note"></a>

## DEF — Note

**Status: not_violated. Role: none.** The introduced grid and spectral pair have legitimate defining formulas; their later all-lag property fails.

For each integer $J\ge1$, the uniform partition consists of the $2J$ intervals

$$
I_j=[-1+(j-1)/J,-1+j/J],\qquad 1\le j\le2J,
$$

with the common endpoints assigned consistently if a disjoint measurable partition is desired. Their unique midpoints are $a_j=-1+(j-1/2)/J\in(-1,1)$. The affine map

$$
T_\varepsilon:[-1,1]\longrightarrow B_\varepsilon,
\qquad T_\varepsilon(a)=\omega_{0,\varepsilon}+\mathsf w_\varepsilon a
$$

is a bijection, since $\mathsf w_\varepsilon>0$. It gives distinct admissible frequencies $\omega_{\varepsilon,j}=T_\varepsilon(a_j)$.

The fixed cutoff has $\mathsf b_0\ge0$, equals $1$ on $[-1/8,1/8]$, and vanishes for $|a|\ge1/4$. Thus

$$
\mathsf b(a)=\frac{\mathsf b_0(a)}{\int_{\mathbb R}\mathsf b_0(v)\,dv},\qquad
\mathsf k(a)=\int_{\mathbb R}\mathsf b(v)\mathsf b(a-v)\,dv
$$

are uniquely defined smooth nonnegative functions $\mathbb R\to\mathbb R$. The denominator for $\mathsf b$ is finite and positive. The convolution vanishes for $|a|\ge1/2$, and is positive for $|a|<1/4$: the interiors where both factors equal the positive plateau overlap in an interval of positive length. Consequently every $J\ge3$ has a midpoint at distance $1/(2J)<1/4$ from zero with positive kernel value. This gives an explicit sufficient fineness condition for normalization, independent of any feasibility assertion.

The radius and phase amplitude satisfy

$$
r_\varepsilon=1-c\varepsilon>0,\quad
 t_\varepsilon=\log r_\varepsilon\in\mathbb R,\quad
 R_\varepsilon(\omega)=\sqrt{g_\varepsilon(\omega)^2+4s_\varepsilon(\omega)^2}>0
\quad(\omega\in B_\varepsilon).
$$

For $J\ge3$, each numerator $\mathsf k(a_j)/R_\varepsilon(\omega_{\varepsilon,j})$ is finite and nonnegative, and at least one is positive. Hence $Z_{\varepsilon,J}>0$ and the displayed vector $(\nu_{\varepsilon,J,j})_{j=1}^{2J}$ lies in the probability simplex. It uniquely determines a Borel probability measure $\nu_{\varepsilon,J}$ on $[0,\pi]$, supported in $B_\varepsilon$. Relabeling the nodes does not change the sum, and deleting zero weights does not change the measure. No quotient representative, branch choice, or recursive specification is involved in this introduction.

Since $g_\varepsilon>0$ on the support,

$$
G_{\varepsilon,J}=\sum_j\nu_{\varepsilon,J,j}g_\varepsilon(\omega_{\varepsilon,j})>0,
\qquad C_{\varepsilon,J}=-(1-\eta)G_{\varepsilon,J}\in\mathbb R,
\qquad G_{\varepsilon,J}-|C_{\varepsilon,J}|=\eta G_{\varepsilon,J}>0.
$$

These formulas meet the probability, support, normalization and scalar-definition requirements exactly. As a concrete admissible instance, the TMM family and rational band in the CONV Note have $R_\varepsilon\to4\xi\cos(\omega/2)>0$ uniformly on the band, so all these objects exist for every sufficiently small positive parameter and every $J\ge3$.

There is also no dimension mismatch caused by the $2J$ cells. Positive weights occur only where $|a_j|<1/2$; at most $J$ midpoints have this property. If there are $m<J$ nonzero atoms, the claimed space $\mathbb C^J\oplus\mathbb R$ has enough coordinates. Given a legitimate startup objective on $\mathbb C^m\oplus\mathbb R$, its extension

$$
\widetilde f(z,v,w)=f(z,v)+\frac{1+\varepsilon^2}{4}\|w\|^2,
\qquad w\in\mathbb C^{J-m},
$$

belongs to the same $\mathcal F_{\varepsilon^2,1}$ class; zero initial unused coordinates remain zero. This checks the space convention, conditional on the actual startup hypotheses.

The claimed $f$ at line 4335 is introduced by the separate startup existence theorem, not by a new defining formula for a function. The invalid step is applying that theorem without feasibility. Likewise, “sufficiently fine” invokes the preceding finite-approximation existence guarantee; its unsupported common-parameter interpretation is the G2 witness-property failure. The concrete definitions of $I_j,a_j,T_\varepsilon,Z_{\varepsilon,J},\nu_{\varepsilon,J},G_{\varepsilon,J}$ and $C_{\varepsilon,J}$ remain valid, so no additional direct DEF label is justified.

<a id="conv-note"></a>

## CONV — Note

**Status: not_violated. Role: diagnostic.** The computations actually printed in the target are correct. Expanding the lag definition independently exhibits the missing feasibility property.

### The target's computations

The starting expression for the midpoint weighting is the density in [`lem:spreadhalf`](../paper/paper.tex#L3499), proportional to

$$
\frac{\mathsf k((\omega-\omega_{0,\varepsilon})/\mathsf w_\varepsilon)}{R_\varepsilon(\omega)}\,d\omega.
$$

Substitute $\omega=\omega_{0,\varepsilon}+\mathsf w_\varepsilon a$ and $d\omega=\mathsf w_\varepsilon da$. A midpoint cell has width $1/J$ in $a$, so its unnormalized mass is

$$
\frac{\mathsf w_\varepsilon}{J}\,
\frac{\mathsf k(a_j)}{R_\varepsilon(\omega_{\varepsilon,j})}.
$$

Normalizing cancels the common positive factor $\mathsf w_\varepsilon/J$, giving exactly the manuscript's weights $\nu_{\varepsilon,J,j}$. Substituting the printed $C'=-(1-\eta)\bar g'$ gives the claimed strict minimizer endpoint

$$
\bar g'-|C'|=G_{\varepsilon,J}-(1-\eta)G_{\varepsilon,J}
=\eta G_{\varepsilon,J}>0.
$$

The preceding lag-one computation also holds. Its starting hyperbolic term and complete reduction are

$$
e^{t_\varepsilon}\sinh|t_\varepsilon|
=r_\varepsilon\frac{r_\varepsilon^{-1}-r_\varepsilon}{2}
=\frac{1-r_\varepsilon^2}{2}
=c\varepsilon-\frac{c^2\varepsilon^2}{2}\le c\varepsilon.
$$

Since $\eta c\le\lambda_0/2$, $G_\varepsilon(\nu)\le\mathfrak c_\varepsilon\Xi_{B,\varepsilon}$ and $\Phi^{(1)}_{t_\varepsilon}=-\mathfrak c_\varepsilon H_{r_\varepsilon}$,

$$
\eta e^{t_\varepsilon}\sinh|t_\varepsilon|G_\varepsilon(\nu)
\le\tfrac12\lambda_0\varepsilon\mathfrak c_\varepsilon\Xi_{B,\varepsilon}
<\int\Phi^{(1)}_{t_\varepsilon}\,d\nu.
$$

For $C=-(1-\eta)G_\varepsilon(\nu)$, direct expansion of the lag-one definition gives

$$
\begin{aligned}
\ell_{1,\varepsilon}
&=G_\varepsilon(\nu)\cosh t_\varepsilon
-\int(g_\varepsilon\cos\omega+2s_\varepsilon\sin\omega)d\nu
-(1-\eta)G_\varepsilon(\nu)\sinh t_\varepsilon\\
&=r_\varepsilon^{-1}\int\Phi^{(1)}_{t_\varepsilon}\,d\nu
-\eta\sinh|t_\varepsilon|G_\varepsilon(\nu)>0.
\end{aligned}
$$

Thus there is no incorrect conversion in the weighting, minimizer slack, or lag-one calculation. The next assertion is a theorem application at [line 4335](../paper/paper.tex#L4335), not an equality obtained by expanding these expressions into all the other lag inequalities.

### Admissible counterfamily and independently expanded symbols

Use the exact TMM family from [the robust parameters](../paper/paper.tex#L4734) and [the TMM calculation](../paper/paper.tex#L4814):

$$
\mu=\varepsilon^2,\quad L=1,\quad
\beta_\varepsilon=\frac{(1-\varepsilon)^2}{1+\varepsilon},\quad
 y_\varepsilon=h_\varepsilon=2-\varepsilon,\quad
\tau_\varepsilon=\frac{\beta_\varepsilon}{2-\varepsilon}.
$$

For $0<\varepsilon<1/2$, these satisfy $0<\beta_\varepsilon<1$, $\tau_\varepsilon>0$, $h_\varepsilon>0$ and

$$
y_\varepsilon(1+2\tau_\varepsilon)-2(1+\beta_\varepsilon)
=y_\varepsilon-2=-\varepsilon<0.
$$

Their limits are $(\theta,y,\tau)=(3,2,1/2)$, because $\theta_\varepsilon=(3-\varepsilon)/(1+\varepsilon)$. Choose

$$
c=\frac98<\frac32,\qquad K=3,\qquad \omega_0=\frac{2\pi}{3},\qquad
q\in\mathbb N,\quad q\ge12,\quad q^{-1}\le\mathsf s_1,
\qquad \mathsf s=q^{-1},\quad\mathsf w=\omega_0/q.
$$

The band $B=[(1-1/q)\omega_0,(1+1/q)\omega_0]$ is fixed and allowed. On it,

$$
\frac{11\pi}{18}\le\omega\le\frac{13\pi}{18}<\frac{3\pi}{4},\qquad
1<\xi=1-\cos\omega<1+\frac{\sqrt2}{2}<\frac{12}{7}.
$$

The last inequality is exact, since $\sqrt2<10/7$ follows from $2<100/49$.

Here is an independent algebraic verification of the first-order symbols, also checking the identities tested in the [existing calculation](checker_calculation.py). Put $\rho=1-\varepsilon$, $w=e^{i\omega}$ and $z=(1-c\varepsilon)w$. The exact factors are

$$
\chi_\mu(z)=(z-\rho)(z-\rho^2),\qquad
\chi_L(z)=z(z+\rho),\qquad X_\varepsilon=\chi_\mu\overline{\chi_L}.
$$

At $\varepsilon=0$, using $w\overline w=1$ and $(w-1)^2=-2\xi w$,

$$
X_0=(w-1)^2\overline{w(w+1)}=-2\xi(1+\overline w),
\qquad
\operatorname{Re}X_0=-2\xi(2-\xi),\qquad
\operatorname{Im}X_0=2\xi\sin\omega.
$$

Differentiate with respect to $\varepsilon$ at fixed $\omega$. Since $z'=-cw$, $\rho'=-1$ and $(\rho^2)'=-2$ at zero,

$$
\begin{aligned}
\chi_\mu'(0)&=(w-1)(3-2cw),\\
\chi_L'(0)&=-2cw^2-(c+1)w,\\
X'_0&=(w-1)(3-2cw)\overline{w(w+1)}
+(w-1)^2\overline{-2cw^2-(c+1)w}\\
&=5-(3c+1)w+(5c-1)w^{-1}-(2c+3)w^{-2}.
\end{aligned}
$$

Substitution of $\cos\omega=1-\xi$, $\cos2\omega=1-4\xi+2\xi^2$ and $\sin2\omega=2(1-\xi)\sin\omega$ gives

$$
\begin{aligned}
\operatorname{Re}X'_0&=(6c+14)\xi-(4c+6)\xi^2,\\
\operatorname{Im}X'_0&=[6-4c-(4c+6)\xi]\sin\omega.
\end{aligned}
$$

The mixed symbol is $\xi\operatorname{Re}X_\varepsilon+\sin\omega\operatorname{Im}X_\varepsilon$. It vanishes at zero, and, since $\sin^2\omega=\xi(2-\xi)$,

$$
\begin{aligned}
\left.\partial_\varepsilon(\xi\mathsf M_{r_\varepsilon})\right|_0
&=\xi[(6c+14)\xi-(4c+6)\xi^2]
+\xi(2-\xi)[6-4c-(4c+6)\xi]\\
&=\xi[12-8c+(2c-4)\xi].
\end{aligned}
$$

For $H_{r_\varepsilon}=\operatorname{Re}[(1-(1-c\varepsilon)w)X_\varepsilon]$, the additional differentiated factor contributes $c\operatorname{Re}(wX_0)=-2c\xi(2-\xi)$. Therefore

$$
\left.\partial_\varepsilon H_{r_\varepsilon}\right|_0
=\xi[12-8c+(2c-4)\xi]-2c\xi(2-\xi)
=4(1-c)\xi(3-\xi).
$$

All expressions are smooth on the fixed compact band, so the expansions are uniform. At $c=9/8$ they give

$$
\frac{\mathsf M_{r_\varepsilon}(\xi)}{\varepsilon}\longrightarrow
3-\frac74\xi,\qquad
\frac{H_{r_\varepsilon}(\omega)}{\varepsilon}\longrightarrow
-\frac12\xi(3-\xi).
$$

These computations independently reproduce the relevant [corner expansions](../paper/paper.tex#L4830). Because $1<\xi<12/7<2$, $\xi(3-\xi)\ge2$; hence eventually $H_{r_\varepsilon}\le-3\varepsilon/4$ uniformly. At zero, $|X_0|\le8$, so eventually $\Xi_B\le9$. Consequently

$$
H_{r_\varepsilon}\le-\frac34\varepsilon
\le-\frac1{16}\varepsilon\Xi_B.
$$

Take $\lambda_0=1/16$. This gives exactly the proof's choice $\eta=1/36$. Since $\xi_{\max}>0$ is fixed and $\mathsf M_{r_\varepsilon}=O(\varepsilon)$, both little-$o$ assumptions of `lem:spreadwit` hold.

Finally $\mathfrak c_\varepsilon\to1$, so

$$
g_0=2\xi(2-\xi)>0,\qquad 2s_0=2\xi\sin\omega>0,\qquad
R_0=4\xi\cos(\omega/2)>0,\qquad\Theta_0=\omega/2.
$$

The continuous phase persists with defect $\mathsf d=O(\varepsilon)$. The positive $\mathsf m,\mathsf w,\eta$ are fixed, and $|t_\varepsilon|=O(\varepsilon)$, so both small-defect inequalities of the half-step lemma hold eventually. Its lower lag-one hypothesis was verified above for every probability measure on this band. Thus the witness satisfies all the actual hypotheses at positive $\varepsilon$, including $0<\mu<L$.

### The exact failed upper lag

Fix any $J\ge3$. Its frequencies have the exact rational form

$$
\omega_j=\frac{2\pi}{3}\left(1+\frac{a_j}{q}\right)
=\frac{2\pi}{6qJ}(2qJ+2j-1-2J).
$$

Thus $P=6qJ$ is a common phase period, whether or not it is minimal. Set $n=P-1$. At every atom, including every atom with positive weight,

$$
e^{iP\omega_j}=1,\qquad
\cos(n\omega_j)=\cos\omega_j,\qquad
\sin(n\omega_j)=-\sin\omega_j.
$$

Define the local mixed expression and its average by

$$
b_\varepsilon(\omega)
=g_\varepsilon(\omega)(1-\cos\omega)-2s_\varepsilon(\omega)\sin\omega,
\qquad
D_{\varepsilon,J}=\sum_j\nu_{\varepsilon,J,j}b_\varepsilon(\omega_j).
$$

This $b_\varepsilon$ is distinct from the kernel $\mathsf b$. Expanding the factor identity and mixed symbol gives

$$
\begin{aligned}
b_\varepsilon
&=-\mathfrak c_\varepsilon
[\xi\operatorname{Re}X_\varepsilon+\sin\omega\operatorname{Im}X_\varepsilon]\\
&=-\mathfrak c_\varepsilon\xi\mathsf M_{r_\varepsilon},\qquad
\frac{b_\varepsilon}{\varepsilon}\longrightarrow
-\xi\left(3-\frac74\xi\right).
\end{aligned}
$$

The limit is uniformly strictly negative, since

$$
3-\frac74\xi>\frac{10-7\sqrt2}{8}>0.
$$

The prescribed weights converge to $\nu_{0,J,j}$ because $R_0>0$ and the normalization denominator stays positive. Therefore

$$
G_{\varepsilon,J}\to G_{0,J}>0,\qquad
\frac{D_{\varepsilon,J}}{\varepsilon}\to
D_{*,J}:=-\sum_j\nu_{0,J,j}\xi_j\left(3-\frac74\xi_j\right)<0.
$$

Starting from the manuscript's exact upper-slack expression, every material substitution is

$$
\begin{aligned}
\upsilon_{n,\varepsilon}(\nu_{\varepsilon,J},C)
&=G_{\varepsilon,J}\cosh(nt_\varepsilon)
-\sum_j\nu_{\varepsilon,J,j}g_\varepsilon(\omega_j)\cos(n\omega_j)
+\sum_j\nu_{\varepsilon,J,j}2s_\varepsilon(\omega_j)\sin(n\omega_j)
-C\sinh(nt_\varepsilon)\\
&=G_{\varepsilon,J}\cosh(nt_\varepsilon)
-\sum_j\nu_{\varepsilon,J,j}g_\varepsilon(\omega_j)\cos\omega_j
-\sum_j\nu_{\varepsilon,J,j}2s_\varepsilon(\omega_j)\sin\omega_j
-C\sinh(nt_\varepsilon)\\
&=D_{\varepsilon,J}+G_{\varepsilon,J}(\cosh(nt_\varepsilon)-1)
-C\sinh(nt_\varepsilon).
\end{aligned}
$$

For the printed $C=C_{\varepsilon,J}=-(35/36)G_{\varepsilon,J}$ this becomes

$$
\upsilon_{n,\varepsilon}
=D_{\varepsilon,J}+G_{\varepsilon,J}(\cosh(nt_\varepsilon)-1)
+\frac{35}{36}G_{\varepsilon,J}\sinh(nt_\varepsilon).
$$

Since $J$ and hence $n$ are fixed in this limit,

$$
\frac{t_\varepsilon}{\varepsilon}\to-\frac98,
\qquad \cosh(nt_\varepsilon)-1=O(\varepsilon^2),
\qquad \frac{\sinh(nt_\varepsilon)}{\varepsilon}\to-\frac98n.
$$

The correct endpoint is consequently

$$
\boxed{\frac{\upsilon_{n,\varepsilon}}{\varepsilon}
\longrightarrow D_{*,J}-\frac{35}{32}nG_{0,J}<0.}
$$

This contradicts the upper-lag property required for the startup invocation. At the same time $G_{\varepsilon,J}-|C_{\varepsilon,J}|=G_{\varepsilon,J}/36>0$. The lower lag-one slack also stays positive: its first-order limit is $D_{*,J}+35G_{0,J}/32$, and pointwise

$$
\frac{-\xi(3-7\xi/4)}{2\xi(2-\xi)}
=\frac{7\xi/4-3}{2(2-\xi)}> -\frac58
\quad(\xi>1),
$$

because the derivative of the ratio is $1/[4(2-\xi)^2]>0$. Its averaged lower-lag limit therefore exceeds $15G_{0,J}/32>0$. The diagnostic separates the correctly checked local constraints from the actual later failure.

For completeness, this obstruction survives **every** choice of the real value constant, even one depending arbitrarily on $\varepsilon$. At the same lag,

$$
\begin{aligned}
\ell_{1,\varepsilon}&=D_{\varepsilon,J}+G_{\varepsilon,J}(\cosh t_\varepsilon-1)+C\sinh t_\varepsilon,\\
\upsilon_{n,\varepsilon}&=D_{\varepsilon,J}+G_{\varepsilon,J}(\cosh(nt_\varepsilon)-1)-C\sinh(nt_\varepsilon).
\end{aligned}
$$

Let $A_\varepsilon=\sinh(nt_\varepsilon)/\sinh t_\varepsilon>0$. Multiplying the first equality by $A_\varepsilon$ and adding cancels $C$ exactly:

$$
\begin{aligned}
A_\varepsilon\ell_{1,\varepsilon}+\upsilon_{n,\varepsilon}
&=(A_\varepsilon+1)D_{\varepsilon,J}\\
&\quad+G_{\varepsilon,J}
[A_\varepsilon(\cosh t_\varepsilon-1)+\cosh(nt_\varepsilon)-1].
\end{aligned}
$$

Here $A_\varepsilon\to n$ and the bracket is $O(\varepsilon^2)$, whence

$$
\boxed{\frac{A_\varepsilon\ell_{1,\varepsilon}+\upsilon_{n,\varepsilon}}{\varepsilon}
\longrightarrow(n+1)D_{*,J}<0.}
$$

Two nonnegative slacks would have a nonnegative positive combination. Thus no $C$ gives feasibility for this grid at all sufficiently small positive parameters. The threshold may depend on $J$, exactly as required to refute a single fixed resolution on an eventual tail. Moreover

$$
n_2(\varepsilon)=\left\lceil\frac{\log288}{|\log(1-9\varepsilon/8)|}\right\rceil\to\infty,
$$

so the bad lag $6qJ-1$ eventually lies below the cited finite-atom proof's cutoff.

By the exact interpolation identity in [`lem:waves`](../paper/paper.tex#L2731), the failed upper wave slack is

$$
R_{k,k+n}-T_{k,k+n}
=\tfrac12e^{(2k+n)t_\varepsilon}\upsilon_{n,\varepsilon}<0.
$$

This gives its mathematical significance: the selected spectral data violate a necessary interpolation inequality. The calculation diagnoses the G2 witness property and MP antecedent. The manuscript does not print a false equality in this calculation; its incorrect transition is from the correctly defined pair and correct minimizer slack to the startup conclusion. Hence CONV has a diagnostic role and is not a direct label.

## Final direct classification

**Direct labels: G2 (G), MP.** G2 is the unsupported use of a parameter-specific finite quadrature witness as a uniform fixed-resolution witness. MP is the explicit startup invocation with a pair that violates its required upper-lag inequality.

This agrees with the [curated README's G2 primary and MP secondary labels](../README.md#L3). Relative to the [tricker report's G2-only assignment](tricker_report.md#L625), this review also records MP as a demonstrated direct violation; the [original checker](checker_report.md#L37) already identifies that precise missing startup antecedent. The five-item audit adds no direct G1, DEF or CONV label: universal introduction does not introduce another dependency error, the spectral objects are well-defined, and the correct computations expose the failed premise.

The witness is verified for every fixed sufficiently fine midpoint resolution on the stated admissible TMM family, with $c=9/8$, a permitted rational-width band around $2\pi/3$, and bad lag $6qJ-1$. The proof's strict minimizer and lower lag-one checks both remain valid there. The unchanged lemma permits parameter-dependent $J_\varepsilon$; the mathematical defect is in the submitted fixed-grid proof. No mathematical issue remains unresolved for this classification.
