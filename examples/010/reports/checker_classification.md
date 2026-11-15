# 010: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow. It is informed by the complete modified manuscript, the original manuscript and its exact mutation, and the existing construction/checker materials; it is a classification review rather than an original workflow report or a blind reviewer run.

The direct labels are **MP and G2 (G)**. The revised proof selects an arbitrary block certified through an initial horizon, obtains a later covering horizon depending on that block, and applies the original certificate beyond its range. The selected witness satisfies its actual construction requirements. Its second image nevertheless fails the per-iterate assertion used to finish the proof.

## Exact target, assumptions, and notation

The target is the proof of Theorem 7.12 (`TB`), specifically the [finite-range block selection, lines 4218–4220](../paper/paper.tex#L4218), the [enlargement of the covering horizon, lines 4232–4233](../paper/paper.tex#L4232), and the final assertion:

> “By the choice of $B$, each set $T^nB$ in this union is a finite union of good blocks, and the result follows.”

This assertion occurs at [lines 4257–4258](../paper/paper.tex#L4257), immediately after the equality $K^*=\bigcup_{n=0}^N T^nB$. The [mutation](../mutation.diff) contains these three coordinated changes. The [original selection](../original/paper.tex#L4218) required widths chosen as in Lemma 7.11 (`LTB`), and its [final inference](../original/paper.tex#L4259) invoked that lemma's all-iterate conclusion.

The actual background is as follows.

- $m\in\mathbb N$, $m\ge2$, and $\mathbf p=(p_1,\ldots,p_m)\in\mathbb R^m$, with $p_i>0$ and $\sum_i p_i=1$. Positivity is a [standing assumption](../paper/paper.tex#L2452). The indexed family $(p_1,\ldots,p_m)$ is linearly independent over $\mathbb Q$, the manuscript's [ergodic hypothesis](../paper/paper.tex#L3107).
- $H_{\boldsymbol0}=\{\mathbf x\in\mathbb R^m:\sum_i x_i=0\}$, $\ell_{ij}(\mathbf x)=x_i-x_j$, and $\mathbf e_i$ is the $i$th coordinate vector. The target explicitly uses the **multivalued** Frege map. As a function on subsets it is

$$
T:\mathcal P(H_{\boldsymbol0})\longrightarrow\mathcal P(H_{\boldsymbol0}),\qquad
T(S)=\bigcup_{i=1}^m
\left(\left((S+\mathbf p)\cap\mathcal V_i\right)-\mathbf e_i\right),
\quad
\mathcal V_i=\{\mathbf y:y_i\ge y_j\text{ for every }j\}.
$$

  Both winning branches are retained at a tie. This is the [set interpretation of $T$](../paper/paper.tex#L1423), also written as [cutting and translation](../paper/paper.tex#L4003). Write $T^0S=S$ and $T^{n+1}S=T(T^nS)$ for $n\in\mathbb N_0=\{0,1,\ldots\}$.
- $\pi(\mathbf x)=[\mathbf x]\in\mathbb R^m/\mathbb Z^m$, $\widehat H_{\boldsymbol0}=\pi(H_{\boldsymbol0})$, and $R_{\mathbf p}(\widehat{\mathbf x})=\widehat{\mathbf x}+[\mathbf p]$. The torus $\widehat H_{\boldsymbol0}$ is compact, and both forward and backward orbits of this translation are dense under the ergodic hypothesis. The [projection identity](../paper/paper.tex#L2728) is $\pi(T^nS)=R_{\mathbf p}^n(\pi(S))$.
- Fix $\delta\in\mathbb R$ with $0<\delta\le1/m$. The [neighborhoods used in the proof](../paper/paper.tex#L3378) are

$$
\mathcal N_\delta=\{\mathbf x\in H_{\boldsymbol0}:\max_i|x_i|<\delta\},
\qquad
\widehat{\mathcal N}_\delta=\pi(\mathcal N_\delta).
$$

- Theorem 7.5 (`Tinv`) already supplies the nonempty compact invariant set $K^*$, with $T(K^*)=K^*$, $K^*\subseteq K_0:=H_{\boldsymbol0}\cap[-1+1/m,m-1]^m$, and $\pi(K^*)=\widehat H_{\boldsymbol0}$. Its proof supplies $\mathcal N_\delta\subseteq K^*$ and

$$
\mathbf v\in K_0,\quad \pi(\mathbf v)\in\widehat{\mathcal N}_\delta
\quad\Longrightarrow\quad \mathbf v\in\mathcal N_\delta,
$$

  with $\pi$ injective on $\mathcal N_\delta$; see [the neighborhood argument](../paper/paper.tex#L3385) and [source step `Tinv4`](../paper/paper.tex#L3428).

For precise formulas, let $I_m=\{(i,j):1\le i<j\le m\}$. For $\rho\in(0,\infty)^{I_m}$ define the actual block formula

$$
B_\rho=\{\mathbf x\in H_{\boldsymbol0}: -\rho_{ij}\le x_i-x_j\le\rho_{ij}
\text{ for every }(i,j)\in I_m\}.
$$

A **good block** is a compact polytope given by finitely many inequalities of the form $\ell_{ij}(\mathbf x)\ge a$ and having nonempty interior in $H_{\boldsymbol0}$, exactly as at [lines 4015–4023](../paper/paper.tex#L4015). For $S\subseteq H_{\boldsymbol0}$ write

$$
\operatorname{FG}(S)\ \Longleftrightarrow\
\exists r\in\mathbb N_0\ \exists Q_1,\ldots,Q_r\subseteq H_{\boldsymbol0}
\left(S=\bigcup_{j=1}^r Q_j\ \land\ \bigwedge_{j=1}^r Q_j\text{ is a good block}\right).
$$

Allowing the empty union is immaterial here: the selected block, its iterates, and $K^*$ are nonempty. Introduce the following abbreviations, with $b\subseteq H_{\boldsymbol0}$ and $L,N_0,M,n\in\mathbb N_0$:

$$
\begin{aligned}
Q(b,n)&:=\operatorname{FG}(T^n b),\\
F(b,L)&:=\forall n\in\mathbb N_0\,(n\le L\ \Longrightarrow\ Q(b,n)),\\
\operatorname{Form}_\delta(b)&:=
\exists\rho\in(0,\infty)^{I_m}\,(b=B_\rho\ \land\ b\subseteq\mathcal N_\delta),\\
P(b,N_0)&:=\operatorname{Form}_\delta(b)\land F(b,N_0),\\
C_\delta(N_0)&:=\widehat H_{\boldsymbol0}
=\bigcup_{k=0}^{N_0}R_{\mathbf p}^{k}(\widehat{\mathcal N}_\delta),\\
C_b(M)&:=\widehat H_{\boldsymbol0}
=\bigcup_{k=0}^{M}R_{\mathbf p}^{k}\bigl(\pi(\operatorname{int}_{H_{\boldsymbol0}}b)\bigr),\\
S(b,M)&:=(M\ge N_0)\land C_b(M),\\
E(b,M)&:=K^*=\bigcup_{n=0}^M T^n b,\\
H&:=\operatorname{FG}(K^*).
\end{aligned}
$$

The manuscript uses the same letter $N$ for two values. Here $N_0$ denotes its value at the initial choice, and $M$ its value after enlargement. This records the existing proof's dependencies without changing its assumptions. The first cover, [(tinv5a)](../paper/paper.tex#L3458), concerns $\widehat{\mathcal N}_\delta$; the later cover concerns the generally smaller $\pi(\operatorname{int}B)$.

In the Notes, $\Gamma_0$ consists of all the typed background assumptions and established facts just listed, the definition of $\operatorname{FG}$ and the displayed abbreviations, the universally quantified statement of [Lemma `LTB`](../paper/paper.tex#L4050), and a fixed $N_0\in\mathbb N_0$ satisfying $C_\delta(N_0)$. No selected block or later horizon is part of $\Gamma_0$. In particular, all its free mathematical parameters are among $m,\mathbf p,\delta,N_0$; $H$ depends only on $m,\mathbf p$.

Lemma `LTB` states that **joint** rational independence of the coordinates of $\mathbf p$ and the positive widths $\rho_{ij}$ implies $Q(B_\rho,n)$ for every $n\in\mathbb N_0$. Joint independence means that

$$
\sum_i a_i p_i+\sum_{i<j}b_{ij}\rho_{ij}=0,
\qquad a_i,b_{ij}\in\mathbb Q,
$$

forces every coefficient to vanish. The revised selection retains only $P(B,N_0)$, expressly permitting **any** block with those properties.

## Five-item audit summary

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | direct | [4218–4220](../paper/paper.tex#L4218), [4257–4258](../paper/paper.tex#L4257) | The certificate gives $n\le N_0\Rightarrow Q(B,n)$; the final application establishes only $n\le M$. [Full Note](#mp-note). |
| G1 | not_violated | downstream | [4225–4230](../paper/paper.tex#L4225), [4235–4258](../paper/paper.tex#L4235) | The local universal-introduction steps preserve their ranges. The final universal goodness assertion inherits the failed certificate application; no separate generalization step removes an index restriction. [Full Note](#g1-note). |
| G2 | violated | direct | [4218–4220](../paper/paper.tex#L4218), [4232–4233](../paper/paper.tex#L4232), [4257–4258](../paper/paper.tex#L4257) | The witness-to-conclusion derivation uses $F(B,M)$ although the chosen witness supplies only $F(B,N_0)$. [Full Note](#g2-note). |
| DEF | not_violated | none | [(tb4)](../paper/paper.tex#L4056), [4218–4223](../paper/paper.tex#L4218), [4232–4246](../paper/paper.tex#L4232) | The block, projections, multivalued iterates, covering horizon, and lift satisfy their actual defining requirements. [Full Note](#def-note). |
| CONV | not_violated | diagnostic | [4241–4255](../paper/paper.tex#L4241), [4257–4258](../paper/paper.tex#L4257), [(T1b)](../paper/paper.tex#L4895) | The set/projection calculations are correct. Exact branch arithmetic exposes a false property assertion rather than an erroneous printed computation. [Full Note](#conv-note). |

<a id="mp-note"></a>
## MP — Note

**Status: violated. Role: direct.** The direct failure is the use of the earlier finite certificate in the final “By the choice of $B$” sentence. There are also valid MP applications in the same proof, which must be distinguished from that failure.

The rule is

$$
\frac{\Gamma\vdash A\qquad\Gamma\vdash A\to B_{\mathrm{MP}}}
{\Gamma\vdash B_{\mathrm{MP}}}.
$$

First check the explicit invocation of `LTB` at [line 4220](../paper/paper.tex#L4220). Instantiate its width variables by a positive vector $\sigma\in(0,\infty)^{I_m}$ jointly rationally independent with $\mathbf p$, and its block by $B_\sigma$. The instantiated antecedent and consequent are

$$
\begin{aligned}
A_{\mathrm{LTB}}&:=
\bigl(\mathbf p\text{ is ergodic}\bigr)\land
\bigl(\sigma_{ij}>0\text{ for all }(i,j)\in I_m\bigr)\land
\operatorname{Ind}_{\mathbb Q}(\mathbf p,\sigma),\\
B_{\mathrm{LTB}}&:=\forall n\in\mathbb N_0\ Q(B_\sigma,n).
\end{aligned}
$$

All parts of $A_{\mathrm{LTB}}$ can be satisfied while making $B_\sigma\subset\mathcal N_\delta$: positive widths can be chosen successively in an arbitrarily small interval outside the rational span of the preceding choices and the $p_i$. The containment calculation is given in the DEF Note. MP therefore supplies exactly $B_{\mathrm{LTB}}$, which implies $F(B_\sigma,N_0)$ and then

$$
C_{\mathrm{existence}}:=\exists b\subseteq H_{\boldsymbol0}\ P(b,N_0).
$$

This validates the manuscript's existence assertion. It does not attach $A_{\mathrm{LTB}}$ to each witness of the weaker existential conclusion.

For the defective application, fix the block actually selected by the revised text and write

$$
\Gamma_{\mathrm{MP}}
=\Gamma_0,\ P(B,N_0),\ M\in\mathbb N_0,\ M\ge N_0,\ C_B(M).
$$

Here $B\in\mathcal P(H_{\boldsymbol0})$ and the components of $P$ are exactly the positive-width formula, containment in $\mathcal N_\delta$, and goodness for $0\le n\le N_0$. No joint independence of $B$'s widths, no all-iterate certificate, and no upper bound $M\le N_0$ occurs among these assumptions. The set equality $E(B,M)$ is derived from this context by the intervening geometric argument.

The following is a **symbolic reconstruction of the printed reference to the choice of $B$**. It retains the original range. For an index $n\in\mathbb N_0$, universal instantiation of the selected certificate gives

$$
\Gamma_{\mathrm{MP}}\vdash
\underbrace{n\le N_0}_{A_n}
\ \Longrightarrow\
\underbrace{\operatorname{FG}(T^nB)}_{B_n}.
$$

For a term in the final union, the additional available assumption is $n\le M$. The manuscript claims $C_n:=\operatorname{FG}(T^nB)$ for every such term. Thus $C_n=B_n$; the failure is the antecedent, not a strengthened consequent:

$$
\begin{aligned}
\Gamma_{\mathrm{MP}},\ n\le M&\vdash n\le N_0\ \Longrightarrow\ Q(B,n),\\
\Gamma_{\mathrm{MP}},\ n\le M&\not\models n\le N_0.
\end{aligned}
$$

The verified instance in the CONV Note has

$$
N_0=1,\qquad B=[-2\epsilon,2\epsilon],\qquad M=353,\qquad n=2,
\qquad \epsilon=\frac{\sqrt2}{1000}.
$$

It satisfies every component of $\Gamma_{\mathrm{MP}}$ and $2\le353$. The required antecedent is $2\le1$, which is false, and $Q(B,2)$ itself is false. More generally, every admissible covering horizon for this $B$ is at least $176$. The failed use is therefore present for every horizon the proof can select for this witness.

The last words “the result follows” apply the valid finite-union implication

$$
\underbrace{\left(K^*=\bigcup_{n=0}^M T^nB\right)
\land\left[\forall n\in\mathbb N_0\,(n\le M\Rightarrow\operatorname{FG}(T^nB))\right]}_{A_{\mathrm{union}}}
\quad\Longrightarrow\quad
\underbrace{\operatorname{FG}(K^*)}_{B_{\mathrm{union}}}.
$$

For each of the finitely many $n$, a finite list of good blocks for $T^nB$ would concatenate into a finite list for $K^*$. This implication has the claimed consequent $C=H=B_{\mathrm{union}}$. Its unestablished conjunct is $F(B,M)$, inherited from the preceding direct MP failure.

The later application of [the polytope-support lemma](../paper/paper.tex#L4288) in [Theorem `TX`](../paper/paper.tex#L4341) has the same distinction: substituting $K=K^*$ into “finite union of compact full-dimensional polytopes $\Rightarrow\operatorname{supp}(\lambda_K)=K$” preserves that lemma's consequent. Its geometric premise is attributed to `TB`, so its missing justification is downstream. No second direct MP label is needed for that propagation.

<a id="g1-note"></a>
## G1 — Note

**Status: not_violated. Role: downstream.** The target's goodness claim is universal, but the actual unsupported operation is reuse of an already universally quantified certificate at a new bound. The ordinary generalizations used to form the covers and set inclusions are valid.

The rule to audit is

$$
\frac{\Gamma\vdash A\to B_{\mathrm{G1}}(x)}
{\Gamma\vdash A\to\forall x\,B_{\mathrm{G1}}(x)},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(A).
$$

Take $\Gamma=\Gamma_{\mathrm{MP}}$ from the preceding Note. Its free parameters are among $m,\mathbf p,\delta,N_0,B,M$; in particular, a fresh index $n\in\mathbb N_0$ is absent. Set $A=\top$ and

$$
B_{\mathrm{G1}}(n):=(n\le N_0\Rightarrow Q(B,n)).
$$

The available pre-generalization derivation is completely specified:

$$
\begin{array}{ll}
\Gamma\vdash F(B,N_0),&\text{conjunction elimination from }P(B,N_0),\\
[n\le N_0]^{1},&\text{local range assumption},\\
Q(B,n),&\text{instantiate }F(B,N_0)\text{ at }n\text{ and apply MP},\\
\Gamma\vdash n\le N_0\Rightarrow Q(B,n),&\text{discharge assumption }1.
\end{array}
$$

G1 therefore correctly yields

$$
\Gamma\vdash\top\Rightarrow
\forall n\in\mathbb N_0\,(n\le N_0\Rightarrow Q(B,n)).
$$

The only special restriction, $n\le N_0$, remains inside the quantified formula. The enlarged claim is instead

$$
\forall n\in\mathbb N_0\,(n\le M\Rightarrow Q(B,n)).
$$

Its pre-generalization obligation would be $n\le M\Rightarrow Q(B,n)$. The earlier certificate does not prove this conditional: at the witness above, $n=2$ satisfies the new range and fails $Q(B,2)$. The text does not first establish goodness for a specially chosen index and then discharge its restriction by universal introduction. It refers back to the **choice of the block**, whose existing certificate already contains the quantifier over $n$. Replacing $N_0$ by $M$ occurs in that application, identified in the MP Note. If one expands “each” into a pointwise argument followed by G1, the pointwise premise has already failed, while the eigenvariable condition for that final G1 step is satisfied. This is the downstream role recorded in the table.

For comparison, the actual arbitrary-point arguments in this target have sound pre-generalization derivations.

1. At [lines 4225–4230](../paper/paper.tex#L4225), take $x=\widehat{\mathbf u}\in\widehat H_{\boldsymbol0}$, $A=\top$, and

$$
B_{\mathrm{cover}}(\widehat{\mathbf u})
:=\exists k\in\mathbb N_0\,
\widehat{\mathbf u}\in R_{\mathbf p}^k\bigl(\pi(\operatorname{int}B)\bigr).
$$

   The open set $\pi(\operatorname{int}B)$ is nonempty, and the backward orbit of every $\widehat{\mathbf u}$ is dense. This supplies a suitable $k$ for an arbitrary point. No assumption special to that point remains open. Thus G1 gives $\forall\widehat{\mathbf u}\in\widehat H_{\boldsymbol0}\,B_{\mathrm{cover}}(\widehat{\mathbf u})$. The integer $k$ remains existentially quantified inside the formula and may depend on the point. Compactness subsequently supplies a finite subcover.

2. At [lines 4235–4249](../paper/paper.tex#L4235), take $x=\mathbf u\in H_{\boldsymbol0}$, $A=\top$, and

$$
B_{\mathrm{inclusion}}(\mathbf u)
:=\left(\mathbf u\in K^*\Rightarrow
\mathbf u\in\bigcup_{n=0}^M T^nB\right).
$$

   Assume $[\mathbf u\in K^*]^2$. The cover gives some $k\le M$ with $R_{\mathbf p}^{-k}\pi(\mathbf u)\in\pi(\operatorname{int}B)$. Backward invariance supplies $\mathbf v\in K^*$ with $\mathbf u\in T^k\{\mathbf v\}$. Projection and the unique-lift property give $\mathbf v\in\operatorname{int}B$, so $\mathbf u\in T^kB$ and hence membership in the displayed union. The local witnesses $k,\mathbf v$ are eliminated after this membership assertion; assumption 2 is discharged. Neither $\mathbf u$ nor these witness names occurs in the remaining background. G1 yields the stated restricted universal inclusion with the range predicate $\mathbf u\in K^*$ preserved.

The reverse inclusion at [lines 4251–4253](../paper/paper.tex#L4251) likewise preserves its range: $B\subseteq K^*$ is the base case, and monotonicity of $T$ gives $T^{n+1}B\subseteq T(K^*)=K^*$ from $T^nB\subseteq K^*$. Thus $\forall n\in\mathbb N_0\,(T^nB\subseteq K^*)$ is justified. This argument asserts invariance-based containment, not good-block decomposability.

<a id="g2-note"></a>
## G2 — Note

**Status: violated. Role: direct.** The block is an existential witness whose stated properties are insufficient for the particular conditional derivation printed in the proof. The eigenvariable restrictions themselves are satisfied.

The rule is

$$
\frac{\Gamma\vdash A(x)\to B_{\mathrm{G2}}}
{\Gamma\vdash (\exists x\,A(x))\to B_{\mathrm{G2}}},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(B_{\mathrm{G2}}).
$$

Use $\Gamma=\Gamma_0$, the fresh witness $x=b\in\mathcal P(H_{\boldsymbol0})$, and

$$
A(b)=P(b,N_0)
=\left[\exists\rho\in(0,\infty)^{I_m}
\,(b=B_\rho\land b\subseteq\mathcal N_\delta)\right]
\land\left[\forall n\in\mathbb N_0\,(n\le N_0\Rightarrow Q(b,n))\right],
\qquad B_{\mathrm{G2}}=H.
$$

Here $H=\operatorname{FG}(K^*)$ is the existence of a finite list of good blocks whose union is $K^*$, expanded above. Its free parameters are only $m,\mathbf p$. The selected witness's defining widths $\rho$, its interior, its projected interior, and the covering sets

$$
U_k(b):=R_{\mathbf p}^k\bigl(\pi(\operatorname{int}_{H_{\boldsymbol0}}b)\bigr)
$$

are local constructions depending on $b$. A covering horizon $M$ is subsequently selected for these $U_k(b)$, so its permissible values depend on $b$. Writing $M(b)$ informally indicates that dependency; the proof does not define a canonical function or require uniqueness of the horizon.

The printed argument has the following existential-elimination structure. This is a symbolic reconstruction, with the missing obligation marked explicitly:

$$
\begin{array}{lll}
1.&\exists b\,P(b,N_0)&\text{valid existence consequence of LTB},\\
2.&[P(b,N_0)]^{a}&b\text{ a fresh witness for line 1},\\
3.&\exists M\in\mathbb N_0\ S(b,M)&\text{density and compactness for }U_k(b),\\
4.&[S(b,M)]^{c}&M\text{ a fresh witness for line 3},\\
5.&E(b,M)&\text{the printed backward/forward invariance argument},\\
6.&F(b,M)&\text{claimed from line 2; unsupported},\\
7.&H&\text{finite-union implication using lines 5 and 6},\\
8.&H&\text{intended elimination of }M\text{ and discharge of }c,\\
9.&H&\text{intended elimination of }b\text{ and discharge of }a.
\end{array}
$$

The proposed conditional before G2 is $\Gamma_0\vdash P(b,N_0)\to H$, formed by discharging assumption $a$. Its printed derivation fails at line 6. Assumption $a$ supplies $F(b,N_0)$, whereas line 6 requires $F(b,M)$ after a potentially strict enlargement of the horizon. Both $b$ and $M$ would be absent from the exported conclusion $H$, and $b$ is absent from $\Gamma_0$; $M$ is absent from $\Gamma_0$ and $P(b,N_0)$. Thus no eigenvariable escape is needed to diagnose the failure. The additional witness property itself is false for an allowed witness.

The preceding choice of $N_0$ is also legitimate existential elimination: compactness gives $\exists N_0\in\mathbb N_0\,C_\delta(N_0)$, and $N_0$ can be fixed in the outer scope. Neither the final $H$ nor the argument establishing the initial cover requires an illicit dependence on $b$.

The quantifier structure makes the missing compatibility precise. Lemma `LTB` supplies the strong existence statement

$$
\exists b\left(\operatorname{Form}_\delta(b)
\land\forall L\in\mathbb N_0\,F(b,L)\right).
$$

In particular it supplies $\forall L\in\mathbb N_0\,\exists b\,P(b,L)$. The modified text retains only $\exists b\,P(b,N_0)$ and explicitly permits any such $b$. Separately, the valid covering argument gives

$$
\forall b\left(P(b,N_0)\Rightarrow
\exists M\in\mathbb N_0\,S(b,M)\right).
$$

The compatibility claim needed by the printed witness argument is stronger:

$$
\forall b\left(P(b,N_0)\Rightarrow
\exists M\in\mathbb N_0\,igl(S(b,M)\land F(b,M)\bigr)\right).
$$

It is false. For the explicit block in the CONV Note, $P(b,1)$ holds, every $M$ satisfying $S(b,M)$ obeys $M\ge176$, and $Q(b,2)$ fails. Thus no such $M$ satisfies $F(b,M)$. Existence of an especially well-behaved block does not establish the required conditional for the arbitrary weaker witness allowed by the revised selection.

The full manuscript supplies no premise that strengthens this particular choice. The [warning before `LTB`](../paper/paper.tex#L4038) expressly describes the lower-dimensional tied pieces that can occur. [Lemma `Luni`](../paper/paper.tex#L3262) concerns eventual absence of ties along each point's orbit and gives no full-dimensionality assertion for every image of a selected block. The [later facet remark](../paper/paper.tex#L4269) introduces joint independence for a comparison construction; it does not establish that the earlier arbitrary block has it. Indeed, an additional independent family cannot make an already dependent subfamily independent. Finally, the [two-party attractor example](../paper/paper.tex#L4973) concerns the entire invariant set, not the individual terms $T^nB$ of this decomposition.

<a id="def-note"></a>
## DEF — Note

**Status: not_violated. Role: none.** The objects introduced in the target exist and meet their stated definitions. The later assertion about a longer range of images is a property asserted after these introductions.

The principal construction is

$$
(0,\infty)^{I_m}\longrightarrow\mathcal P(H_{\boldsymbol0}),
\qquad \rho\longmapsto B_\rho
=\bigcap_{i<j}\{\mathbf x\in H_{\boldsymbol0}:-\rho_{ij}\le x_i-x_j\le\rho_{ij}\}.
$$

For each fixed width vector this specifies a unique set. It is a closed convex polyhedron. To check boundedness, use $\sum_jx_j=0$ to obtain

$$
x_i=\frac1m\sum_{j=1}^m(x_i-x_j),
\qquad
|x_i|\le\frac1m\sum_{j\ne i}\rho_{\min(i,j),\max(i,j)}.
$$

Thus it is compact. Let $r=\min_{i<j}\rho_{ij}>0$. Every $\mathbf x\in H_{\boldsymbol0}$ with $\max_i|x_i|<r/2$ satisfies $|x_i-x_j|<r\le\rho_{ij}$, proving nonempty relative interior. In particular, $B_\rho$ is a good block. No uniqueness of the choice of widths or of a halfspace representation is required: the chosen widths define a set by membership inequalities, not a function on representations.

If all widths are smaller than $s<m\delta/(m-1)$, the coordinate bound above gives $|x_i|<(m-1)s/m<\delta$, so $B_\rho\subset\mathcal N_\delta$. Such positive widths can be chosen successively outside the countable rational span of $p_1,\ldots,p_m$ and the previously chosen widths. The resulting indexed family is jointly rationally independent, and `LTB` then gives $F(B_\rho,N_0)$. Consequently the existence requirement for the **initial** contract $P(B,N_0)$ is satisfied for every permissible background.

For the concrete witness, with $m=2$ and $\rho_{12}=4\epsilon>0$, the defining inequality is

$$
-4\epsilon\le\ell_{12}(x,-x)=2x\le4\epsilon,
\qquad B_\rho=[-2\epsilon,2\epsilon].
$$

It lies in $\mathcal N_{1/2}=(-1/2,1/2)$, and both it and its first image are nondegenerate intervals. Hence this particular choice satisfies $P(B,1)$, even though its widths are not jointly independent with the votes.

The remaining target objects have the following concrete definitions and obligations.

- $B^\circ=\operatorname{int}_{H_{\boldsymbol0}}B$, $\widehat B=\pi(B)$, and $\widehat B^\circ=\pi(B^\circ)$ are the objects introduced at [lines 4221–4223](../paper/paper.tex#L4221). The interior is nonempty by the preceding calculation. The quotient projection is well defined because $\mathbf x$ and $\mathbf x+\mathbf z$, $\mathbf z\in\mathbb Z^m$, have the same class. Restricted to $H_{\boldsymbol0}$ it is an open map onto $\widehat H_{\boldsymbol0}$, so $\widehat B^\circ$ is a nonempty open set. The notation is explicitly defined as the image of the interior; the proof does not require a general identity exchanging interior and projection.
- $R_{\mathbf p}:\widehat H_{\boldsymbol0}\to\widehat H_{\boldsymbol0}$ is $[\mathbf x]\mapsto[\mathbf x+\mathbf p]$. Different representatives produce the same class, and $\sum_i p_i=1$ preserves the zero coordinate sum modulo $\mathbb Z$. Its inverse is translation by $-[\mathbf p]$.
- $T^nB$ is obtained by the well-founded recursion on $n\in\mathbb N_0$ displayed above. Every step uses a finite union of intersections with closed winner cones followed by translations. Since $\sum_i(x_i+p_i-(e_j)_i)=0$, every output remains in $H_{\boldsymbol0}$. Each point has at least one maximizing coordinate; ties produce a specified finite set of outputs. Thus the power-set map and all its iterates are uniquely determined. A singleton output component is a valid part of this set construction.
- $N_0\in\mathbb N_0$ is chosen to satisfy $C_\delta(N_0)$. The later $M\in\mathbb N_0$ is chosen to satisfy $M\ge N_0$ and $C_B(M)$. Nonempty openness, density of backward orbits, and compactness give a finite cover in each case. If its largest index is $h$, replacing it by $\max(h,N_0)$ gives the stated later contract. For the witness, $N_0=1$ and $M=353$ are both explicitly verified below. The later horizon's defining contract does not contain $F(B,M)$.
- At [lines 4235–4246](../paper/paper.tex#L4235), $k\le M$, $\widehat{\mathbf v}=R_{\mathbf p}^{-k}\pi(\mathbf u)$, and a preimage $\mathbf v\in K^*$ are introduced for $\mathbf u\in K^*$. Backward invariance supplies $\mathbf u\in T^k\{\mathbf v\}$; projection fixes $\pi(\mathbf v)=\widehat{\mathbf v}$. The source's point-style notation $T^k\mathbf v=\mathbf u$ is interpreted with its stated multivalued convention. The neighborhood lemma and injectivity of $\pi$ on $\mathcal N_\delta$ imply $\mathbf v\in B^\circ$. Injectivity follows directly: if $\mathbf x,\mathbf y\in\mathcal N_\delta$ have the same projection, each integer $x_i-y_i$ has absolute value $<2\delta\le1$, hence is zero. These are legitimate existence and unique-lift uses.

The witness's $T^2B$ is consequently a well-defined compact set with an isolated point. The failed requirement is the later assertion $\operatorname{FG}(T^2B)$, not existence or unambiguity of that image. The comparison construction in the later facet remark inherits the lost independence premise discussed in the G2 Note; it does not change the defining contract at the planted step.

<a id="conv-note"></a>
## CONV — Note

**Status: not_violated. Role: diagnostic.** The target makes no changed algebraic or branch-computation claim. Its exact final starting assertion is

$$
K^*=\bigcup_{n=0}^M T^nB,
$$

and its claimed endpoint is that every term of this union is a finite union of good blocks, hence so is $K^*$. The first of these assertions follows from the invariant-set argument. The second is a theorem/property inference from the chosen certificate, audited under MP and G2, rather than a definitional conversion of the union.

The actual projection calculation at [lines 4241–4246](../paper/paper.tex#L4241) expands correctly. Along a branch with winners $i_1,\ldots,i_k$,

$$
\mathbf y=\mathbf v+k\mathbf p-\sum_{j=1}^k\mathbf e_{i_j}
\quad\Longrightarrow\quad
\pi(\mathbf y)=[\mathbf v]+k[\mathbf p]
=R_{\mathbf p}^k(\pi(\mathbf v)).
$$

All branches have that same projection because the subtracted vector is integral. Therefore $\mathbf u\in T^k\{\mathbf v\}$ gives

$$
\pi(\mathbf v)=R_{\mathbf p}^{-k}\pi(\mathbf u)
=\widehat{\mathbf v}\in\pi(B^\circ).
$$

The unique-lift argument then gives $\mathbf v\in B^\circ$, establishing $\mathbf u\in T^kB$. Conversely $B\subseteq K^*$ and $T(K^*)=K^*$ give every $T^nB\subseteq K^*$. These calculations and inclusions establish the displayed union equality with its actual bound $M$.

Here is a complete independent calculation of the counterexample, also agreeing with the [existing exact-arithmetic checker](checker_calculation.py), which runs successfully. Set

$$
m=2,\qquad \epsilon=\frac{\sqrt2}{1000},\qquad
p_1=\frac14+\epsilon,\quad p_2=\frac34-\epsilon,
\quad\delta=\frac12,\quad N_0=1,\quad\rho_{12}=4\epsilon.
$$

Both votes are positive and sum to one. For $a,b\in\mathbb Q$,

$$
a p_1+b p_2=0
\quad\Longrightarrow\quad (a-b)p_1+b=0
\quad\Longrightarrow\quad a=b=0,
$$

using the irrationality of $p_1$. Thus the paper's exact ergodic assumption holds. With $H_{\boldsymbol0}$ identified with $\mathbb R$ by $x\mapsto(x,-x)$, formula (tb4) gives $B=[-2\epsilon,2\epsilon]\subset(-1/2,1/2)=\mathcal N_\delta$.

On the scalar circle, $\widehat{\mathcal N}_{1/2}$ is the complement of $[1/2]$. Its translate omits $[1/2+p_1]$, a different point because $0<p_1<1$. The two sets therefore cover the circle, verifying $C_\delta(1)$.

To compute the iterates, start directly from the vector scores:

$$
(x,-x)+\mathbf p=(x+p_1,1-x-p_1).
$$

If $x+p_1\le1/2$, party 2 is a winner and subtracting $\mathbf e_2$ gives first coordinate $x+p_1$. If $x+p_1\ge1/2$, party 1 is a winner and subtracting $\mathbf e_1$ gives $x+p_1-1$. Both possibilities occur at equality. Thus the [printed formula (T1b)](../paper/paper.tex#L4895) gives, for any scalar set $J$,

$$
T_1(J)=\left((J+p_1)\cap(-\infty,1/2]\right)
\cup\left(\left((J+p_1)\cap[1/2,\infty)\right)-1\right).
$$

The first shifted interval is

$$
B+p_1
=[-2\epsilon+1/4+\epsilon,\ 2\epsilon+1/4+\epsilon]
=[1/4-\epsilon,\ 1/4+3\epsilon].
$$

Since $0<\epsilon<1/12$, this entire interval lies below $1/2$. The second branch has empty domain at this first step, so

$$
TB=[1/4-\epsilon,\ 1/4+3\epsilon].
$$

Both $B$ and $TB$ are nondegenerate compact intervals, hence good blocks in the one-dimensional $H_{\boldsymbol0}$. This verifies $F(B,1)$ and completes admissibility of the selected witness.

For the next image,

$$
\begin{aligned}
TB+p_1
&=[1/4-\epsilon+1/4+\epsilon,\ 1/4+3\epsilon+1/4+\epsilon]\\
&=[1/2,\ 1/2+4\epsilon],\\
(TB+p_1)\cap(-\infty,1/2]&=\{1/2\},\\
\left((TB+p_1)\cap[1/2,\infty)\right)-1
&=[-1/2,\ -1/2+4\epsilon],\\
T^2B&=[-1/2,\ -1/2+4\epsilon]\cup\{1/2\}.
\end{aligned}
$$

The gap between the interval and the point is $1-4\epsilon>0$. Every good block in this dimension is a nondegenerate closed interval. A finite union of such intervals has no isolated point: whichever interval contains a given point also contains other points arbitrarily close to it. Therefore $Q(B,2)$ is false.

The missing stronger condition can also be checked numerically without approximation:

$$
3p_1-p_2
=3(1/4+\epsilon)-(3/4-\epsilon)
=4\epsilon=\rho_{12}.
$$

Hence these widths fail `LTB`'s joint independence hypothesis, while satisfying every property of the revised selection.

Every covering horizon includes the failed second iterate. The normalization of Haar measure is the first-coordinate normalization specified [before Lemma `LC`](../paper/paper.tex#L3151). Consequently $\lambda(\pi(B^\circ))=4\epsilon$, and a cover through $M$ requires

$$
1\le\sum_{k=0}^M\lambda\bigl(R_{\mathbf p}^k(\pi(B^\circ))\bigr)
=(M+1)4\epsilon.
$$

For $M\le175$ the right side is at most

$$
176\cdot4\epsilon=\frac{88\sqrt2}{125}<1,
\qquad
(88\sqrt2)^2=15488<15625=125^2.
$$

Thus every admissible $M$ is at least $176$ and fails $F(B,M)$ at $n=2$.

One can also give a concrete later cover, removing any need to leave its horizon unspecified. Take $M=353$ and the $354$ centers $[kp_1]$, $0\le k\le353$. Traverse their indices by

$$
k\longmapsto
\begin{cases}
k+179,&0\le k\le174,\\
k-175,&175\le k\le353.
\end{cases}
$$

This is addition by $179$ modulo $354$, a single cycle since $\gcd(179,354)=1$. The corresponding positive circular displacements are

$$
d_1=179\epsilon-\frac14\quad(175\text{ occurrences}),
\qquad
d_2=\frac14-175\epsilon\quad(179\text{ occurrences}).
$$

Indeed, $179p_1=45+d_1$ and $-175p_1=-44+d_2$. The exact bounds

$$
\frac1{716}<\epsilon<\frac1{700}
$$

follow by squaring from $\epsilon^2=1/500000$ and $700^2<500000<716^2$. They give $0<d_1,d_2<4\epsilon$. Also

$$
175d_1+179d_2=1.
$$

Thus the traversal visits every center in positive cyclic order during exactly one revolution, with every consecutive gap smaller than the length $4\epsilon$ of the open translated intervals. Those intervals cover the circle, proving $C_B(353)$ exactly. This is an admissible later horizon with $F(B,353)$ false.

No equality in these expansions is erroneous. They establish the correct image and expose the logical discrepancy between the finite certificate and the final claimed range. In the same example the [later manuscript gives $K^*=[-1/2,1/2]$](../paper/paper.tex#L4973). The total union in the target proof equals this good block; it is the assertion that **each individual term** has a good-block decomposition that fails.

## Final classification and comparison with the existing labels

**Final direct labels: MP, G2 (top-level G).** These are two demonstrated proof obligations within the same coordinated defect:

- **MP:** at the final reference to the choice of $B$, the implication supplied by the finite certificate has antecedent $n\le N_0$, which is unestablished and can be false for an index in the enlarged union.
- **G2:** the conditional derivation for an arbitrary witness of $P(B,N_0)$ uses the additional property $F(B,M)$ after selecting a horizon that depends on that witness. The existential-elimination side conditions hold; its conditional derivation fails.

The prior direct classification was G2, as recorded in the [tricker report](tricker_report.md) and [original checker report](checker_report.md). This review retains that finding and adds MP; the [case README](../README.md) reflects the updated classification. Their valid observation that the initial invocation of `LTB` proves existence addresses that invocation; the separate final application of the chosen finite certificate violates the protocol's MP requirement to establish the instantiated antecedent of an earlier result. The [classification standard](../../../protocol/classification.md) permits overlapping labels for demonstrated obligations, so this addition does not posit a second independent planted error.

There is no additional direct G1, DEF, or CONV finding. The finite-cover and invariant-set arguments remain valid for the witness. The proof gap propagates through the invocation of `TB` in `TX` and then [Corollary `CTX`](../paper/paper.tex#L4359); these later uses supply no stronger property for the chosen block. The exact witness verifies $P(B,1)$, $C_B(353)$, failure of $Q(B,2)$, and failure of $F(B,M)$ for every admissible covering horizon. **No unresolved mathematical issue affects this classification.**
