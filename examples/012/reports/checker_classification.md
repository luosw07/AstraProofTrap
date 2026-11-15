# 012: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow, informed by the complete source and the existing construction/checker materials. It is a classification audit rather than an original workflow report or a blind reviewer run. The mathematical findings below use the [classification standard](../../../protocol/classification.md), the [modified manuscript](../paper/paper.tex), the [original manuscript](../original/paper.tex), the [exact mutation](../mutation.diff), the [construction report](tricker_report.md), the three existing [checker](checker_report.md) [reports](checker_report_02.md) [and their mathematical analysis](checker_report_03.md), and the supplied [calculation](checker_calculation.cjs). Their labels were checked against the actual construction and independently recomputed witness.

## Exact target and actual assumptions

The operative mutation is the unmatched-demand rule in Appendix G.3, [lines 4263–4266](../paper/paper.tex#L4263): an unmatched demand $u$ may choose **any** edge of $\mathcal E_u$, instead of its own connector $c_{S_u}$. The [overview](../paper/paper.tex#L1304) makes the same change. The original [lines 4270–4280](../original/paper.tex#L4270), which confined paid nonremovable-edge increases to edges joining two matched vertex demands, are removed. Comparing the complete source files gives exactly the two hunks in the supplied mutation.

The relevant assumptions are those stated [throughout Appendix G](../paper/paper.tex#L3630) and in [its theorem](../paper/paper.tex#L3744): $G=(V,E)$ is a finite simple, $4$-regular, $4$-vertex-connected graph, $n=|V|$, and $T$ is any DFS tree rooted at $r\in V$. The graph and DFS hypotheses in the separate [general-graph analysis](../paper/paper.tex#L5463) concern a different construction. In particular, the quartic construction uses neither an extreme subtour support nor a greedy DFS restriction.

For a tree edge $uv$ directed from parent to child, the [DFS definitions](../paper/paper.tex#L2735) are

$$
I(u,v)=\{uw\in E\setminus E(T):w\in V(T_v)\},\qquad
S(u,v)=\{uv\}\cup I(u,v)\quad\text{when }I(u,v)\ne\varnothing.
$$

The stars form $\mathcal S$; $R=\bigcup_{S\in\mathcal S}S$ and $N=E\setminus R$. Splitting the center $u$ of each star $S$ introduces $z_S$, replaces $uw\in S$ by $\operatorname{rep}(uw)=z_Sw$, and adds $c_S=uz_S$. An edge of $N$ keeps its endpoints. Write $H^\circ=(W,A^\circ)$ for this loopless auxiliary graph. The stars are edge-disjoint, so every representative is specified uniquely.

For any loopless graph $J=(W_J,E_J)$ and $y\in\mathbb R^{E_J}$, define the following notation for the manuscript's actual constraints:

$$
\begin{aligned}
\operatorname{Feas}_J(y)\quad\Longleftrightarrow\quad
&\bigl[\forall a\in E_J\ (0\le y_a\le1)\bigr]\\
&\land\Bigl[\forall X\subseteq W_J\ \forall F\subseteq E_J\,
\Bigl(F\subseteq\delta_J(X)\ \land\ |\delta_J(X)\setminus F|\text{ odd}\Bigr)\\
&\hspace{35mm}\Longrightarrow
\sum_{a\in\delta_J(X)\setminus F}y_a+
\sum_{a\in F}(1-y_a)\ge1\Bigr].
\end{aligned}
$$

Thus $\operatorname{Feas}_{H^\circ}(y)$ means $y\in\mathcal P^\circ$, by [the displayed nonloop polytope](../paper/paper.tex#L2344). The alternative parity condition $|\delta_J(X)|+|F|$ odd in [the quartic cut goal](../paper/paper.tex#L4299) is identical, since its difference from $|\delta_J(X)\setminus F|$ is $2|F|$.

The [initial vector](../paper/paper.tex#L3763) assigns $1/4$ to every tree-edge representative and nonroot connector, $1/2$ to the back-edge representative in a nonroot size-two star, $3/4$ to the back-edge representatives in a size-three or root star, and $1$ to the root connector. Let $j(v)$ be the number of DFS children and $i(v)$ the number of back edges from proper descendants to $v$. Then

$$
B_2=\{v\ne r:j(v)=2,\ i(v)=1\},\qquad
\mathcal U=\{u\in B_2:\operatorname{par}(u)u\in N\}.
$$

The free changes raise the representatives of removable parent edges of $B_2$ vertices to $1/2$. Triangle demands $\mathcal D$ are the [specified configuration](../paper/paper.tex#L4013) with $u\in B_2$, $p=\operatorname{par}(u)$, a size-two star $S_p=\{pu,pw\}$, and a size-two star at the other child $w$ of $u$, which has exactly one DFS child and one entering back edge. Consequently $\mathcal D\cap\mathcal U=\varnothing$. The [boundary sets and correction graph](../paper/paper.tex#L4242) are

$$
\mathcal E_u=
\begin{cases}
\{\operatorname{rep}(pu),c_{S_u},\operatorname{rep}(uw)\},&u\in\mathcal U,\\
\{c_{S_p},c_{S_u},c_{S_w}\},&u\in\mathcal D,
\end{cases}
\qquad
uv\in E(K)\Longleftrightarrow
u\ne v\ \land\ \mathcal E_u\cap\mathcal E_v\ne\varnothing.
$$

Here $w$ is the child whose subtree contains no back edge ending at $u$, and $V(K)=\mathcal U\mathbin{\dot\cup}\mathcal D$. Fix a maximum matching $M$ of $K$. A selection $s$ specifies an edge in $\mathcal E_u\cap\mathcal E_v$ for each $uv\in M$, and an edge in $\mathcal E_u$ for each unmatched $u$. Repeatedly selected edges are raised only once. Denote the resulting vector by $y_s=\bar x^{(s)}$.

The first false assertion is [lines 4309–4310](../paper/paper.tex#L4309): every degree-two vertex of $H^\circ$ has both incident coordinates $1/4$. Its consequences occur in the [suppression calculation](../paper/paper.tex#L4377), the [reduced vertex-cut argument](../paper/paper.tex#L4498), the [final-vector proposition](../paper/paper.tex#L4589), and the [tour-bound invocation](../paper/paper.tex#L5193). The later [figure caption](../paper/paper.tex#L4961) illustrates own-connector choices, which remain permitted choices; it supplies no restriction on the explicit arbitrary-edge rule.

### Verified admissible witness

Take $V=\{0,1,\ldots,12\}$ and the following complete edge list, with every edge written once:

```text
0-1  0-5  0-9  0-12
1-2  1-8  1-11
2-3  2-5  2-9
3-4  3-10 3-12
4-5  4-10 4-11
5-6
6-7  6-11 6-12
7-8  7-9  7-10
8-9  8-10
11-12
```

There are $26$ distinct nonloop edges and every vertex has degree four. I independently checked connectivity after deleting each set of zero, one, two, or three vertices: respectively $1,13,78,286$ checks, all connected. This verifies the required $4$-vertex-connectivity. Increasing-neighbor DFS rooted at $0$ has preorder $0,1,\ldots,12$ and parent array

```text
[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 6, 11].
```

Reconstructing the stars directly from descendant membership gives the following sets. In this witness, $S_v$ denotes the unique star centered at $v$, including the size-three stars; $z_v=z_{S_v}$ and $c_v=c_{S_v}$.

| Center | Star edges |
|---|---|
| $0$ | $\{(0,1),(0,5),(0,9),(0,12)\}$ |
| $1$ | $\{(1,2),(1,8),(1,11)\}$ |
| $2$ | $\{(2,3),(2,5),(2,9)\}$ |
| $3$ | $\{(3,4),(3,10),(3,12)\}$ |
| $4$ | $\{(4,5),(4,10),(4,11)\}$ |
| $6$ | $\{(6,11),(6,12)\}$ |
| $7$ | $\{(7,8),(7,9),(7,10)\}$ |

The remaining edges are

$$
N=\{(5,6),(6,7),(8,9),(8,10),(11,12)\}.
$$

Vertex $6$ has children $7,11$ and the sole entering back edge $(6,12)$. Vertex $8$ has two children and no entering back edge. These facts give $B_2=\mathcal U=\{6\}$ and $\mathcal D=\varnothing$. There are no free changes. The graph $K$ has one isolated vertex, so $M=\varnothing$ is its unique maximum matching. Its sole demand has boundary

$$
\mathcal E_6=\{\operatorname{rep}(5,6),c_6,\operatorname{rep}(6,7)\}.
$$

Let $s_*$ select $a=\operatorname{rep}(6,7)$ and raise it to $1/2$. The demand at $6$ is satisfied because its boundary sum is $1/4+1/4+1/2=1$. Vertex $7$ centers a size-three star and has degree two in $H^\circ$, with boundary $\{a,b\}$ where $b=c_7$. The actual values are

$$
(y_{s_*}(a),y_{s_*}(b))=(1/2,1/4).
$$

For $X=\{7\}$ and $F=\{a\}$, the complement of $F$ in the cut has one edge, and

$$
y_{s_*}(\delta_{H^\circ}(X)\setminus F)+|F|-y_{s_*}(F)
=y_{s_*}(b)+1-y_{s_*}(a)
=\frac14+1-\frac12=\frac34<1.
$$

Hence this allowed output is outside $\mathcal P^\circ$. The original selection raises $c_6$ instead and leaves the incident pair at $7$ equal to $(1/4,1/4)$.

The auxiliary graph has $20$ vertices. I also independently minimized each cut's Blossom expression by dynamic programming over the parity of $|C\setminus F|$, using integer coordinates in units of $1/4$. For each crossing edge the two choices add $4y_a$ and toggle parity, or add $4-4y_a$ and preserve parity. Checking all $2^{19}-1=524{,}287$ nontrivial shores with $z_7$ outside gives minimum $1$ and zero violated shores for the original selection, and minimum $3/4$ and four violated shores for $s_*$. The latter shores are $\{7\}$, $\{0,7\}$, $\{6,7\}$, and $\{0,6,7\}$. The supplied [checker calculation](checker_calculation.cjs) gives the same results.

## Five-rule audit summary

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | downstream | [4365–4397](../paper/paper.tex#L4365), [4595–4605](../paper/paper.tex#L4595), [5194–5207](../paper/paper.tex#L5194) | The suppression premise and later certificate antecedent fail because of the broadened selection family. [Full Note](#mp--note). |
| G1 | violated | direct | [4263–4269](../paper/paper.tex#L4263), [4309–4310](../paper/paper.tex#L4309), [4591–4592](../paper/paper.tex#L4591) | The retained selected-object argument does not establish its conclusion for every newly allowed selection. [Full Note](#g1--note). |
| G2 | not_violated | none | [4260–4269](../paper/paper.tex#L4260), [5193–5212](../paper/paper.tex#L5193) | Choices remain scoped parameters; the genuine feasible-certificate sufficiency implication has a witness-independent conclusion. [Full Note](#g2--note). |
| DEF | not_violated | none | [4242–4269](../paper/paper.tex#L4242), [4310–4319](../paper/paper.tex#L4310) | The selections, output vector, reduced graph and reduced vector are specified; their later asserted feasibility/preservation properties fail. [Full Note](#def--note). |
| CONV | violated | downstream | [4378–4383](../paper/paper.tex#L4378), [4498–4503](../paper/paper.tex#L4498) | The actual cut contributions differ from the inherited common-value substitutions. The modified cost computations are correct. [Full Note](#conv--note). |

Here “downstream” records a failed obligation whose erroneous premise is the earlier direct G1 failure. Only the demonstrated direct violation enters the final label set.

## MP — Note

**Status: violated. Role: downstream.** The rule being checked is

$$
\frac{\Gamma\vdash A\qquad\Gamma\vdash A\to B}{\Gamma\vdash B}.
$$

There is no theorem citation in the changed instruction itself: it specifies which coordinate to raise. Its later proof uses both common-value suppression and the tour-certificate theorem. Those applications can be instantiated precisely.

Let $\Gamma_{\mathrm{MP}}$ consist of the following valid background data: the finite simple quartic $4$-vertex-connected graph $G$; its rooted DFS tree $T$; the star system defined above, whose removability follows from [the DFS lemma](../paper/paper.tex#L2851); the associated $H^\circ$, initial vector, $B_2$, $\mathcal U$, $\mathcal D$, boundary sets and $K$; a maximum matching $M$; and a selection $s$ satisfying the modified boundary-membership requirements. The free changes and the set of selected paid edges determine $y_s$ exactly as specified in the DEF Note. Also available are the genuine nonloop-polytope description and the general tour-certificate theorem. The false degree-two invariant and the final-vector proposition are **not** added to this valid background as established facts.

First consider [the reduction proof](../paper/paper.tex#L4377). For each original size-three-star center $v$, extend the notation $S_v$ to denote its unique star, let $a_v$ be its parent-edge representative, and put $b_v=c_{S_v}$. These are exactly its two incident edges in $H^\circ$. The degree-two vertices are precisely these centers: other original nonroot vertices have degree at least three, auxiliary vertices have degree at least three, and the root has degree one. Define

$$
I(y):=\forall v\in W\;
\Bigl(\deg_{H^\circ}(v)=2\Longrightarrow
\forall a\in\delta_{H^\circ}(v)\ (y_a=1/4)\Bigr).
$$

Let $R_Q(y)$ be the reduced vector obtained by the manuscript's formula: assign $1/4$ to each replacement edge and retain $y$ on unchanged edges, after deleting the root and its connector. A symbolic reconstruction of the reduction's printed reasoning, preserving its actual common-value hypothesis, is

$$
\begin{aligned}
A_{\mathrm{red}}(y)
&:=\bigl[\forall a\in A^\circ\ (0\le y_a\le1)\bigr]
\land[y_{c_{S_r}}=1]\land I(y),\\
B_{\mathrm{red}}(y)
&:=\bigl(\operatorname{Feas}_{H^\circ}(y)
\Longleftrightarrow\operatorname{Feas}_Q(R_Q(y))\bigr),\\
&A_{\mathrm{red}}(y)\Longrightarrow B_{\mathrm{red}}(y).
\end{aligned}
$$

This is a reconstruction of the local argument, not an additional assumption of the modified construction. Its substitution is $y=y_s$, with $Q$ determined by the fixed $G,T$. The manuscript claims $C_{\mathrm{red}}=B_{\mathrm{red}}(y_s)$ in [lines 4367–4369](../paper/paper.tex#L4367). Box constraints and the root coordinate are established; $I(y_s)$ is the first failed antecedent component. At $s=s_*$ and $v=7$, it would require $y_{s_*}(a)=1/4$, whereas the procedure sets it to $1/2$. The local common-value implication therefore cannot be applied to this selected vector. The CONV Note computes the failed transport explicitly. Both feasibility statements in the printed biconditional are false on this particular witness; the identified failure of its proof is the cut-transport premise.

For the final tour application, separate the algebraic expression from its feasible domain. Define on all of $\mathbb R^{A^\circ}$

$$
\Psi(y):=n-1+y(N_H)+
\sum_{S\in\mathcal S}\max\{y_{c_S},k_S-1-y(S_H)\}.
$$

On $\mathcal P^\circ$, this equals the manuscript's $\Phi_{G,\mathcal S}(y)$ by [the projected objective formula](../paper/paper.tex#L2370). Write $L_{\mathrm{SR}}$ for its $\mathrm{StarReconnectionLP}_{\mathrm{OPT}}(G,\mathcal S)$. The [certificate theorem](../paper/paper.tex#L774) and [its corollary](../paper/paper.tex#L2401), together with minimization over the feasible region, give the available implication

$$
\forall y\in\mathbb R^{A^\circ}\;
\left(\operatorname{Feas}_{H^\circ}(y)
\Longrightarrow
\operatorname{tsp}(G)\le L_{\mathrm{SR}}\le\Psi(y)\right).
$$

The substitution is again $y=y_s$. Here the instantiated antecedent is

$$
A_{\mathrm{tour}}=
\bigl[\forall a\in A^\circ\ (0\le(y_s)_a\le1)\bigr]
\land
\Bigl[\forall X\subseteq W\ \forall F\subseteq\delta_{H^\circ}(X)\;
\bigl(|\delta_{H^\circ}(X)\setminus F|\text{ odd}
\Longrightarrow
y_s(\delta_{H^\circ}(X)\setminus F)+|F|-y_s(F)\ge1\bigr)\Bigr],
$$

and $B_{\mathrm{tour}}$ is $\operatorname{tsp}(G)\le L_{\mathrm{SR}}\le\Psi(y_s)$. The conclusion actually exported at [lines 5202–5207](../paper/paper.tex#L5202) is

$$
C_{\mathrm{tour}}:
\operatorname{tsp}(G)\le L_{\mathrm{SR}}\le\Psi(y_s)
\le\frac54n-\frac12+\frac14\rho
\le\frac{13}{10}n-\frac35.
$$

The numerical inequalities following $B_{\mathrm{tour}}$ are valid, as calculated below. The failure is the unavailable antecedent $A_{\mathrm{tour}}$, whose asserted provenance is [the final-vector proposition](../paper/paper.tex#L5194). The witness falsifies its cut component at $(X,F)=(\{7\},\{\operatorname{rep}(6,7)\})$. The theorem is accurately stated, its graph and star hypotheses hold, and its consequent has not been strengthened by changing a qualifier. Its attempted use inherits the unsupported universal feasibility assertion from G1.

In sequent form, the actual background supplies

$$
\Gamma_{\mathrm{MP}}\vdash A_{\mathrm{tour}}\to B_{\mathrm{tour}},
\qquad
\Gamma_{\mathrm{MP}},A_{\mathrm{tour}}\vdash B_{\mathrm{tour}}.
$$

The missing obligation is $\Gamma_{\mathrm{MP}}\vdash A_{\mathrm{tour}}$: the admissible instance $G,T,M,s_*$ satisfies this background and falsifies that antecedent. This pinpoints the failed premise of the printed application without treating the final tour bound itself as the counterexample's conclusion.

Similarly, [lines 4596–4605](../paper/paper.tex#L4596) use the reduced vertex-cut lemma to assert $\operatorname{Feas}_Q(R_Q(y_s))$ before applying the reduction. For $s_*$, the reduced singleton cut at $6$ still has sum $3/4$, so that intermediate antecedent also fails. These are downstream applications with false premises, rather than additional direct labels at the changed choice rule.

## G1 — Note

**Status: violated. Role: direct.** The rule is

$$
\frac{\Gamma\vdash A\to B(x)}{\Gamma\vdash A\to\forall x\,B(x)},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(A).
$$

The universally generalized variable at issue is the **repair selection**, not merely a vertex or cut shore. To specify its domain, let $U_M$ be the unmatched demands and use the tagged finite index set

$$
J_M=(\{0\}\times M)\mathbin{\dot\cup}(\{1\}\times U_M).
$$

A candidate selection is a function $s:J_M\to A^\circ$. Its actual modified range predicate is

$$
\begin{aligned}
D_{\mathrm{new}}(s):={}&
\bigl[\forall uv\in M\;
s(0,uv)\in\mathcal E_u\cap\mathcal E_v\bigr]\\
&\land\bigl[\forall u\in U_M\;
s(1,u)\in\mathcal E_u\bigr].
\end{aligned}
$$

Define the removed restriction and the old range by

$$
H_{\mathrm{own}}(s):=\forall u\in U_M\;
s(1,u)=c_{S_u},\qquad
D_{\mathrm{old}}(s):=D_{\mathrm{new}}(s)\land H_{\mathrm{own}}(s).
$$

The free changes do not depend on $s$. Let

$$
P(s):=I(y_s)\land\operatorname{Feas}_{H^\circ}(y_s),
$$

where both predicates were fully expanded above. This includes the first universal assertion about degree-two vertices and the later universal cut conclusion.

For an explicit G1 presentation, take $\Gamma_0$ to contain the fixed finite graph/tree/edge domains, the definitions of $I(u,v)$, $\mathcal S$, $H^\circ$, $x^{\mathrm{init}}$, demands, $K$, $J_M$, $y_s$, and the valid general graph/join facts used by the proof. The definition of the function $s\mapsto y_s$ binds its argument; it is not an open hypothesis about a chosen $s$. Let

$$
\begin{aligned}
A:= {}&G\text{ is simple, }4\text{-regular and }4\text{-vertex-connected}\\
&\land\ T\text{ is a DFS tree of }G\text{ rooted at }r\in V\\
&\land\ M\subseteq E(K)\text{ is a matching and}
\ \forall M'\subseteq E(K)\\
&\hspace{12mm}\bigl(M'\text{ is a matching}\Longrightarrow |M'|\le|M|\bigr),\\
B(s):={}&D_{\mathrm{new}}(s)\Longrightarrow P(s).
\end{aligned}
$$

Then $\operatorname{FV}(\Gamma_0)\cup\operatorname{FV}(A)$ contains only the fixed background parameters, in particular $G,T,r,M$ and their defined data, and excludes $s$. The assertion about every output of the modified procedure has the form

$$
\Gamma_0\vdash
A\Longrightarrow\forall s:J_M\to A^\circ\;
\bigl(D_{\mathrm{new}}(s)\Longrightarrow P(s)\bigr).
$$

Here is the concrete pre-generalization argument that supports the original invariant. Choose $s$ and assume $A$, $D_{\mathrm{new}}(s)$ and $H_{\mathrm{own}}(s)$. For an arbitrary $v$ with $\deg_{H^\circ}(v)=2$, the structural classification gives a size-three star at $v$, one DFS child, and incident edges $a_v,b_v$ as in the MP Note. Both start at $1/4$.

1. A free parent-edge increase requires its child endpoint to lie in $B_2$, so it cannot change $a_v$.
2. Under $H_{\mathrm{own}}(s)$, an unmatched demand changes only its own size-two-star connector. It changes neither $a_v$ nor $b_v$.
3. A matched choice in $N_H$ belongs to two vertex-demand boundaries, so both endpoints lie in $\mathcal U\subseteq B_2$. It cannot change a parent edge whose child $v$ has one DFS child. A matched connector belongs to a size-two star, so it cannot be $b_v$.

Thus $(y_s)_{a_v}=(y_s)_{b_v}=1/4$. Discharge the condition on $v$ and generalize $v$ to obtain $I(y_s)$. This is the endpoint argument printed in the [original selection passage](../original/paper.tex#L4270). The subsequent common-value reduction and small-cut proof use this invariant to derive the feasibility part of $P(s)$.

The resulting supported conditional has the restriction still present:

$$
\Gamma_0\vdash A\Longrightarrow
\forall s\;
\bigl((D_{\mathrm{new}}(s)\land H_{\mathrm{own}}(s))\Longrightarrow P(s)\bigr).
$$

In that derivation, $H_{\mathrm{own}}(s)$ has free variables $s,G,T,M$ through the connector and unmatched-demand definitions. Proper conditional introduction discharges it **into** the range predicate. Removing it from the conclusion is not a valid discharge. If it were retained as an open assumption while quantifying $s$, then $s\in\operatorname{FV}(H_{\mathrm{own}}(s))$ would also violate the usual variable condition. The modified text, however, does not explicitly assume $H_{\mathrm{own}}(s)$: its actual failure is that the required pre-generalization derivation

$$
\Gamma_0\vdash A\to
\bigl(D_{\mathrm{new}}(s)\to P(s)\bigr)
$$

has no valid endpoint argument for all selected objects in its declared range. This is a failed derivation and range check, not an invented eigenvariable defect.

The witness supplies the precise failure: $D_{\mathrm{new}}(s_*)$ holds, $H_{\mathrm{own}}(s_*)$ fails because $s_*(1,6)=\operatorname{rep}(6,7)\ne c_6$, and both $I(y_{s_*})$ and $\operatorname{Feas}_{H^\circ}(y_{s_*})$ fail. The selected object's needed restriction has been lost at the changed rule and first reused at [the degree-two assertion](../paper/paper.tex#L4309).

The cut quantifiers also have explicit scopes. For fixed $s$, one must derive

$$
\forall X\subseteq W\ \forall F\subseteq A^\circ\;
\Bigl(F\subseteq\delta_{H^\circ}(X)\land
|\delta_{H^\circ}(X)\setminus F|\text{ odd}
\Longrightarrow y_s(\delta_{H^\circ}(X)\setminus F)+|F|-y_s(F)\ge1\Bigr).
$$

The shore and subset conditions must be discharged before generalizing $X,F$; the fixed parameters $G,T,M,s$ may remain open. Nothing about the witness relies on an illicit choice of $X$ or $F$: it uses one explicitly allowed pair. The direct G1 finding concerns the unjustified enlargement from $D_{\mathrm{old}}$ to $D_{\mathrm{new}}$, demonstrated by the lost pre-generalization premise, as well as by the false quantified result.

## G2 — Note

**Status: not_violated. Role: none.** The rule is

$$
\frac{\Gamma\vdash A(x)\to B}
{\Gamma\vdash(\exists x\,A(x))\to B},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(B).
$$

At [the changed rule](../paper/paper.tex#L4263), the operation is coordinate assignment after choosing an edge. For fixed $G,T,M,u$, a permissible $e\in\mathcal E_u$ determines the updated vector $z^{(e)}$ by setting its $e$-coordinate to $1/2$ and retaining the other current coordinates. The chosen name is retained in the construction and its resulting vector. For the witness, $e=\operatorname{rep}(6,7)$ and $z^{(e)}=y_{s_*}$. This is an arbitrary parameter in a claimed correctness argument; it does not export an edge or vector as independent of that choice. The direct claim audited in G1 is $\forall s(D_{\mathrm{new}}(s)\to\operatorname{Feas}_{H^\circ}(y_s))$.

The genuine existential sufficiency argument later used in the tour proof has the following fully instantiated form. Fix $G,T,\mathcal S,H^\circ$ as above and put $\beta_n=13n/10-3/5$. Let $\Gamma_2$ contain precisely these fixed graph assumptions, the definitions of $\Psi$ and $\mathcal P^\circ$, and the valid certificate theorem [stated here](../paper/paper.tex#L774) and [proved through the corollary](../paper/paper.tex#L2401). Its witness variable $z$ ranges over $\mathbb R^{A^\circ}$. Define

$$
\begin{aligned}
A_2(z):={}&\bigl[\forall a\in A^\circ\ (0\le z_a\le1)\bigr]\\
&\land\Bigl[\forall X\subseteq W\ \forall F\subseteq\delta_{H^\circ}(X)\;
\bigl(|\delta_{H^\circ}(X)\setminus F|\text{ odd}
\Longrightarrow z(\delta_{H^\circ}(X)\setminus F)+|F|-z(F)\ge1\bigr)\Bigr]\\
&\land\left[n-1+z(N_H)+\sum_{S\in\mathcal S}
\max\{z_{c_S},k_S-1-z(S_H)\}\le\beta_n\right].
\end{aligned}
$$

For $m\in\mathbb N_0^E$, let $\operatorname{Tour}_G(m)$ mean that the multigraph with $m_e$ copies of each edge $e$ spans $V$, is connected, and has even degree $\sum_{e\ni v}m_e$ at every vertex $v$. Its length is $\ell(m)=\sum_{e\in E}m_e$. The desired witness-independent conclusion is

$$
B_2^{\mathrm{tour}}:=\exists m\in\mathbb N_0^E\;
\bigl(\operatorname{Tour}_G(m)\land\ell(m)\le\beta_n\bigr).
$$

An explicit existential-elimination subderivation is

$$
\begin{array}{ll}
1.&[\exists z\in\mathbb R^{A^\circ}\ A_2(z)]^{\alpha},\\
2.&\quad[A_2(z^\dagger)]^{\gamma}
\quad(z^\dagger\text{ fresh}),\\
3.&\quad\operatorname{Feas}_{H^\circ}(z^\dagger),\quad
\Psi(z^\dagger)\le\beta_n,\\
4.&\quad\exists m\in\mathbb N_0^E\;
\bigl(\operatorname{Tour}_G(m)\land\ell(m)\le\Psi(z^\dagger)\bigr)
\quad\text{(certificate theorem)},\\
5.&\qquad[\operatorname{Tour}_G(m^\dagger)\land
\ell(m^\dagger)\le\Psi(z^\dagger)]^{\eta}
\quad(m^\dagger\text{ fresh}),\\
6.&\qquad\operatorname{Tour}_G(m^\dagger)\land\ell(m^\dagger)\le\beta_n,\\
7.&\qquad B_2^{\mathrm{tour}}\quad(\exists\text{-introduction}),\\
8.&\quad B_2^{\mathrm{tour}}\quad(\exists\text{-elimination, discharge }\eta),\\
9.&B_2^{\mathrm{tour}}\quad(\exists\text{-elimination, discharge }\gamma),\\
10.&(\exists z\ A_2(z))\to B_2^{\mathrm{tour}}
\quad(\to\text{-introduction, discharge }\alpha).
\end{array}
$$

Every quantity that depends on $z^\dagger$ remains within its scope. In the supplied certificate proof these include the loop lift

$$
\widetilde z_{\ell_S}
=\min\left\{1,\frac{k_S+1-z^\dagger(S_H)-z^\dagger_{c_S}}2\right\},
$$

its join decomposition, the resulting tours, and their intermediate bound $\Psi(z^\dagger)$. The exported formula mentions only $G$ and $\beta_n$. Thus neither $z^\dagger$ nor $m^\dagger$ is free in the remaining background or exported conclusion; their dependent constructions are not exported as fixed objects.

The modified procedure establishes the box and cost parts for $y_{s_*}$ but fails the cut part of $A_2(y_{s_*})$. That prevents using this output as a feasible certificate at the earlier step. The valid G2 implication just displayed requires exactly that cut part; it neither discards a witness property nor reverses a quantifier order. The difference between $\exists s\,D_{\mathrm{new}}(s)$ and $\exists s\,(D_{\mathrm{new}}(s)\land\operatorname{Feas}_{H^\circ}(y_s))$ is the missing feasibility property. The manuscript's failed attempt to supply it is the universal selected-object argument already identified under G1, not an additional existential elimination error.

## DEF — Note

**Status: not_violated. Role: none.** The objects introduced at [the selection step](../paper/paper.tex#L4242) are the boundary sets $\mathcal E_u$, the finite simple graph $K$, a maximum matching $M$, the selected edges, and the output vector $\bar x$. The later [reduction](../paper/paper.tex#L4310) introduces $Q$ and $\bar x^Q$. Their actual defining requirements can be checked separately from the feasibility proposition.

The map $\operatorname{rep}:E\to A^\circ$ is the explicit injective edge map given above. Each edge belongs to at most one star, and each star has a newly named auxiliary vertex, so there is no choice of representative. For $u\in B_2$, exactly one of its two child subtrees contains the unique entering back edge; hence its other child $w$ is uniquely specified. In a vertex demand, its parent and other-child edges belong to $N$, and its own connector belongs to a size-two star. In a triangle demand, the three connectors come from the three specified size-two stars. In both cases $\mathcal E_u$ consists of three distinct existing edges and has type $\mathcal P(A^\circ)$. The formula defining adjacency makes $K$ a finite simple graph on $\mathcal U\mathbin{\dot\cup}\mathcal D$.

A maximum matching exists because the set of matchings of finite $K$ is finite and nonempty. It need not be unique, and the manuscript does not require uniqueness. For every matched pair its shared boundary is nonempty by the definition of $E(K)$; every unmatched boundary has three elements. Consequently the finite set of selections satisfying $D_{\mathrm{new}}$ is nonempty for each chosen $M$.

For a completely explicit output formula, define

$$
L:=\{\operatorname{rep}(\operatorname{par}(u)u):
u\in B_2,\ \operatorname{par}(u)u\in R\},\qquad
P_s:=\{s(j):j\in J_M\}.
$$

Then the construction is the function

$$
\begin{aligned}
\mathcal C_{\mathrm{new}}(G,T,M)&\longrightarrow\mathbb R^{A^\circ},\\
s&\longmapsto y_s,\qquad
(y_s)_a=
\begin{cases}
1/2,&a\in L\cup P_s,\\
x^{\mathrm{init}}_a,&a\notin L\cup P_s.
\end{cases}
\end{aligned}
$$

Here $\mathcal C_{\mathrm{new}}$ is the set of functions satisfying $D_{\mathrm{new}}$. Every coordinate in $L\cup P_s$ initially equals $1/4$. The set $L$ consists of removable tree-edge representatives, whereas $P_s$ consists of nonremovable representatives or nonroot connectors. Thus the free and paid types are disjoint; repeated paid choices are resolved by the set $P_s$. This gives a unique, order-independent vector for every specified $M,s$, with values in $\{1/4,1/2,3/4,1\}$. The codomain at this definition is a coordinate space; membership in $\mathcal P^\circ$ is the separate assertion [in the later proposition](../paper/paper.tex#L4589).

On the witness, $L=\varnothing$, $P_{s_*}=\{\operatorname{rep}(6,7)\}$, and the formula gives exactly $(y_{s_*})_{\operatorname{rep}(6,7)}=1/2$ and $(y_{s_*})_{c_7}=1/4$. The output exists uniquely and meets the stated coordinate-update instructions. Its violation of the later Blossom requirement is therefore a failure of the universal correctness claim.

The reduced objects are equally concrete. Each degree-two vertex is an original size-three-star center $v$ with two edges $a_v=\bar p v$ and $b_v=vz_{S_v}$. Suppression replaces this path by $q_v=\bar p z_{S_v}$, labeled by the parent edge. These degree-two centers are not adjacent to one another in $H^\circ$: an edge from one such center to its DFS child has already been moved to its auxiliary vertex. Consequently their two-edge paths are edge-disjoint and suppression introduces no order ambiguity. Delete the degree-one root and $c_{S_r}$. The resulting graph $Q$ is, after relabeling the surviving auxiliary vertices of root and size-three stars, exactly $G$ split only at size-two stars, which also establishes its simplicity.

The manuscript defines a unique map $R_Q:\mathbb R^{A^\circ}\to\mathbb R^{E(Q)}$ by

$$
(R_Q(y))_{q_v}=1/4\quad\text{on a replacement edge},\qquad
(R_Q(y))_a=y_a\quad\text{on an unchanged edge}.
$$

It is an explicit assignment even when the values on $a_v,b_v$ differ. For the witness, the suppressed centers are $1,2,3,4,7$; deleting the root leaves $Q$ with $14$ vertices and $27$ edges. The replacement for the path $6-7-z_7$ has value $1/4$. Thus

$$
\delta_Q(\{6\})=\{\operatorname{rep}(5,6),c_6,q_7\},
\qquad R_Q(y_{s_*})|_{\delta_Q(\{6\})}=(1/4,1/4,1/4).
$$

The definition succeeds, while the claimed preservation of repaired cuts fails. The asserted common value is a premise of that preservation proof, not an unresolved choice in the definition of $R_Q$.

Finally, the projected objective $\Phi_{G,\mathcal S}$ is [defined on $\mathcal P^\circ$](../paper/paper.tex#L2366) as a minimum over loop extensions. Its algebraic formula $\Psi$ is a well-defined expression on all coordinate vectors. For $y_{s_*}$ the extension fiber in $P_{\mathcal R}$ is empty: loops cross no cut, so they cannot alter the violated cut at $7$. The final proof's use of $\Phi(y_{s_*})$ rests on its earlier false membership assertion. The correctly computed number $16$ below is the value of $\Psi$, and the relevant failed obligation is the inherited certificate premise described under MP. There is no direct failure to specify the introduced vector or graph.

## CONV — Note

**Status: violated. Role: downstream.** There is a literal discrepancy in the later cut computations under the modified procedure. Its provenance is the false common-value invariant; the newly inserted cost sentence and the objective arithmetic are correct. This distinction separates a downstream computational consequence from the direct G1 label.

The manuscript's [suppression proof](../paper/paper.tex#L4378) says that crossing one incident edge gives the same contribution as the replacement edge, and that when both incident edges cross and exactly one is in $F$, their contribution is $1/4+3/4=1$. For the witness, write $a=\operatorname{rep}(6,7)$ and $b=c_7$. The exact starting expression and its definitional expansion for $X=\{7\}$, $F=\{a\}$ are

$$
\begin{aligned}
y_{s_*}(\delta_{H^\circ}(X)\setminus F)+|F|-y_{s_*}(F)
&=\sum_{e\in\{b\}}(y_{s_*})_e+
\sum_{e\in\{a\}}\bigl(1-(y_{s_*})_e\bigr)\\
&=(y_{s_*})_b+1-(y_{s_*})_a\\
&=\frac14+1-\frac12\\
&=\frac34.
\end{aligned}
$$

The printed endpoint $1/4+3/4=1$ replaces $1-(y_{s_*})_a$ by $3/4$. That replacement is the first incorrect evaluation here: the coordinate update gives $1-(y_{s_*})_a=1/2$. The addition $1/4+3/4=1$ itself is correct. For arbitrary incident values $p=y_a$, $q=y_b$, the two allowed two-edge-cut expressions are $q+1-p$ and $p+1-q$. Their simultaneous lower bounds by $1$ require $p=q$. Under the original common-value premise $p=q=1/4$, both evaluate to $1$ exactly.

The one-crossing-edge identity fails as well. Take $X=\{6\}$ and $F=\varnothing$ in $H^\circ$. Its three-edge cut has odd cardinality, and

$$
\begin{aligned}
y_{s_*}(\delta_{H^\circ}(\{6\}))
&=(y_{s_*})_{\operatorname{rep}(5,6)}+(y_{s_*})_{c_6}+(y_{s_*})_a\\
&=\frac14+\frac14+\frac12=1.
\end{aligned}
$$

After suppression the corresponding shore in $Q$ has boundary $\{\operatorname{rep}(5,6),c_6,q_7\}$ and

$$
\begin{aligned}
R_Q(y_{s_*})(\delta_Q(\{6\}))
&=(y_{s_*})_{\operatorname{rep}(5,6)}+(y_{s_*})_{c_6}+\frac14\\
&=\frac14+\frac14+\frac14=\frac34.
\end{aligned}
$$

Thus the purported equal contribution replaces $1/2$ by $1/4$. It is the same lost invariant, now appearing as the incorrect transfer of the paid correction to the reduced graph. It also falsifies the subsequent [assertion that the reduced vertex cut has been raised](../paper/paper.tex#L4498). These discrepancies are actual calculations on the defined vectors, so this audit records them as downstream CONV failures. The diagnostic Blossom calculation alone would not justify a CONV label; the specific printed transformations just identified are what fail.

In contrast, expanding the [objective expression](../paper/paper.tex#L3850) confirms the cost claim. For the three star types at the initial vector, the second entries in the maximum are

$$
\begin{array}{c|c|c}
\text{star type}&k_S-1-x^{\mathrm{init}}(S_H)&x^{\mathrm{init}}_{c_S}\\\hline
\text{nonroot size two}&1-(1/4+1/2)=1/4&1/4\\
\text{nonroot size three}&2-(1/4+3/4+3/4)=1/4&1/4\\
\text{root size four}&3-(1/4+3/4+3/4+3/4)=1/2&1
\end{array}
$$

Every change increases coordinates. Therefore $k_S-1-y_s(S_H)\le(y_s)_{c_S}$ is preserved, and

$$
\begin{aligned}
\Psi(y_s)
&=n-1+y_s(N_H)+\sum_{S\in\mathcal S}
\max\{(y_s)_{c_S},k_S-1-y_s(S_H)\}\\
&=n-1+y_s(N_H)+\sum_{S\in\mathcal S}(y_s)_{c_S}.
\end{aligned}
$$

A removable tree-edge increase changes neither remaining sum. Each actual increase of a nonremovable representative or nonroot connector contributes exactly $1/4$. Deduplicating the selected edges gives at most $|M|+|U_M|=|V(K)|-|M|=\rho$ paid increases, as claimed [at the modified step](../paper/paper.tex#L4271).

On the witness there are five nonremovable edges and seven stars. Hence

$$
\begin{aligned}
\Psi(x^{\mathrm{init}})
&=12+\frac54+\left(1+\frac64\right)=\frac{63}{4},\\
\Psi(y_{s_*})
&=12+\left(\frac54+\frac14\right)+\left(1+\frac64\right)=16,\\
\rho&=1-0=1\le\frac{13-2}{5}=\frac{11}{5}.
\end{aligned}
$$

The original connector selection also has expression value $16$, by moving the added $1/4$ from the nonremovable-edge sum to the connector sum. Finally, the manuscript's bound calculation expands correctly:

$$
\frac54n-\frac12+\frac{n-2}{20}
=\frac{25n-10+n-2}{20}
=\frac{26n-12}{20}
=\frac{13}{10}n-\frac35,
\qquad
16\le\frac{163}{10}\quad(n=13).
$$

The conversion errors occur in transporting cut values after the false degree-two assertion, while the cost expression and paid-increase count continue to compute exactly as stated.

## Final direct labels and remaining issues

**Final direct label: G, subtype G1.** This agrees with the primary G1 classification in the [case description](../README.md) and the [construction](tricker_report.md) and checker reports. The exact direct obligation is the pre-generalization derivation for all boundary-edge selections allowed at lines 4263–4266; the old endpoint restriction is needed for the degree-two invariant and is absent from the new range.

The audit makes the downstream roles explicit. MP fails when the reduction and tour theorem are used with unestablished antecedents. It also records the literal cut-value substitutions at lines 4378–4383 and the erased correction at lines 4498–4503 as downstream CONV failures; the earlier reports principally describe these as consequences of the lost suppression premise and emphasize the correct arithmetic of the cost. This refinement leaves the direct label set unchanged. G2 and DEF have no demonstrated violation at the planted step.

The verified witness has $13$ vertices, satisfies all graph and DFS assumptions, uses the unique maximum matching, and selects the permitted edge $\operatorname{rep}(6,7)$. Its decisive Blossom left-hand side is $3/4$, while its correctly computed objective expression is $16$. The established failure is the arbitrary-choice feasibility guarantee used by the submitted proof. No unresolved mathematical issue affects this classification.
