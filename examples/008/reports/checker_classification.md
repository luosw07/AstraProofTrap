# 008: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow. It is informed by the source and existing construction/checker materials, rather than being an original workflow report or a blind reviewer run. The existing labels are assessed independently. Reviewer verdicts and target-detection counts are outside this review.

## Target, assumptions, and source trace

The target is the instruction in the proof of Theorem 4.1, under “Validity of the completed stages,” to use Lemma 4.2's construction with

$$
Q=\min\{q:q\text{ is a prime power},\ q\ge\max\{D_{i+1},k-1\}\}.
$$

It is at [manuscript line 1866](../paper/paper.tex#L1866), printed page 30. The consequential application is the assertion at [line 1881](../paper/paper.tex#L1881) that the same construction preserves the prescribed codegree bounds. The induction and the next applications of the short-trajectory and one-stage results use that assertion at [lines 1882–1887](../paper/paper.tex#L1882).

The [original manuscript](../original/paper.tex#L1866) instead invokes Lemma 4.2 without changing its construction. An independent comparison of the complete TeX files confirms that the [supplied patch](../mutation.diff) is their only difference. I read the complete modified manuscript, the original passage together with that comparison, the [tricker report](tricker_report.md), the [original checker report](checker_report.md), the [checker calculation](checker_calculation.py), the [case README](../README.md), the [classification standard](../../../protocol/classification.md), and the complete supplied [Bennett–Bohman reference](../paper/references/bennett_bohman.txt). The calculations below independently check both the local construction and its occurrence in the iteration.

The actual ambient assumptions are those of [Theorem 4.1](../paper/paper.tex#L1191): fixed integer $k\ge3$, a finite simple $n$-vertex $d$-regular $k$-uniform hypergraph, and

$$
\Gamma(H)(\log n)^L=o(1),\qquad
n^{-C_0}\le\lambda\le n^{C_0},
$$

for fixed $C_0>0$. Here, by [equation (1.3)](../paper/paper.tex#L439),

$$
\Gamma(H)=\sqrt{\Delta_2(H)/d}
+\max_{3\le j\le k}(\Delta_j(H)/d)^{1/(j-1)},
\qquad
\Delta_j(H)=\max_{|U|=j}|\{e\in E(H):U\subseteq e\}|.
$$

Theorem 4.1 itself imposes no polynomial lower bound on $d$. The witness below also satisfies the stronger main-theorem hypotheses, which do impose such a bound.

The proof reduces to $2k\mid n$, sets $\ell=\log(n+2)$, and defines the deterministic sequences before selecting prefixes or completions. To distinguish the constants in the two recurrences, write $c_D,c_L>0$ for the sufficiently large fixed constants denoted by $C_k$ in [equations (4.9)–(4.10)](../paper/paper.tex#L1717):

$$
\begin{aligned}
D_{i+1}&=\left\lceil 2^{-(k-1)}D_i
+c_D\ell\sqrt{D_iL_2^{(i)}}\right\rceil,\\
L_j^{(i+1)}&=(2^{-(k-j)}+c_L\ell^{-2})L_j^{(i)}
+c_L\ell^4L_{j+1}^{(i)}\quad(2\le j<k),\\
L_k^{(i)}&=1.
\end{aligned}
$$

A completed stage must be simple and $D_i$-regular, have order divisible by $2k$, and satisfy $\Delta_j(H_i)\le L_j^{(i)}$. The intended stopping index is

$$
T=\left\lfloor\log_2\frac1{\Gamma(H)\ell^B}\right\rfloor.
$$

The relevant source dependencies are concrete:

- [Lemma 4.2, lines 1239–1275](../paper/paper.tex#L1239), supplies an existential completion with codegree control. Its displayed recipe explicitly chooses a **prime** $Q$, and uses the ordinary integer coefficients $j$ in $b+ja$.
- [Theorem 4.3 and Lemma 4.5](../paper/paper.tex#L1335) require the *actual* pair-codegree bound $L_2=o(D/(\log N)^5)$. The supplied reference's [Section 2 and Theorem 2.1](../paper/references/bennett_bohman.txt#L180) impose that condition and give the degree error $O_k(\sqrt{DL_2\log N})$ on a fixed-fraction interval. They provide no additional restriction on a completion's field characteristic.
- [Lines 1583–1584](../paper/paper.tex#L1583) choose completions from Lemma 4.2 with its codegree guarantee. [Lines 1712–1725](../paper/paper.tex#L1712) and [1854–1883](../paper/paper.tex#L1854) make that guarantee the recursive stage invariant.
- The ensuing remainder iteration is [Claim 4.6](../paper/paper.tex#L1891). The lower-bound application at [Proposition 6.2](../paper/paper.tex#L2755), particularly [line 2780](../paper/paper.tex#L2780), subsequently invokes Theorem 4.1 at activity $\lambda d$.

No other passage specifies distinct field evaluation elements in place of the integers $0,\ldots,k-2$, or supplies a characteristic bound for the new least-prime-power choice. The prime-power parameters in the subspace-design applications concern different hypergraphs. The unchanged prime-field construction in Lemma 4.2 remains valid under its own hypotheses.

## Verified witness in an actual stage

Fix $k=4$ and the proof's chosen constants $c_D,c_L$. Let $p>3$ tend to infinity through primes, set $n=8p$, $\ell=\log(8p+2)$, and let $Q_p$ be the least power of two at least $p/32$. Then

$$
\frac p{32}\le Q_p<\frac p{16}.
$$

For integers $d\in[\lceil p/16\rceil,p]$, put

$$
f_p(d)=d/8+c_D\ell\sqrt d.
$$

For all sufficiently large $p$,

$$
f_p(\lceil p/16\rceil)<p/64<Q_p,
\qquad f_p(p)>p/8>Q_p,
$$

and, uniformly throughout this interval,

$$
0<f_p(d+1)-f_p(d)
=\frac18+\frac{c_D\ell}{\sqrt{d+1}+\sqrt d}<1.
$$

Consequently the nondecreasing integer sequence $\lceil f_p(d)\rceil$ has increments zero or one and crosses $Q_p$. Choose a $d=d_p$ with

$$
D_1=\left\lceil d/8+c_D\ell\sqrt d\right\rceil=Q_p.
\tag{W1}
$$

This works for every fixed permitted $c_D$, and $d=\Theta(p)$.

Choose $A_0\subseteq\mathbb F_p$ of cardinality $d$. On $\{0,1,2,3\}\times\mathbb F_p$, take the edges

$$
\{(j,b+j\alpha):0\le j\le3\},
\qquad \alpha\in A_0,\ b\in\mathbb F_p,
$$

and let $H_0$ be the disjoint union of two copies. Each vertex has exactly one incident edge for each slope $\alpha$, hence degree $d$. Distinct coordinate positions have nonzero difference in the prime field $\mathbb F_p$; two specified vertices therefore determine at most one slope and intercept. The graph is simple and linear, with

$$
|V(H_0)|=8p,\qquad
\Delta_2(H_0)=\Delta_3(H_0)=\Delta_4(H_0)=1.
$$

Thus $8\mid n$, and

$$
\Gamma(H_0)=d^{-1/2}+d^{-1/3}=O(p^{-1/3}),
\qquad \Gamma(H_0)(\log n)^L\longrightarrow0
$$

for every fixed $L$. Take $\lambda=1$. The stopping index tends to infinity, so $T\ge2$ eventually. The stronger weighted-counting hypotheses also hold, for example with $\varepsilon=1/24$: linearity gives every intersection coefficient zero, $d\ge n^{1/24}$ eventually, and

$$
\frac{\Gamma(H_0)}{d^{-1/4}n^{-1/24}}
=O(p^{-1/24})\longrightarrow0.
$$

At stage zero, the actual short-trajectory hypothesis is

$$
\frac{L_2^{(0)}(\log n)^5}{D_0}
=\frac{(\log(8p))^5}{d}\longrightarrow0.
$$

The unmodified Theorem 4.3 and Lemma 4.5 therefore give good trajectories with probability at least $1/2$, for large $p$. Every good prefix $P$ has $p=n/8$ edges. Its residual $F=H_0-V(P)$ has $4p$ vertices, remains simple and linear, and satisfies the sharper degree estimate

$$
|d_F(v)-d/8|\le C_B\sqrt{d\log n}
\qquad(v\in V(F)),
$$

for a fixed constant $C_B$. From (W1),

$$
D_1-d_F(v)\ge
\sqrt d\bigl(c_D\ell-C_B\sqrt{\log n}\bigr)>0
$$

eventually. Hence the deficit sum $S=\sum_v(D_1-d_F(v))$ is positive for **every** good first prefix. All input hypotheses on $F,D_1$ in Lemma 4.2 hold.

The changed instruction chooses $Q=D_1=Q_p=2^r$, with $r\ge2$, and forces the slope set to be all of $\mathbb F_Q$. In each fresh auxiliary copy,

$$
E_{\alpha,b}
=\{(0,b),(1,b+\alpha),(2,b+2\alpha)\}
=\{(0,b),(1,b+\alpha),(2,b)\}.
\tag{W2}
$$

For fixed $b$, these are $D_1$ distinct edges containing the pair $\{(0,b),(2,b)\}$. Appending old vertices and taking eight disjoint copies retain this pair and its incident edges. All vertices still have degree $D_1$, so the output $H_1$ has

$$
\Delta_2(H_1)=D_1=Q_p=\Theta(p).
\tag{W3}
$$

In contrast, the unchanged recurrence gives

$$
L_2^{(1)}=\frac14+c_L\ell^{-2}+c_L\ell^4
=O(\ell^4)=o(Q_p).
\tag{W4}
$$

Thus the asserted completed-codegree bound fails at the first completion. All choices of good prefix and edge labels have this defect. In particular, the later minimization over prefixes does not change the witness.

The next short-trajectory application has an actual required ratio at least

$$
\frac{\Delta_2(H_1)(\log N_1)^5}{D_1}
=(\log N_1)^5\longrightarrow\infty,
$$

where $N_1=|V(H_1)|\to\infty$. It therefore loses its required hypothesis. The deterministic sequences remain defined and retain their numerical estimates; (W3)–(W4) show the failure to connect them to the constructed hypergraph.

## Five-item audit summary

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | direct | [1866 and 1881](../paper/paper.tex#L1866), using [1250–1265](../paper/paper.tex#L1250) | [The proven prime-field construction guarantee is applied to a specified output whose field order is not prime.](#mp-note) |
| G1 | violated | downstream | [1881–1882](../paper/paper.tex#L1881); compare the valid degree uniformity at [1866](../paper/paper.tex#L1866) | [The universal stage claim lacks its pointwise premise because of the completion failure; the quantified ranges and variable conditions add no direct error.](#g1-note) |
| G2 | not_violated | none | [1240–1246](../paper/paper.tex#L1240), [1583](../paper/paper.tex#L1583), and [1887](../paper/paper.tex#L1887) | [Existential completions and minimizing prefixes can be scoped correctly; the altered field prescription is a specified construction, not an escaping witness.](#g2-note) |
| DEF | violated | direct | [1712–1725](../paper/paper.tex#L1712), [1866–1882](../paper/paper.tex#L1866) | [The proposed next-stage construction fails its explicit codegree contract, although its finite hypergraph and field expressions exist.](#def-note) |
| CONV | not_violated | diagnostic | [1252–1266](../paper/paper.tex#L1252), as invoked at [1866–1881](../paper/paper.tex#L1866) | [Correct expansion gives codegree $D_1$; the erroneous endpoint is imported through an inapplicable guarantee, rather than a printed invalid algebraic transformation.](#conv-note) |

<a id="mp-note"></a>

## MP — Note

**Status: violated. Role: direct.** The original rule is

$$
\frac{\Gamma_{\mathrm{MP}}\vdash A_{\mathrm{MP}}
\qquad\Gamma_{\mathrm{MP}}\vdash A_{\mathrm{MP}}\to B_{\mathrm{MP}}}
{\Gamma_{\mathrm{MP}}\vdash B_{\mathrm{MP}}}.
$$

Here the first failure is the unestablished—and in the witness false—prime-order hypothesis of the construction guarantee.

### Objects and full instantiated context

Use the stage-zero witness above, with $k=4$, $D=D_1=Q_p$, and $F=H_0-V(P)$ for a good prefix. Write $\mathbb E=\mathbb F_Q$ to distinguish the field from the hypergraph $F$. In this Note, $A_{\mathrm{MP}}$ is a logical formula; $A\subseteq\mathbb E$ is the manuscript's slope set.

The local background $\Gamma_{\mathrm{MP}}$ consists of the following specified data and established facts:

1. $p>3$ is a sufficiently large prime, $n=8p$, $\ell=\log(n+2)$, $c_D,c_L$ are the proof's fixed positive constants, $d\in\mathbb N$ is the degree chosen in (W1), and $\lambda=1$.
2. $H_0$ is the simple linear $d$-regular 4-uniform hypergraph constructed above; $T\ge2$. Its initial codegree bounds are all one.
3. $P$ is a matching of $p$ edges admitting a good ordering. The finite residual $F$ has vertex set of size $4p$, is simple and 4-uniform, has $\Delta(F)\le D$, and has $\Delta_j(F)\le1$ for $j=2,3,4$.
4. $\delta(v)=D-d_F(v)\in\mathbb N$ for each $v\in V(F)$, $\mathcal S=\{(v,t):1\le t\le\delta(v)\}$, and $S=|\mathcal S|>0$.
5. $D=Q_p$, $Q$ is the least eligible prime power in the modified instruction, and hence $Q=D=2^r$, $r\ge2$. The field $\mathbb E$ has $Q$ elements. Its canonical integer-scalar map is $\iota(m)=m1_{\mathbb E}$. The slope set is $A=\mathbb E$, of cardinality $D$.
6. $\eta:A\times\mathbb E\to[DQ]$ is a bijection labeling the auxiliary edges. $K$, together with its old-copy embeddings, is the output of the displayed auxiliary-edge, stub-attachment, and eight-copy recipe. Denote its number of old copies by $a=8DQ$ and new vertices by $w=24QS$.
7. The numerical next bounds are $L_2^{(1)}=1/4+c_L\ell^{-2}+c_L\ell^4$, $L_3^{(1)}=1/2+c_L\ell^{-2}+c_L\ell^4$, and $L_4^{(1)}=1$; they are at least one. They bound the residual codegrees.

These facts do not include the disputed codegree assertion about $K$. The notation for the output recipe is expanded in the DEF Note.

### The implication actually available

There are two useful ways to expose the same application. First, the **statement** of Lemma 4.2 is existential. With its variables instantiated by $k=4,F,D$, its antecedent is

$$
I(F,D):=
F\text{ finite, simple and 4-uniform}
\ \land\ D\in\mathbb N_{>0}
\ \land\ \forall v\in V(F)\ d_F(v)\le D.
$$

Its consequent is

$$
\exists K'\,\exists a'\,\exists w'\,
\operatorname{Comp}(F,D;K',a',w'),
\tag{MP1}
$$

where $\operatorname{Comp}$ includes: $K'$ is finite, simple, 4-uniform and $D$-regular; it contains the specified number $a'$ of disjoint copies of $F$ and exactly $w'$ other vertices; $a'=O(D^2)$; $w'/a'=3S/D$; $8\mid |V(K')|$; and

$$
\begin{gathered}
\forall j\in\{2,3,4\}\quad
\Delta_j(K')\le\max\{\Delta_j(F),1\},\\
\forall t\in\mathbb R_{>0}\quad
\log Z_F(t)\ge\frac1{a'}\log Z_{K'}(t)
-\frac{w'}{a'}\log(1+D\max\{1,t\}).
\end{gathered}
$$

Here $Z_J(t)=\sum_{M\in\mathcal M(J)}t^{|M|}$; embeddings and the old/new vertex partition are part of the completion data. For $j>4$, the codegrees are zero. The input $I(F,D)$ is established, so MP legitimately gives (MP1). That existential consequent does not identify its witness with the separately prescribed output $K$.

Second, to audit the instruction to use the **construction**, the following is a symbolic reconstruction of the guarantee established by the proof of Lemma 4.2. It retains the proof's prime hypothesis and all its actual choices; it is not an additional theorem assumed for prime powers:

$$
\forall(F,D,Q,\mathbb E,A,\eta,K,a,w)\quad
\bigl(\mathcal A(F,D,Q,\mathbb E,A,\eta,K,a,w)
\to\operatorname{Comp}(F,D;K,a,w)\bigr).
\tag{MP2}
$$

For the nonzero-deficit branch, $\mathcal A$ is the conjunction of:

$$
\begin{aligned}
&I(F,D),\qquad S=\sum_{v\in V(F)}(D-d_F(v))>0,\\
&Q\text{ prime},\qquad Q\ge\max\{D,3\},\qquad Q=O(D),\\
&\mathbb E\text{ a field of cardinality }Q,\quad
A\subseteq\mathbb E,\quad |A|=D,\\
&\eta:A\times\mathbb E\to[DQ]\text{ bijective},\\
&E_{\alpha,b}=\{(j,b+\iota(j)\alpha):j=0,1,2\},\\
&(K,a,w)\text{ obtained by the stated stubs, attachments and eight copies}.
\end{aligned}
$$

In these logical formulas, $Q=O(D)$ means $Q\le C_QD$, and $a=O(D^2)$ means $a\le C_aD^2$, for fixed constants chosen in the lemma's construction, independent of the input size. They record its uniform size requirements; the witness has $Q=D$. They have no bearing on the failed characteristic condition.

Substitute all the objects of $\Gamma_{\mathrm{MP}}$ into (MP2). This gives the implication $A_{\mathrm{MP}}\to B_{\mathrm{MP}}$, with

$$
A_{\mathrm{MP}}=\mathcal A(F,D,Q,\mathbb E,A,\eta,K,a,w),
\qquad B_{\mathrm{MP}}=\operatorname{Comp}(F,D;K,a,w).
$$

The manuscript's exported conclusion at line 1881 is

$$
C:\quad \forall j\in\{2,3,4\}\quad
\Delta_j(K)\le L_j^{(1)}.
$$

If $B_{\mathrm{MP}}$ held, this $C$ would follow from the established residual bounds and $L_j^{(1)}\ge1$. The claimed degree equality $\deg K=D_1$ at line 1866 is a separate, valid component of the construction.

The failed sequent is therefore explicit:

$$
\begin{gathered}
\Gamma_{\mathrm{MP}}\vdash A_{\mathrm{MP}}\to B_{\mathrm{MP}},\\
\Gamma_{\mathrm{MP}}\vdash
\text{every listed conjunct of }A_{\mathrm{MP}}
\text{ except }\operatorname{Prime}(Q),\\
\Gamma_{\mathrm{MP}}\vdash Q=2^r,\quad r\ge2,\quad
\neg\operatorname{Prime}(Q).
\end{gathered}
$$

Thus MP cannot supply $B_{\mathrm{MP}}$. More strongly, (W3) shows its pair-codegree component false, and (W4) shows $C$ false. If the citation is read solely as the existential lemma (MP1), the same defect appears as exporting a property of the designated $K$ instead of preserving the existential consequent. These are two descriptions of the same direct misuse, not independent planted errors.

### Downstream theorem application

At the next stage, substitute $G=H_1$, $N=N_1$, $D=D_1$, $k=4$, and $L_2=L_2^{(1)}$ into Theorem 4.3. Its compound antecedent requires regularity, uniformity, $8\mid N_1$,

$$
\Delta_2(H_1)\le L_2^{(1)}
\quad\text{and}\quad
L_2^{(1)}(\log N_1)^5/D_1\longrightarrow0.
$$

The consequent is high-probability degree control throughout $N_1/8$ greedy steps. The numerical smallness assertion does not establish the missing actual-codegree bound. Choosing a larger honest upper bound cannot restore the hypothesis, since every such bound is at least $D_1$. This later MP failure is downstream of the direct completion error. Theorem 4.1's subsequent use in Proposition 6.2 inherits the broken proof dependency.

<a id="g1-note"></a>

## G1 — Note

**Status: violated. Role: downstream.** This records the unproved universal validity assertion at line 1882. There is no additional direct restriction-dropping or variable-scope defect. In particular, the literal claim at line 1866 that the completed degree is the same for all good completions is correct.

The rule to audit is

$$
\frac{\Gamma_{\mathrm{G1}}\vdash A_*\to B_*(x)}
{\Gamma_{\mathrm{G1}}\vdash A_*\to\forall x\,B_*(x)},
\qquad x\notin\operatorname{FV}(\Gamma_{\mathrm{G1}})\cup\operatorname{FV}(A_*).
$$

Here is a concrete reconstruction of the local uniformity in the witness. Fix the initial data $p,n,d,H_0,\ell,D_1,Q,\mathbb E$, the sequences $D_i,L_j^{(i)}$, and the completion algorithm. Let $\mathcal P$ be the finite set of good unordered prefixes of $H_0$ of size $p$, as defined at [lines 1573–1576](../paper/paper.tex#L1573). The field is fixed with $|\mathbb E|=Q=D_1$, so the slope set is forced to be $\mathbb E$.

Take $x=(P,\eta)$, ranging over pairs consisting of a subset $P\subseteq E(H_0)$ and a map $\eta:\mathbb E^2\to[D_1Q]$. Define the range predicate

$$
\begin{aligned}
\mathcal D(P,\eta):={}&
P\text{ a matching}\ \land\ |P|=p
\ \land\ P\text{ admits a good ordering}\\
&\land\ \eta\text{ is bijective}.
\end{aligned}
$$

Explicitly, a good ordering is an enumeration $(e_1,\ldots,e_p)$ of $P$. Set $G_t=H_0-\bigcup_{h\le t}e_h$ and $q_t=1-t/(2p)$. For fixed constants $C_B,C_S$ in the two cited estimates, the ordering satisfies

$$
\begin{gathered}
\forall t\in\{0,\ldots,p\}\ \forall v\in V(G_t)\quad
|d_{G_t}(v)-dq_t^3|\le C_B\sqrt{d\log n},\\
\forall j\in\{2,3\}\quad
\Delta_j(G_p)\le 2^{-(4-j)}
+C_S\left(\sqrt{\frac{\log n}{d}}+\sqrt{\log n}+\log n\right).
\end{gathered}
$$

The second line is Lemma 4.5 with the initial $L_2,L_3,L_4$ all equal to one. These are residual conditions. For $\mathcal D(P,\eta)$, define $F_P=G_p=H_0-V(P)$, $S_P=\sum_v(D_1-d_{F_P}(v))$, and $K_{P,\eta}$ by the modified recipe. These dependencies stay inside the range predicate's conditional scope.

The background $\Gamma_{\mathrm{G1}}$ consists exactly of the fixed initial data and their properties established in the witness, the deterministic sequence definitions, the definition of good prefixes, and the finite-field and completion formulas. It includes the uniform residual estimates supplied by the unchanged short-trajectory results. It excludes every assertion of completed codegree control. Let

$$
A_*:=\mathcal P\ne\varnothing,
$$

which is established independently of the selected $P,\eta$. Define

$$
\begin{aligned}
B_{\deg}(P,\eta)
&:=\mathcal D(P,\eta)\to
\bigl(\forall v\in V(K_{P,\eta})\quad d_{K_{P,\eta}}(v)=D_1\bigr),\\
B_{\mathrm{stage}}(P,\eta)
&:=\mathcal D(P,\eta)\to
\left(
\begin{array}{l}
K_{P,\eta}\text{ simple, 4-uniform and }D_1\text{-regular},\\
8\mid |V(K_{P,\eta})|,\\
\forall j\in\{2,3,4\}\ \Delta_j(K_{P,\eta})\le L_j^{(1)}
\end{array}
\right).
\end{aligned}
$$

For an arbitrary selected $(P,\eta)$, the pre-generalization argument actually has this structure:

$$
\begin{array}{ll}
1.&[A_*],\ [\mathcal D(P,\eta)]\quad\text{open local assumptions};\\
2.&F_P\text{ satisfies the residual bounds, and }S_P>0;\\
3.&\text{form }K_{P,\eta}\text{ by the prescribed recipe};\\
4.&d_{K_{P,\eta}}(v)=D_1\text{ for every old and new vertex};\\
5.&\Delta_j(K_{P,\eta})\le L_j^{(1)}
\quad\text{claimed by the failed application at line 1881};\\
6.&\text{discharge }\mathcal D(P,\eta)\text{ and }A_*.
\end{array}
$$

Step 4 follows from the degree count in the DEF Note. Thus

$$
\Gamma_{\mathrm{G1}}\vdash A_*\to B_{\deg}(P,\eta)
\quad\Longrightarrow\quad
\Gamma_{\mathrm{G1}}\vdash
A_*\to\forall P\,\forall\eta\,B_{\deg}(P,\eta)
$$

is a valid instantiated G1 application. It proves exactly the degree uniformity asserted in the edited sentence.

For $B_{\mathrm{stage}}$, however, step 5 fails already for the selected object: every permitted $(P,\eta)$ in this witness satisfies

$$
\Delta_2(K_{P,\eta})=D_1>L_2^{(1)}.
$$

The pre-generalization premise

$$
\Gamma_{\mathrm{G1}}\vdash A_*\to B_{\mathrm{stage}}(P,\eta)
$$

has therefore not been derived. Its attempted universal conclusion is a downstream failure of G1's requirement for a proved pointwise implication.

The free-variable check is separate and passes. The free parameters of the background are the fixed initial hypergraph, numeric sequences, field, algorithm and good-prefix family; neither the local $P$ nor $\eta$ occurs freely there. $A_*$ contains the family $\mathcal P$, not a selected member. All selected-object restrictions—matching, prefix size, good ordering and bijective labeling—are inside $\mathcal D$ and are discharged into $B$. No minimizing property is assumed before this generalization: minimization occurs later at line 1887.

The assertion “this verifies every stage through $T$” is similarly the restricted conclusion

$$
\forall i\in\mathbb Z\quad
\left(0\le i\le T\to
\left[
\begin{array}{l}
H_i\text{ simple, }D_i\text{-regular, }k\text{-uniform}\\
\land\ 2k\mid N_i\\
\land\ \forall j\in\mathbb Z\,
(2\le j\le k\to\Delta_j(H_i)\le L_j^{(i)})
\end{array}
\right]\right).
$$

Its initial case holds, but the prescribed transition from stage zero does not establish the case $i=1$. The universal claim fails because the earlier construction/application fails at a particular stage, not because a valid prime-only derivation was generalized by an illicit eigenvariable step. Accordingly this downstream G1 finding adds no direct **G** label.

<a id="g2-note"></a>

## G2 — Note

**Status: not_violated. Role: none.** The changed prescription is a particular construction. Nearby existential choices have a valid scope structure, and there is no direct inference claiming that an insufficient existential witness alone provides the missing codegree property.

The rule is

$$
\frac{\Gamma_{\mathrm{G2}}\vdash A(x)\to B}
{\Gamma_{\mathrm{G2}}\vdash(\exists x\,A(x))\to B},
\qquad x\notin\operatorname{FV}(\Gamma_{\mathrm{G2}})\cup\operatorname{FV}(B).
$$

First, the exact local operation at line 1866 is

$$
\mathcal Q_D=\{q\in\mathbb N:q\text{ a prime power},\ q\ge\max\{D,k-1\}\},
\qquad Q=\min\mathcal Q_D,
\qquad K=\mathcal C(F,D,Q,\mathbb E,A,\eta).
$$

The set $\mathcal Q_D$ is nonempty (it contains sufficiently large powers of two), and its least element is unique. This specification is not a derivation of a conclusion independent of a fresh variable from $\exists q\,A(q)$. Existence of a field of order $Q$ supplies exactly that field; it supplies no claim that the integers $0,1,2$ have distinct images in it. The changed construction is evaluated in that field, with the result (W2).

For comparison, Lemma 4.2's genuine existential conclusion is (MP1): a tuple $y=(K',a',w',\text{embeddings})$ satisfies the full predicate $\operatorname{Comp}(F,D;y)$. Every field or labeling used to produce that witness is internal to its construction. Selecting a witness satisfying this full predicate is legitimate. The modified recipe fails to establish that predicate for its chosen tuple. This is the contract/application failure already identified, rather than an eigenvariable escaping an existential elimination.

### Explicit existential elimination for the actual minimizing-prefix choice

The instruction at [line 1887](../paper/paper.tex#L1887) chooses a prefix attaining the finite minimum in Lemma 4.6. Its logical scope can be made completely explicit. Fix a stage $i$, its finite hypergraph $G=H_i$, order $N=N_i$, degree $D_i>0$, $\lambda>0$, $\ell$, $L_2^{(i)}$, and the finite nonempty good-prefix family $\mathcal P_i$. Fix the chosen completion family

$$
\kappa(P)=(K_P,a_P,w_P)\qquad(P\in\mathcal P_i).
$$

Each $K_P$ is a finite regular hypergraph with positive degree, $a_P\in\mathbb N_{>0}$, $w_P\in\mathbb N_0$, and

$$
N_P=|V(K_P)|=a_PN/2+w_P>0.
$$

Set

$$
\begin{aligned}
R_J(\lambda)&=\log Z_J(\lambda)
-\frac{|V(J)|}{k}(\log(\lambda\deg J)-k+1),\\
\rho_i&=R_G(\lambda)/N,\\
e_i&=C\ell^2\sqrt{L_2^{(i)}/D_i},\\
\Phi(P)&=\left(\frac12+\frac{w_P}{a_PN}\right)\frac{R_{K_P}(\lambda)}{N_P}.
\end{aligned}
$$

Here $C$ is a fixed sufficiently large constant for the one-stage error. Positivity of $Z_J(\lambda)$, $\deg J$, $\lambda$ and the denominators makes every $\Phi(P)$ a real number.

For this elimination, $\Gamma_{\mathrm{G2}}$ consists of precisely these fixed data, their indicated finite/positive domains, the definitions of $\kappa,N_P,R_J,\rho_i,e_i,\Phi$, the order identities, and the displayed one-stage premise

$$
\rho_i\ge-e_i+\min_{P\in\mathcal P_i}\Phi(P).
\tag{G2-premise}
$$

This names the premise used at that selection step. Its availability at later modified stages is an upstream theorem-application issue; it is not being independently certified here for stages whose hypotheses have failed.

Let the witness $x$ range over subsets of the finite edge set $E(G)$, and put

$$
A(x):=x\in\mathcal P_i\ \land\
\forall P\in\mathcal P_i\ \Phi(x)\le\Phi(P).
$$

These are exactly the properties supplied by “a prefix attaining the minimum.” Let the witness-independent target be

$$
B:=\exists K\,\exists a\,\exists w\left[
(K,a,w)\in\operatorname{im}\kappa
\ \land\
\rho_i\ge-e_i+\frac{|V(K)|}{aN}\frac{R_K(\lambda)}{|V(K)|}
\right].
$$

An explicit fresh-witness subderivation is

$$
\begin{array}{ll}
1.&[A(x_*)]\quad(x_*\text{ fresh});\\
2.&\Phi(x_*)=\min_{P\in\mathcal P_i}\Phi(P);\\
3.&(K_*,a_*,w_*):=\kappa(x_*),\quad N_*=|V(K_*)|;\\
4.&\rho_i\ge-e_i+\Phi(x_*)
=-e_i+\dfrac{N_*}{a_*N}\dfrac{R_{K_*}(\lambda)}{N_*};\\
5.&B\quad\text{by existential introduction of }K_*,a_*,w_*;\\
6.&A(x_*)\to B\quad\text{by discharging line 1};\\
7.&(\exists x\,A(x))\to B\quad\text{by G2}.
\end{array}
$$

The equality in line 4 uses $N_*=a_*N/2+w_*$. All hidden dependencies are exposed: $F_{x_*}$, its deficit sum, $K_*$, $a_*$, $w_*$, $N_*$, and $R_{K_*}$ may depend on the prefix. They stay within its scope and are bound in $B$. The free parameters of $\Gamma_{\mathrm{G2}}$ and $B$ are $G,N,D_i,k,\lambda,\ell,L_2^{(i)},C,\mathcal P_i,\kappa$, with the displayed definitions; neither contains $x_*$ freely. Finite nonemptiness supplies $\exists x\,A(x)$.

The manuscript then names such a selected completion $H_{i+1}$ and continues its construction within that choice. Writing $A_i$ for the displayed minimizing-prefix predicate $A$ instantiated at stage $i$, its intended choice order, conditional on the stage premises being available, is

$$
\forall i\in\mathbb Z\quad
(0\le i<T\to\exists P_i\,A_i(P_i)).
$$

The distinct assertion requiring a single prefix for all stages would be

$$
\exists P\ \forall i\in\mathbb Z\quad
(0\le i<T\to A_i(P)).
$$

The source never makes that exchange. The data defining $A_i$, including $H_i$, $\mathcal P_i$, $\kappa$ and $\Phi$, vary with the current stage and its prior choices. The loss of the codegree invariant happens before this minimization and holds for all its eligible prefixes. There is no additional unproved *minimizer-specific* property or witness-scope violation to classify as G2.

<a id="def-note"></a>

## DEF — Note

**Status: violated. Role: direct.** The defective construction is the next-stage completion with its required codegree bounds. The underlying finite graph exists, but the stated iterative construction does not return an object in the required class.

### Formula, domains, and output

For an admissible finite simple $k$-uniform input $F=(V,E)$ and positive integer $D\ge\Delta(F)$, define

$$
\delta(v)=D-d_F(v)\in\mathbb N_0,
\quad
\mathcal S=\{(v,t):v\in V,\ 1\le t\le\delta(v)\},
\quad S=|\mathcal S|.
$$

If $S=0$, the recipe takes $2k$ disjoint copies of $F$. In the branch relevant here, $S>0$. Choose $Q$ by the altered minimum rule, a field $\mathbb E$ of order $Q$, and a set $A\subseteq\mathbb E$ of size $D$. Let

$$
J=\{0,\ldots,k-2\},\qquad
\iota:\mathbb Z\to\mathbb E,\quad m\mapsto m1_{\mathbb E},
$$

and define the auxiliary edge map

$$
\begin{aligned}
e:A\times\mathbb E&\longrightarrow\binom{J\times\mathbb E}{k-1},\\
(\alpha,b)&\longmapsto E_{\alpha,b}
=\{(j,b+\iota(j)\alpha):j\in J\}.
\end{aligned}
$$

The first coordinates are integer tags, so every such set has $k-1$ vertices even when their field coefficients coincide. Since $k\ge3$, coordinates 0 and 1 recover $b$ and $\alpha$. Thus $e$ is injective and there are $a_0=DQ$ distinct auxiliary edges. Choose a labeling bijection $\eta:A\times\mathbb E\to[a_0]$.

Use disjointly tagged vertex sets

$$
V_{\mathrm{old}}=[a_0]\times V,
\qquad
V_{\mathrm{new}}=\mathcal S\times J\times\mathbb E.
$$

The pre-divisibility graph $\widetilde K$ contains the old edges $\{(h,v):v\in e_0\}$, for $h\in[a_0]$, $e_0\in E$, together with, for each $\sigma=(v,t)\in\mathcal S$, the added edges

$$
\{(\eta(\alpha,b),v)\}
\ \cup\
\{(\sigma,j,b+\iota(j)\alpha):j\in J\},
\qquad(\alpha,b)\in A\times\mathbb E.
$$

Finally set $K$ to be the disjoint union of $2k$ copies of $\widetilde K$. The actual algorithm has domain consisting of the input $F,D$ and these permitted field, slope and labeling choices, and codomain the finite simple $k$-uniform hypergraphs equipped with their old-copy embeddings. Its advertised codomain is the subclass satisfying Lemma 4.2's completion properties, including codegree preservation.

### Obligations that hold

The least eligible prime power exists and is unique by well-ordering. A power of two between $M=\max\{D,k-1\}$ and $2M$ shows $Q<2M=O_k(D)$, allowing equality $Q=M$ when $M$ itself is eligible. A field of prime-power order exists, and $Q\ge D$ permits the slope set. The finite-field expressions, the stub set and the labeling all have the displayed domains.

The construction is simple: distinct old copies are disjoint; every added edge has one old vertex and $k-1$ new vertices; different stubs have disjoint new vertices; and within a stub, distinct $(\alpha,b)$ produce distinct auxiliary edges. Old vertices gain one edge per deficit stub, so their final degrees are

$$
d_F(v)+\delta(v)=D.
$$

A new vertex $(\sigma,j,x)$ lies in exactly one edge for each $\alpha\in A$, with the uniquely determined intercept

$$
b=x-\iota(j)\alpha.
$$

It therefore also has degree $D$. The counts are

$$
a=2kDQ,\qquad w=2k(k-1)QS,\qquad
\frac wa=\frac{(k-1)S}{D},\qquad 2k\mid |V(K)|.
$$

The matching encoding at [lines 1268–1274](../paper/paper.tex#L1268) remains injective: restrictions to the old copies plus the incident-edge/absence record at every new vertex determine the matching. An added matching edge has $k-1$ new vertices, so its record weight $\max\{1,\lambda\}^{k-1}$ is at least $\lambda$, for every $\lambda>0$. Thus this encoding's partition-function inequality survives.

Uniqueness of the resulting labeled hypergraph is not a requirement: the source explicitly permits choices. There is no quotient representative or recursion ambiguity. The coefficient $\iota(j)$ is canonical, and a field isomorphism preserves its values and all the incidence equations. Relabeling edges or field elements preserves the codegree calculation below. The deterministic recurrences for $D_i,L_j^{(i)}$ themselves have unique real/integer values at every finite index; their validity as numerical definitions is separate from their proposed bounds on $H_i$.

### Failed construction requirement

For the witness, $k=4$, $D=Q=2^r$, $A=\mathbb E$, and $S>0$. Fix any stub $\sigma$ and intercept $b$. The two new vertices

$$
u=(\sigma,0,b),\qquad v=(\sigma,2,b)
$$

belong together to all $D$ edges indexed by $(\alpha,b)$, $\alpha\in\mathbb E$, because $\iota(2)\alpha=0$. Those edges are distinct. The outer copies do not change their common incidence. Consequently

$$
d_K(\{u,v\})=D,
\qquad \Delta_2(K)=D,
$$

where the upper bound follows from $D$-regularity. This violates both

$$
\Delta_2(K)\le\max\{\Delta_2(F),1\}=1
\quad\text{and}\quad
\Delta_2(H_1)\le L_2^{(1)}.
$$

This is a construction-contract failure, rather than merely a subsequent conjecture about an arbitrary well-defined graph. The source introduces the completion specifically to preserve higher codegree bounds at [lines 1234–1242](../paper/paper.tex#L1234), requires such completions in [lines 1583–1584](../paper/paper.tex#L1583), states that the deterministic $L_j^{(i)}$ bound the constructed stages at [lines 1712–1715](../paper/paper.tex#L1712), and checks closure of that invariant at [lines 1854–1882](../paper/paper.tex#L1854). The modified recipe fails this declared output specification at its first transition. Existence of other completions from the unchanged lemma does not fulfill the specification of this prescribed construction.

<a id="conv-note"></a>

## CONV — Note

**Status: not_violated. Role: diagnostic.** The relevant computations can be performed exactly. They expose the failed construction guarantee. The altered passage's first invalid step is the application of that guarantee, with its prime hypothesis missing; it does not print an independent erroneous conversion of field expressions.

### Exact starting expression and claimed endpoint

The starting expression is the [display at lines 1252–1256](../paper/paper.tex#L1252), imported by line 1866:

$$
E_{\alpha,b}=\{(j,b+j\alpha):0\le j<k-1\}.
$$

The original prime-field proof's claimed property is linearity, followed by the pair-incidence bound at line 1265. The target later imports its endpoint

$$
\Delta_2(K)\le\max\{\Delta_2(F),1\},
$$

and hence $\Delta_2(K)\le L_2^{(1)}$ at line 1881.

For two auxiliary vertices $(j,x),(h,y)$ with $j\ne h$, expand their incidence conditions:

$$
\begin{aligned}
(j,x),(h,y)\in E_{\alpha,b}
&\iff x=b+\iota(j)\alpha\ \land\ y=b+\iota(h)\alpha\\
&\iff (\iota(j)-\iota(h))\alpha=x-y
\ \land\ b=x-\iota(j)\alpha.
\end{aligned}
$$

For prime $Q\ge k-1$, the nonzero integer $j-h$, of absolute value at most $k-2<Q$, has nonzero image. Thus

$$
\alpha=(\iota(j)-\iota(h))^{-1}(x-y),
\qquad b=x-\iota(j)\alpha
$$

gives at most one allowed edge. This calculation under the lemma's stated hypothesis is correct.

For the changed choice $k=4,Q=D=2^r$, the actual expansion is instead

$$
\begin{aligned}
\iota(0)\alpha&=0,\\
\iota(1)\alpha&=\alpha,\\
\iota(2)\alpha&=(1_{\mathbb E}+1_{\mathbb E})\alpha
=\alpha+\alpha=0,\\
E_{\alpha,b}&=\{(0,b),(1,b+\alpha),(2,b)\}.
\end{aligned}
$$

For the pair $\{(0,b_0),(2,b_0)\}$, its codegree is therefore

$$
\begin{aligned}
\bigl|\{(\alpha,b)\in\mathbb E^2:
b=b_0,\ b+2\alpha=b_0\}\bigr|
&=\bigl|\{\alpha\in\mathbb E:0=0\}\bigr|\\
&=|\mathbb E|=D.
\end{aligned}
$$

Distinct slopes give distinct values at coordinate 1, so this count is a count of distinct edges. Attachment adds one old vertex to each edge without deleting any new vertex. Copies remain disjoint. The endpoint of the correct computation is $\Delta_2(K)=D$, exactly as used in (W3).

There is no valid intermediate equality replacing $0\alpha=0$ by a unique value of $\alpha$. The source does not actually write such a division for the modified field: its explicit linearity assertion is still inside the prime-field proof. The first unjustified transition in the target is invoking that proven assertion for the different prescribed construction at lines 1866/1881. This is the MP/DEF failure, with the computation serving as its certificate.

### Other computations used at the target

The original size normalization remains exact:

$$
\frac{2k(k-1)QS}{2kDQ}=(k-1)S/D.
$$

The Young-inequality calculation immediately before the false completed-codegree assertion also remains valid. For $u=\ell^{-1}\sqrt{L_j^{(i)}}$ and $v=\ell^2\sqrt{L_{j+1}^{(i)}}$,

$$
0\le(u-v)^2
=\ell^{-2}L_j^{(i)}
-2\ell\sqrt{L_j^{(i)}L_{j+1}^{(i)}}
+\ell^4L_{j+1}^{(i)}.
$$

Rearrangement gives precisely [lines 1876–1878](../paper/paper.tex#L1876). With $k=4$, $L_2^{(0)}=L_3^{(0)}=1$, substitution in (4.10) gives

$$
L_2^{(1)}=(2^{-(4-2)}+c_L\ell^{-2})\cdot1
+c_L\ell^4\cdot1
=1/4+c_L\ell^{-2}+c_L\ell^4.
$$

This calculation correctly bounds the residual by the preceding short-trajectory argument. Passing from that residual to the modified completion is the failed extra obligation.

### Independent finite calculation

I reran the supplied [checker calculation](checker_calculation.py), obtaining auxiliary pair-codegree 4 over $\mathbb F_4$ and 1 over $\mathbb F_5$ with four slopes. I also independently enumerated the **entire** stub-attachment and eight-copy construction for a valid local input: $F$ consists of one 4-edge, $D=4$, and thus $S=4(4-1)=12$. Integer scalar multiplication was implemented by repeated field addition. The exact results were:

| Field order | Old copies $a$ | New vertices $w$ | Total vertices | Edges | Degree | $\Delta_2$ | $\Delta_3$ | $\Delta_4$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $Q=4$, characteristic 2 | 128 | 1152 | 1664 | 1664 | 4 | 4 | 1 | 1 |
| $Q=5$, prime field, four slopes | 160 | 1440 | 2080 | 2080 | 4 | 1 | 1 | 1 |

Both outputs are simple, 4-uniform and 4-regular, with the claimed size ratio and divisibility. This finite calculation verifies the local completion failure and the surviving structural properties. The asymptotic witness above separately places the same failure inside the theorem's actual iteration.

## Final direct classification

**Final direct labels: MP, DEF.** MP is the unsupported transfer of the prime-field construction guarantee to the least-prime-power output. DEF is the failure of the prescribed next-stage construction to satisfy its explicit codegree invariant.

These agree with the primary MP and secondary DEF labels in the [case README](../README.md) and the construction/checker evidence. This review makes DEF precise as an output-contract and recursive-invariant failure; it does not base DEF on nonexistence of the finite field or hypergraph. The universal stage assertion has a downstream G1 failure because its pointwise premise is already false. G2 contributes no additional violation, and the finite-field calculation is diagnostic rather than a direct CONV error.

There is no unresolved mathematical issue affecting this classification. The pair collision, its persistence through the full completion, and its occurrence at a required stage under the actual hypotheses are verified.
