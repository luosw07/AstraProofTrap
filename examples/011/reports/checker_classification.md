# 011: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow. It is informed by the complete modified manuscript, its original and mutation, and the supplied construction and checker materials. It is a classification reassessment, rather than an original workflow report or a blind reviewer run.

## Exact target and actual assumptions

The target is the selection of a realization in [Proposition 9.5, lines 4340–4345](../paper/paper.tex#L4340), followed by the application of Lemma 9.1 at [lines 4386–4393](../paper/paper.tex#L4386) and the normalized-moment contradiction at [lines 4394–4416](../paper/paper.tex#L4394), on printed pages 37–38. The [mutation](../mutation.diff) replaces the [original full-extension realization](../original/paper.tex#L4340) with a realization of the values on $U(\mathbb F_p)$ and the instruction:

> Fix any such realization and write $T_{p^a}$ for its trace on $U(\mathbb F_{p^a})$, for $a\ge1$.

The original and modified TeX differ precisely by that paragraph. In particular, the definition (9.1), Lemma 9.1, the canonical complex, and Proposition 9.5's statement remain the same.

The following data and assertions form the background $\Gamma_0$ used in the Notes:

1. $n\in\mathbb Z$, $n\ge10$; $F\in\mathbb Z[x_1,\ldots,x_n]$ is a nonzero homogeneous cubic; $X=V(F)\subset\mathbb P^{n-1}_{\mathbb Q}$; and $X(\mathbb Q)=\varnothing$. These are the [standing assumptions of Section 9](../paper/paper.tex#L4071). Geometric integrality is available from Proposition 2.3.
2. $V\subset\mathbb A^n_{\mathbb Q}$ is a geometrically irreducible affine cone of codimension $r+1$ and degree $d\in\mathbb Z_{\ge1}$. The set $U\subset V\setminus\{0\}$ is a nonempty smooth open subset defined over $\mathbb Q$. Thus $m:=\dim U=n-r-1$, and $w:=n+r-2$ is an integer. On the branch $d\le r$, necessarily $r\ge1$.
3. Integral models are fixed. Let $\mathcal P$ be the primes beyond a sufficiently large fixed threshold, excluding an auxiliary prime $\ell$, such that the models and the relevant canonical lissity and rank statements hold. Fix $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$ and the nontrivial additive characters $\psi_p$ used in the proof. For $p\in\mathcal P$ and $a\in\mathbb Z_{\ge1}$, put $q=p^a$ and $\psi_{p,a}=\psi_p\circ\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}$. This character is nontrivial, since the finite-field trace is surjective.
4. To distinguish the two meanings of the printed $T_q$, write

   $$
   T^{\mathrm{can}}_{p,a}(v)
   =\sum_{\substack{x\in\mathbb F_{p^a}^{n}\\F(x)=0}}
     \psi_{p,a}(x\cdot v)
     -p^{a(n-1)}\mathbf1_{v=0}.
   $$

   This is exactly [(9.1)](../paper/paper.tex#L4078), with its character specified. Write $\mathcal K_p=K_{p,\psi_p}|_{U_{\mathbb F_p}}$ for the restriction of [(9.4)](../paper/paper.tex#L4201). Its cohomology sheaves are lisse on $U_{\mathbb F_p}$, mixed with integer weights, and have total rank at most a fixed $R_0$, independent of $p$. Formula [(9.5)](../paper/paper.tex#L4219) supplies the identity $t_{\mathcal K_p}(v;p^a)=T^{\mathrm{can}}_{p,a}(v)$ for **every** $a\ge1$ and $v\in U(\mathbb F_{p^a})$.
5. The available results include [Lemma 9.1](../paper/paper.tex#L4097), [Lemma 9.3](../paper/paper.tex#L4245), and the cited degree-versus-linear-span result used at [lines 4372–4384](../paper/paper.tex#L4372). The supplied [Xu Theorem 3.5 and Remark 3.6](../paper/references/Xu20.txt#L968) concern the entire collection of trace functions over finite extensions. The mixed-lisse version applies on a normal variety; the smooth $U_{\mathbb F_p}$ here is normal. Lemma 9.3's uniform constructibility input is also supported by the supplied [Fouvry–Katz Theorem 2.1](../paper/references/FK01.txt#L332).

A selected realization can be represented by a bounded constructible complex $E$ on $U_{\mathbb F_p}$ with lisse cohomology, or equivalently for this purpose by its finite signed list of cohomology sheaves. Its trace is

$$
\tau_{p,E}(v;a)
=\sum_i(-1)^i\iota\!\left(
\operatorname{Tr}(\operatorname{Fr}_{p^a,v}\mid\mathcal H^i(E)_{\bar v})
\right).
$$

For a fixed bound $R$, define its retained selection predicate by

$$
\begin{aligned}
\mathcal R_p(E,R)\;:\Longleftrightarrow\;&
 E\in D^b_c(U_{\mathbb F_p},\overline{\mathbb Q}_\ell),\\
&\mathcal H^i(E)\text{ is lisse and mixed with integer weights for every }i,\\
&\sum_i\operatorname{rank}\mathcal H^i(E)\le R,\\
&\forall v\in U(\mathbb F_p),\quad
  \tau_{p,E}(v;1)=T^{\mathrm{can}}_{p,1}(v).
\end{aligned}
$$

Uniformity means that one finite $R$ works as $p$ varies. The selected trace is fixed before $a$ varies. No identity at $a>1$ appears in $\mathcal R_p$.

The earlier identity (9.5) is explicitly about $\mathcal K_p$. [Remark 9.4](../paper/paper.tex#L4312) and [Appendix A's alternative trace formula](../paper/paper.tex#L6847) likewise identify specific geometric realizations of the exponential sums. Neither passage identifies every realization of the degree-one values with the canonical extension sequence. The full manuscript therefore supplies a canonical witness with stronger properties, but does not supply the missing property for the arbitrary witness permitted by the altered paragraph.

## Five-rule audit summary

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | direct | Proposition 9.5, [4386–4393](../paper/paper.tex#L4386) | Lemma 9.1 yields a bound for the canonical sums; the proof exports it for the selected trace sequence. [Full Note](#mp--note). |
| G1 | not_violated | downstream | The “for every $a\ge1$” assertion at [4386](../paper/paper.tex#L4386), and the degree-one specialization at [4369](../paper/paper.tex#L4369) | The arbitrary-degree derivation fails at the MP application. The universal-introduction variable conditions introduce no additional defect. [Full Note](#g1--note). |
| G2 | violated | direct | Realization selection at [4340–4345](../paper/paper.tex#L4340), discharged through the argument ending at [4416](../paper/paper.tex#L4416) | The supplied witness properties do not suffice for the proposed elimination of Xu's large-moment alternative. [Full Note](#g2--note). |
| DEF | not_violated | none | The realization and its trace at [4340–4345](../paper/paper.tex#L4340); projective and affine linear spaces at [4372–4384](../paper/paper.tex#L4372) | The selected object and its trace are well-defined. The explicit rank-two addition meets the selection contract. [Full Note](#def--note). |
| CONV | not_violated | diagnostic | The normalization at [4363–4367](../paper/paper.tex#L4363) and the limiting argument at [4394–4413](../paper/paper.tex#L4394) | The powers, Frobenius traces and valid moment computations check correctly. They expose a missing identification in a theorem application. [Full Note](#conv--note). |

## MP — Note

**Status: violated. Role: direct.** The original rule is

$$
\frac{\Gamma\vdash A\qquad\Gamma\vdash A\to B}{\Gamma\vdash B}.
$$

The application at issue is the explicit “By Lemma 9.1” at [line 4386](../paper/paper.tex#L4386). Fix $p\in\mathcal P$, an integer $\alpha\ge1$, $q=p^\alpha$, the selected $E$ and rank bound $R$, and the rational linear space $L$ obtained in the preceding paragraph. The local context $\Gamma_{\mathrm{MP}}$ consists of $\Gamma_0$, these fixed choices, $\mathcal R_p(E,R)$, $d\le r$, $V\subset L$, $\dim L=n-2$, and the open large-moment branch

$$
H_p(E):\quad
\limsup_{a\to\infty}p^{-a(2n-2)}
\sum_{v\in U(\mathbb F_{p^a})}|\tau_{p,E}(v;a)|^2\ge1.
$$

The $a$ in this formula is bound; $E,p,F,L$ are fixed. Put $L_q^\times=L(\mathbb F_q)\setminus\{0\}$. The background for the instantiated Lemma 9.1 is the following fully specified antecedent:

$$
\begin{aligned}
A_\alpha:\quad& n\in\mathbb Z_{\ge10},\quad
F\in\mathbb Z[x_1,\ldots,x_n]\text{ nonzero homogeneous of degree }3,\\
&X=V(F)\subset\mathbb P^{n-1}_{\mathbb Q},\quad X(\mathbb Q)=\varnothing,\\
&L\subset\mathbb Q^n\text{ a }\mathbb Q\text{-linear subspace of dimension }n-2,\\
&p\text{ a sufficiently large prime for }F,L,\quad
\alpha\in\mathbb Z_{\ge1},\quad q=p^\alpha,\\
&\eta:=\psi_p\circ\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}
   : (\mathbb F_q,+)\to\mathbb C^\times\text{ a nontrivial additive character}.
\end{aligned}
$$

The substitution into the quantified lemma is precisely $(L,p,q,\psi_q)=(L,p,p^\alpha,\eta)$, with the unchanged $n,F$. The consequent, after omitting the nonnegative origin term, is

$$
B_\alpha:\quad
\sum_{v\in L_q^\times}
\left|\sum_{\substack{x\in\mathbb F_q^n\\F(x)=0}}
\eta(x\cdot v)\right|^2
=\sum_{v\in L_q^\times}|T^{\mathrm{can}}_{p,\alpha}(v)|^2
\le b_{F,L}q^{2n-3},
$$

where $b_{F,L}$ is independent of $p,\alpha,\eta$. In fact, Lemma 9.1 bounds the sum including the origin, with the correction term of (9.1) retained there. Every hypothesis of this canonical application is available, so

$$
\Gamma_{\mathrm{MP}}\vdash A_\alpha,\qquad
\Gamma_{\mathrm{MP}}\vdash A_\alpha\to B_\alpha,
\qquad
\Gamma_{\mathrm{MP}}\vdash B_\alpha
$$

is sound.

The displayed conclusion $C_\alpha$ actually claimed at [lines 4388–4392](../paper/paper.tex#L4388) instead uses the locally reassigned $T_{p^\alpha}$:

$$
C_\alpha:\quad
\sum_{v\in L_q^\times}|T_{p^\alpha}(v)|^2
\ll_{F,L}q^{2n-3},
\qquad
T_{p^\alpha}|_{U(\mathbb F_q)}=\tau_{p,E}(\,\cdot\,;\alpha).
$$

In particular, the use of $C_\alpha$ in the next display requires

$$
C^U_\alpha:\quad
M_{p,E}(\alpha):=
\sum_{v\in U(\mathbb F_q)}|\tau_{p,E}(v;\alpha)|^2
\ll_{F,L}q^{2n-3}.
$$

The first failed obligation is preservation of the lemma's consequent: $B_\alpha$ concerns $T^{\mathrm{can}}_{p,\alpha}$, while $C_\alpha$ must bound the chosen sequence. A bridge that would justify the restricted conclusion is

$$
\operatorname{Agree}_{p,\alpha}(E):\quad
\forall v\in U(\mathbb F_{p^\alpha}),\quad
\tau_{p,E}(v;\alpha)=T^{\mathrm{can}}_{p,\alpha}(v).
$$

The selection supplies $\operatorname{Agree}_{p,1}(E)$ only. Equivalently, if the lemma is reconstructed as an implication about an input function $f:L_q^\times\to\mathbb C$, its antecedent must include $f(v)=T^{\mathrm{can}}_{p,\alpha}(v)$ throughout that domain. Substituting the selected trace leaves that antecedent unestablished. This reconstruction describes the same failed application, rather than an additional error.

There is also a visible domain mismatch: the new realization was selected only on $U$, whereas the displayed sum runs over $L_q^\times$. If that larger sum keeps the old canonical meaning, it is bounded by Lemma 9.1, but the following comparison with the selected $U$-sum lacks the trace identification. If the larger sum is to use an extension of the selected realization, the selection provides neither that extension nor its moment bound. The witness below has an explicit extension to the entire punctured ambient space and already violates $C^U_\alpha$ on $U$ itself, so its quantitative failure covers both readings.

The earlier applications in this fragment remain valid:

- **Xu:** take the even cohomology sheaves of $E$ for the positive sheaves and the odd cohomology sheaves for the negative sheaves; take the variety to be $U_{\mathbb F_p}$, $\kappa=\mathbb F_p$, $w=n+r-2$, and moment index $s=1$. Normality, mixed lissity, integer weights and the rank bound are supplied. The consequent is exactly

  $$
  S_p(E,R)\ \lor\ H_p(E),\qquad
  S_p(E,R):\,
  \forall a\ge1\ \forall v\in U(\mathbb F_{p^a}),\quad
  |\tau_{p,E}(v;a)|\le R p^{aw/2}.
  $$

  Its small alternative gives the desired base-field estimate by $a=1$ and the supplied agreement at degree one. Its large alternative concerns the selected trace.
- **Linear span:** on the branch $d\le r$, the projective variety $Y$ has dimension $n-r-2$, degree $d$, and ambient codimension $r+1$. The cited degree bound for a variety in its linear span gives $\operatorname{codim}_{\mathbb P^{n-1}}\langle Y\rangle\ge r+2-d\ge2$. Its span is defined over $\mathbb Q$, so it lies in a rational codimension-two projective space $P$, whose affine cone is the stated $L$. This supplies the geometric hypotheses of Lemma 9.1 without imposing a condition on $E$.

The [DEF](#def--note) and [CONV](#conv--note) Notes exhibit $\mathcal R_p(E,R)$ with $r=d=1$ and $M_{p,E}(a)\ge\frac12q^{3n-4}$ along all sufficiently large even degrees. Thus the failed application is a direct MP error at its own printed location, even though it occurs later than the witness selection. The later contradiction and the uses of Proposition 9.5 inherit this error.

## G1 — Note

**Status: not_violated. Role: downstream.** The rule being audited is

$$
\frac{\Gamma\vdash A\to B(x)}
     {\Gamma\vdash A\to\forall x\,B(x)},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(A).
$$

Here the actual quantified extension variable is $a\in\mathbb Z$, with range predicate $D(a):=(a\ge1)$. Keep $p,E,R,L$ fixed as in the MP Note, and let $b=b_{F,L}>0$ be the canonical moment constant, chosen before $a$. Let $\Gamma_1$ consist of $\Gamma_0$, the fixed choices $p,E,R,L,b$, $\mathcal R_p(E,R)$, $d\le r$, $V\subset L$, $\dim L=n-2$, $H_p(E)$, and the canonical moment estimate with constant $b$. No extension degree is free in these assumptions: the index in $H_p(E)$ and in the canonical estimate is bound.

Use $A=\top$ and

$$
B(a)=D(a)\ \longrightarrow\
\sum_{v\in U(\mathbb F_{p^a})}|\tau_{p,E}(v;a)|^2
\le b p^{a(2n-3)}.
$$

The relevant pre-generalization attempt at [line 4386](../paper/paper.tex#L4386) is as follows. Take a fresh integer $\alpha$ and open $[D(\alpha)]$. Lemma 9.1 and positivity validly give

$$
\Gamma_1,D(\alpha)\vdash
\sum_{v\in U(\mathbb F_{p^\alpha})}|T^{\mathrm{can}}_{p,\alpha}(v)|^2
\le b p^{\alpha(2n-3)}.
$$

The manuscript uses this as the corresponding estimate for $\tau_{p,E}(v;\alpha)$. That is the failed MP step just formalized. Were this particular-degree estimate established, discharging $D(\alpha)$ would give $\Gamma_1\vdash\top\to B(\alpha)$ and universal introduction would give

$$
\Gamma_1\vdash\top\to
\forall a\in\mathbb Z\left(
a\ge1\ \longrightarrow\ M_{p,E}(a)\le b p^{a(2n-3)}
\right).
$$

This is the restricted quantified form of the claimed moment bound; allowing an unspecified uniform implied constant adds an outer $\exists b>0$. The variables $v$ in the sums are bound, and $q$ is the abbreviation $p^\alpha$, not a new parameter selected independently of $\alpha$. The undischarged parameters $n,F,X,V,U,r,d,p,\ell,\iota,\psi_p,E,R,L,b$ do not include $\alpha$. The assumptions $d\le r$ and $H_p(E)$ are discharged later in the contradiction and case argument. Thus the eigenvariable condition for the extension-degree generalization is satisfied. Its input derivation is unsupported because the selected trace was substituted into the canonical moment estimate, not because a special extension degree was generalized.

For comparison, the exact same derivation with $T^{\mathrm{can}}_{p,\alpha}$ throughout is a valid instantiated G1 application: discharge $\alpha\ge1$ and conclude the canonical moment bound for every positive extension degree. This confirms the role of the actual missing step.

At [line 4369](../paper/paper.tex#L4369), “taking $a=1$” is universal **elimination** from $S_p(E,R)$, followed by the established identity $\tau_{p,E}(v;1)=T^{\mathrm{can}}_{p,1}(v)$. It is valid. At [lines 4344–4345](../paper/paper.tex#L4344), assigning the symbol $T_{p^a}$ to the selected trace is a definition for every positive $a$; it is not a printed derivation of $\forall a\,\operatorname{Agree}_{p,a}(E)$ from the $a=1$ instance.

The [tricker report](tricker_report.md#L9) calls G1 an equivalent description, and the [earlier checker](checker_report.md#L47) calls it a useful secondary description. The explicit proof structure supports a more precise distinction: the universal moment claim is downstream of the incorrect theorem application, while the witness-sufficiency error is G2. There is no additional direct G1 violation to label.

## G2 — Note

**Status: violated. Role: direct.** The rule is

$$
\frac{\Gamma\vdash A(x)\to B}
     {\Gamma\vdash(\exists x\,A(x))\to B},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(B).
$$

The existence claim and “Fix any such realization” in [lines 4340–4345](../paper/paper.tex#L4340) form the witness-selection step. To make the stated uniformity in $p$ explicit, the following is a symbolic reconstruction of that proof, packaging its choices over the allowed primes into a family. This introduces no agreement requirement beyond the one printed.

Let the witness variable be

$$
x=\bigl((E_{x,p})_{p\in\mathcal P},R_x\bigr),
$$

where each $E_{x,p}$ is a bounded constructible $\overline{\mathbb Q}_\ell$-complex on $U_{\mathbb F_p}$ and $R_x\in\mathbb Z_{\ge1}$. Define

$$
A(x):\quad
\forall p\in\mathcal P,\quad \mathcal R_p(E_{x,p},R_x).
$$

Thus its supplied properties are exactly lissity of every cohomology sheaf, mixedness with integer weights, a common finite total-rank bound, and equality with $T^{\mathrm{can}}_{p,1}$ on all $U(\mathbb F_p)$. The canonical family $(\mathcal K_p,R_0)$, with $R_0$ enlarged to at least one if necessary, proves $\exists x\,A(x)$. The selection class permits the explicit modified family in the DEF Note as well.

The exported conclusion is the original proposition, written with its uniform constant and point range exposed:

$$
\begin{aligned}
B:\quad &(d\ge r+1)\ \lor\\
&\left[\exists D>0\ \forall p\in\mathcal P\ \forall v\in U(\mathbb F_p),\quad
|T^{\mathrm{can}}_{p,1}(v)|\le Dp^{(n+r-2)/2}\right].
\end{aligned}
$$

The constant $D$ may depend on the fixed $F,V,U$ and is independent of $p,v$. The free background parameters are precisely those in $\Gamma_0$; $p,v,D$ in $B$ are bound. Neither the realization family nor its rank-bound coordinate is free in $B$.

Here is the existential-elimination subderivation attempted by the printed argument, with the gap marked at its first occurrence:

$$
\begin{array}{ll}
1.&\exists x\,A(x).\\[2pt]
2.&[A(z)]^{(1)}\quad
z=((E_{z,p})_{p\in\mathcal P},R_z)\text{ fresh}.\\[2pt]
3.&[d\le r]^{(2)};\quad p\in\mathcal P\text{ arbitrary}.\\[2pt]
4.&S_p(E_{z,p},R_z)\ \lor\ H_p(E_{z,p})
\quad\text{by Xu}.\\[2pt]
5.&[S_p(E_{z,p},R_z)]^{(3)}
\ \Longrightarrow\
\forall v\in U(\mathbb F_p),\,
|T^{\mathrm{can}}_{p,1}(v)|\le R_zp^{w/2}.\\[2pt]
6.&[H_p(E_{z,p})]^{(4)}
\ \Longrightarrow\ V\subset L,\quad \dim L=n-2.\\[2pt]
7.&\text{Claimed, but unsupported: }\quad
\forall a\ge1,\quad M_{p,E_{z,p}}(a)\ll_{F,L}p^{a(2n-3)}.\\[2pt]
8.&\text{Using line 7, the manuscript claims a contradiction to line 6's }H_p(E_{z,p}).
\end{array}
$$

Line 5 discharges the small-case assumption only when the two cases are joined. Line 8 is intended to discharge the large-case assumption $(4)$ by contradiction, leaving the same base-field bound in both cases. Generalizing the arbitrary prime $p$ would then give that bound for all $p\in\mathcal P$ with the single constant $R_z$. Introducing $\exists D$ with $D=R_z$, and joining with the complementary case $d\ge r+1$, would discharge $(2)$ and yield $B$ inside the witness scope. Discharging $(1)$ would establish $\Gamma_0\vdash A(z)\to B$; existential elimination with line 1 would then yield $B$.

This reconstruction specifies both the local witness scope and the intended exported result. Its first failed conditional obligation is line 7. It requires control of the sequence

$$
a\longmapsto
\bigl(\tau_{p,E_{z,p}}(v;a)\bigr)_{v\in U(\mathbb F_{p^a})},
$$

which depends on $z$ through all the Frobenius representations of $E_{z,p}$. Consequently $M_{p,E_{z,p}}(a)$, $S_p(E_{z,p},R_z)$ and $H_p(E_{z,p})$ depend on $z$. Those are legitimate intermediate dependencies inside the witness scope. The difficulty is that the printed witness predicate supplies no full-extension comparison with the canonical sequence from Lemma 9.1.

The following two statements expose the missing property:

$$
A(z)\quad\text{supplies}\quad
\forall p\in\mathcal P\ \forall v\in U(\mathbb F_p),\quad
\tau_{p,E_{z,p}}(v;1)=T^{\mathrm{can}}_{p,1}(v),
$$

whereas the proposed moment transfer would be justified by

$$
\forall p\in\mathcal P\ \forall a\ge1\ \forall v\in U(\mathbb F_{p^a}),\quad
\tau_{p,E_{z,p}}(v;a)=T^{\mathrm{can}}_{p,a}(v).
$$

This is a missing witness property, not a switch from $\forall a\exists E$ to $\exists E\forall a$: the manuscript fixes the realization before varying $a$, and the witness below does the same. Also, the G2 side condition is satisfied: $z\notin\operatorname{FV}(\Gamma_0)\cup\operatorname{FV}(B)$. The dependence of a permissible intermediate trace does not itself violate the eigenvariable condition. G2 fails because the proposed conditional derivation of the witness-independent $B$ uses more than $A(z)$ supplies.

For the degree-one cone $V=L$ below, $r=d=1$, the modified family satisfies $A(z)$ at every permitted prime. Its normalized selected second moment has limsup $+\infty$. Thus Xu's large alternative holds on this branch while the proposed line 7 fails by an unbounded power of $q$. This verifies the failure of the stated sufficiency argument. The construction is relative to the canonical complexes under the manuscript's standing contradiction assumptions and works for every such complex.

## DEF — Note

**Status: not_violated. Role: none.** The relevant objects are the canonical realization, the arbitrarily selected realization and its extension-indexed trace, and the projective and affine spaces used in the large-moment branch. Their definition obligations can be checked concretely.

First, [(9.4)](../paper/paper.tex#L4208) defines

$$
K_{p,\psi_p}
=R\pi_{2!}\bigl(\pi_1^*i_*\overline{\mathbb Q}_\ell
\otimes\mathcal L_{\psi_p}(x\cdot v)\bigr)
\in D^b_c(\mathbb A^n_{\mathbb F_p},\overline{\mathbb Q}_\ell).
$$

Here $i:\{F=0\}\hookrightarrow\mathbb A^n_x$ is a closed immersion, $\pi_1,\pi_2$ are the projections from $\mathbb A^n_x\times\mathbb A^n_v$, and $(x,v)\mapsto x\cdot v$ is a regular map to $\mathbb A^1$. The pullback, tensor product and compactly supported derived pushforward therefore have the stated domains and codomain. Restriction to $U_{\mathbb F_p}$ gives $\mathcal K_p$, an existing member of the selection class by (9.5) and the proposition's hypotheses.

For any selected $E$, the trace definition is a function

$$
\tau_{p,E}:\coprod_{a\ge1}\bigl(\{a\}\times U(\mathbb F_{p^a})\bigr)
\longrightarrow\mathbb C.
$$

The tag $a$ matters: a point rational over two extensions is evaluated with the corresponding Frobenius power. Each stalk is finite dimensional, the alternating sum is finite, and changing a geometric lift of $v$ conjugates the Frobenius action, leaving its trace unchanged. Isomorphic realizations, or quasi-isomorphic complexes, give the same trace. The selection asks for an object with the stated properties, not a unique object determined by the base-field trace. Accordingly, nonuniqueness is permitted by its definition.

The following explicit permitted object verifies that distinction. Set

$$
L=\{v_1=v_2=0\}\subset\mathbb A^n_{\mathbb Q},\qquad V=L.
$$

This is a geometrically irreducible affine cone with $\dim L=n-2$, $r=1$, $d=1$. A finite partition from [Lemma 9.3](../paper/paper.tex#L4245) has a stratum whose intersection with $L\setminus\{0\}$ contains a nonempty open subset of $L$. Choose such an open $U$, defined over $\mathbb Q$. It is smooth because it is open in a linear space. Pullback from that stratum gives lisse cohomology of $\mathcal K_p$ on $U$ and a uniform total-rank bound $R_0$ for all sufficiently large $p$. This supplies exactly the geometric range of Proposition 9.5; $V$ is a frequency-space cone and is not required to lie in $X$.

For each permitted $p$, let $\chi_p$ be the rank-one sheaf pulled back from $\operatorname{Spec}\mathbb F_p$ corresponding to the order-two constant-field character, with geometric Frobenius acting by $-1$. Put $M=n-1$ and define

$$
\mathcal G_p=
\overline{\mathbb Q}_\ell(-M)
\oplus\bigl(\chi_p\otimes\overline{\mathbb Q}_\ell(-M)\bigr),
\qquad
E_p=\mathcal K_p\oplus\mathcal G_p[-2M].
$$

These are sheaves and a complex on $U_{\mathbb F_p}$. The added sheaf comes from the explicit two-dimensional continuous Galois representation with Frobenius matrix

$$
\begin{pmatrix}p^M&0\\0&-p^M\end{pmatrix}.
$$

Existence follows from the Tate sheaf and the character of $\operatorname{Gal}(\mathbb F_{p^2}/\mathbb F_p)$; the direct sum and shift specify $E_p$ unambiguously up to the usual isomorphism of complexes. It has the following defining properties:

- $\mathcal G_p$ is geometrically constant and lisse; both eigenvalues have absolute value $p^M$, so it is pure of the integer weight $2M=2n-2$.
- The shift $[-2M]$ places it in cohomological degree $2M$, so its alternating sign is $(-1)^{2M}=1$. This preserves even the canonical envelope “weight at most cohomological degree” at [lines 4235–4241](../paper/paper.tex#L4235), and uses a degree within $0,\ldots,2(n-1)$, the compact-support range for the fibers in (9.4).
- Its total-rank cost is exactly two. The common bound $R=R_0+2$ bounds both the canonical ranks and the chosen ranks for all $p$. The paper specifies a uniform upper bound, rather than a prescribed sharp numerical bound.
- At every $v\in U(\mathbb F_p)$, the additional trace is $p^M-p^M=0$. Thus $\tau_{p,E_p}(v;1)=T^{\mathrm{can}}_{p,1}(v)$ exactly, as required by $\mathcal R_p(E_p,R)$.
- The object is selected once for each $p$. It is unchanged when the extension degree varies. Because the summand is pulled back from the base field, it also respects homogeneity and is lisse on every stratum.

The trace calculation in the next Note gives its behavior at all extension degrees. In particular, every requirement for introducing this realization holds; the later moment bound is an asserted property that fails.

For completeness, the projectivization introduced in the proof is $Y=\operatorname{Proj}(\mathbb Q[V])$. On the low-degree branch the rational linear span of $Y$ lies in some rational codimension-two space $P$, as detailed in the MP Note, and $L$ is the affine cone over $P$. Neither $P$ nor $L$ is required to be uniquely chosen. For the concrete witness above, $Y=P=\mathbb P^{n-3}$ and $L=\{v_1=v_2=0\}$ already satisfy those requirements.

Finally, the same added sheaf is defined on all of $\mathbb A^n_{\mathbb F_p}\setminus\{0\}$. Hence

$$
\widetilde E_p=
K_{p,\psi_p}|_{\mathbb A^n_{\mathbb F_p}\setminus\{0\}}
\oplus\mathcal G_p[-2M]
$$

is an explicit constructible extension of $E_p$ and has traces at every point in the printed larger $L$-sum. The arbitrary selection on $U$ itself specifies no such extension, but the verified failure persists for this object where that larger expression is meaningful. The fault lies in the asserted estimate and trace identification, rather than the existence, uniqueness or representative independence of the selected object.

## CONV — Note

**Status: not_violated. Role: diagnostic.** The exact expression at the beginning of the decisive display is

$$
1\le
\limsup_{a\to\infty}p^{-a(2n-2)}
\sum_{v\in U(\mathbb F_{p^a})}|T_{p^a}(v)|^2,
$$

and its claimed endpoint is $\ll\lim_{a\to\infty}p^{-a}=0$, at [lines 4398–4413](../paper/paper.tex#L4398). The normalization preceding it is correctly computed:

$$
\dim U+w+1=(n-r-1)+(n+r-2)+1=2n-2.
$$

The moment estimate used between these expressions is a separate theorem application. Expanding its canonical input shows exactly what that theorem bounds. In coordinates $L=\{v_1=v_2=0\}$, put $v=(0,0,v')$, $x'=(x_3,\ldots,x_n)$, and

$$
\nu_F(x')=\#\{(x_1,x_2)\in\mathbb F_q^2:F(x_1,x_2,x')=0\}.
$$

Additive-character orthogonality gives

$$
q\sum_{x'\in\mathbb F_q^{n-2}}\psi_{p,a}(v'\cdot x')
=q^{n-1}\mathbf1_{v'=0},
$$

so the definition (9.1) expands as

$$
\begin{aligned}
T^{\mathrm{can}}_{p,a}(0,0,v')
&=\sum_{x'}\nu_F(x')\psi_{p,a}(v'\cdot x')
  -q^{n-1}\mathbf1_{v'=0}\\
&=\sum_{x'}(\nu_F(x')-q)\psi_{p,a}(v'\cdot x').
\end{aligned}
$$

Because $\nu_F(x')-q$ is real and $\overline{\psi(t)}=\psi(-t)$, squaring and summing yields

$$
\begin{aligned}
\sum_{v\in L(\mathbb F_q)}|T^{\mathrm{can}}_{p,a}(v)|^2
&=\sum_{x',y'}(\nu_F(x')-q)(\nu_F(y')-q)
  \sum_{v'}\psi_{p,a}(v'\cdot(x'-y'))\\
&=q^{n-2}\sum_{x'}(\nu_F(x')-q)^2.
\end{aligned}
$$

This is the computation actually printed in [Lemma 9.1](../paper/paper.tex#L4110). Its good fibers contribute $O(q)$ each, and its $O(q^{n-3})$ exceptional fibers contribute $O(q^2)$ each, using the stated geometric irreducibility and point-count inputs. Thus the powers are

$$
q^{n-2}\bigl(O(q^{n-2})O(q)+O(q^{n-3})O(q^2)\bigr)
=O(q^{2n-3}).
$$

For this canonical sequence the normalized conclusion is correctly

$$
0\le q^{-(2n-2)}\sum_{v\in U(\mathbb F_q)}|T^{\mathrm{can}}_{p,a}(v)|^2
\le b_{F,L}q^{-1}\longrightarrow0.
$$

Now expand the actual permitted selected realization from the DEF Note. Geometric Frobenius over $\mathbb F_{p^a}$ acts on the added constant sheaf by the $a$th power of its base-field Frobenius matrix. Consequently

$$
\begin{aligned}
t_{\mathcal G_p}(v;p^a)
&=(p^M)^a+(-p^M)^a\\
&=p^{aM}\bigl(1+(-1)^a\bigr)
=q^{n-1}\bigl(1+(-1)^a\bigr),\\
\tau_{p,E_p}(v;a)
&=T^{\mathrm{can}}_{p,a}(v)
  +(-1)^{2M}t_{\mathcal G_p}(v;p^a)\\
&=T^{\mathrm{can}}_{p,a}(v)
  +q^{n-1}\bigl(1+(-1)^a\bigr).
\end{aligned}
$$

At $a=1$ the added value is zero. At every even $a$ it is $2q^{n-1}$. This is equality of the trace of Frobenius at degree one without equality of the traces of its powers.

Here $U$ is a fixed nonempty open subset of $L\simeq\mathbb A^{n-2}$. For each sufficiently large fixed $p$, its complement has dimension at most $n-3$, giving

$$
N_q:=\#U(\mathbb F_q)=q^{n-2}+O(q^{n-3})
\ge\tfrac12q^{n-2}
$$

for sufficiently large $q=p^a$. Regard the canonical trace as a vector $t$ in $\mathbb C^{U(\mathbb F_q)}$ and the added trace, for even $a$, as the constant vector $h=2q^{n-1}\mathbf1$. Lemma 9.1 and positivity give

$$
\|t\|_2^2\le b_{F,L}q^{2n-3},\qquad
\|h\|_2^2=4q^{2n-2}N_q\ge2q^{3n-4}.
$$

Once $q^{n-1}\ge2b_{F,L}$,

$$
\frac{\|h\|_2^2}{b_{F,L}q^{2n-3}}
\ge\frac{2q^{n-1}}{b_{F,L}}\ge4.
$$

The reverse triangle inequality then accounts for every possible phase and cancellation in $t$:

$$
\begin{aligned}
M_{p,E_p}(a)=\|t+h\|_2^2
&\ge(\|h\|_2-\|t\|_2)^2\\
&\ge\tfrac14\|h\|_2^2
=q^{2n-2}N_q\\
&\ge\tfrac12q^{3n-4}.
\end{aligned}
$$

The lower exponent exceeds the claimed canonical exponent by

$$
(3n-4)-(2n-3)=n-1,
$$

and normalization gives

$$
q^{-(2n-2)}M_{p,E_p}(a)
\ge\tfrac12q^{n-2}\longrightarrow+\infty
\qquad(a\to\infty\text{ through even integers}).
$$

For $n=10$, these are the incompatible moment powers $q^{26}$ and $q^{17}$, with normalized growth at least $q^8/2$. On the same cone $r=d=1$, Xu's small alternative has $w=n-1$ and would imply

$$
M_{p,E_p}(a)\le N_qR^2q^{n-1}\le R^2q^{2n-3},
$$

which conflicts with the derived lower bound. The selected trace therefore satisfies the large-moment alternative, while its cone still has degree one. Its full normalized limsup is $+\infty$, rather than the printed endpoint zero.

All the displayed powers and trace operations check correctly. The first invalid step in the manuscript's limiting argument is importing the canonical estimate for the selected trace, as detailed under MP. It is neither a false expansion of $(p^M)^a+(-p^M)^a$ nor an arithmetic error in the normalization. Accordingly, these computations are diagnostic evidence for MP and G2, rather than a direct CONV violation. The supplied [checker calculation](checker_calculation.py) passes, and independent exact evaluations confirm the Frobenius powers, all moment exponents, and the threshold in the reverse-triangle estimate; the displayed formulas provide the argument for every $n\ge10$ and all sufficiently large even extension degrees.

## Final direct classification and consequences

**Final direct labels: G (G2), MP.** G2 identifies the failed conditional derivation from the selected witness's stated properties to the witness-independent conclusion. MP identifies the explicit use of Lemma 9.1 with a different extension-field trace sequence. The MP application is later in the proof but directly violates the theorem-application obligation at its own location. These are the two demonstrated rule obligations of the same trace-compatibility defect.

This agrees with the [case README's primary and secondary labels](../README.md#L3). It retains the earlier checker's G2 and MP findings while declining the suggested direct G1 characterization in the [tricker](tricker_report.md#L9) and [checker](checker_report.md#L47) discussions: the manuscript does not generalize an $a=1$ equality to all $a$ by a distinct G1 step. DEF and CONV receive no direct label because the objects and computations are valid; the missing compatibility is used in the logical argument.

The verified witness is the uniform family $E_p=\mathcal K_p\oplus\mathcal G_p[-(2n-2)]$ on an admissible open subset of the rational degree-one cone $L$. It has rank increment two, preserves integer weights and the recorded weight-degree envelope, agrees at every base-field point, and forces a normalized second moment tending to infinity along even extension degrees.

The proof subsequently uses Proposition 9.5 to obtain the improved base-field bound on low-degree components at [lines 4509–4516](../paper/paper.tex#L4509) and in [Proposition 10.1](../paper/paper.tex#L4612). Those uses feed the estimates in Sections 10–12 and inherit the missing justification. They are downstream consequences of the identified defect, rather than additional direct labels.

There are no unresolved mathematical issues for this targeted classification. The required missing premise is precisely full-extension trace compatibility, or a selected-trace moment estimate established independently of that compatibility; neither is supplied for the arbitrary realization in the submitted proof.
