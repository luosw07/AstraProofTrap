# 014: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow, informed by the source and existing construction/checker materials, rather than an original workflow report or blind reviewer run. The review uses the complete modified manuscript, the original and [mutation](../mutation.diff), the [tricker report](tricker_report.md), all three [existing](checker_report.md) [checker](checker_report_02.md) [reports](checker_report_03.md), the [checker calculation](checker_calculation.py), the [case README](../README.md), and the [classification standard](../../../protocol/classification.md). The two manuscript sources differ only by the recorded replacement.

## Exact target and actual assumptions

The target is the direction-enclosure construction in “Values at the vertices,” [line 2315](../paper/paper.tex#L2315). The [original](../original/paper.tex#L2315) takes “the arc of directions that they span”; the modification takes “the shortest closed arc of $\mathbb P(T)$ containing their directions.” The preceding signed-vector and positive-combination assertions are unchanged. The new arc is used as an enclosure, not merely introduced as an unrelated geometric set: the paragraph calls its outputs “resulting enclosures,” [line 2305](../paper/paper.tex#L2305) selects test-function cells from the image enclosure, and [cases (b) and (c)](../paper/paper.tex#L2251) require sets containing all relevant images.

Here is the notation used below, with the manuscript's domains preserved:

$$
\begin{gathered}
\mathbf1=(1,1,1),\qquad
T=\{v\in\mathbb R^3:\mathbf1^*v=0\},\qquad
\mathcal T=\{x\in\mathbb R^3:\mathbf1^*x=1,\ 0\le x_i\le\tfrac12,\ i=1,2,3\},\\
C_i=\{x\in\mathcal T:x_i\le\tfrac14\},\qquad
\mathbb P(T)=(T\setminus\{0\})/\mathbb R^*,\qquad
\langle a\rangle=a/(\mathbf1^*a),\\
\psi_j^k(x)=\frac{x+kx_j(\mathbf1-e_j)}{1+2kx_j}.
\end{gathered}
$$

The matrices $A_j=\mathrm{id}+(\mathbf1-e_j)e_j^*$ generate the manuscript's semigroup $\Gamma_{\mathcal N}$; $s_A(\Gamma_{\mathcal N})$ denotes its affinity exponent and $\mathcal N$ its gasket. The projective line consists of **unoriented** directions ([line 1673](../paper/paper.tex#L1673)). A run starts at $x\in C_i$, uses $j\ne i$, and has integer length $k\ge1$. Consequently $x_j\ge1/4$ by [Lemma `lem:trap`](../paper/paper.tex#L1978). Its input direction ranges over the entire $\mathbb P(T)$ in [Proposition `cor:certA`](../paper/paper.tex#L2084). For a nonzero representative $w\in T$, [Lemma `lem:contraction`](../paper/paper.tex#L2000) and [lines 2301–2305](../paper/paper.tex#L2301) define

$$
\begin{gathered}
u=2x_j,\quad d_k=1+ku,\quad
c=\frac{\langle\mathbf1-e_j\rangle-x}{x_j},\quad
p_w=w+w_jc,\quad \alpha_w=w_jc,\\
V_k(x)w=d_k^2D_x\psi_j^k(w)=d_kp_w-w_jc,\qquad
U(x)w=up_w,\\
V_k(x)w=V_K(x)w+(k-K)U(x)w\quad(k\ge K).
\end{gathered}
$$

The endpoint vectors are enclosed in closed coordinate rectangles using the linear isomorphism

$$
\Xi:T\longrightarrow\mathbb R^2,\qquad
\Xi(v)=(\xi,\eta)=(3v_1,v_2-v_3).
$$

The manuscript's [direction coordinate](../paper/paper.tex#L2169) is

$$
\vartheta([v])=
\begin{cases}
1+\eta/\xi,&|\eta|\le|\xi|,\\
3-\xi/\eta,&|\eta|>|\xi|,
\end{cases}
\pmod4.
$$

The tail begins at $K=2^{28}+1$ in the point evaluation. The witness below works for every fixed integer $K\ge1$, including that value. The derivative weights use $\hat w=w/|w|$, so normalization imposes no restriction on $[w]$. Symmetry reduction applies the transposition $\tau_j$ of coordinates $1,j$ to both the base image and the derivative image ([Lemma `lem:sym`](../paper/paper.tex#L2139), [line 2246](../paper/paper.tex#L2246)). The same grouped-run enclosure is reused on prisms and boxes at [lines 2332–2336](../paper/paper.tex#L2332).

The complete manuscript supplies no acute-angle condition on the signed endpoint vectors. Its derivative norm bounds control lengths, and [Remark `rem:fan`](../paper/paper.tex#L2278) explicitly discusses the nearby repelling kernel directions. The later storage coordinate $y=\mathbf1-2x$ has tangent linear part $-2\,\mathrm{id}$ ([line 2389](../paper/paper.tex#L2389)); it preserves the projective directions and the signed-cone issue.

## Five-item audit

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | downstream | [2251–2256](../paper/paper.tex#L2251), [2305](../paper/paper.tex#L2305), [2394–2395](../paper/paper.tex#L2394) | [MP — Note](#mp--note): the derivative lemma is correctly applied; the later certificate application inherits an unestablished enclosure antecedent. |
| G1 | violated | direct | [2315](../paper/paper.tex#L2315) | [G1 — Note](#g1--note): corner membership is extended to all run directions without a valid derivation for that range. |
| G2 | not_violated | none | [2123](../paper/paper.tex#L2123), [2315](../paper/paper.tex#L2315) | [G2 — Note](#g2--note): the actual test-function sufficiency argument preserves its witness properties and scope. |
| DEF | violated | direct | [2315](../paper/paper.tex#L2315), with the construction requirements at [2251–2256](../paper/paper.tex#L2251) | [DEF — Note](#def--note): the prescribed output fails its defining enclosure requirement, although its shortest arc exists uniquely in the witness. |
| CONV | not_violated | diagnostic | [2301–2315](../paper/paper.tex#L2301), [2169–2173](../paper/paper.tex#L2169) | [CONV — Note](#conv--note): differentiation, affine dependence, normalization, and direction conversion all give the stated vectors; the false step is the geometric inclusion. |

## MP — Note

**Status: violated; role: downstream.** There is no separate direct MP defect at the replacement. The exact rule is

$$
\frac{\Gamma\vdash A\qquad\Gamma\vdash A\to B}{\Gamma\vdash B}.
$$

**The genuine local theorem application.** At [line 2301](../paper/paper.tex#L2301), “By (eq:DR)” applies the derivative formula of [Lemma `lem:contraction`](../paper/paper.tex#L2000). Let $\Gamma_D$ consist of: real Euclidean vector calculus; the definitions of $T,\mathcal T,C_i,\psi_j^k$ above; the stated derivative lemma; and fixed parameters $i,j\in\{1,2,3\}$, $i\ne j$, $x\in C_i$, $k\in\mathbb Z_{\ge1}$ and $w\in T\setminus\{0\}$. The substitution into the universally quantified lemma is exactly $(j,k,x,v)=(j,k,x,w)$, with $u=2x_j$, $d=d_k$ and $c=(\langle\mathbf1-e_j\rangle-x)/x_j$. Its instantiated antecedent and relevant consequent are

$$
\begin{aligned}
A_D={}&j\in\{1,2,3\}\ \land\ k\in\mathbb Z_{\ge1}
\ \land\ x\in\mathcal T\ \land\ x_j>0\ \land\ w\in T,\\
B_D={}&D_x\psi_j^k(w)
=d_k^{-1}\left(w+\frac{ku}{d_k}w_jc\right).
\end{aligned}
$$

Every component of $A_D$ follows from $\Gamma_D$, including $x_j\ge1/4>0$. Thus

$$
\Gamma_D\vdash A_D,\qquad
\Gamma_D\vdash A_D\to B_D,\qquad
\Gamma_D\vdash B_D.
$$

Multiplying by $d_k^2$ and using $ku=d_k-1$ produces the manuscript's actual local conclusion

$$
C_D:\quad V_k(x)w=d_kp_w-w_jc.
$$

The calculation in the CONV Note verifies this last conversion. No hypothesis or qualification is lost in this application.

The replacement itself performs the set construction

$$
S=\operatorname{Short}\{[\Xi^{-1}b]:b\text{ is an endpoint-box corner}\}
$$

under a half-plane test, then treats $S$ as containing all the corresponding run directions. It neither cites nor states a previously established implication that positive combinations belong to this *shortest* arc. The actual available geometric conclusion is membership in the projectivized positive cone of the signed corners. Declaring the false shortest-arc inclusion to be an extra theorem would manufacture an MP application; the direct obligations here are the generalization and the enclosure construction audited below.

**The downstream theorem application.** [Line 2394](../paper/paper.tex#L2394) invokes [Proposition `prop:P1`](../paper/paper.tex#L2220) at $(\kappa,h_1)=(\kappa_-,h^-)$ and $(\kappa_+,h^+)$, with upper comparison constant $\theta=0.99999999$. Define $\Gamma_P$ to contain the state spaces, the operator and mesh definitions, the stated proposition, the named candidate functions $h^\pm$, the exact binary64 parameters specified at [line 2362](../paper/paper.tex#L2362), and [Corollary `cor: dimB`](../paper/paper.tex#L1914), which identifies the two dimensions with $s_A(\Gamma_{\mathcal N})$. No successful enclosure assertion is assumed in this context.

For each sign $\sigma\in\{-,+\}$, the instantiated antecedent $A_P^\sigma$ has the following components:

1. $0<\kappa_\sigma<1$; $h^\sigma:C_1\times\mathbb P(T)\to\mathbb R$ is continuous, positive, $\tau_{23}$-invariant and separately affine in base and angular coordinates on every cell of a mesh with the specified symmetries. For $\sigma=+$, $0<\theta<1$.
2. Each cell $\gamma=Q_{mn}^{\pm}\times\Theta_t$ with $m\le n$ has a finite covering family $\mathscr Q_\gamma$. Each member $Q$ is either $\gamma$ itself or a coordinate box contained in $R_\gamma\times\Theta_t$. The extension of the operator to the square in the base coordinates is used where necessary.
3. For every such $Q$, there are the asserted functions and bounds, allowed to depend on $\gamma,Q,\sigma$, satisfying **the exact identity**

$$
\widetilde{\mathcal K}_{\kappa_\sigma}h^\sigma=F_S+F_K+F_R\quad\hbox{on }Q.
$$

Here $F_S\in C^1(Q)$ has Lipschitz gradient and $D^2F_S(y)\in[H]$ almost everywhere; for every $p,q\in Q$,

$$
F_K(q)-F_K(p)\in\sum_{r=1}^3[G_r^-,G_r^+](q_r-p_r);
\qquad \sup_QF_R-\inf_QF_R\le o.
$$

Writing $\Delta_r$ for the coordinate widths of $Q$, these bounds define

$$
\begin{gathered}
A_Q^\pm=\frac18\left(\sum_r(H_{rr}^\pm)_\pm\Delta_r^2
+2\sum_{r<s}\max(|H_{rs}^-|,|H_{rs}^+|)\Delta_r\Delta_s\right),\\
E_Q=\frac12\sum_r(G_r^+-G_r^-)\Delta_r,\qquad
L_Q^\pm=A_Q^\pm+E_Q+o,
\end{gathered}
$$

where $a_+=\max(a,0)$ and $a_-=\max(-a,0)$.

4. At **every** vertex $v$ of every such $Q$, the true operator value satisfies

$$
\begin{cases}
(\widetilde{\mathcal K}_{\kappa_-}h^-)(v)-h^-_\gamma(v)\ge L_Q^+,&\sigma=-,\\
(\widetilde{\mathcal K}_{\kappa_+}h^+)(v)-\theta h^+_\gamma(v)\le-L_Q^-,&\sigma=+.
\end{cases}
$$

With these full antecedents, the proposition supplies the valid implications

$$
A_P^-\to B_P^-,\quad B_P^-:\ s_A(\Gamma_{\mathcal N})\ge2-\kappa_-;
\qquad
A_P^+\to B_P^+,\quad B_P^+:\ s_A(\Gamma_{\mathcal N})\le2-\kappa_+.
$$

The manuscript claims these same consequents, then combines them with $2-\kappa_->1.6853$, $2-\kappa_+<1.6854$ and the dimension identity to obtain the actual claimed conclusion

$$
C_P:\quad 1.6853<\dim_{\mathrm H}\mathcal N=\dim_{\mathrm B}\mathcal N=s_A(\Gamma_{\mathcal N})<1.6854.
$$

The implication and the exported consequent match. The failed obligation is **establishment of the antecedent**: a hull over selected target cells is a bound on the required values and gradients only when those cells contain the actual images. The construction at line 2315 does not establish that premise, and the admissible tent function in the DEF Note gives an explicit false factor enclosure. Consequently the method used to assert components 3 and 4 does not generally establish them. This is downstream propagation of the direct enclosure defect, and is recorded separately from the final direct labels.

## G1 — Note

**Status: violated; role: direct.** The relevant rule is

$$
\frac{\Gamma\vdash A\to B(z)}{\Gamma\vdash A\to\forall z\,B(z)},
\qquad z\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(A).
$$

The prose at [line 2315](../paper/paper.tex#L2315) expressly moves from endpoint vectors and box corners to **every** $V_k(x)w$ for all the inputs under consideration. The following is a symbolic reconstruction of that range argument, preserving its assumptions.

Fix $i\ne j$, an integer $K\ge1$, an input set $D\subset C_i\times(T\setminus\{0\})$, and two coordinate rectangles $B_0,B_\infty\subset\mathbb R^2$. For a point evaluation $D$ can be a singleton; on a check set it can be the set of pairs $(x,w(\vartheta))$ whose base points lie in $C_i$. This restriction is a subset of the manuscript's claimed range, and already contains the counterexample. The extension to off-cell base points is not needed for this witness. Write $\mathscr B$ for the finite set of signed vectors in $T$ corresponding under $\Xi^{-1}$ to all corners of these rectangles. Let $S$ be the shortest projective arc containing $\{[b]:b\in\mathscr B\}$ on the tested branch. Define

$$
\begin{aligned}
A={}&\left[\forall(y,v)\in D:\ \Xi(V_K(y)v)\in B_0\ \land\ \Xi(U(y)v)\in B_\infty\right]\\
&\land\left[\exists\ell\in(\mathbb R^2)^*\setminus\{0\}:\
\forall b\in\mathscr B,\ \ell(\Xi b)>0\right],\\
D_\mathrm{tail}(y,v,n)={}&(y,v)\in D\ \land\ n\in\mathbb Z\ \land\ n\ge K,\\
B(y,v,n)={}&D_\mathrm{tail}(y,v,n)\to[V_n(y)v]\in S.
\end{aligned}
$$

The background $\Gamma_G$ consists exactly of the real vector/projective spaces and maps defined above, the fixed parameters $i,j,K,D,B_0,B_\infty,\mathscr B,S$, the derivative identity, and the elementary fact that a point in a rectangle is a convex combination of its corners. The input set is restricted to the admissible base points and nonzero tangent representatives. No assumption that the signed endpoints are acute, or that their positive cone projects into $S$, belongs to $\Gamma_G$ or $A$.

For a fresh tuple $z=(y,v,n)\in C_i\times(T\setminus\{0\})\times\mathbb Z_{\ge1}$, the actual pre-generalization fragment under open assumptions $A$ and $D_\mathrm{tail}(z)$ is

$$
\begin{aligned}
V_n(y)v&=V_K(y)v+(n-K)U(y)v,\\
V_K(y)v&=\sum_{b\in\mathscr B}\lambda_b b,
&U(y)v&=\sum_{b\in\mathscr B}\mu_b b,\\
\lambda_b,\mu_b&\ge0,\qquad \sum_b\lambda_b=\sum_b\mu_b=1,\\
V_n(y)v&=\sum_{b\in\mathscr B}(\lambda_b+(n-K)\mu_b)b.
\end{aligned}
$$

Coefficients outside the relevant rectangle's corners are set to zero. The coefficients may depend on $(y,v)$ inside this derivation. The vector is nonzero because $D_y\psi_j^n$ is invertible. This proves

$$
[V_n(y)v]\in A_{\mathscr B},\qquad
A_{\mathscr B}:=\left\{\left[\sum_{b\in\mathscr B}a_b b\right]:
a_b\ge0,\ \sum_ba_b>0\right\}.
$$

The half-plane assumption makes every such sum nonzero and gives a specific cone arc $A_{\mathscr B}$. By construction of $S$, the argument also knows $[b]\in S$ for each corner $b$. Its first failed obligation is the passage from those facts to $[V_n(y)v]\in S$: corner membership in a shortest projective arc does not imply membership of their positive combinations. The missing inclusion is $A_{\mathscr B}\subseteq S$.

The asserted conclusion would be

$$
\Gamma_G\vdash A\to
\forall y\in C_i\ \forall v\in T\setminus\{0\}\ \forall n\in\mathbb Z_{\ge1}\,
\left(D_\mathrm{tail}(y,v,n)\to[V_n(y)v]\in S\right).
$$

All range restrictions are inside the formula. In a valid derivation the assumption $D_\mathrm{tail}(z)$ would be discharged to form $B(z)$, then $A$ would be discharged. The fresh variables $y,v,n$ do not occur free in $\Gamma_G$ or $A$; the occurrences of $y,v$ in $A$ are bound. The remaining free parameters are $i,j,K,D,B_0,B_\infty,\mathscr B,S$. Thus the eigenvariable condition is satisfied; **the conditional derivation required before generalization fails**. This locates the G1 failure in the printed extension from endpoints/corners to all run directions, rather than assigning G1 solely because a universal statement is false.

For a concrete instance, fix $K$ first and use

$$
x=(0,\tfrac12,\tfrac12),\quad i=1,\quad j=2,\quad
w_K=(4K+3,-4K-4,1).
$$

The CONV Note computes

$$
b_0=V_K(x)w_K=(K+1)(3,-4,1),\qquad
U=(-1,0,1),\qquad
S=\{\vartheta:4/9\le\vartheta\le4/3\}.
$$

The short arc is the projection of the positive cone of $b_0$ and $b_1=-U$. This pair is a **diagnostic representation of the chosen arc**, not an added manuscript hypothesis. The valid restricted implication for a vector $q\in T$ is

$$
\left[\exists a,b\ge0:\ a+b>0\ \land\ q=ab_0+bb_1\right]
\ \to\ [q]\in S.
$$

But the actual tail has

$$
V_n=b_0-(n-K)b_1.
$$

For $n>K$ its two coefficients have opposite signs. Since $b_0,b_1$ are independent, neither $V_n$ nor $-V_n$ has nonnegative coefficients in this pair. In particular $n=2K+1$ yields $\vartheta([V_n])=0\notin S$. The source establishes positivity relative to $V_K,+U$, while the shortest arc is associated with $V_K,-U$. That lost restriction explains the failed conditional derivation. The dependence $w_K=w(K)$ respects the quantified order: the cutoff is fixed, and the enclosure is then required for every admissible input direction and run length.

## G2 — Note

**Status: not_violated; role: none.** The rule is

$$
\frac{\Gamma\vdash A(f)\to B}{\Gamma\vdash(\exists f\,A(f))\to B},
\qquad f\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(B).
$$

There is a genuine existence-sufficiency argument at [line 2123](../paper/paper.tex#L2123): finding a positive bounded test function with the appropriate **pointwise operator inequality** suffices for an affinity-exponent bound. Its full instantiation is as follows. Let

$$
X=\bigsqcup_{i=1}^3(C_i\times\mathbb P(T)\times\{i\}),
$$

fix $0<\kappa<1$, and, for the upper statement, fix $0<\theta<1$. The background $\Gamma_\exists$ contains these parameters, the definition and bounded positivity of $\mathcal K_\kappa$ on bounded real functions on $X$, the definition of $s_A(\Gamma_{\mathcal N})$, and [Proposition `cor:certA`](../paper/paper.tex#L2084). The witness variable $f$ ranges over functions $X\to\mathbb R$. Define

$$
\begin{aligned}
P(f)={}&\exists m,M\in\mathbb R:\ 0<m\le M\ \land\
\forall z\in X\ (m\le f(z)\le M),\\
A_-(f)={}&P(f)\ \land\ \forall z\in X\ ((\mathcal K_\kappa f)(z)\ge f(z)),\\
A_+(f)={}&P(f)\ \land\ \forall z\in X\ ((\mathcal K_\kappa f)(z)\le\theta f(z)),\\
B_-={}&s_A(\Gamma_{\mathcal N})\ge2-\kappa,\qquad
B_+=s_A(\Gamma_{\mathcal N})\le2-\kappa.
\end{aligned}
$$

For either sign, the existential-elimination subderivation has this explicit scope:

$$
\begin{array}{ll}
1.&[\exists f\,A_\sigma(f)]^{e}\\
2.&\quad[A_\sigma(f_0)]^{a}\quad(f_0:X\to\mathbb R\text{ fresh})\\
3.&\quad\quad[0<m_0\le M_0\ \land\ \forall z\in X\ (m_0\le f_0(z)\le M_0)]^{b}\\
 &\quad\quad(m_0,M_0\text{ fresh witnesses from }P(f_0))\\
4.&\quad\quad\text{The pointwise inequality for }f_0\text{ follows from line 2.}\\
5.&\quad\quad B_\sigma\quad\text{by Proposition `cor:certA` with }h=f_0.\\
6.&\quad B_\sigma\quad\text{discharging the }m_0,M_0\text{ witness scope }b.\\
7.&B_\sigma\quad\text{by }\exists\text{-elimination on line 1, discharging }a.\\
8.&(\exists f\,A_\sigma(f))\to B_\sigma\quad\text{discharging }e.
\end{array}
$$

All witness-dependent objects—$f_0$, its bounds $m_0,M_0$, the values $(\mathcal K_\kappa f_0)(z)$ and, for a mesh witness, its nodal values and cell polynomials—stay within the witness scope. Neither $B_\sigma$ nor $\Gamma_\exists$ contains $f_0,m_0,M_0$. The consequent is the same for every qualifying test function. The required order is $\exists f\,\forall z\in X$ with the bounds and operator inequality above; the manuscript does not replace it by $\forall z\in X\,\exists f$.

For the reduced functions, [Lemma `lem:sym`](../paper/paper.tex#L2139) explicitly constructs

$$
f(y,[v],i)=h_1(\tau_i y,[\tau_i v]).
$$

The supplied $\tau_{23}$ symmetry makes this an invariant function, preserves its infimum and supremum, and transports the whole pointwise inequality. Positivity of the candidate nodal values supplies $P(f)$ on the compact mesh, while the operator inequality is a separate component of $A_\sigma(f)$. The planted defect affects the claimed verification of that component; it does not change the sufficient witness specification or allow a witness-dependent conclusion to escape.

The half-plane test at [line 2315](../paper/paper.tex#L2315) can also be written existentially:

$$
\operatorname{HP}(\mathscr B)\equiv
\exists\ell\in(\mathbb R^2)^*\setminus\{0\}\
\forall b\in\mathscr B\ (\ell(\Xi b)>0).
$$

Here the actual operation is the conditional set-selection algorithm $S=\operatorname{Short}(\{[b]\})$ if $\operatorname{HP}(\mathscr B)$, and $S=\mathbb P(T)$ otherwise. The selected $S$ depends on the corner directions, not on a chosen name $\ell$. To make the witness scope explicit, under a fresh $\ell_0$ with the displayed properties and coefficients $a_b\ge0$, $\sum a_b>0$, one obtains

$$
\ell_0\!\left(\Xi\sum_ba_b b\right)=\sum_ba_b\ell_0(\Xi b)>0.
$$

Thus every such sum is nonzero, and the signed cone lies in a half-plane and projects to its definite cone arc $A_{\mathscr B}$. This conclusion and the definition of $A_{\mathscr B}$ are independent of $\ell_0$, so its assumption can be discharged. This describes what the half-plane condition supplies; it does not alter the manuscript's choice of $S$. In the witness, $\ell_0(\xi,\eta)=-\eta$ supplies every required half-plane property. The false inclusion $A_{\mathscr B}\subseteq S$ already fails while that very witness is fixed. There is no separate loss of a witness property, scope condition, or quantifier order at existential elimination.

## DEF — Note

**Status: violated; role: direct.** The failing object is the **directional enclosure produced by the algorithm**, not the existence of a shortest arc as an abstract set.

The scalar and vector objects at [lines 2301–2315](../paper/paper.tex#L2301) have the actual definitions given above: $u,d_k\in\mathbb R$, $c,p_w,\alpha_w,V_k(x)w,U(x)w\in T$, with $x\in C_i$, $j\ne i$, $w\in T\setminus\{0\}$. They exist uniquely because $x_j\ge1/4$ and $d_k\ge1+k/2>0$. The map $V_k(x):T\to T$ is linear and invertible. Indeed, on the two-dimensional space $T$, with $g=e_j-\mathbf1/3$, $g^*c=-1$ and $\beta=ku/d_k$,

$$
\det D_x\psi_j^k=d_k^{-2}\det(\mathrm{id}+\beta cg^*)
=d_k^{-2}(1-\beta)=d_k^{-3}>0.
$$

Consequently $V_k(x)w\ne0$. The limiting vector $U(x)w$ may vanish for other inputs, but a box containing zero cannot have all its corners in a strict half-plane, so such an input does not pass this branch's test. The witness has $U\ne0$.

The coordinate map is unambiguous, with inverse

$$
\Xi^{-1}(\xi,\eta)=
\left(\frac\xi3,-\frac\xi6+\frac\eta2,-\frac\xi6-\frac\eta2\right).
$$

For an input set $D$ and a tail starting at $K$, the algorithm accepts rectangles $B_0,B_\infty$ containing the two endpoint-vector ranges. Its codomain is closed subsets of $\mathbb P(T)$, and its prescribed output is

$$
\mathcal S(D,j,K;B_0,B_\infty)=
\begin{cases}
\operatorname{Short}(\{[b]:b\in\mathscr B\}),&\operatorname{HP}(\mathscr B),\\
\mathbb P(T),&\text{otherwise}.
\end{cases}
$$

Its defining **enclosure contract**, required by [case (c)](../paper/paper.tex#L2256) and by the image-cell selection at [line 2305](../paper/paper.tex#L2305), is

$$
\forall(x,w)\in D\ \forall k\in\mathbb Z_{\ge K},\qquad
[D_x\psi_j^k(w)]=[V_k(x)w]\in\mathcal S(D,j,K;B_0,B_\infty).
\tag{E}
$$

After symmetry reduction, the corresponding target set uses $\tau_j\mathcal S$ and must contain the directional coordinate of every $\Phi_{j,k}$ image. The hulls $[h_1]$ and $[\nabla h_1]$ are then constructed over cells meeting that target set. Their intended codomains are real intervals and interval vectors that contain the actual target values and gradients.

For the explicit admissible input

$$
D=\{((0,\tfrac12,\tfrac12),(4K+3,-4K-4,1))\},\qquad i=1,\quad j=2,
$$

the defining formulas give

$$
V_K=(K+1)(3,-4,1),\qquad U=(-1,0,1),\qquad
V_{2K+1}=2(K+1)(1,-2,1).
$$

The exact singleton rectangles

$$
B_0=\{(9(K+1),-5(K+1))\},\qquad B_\infty=\{(-3,-1)\}
$$

contain the endpoint ranges and pass the half-plane test $\eta<0$. Their unique shortest projective arc is $S=[4/9,4/3]$ in $\vartheta$. The output at the finite admissible run $k=2K+1$ has $\vartheta=0$. Thus the produced set fails (E).

The failure also holds with explicit positive-width rectangles. Put $q=K+1$ and take

$$
\begin{aligned}
B_0&=q\left([899/100,901/100]\times[-501/100,-499/100]\right),\\
B_\infty&=[-301/100,-299/100]\times[-101/100,-99/100].
\end{aligned}
$$

Their corner directions lie respectively in $[398/899,402/901]$ and $[400/301,400/299]$. They still pass $\eta<0$, and the shortest containing arc excludes zero. The signed cross-pair inner products are all negative (in these coordinates the inner product is $\xi\xi'/6+\eta\eta'/2$), so this is also the short arc for the Euclidean angular metric. No zero-vector or tied-arc case is involved.

A shortest closed arc containing a finite set of directions exists: remove a largest gap between successive distinct directions on the projective circle. In this witness the largest gap is unique, so the shortest-arc set itself satisfies its narrow definition and is unique. Changing the global representative $w$ multiplies both true endpoint vectors by the same scalar and leaves their projective directions unchanged. The angular coordinate is also invariant under every nonzero scalar. The failed requirement is instead **containment of the run range for the enclosure being constructed**. This is part of the object's introduction in the submitted verification procedure, not an unrelated theorem asserted later about a successfully constructed enclosure.

For a concrete failure of the next constructed value interval, choose the base mesh $\ell_0=0,\ell_1=1$ and the angular nodes

$$
0,\ \tfrac34,\ \tfrac78,\ 1,\ \tfrac98,\ \tfrac54,\ 2,
\qquad\text{with closing node }4.
$$

Both meshes have the required symmetries in [Section `ssec:P1`](../paper/paper.tex#L2167). Define a base-independent function on $C_1\times\mathbb P(T)$ by

$$
h_1(\vartheta)=
\begin{cases}
8\vartheta-6,&7/8\le\vartheta\le1,\\
10-8\vartheta,&1\le\vartheta\le9/8,\\
1,&\text{elsewhere on }\mathbb R/4\mathbb Z.
\end{cases}
$$

The values at $7/8,1,9/8$ are $1,2,1$. Thus $h_1$ is continuous, separately affine on each cell, positive, bounded and invariant under $\vartheta\mapsto2-\vartheta$; independence of the base coordinates supplies the remaining $\tau_{23}$ symmetry. It is an admissible test function for the stated enclosure method.

The required transposition gives

$$
\vartheta([\tau_2V_K])=5/6,\quad
\vartheta([\tau_2U])=3,\quad
\vartheta([\tau_2V_{2K+1}])=1.
$$

Hence the constructed false target arc is $[3,4]\cup[0,5/6]$. Every whole angular cell meeting it has $h_1=1$; the last selected cell below the peak ends at $7/8$, whereas $5/6<7/8$ with gap $1/24$. The constructed value hull is therefore $[1,1]$. The actual target has value $h_1(1)=2$. Its base coordinate is admissible, since

$$
\tau_2\psi_2^k(x)=
\left(\frac1{2(k+1)},\frac{k}{2(k+1)},\frac12\right)\in C_1.
$$

The weight $W_{2,2K+1}$ is strictly positive by invertibility of the derivative. Thus the actual factor $h_1\circ\Phi_{2,2K+1}$ falls outside its asserted hull at an admissible target state. Even the positive-width rectangles above preserve this example: the upper end of the transformed low-coordinate corner cluster is $1002/1201<7/8$. The stated conservative cell-selection tolerance is much smaller than these strict separations.

## CONV — Note

**Status: not_violated; role: diagnostic.** The exact starting expression at [line 2301](../paper/paper.tex#L2301) is $d_k^2D_x\psi_j^k(w)$; its claimed endpoint at [line 2303](../paper/paper.tex#L2303) is $d_kp_w-w_jc$. Expanding [eq:DR](../paper/paper.tex#L2005) gives

$$
\begin{aligned}
d_k^2D_x\psi_j^k(w)
&=d_k^2\frac1{d_k}\left(w+\frac{ku}{d_k}w_jc\right)\\
&=d_kw+ku\,w_jc\\
&=d_kw+(d_k-1)w_jc\\
&=d_k(w+w_jc)-w_jc\\
&=d_kp_w-w_jc.
\end{aligned}
$$

Consequently

$$
V_k-V_K=(d_k-d_K)p_w=(k-K)up_w=(k-K)U.
$$

For a finite block $k_1<k_2$ the corresponding identity is

$$
V_k=\frac{k_2-k}{k_2-k_1}V_{k_1}
+\frac{k-k_1}{k_2-k_1}V_{k_2}\qquad(k_1\le k\le k_2).
$$

Both affine-combination formulas and their nonnegative coefficients are correct. At an endpoint one coefficient is zero, which causes no problem for the cone argument.

The weight conversion is correct as well. From its definition at [line 2245](../paper/paper.tex#L2245),

$$
\begin{aligned}
W_{j,k}
&=d_k^{-3(1-\kappa)}|D_x\psi_j^k(\hat w)|^\kappa\\
&=d_k^{-3+3\kappa}d_k^{-2\kappa}|V_k(x)\hat w|^\kappa\\
&=d_k^{-3}(d_k|V_k(x)\hat w|)^\kappa\\
&=d_k^{-(3-2\kappa)}\left|p_{\hat w}-\frac{\alpha_{\hat w}}{d_k}\right|^\kappa,
\end{aligned}
$$

as in [lines 2305–2309](../paper/paper.tex#L2305).

Here is the complete substitution for the counterexample. With $x=(0,1/2,1/2)$, $j=2$ and $w_K=(4K+3,-4K-4,1)$,

$$
\begin{aligned}
u&=1,&d_k&=k+1,\\
c&=\frac{(1/2,0,1/2)-(0,1/2,1/2)}{1/2}=(1,-1,0),\\
p_{w_K}&=(4K+3,-4K-4,1)+(-4K-4)(1,-1,0)=(-1,0,1),\\
U&=(-1,0,1),\\
V_k&=(k+1)(-1,0,1)-(-4K-4)(1,-1,0)\\
&=(4K+3-k,-4K-4,k+1).
\end{aligned}
$$

This also follows independently by differentiating the projective quotient: if $A=A_2^k$, then $Ax=(k/2,1/2,(k+1)/2)$, $\mathbf1^*Ax=k+1$ and $\mathbf1^*Aw_K=2k(w_K)_2$, so

$$
d_k^2D_x\psi_2^k(w_K)
=d_kAw_K-(\mathbf1^*Aw_K)Ax
=(4K+3-k,-4K-4,k+1).
$$

The witness is within the prescribed representative convention. Its source direction is

$$
\vartheta([w_K])=1-\frac{4K+5}{12K+9}
=\frac{8K+4}{12K+9}\in(0,2/3),
$$

and the manuscript's representative $w(\vartheta)=(2,-1+3(\vartheta-1),-1-3(\vartheta-1))$ satisfies $w_K=((4K+3)/2)w(\vartheta)$. This is a positive rescaling of the same input, and $\mathbf1^*w_K=0$.

At the relevant endpoints and intermediate run,

$$
\begin{array}{c|c|c|c}
\text{vector}&\xi&\eta&\vartheta\pmod4\\ \hline
V_K=(K+1)(3,-4,1)&9(K+1)&-5(K+1)&1-5/9=4/9\\
U=(-1,0,1)&-3&-1&1+1/3=4/3\\
V_{2K+1}=2(K+1)(1,-2,1)&6(K+1)&-6(K+1)&1-1=0
\end{array}
$$

Every displayed direction uses the first branch of the manuscript's formula, including equality in the last row. The signed angle satisfies

$$
V_K\cdot U=-2(K+1),\qquad
|V_K|=\sqrt{26}(K+1),\qquad |U|=\sqrt2,\qquad
\cos\angle(V_K,U)=-\frac1{\sqrt{13}}.
$$

It lies strictly between $\pi/2$ and $\pi$. Therefore the cone of the actual signed vectors projects to

$$
A_{\mathscr B}=[4/3,4]\cup[0,4/9],
$$

whereas the unique shortest endpoint arc is $S=[4/9,4/3]$. The same shorter arc is selected using the period-four coordinate, since its coordinate length is $8/9<2$. Thus the witness does not depend on choosing between the two natural meanings of angular length.

Finally, applying $\tau_2$ directly gives proportional vectors $(-4,3,1)$, $(0,-1,1)$ and $(-2,1,1)$. Their $(\xi,\eta)$ values are respectively $(-12,2)$, $(0,-2)$ and $(-6,0)$, giving

$$
1+2/(-12)=5/6,\qquad 3-0/(-2)=3,\qquad 1+0/(-6)=1.
$$

For example,

$$
|D_x\psi_2^{2K+1}(\hat w_K)|
=\frac{\sqrt6}{2(K+1)\sqrt{32K^2+56K+26}}>0.
$$

These substitutions verify the test-function and positive-weight statements in the DEF Note. Exact rational checks of the supplied calculation and an independent quotient-derivative calculation agree at $K=1,1025,2^{28}+1,10^{12}$; the displayed algebra proves the family for every integer $K\ge1$.

There is no incorrect equality in these conversions. At the planted sentence, the starting geometric information is $V_k\in\operatorname{cone}_{\ge0}(\mathscr B)\setminus\{0\}$, and the claimed endpoint is $[V_k]\in S$. Projectivizing the starting set yields $A_{\mathscr B}$, not $S$. The manuscript does not give a composition, substitution or algebraic identity equating these sets; it supplies a false geometric enclosure inference. The calculations diagnose that failed range/construction obligation and do not establish an additional direct CONV label.

## Final direct labels and comparison

**Final direct labels: G (G1) and DEF.**

The [tricker report](tricker_report.md#g1-classification-and-quantified-inference) and three existing checker reports classify the planted error as G1. This review retains G1, with the precise failure located in the unproved conditional derivation that extends endpoint/corner membership to the full run range. Its variable-freshness condition itself is satisfied.

This review **adds DEF**. The earlier reports reject DEF because the witness's shortest arc exists uniquely. That correctly settles existence of the arc, but the classification standard also requires a construction to satisfy its defining contract. The manuscript introduces the output specifically as a directional enclosure used to contain every image in the value and increment bounds. The finite run $k=2K+1$ violates that contract, and the explicit admissible $h_1$ gives a constructed factor hull $[1,1]$ that misses the actual value $2$, because the selected target cells omit the cell containing that image.

MP is recorded only as downstream failure to establish the full antecedent of the certificate proposition. G2 has no separate failure, and the CONV calculations are correct and diagnostic.

The witness settles the classification: the universal directional inclusion and the enclosure contract both fail for the same admissible input, for every integer $K\ge1$, including the manuscript's tail cutoff $K=2^{28}+1$.
