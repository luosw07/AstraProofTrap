# 007: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow. It is informed by the manuscript and existing construction/checker materials; it is neither an original workflow report nor a blind reviewer run.

The materials examined are the complete [modified manuscript](../paper/paper.tex), the [original manuscript](../original/paper.tex), the [mutation](../mutation.diff), the [tricker report](tricker_report.md), the [original checker report](checker_report.md), the [checker calculation](checker_calculation.py), the [case README](../README.md), and the [classification standard](../../../protocol/classification.md). A whole-file comparison verified that the original and modified manuscripts differ exactly by the two supplied patch hunks; the unchanged text and both original passages were examined. Reviewer verdicts and detection counts play no role in this review. The formalizations below reconstruct the printed operations in ordinary mathematical logic; they are not machine-checked proofs.

## Exact target and actual assumptions

The first insertion, [lines 3887–3891](../paper/paper.tex#L3887), specifies a base-linear coefficient comparison in the basis

$$
 z^rP^j,\qquad 0\leq r<m=\deg P,\quad 0\leq j<n.
$$

This is a valid comparison of finite free modules. The planted structural step is in the proof of Proposition 7.3, `loop:crystal`, [lines 4336–4338](../paper/paper.tex#L4336): obtain the lifted inducing representations in (7.2) by retaining their jet-current action matrices, and then restrict to a common depth. The accompanying assertion at [lines 4338–4343](../paper/paper.tex#L4338) is that the PBW and group-cobar constructions use identical coefficient diagrams, so their comparisons intertwine induction and satisfy the required higher compatibilities.

The actual input range matters:

- [Lines 3878–3885](../paper/paper.tex#L3878) allow any smooth affine parameter scheme and additional parameters, complete along the **sum** of graph divisors, and permit collisions and repeated graphs.
- [Lines 3960–3966](../paper/paper.tex#L3960) require tests on all finite infinitesimal multiple diagonals, using finite flat projections. They explicitly distinguish moving congruences from a horizontally constant finite jet group.
- [Lines 4130–4159](../paper/paper.tex#L4130) work in the underlying quasi-coherent categories. In (7.2), the inducing input is any algebraic representation of the specified arc/congruence group whose underlying object is a vector bundle. It need not be horizontal or trivial.
- Proposition 7.2, [lines 4161–4177](../paper/paper.tex#L4161), includes finite flat scalar extensions and fully faithful restriction **between pro-unipotent opens**. Its proof uses genuine group representations and their genuine Lie actions.

Use the following admissible data throughout the explicit certificate. Let

$$
 X=\mathbb P^1_{\mathbb C},\quad \vartheta=\mathcal O(-1),
 \quad G=\mathrm{SL}_2,\quad c=-\sqrt2.
$$

Choose the standard pinning and trivialize the fixed bundle $P_0$ on $\mathbb A^1_z$. With the manuscript's conventions, $a=\sqrt2$, $h^\vee=2$, $k_a=\sqrt2-2$, and $s=(2-\sqrt2)/4$. Set

$$
 R_0=\mathbb C[t],\quad S=\operatorname{Spec}R_0,
 \quad x_1=t,\quad x_2=-t,
$$

$$
 B=\mathbb C[t,\epsilon]/(\epsilon^3),\quad I=(\epsilon),
 \quad p_1^*t=t,\quad p_2^*t=t+\epsilon.
$$

This is the second infinitesimal diagonal of the smooth curve $S$. Each projection is finite free of rank three: for $p_2$, use $u=t+\epsilon$ and $t=u-\epsilon$. The two divisor equations are

$$
 P=z^2-t^2,\qquad Q=z^2-(t+\epsilon)^2=P-\delta,
 \qquad \delta=2t\epsilon+\epsilon^2.
 \tag{1}
$$

Both are monic degree-two graph sums, and $P\equiv Q\pmod I$. The markings collide at $t=0$; separating disjoint clusters does not remove that permitted collision.

For $D=P,Q$, put

$$
 A_{D,n}=B[z]/(D^n),\qquad
 \mathfrak j_{D,n}=\mathfrak{sl}_2\otimes_{\mathbb C} A_{D,n},
$$

with $[x\otimes f,y\otimes g]=[x,y]\otimes fg$. Write $A_D=A_{D,1}$ and $\mathfrak j_D=\mathfrak j_{D,1}$. The pinned basis obeys

$$
 [e,f]=h,\qquad [h,e]=2e,\qquad [h,f]=-2f.
$$

Over the original smooth base, the conjugation representation of

$$
 J_0=\operatorname{Res}_{\operatorname{Spec}(R_0[z]/P)/S}
                  \mathrm{SL}_2
 \quad\text{on}\quad
 V_0=\mathfrak{sl}_2\otimes R_0[z]/P
$$

is an algebraic representation on a rank-six vector bundle. Inflating along the arc-to-jet quotient gives an allowed input to (7.2). Its first pullback to $B$ has differential $\rho_P=\operatorname{ad}_{\mathfrak j_P}$. The coefficient comparison $\beta:A_P\to A_Q$ fixes $1,z$ and all scalars of $B$. With both vector bundles displayed in the ordered basis $(e,h,f,ez,hz,fz)$, retaining the action matrices prescribes

$$
 \rho_{\mathrm{copy}}(x)
   =\rho_P(\beta_{\mathfrak g}^{-1}x),
 \qquad \beta_{\mathfrak g}=1_{\mathfrak{sl}_2}\otimes\beta.
 \tag{2}
$$

Equation (2) is a reconstruction of the printed base-linear matrix-copying instruction, not an additional assumption about transport. Ordinary scalar pullback along $p_2$, which replaces coefficients $t^2$ by $(t+\epsilon)^2$, is a different operation.

All currents used below are regular polynomial currents. In the cocycle at [lines 3905–3908](../paper/paper.tex#L3905), their products with their differentials are regular differentials, hence have zero total residue. The central extension splits on arcs, and we take $\chi_J=0$. Thus the prescribed central scalar and character convention leave the tested brackets unchanged.

## Five-item audit

Statuses concern the identified local operation and any explicitly recorded propagation. A downstream failure does not contribute a direct label.

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | downstream | 4342–4346; reliance on `loop:crystal` at 4391–4392 | [MP — Note](#mp--note): descent is applied after its structural-diagram premise has failed; the earlier application of Proposition 7.2 is valid. No independent direct MP failure. |
| G1 | not_violated | none | 3887–3891; 4336–4341 | [G1 — Note](#g1--note): the broad construction already fails for a legal selected input; no separate restriction is dropped by universal introduction. |
| G2 | not_violated | none | 4311–4335 | [G2 — Note](#g2--note): the common-level witness has the stated properties, its dependent constructions remain in scope, and refinement removes its choice. |
| DEF | violated | direct | 4336–4338, with the input contract at 4150–4154 | [DEF — Note](#def--note): the prescribed matrices specify a linear operator assignment that fails the defining representation identity. |
| CONV | violated | direct | 4338–4341, using 3887–3891 | [CONV — Note](#conv--note): expansion of the required coefficient/PBW relation gives a nonzero $\delta h$ correction. |

## MP — Note

The rule is

$$
 \frac{\Gamma\vdash A\qquad\Gamma\vdash A\to B_{\mathrm{MP}}}
      {\Gamma\vdash B_{\mathrm{MP}}}.
$$

There are three distinct operations to separate: an actual application of Proposition 7.2 before the mutation, the new construction itself, and the final application of descent.

**The actual earlier theorem application.** At [lines 4311–4318](../paper/paper.tex#L4311), Proposition 7.2 is used for restriction to a common positive congruence. Instantiate it as follows. Let $\widehat A$ be the common $P$-adic and $Q$-adic completed $B[z]$-algebra, let $\mathcal K=\widehat A[P^{-1}]=\widehat A[Q^{-1}]$, and let $\ell$ be the manuscript's central extension of $\mathfrak{sl}_2\otimes\mathcal K$ with central value $-s$. For a divisor equation $D$, define

$$
 K(D)=\ker\bigl(\mathrm{SL}_2(\widehat A)
                    \longrightarrow\mathrm{SL}_2(\widehat A/(D))\bigr).
$$

Take $K_P=K(P)$, $K_Q=K(Q)$, and $K_*=K(P^3)$. Here $\delta^3=0$, and

$$
 P^3=(Q+\delta)^3=Q(Q^2+3\delta Q+3\delta^2).
 \tag{3}
$$

Consequently $K_*\subset K_P\cap K_Q$. These are normal positive congruences, hence pro-unipotent. Their relative finite quotient Lie modules are respectively built from $(P)/(P^3)$ and $(Q)/(P^3)$; the monic quotients have degree four, so these coefficient modules are free of rank four over $B$. Finite logarithm and exponential identify each group kernel with the trace-zero matrices in its nilpotent coefficient ideal, making both quotients smooth unipotent of finite relative dimension. The regular-arc splitting restricts compatibly and the character is zero.

Let $\mathcal C_J$ be exactly the renormalized category defined at (7.2) for $(\ell,J)$. For each $D=P,Q$, substitute

$$
 (\text{base},\text{Tate Lie algebra},\text{larger group},
         \text{smaller group},\chi)
   =(B,\ell,K_D,K_*,0)
$$

into Proposition 7.2(4), using its finite-flat base-extension clause. In this application:

- $\Gamma_{\mathrm{res}}$ consists of the fixed global curve/group/level data above, the smooth base $S$, the displayed finite-flat diagonal $B$, the monic equations (1), their cofinal full algebras, the canonical arc splitting, and Proposition 7.2 with its stated range. It contains no assumption that $\beta$ preserves products or brackets.
- $\mathsf A_D$ says that $K_D$ and $K_*$ are allowed pro-unipotent compact opens in that same full arc group, $K_*\subset K_D$, the quotient $K_D/K_*$ is smooth and finite dimensional, and the central/character splittings agree. Every component is established above.
- $\mathsf B_D$ says that the actual restriction $\operatorname{Res}^{K_D}_{K_*}:\mathcal C_{K_D}\to\mathcal C_{K_*}$ preserves compact objects, is fully faithful, and has a continuous right adjoint.
- The conclusion $\mathsf C_D$ claimed at lines 4316–4318 is precisely this $\mathsf B_D$. The logical formula $\mathsf A_D$ is distinct from the coefficient algebra $A_D$.

The instantiated fragment is therefore

$$
 \Gamma_{\mathrm{res}}\vdash\mathsf A_D,
 \qquad \Gamma_{\mathrm{res}}\vdash\mathsf A_D\to\mathsf B_D,
 \qquad \Gamma_{\mathrm{res}}\vdash\mathsf B_D.
$$

This application is sound and uses the pro-unipotent restriction of the theorem exactly as printed. It supplies restriction functors on already existing representations and Harish--Chandra modules.

**The planted operation.** At lines 4336–4338 the manuscript gives the algorithm (2). Its mathematical form is introduction of a named object with a structural contract:

$$
 \rho_{\mathrm{copy}}:\mathfrak j_Q\longrightarrow
       \operatorname{End}_B(B^6),\qquad
 \rho_{\mathrm{copy}}(x)=\rho_P(\beta_{\mathfrak g}^{-1}x),
 \quad \rho_{\mathrm{copy}}\stackrel{\mathrm{claimed}}{\in}
       \operatorname{Rep}_{\mathrm{Lie},B}(\mathfrak j_Q).
$$

The last membership means, explicitly,

$$
 \forall x,y\in\mathfrak j_Q,
 \quad [\rho_{\mathrm{copy}}(x),\rho_{\mathrm{copy}}(y)]
       =\rho_{\mathrm{copy}}([x,y]_Q).
 \tag{4}
$$

It fails for $x=ez,y=fz$, as computed below. No cited theorem at this location asserts that a base-linear map of coefficient modules transports representations. Recasting the algorithm as an invented implication “linear isomorphism implies Lie-representation transport” would add a theorem application to the text. The direct obligation actually present is the validity of the prescribed representation and its coefficient computation.

**The downstream implication application.** The inference at [lines 4342–4343](../paper/paper.tex#L4342) does have MP form. This is a reconstruction of the formal-diagonal descent invoked there. For each finite infinitesimal multiple diagonal $T$, denote its projections by $p_i:T\to S$, its pulled-back categories by $\mathcal E_i$, and the prescribed comparison functors by $\tau_{ij}:\mathcal E_i\to\mathcal E_j$. Let $\Gamma_{\mathrm{desc}}$ consist of the actual smooth $S$, the underlying categories and functors of (7.2), the finite-flat formal-diagonal system, the valid common-level restriction results, and the descent/crystal equivalence recalled at [lines 3944–3948](../paper/paper.tex#L3944). The required antecedent $A_{\mathrm{desc}}$ is the conjunction that:

$$
\begin{gathered}
 \text{each inducing input used by every }\tau_{ij}
       \text{ is an algebraic representation of the target group};\\
 \text{each }\tau_{ij}\text{ is a well-defined equivalence of the stated categories};\\
 \tau_{ii}\simeq\operatorname{Id},\qquad
 \tau_{jk}\tau_{ij}\simeq\tau_{ik},
 \quad\text{with the higher associativity coherences};\\
 \text{these maps commute with all formal-diagonal pullbacks and
 the restriction and induction functors.}
\end{gathered}
$$

The consequent $B_{\mathrm{desc}}$ is that these particular categories and functors descend to a crystal over $S$, whose sections are $D(S)$-linear and have the given underlying categories. This is the conclusion $C_{\mathrm{desc}}$ claimed there, not a strengthened consequent. The attempted fragment is

$$
 \Gamma_{\mathrm{desc}}\vdash A_{\mathrm{desc}}\to B_{\mathrm{desc}},
 \qquad
 \Gamma_{\mathrm{desc}}\mathrel{\not\vdash}A_{\mathrm{desc}},
 \qquad
 \text{the manuscript claims }C_{\mathrm{desc}}=B_{\mathrm{desc}}.
$$

The first failed obligation is the antecedent: its representation and structural-diagram components were falsely supplied at lines 4336–4341. The implication itself and its consequent are the appropriate ones. This is a **downstream MP failure**, with the DEF/CONV failure as its explicit provenance, rather than a further direct label. The use of `loop:crystal` at [lines 4391–4392](../paper/paper.tex#L4391) inherits the same gap.

## G1 — Note

The relevant rule is

$$
 \frac{\Gamma\vdash A\to B_1(x)}
      {\Gamma\vdash A\to\forall x\,B_1(x)},
 \qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(A).
$$

The target does not establish compatibility for a specially restricted representation and then remove that restriction. It prescribes a construction directly on the actual inducing range. The following formalization makes both that range and the failed preliminary obligation explicit.

Fix $R_0,S,B,p_1$, the two monic polynomials $P,Q$, a finite jet order $n$, and the arc splitting with zero character. Let $\Gamma_1$ consist of these fixed data, their common full curve, and the unique monic coefficient presentations. These are parameters, not variables to be generalized in the next step. Define the source jet groups before and after scalar extension by

$$
 J_{0,n}=\operatorname{Res}_{\operatorname{Spec}(R_0[z]/P^n)/S}
                       \mathrm{SL}_2,\qquad
 J_{P,n}=p_1^*J_{0,n}.
$$

Let $x=(W_0,\sigma_0)$ range over finite free $R_0$-modules with a chosen basis and identity-preserving algebraic maps $\sigma_0:J_{0,n}\to\mathrm{GL}_{R_0}(W_0)$. Define the range predicate $D(x)$ by the group-law identity $\sigma_0(gh)=\sigma_0(g)\sigma_0(h)$ on all base extensions. Thus $D(x)$ asserts exactly that this is an algebraic group representation on the original smooth base. Put $W=B\otimes_{R_0,p_1}W_0$ and $\sigma=p_1^*\sigma_0$. Working locally with free vector bundles is sufficient for the manuscript's vector-bundle range and includes the counterexample. No horizontality or annihilation of coefficient defects is included. Inflation to arcs and then this scalar extension are actual allowed inducing operations.

Write $\beta_n(z^rP^j)=z^rQ^j$ for the base-linear coefficient comparison, and $\beta_{\mathfrak g,n}=1_{\mathfrak{sl}_2}\otimes\beta_n$.

For such a pair, the printed recipe specifies

$$
 T(x)(y)=d\sigma(\beta_{\mathfrak g,n}^{-1}y),
 \qquad y\in\mathfrak j_{Q,n}.
$$

Let $P_1(x)$ mean that this operator assignment is the differential of an algebraic $J_{Q,n}$-representation on $W$, so in particular it satisfies all target brackets, and that its claimed coefficient maps define the compatible induction comparison. The universal content of the instruction is

$$
 \forall x\,\bigl(D(x)\to P_1(x)\bigr).
 \tag{5}
$$

To put (5) in the requested G1 form, take $A=\top$ and $B_1(x)=D(x)\to P_1(x)$. The pre-generalization derivation implicit in the construction would have to be

$$
\begin{array}{ll}
 x_0=(W_0,\sigma_0) & \text{fresh arbitrary pair},\\
 [D(x_0)] & \text{open range assumption},\\
 T(x_0)=d\sigma\circ\beta_{\mathfrak g,n}^{-1}
       & \text{well-defined linear operator assignment},\\
 P_1(x_0) & \text{claimed at 4336–4341; this line fails},\\
 D(x_0)\to P_1(x_0) & \text{would discharge }D(x_0),\\
 \top\to\forall x(D(x)\to P_1(x)) & \text{would universally introduce }x.
\end{array}
$$

All dependence on the selected representation is contained in $x_0$ and its defined quantities $W,\sigma,T(x_0)$. After discharging $D(x_0)$, the fixed parameters are $R_0,S,B,p_1,P,Q,n$, the pinned group and level, and the prescribed coefficient bases; $x_0$ is free in neither $\Gamma_1$ nor $A$. There is no extra assumption such as $n=1,m=1$, $P=Q$, $\epsilon^2=0$, or trivial source action that is dropped in passing to (5). The admissible selected pair $x_0=(V_0,\operatorname{Ad}_{J_0})$, with $n=1$ and $W=B^6$, already violates $P_1(x_0)$ before universal introduction: its bracket defect on $e$ is $-2\delta e$.

For comparison, the actual coefficient assertion at [lines 3887–3891](../paper/paper.tex#L3887) has a valid arbitrary-input structure. For a fresh coefficient array $a=(a_{rj})\in B^{mn}$, define

$$
 F_P(a)=\sum_{r,j}a_{rj}z^rP^j,
 \qquad F_Q(a)=\sum_{r,j}a_{rj}z^rQ^j.
$$

Unique monic expansion gives $\beta_n(F_P(a))=F_Q(a)$. The coefficient array is unrestricted, and the range can be retained explicitly as

$$
 \Gamma_1\vdash\top\to
 \forall a\bigl(a\in B^{mn}\to\beta_n(F_P(a))=F_Q(a)\bigr).
$$

Here the domain assumption $a\in B^{mn}$ is discharged into the conditional, and $a$ is absent from the remaining assumptions. This sound universal statement concerns a linear map.

Thus the failing universal claim in (5) is the range of an invalid pointwise construction, rather than a separate G1 inference from a special successful instance. The report assigns **no direct G1 violation**: the explicit failure is the representation construction and the coefficient computation already present before any generalization. In particular, success on the reduced fiber or on the first-order collision fiber is a diagnostic observation in the reports, not a premise from which the manuscript generalizes.

## G2 — Note

The relevant rule is

$$
 \frac{\Gamma\vdash A_2(x)\to B_2}
      {\Gamma\vdash(\exists x\,A_2(x))\to B_2},
 \qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(B_2).
$$

The genuine existential choice near the target is the common deeper congruence at [lines 4311–4318](../paper/paper.tex#L4311), repeated for finitely many lifts at [lines 4333–4335](../paper/paper.tex#L4333). The witness is a subgroup, not a new representation. Here is its scope and the conclusion for which its existence actually suffices.

Fix the global data, a finite infinitesimal comparison base with nilpotent ideal $I$, and a finite list of lifted equations $P_i\equiv P_1\pmod I$. To formalize comparison of the lifts of one selected positive congruence stage, fix $n\geq1$ and put $J_i=K(P_i^n)$; the explicit witness uses $n=1$. These levels have the same reduction modulo $I$, exactly the coincidence used at line 4322. Let $\Gamma_2$ contain those fixed objects, the common full arc/Laurent algebra and splitting, Proposition 7.2's restriction result, and the integrability calculation at [lines 4320–4331](../paper/paper.tex#L4320). The latter concerns actual Lie modules: the finite filtration by $I^aM$ has identical integrability conditions on its successive quotients, and pro-unipotent integrability is preserved under extensions. It establishes equality of the essential images of the genuine restriction functors for these lifts. There is no coefficient-copying assertion in $\Gamma_2$.

Let the witness $x=K$ range over normal pro-unipotent congruence subgroups of the common full arc group. The supplied predicate is

$$
 A_2(K):\quad K\subseteq\bigcap_iJ_i,
 \quad J_i/K\text{ smooth finite dimensional for every }i,
 \quad\text{the canonical splittings restrict compatibly}.
 \tag{6}
$$

Existence is concrete. If $I^r=0$, choose

$$
 N\geq n+r-1,\qquad K=K(P_1^N).
$$

The cofinal-ideal calculation gives $P_1^N\in(P_i^n)$, and monic quotients give the finite locally free lattice differences. The positive congruence quotients have the smooth unipotent structure used by the manuscript. For the two explicit first-depth levels in this review, $K(P^3)$ is such a witness, by (3). For a finite diagram involving several original stages, one takes the maximum of their bounds to obtain a common refinement; equality of essential images here concerns the lifts of the same stage, not arbitrary unrelated depths.

For two levels, write $\mathcal C_i=\mathcal C_{J_i}$. The witness-dependent quantities are

$$
 R_{i,K}:\mathcal C_i\longrightarrow\mathcal C_K,
 \quad \mathcal I_K=\operatorname{im}R_{1,K}
                  =\operatorname{im}R_{2,K},
 \quad F_K=\overline R_{2,K}^{\,-1}R_{1,K},
$$

where $\overline R_{2,K}:\mathcal C_2\xrightarrow{\sim}\mathcal I_K$ is the corestriction of $R_{2,K}$, and $R_{1,K}$ is also viewed with codomain $\mathcal I_K$ in this composite. The inverse is an inverse equivalence onto the full essential image, not a chosen inverse linear coefficient map. Let $B_2$ be the following witness-independent statement:

$$
 \exists F:\mathcal C_1\xrightarrow{\sim}\mathcal C_2
 \quad\forall L\,
 \left(A_2(L)\to
    R_{2,L}F\simeq R_{1,L}\right),
 \tag{7}
$$

where the displayed identifications commute with restriction to smaller common levels. For multiple lifts the same statement supplies $F_{ij}$ with $F_{jk}F_{ij}\simeq F_{ik}$, using the same actual restrictions.

The existential-elimination subderivation corresponding to the unchanged common-level argument is:

$$
\begin{array}{ll}
 [\exists K\,A_2(K)] & \text{existential premise},\\
 \quad [A_2(k_0)] & k_0\text{ fresh; open witness scope},\\
 \quad R_{1,k_0},R_{2,k_0}\text{ fully faithful}
       & \text{Proposition 7.2 with (6)},\\
 \quad\operatorname{im}R_{1,k_0}=\operatorname{im}R_{2,k_0}
       & \text{the finite nilpotent filtration argument},\\
 \quad F_{k_0}=\overline R_{2,k_0}^{\,-1}R_{1,k_0}
       & \text{equivalence on these essential images},\\
 \quad\forall L\,(A_2(L)\to R_{2,L}F_{k_0}\simeq R_{1,L})
       & \text{comparison through a common refinement},\\
 \quad B_2 & \exists F\text{-introduction using }F_{k_0},\\
 B_2 & \exists K\text{-elimination, discharging }A_2(k_0),\\
 (\exists K\,A_2(K))\to B_2 & \text{discharging the existential premise}.
\end{array}
$$

The refinement line is precise: for $k_0,L$, choose a deeper normal $H\subset k_0\cap L$; the two restrictions to $\mathcal C_H$ agree by actual inclusion of Lie/group data. The fully faithful restriction $\mathcal C_L\to\mathcal C_H$ identifies the comparison uniquely. Further refinements give the same map, and compositions of actual restrictions supply its coherence. The argument applies on morphisms and natural comparison maps as well as objects.

The free parameters in $\Gamma_2$ are the base, the finite list $(P_i)$, the selected depth $n$, the group/level and the full algebras. Neither $k_0$ nor $F_{k_0}$ remains free in (7): $F$ is existentially bound and $L$ universally bound. The temporary refinement $H$ also stays inside the comparison subderivation. Thus the eigenvariable condition holds. The quantifier order used is

$$
 \forall\text{ finite lists of lifts of a selected level}\;\exists K\;A_2(K),
$$

not a single $K$ chosen before all lists or all infinitesimal orders.

This identifies the valid existential step already present in the submitted proof; it does not replace the added paragraph with a repaired one. The new $\rho_{\mathrm{copy}}$ is defined before its restriction and independently of which common $K$ was selected. Predicate (6) supplies no assertion that $\beta$ preserves the bracket, and the text does not prove such an assertion from a specially chosen witness. Its failure is therefore located in the added construction, not in witness discharge or a change of quantifier order. **G2 is not violated at the common-level choice.**

## DEF — Note

There are two legitimate linear objects and one failed structural object at the planted step.

**Finite jets and coefficient transport.** For a monic $D\in B[z]$ of degree $m$, the quotient $A_{D,n}=B[z]/(D^n)$ is a well-defined finite free $B$-algebra. Repeated monic division writes each residue class uniquely as

$$
 \sum_{j=0}^{n-1}f_j(z)D^j,\qquad \deg f_j<m.
$$

For uniqueness, if a nonzero such expression were divisible by the monic polynomial $D^n$, its largest nonzero $j$-term would have degree $mj+\deg f_j<mn$, whereas any nonzero multiple of $D^n$ has degree at least $mn$. Monicity makes this degree argument valid over the nonreduced ring $B$. Thus the displayed coefficients depend only on the residue class. This establishes existence, uniqueness and representative independence of the basis and of

$$
 \beta_n:A_{P,n}\longrightarrow A_{Q,n},
 \qquad \sum a_{rj}z^rP^j\longmapsto\sum a_{rj}z^rQ^j.
 \tag{8}
$$

Its domain and codomain are finite free modules of rank $mn$. It is $B$-linear, preserves the unit, has inverse $\beta_{Q,P,n}$, and commutes with truncation by deleting the high $j$-terms. For a third lifted equation $D$, coefficient copying gives $\beta_{Q,D,n}\beta_{P,Q,n}=\beta_{P,D,n}$ as linear maps. There is no recursive or representative-choice defect in (8).

**The intended lifted representation.** The group $J_D=\operatorname{Res}_{A_D/B}\mathrm{SL}_2$, its Lie algebra $\mathfrak j_D$, and its true adjoint action are separately well-defined. Conjugation on traceless $2\times2$ matrices over $A_D$ supplies an actual algebraic group action; it differentiates to $\operatorname{ad}_{\mathfrak j_D}$. The source in (2) is the base extension of precisely such an action over the smooth $S$, so it satisfies the input contract of (7.2).

The construction at [lines 4336–4338](../paper/paper.tex#L4336) requires its output to be an algebraic representation of the lifted group $J_Q$, on the coefficient-identified rank-six bundle. Equation (2) uniquely specifies a $B$-linear map to $\operatorname{End}_B(B^6)$. To have the required codomain of **representations**, it must satisfy (4), a necessary condition for the differential of a group homomorphism. For the two permitted generators,

$$
 [ez,fz]_P=t^2h,
 \qquad [ez,fz]_Q=(t+\epsilon)^2h.
$$

Because the source action is a representation,

$$
\begin{aligned}
 [\rho_{\mathrm{copy}}(ez),\rho_{\mathrm{copy}}(fz)]
   &=t^2\rho_P(h),\\
 \rho_{\mathrm{copy}}([ez,fz]_Q)
   &=(t+\epsilon)^2\rho_P(h),\\
 \bigl([\rho_{\mathrm{copy}}(ez),\rho_{\mathrm{copy}}(fz)]
       -\rho_{\mathrm{copy}}([ez,fz]_Q)\bigr)e
   &=-2\delta e=-(4t\epsilon+2\epsilon^2)e\ne0.
\end{aligned}
 \tag{9}
$$

The coefficient $4t\epsilon+2\epsilon^2$ is nonzero in the free $\mathbb C[t]$-module with basis $1,\epsilon,\epsilon^2$, and $e$ belongs to a free $B$-basis. This is already a failure over the actual finite-flat diagonal, before specialization.

On the collision fiber, set $R_c=B/(t)=\mathbb C[\epsilon]/\epsilon^3$. The two algebras become

$$
 R_c[z]/z^2,\qquad R_c[z]/(z^2-\epsilon^2).
$$

The copied $ez$ and $fz$ operators send the constant summand into the $z$-summand and kill the latter; their composites in both orders are zero. The required target bracket nevertheless sends $e$ to $2\epsilon^2e\ne0$. Specializing an asserted equality of matrices preserves equality, so this fiber also certifies the failure. No flatness of the specialization $B\to R_c$ is needed for that elementary test.

**Positive congruences also supply legal inputs.** To meet the narrower pro-unipotent setting of the common-depth argument, take

$$
 V_0^{(4)}=\mathfrak{sl}_2\otimes R_0[z]/(P^4)
$$

with its adjoint action restricted to the finite smooth unipotent group

$$
 \ker\bigl(\operatorname{Res}_{R_0[z]/P^4\,/\,R_0}\mathrm{SL}_2
       \longrightarrow
       \operatorname{Res}_{R_0[z]/P\,/\,R_0}\mathrm{SL}_2\bigr).
$$

This is a rank-24 vector-bundle representation, inflated to the positive congruence. Its target currents $ezQ,fzQ$ are copied from $ezP,fzP$. Since $z^2=P+t^2=Q+(t+\epsilon)^2$,

$$
 [ezP,fzP]_P=hP^3+t^2hP^2,
 \qquad [ezQ,fzQ]_Q=hQ^3+(t+\epsilon)^2hQ^2.
$$

The copied action has defect $-\delta\operatorname{ad}_P(hP^2)$, which sends the constant vector $e$ to

$$
 -2\delta eP^2,
 \qquad\text{and at }t=0\text{ to }-2\epsilon^2 eP^2\ne0.
 \tag{10}
$$

Thus the construction fails even when its source inducing group is pro-unipotent. Restriction is ordered after the purported lifted representation is obtained. A sufficiently deep restriction may kill some operators of a finite-stage action, but it does not provide the required preceding representation of the lifted inducing group with the specified matrices.

The failed requirement is **existence of a representation with the prescribed action matrices**. The underlying module and linear operator assignment exist uniquely. The assertion that the output is a representation is part of the construction contract, rather than a later optional property of an already valid representation. Let $j_Q$ denote the Lie algebra of the full target inducing arc or congruence group, whose prescribed action factors through the tested finite quotient. Then $U(\ell)\otimes_{U(j_Q)}V_{\mathrm{copy}}$ cannot use these matrices as a $U(j_Q)$-module action: its defining Lie relations fail. This certifies **DEF as a direct violation**.

The valid full-algebra identification in the surrounding proof does not identify (8) with an algebra map at a fixed jet order. Indeed, for the genuine source action viewed on the common full arcs,

$$
 \rho_P(xQ)=\rho_P(x(P-\delta))=-\delta\rho_P(x),
 \qquad x\in\mathfrak{sl}_2,
 \tag{11}
$$

whereas a first-$Q$-jet action kills $xQ$. Formula (11) retains the divisor-change term. The preceding equality-of-essential-images argument, the fixed-$z$ derivative at [lines 4348–4353](../paper/paper.tex#L4348), and the later absolute-BRST comparison at [lines 5311–5326](../paper/paper.tex#L5311) use the full algebra; none proves the missing bracket identity for the newly prescribed matrices.

## CONV — Note

The manuscript's exact starting presentation is

$$
 \sum_{0\leq r<m,\;0\leq j<n}a_{rj}z^ru^j,
 \qquad u=P(z),
$$

with coefficients retained when $u$ is replaced by the lifted equation. Its claimed endpoint is the assertion at [lines 4338–4341](../paper/paper.tex#L4338) that the PBW and group-cobar constructions therefore use identical coefficient diagrams and their comparisons intertwine induction. The following equations reconstruct the multiplication, bracket, and action components required by that exact assertion. They are not claimed to be displayed equations of the manuscript.

At $n=1$, evaluate the coefficient multiplication diagram on $z\otimes z$. Its two routes are

$$
\begin{aligned}
 (\beta\circ\mu_P)(z\otimes z)
     &=\beta(z^2\bmod P)
       =\beta(t^2\cdot1)=t^2\cdot1,\\
 (\mu_Q\circ(\beta\otimes\beta))(z\otimes z)
     &=z\cdot_Q z
       =z^2\bmod Q
       =(t+\epsilon)^2\cdot1\\
     &=(t^2+2t\epsilon+\epsilon^2)\cdot1.
\end{aligned}
 \tag{12}
$$

The first false component equality is therefore

$$
 \beta(z\cdot_P z)
       \stackrel{\mathrm{claimed\ diagram}}{=}
       \beta(z)\cdot_Q\beta(z).
$$

The right side minus the left side is $\delta\cdot1\ne0$. At higher jets the same calculation reads $\beta_n(z^2)=Q+t^2$ while $z^2=Q+(t+\epsilon)^2$, so increasing the displayed basis alone does not change the discrepancy.

For the current bracket this gives all intermediate steps

$$
\begin{aligned}
 \beta_{\mathfrak g}([ez,fz]_P)
   &=\beta_{\mathfrak g}([e,f]\otimes(z\cdot_P z))
     =\beta_{\mathfrak g}(h\otimes t^2)
     =t^2h,\\
 [\beta_{\mathfrak g}(ez),\beta_{\mathfrak g}(fz)]_Q
   &=[e,f]\otimes(z\cdot_Qz)
     =h\otimes(t+\epsilon)^2
     =t^2h+\delta h.
\end{aligned}
 \tag{13}
$$

Thus the difference is $\delta h$, not zero. This is a calculation with the actual coefficient multiplication, rather than a use of a separate theorem asserting transport.

The matrix expansion confirms that a permitted source representation detects this coefficient difference. In the ordered root basis $(e,h,f)$, set

$$
 E=\operatorname{ad}(e)=
 \begin{pmatrix}0&-2&0\\0&0&1\\0&0&0\end{pmatrix},\quad
 F=\operatorname{ad}(f)=
 \begin{pmatrix}0&0&0\\-1&0&0\\0&2&0\end{pmatrix},\quad
 H=\operatorname{ad}(h)=\operatorname{diag}(2,0,-2).
$$

Multiplication gives

$$
 EF=\operatorname{diag}(2,2,0),\qquad
 FE=\operatorname{diag}(0,2,2),\qquad EF-FE=H.
$$

Put $a=t^2$, $b=(t+\epsilon)^2$. The copied operators on $B^3\oplus zB^3$ are

$$
 X=\rho_{\mathrm{copy}}(ez)=
   \begin{pmatrix}0&aE\\E&0\end{pmatrix},\qquad
 Y=\rho_{\mathrm{copy}}(fz)=
   \begin{pmatrix}0&aF\\F&0\end{pmatrix}.
$$

Hence

$$
 XY=\begin{pmatrix}aEF&0\\0&aEF\end{pmatrix},\quad
 YX=\begin{pmatrix}aFE&0\\0&aFE\end{pmatrix},\quad
 [X,Y]=a\begin{pmatrix}H&0\\0&H\end{pmatrix}.
$$

But expansion of the target bracket gives

$$
 \rho_{\mathrm{copy}}([ez,fz]_Q)
       =b\begin{pmatrix}H&0\\0&H\end{pmatrix}.
$$

The operator discrepancy is therefore

$$
 (a-b)\begin{pmatrix}H&0\\0&H\end{pmatrix}
 =-\delta\begin{pmatrix}H&0\\0&H\end{pmatrix},
$$

whose first diagonal entry is $-4t\epsilon-2\epsilon^2$, proving (9). Replacing $a$ by $b$ also in the operators gives the genuine target adjoint action and verifies the target relation; the issue is retaining the source matrices.

For the rank-24 witness, let $N$ be multiplication by $P$ on the coefficient basis $1,z,P,zP,P^2,zP^2,P^3,zP^3$, and let $Z_a$ be multiplication by $z$. They satisfy

$$
 N^4=0,\qquad Z_aN=NZ_a,\qquad Z_a^2=N+a\operatorname{Id}.
$$

With the same basis labels for the target, multiplication by $Q$ has the same matrix $N$, but $Z_b^2=N+b\operatorname{Id}$. Thus copying the positive-current operators gives

$$
\begin{aligned}
 [Z_aN\otimes E,Z_aN\otimes F]
   &=(Z_aN)^2\otimes(EF-FE)\\
   &=(N^3+aN^2)\otimes H,\\
 \rho_{\mathrm{copy}}([ezQ,fzQ]_Q)
   &=(N^3+bN^2)\otimes H.
\end{aligned}
$$

Their difference is $-\delta N^2\otimes H$, giving (10). This calculation includes the nonzero $P^3$ term in the positive-depth source bracket.

There is also a direct PBW relation test. In the tensor algebra on $\mathfrak j_P$, the relation

$$
 r_P=(ez)(fz)-(fz)(ez)-t^2h
$$

maps to zero in $U(\mathfrak j_P)$. The tensor-algebra map on generators induced by $\beta_{\mathfrak g}$, followed by the target quotient, sends it to

$$
 (ez)(fz)-(fz)(ez)-t^2h
   =[ez,fz]_Q-t^2h
   =(b-a)h=\delta h
       \quad\text{in }U(\mathfrak j_Q).
 \tag{14}
$$

The Lie algebra $\mathfrak j_Q$ is finite free over the characteristic-zero base $B$, so PBW injects it into its enveloping algebra. The element $\delta h$ is nonzero there. Thus the alleged coefficient comparison does not descend to the enveloping-algebra map required for induction. The application of PBW to establish nonvanishing is valid; the failed computation is the image of the defining relation. On the collision fiber it is $\epsilon^2h$, while the source relation has zero bracket term.

The action component of a compatible cobar diagram also fails before higher coherences can be checked. Its differentiated representation condition is (4). Equivalently, the Lie cochain expression built from the copied action has

$$
 (d_{\rho}^{\,2}v)(x,y)
   =\rho(x)\rho(y)v-\rho(y)\rho(x)v-\rho([x,y])v,
 \qquad
 (d_{\rho}^{\,2}e)(ez,fz)=-2\delta e.
$$

This is the necessary differentiated action diagram, not an identification of the entire group-cobar complex with a Lie complex. The explicit PBW failure (14) already contradicts the printed claim of identical coefficient diagrams. The calculation is therefore a **direct CONV violation**, independently of the construction-contract failure recorded under DEF.

The surrounding cofinality computation is correct. In this witness,

$$
 Q^{n+2}=(P-\delta)^{n+2}
   =\sum_{k=0}^{2}\binom{n+2}{k}P^{n+2-k}(-\delta)^k
       \in(P^n),
$$

because $\delta^3=0$; the symmetric inclusion follows in the same way. It identifies the completed full algebras, and does not assert (12) at a fixed jet order.

I independently checked the displayed block-matrix calculations over $\mathbb Z[\epsilon]/\epsilon^3$, at $t=0$ and $t=1$, for ranks six and 24. The genuine source and target brackets agreed with their respective multiplication tables; the copied-action defect on the stated basis vector was $-2\epsilon^2$ at $t=0$ and $-4\epsilon-2\epsilon^2$ at $t=1$. I also reran the supplied [checker calculation](checker_calculation.py): its checks of all 36 ordered basis-pair relations for each genuine rank-six action and all 324 positive-congruence relations for each genuine rank-24 action passed, together with its assertions of the symbolic defects in (9)–(10).

At the collision fiber, reduction modulo $\epsilon^2$ erases this particular defect. Over the full $t$-family the first-order term $-4t\epsilon e$ remains. This qualification agrees with the existing checker and follows directly from (9).

## Final direct labels and comparison with the existing classification

**Final direct labels: DEF, CONV.** There is no G subtype and no direct MP label.

These labels agree with the [case README](../README.md), the [tricker's proposed classification](tricker_report.md), and the [original checker's classification](checker_report.md). The present review makes the logical propagation explicit: MP is recorded as a downstream failed antecedent at descent, while the common-level existential choice and the scope of universal claims do not supply separate direct quantifier-rule errors.

The direct failures are distinct obligations at adjacent locations. Lines 4336–4338 fail to construct an algebraic inducing representation with the specified matrices; lines 4338–4341 falsely identify the multiplication/bracket diagrams required by PBW induction. The coefficient module isomorphism itself is valid. Equations (9), (10), and (14) certify both direct labels under the manuscript's actual collision and finite-flat hypotheses.

The proof subsequently consumes the affected structure in the strong loop action at [lines 4391–4392](../paper/paper.tex#L4391), parameter operations at [lines 4701–4707](../paper/paper.tex#L4701), relative Skryabin transport at [lines 5311–5326](../paper/paper.tex#L5311), the common-target descent at [lines 5493–5497](../paper/paper.tex#L5493), and localization at [lines 6592–6607](../paper/paper.tex#L6592). These are consequences of the missing structural comparison, not additional direct labels for the same planting.

No mathematical issue remains unresolved for the local failure or the final direct classification.
