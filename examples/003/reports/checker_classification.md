# 003: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow. It is informed by the source and existing construction/checker materials, rather than an original workflow report or a blind reviewer run. Reviewer verdicts and detection counts are outside this review.

The complete modified manuscript was read, its original was compared in full, and the [mutation](../mutation.diff), [tricker report](tricker_report.md), [checker report](checker_report.md), and [case description](../README.md) were examined under the [classification standard](../../../protocol/classification.md). The finite group, surface relation, character discrepancy, and geometric nonvanishing argument below were independently checked.

## Exact target and actual assumptions

The sole source difference is [line 8694](../paper/paper.tex#L8694), in §13.5:

$$
 [qz,x]=[q,zx]
 \quad\longmapsto\quad
 [qz,x]=[q,z^{-1}x].
$$

The [original passage](../original/paper.tex#L8692) and all subsequent formulas have otherwise identical text. The first incompatible calculation is at [lines 8777–8784](../paper/paper.tex#L8777): changing a lift by $z$ is said to change the translated frame by $z$, and this is used to construct

$$
 \tau_Q^!L(V)\simeq L(V[Q]). \tag{1}
$$

The intended construction is a comparison natural in the torsor groupoid, not just an isomorphism after choosing a trivialization. It feeds into [Theorem 13.5, equation (13.7)](../paper/paper.tex#L8733):

$$
 \Phi\tau_Q^!\simeq u_Q^{-1}\otimes\Phi,
 \qquad
 \tau_{Q'}^!\Phi\simeq\Phi(u'_{Q'}\otimes-), \tag{2}
$$

with naturality for all torsor isomorphisms and automorphisms and compatibility with tensor products. The final automorphism check at [lines 8919–8926](../paper/paper.tex#L8919) repeats the same sign error.

The actual hypotheses are: a smooth projective connected complex curve $X$; a connected simple complex algebraic group $G$ with its actual global form and full dual root datum; fixed dual pinnings and a theta characteristic; and $c\in\mathbb C\setminus\mathbb Q$. Write

$$
 \begin{gathered}
 a=-c,\qquad d=(ra)^{-1},\qquad
 k_a=a-h^\vee,\qquad k_d=d-\check h^\vee,\\
 s=-k_a/(2h^\vee),\qquad s'=-k_d/(2\check h^\vee),\\
 Y_H=\operatorname{Bun}_H(X),\qquad
 L_H|_E=\det R\Gamma(X,\mathfrak h_E),\\
 A=D(L_G^s),\quad A'=D(L_G^{-s}),\quad
 B=D(L_{G^\vee}^{-s'}),\quad B'=D(L_{G^\vee}^{s'}).
 \end{gathered}
$$

These are the [level and category definitions](../paper/paper.tex#L305), also recalled at [lines 8322–8335](../paper/paper.tex#L8322). All components and central characters are retained, and the finite center acts trivially on the adjoint determinant ([lines 338–348](../paper/paper.tex#L338)). The inertia-vanishing lemma has a different hypothesis: a central $\mathbb G_m$ must act on the twisting line with a **nonzero** integral weight ([lines 364–370](../paper/paper.tex#L364)). It does not remove the finite-center sector used below.

The following conventions remain fixed throughout the manuscript:

- Localization carries a KL central character to bundle inertia **without inversion** ([lines 8645–8652](../paper/paper.tex#L8645)).
- The already constructed equivalence sends $(\eta,p)$ to $(p,-\eta)$, with character first and component second ([Proposition 13.4](../paper/paper.tex#L8635)).
- Transgression is $[u_Q]=\int_X\langle[Q]\cup\operatorname{obs}\rangle$, with $Q$ first; the integral of the obstruction is the specified bundle component; associated-line transport by $z$ has scalar $\gamma(z)$ ([lines 8699–8731](../paper/paper.tex#L8699)).
- The $!$-pullback convention is the sheaf/left-crystalline convention at [lines 289–303](../paper/paper.tex#L289). On a finite residual gerbe, evaluating an inertia automorphism acts by its given representation. No dualization is inserted into this evaluation.

The full-source check found no additional center-exponent, character, or curve restriction that changes these hypotheses. The local $W$-algebra comparisons, determinant normalizations, and integral determinant transport retain the actual group data. The [final determinant-transport argument](../paper/paper.tex#L8928) uses the adjoint bundle and hence supplies no extra finite-center character.

## Verified admissible witness

Take

$$
 \begin{gathered}
 G=\mathrm{SL}_3(\mathbb C),\qquad G^\vee=\mathrm{PGL}_3(\mathbb C),
 \qquad Z_G=\mu_3,\qquad r=1,\qquad h^\vee=\check h^\vee=3,\\
 g(X)=2,\qquad c=-\sqrt2,\quad a=\sqrt2,\quad d=1/\sqrt2,
 \quad s=(3-\sqrt2)/6,\quad s'=(3-1/\sqrt2)/6,\\
 Q_0=X\times\mu_3,\qquad q_0=(1\text{ in each fiber}),\qquad
 \zeta^2+\zeta+1=0,\quad\zeta\ne1,\quad\eta(\zeta)=\zeta.
 \end{gathered}
$$

The theta characteristic and dual pinnings may be fixed as required. Both twists are irrational, $\pi_1(\mathrm{SL}_3)=0$, and $\pi_1(\mathrm{PGL}_3)=X^*(\mu_3)$.

Here is a nonzero object in the actual $\eta$-sector, including the geometric nonvanishing argument. Put

$$
 A_0=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},
 \qquad B_0=\operatorname{diag}(1,\zeta,\zeta^2).
$$

Direct multiplication gives

$$
 A_0^3=B_0^3=I,\qquad \det A_0=\det B_0=1,
 \qquad [A_0,B_0]=\zeta^2I,\qquad[B_0,A_0]=\zeta I.
$$

The matrices $\zeta^kA_0^iB_0^j$, $0\le i,j,k<3$, form a group $H$ of order $27$. Different $i$ have different permutation supports; for fixed $i$, the diagonal phases distinguish $j,k$. Its action on $\mathbb C^3$ is irreducible: every $B_0$-invariant subspace is a sum of its distinct eigenlines, and the cycle $A_0$ preserves only the empty and full such sums. The assignments

$$
 a_1\mapsto A_0,\quad b_1\mapsto B_0,\quad
 a_2\mapsto B_0,\quad b_2\mapsto A_0
$$

satisfy $[a_1,b_1][a_2,b_2]=1$ and have image $H$. The corresponding connected finite étale cover $\pi:Y\to X$ gives

$$
 E=Y\times^H\mathbb C^3,\qquad \det E\simeq\mathcal O_X,
 \qquad\pi^*E\simeq\mathcal O_Y^3.
$$

For a nonzero proper saturated subbundle $F\subset E$, the Plücker inclusion of $\det\pi^*F$ into a trivial exterior power gives $\deg F\le0$. If equality held, the map $Y\to\operatorname{Gr}(\operatorname{rk}F,3)$ would pull back its ample Plücker line to degree zero, so it would be constant. Then $\pi^*F=\mathcal O_Y\otimes W$, and descent would make $W$ a nonzero proper $H$-invariant subspace. Thus $E$ is stable. Its determinant-preserving automorphism group is exactly $\mu_3$.

Let

$$
 i:B\mu_3\hookrightarrow Y_G^{\mathrm{st}},\qquad
 j:Y_G^{\mathrm{st}}\hookrightarrow Y_G
$$

be its residual-gerbe inclusion and the stable-open inclusion. The first is the closed fiber over its stable coarse-moduli point. On this gerbe the adjoint determinant has trivial $\mu_3$-character, since the center acts trivially on $\mathfrak{sl}_3$. Choosing a basis of its one-dimensional fiber trivializes the restricted twisting line. Hence $D(L_G^s)|_{B\mu_3}\simeq D(B\mu_3)$ contains the one-dimensional representation $k_\eta$. Define

$$
 \mathcal F=j_*i_*k_\eta\in A_\eta.
$$

Kashiwara full faithfulness and open restriction give

$$
 i^!j^!\mathcal F\simeq k_\eta\ne0.
$$

The pushforwards retain central inertia, so $\mathcal F\ne0$ has precisely character $\eta$. Its stable degree-zero point also lies in the range retained by the irrational-twist cutoff. This verifies the nonvanishing claim in [the existing checker, §§2–3](checker_report.md), without inferring nonvanishing from an abstract character label.

The earlier localization theorem and its sector projection ([lines 8399–8447](../paper/paper.tex#L8399), [8670–8673](../paper/paper.tex#L8670)) provide a KL object $V$ of character $\eta$ with $L(V)\simeq\mathcal F$. The equivalence $\Phi$, constructed at [lines 8510–8549](../paper/paper.tex#L8510) before the changed definition, has $\Phi(\mathcal F)\ne0$ in component $-\eta$. Thus the same witness tests both (1) and (2).

## Five-item audit summary

Here a **downstream** violation means that a later inference lacks an input already invalidated at the planted construction; it is excluded from the final direct labels. The Notes distinguish that situation from a new theorem-hypothesis or variable-scope error.

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | downstream | [8777–8788](../paper/paper.tex#L8777), [8866–8871](../paper/paper.tex#L8866) | Localization descent has the correct implication, but its required natural comparison was not constructed. [Full MP Note](#mp-note). |
| G1 | violated | downstream | [8786–8788](../paper/paper.tex#L8786), [8919–8926](../paper/paper.tex#L8919) | The asserted family has a failed pre-generalization calculation at a fixed admissible automorphism; freshness and range conditions are sound. [Full G1 Note](#g1-note). |
| G2 | not_violated | none | [8751–8775](../paper/paper.tex#L8751), [8777–8784](../paper/paper.tex#L8777) | Local section witnesses are used within their scope and correctly construct $V[Q]$; the comparison fails its separate overlap calculation. [Full G2 Note](#g2-note). |
| DEF | violated | direct | [8777–8788](../paper/paper.tex#L8777), required structure at [8733–8743](../paper/paper.tex#L8733) | The proposed comparison does not descend to a torsor-groupoid-natural isomorphism. The inverted torsor action itself is well-defined. [Full DEF Note](#def-note). |
| CONV | violated | direct | [8694](../paper/paper.tex#L8694) used at [8779–8784](../paper/paper.tex#L8779), repeated at [8919–8926](../paper/paper.tex#L8919) | Expanding the contracted product gives $z^{-1}$, whereas the proof substitutes $z$. [Full CONV Note](#conv-note). |

<a id="mp-note"></a>

## MP — Note

**Status: violated. Role: downstream.** Start with the original rule

$$
 \frac{\Gamma\vdash A_{\mathrm{MP}}\qquad
       \Gamma\vdash A_{\mathrm{MP}}\Rightarrow B_{\mathrm{MP}}}
      {\Gamma\vdash B_{\mathrm{MP}}}.
$$

The concrete application is the [fully faithful localization descent at lines 8866–8871](../paper/paper.tex#L8866), together with the [preceding universal property at lines 8440–8447](../paper/paper.tex#L8440). The following is a symbolic reconstruction of that printed inference, preserving its assumptions.

To expose the domains, let $\mathcal K=\operatorname{KL}_G(a)_{\operatorname{Ran}}$, and let $\alpha:\mathcal K\simeq\mathcal C$ be the manuscript's identification with the dual-group Whittaker category. Put

$$
 \mathsf L=L\alpha:\mathcal K\longrightarrow A,
 \qquad P_B=e_B(S')^\vee:\mathcal C\longrightarrow B.
$$

Thus $\mathsf L$ denotes the same localization written as $L(V)$ for a KL input in §13.5. Let $\mathscr T_Z$ be the full groupoid of $Z_G$-torsors on $X$, including its family pullbacks. Write $T_Q(V)=V[Q]$. The two functors whose comparison is sought are

$$
 \mathscr F_Q=\Phi\tau_Q^!:A\to B,
 \qquad \mathscr H_Q=u_Q^{-1}\otimes\Phi:A\to B.
$$

The background $\Gamma_{\mathrm{MP}}$ consists of the following data and available statements, with no assumption of (1):

1. The field, curve, group, full root datum, pinnings, theta characteristic, level relations, and four twisted categories specified above.
2. The well-defined functors $\tau_Q^!$, $T_Q$, and tensor by $u_Q^{\pm1}$, with the exact defining conventions of §13.5; all functors under discussion are continuous and $\mathbb C$-linear.
3. The localization property of $\mathsf L$, and the universal property that precomposition with a localization is fully faithful on continuous functor categories. Pointwise application and the naturality diagrams give the same full faithfulness for $\mathscr T_Z$-indexed functors.
4. The preceding equivalence $\Phi$, the comparison $b:\Phi\mathsf L\simeq P_B\alpha$ from (13.5), and the already proved sector formula $(\eta,p)\mapsto(p,-\eta)$.
5. The independent Whittaker comparison $\gamma_Q:\alpha T_Q\simeq u_Q^{-1}\otimes\alpha$, equation (13.8), and the tensor comparison $P_B(u_Q^{-1}\otimes W)\simeq u_Q^{-1}\otimes P_B(W)$ at [lines 8857–8864](../paper/paper.tex#L8857). Their calculation uses the unchanged KL action and unchanged transgression, which agree with one another.

Instantiate the localization implication with domain $\mathcal K$, quotient $A$, target $B$, localization $\mathsf L$, and functors $\mathscr F,\mathscr H$. Its antecedent $A_{\mathrm{MP}}$ is the existence of a family of isomorphisms

$$
 \varepsilon_{Q,V}:\mathscr F_Q(\mathsf L V)
          \xrightarrow{\sim}\mathscr H_Q(\mathsf L V)
 \quad(Q\in\mathscr T_Z,\ V\in\mathcal K)
$$

that is a **natural transformation**, not just a list of maps. Explicitly, for every $f:V\to W$ and every torsor isomorphism $a:Q\to R$, it must satisfy

$$
 \begin{aligned}
 \mathscr H_Q(\mathsf L f)\varepsilon_{Q,V}
   &=\varepsilon_{Q,W}\mathscr F_Q(\mathsf L f),\\
 \mathscr H(a)_{\mathsf L V}\varepsilon_{Q,V}
   &=\varepsilon_{R,V}\mathscr F(a)_{\mathsf L V}.
 \end{aligned} \tag{3}
$$

The family must also respect the parameter pullbacks already used to define these functors: for every allowed base map $r:S_1\to S_2$, its pullback is $\varepsilon_{r^*Q,r^!V}$ under the specified pullback identifications. Thus, writing $\operatorname{Par}(\varepsilon)$ for this explicitly stated equality for every $r$, the instantiated antecedent is

$$
 A_{\mathrm{MP}}:=\exists\varepsilon\left[
 \begin{array}{l}
 \forall Q\in\mathscr T_Z\ \forall V\in\mathcal K,
     \ \varepsilon_{Q,V}:\mathscr F_Q\mathsf L(V)
       \xrightarrow{\sim}\mathscr H_Q\mathsf L(V),\\
 \forall Q\in\mathscr T_Z\ \forall V,W\in\mathcal K\quad
     \forall f\in\operatorname{Hom}_{\mathcal K}(V,W),
     \ \mathscr H_Q(\mathsf Lf)\varepsilon_{Q,V}
       =\varepsilon_{Q,W}\mathscr F_Q(\mathsf Lf),\\
 \forall Q,R\in\mathscr T_Z\ \forall a\in\operatorname{Iso}(Q,R)\quad
     \forall V\in\mathcal K,
     \ \mathscr H(a)_{\mathsf LV}\varepsilon_{Q,V}
       =\varepsilon_{R,V}\mathscr F(a)_{\mathsf LV},\\
 \operatorname{Par}(\varepsilon)
 \end{array}\right].
$$

All four lines inside the brackets are conjoined. The quantifier over $\varepsilon$ is over homotopy-coherent transformations of the indicated DG functors; the displayed equations explicitly record their constraints on ordinary arrows. The consequent $B_{\mathrm{MP}}$ is the existence of an invertible natural transformation

$$
 \theta_Q:\mathscr F_Q\xrightarrow{\sim}\mathscr H_Q
$$

with the same two naturality conditions for all objects and morphisms of $A$, and the same parameter compatibilities. Explicitly,

$$
 B_{\mathrm{MP}}:=\exists\theta\left[
 \begin{array}{l}
 \forall Q\in\mathscr T_Z\ \forall F\in A,
     \ \theta_{Q,F}:\mathscr F_Q(F)\xrightarrow{\sim}\mathscr H_Q(F),\\
 \forall Q\in\mathscr T_Z\ \forall F,F'\in A\quad
     \forall h\in\operatorname{Hom}_A(F,F'),
     \ \mathscr H_Q(h)\theta_{Q,F}
       =\theta_{Q,F'}\mathscr F_Q(h),\\
 \forall Q,R\in\mathscr T_Z\ \forall a\in\operatorname{Iso}(Q,R)\quad
     \forall F\in A,
     \ \mathscr H(a)_F\theta_{Q,F}
       =\theta_{R,F}\mathscr F(a)_F,\\
 \operatorname{Par}(\theta)
 \end{array}\right].
$$

The quantifier over $\theta$ has the same coherent-transformation meaning, and $\operatorname{Par}(\theta)$ is the identical pullback condition with $F\in A$ in place of $V\in\mathcal K$. There is no free $\varepsilon$ in this exported consequent. Inside the scope of any witness $\varepsilon$ for the antecedent, full faithfulness supplies the lift satisfying $\theta_Q\mathsf L=\varepsilon_Q$, uniquely with its specified comparison up to coherent identification; forgetting that specification gives $B_{\mathrm{MP}}$. Inverses descend as well: their two composite identities are detected after precomposition. The conclusion $C$ actually claimed at line 8871 is this first isomorphism of (13.7); the full-groupoid assertion is made explicit at lines 8914–8918. Thus the implication has the right consequent. The subsequent unit and tensor coherence diagrams would likewise be detected by full faithfulness once their comparison existed.

The manuscript attempts to establish the antecedent by composing

$$
 \begin{aligned}
 \Phi\tau_Q^!\mathsf L(V)
 &\xrightarrow{\Phi(\ell_{Q,V})}\Phi\mathsf L(T_QV)
 \xrightarrow{b_{T_QV}}P_B\alpha(T_QV)\\
 &\xrightarrow{P_B(\gamma_{Q,V})}P_B(u_Q^{-1}\otimes\alpha V)
 \xrightarrow{\sim}u_Q^{-1}\otimes P_B\alpha V
 \xrightarrow{1\otimes b_V^{-1}}u_Q^{-1}\otimes\Phi\mathsf L(V),
 \end{aligned} \tag{4}
$$

where $\ell$ is precisely the proposed comparison (1). All arrows after the first are provided by the listed background. The first arrow has no torsor-natural construction: on the verified $\eta$-sector and $a_\zeta:Q_0\to Q_0$, its two sides carry $\zeta^2$ and $\zeta$. Consequently the second equality of (3) would require

$$
 \zeta\,\varepsilon_{Q_0,V}
   =\varepsilon_{Q_0,V}\,\zeta^2.
$$

Since $\Phi\mathsf L(V)\simeq\Phi(\mathcal F)\ne0$, no isomorphism satisfies this equation. The first failed MP obligation is therefore the **unestablished antecedent**, specifically the existence and torsor naturality of $\varepsilon$; the localization implication is available and correctly instantiated. Its provenance is the false frame conversion at line 8780 and failed comparison descent at line 8784. This is downstream propagation, not an additional direct MP label.

<a id="g1-note"></a>

## G1 — Note

**Status: violated. Role: downstream.** The relevant rule is

$$
 \frac{\Gamma\vdash A_{\mathrm{G1}}\Rightarrow B_{\mathrm{G1}}(x)}
      {\Gamma\vdash A_{\mathrm{G1}}\Rightarrow\forall x\,B_{\mathrm{G1}}(x)},
 \qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(A_{\mathrm{G1}}).
$$

There is an actual family assertion to check: [lines 8777–8788](../paper/paper.tex#L8777) construct a comparison at chosen lifts, assert it on bounded formulas and their morphisms, and extend it continuously; [lines 8919–8926](../paper/paper.tex#L8919) purport to verify its signs on arbitrary torsor automorphisms. The latter supplies a particularly concrete specialization of the pre-generalization obligation. It already fails before any passage from bounded inputs to all inputs.

Fix the curve, group, level, and the trivial torsor $Q_0$ as above. Let $\mathcal F\in A$, $\eta\in X^*(Z_G)$, and the unit section $q_0$ be fixed parameters. The background $\Gamma_{\mathrm{G1}}$ consists of those data, the quotient relation, the stated sheaf convention, and the central-inertia action on objects of $A$; it contains no chosen element of $Z_G$. Let

$$
 A_{\mathrm{G1}}:
 \quad\forall g\in Z_G(\mathbb C),\,
       \rho_{\mathcal F}(g)=\eta(g)\operatorname{id}_{\mathcal F}.
$$

This is exactly the condition that $\mathcal F$ has character $\eta$. The generalized variable is $x=z$, ranging over complex elements, with range predicate $D(z):z\in Z_G(\mathbb C)$. Because $X$ is connected and $Z_G$ is finite, these are the global central automorphisms of $Q_0$. Write $a_z(q)=qz$ and let $K_{\mathcal F}(z)$ denote the endomorphism induced by $a_z$ on $\tau_{Q_0}^!\mathcal F$, identified with $\mathcal F$ using $q_0$. The printed scalar assertion is

$$
 B_{\mathrm{G1}}(z):
 D(z)\Rightarrow
 K_{\mathcal F}(z)=\eta(z)\operatorname{id}_{\mathcal F}. \tag{5}
$$

In a fresh-parameter presentation, the actual local obligations are

$$
 \begin{array}{ll}
 1.&[A_{\mathrm{G1}}]\quad\text{and a fresh }z\text{ with }[D(z)];\\
 2.&t_{q_0z}=t_{q_0}\circ m_{z^{-1}}
       \quad\text{by the changed contracted product};\\
 3.&K_{\mathcal F}(z)=\rho_{\mathcal F}(z^{-1})
       =\eta(z^{-1})\operatorname{id}_{\mathcal F};\\
 4.&K_{\mathcal F}(z)\mathrel{\stackrel{\mathrm{printed}}{=}}
       \eta(z)\operatorname{id}_{\mathcal F}.
 \end{array} \tag{6}
$$

Here $m_g$ is the central automorphism $x\mapsto gx$ of a principal bundle. Line 4 is the failed pre-generalization calculation. If it were established, discharging $D(z)$ and $A_{\mathrm{G1}}$ would give the rule's premise, and G1 would give

$$
 A_{\mathrm{G1}}\Rightarrow
 \forall z\bigl(z\in Z_G(\mathbb C)\Rightarrow
 K_{\mathcal F}(z)=\eta(z)\operatorname{id}_{\mathcal F}\bigr). \tag{7}
$$

This is the automorphism part of the claimed groupoid comparison at the trivial torsor. The section $q_0$ is specially chosen to be a section of $Q_0$; it remains fixed throughout this specialization, and no conclusion about all torsors is inferred from its global existence. The free parameters of $\Gamma_{\mathrm{G1}}$ are $G,X,c,a,d,s,s',Q_0,q_0,\mathcal F,\eta$ and the fixed categorical data. The free parameters of $A_{\mathrm{G1}}$ are among $G,\mathcal F,\eta$; its variable $g$ is bound. The parameter $z$ is absent from both. The assumptions $D(z)$ and $A_{\mathrm{G1}}$ are discharged as displayed. Thus the variable condition is satisfied.

For the admissible nonzero $\mathcal F$ above, substituting $z=\zeta$ in line 3 gives $\zeta^2\operatorname{id}$; line 4 demands $\zeta\operatorname{id}$. The failed derivation is therefore explicit at one fixed input, not inferred merely from the falsity of a universal statement. The proof never first restricts $z$ to an involution or $\eta$ to a two-torsion character and then drops that restriction. Likewise, its lift-cover construction works for arbitrary torsors and includes collisions. The universal family is unjustified because its local input calculation already fails. This is the downstream G1 check-1 failure; it supplies no separate direct G label.

<a id="g2-note"></a>

## G2 — Note

**Status: not_violated. Role: none.** The rule is

$$
 \frac{\Gamma\vdash A_{\mathrm{G2}}(x)\Rightarrow B_{\mathrm{G2}}}
      {\Gamma\vdash(\exists x\,A_{\mathrm{G2}}(x))\Rightarrow B_{\mathrm{G2}}},
 \qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(B_{\mathrm{G2}}).
$$

The nearby existential choices are the lifts used to define $V[Q]$, at [lines 8751–8775](../paper/paper.tex#L8751). Their actual structure can be formalized completely. Fix a tuple base $S$, its marked graphs $\Gamma_i$,

$$
 D=\sum_i\Gamma_i\subset X\times S,
$$

a $Z_G$-torsor $Q$, and a KL input $V\in\mathcal K_S$. The background $\Gamma_{\mathrm{G2}}$ consists of the curve and group hypotheses, these fixed data, the strong central-arc action $\rho$, and descent for the KL crystal category. In particular

$$
 \rho(z_1z_2)=\rho(z_1)\rho(z_2),\qquad\rho(1)=1,
$$

as natural transformations, also on morphisms of inputs. No local section is part of this background.

The witness $x$ is a pair $(r:U\to S,q)$. Its domain consists of schemes over $S$ and sections of the pulled-back torsor on the completed divisor. The supplied predicate is exactly

$$
 \begin{aligned}
 A_{\mathrm{G2}}(x):\quad &r\text{ is étale and surjective},\\
 &q\in\Gamma(\widehat D_U,Q|_{\widehat D_U})
   \text{ is a torsor section},\\
 &q|_D\text{ extends compatibly to every }nD_U.
 \end{aligned} \tag{8}
$$

Such witnesses exist by the manuscript's actual section scheme

$$
 U=\operatorname{Res}_{D/S}(Q|_D).
$$

The divisor is finite locally free even at a collision. Over a geometric point, each Artinian cluster admits a section of a finite étale torsor; formal étaleness extends that section uniquely through nilpotent thickenings. Restriction of scalars gives the stated étale surjective section cover and its universal section. Finiteness of $U\to S$ is neither required nor asserted.

Let $B_{\mathrm{G2}}$ be the existence of the descended KL object $V[Q]$, with its central-arc transition data and its canonical independence from the section cover; on morphisms this gives the operation $T_Q:\mathcal K_S\to\mathcal K_S$. Its definition mentions only $S,D,Q,V,\rho$, not the local witness $x$. The existential-elimination subderivation is:

$$
 \begin{array}{ll}
 1.&[\exists x\,A_{\mathrm{G2}}(x)];\\
 2.&\quad[x_*=(r_*:U_*\to S,q_*)\text{ fresh},\ A_{\mathrm{G2}}(x_*)];\\
 3.&\quad V_i=V|_{U_*},\quad
       q_j=q_i z_{ij}\text{ on }U_*\times_S U_*;\\
 4.&\quad z_{ik}=z_{ij}z_{jk},\quad
       \varphi_{ij}=\rho(z_{ij}):V_j\to V_i;\\
 5.&\quad\varphi_{ij}\varphi_{jk}=\varphi_{ik},
       \quad\varphi_{ii}=1;\\
 6.&\quad\text{descent produces }V[Q]\text{ and descends every input morphism};\\
 7.&\quad B_{\mathrm{G2}};\\
 8.&B_{\mathrm{G2}}\quad(\exists\text{-elimination, discharging line 2}).
 \end{array} \tag{9}
$$

All dependent constructions in the witness scope are explicit: $U_*$, the section $q_*$, its two pullbacks $q_i,q_j$, their differences $z_{ij}$, the pulled objects $V_i$, and the descent morphisms $\varphi_{ij}$. To check the claimed independence, pass to a common refinement for another cover and write $q'_i=q_i h_i$. Then

$$
 z'_{ij}=h_i^{-1}z_{ij}h_j,
 \qquad
 \rho(z_{ij})\rho(h_j)=\rho(h_i)\rho(z'_{ij}). \tag{10}
$$

Thus $\rho(h_i)$ identifies the two descent data and composes correctly under a third choice. Unique formal extension gives the corresponding compatibility under further thickenings, tuple refinements, and collisions. The exported object is unique with its descent data up to the specified isomorphism; a section itself is not exported.

The free variables of $\Gamma_{\mathrm{G2}}$ and $B_{\mathrm{G2}}$ are the fixed curve/group/level data, $S,D,Q,V,\rho$, not $U_*$ or $q_*$. Discharging line 1 gives the required implication $(\exists x A_{\mathrm{G2}}(x))\Rightarrow B_{\mathrm{G2}}$. The quantifier order is

$$
 \forall(S,D,Q)\ \exists(U,q)\ A_{\mathrm{G2}}(U,q;S,D,Q),
$$

with the choice allowed to depend on the displayed data. The proof does not replace this with one common $(U,q)$ for all torsors or with a global section of every $Q$.

For comparison (1), a local lift additionally supplies a local identification $\ell_{q,V}$. Its descent requires the separate overlap equation

$$
 \rho(z)\ell_{q,V}=\ell_{qz,V}\rho(z^{-1}). \tag{11}
$$

The proof explicitly attempts to verify that equation by the frame calculation at line 8780. It fails there. Mere existence of a lift is not presented as a substitute for the overlap check, and no local witness name escapes its scope. On the order-three witness the overlap check fails for every choice of lift. The actual existential construction (9) is valid; the additional comparison has the concrete DEF/CONV failure in (11), rather than a new eigenvariable or quantifier-order error.

<a id="def-note"></a>

## DEF — Note

**Status: violated. Role: direct.** The definition/construction failure is the proposed natural comparison, not the definition of central translation.

The introduced objects and their obligations at the target are as follows.

1. **Central translation.** For a $Z$-torsor $Q$ and a principal $G$-bundle $E$, the definition is

   $$
   \tau_Q(E)=(Q\times_XE)/\sim,
   \qquad(qz,x)\sim(q,z^{-1}x).
   $$

   Equivalently take the quotient by $(q,x)\cdot z=(qz,zx)$. This is a genuine group action because $Z$ is central and abelian; its action is free on the torsor factor. Étale locally a section $q$ gives the $G$-equivariant isomorphism $t_q:E\to\tau_Q(E)$, $x\mapsto[q,x]$. These local models and their transition maps define a principal $G$-bundle, and a torsor isomorphism $a:Q\to R$ induces $[q,x]\mapsto[a(q),x]$, independently of representatives. Thus $\tau:\mathscr T_Z\times Y_G\to Y_G$ exists as a groupoid action. In the original convention it is translation by $Q^{-1}$. Adjoint bundles and the line $L_G$ are canonically preserved since $\operatorname{Ad}(z)=1$. This also defines $\tau_Q^!:A\to A$. No representative, existence, or recursion defect occurs here.

2. **The lift scheme and KL twist.** The domain of $\operatorname{Res}_{D/S}(Q|_D)$ is $S$-schemes, and its points over $T\to S$ are sections of $Q|_{D_T}$. It exists for the finite locally free divisor, is étale surjective, and supplies unique extensions of its universal section to every thickening. The operation $T_Q:V\mapsto V[Q]$ has domain and codomain the KL category over the tuple base and is defined by the cocycle $\rho(z_{ij})$. Equations (9)–(10) verify its descent and independence of local sections, also on morphisms. These requirements hold.

3. **Transgression.** The obstruction is the lift gerbe for the universal $G^\vee$-bundle, valued in $A_{G^\vee}=\ker(G^\vee_{\mathrm{sc}}\to G^\vee)$. Pairing its degree-two class with the degree-one torsor $Q$, in the prescribed order, and integrating over the oriented curve gives

   $$
   u:\mathscr T_Z\longrightarrow
       \operatorname{LocSys}^{\mathrm{fin}}_1(Y_{G^\vee}),
   \qquad [u_Q]=\int_X\langle[Q]\cup\operatorname{obs}\rangle.
   $$

   Its codomain is rank-one finite-monodromy local systems with their isomorphisms. The paper performs the construction on torsors and gerbes, so automorphisms and tensor maps are retained; on charts finite-coefficient comparison gives the algebraic system and smooth descent gives it on the stack. Its inverse $u_Q^{-1}$ is the dual line local system. This construction is unchanged by the modified quotient and is well-defined. The calculation of its automorphisms below confirms its stated convention.

4. **The comparison being constructed.** At [lines 8777–8788](../paper/paper.tex#L8777), chosen lifts identify the adjoint bundles, outside Lie algebras, differential operators, and determinant factors. Reconstructing the printed chart-coinvariant procedure, the map $\ell_{q,V}$ identifies the same module generators in those two local coinvariant formulas. It has local source $\tau_Q^!\mathsf L(V)$ and local target $\mathsf L(T_QV)$. The required output is an isomorphism

   $$
   \ell\in\operatorname{Iso}\!\left(
       [Q\mapsto\tau_Q^!\mathsf L],
       [Q\mapsto\mathsf L T_Q]\right)
   $$

   in the category of $\mathscr T_Z$-indexed continuous functors $\mathcal K\to A$, with the indicated parameter compatibilities. Descent therefore requires equality (11) on every change of lift, as well as the composition laws. This naturality is part of the construction contract, already required to use the comparison in Theorem 13.5.

The last requirement fails concretely. At $Q_0$, choose the nonzero $\eta$-sector preimage $V$. The local trivializations identify both objects with $\mathcal F$. The torsor automorphism $a_\zeta$ acts on the source by $\zeta^2$ and the target by $\zeta$. Every descended isomorphism would have to satisfy

$$
 \zeta\ell_{Q_0,V}=\ell_{Q_0,V}\zeta^2,
 \qquad(\zeta^2-\zeta)\ell_{Q_0,V}=0. \tag{12}
$$

The coefficient is invertible, so (12) forces the map to be zero. That is incompatible with an isomorphism of the nonzero object $\mathcal F$. The failure persists for any altered local map or scalar normalization, because distinct scalar characters have no invertible intertwiner.

The final construction $\theta:\Phi\tau_Q^!\simeq u_Q^{-1}\otimes\Phi$ similarly has codomain the space of invertible natural transformations $A\to B$ indexed by the torsor groupoid. On $\Phi(\mathcal F)\ne0$, it has the same obstruction (12). Thus the failure concerns **existence of the comparison with its defining descent/naturality structure**, not a later optional property of an already constructed groupoid-natural map. Objectwise maps after choosing a lift exist; they do not constitute that specified object. Uniqueness and higher coherence cannot be reached once this overlap condition fails. This supplies the direct DEF label independently of whether one also records the erroneous computation that led to it.

<a id="conv-note"></a>

## CONV — Note

**Status: violated. Role: direct.** The manuscript's starting operation is the lift change $q\mapsto qz$; [line 8780](../paper/paper.tex#L8780) claims the resulting translated-frame change is multiplication by $z$. The complete definitional computation is

$$
 \begin{aligned}
 t_{qz}(x)
   &=[qz,x] &&\text{definition of the frame determined by }qz\\
   &=[q,z^{-1}x] &&\text{modified contracted-product relation}\\
   &=t_q(z^{-1}x) &&\text{definition of }t_q\\
   &=(t_q\circ m_{z^{-1}})(x).
 \end{aligned} \tag{13}
$$

The claimed endpoint would be $(t_q\circ m_z)(x)=[q,zx]$. The first wrong transformation is replacing the actual $z^{-1}x$ by $zx$ in this use of the quotient relation. For a principal bundle the central action is free on each geometric fiber, so at $z=\zeta$ these frames differ.

For the trivial torsor, its automorphism also computes without any choice of a theorem:

$$
 \begin{aligned}
 \tau_{a_z}(E)([q_0,x])
   &=[q_0z,x]=[q_0,z^{-1}x],\\
 t_{q_0}^{-1}\tau_{a_z}(E)t_{q_0}
   &=m_{z^{-1}}.
 \end{aligned} \tag{14}
$$

On a central-character object, the fixed inertia representation therefore gives

$$
 \operatorname{act}_{\tau_{Q_0}^!\mathcal F}(a_z)
   =\rho_{\mathcal F}(z^{-1})
   =\eta(z^{-1})\operatorname{id}
   =\eta(z)^{-1}\operatorname{id}. \tag{15}
$$

This can be read on $B\mu_3$, where the chosen object is the representation $k_\eta$: evaluate that representation on the actual automorphism $z^{-1}$ from (14). The determinant twist is trivial on this inertia. Thus the printed $!$-pullback and adjoint normalization supply no additional character factor. In contrast, the retained KL operation descends using $\rho(z)$, and localization retains that action without inversion. Hence

$$
 \operatorname{act}_{\mathsf L(V[Q_0])}(a_z)
       =\eta(z)\operatorname{id}. \tag{16}
$$

Equations (15) and (16) already contradict the claimed chart descent (1).

The transgression side can also be calculated completely. An automorphism $a_z$ of $Q_0$ is a degree-zero variation $z$ of the torsor class. The induced automorphism of the transgression line on the dual-group component $p'\in\pi_1(G^\vee)=X^*(Z)$ is

$$
 \begin{aligned}
 \operatorname{act}_{u_{Q_0}|_{p'}}(a_z)
   &=\int_X\langle z\cup\operatorname{obs}\rangle\\
   &=\left\langle z,\int_X\operatorname{obs}\right\rangle\\
   &=\langle z,p'\rangle=p'(z).
 \end{aligned} \tag{17}
$$

The middle expressions in (17) denote the multiplicative scalar obtained by the finite pairing. The first factor remains first in the cup product, and the specified orientation and obstruction normalization make the integral equal to $p'$. No permutation of factors or sign change occurs. Proposition 13.4 supplies $p'=-\eta$, so

$$
 \operatorname{act}_{u_{Q_0}}(a_z)=(-\eta)(z)=\eta(z)^{-1},
 \qquad
 \operatorname{act}_{u_{Q_0}^{-1}}(a_z)=\eta(z). \tag{18}
$$

Since $\Phi$ is $\mathbb C$-linear, it retains the scalar in (15). At $z=\zeta$, the two sides of the first identity in (2) therefore have scalars

$$
 \underbrace{\eta(\zeta^{-1})}_{\Phi\tau_{Q_0}^!\mathcal F}
    =\zeta^2,
 \qquad
 \underbrace{(( -\eta)(\zeta))^{-1}}_{u_{Q_0}^{-1}\otimes\Phi\mathcal F}
    =\zeta.
$$

The exact discrepancy and its square are

$$
 \begin{aligned}
 \delta&=\zeta^2-\zeta=(-1-\zeta)-\zeta=-1-2\zeta,\\
 \delta^2&=1+4\zeta+4\zeta^2
       =1+4\zeta+4(-1-\zeta)=-3,
 \qquad\delta^{-1}=-\delta/3.
 \end{aligned} \tag{19}
$$

Naturality requires $\theta\zeta^2=\zeta\theta$, which forces $\theta=0$ by (19), while $\Phi(\mathcal F)\ne0$. The necessary character condition in general would be $\eta(z^{-1})=\eta(z)$ for every $z$, equivalently $2\eta=0$; that condition is not among the hypotheses.

For the second identity, the same expansion with $Z_{G^\vee}$ gives $p((z')^{-1})$ on $\tau_{Q'}^!\Phi(\mathcal F)$, whereas the retained transgression $u'_{Q'}$ on component $p$ gives $p(z')$. This explains the second repeated sign in the final check. The certified $\mathrm{SL}_3$ witness already disproves the first identity, so no additional nonzero sector is required for the classification.

The matrices, the 27-element group, its determinant-one property, both commutators, the genus-two relation, the eigenline test, and (19) were checked with exact arithmetic. For characters $\eta^m$, $m=0,1,2$, the two exponents are respectively $(-m)\bmod3$ and $m\bmod3$; they disagree for $m=1,2$. These computations verify the existing witness. The **direct** CONV violation is specifically (13), also repeated through (15) at line 8920; the finite-group and nonvanishing calculations are diagnostic certificates, not additional planted computational errors.

## Final direct classification

**Final direct labels: DEF, CONV.** This agrees with the existing labels in the [case README](../README.md). The precise DEF target is the chart comparison and its required groupoid descent at lines 8777–8788, not the inverted contracted product, which defines a valid action. CONV targets the wrong expansion of that action on changes of lift and torsor automorphisms.

The later localization application and universal family assertion inherit the failed comparison/calculation, as recorded under MP and G1. The actual local existential construction for $V[Q]$ is valid. They add no direct label. The order-three witness supplies a nonzero object under the manuscript's actual irrational-level hypotheses and an invertible scalar obstruction to the claimed natural isomorphism. No mathematical issue needed for these direct labels remains unresolved.
