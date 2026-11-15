# 006: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow, informed by the source and existing construction/checker materials, rather than an original workflow report or a blind reviewer run. The classifications below follow the [classification standard](../../../protocol/classification.md). Reviewer verdicts and target-detection counts do not enter the assessment.

## Target, actual assumptions, and evidence

The planted change is the fraction defining $\gamma_d(p)$ in [§1.2, equation (1.8), line 369](../paper/paper.tex#L369). Write this printed function as $\widetilde\gamma_d$ in this review:

$$
\widetilde\gamma_d(p)
=\frac{30+d^2+15d-p(d^2+7d-2)}
 {d^2+7d-2-(d+1)(d-2)p}.
$$

The immediately following [equation (1.9), lines 373–380](../paper/paper.tex#L373) asserts

$$
q>\widetilde\gamma_d(p)
\quad\Longleftrightarrow\quad
\mathcal D(\phi_0)<0,
\qquad
\mathcal D(u):=
\left.\frac{d^2}{d\lambda^2}E(u^\lambda)\right|_{\lambda=1},
\qquad
u^\lambda(z)=\lambda^{d/2}u(\lambda z).
$$

Here $z\in\mathbb R^d$, $\lambda>0$, and the unchanged energy is

$$
E(u)=\frac12\int_{\mathbb R^d}|\nabla u|^2
 +\frac1{p+1}\int_{\mathbb R^d}|u|^{p+1}
 -\frac1{q+1}\int_{\mathbb R^d}|u|^{q+1}.
$$

The [global parameter assumptions, lines 211–241](../paper/paper.tex#L211), are

$$
d\in\mathbb N_{\ge1},\qquad p,q\in\mathbb R,\qquad
1<p<q<q_S(d),\qquad
q_S(d)=
\begin{cases}\infty,&d=1,2,\$d+2)/(d-2),&d\ge3.\end{cases}
$$

Equation (1.8) is introduced in the mass-subcritical regime $q<p_{\mathrm c}(d)=1+4/d$. The later application at [lines 682–684](../paper/paper.tex#L682) also claims the non-strict characterization
$q\ge\widetilde\gamma_d(p)\iff\mathcal D(\phi_0)\le0$.
It uses this to supply the hypothesis of [Theorem 1.3, lines 672–679](../paper/paper.tex#L672):

$$
d\ge2,\quad \phi_0\in\mathcal F(H^1),\quad
\mathcal D(\phi_0)\le0
\quad\Longrightarrow\quad
\langle\eta_0,\phi_0\rangle<0.
$$

The objects and conventions in this implication are as follows.

- $\phi_0$ is the unique positive, centered radial, decreasing ground state of $-\Delta u+u^p-u^q=0$. Its ground-state definition is minimization of $E$ among nonzero stationary solutions in $X_0=\dot H^1\cap L^{p+1}$; see [lines 805–838](../paper/paper.tex#L805).
- $\mathcal F(H^1)=\{u:\int(1+|z|^2)|u(z)|^2\,dz<\infty\}$, as defined at [lines 478–488](../paper/paper.tex#L478). Thus this assumption includes $L^2$-integrability.
- $L_0=-\Delta+p\phi_0^{p-1}-q\phi_0^{q-1}$, and $\eta_0$ is the canonical regular radial solution of $L_0\eta_0=-\phi_0$, with the asymptotic condition of [Proposition 4.5, lines 2111–2124](../paper/paper.tex#L2111). For the witness below this is $\eta_0\sim-r^2\phi_0$. The [notation convention, lines 756–771](../paper/paper.tex#L756), makes $f\sim g$ mean a ratio tending to a positive constant.
- Pairings are real integrals. The weighted hypothesis gives absolute convergence of $\langle\eta_0,\phi_0\rangle$; the explicit witness below has the stronger property $\eta_0\in H^1$.

I read the complete 5,560-line modified manuscript and compared the complete original against it: the sole differing line is 369, exactly as recorded in the [mutation](../mutation.diff). The [original line 369](../original/paper.tex#L369) contains the correct fraction obtained independently below. I checked the PDF's target and application text and all three unchanged [figure resources](../paper/figures/unstable_dgeq3.pdf). The one- and two-dimensional figures agree with the unchanged low-dimensional specializations; the higher-dimensional figure supplies no additional numerical restriction. The [tricker report](tricker_report.md), [existing checker report](checker_report.md), and [case README](../README.md) were examined as evidence. The displayed mathematical calculations were independently recomputed using exact rational and polynomial arithmetic.

Searching the full manuscript for every threshold reference supplies no alternative corrected formula. In particular, the extra condition $p\ge p^*$ for $d\ge7$ in [equation `eq:high-d`, lines 624–627](../paper/paper.tex#L624) belongs to Theorem 1.2(ii) and the §7 identification of the finite mass-slope limit. Theorem 1.3 and its §8 proof have no such restriction.

The admissible witness is

$$
(d,p,q,\omega)=\left(8,\frac{23}{19},\frac{27}{19},0\right).
$$

For its actual ground state and canonical $\eta_0$, the exact results, proved in the DEF and CONV Notes, are

$$
q-\widetilde\gamma_8(p)=\frac{164}{2375}>0,
\qquad
\mathcal D(\phi_0)=\frac{16}{2793}\|\phi_0\|_{p+1}^{p+1}>0,
\qquad
\frac{\langle\eta_0,\phi_0\rangle}{\|\phi_0\|_2^2}
=\frac{49}{24012}>0.
$$

## Five-item audit summary

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | downstream | [Lines 682–684](../paper/paper.tex#L682), applying [Theorem 1.3](../paper/paper.tex#L672) and then Theorem 1.1(ii) | [MP — Note](#mp--note): the scaling-sign antecedent is supplied by the earlier false computation; the theorem and its consequent are preserved. |
| G1 | not_violated | none | [(1.8)–(1.9)](../paper/paper.tex#L365); [parameter corollary](../paper/paper.tex#L682) | [G1 — Note](#g1--note): a pointwise algebraic failure occurs before universal closure; no special choice is generalized beyond its restrictions. |
| G2 | not_violated | none | [(1.9)](../paper/paper.tex#L373); [§8.2](../paper/paper.tex#L4239); [Proposition 6.1](../paper/paper.tex#L3332) | [G2 — Note](#g2--note): the threshold conversion is nonexistential, and the actual witness-elimination arguments preserve their hypotheses and scopes. |
| DEF | not_violated | none | [Threshold and scaling definitions](../paper/paper.tex#L365); [canonical derivative](../paper/paper.tex#L2071); [cutoff family](../paper/paper.tex#L2928) | [DEF — Note](#def--note): the rational function and the relevant function constructions are well defined; the failed claim is their asserted scaling-sign relation. |
| CONV | violated | direct | [Line 369 and (1.9)](../paper/paper.tex#L369), repeated at [lines 682–683](../paper/paper.tex#L682) | [CONV — Note](#conv--note): energy scaling and elimination give $d(d-2)$, whereas the printed threshold encodes $(d+1)(d-2)/2$. |

## MP — Note

The rule is

$$
\frac{\Gamma\vdash A\qquad\Gamma\vdash A\to B}
     {\Gamma\vdash B}.
$$

The target fraction and (1.9) present a numerical characterization, not an explicit application to a selected object of a theorem with a different consequent. The identifiable subsequent theorem application is at [line 684](../paper/paper.tex#L684). The following is a symbolic reconstruction of that printed application, retaining its actual assumptions.

For explicit typing, write $\mathsf{GS}_{n,r,s}(f)$ for: $f$ is real, positive, centered radial and decreasing, belongs to $C^2(\mathbb R^n)\cap\dot H^1\cap L^{r+1}$, solves $-\Delta f+f^r-f^s=0$, and minimizes the associated energy among nonzero solutions in $\dot H^1\cap L^{r+1}$. Write $\mathsf{Can}_{n,r,s}(f,h)$ for: $h\in C^2_{\rm rad}(\mathbb R^n;\mathbb R)$, $( -\Delta+rf^{r-1}-sf^{s-1})h=-f$, and $h$ has the specified canonical asymptotic, namely $h\sim-|z|^2 f$ except at $(n,r)=(4,2)$, where $h\sim-1$. The integral representation and uniqueness in §4 select this object.

Theorem 1.3, with all contextual dependencies exposed, supplies the universally quantified implication

$$
\begin{aligned}
\forall n\in\mathbb N_{\ge2}\ \forall r,s\in\mathbb R\ \forall f,h:\quad
\bigl[&1<r<s<q_S(n)\ \land\mathsf{GS}_{n,r,s}(f)
\land\mathsf{Can}_{n,r,s}(f,h)\\
&\land\int_{\mathbb R^n}(1+|z|^2)f^2\,dz<\infty
\land\mathcal D_{n,r,s}(f)\le0\bigr]
\ \Longrightarrow\ \int_{\mathbb R^n}hf\,dz<0.
\end{aligned}
$$

The function variables have the types specified by $\mathsf{GS}$ and $\mathsf{Can}$; $\mathcal D_{n,r,s}$ uses exactly the energy and scaling above with $(d,p,q)=(n,r,s)$. The substitution is

$$
(n,r,s,f,h)=(d,p,q,\phi_0,\eta_0).
$$

For the weighted branch of line 684, $\Gamma_{\rm MP}$ consists of:

1. $d\in\mathbb N_{\ge2}$, $p,q\in\mathbb R$, and $1<p<q<q_S(d)$.
2. $\mathsf{GS}_{d,p,q}(\phi_0)$ and $\mathsf{Can}_{d,p,q}(\phi_0,\eta_0)$, with their defining equations, function spaces, and asymptotic convention.
3. $\int(1+|z|^2)\phi_0^2<\infty$ and $q\ge\widetilde\gamma_d(p)$.
4. The displayed definitions of $E$, $u^\lambda$, $\mathcal D$, $L_0$, and real pairing, and the available conditional statements of Theorems 1.3 and 1.1(ii).

The asserted equivalence at lines 682–683 is a proof obligation, not a valid additional background assumption. The instantiated antecedent and consequent are

$$
\begin{aligned}
A={}&[d\ge2]\land[1<p<q<q_S(d)]
\land\mathsf{GS}_{d,p,q}(\phi_0)
\land\mathsf{Can}_{d,p,q}(\phi_0,\eta_0)\\
&\land\left[\int(1+|z|^2)\phi_0^2<\infty\right]
\land[\mathcal D(\phi_0)\le0],\\
B={}&\left[\int\eta_0\phi_0<0\right].
\end{aligned}
$$

The fragment at issue is

$$
\begin{array}{c}
\Gamma_{\rm MP}\vdash q\ge\widetilde\gamma_d(p),\\
\text{lines 682–683 claim }q\ge\widetilde\gamma_d(p)
 \Longrightarrow\mathcal D(\phi_0)\le0,\\
\Gamma_{\rm MP}\vdash A\to B
 \quad\text{(Theorem 1.3)},\\
\text{line 684 claims }C_{\rm pair}=B.
\end{array}
$$

The first failed obligation in applying Theorem 1.3 is establishment of the last conjunct of $A$. The implication supplied by Theorem 1.3 is correctly instantiated, and $C_{\rm pair}$ equals its exact consequent. For the admissible eight-dimensional witness, every other conjunct holds, while
$\mathcal D(\phi_0)=16P/2793>0$, where $P=\|\phi_0\|_{p+1}^{p+1}>0$. The incorrect supply of that conjunct is precisely the preceding CONV failure.

For the final conclusion $C_{\rm inst}$ at line 684, let $\mathsf I(\phi_0)$ denote orbital instability for the stated NLS, in the manuscript's definition. Theorem 1.1(ii) instantiates to

$$
\bigl[d\ge2\land 1<p<q<q_S(d)
\land\mathsf{GS}_{d,p,q}(\phi_0)
\land\phi_0\in L^2\cap\mathcal F(H^1)
\land\mathsf{Can}_{d,p,q}(\phi_0,\eta_0)
\land\langle\eta_0,\phi_0\rangle<0\bigr]
\Longrightarrow\mathsf I(\phi_0).
$$

Here $C_{\rm inst}=\mathsf I(\phi_0)$ again equals the consequent. The missing negative pairing is inherited from the first failed application; the witness actually has pairing $49N/24012>0$, with $N=\|\phi_0\|_2^2$.

This is a **downstream MP failure of antecedent establishment**. The logical implication-elimination steps would be valid if the claimed scaling-sign premise were established. The fraction also alters the preceding description of the condition attributed to FH21, but the manuscript does not provide a separate selected-object argument there that establishes a second, independent MP defect. The certified direct error is the numerical conversion of the stated energy criterion; the later use of that result adds no direct MP label.

## G1 — Note

The rule is

$$
\frac{\Gamma\vdash A\to B(x)}
 {\Gamma\vdash A\to\forall x\,B(x)},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(A).
$$

A concrete formalization of the implicit universal claim in [equations (1.8)–(1.9)](../paper/paper.tex#L365) uses a tuple variable

$$
x=(n,r,s,u)\in
\coprod_{n\in\mathbb N_{\ge1}}
\bigl(\{n\}\times\mathbb R^2\times C^2_{\rm rad}(\mathbb R^n;\mathbb R)\bigr).
$$

The disjoint union keeps the varying spatial dimension explicit. Define the range predicate

$$
D_1(x):=
1<r<s<1+4/n\ \land
\mathsf{GS}_{n,r,s}(u)\ \land\ u\in H^1(\mathbb R^n),
$$

where $\mathsf{GS}$ has the fully expanded meaning in the MP Note. The $H^1$ condition is satisfied by the stated ground states in this mass-subcritical range; it is not a restriction to the chosen counterexample. Set

$$
A_1:=\top,
\qquad
B_1(x):=
D_1(x)\to
\left[(s>\widetilde\gamma_n(r))
\longleftrightarrow\mathcal D_{n,r,s}(u)<0\right].
$$

The background $\Gamma_1$ contains the real/Lebesgue/Sobolev definitions used above, the energy and scaling formulas as parameterized definitions, and the unchanged ground-state and stationarity results. All parameters in those schemas are bound; none is the free tuple $x$. The proposed universal closure is

$$
\Gamma_1\vdash\top\to\forall x\,
\left(D_1(x)\to
[(s>\widetilde\gamma_n(r))\leftrightarrow\mathcal D_{n,r,s}(u)<0]\right).
$$

This display reconstructs the manuscript's parameterized statement; the manuscript does not print a proof by choosing a special dimension or profile and generalizing from it. The actual local calculation available before such a closure, for an arbitrary $x$ under the open assumption $D_1(x)$, is as follows. Put

$$
T_u=\int|\nabla u|^2,\quad P_u=\int u^{r+1}>0,\quad
Q_u=\int u^{s+1},\quad a=\frac{n(r-1)}2,\quad c=\frac{n(s-1)}2.
$$

The ground-state equation and scaling stationarity give

$$
T_u+P_u-Q_u=0,\qquad
T_u+\frac a{r+1}P_u-\frac c{s+1}Q_u=0,
$$

and hence the valid pre-generalization derivation gives

$$
\Gamma_1,D_1(x)\vdash
\frac{\mathcal D_{n,r,s}(u)}{P_u}
=\frac{n(s-r)}{4(r+1)[4-(n-2)(s-1)]}
\left[16-4n(r+s-2)+n(n-2)(r-1)(s-1)\right].
$$

The printed fraction instead requires the coefficient $(n+1)(n-2)/2$. It fails already at the fixed tuple
$(8,23/19,27/19,\phi_0)$, before any universal introduction. The fully worked elimination and witness values appear in the CONV Note.

For the variable conditions, $\operatorname{FV}(A_1)=\varnothing$, and $x\notin\operatorname{FV}(\Gamma_1)$. The components $n,r,s,u$ occur freely in the temporary assumption $D_1(x)$; that entire assumption must be discharged into $B_1(x)$ before $x$ is generalized. The integration variables and scaling variable are bound, and $T_u,P_u,Q_u,a,c$ are abbreviations dependent on $x$, not surviving additional open assumptions. There is no selected-profile restriction beyond $D_1$.

The analogous wider parameter corollary has the structure

$$
\forall x\Bigl(
[n\ge2\land1<r<s<q_S(n)\land\mathsf{GS}_{n,r,s}(u)\land u\in L^2]
\to[(s\ge\widetilde\gamma_n(r))\to\mathsf I(u)]\Bigr).
$$

Its weighted branch inherits the pointwise failure explained in the MP Note. No step exchanges a special assumption for an unrestricted choice. In particular, agreement of the printed fraction with the true threshold at $n=1,2$ is a diagnostic fact, not a premise from which the manuscript generalizes to $n\ge3$. Thus the target does **not violate G1**: its false parameterized result comes from a failed calculation, with no separately demonstrated misuse of universal introduction.

## G2 — Note

The rule is

$$
\frac{\Gamma\vdash A(x)\to B}
 {\Gamma\vdash(\exists x\,A(x))\to B},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(B).
$$

The planted operation in [(1.9)](../paper/paper.tex#L373) is the comparison of two real-valued conditions,
$q>\widetilde\gamma_d(p)$ and $\mathcal D(\phi_0)<0$, for the same fixed parameters and canonical profile. No existential premise is eliminated there: the displayed $\lambda$ is the differentiation variable evaluated at $1$, not an existential witness.

There is a genuine witness choice in the relevant conditional proof [§8.1–§8.2, lines 4157–4310](../paper/paper.tex#L4157). Its formalization is useful for distinguishing the direct error from a G2 error. Fix $d,p,q,\phi_0,\eta_0$ as above, with $d\ge2$, energy-subcritical exponents, $\phi_0\in\mathcal F(H^1)$, and the **actual Theorem 1.3 hypothesis** $\mathcal D(\phi_0)\le0$. Define

$$
\begin{aligned}
\mathscr X&=\{v\in\dot H^1_{\rm rad}(\mathbb R^d;\mathbb R):
\phi_0^{(p-1)/2}v\in L^2\},\\
Q_0(v,w)&=\int(\nabla v\cdot\nabla w+
(p\phi_0^{p-1}-q\phi_0^{q-1})vw),\\
\psi&=(z\cdot\nabla+d/2)\phi_0.
\end{aligned}
$$

The background $\Gamma_2$ consists of these fixed objects and definitions; their equations $L_0\eta_0=-\phi_0$, $\psi,\eta_0\in\mathscr X$, $\psi\ne0$, $Q_0(\psi,\psi)=\mathcal D(\phi_0)\le0$, and $\langle\phi_0,\psi\rangle=0$; the decay statements $\psi=O(\phi_0)$, $\eta_0\sim-r^2\phi_0$; the unique simple negative eigenvalue $e_0<0$ of $(L_0)_{\rm rad}$; and Lemma 8.1 in its eigenfunction-parameterized form. The latter says that for any nonzero real radial eigenfunction for $e_0$, a nonzero vector in $\mathscr X$ orthogonal to it has strictly positive $Q_0$. These are the unchanged hypotheses and statements used by the printed proof.

The witness variable is $x=\chi$, with domain $H^2_{\rm rad}(\mathbb R^d;\mathbb R)$. Define

$$
A_2(\chi):=(\chi\ne0)\land(L_0\chi=e_0\chi),
\qquad
B_2:=\langle\eta_0,\phi_0\rangle<0.
$$

The existential premise supplies exactly a nonzero real radial eigenfunction for the fixed negative eigenvalue. It supplies neither a normalization nor a sign for $\langle\eta_0,\chi\rangle$, and the proof uses neither. With a fresh witness $\widehat\chi$, the elimination subderivation is

$$
\begin{array}{ll}
1.&[A_2(\widehat\chi)]\quad\text{local witness assumption};\\
2.&\langle\psi,\widehat\chi\rangle\ne0:
\text{ otherwise Lemma 8.1 gives }Q_0(\psi,\psi)>0;\\
3.&\displaystyle\beta_{\widehat\chi}:=
-\frac{\langle\eta_0,\widehat\chi\rangle}
 {\langle\psi,\widehat\chi\rangle},\qquad
w_{\widehat\chi}:=\eta_0+\beta_{\widehat\chi}\psi;\\
4.&\langle w_{\widehat\chi},\widehat\chi\rangle=0,
\quad w_{\widehat\chi}\ne0
\quad\text{by the two distinct decay orders};\\
5.&0<Q_0(w_{\widehat\chi},w_{\widehat\chi})
=-\langle\phi_0,\eta_0\rangle
+\beta_{\widehat\chi}^{2}\mathcal D(\phi_0);\\
6.&\langle\phi_0,\eta_0\rangle
<\beta_{\widehat\chi}^{2}\mathcal D(\phi_0)\le0,
\quad\text{hence }B_2.
\end{array}
$$

Only $\beta_{\widehat\chi}$ and $w_{\widehat\chi}$ depend on the chosen eigenfunction. Both remain inside its scope; the last sign inference eliminates this dependence. Discharging $A_2(\widehat\chi)$, and then eliminating the existential premise, yields

$$
\Gamma_2\vdash A_2(\chi)\to B_2,
\qquad
\Gamma_2\vdash(\exists\chi\in H^2_{\rm rad}(\mathbb R^d;\mathbb R)
\ A_2(\chi))\to B_2.
$$

The fresh name $\widehat\chi$ is absent from the remaining assumptions, the existential premise, and $B_2$. The fixed parameters $d,p,q,\phi_0,\eta_0,e_0$ may remain free; they are not the eliminated witness. Thus both the conditional derivation and the G2 variable condition hold. The eight-dimensional counterexample fails the already printed hypothesis $\mathcal D(\phi_0)\le0$, precisely at the earlier conversion; the proof just formalized retains that hypothesis.

The later instability argument has a second, equally explicit existential structure. In [Proposition 6.1 and its application, lines 3332–3341 and 3466–3475](../paper/paper.tex#L3332), fix the admissible $d,p,q,\phi_0\in H^1$, its stationary equation and Nehari characterization, the NLS flow, and the energy and $Q_0$ definitions as $\Gamma_3$. Put

$$
A_3(h):=
h\in H^1_{\rm rad}(\mathbb R^d;\mathbb R)
\land\langle h,\phi_0\rangle=0
\land Q_0(h,h)<0,
\qquad B_3:=\mathsf I(\phi_0).
$$

For fresh $h$, the proof outline derives $B_3$ under $[A_3(h)]$. Its Lyapunov functional $A_h(v)=(e^{i\theta(v)}v,ih)_{L^2}$, vector field $a_h=-iA_h'$, $\mathcal P_h(v)=\langle E'(v),a_h(v)\rangle$, implicit correction $\Lambda_h(v)$, neighborhood size, and perturbations $u_{0,\lambda,h}=\phi_0+\lambda h$ are all allowed to depend on $h$ within this scope. The exported instability statement concerns the fixed $\phi_0$ and asserts the existence of an instability neighborhood and arbitrarily close escaping data; none of those witness names is free in $B_3$. Consequently

$$
\frac{\Gamma_3,[A_3(h)]\vdash\mathsf I(\phi_0)}
 {\Gamma_3\vdash(\exists h\,A_3(h))\to\mathsf I(\phi_0)}
$$

is valid existential elimination. The actual quantifier order is parameterwise existence of a direction, $\forall(d,p,q)\,[\text{criterion}\to\exists h\,A_3(h)]$, not a single direction chosen before all parameters. The planted threshold supplies a false negative-pairing premise to the direction construction; it does not cause an existential witness to escape its scope or confer an additional unproved property on an otherwise sufficient witness. The G2 finding is **not_violated**.

## DEF — Note

The changed definition is an ordinary rational function. For each fixed $d\in\mathbb N_{\ge1}$, its relevant domain is $1<p<q_S(d)$ and its codomain is $\mathbb R$. Put

$$
x=p-1,\qquad C_d=\frac{(d+1)(d-2)}2.
$$

Its printed denominator is exactly

$$
d^2+7d-2-(d+1)(d-2)p
=2(4d-C_dx).
$$

For $d=1$ this equals $2(p+3)>0$; for $d=2$ it equals $16$. For $d\ge3$, $0<x<4/(d-2)$ gives

$$
4d-C_dx>4d-2(d+1)=2(d-1)>0.
$$

Thus every admissible input gives one finite real value. There is no representative choice, recursive prescription, or existence/uniqueness problem. The subsequent claim that this function is the sign threshold of $\mathcal D$ is the failed assertion. The definition itself specifies the fraction explicitly, rather than specifying an object by the requirement that it solve the sign-characterization problem.

The other object introduced in [(1.9)](../paper/paper.tex#L378) is the map

$$
(0,\infty)\times H^1(\mathbb R^d)\longrightarrow H^1(\mathbb R^d),
\qquad (\lambda,u)\longmapsto u^\lambda,
\qquad u^\lambda(z)=\lambda^{d/2}u(\lambda z).
$$

It preserves almost-everywhere equality, since invertible dilation takes null sets to null sets. Its norm identities are $\|u^\lambda\|_2^2=\|u\|_2^2$ and $\|\nabla u^\lambda\|_2^2=\lambda^2\|\nabla u\|_2^2$. The energy $E:H^1\to\mathbb R$ is finite in the stated energy-subcritical range by the usual Sobolev embeddings. On $X_0=\dot H^1\cap L^{p+1}$, the same expression is finite by interpolation with the Sobolev exponent (and the corresponding low-dimensional interpolation); the present witness lies in $H^1$. The explicit powers of $\lambda$ derived in the CONV Note make $\mathcal D(\phi_0)$ an ordinary second derivative of a finite scalar expression.

For the actual admissible witness, define

$$
k=\frac{19}{4},\quad A_0=\left(\frac{23}{7}\right)^{19/4},
\quad b=\frac{92}{931}>0,\quad t=1+br^2,\quad
u(r)=A_0t^{-k},\qquad r=|z|.
$$

This is a smooth positive real function on $\mathbb R^8$, with $u'(0)=0$, $u'(r)=-2bkA_0r\,t^{-k-1}<0$ for $r>0$, and $u(r)\to0$. Direct differentiation gives

$$
\begin{aligned}
(t^{-m})'&=-2bmr\,t^{-m-1},\\
(t^{-m})''&=-2bm\,t^{-m-1}+4b^2m(m+1)r^2t^{-m-2},\\
\Delta(t^{-m})&=
b[4m(m+1)-2dm]t^{-m-1}
-4bm(m+1)t^{-m-2}.
\end{aligned}
$$

With $p=23/19$, $q=27/19$, one has

$$
kp=k+1,\quad kq=k+2,\quad
b[4k(k+1)-2dk]=\frac{23}{7}=A_0^{p-1},\quad
4bk(k+1)=\frac{529}{49}=A_0^{q-1}.
$$

Consequently the two coefficients in

$$
-\Delta u+u^p-u^q
=A_0\bigl[-b(4k(k+1)-2dk)+A_0^{p-1}\bigr]t^{-k-1}
+A_0\bigl[4bk(k+1)-A_0^{q-1}\bigr]t^{-k-2}
$$

are zero. The parameters satisfy

$$
1<\frac{23}{19}<\frac{27}{19}<\frac32=p_{\rm c}(8)<\frac53=q_S(8),
\qquad
\frac{23}{19}<\frac43=p^*(8)<\frac75=p_{\rm w}(8).
$$

The [positive radial solution uniqueness in Theorem A.1](../paper/paper.tex#L4412), together with the existing ground state, identifies $u=\phi_0$. This uses the actual boundary-value problem, not an arbitrary choice among nonlinear solutions. At infinity, $u$ has order $r^{-19/2}$. The radial integrands for $u^2$, $|\nabla u|^2$, and $r^2u^2$ have powers $-12,-14,-10$, respectively, after multiplication by $r^7$; the $u^{p+1}$ and $u^{q+1}$ integrands have powers $-14,-16$. All converge, establishing $\phi_0\in X_0\cap H^1\cap\mathcal F(H^1)$.

The canonical object $\eta_0$ is defined at [lines 2071–2089](../paper/paper.tex#L2071) by

$$
\eta_0(r)=\frac{v_0^+(r)}{W_0}
\int_r^\infty w_0^-(s)\phi_0(s)s^{d-1}\,ds
+\frac{w_0^-(r)}{W_0}
\int_0^r v_0^+(s)\phi_0(s)s^{d-1}\,ds,
$$

with the continuous origin value
$\eta_0(0)=W_0^{-1}\int_0^\infty w_0^-\phi_0s^{d-1}\,ds$.
Here $v_0^+$ is the regular homogeneous solution normalized by $v_0^+(0)=1$, $(v_0^+)'(0)=0$; $w_0^-$ is the decaying homogeneous solution; and
$W_0=r^{d-1}[v_0^+(w_0^-)'-(v_0^+)'w_0^-]>0$.
Lemma 4.3 supplies the improper-integral convergence. Rescaling $w_0^-$ multiplies $W_0$ by the same factor, leaving the formula unchanged. Proposition 4.5 gives its $C^2_{\rm rad}(\mathbb R^d;\mathbb R)$ regularity and uniqueness with the prescribed asymptotic.

For the witness, a concrete candidate is

$$
v(r)=-\frac{A_0}{29b}
\left(t^{-15/4}+12t^{-19/4}-24t^{-23/4}\right).
$$

The radial calculation above gives

$$
L_0(t^{-m})=bC_mt^{-m-1}+bD_mt^{-m-2},
\quad
C_m=2dm-4m(m+1)+pA_0^{p-1}/b,
\quad D_m=4m(m+1)-qA_0^{q-1}/b.
$$

| $m$ | $C_m$ | $D_m$ |
|---|---:|---:|
| $15/4$ | $29$ | $-84$ |
| $19/4$ | $7$ | $-46$ |
| $23/4$ | $-23$ | $0$ |

Thus $-84+12\cdot7=0$ and $12(-46)-24(-23)=0$, leaving $L_0v=-A_0t^{-19/4}=-\phi_0$. The candidate is smooth and radial at the origin, and

$$
\frac{v(r)}{-r^2\phi_0(r)}
=\frac{t+12-24/t}{29br^2}\longrightarrow\frac1{29}>0.
$$

It therefore satisfies the canonical asymptotic with the manuscript's exact convention, and Proposition 4.5 gives $v=\eta_0$. Theorem 4.8 further identifies this same object as the local zero-frequency limit of $\partial_\omega\phi_\omega$. Its decay is $r^{-15/2}$; radial integrands for $\eta_0^2$, $|\nabla\eta_0|^2$, $|\eta_0\phi_0|$, and $\phi_0^{p-1}\eta_0^2$ have powers $-8,-10,-10,-10$. This verifies $\eta_0\in H^1\cap\mathscr X$ and convergence of the actual pairing.

Finally, [the §5 cutoff definition](../paper/paper.tex#L2928) is

$$
\varphi_R(z)=\varphi(z/R),\quad
I_R=\langle\varphi_R\eta_0,\phi_0\rangle,\quad
\beta_R=-N/I_R,\quad
\psi_R=\phi_0+\beta_R\varphi_R\eta_0,
\quad N=\|\phi_0\|_2^2,
$$

where $R>0$, $\varphi\in C_c^\infty$ is radial, equals one on the unit ball, vanishes outside the radius-two ball, and lies between zero and one. The defining condition is explicitly $I_R\ne0$. In the witness, $I_R\to49N/24012>0$, so the denominator is nonzero for every sufficiently large $R$. Then $\psi_R\in H^1_{\rm rad}$ and
$\langle\psi_R,\phi_0\rangle=N-(N/I_R)I_R=0$.
Its positive limiting quadratic form, computed below, concerns the later negativity assertion; it is not a failure to define $\psi_R$. Similarly, the $\beta$ in §8.2 has a nonzero denominator under that theorem's actual hypothesis, as shown in the G2 Note. These concrete checks give **DEF not_violated**.

## CONV — Note

The exact claimed endpoint is [(1.9)](../paper/paper.tex#L373), with the fraction from [line 369](../paper/paper.tex#L369); the manuscript explicitly calls the repeat at [lines 682–683](../paper/paper.tex#L682) “the same computation.” The following reconstructs that computation from the printed energy and scaling. The intermediate sign polynomials are review notation, not additional displayed equations attributed to the manuscript.

Put

$$
T=\|\nabla\phi_0\|_2^2,\quad P=\|\phi_0\|_{p+1}^{p+1}>0,
\quad Q=\|\phi_0\|_{q+1}^{q+1},\quad N=\|\phi_0\|_2^2,
\quad x=p-1,\quad y=q-1,\quad a=dx/2,\quad c=dy/2.
$$

For any power $s>0$ whose integral is finite, substitution $w=\lambda z$, with $dz=\lambda^{-d}dw$, gives

$$
\int|\phi_0^\lambda(z)|^s\,dz
=\lambda^{ds/2-d}\int|\phi_0(w)|^s\,dw.
$$

Also $\nabla\phi_0^\lambda(z)=\lambda^{d/2+1}\nabla\phi_0(\lambda z)$. Therefore the exact starting energy expands to

$$
E(\phi_0^\lambda)
=\tfrac12\lambda^2T+\frac{\lambda^a}{p+1}P
-\frac{\lambda^c}{q+1}Q,
$$

and two scalar derivatives give

$$
\begin{aligned}
\left.\partial_\lambda E(\phi_0^\lambda)\right|_1
&=T+\frac a{p+1}P-\frac c{q+1}Q=0,\\
\mathcal D(\phi_0)
&=T+\frac{a(a-1)}{p+1}P-\frac{c(c-1)}{q+1}Q.
\end{aligned}
$$

The zero first derivative uses stationarity of the ground state. Testing the stationary equation against $\phi_0$ also gives the Nehari identity
$T+P-Q=0$. These are the unchanged stationary identities, not consequences of the altered threshold. For the explicit witness, all integration by parts and differentiations are justified by the decay checked above and are additionally confirmed by direct integrals below.

Subtracting the two first-order identities yields

$$
\left(1-\frac a{p+1}\right)P
=\left(1-\frac c{q+1}\right)Q,
\qquad
\frac QP=\frac{q+1}{p+1}
\frac{4-(d-2)x}{4-(d-2)y}.
$$

Eliminate $T$ from the second derivative using scaling stationarity, and then substitute this ratio:

$$
\begin{aligned}
\frac{\mathcal D(\phi_0)}P
&=\frac{a(a-2)}{p+1}-\frac{c(c-2)}{q+1}\frac QP\\
&=\frac{d}{4(p+1)[4-(d-2)y]}
\bigl[x(dx-4)(4-(d-2)y)
-y(dy-4)(4-(d-2)x)\bigr].
\end{aligned}
$$

The full numerator reduction is

$$
\begin{aligned}
&x(dx-4)(4-(d-2)y)-y(dy-4)(4-(d-2)x)\\
&\quad=4d(x^2-y^2)-16(x-y)-d(d-2)xy(x-y)\\
&\quad=(y-x)[16-4d(x+y)+d(d-2)xy].
\end{aligned}
$$

Hence

$$
\boxed{\frac{\mathcal D(\phi_0)}P
=\frac{d(q-p)}{4(p+1)[4-(d-2)(q-1)]}
F_d(p-1,q-1)},
\qquad
F_d(x,y)=16-4d(x+y)+d(d-2)xy.
$$

The prefactor is strictly positive: $d>0$, $q-p>0$, $p+1>0$, and the last bracket is positive under energy subcriticality (also directly for $d=1,2$). Likewise $4d-d(d-2)x>0$. Solving $F_d(x,y)<0$ gives

$$
\begin{aligned}
\mathcal D(\phi_0)<0
&\iff y>\frac{16-4dx}{4d-d(d-2)x}\\
&\iff q>\gamma^{\rm true}_d(p),\\
\gamma^{\rm true}_d(p)
&=1+\frac{16-4d(p-1)}{4d-d(d-2)(p-1)}
=\frac{16+d^2+6d-pd(d+2)}{d[d+2-(d-2)p]}.
\end{aligned}
$$

The same positive denominators give the corresponding non-strict equivalence with $\le0$ and $\ge$. In contrast, expanding the printed fraction itself gives

$$
\widetilde\gamma_d(p)
=1+\frac{16-4dx}{4d-C_dx},\qquad
C_d=\frac{(d+1)(d-2)}2,
$$

so it is the zero curve of

$$
\widetilde F_d(x,y)=16-4d(x+y)+C_dxy,
\qquad
F_d(x,y)-\widetilde F_d(x,y)
=\frac{(d-1)(d-2)}2xy.
$$

The first incorrect **printed** transformation is the equivalence (1.9): it identifies the sign condition for $F_d$ with the condition for $\widetilde F_d$. Describing this as the replacement $d(d-2)\mapsto(d+1)(d-2)/2$ is an algebraically exact reconstruction of the mismatch, not a claim that the manuscript prints that intermediate replacement. It is a computation error under unchanged definitions, not a change to the energy, the scaling, or the stationary equation.

For the concrete witness,

$$
\begin{gathered}
x=4/19,\quad y=8/19,\quad a=16/19,\quad c=32/19,\\
\widetilde\gamma_8(23/19)=169/125,
\qquad\gamma^{\rm true}_8(23/19)=37/26,\\
q-\widetilde\gamma_8(p)=164/2375>0,
\qquad q-\gamma^{\rm true}_8(p)=-1/494<0,\\
F_8(4/19,8/19)=16/361,
\qquad\widetilde F_8(4/19,8/19)=-656/361.
\end{gathered}
$$

The positive prefactor is $19/147$, so the actual value is

$$
\boxed{\mathcal D(\phi_0)/P=16/2793>0}.
$$

For an independent check without eliminating the stationary identities, set

$$
J_s:=\int_0^\infty z^3(1+z)^{-s}\,dz
=\frac6{(s-1)(s-2)(s-3)(s-4)},\qquad s>4.
$$

The last expression follows by substituting $v=(1+z)^{-1}$ and integrating
$(1-v)^3v^{s-5}$ on $(0,1)$. With the actual profile $\phi_0=A_0(1+br^2)^{-19/4}$, radial measure $|\mathbb S^7|r^7dr$, and $z=br^2$, one obtains

$$
\begin{aligned}
N&=\frac{|\mathbb S^7|A_0^2}{2b^4}J_{19/2},\\
P/N&=\frac{23}{7}\frac{J_{21/2}}{J_{19/2}}=\frac{253}{133},\\
Q/N&=\frac{529}{49}\frac{J_{23/2}}{J_{19/2}},\\
T/N&=4bk^2\frac{J_{21/2}-J_{23/2}}{J_{19/2}}.
\end{aligned}
$$

Thus $T/P=152/147$ and $Q/P=299/147$; substitution into the uneliminated derivative gives

$$
\begin{aligned}
\mathcal D(\phi_0)/P
&=\frac{152}{147}
+\frac{(16/19)(-3/19)}{42/19}
-\frac{(32/19)(13/19)}{46/19}\frac{299}{147}\\
&=\frac{16}{2793}.
\end{aligned}
$$

The same integrals also independently verify the claimed downstream obstruction for the **canonical** $\eta_0$ identified in the DEF Note:

$$
\begin{aligned}
\frac{\langle\eta_0,\phi_0\rangle}{N}
&=-\frac1{29b}
\frac{J_{17/2}+12J_{19/2}-24J_{21/2}}{J_{19/2}}\\
&=-\frac1{29b}\left(\frac{17}{9}+12-24\frac{11}{19}\right)
=\frac1{29b\,171}
=\boxed{\frac{49}{24012}>0}.
\end{aligned}
$$

Finally, since $\eta_0\in H^1$, the cutoffs converge in $H^1$ and $\psi_R\to\phi_0-(N/I)\eta_0$, where $I=\langle\eta_0,\phi_0\rangle\ne0$. Using $L_0\eta_0=-\phi_0$, the limit of the printed quadratic-form expansion is

$$
\begin{aligned}
\lim_{R\to\infty}Q_0(\psi_R,\psi_R)
&=Q_0(\phi_0,\phi_0)
-\frac{2N}{I}\langle L_0\eta_0,\phi_0\rangle
+\frac{N^2}{I^2}\langle L_0\eta_0,\eta_0\rangle\\
&=Q_0(\phi_0,\phi_0)+\frac{N^2}{I},\\
\frac1N\lim_{R\to\infty}Q_0(\psi_R,\psi_R)
&=\frac{P}{N}\left[(p-1)-(q-1)\frac QP\right]+\frac NI\\
&=\frac{253}{133}
\left[\frac4{19}-\frac8{19}\frac{299}{147}\right]
+\frac{24012}{49}
=\boxed{\frac{181578560}{371469}>0}.
\end{aligned}
$$

The §5 expansion itself is correct. These last two calculations diagnose the propagation of the wrong threshold into the pairing and direction criteria. They are not additional direct CONV errors in §5 or §8. The direct CONV violation is already established by expanding the energy and obtaining the wrong threshold in (1.9). Exact independent checks confirm the polynomial identity, radial equations, normalized integrals, and all displayed witness values.

## Final direct labels

**CONV.** This agrees with the existing direct label in the [case README](../README.md); no label is added or removed. The audit adds an explicit distinction between the direct scaling computation error and the downstream MP applications that lack its falsely supplied sign premise. G1, G2, and DEF have no demonstrated direct violations at this target.

The verified witness is the actual ground state at $(d,p,q)=(8,23/19,27/19)$, together with its uniquely specified canonical $\eta_0$. It satisfies the mass-subcritical, energy-subcritical, and weighted assumptions, lies strictly above the printed threshold, and has strictly positive scaling second derivative and strictly positive pairing. The conditional Theorem 1.3 retains the actual scaling-sign hypothesis throughout its proof. No unresolved mathematical issue remains for this classification or its witness.
