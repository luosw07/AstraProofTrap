# 009: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow. It is informed by the complete modified manuscript, its original and exact patch, and the existing construction and checker materials; it is not an original workflow report or a blind reviewer run. The classification follows the [classification standard](../../../protocol/classification.md).

**Final direct label: CONV.** The modified proof incorrectly expands the exterior derivative of a contracted tensor. Differentiating $\Theta_t(e_{tu})$ also differentiates the prescribed vector field $e_{tu}^{\sharp}$. The surviving contribution is $\tfrac12\Theta_t(\widehat c_t(e_{tu})^{\sharp},e_{tl}^{\sharp})$. An admissible flow gives $-\tfrac12$ for the modified equation's left side and $0$ for its right side.

## Exact target and actual assumptions

The target is [TeX lines 3749–3752](../paper/paper.tex#L3749), the first display on manuscript page 46, within the proof of Theorem 4.30, `thm:compatibilityflows`. The [original passage](../original/paper.tex#L3749) contains the additional contraction. The [patch](../mutation.diff) deletes that term and changes the explanation to “Taking its … component and using the symmetry of $\Theta_t$.” The two manuscripts otherwise agree. The surrounding argument compares two mixed Ricci components at [lines 3729–3745](../paper/paper.tex#L3729), then uses the altered display at [line 3769](../paper/paper.tex#L3769) to obtain the transverse momentum/Maxwell identity.

The actual hypothesis of [Theorem 4.30](../paper/paper.tex#L3658) is a **supersymmetric Neveu–Schwarz flow**, explicitly a solution of `eq:susyevol`. Write its data as $\mathscr F=(\lambda_t,\mathfrak e_t,a_t,b_t,\phi_t)$ on an interval $\mathcal I$ containing $0$ and an oriented connected smooth three-manifold $\Sigma$. The gerbe reduction is on a surjective submersion $\pi:Y\to\Sigma$. Here:

- $\lambda_t\in C^\infty(\Sigma,\mathbb R)$ is nowhere zero, with its sign fixed by the normal orientation; $\mathfrak e_t=(e_{tu},e_{tl},e_{tn})$ is a smooth positively oriented coframe.
- $h_t=\sum_{i=u,l,n}e_{ti}\otimes e_{ti}$, $g=-\lambda_t^2dt^2+h_t$, and $\Theta_t=-\tfrac1{2\lambda_t}\partial_t h_t$. The globally hyperbolic configuration has these reductions. The spatial connection is the torsion-free Levi-Civita connection $\nabla^{h_t}$, even though the four-dimensional supersymmetry system also uses a connection with skew torsion.
- $a_t\in\Omega^1(Y)$ and $b_t\in\Omega^2(Y)$ are the reduced curving data. The derived two-form is characterized by $\pi^*c_t=\partial_t b_t-d_Ya_t$; $\widehat c_t=\lambda_t^{-1}c_t$, $\theta_t=*_{h_t}\widehat c_t$, and $H_{b_t}=f_{b_t}\nu_{h_t}$.
- $\phi_t:\Sigma\to S^1$ is smooth; $\varphi_{\phi_t}=\phi_t^*\mu\in\Omega^1(\Sigma)$ and $p_t=\lambda_t^{-1}\mu_{\phi_t}(\partial_t\phi_t)\in C^\infty(\Sigma,\mathbb R)$. In particular $d_\Sigma\varphi_{\phi_t}=0$.
- $\mathfrak a_t\in C^\infty(\Sigma,\mathbb R)$ is the scale function supplied by the supersymmetry system. It is distinct from the one-form $a_t$ on $Y$.

These definitions are given in the [second fundamental form discussion](../paper/paper.tex#L1349), [gerbe reduction](../paper/paper.tex#L3011), and [supersymmetry flow](../paper/paper.tex#L3375). The manuscript [identifies covectors with metric-dual vectors](../paper/paper.tex#L812), explicitly including evaluations of $\Theta_t$ [at line 1368](../paper/paper.tex#L1368).

For completeness, the flow assumption used below, denoted $\operatorname{Sup}(\mathscr F)$, means that the above smooth, globally hyperbolic configuration and coframe admit a smooth family $\mathfrak a_t$ for which, for every $s\in\mathcal I$ and every $i\in\{u,l,n\}$, the following equations hold. Set $E_{si}=e_{si}^{\sharp_{h_s}}$, $D_s=\lambda_s^{-1}\partial_s$ and $\eta_s=\lambda_s^{-1}d_\Sigma\lambda_s$:

$$
\begin{aligned}
\partial_s\mathfrak a_s&=d_\Sigma\lambda_s(E_{su}),\\
D_se_{si}+\Theta_s(E_{si},-)+\tfrac12\iota_{E_{si}}\widehat c_s
&=\delta_{ui}\eta_s-\eta_s(E_{si})e_{su},\\
d_\Sigma e_{si}
&=\Theta_s(E_{si},-)\wedge e_{su}
 +\tfrac12 f_{b_s}*_{h_s}e_{si}-\tfrac12\delta_{ui}\widehat c_s,\\
d_\Sigma\mathfrak a_s&=-\Theta_s(E_{su},-)+\tfrac12\iota_{E_{su}}\widehat c_s,\\
\varphi_{\phi_s}&=p_s e_{su}+\iota_{E_{su}}\widehat c_s,\\
f_{b_s}&=*_{h_s}(\widehat c_s\wedge e_{su}).
\end{aligned}
$$

This is precisely [the system at lines 3383–3391](../paper/paper.tex#L3383), including both evolution and spatial equations. It does not impose the second-order equations of motion. The manuscript explicitly distinguishes the two systems [at line 3990](../paper/paper.tex#L3990). Compactness and completeness are also absent from the target theorem.

At the time fixed in the proof [at line 3677](../paper/paper.tex#L3677), suppress $t$ and set

$$
\begin{gathered}
U=e_{tu}^{\sharp},\qquad L=e_{tl}^{\sharp},\qquad N=e_{tn}^{\sharp},
\qquad h=h_t,\quad\Theta=\Theta_t,\quad\nabla=\nabla^{h_t},\\
q=\Theta(U,-)\in\Omega^1(\Sigma),\qquad
w=\iota_U\widehat c_t\in\Omega^1(\Sigma),\qquad
S(V)=\Theta(V,-)^{\sharp_h},\\
D=(\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U),\qquad
J=\Theta(w^{\sharp_h},L).
\end{gathered}
$$

$S:T\Sigma\to T\Sigma$ is self-adjoint; $D,J\in C^\infty(\Sigma,\mathbb R)$ are abbreviations used in this review. When the time is shown explicitly, write $D(t)$ for this scalar difference and $J_t$ for the contraction; $D(t)$ is distinct from the manuscript's time-derivative operator $D_t=\lambda_t^{-1}\partial_t$. The printed starting equation is $d_\Sigma q=\tfrac12d_\Sigma w$. The printed endpoint is

$$
D=\tfrac12d_\Sigma w(U,L).
$$

The constraints whose compatibility is being proved are the following already defined objects, rather than equations assumed to vanish:

$$
\begin{aligned}
\mathcal H_t={}&s^{h_t}+(\operatorname{Tr}_{h_t}\Theta_t+p_t)^2
-|\Theta_t|_{h_t}^2-|\varphi_{\phi_t}|_{h_t}^2
-\tfrac12(f_{b_t}^2+|\theta_t|_{h_t}^2)
-2\nabla^{h_t*}\varphi_{\phi_t},\\
\mathcal W_t={}&d_\Sigma(\operatorname{Tr}_{h_t}\Theta_t+p_t)
+\nabla^{h_t*}\Theta_t+\Theta_t(\varphi_{\phi_t}^{\sharp},-)
-\tfrac12 f_{b_t}\theta_t,\\
\mathcal M_t={}&d_\Sigma\theta_t-\varphi_{\phi_t}\wedge\theta_t.
\end{aligned}
$$

See [lines 3308–3313](../paper/paper.tex#L3308). The theorem's conclusion is the equality of one-forms $\mathcal H_t e_{tu}=2\mathcal W_t+*_{h_t}\mathcal M_t$ at every time. The sequents in the Notes below are symbolic reconstructions of the printed inferences, retaining their actual assumptions.

## Five-rule audit summary

“Downstream” below records an inherited proof dependency on the defective calculation, rather than an additional direct label.

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | downstream | [3749–3752](../paper/paper.tex#L3749); [3772](../paper/paper.tex#L3772); [4247–4258](../paper/paper.tex#L4247) | [MP — Note](#mp-note): the local differentiating, evaluation, and Ricci applications are valid; the later application fails antecedent establishment because the submitted proof has not established the compatibility identity. |
| G1 | not_violated | downstream | [3659](../paper/paper.tex#L3659), [3677](../paper/paper.tex#L3677), [3729](../paper/paper.tex#L3729), [3769](../paper/paper.tex#L3769) | [G1 — Note](#g1-note): time and the coframe have the correct scopes; the attempted fixed-time derivation fails before generalization. |
| G2 | not_violated | none | [3383–3387](../paper/paper.tex#L3383); [3749](../paper/paper.tex#L3749) | [G2 — Note](#g2-note): eliminating the supplied scale-function witness validly gives $dq=\tfrac12dw$; the component calculation introduces no existential inference. |
| DEF | not_violated | none | [1352–1368](../paper/paper.tex#L1352), [3034–3036](../paper/paper.tex#L3034), [3377–3387](../paper/paper.tex#L3377), [3749–3752](../paper/paper.tex#L3749) | [DEF — Note](#def-note): the coframe, metric, shape tensor, descended two-form, and contractions exist and are well-defined; the display asserts a false property of them. |
| CONV | violated | direct | [3749–3752](../paper/paper.tex#L3749); propagated at [3769](../paper/paper.tex#L3769) | [CONV — Note](#conv-note): the covariant product rule leaves $\tfrac12J$; explicit admissible data give $D=-\tfrac12$ and $\tfrac12dw(U,L)=0$. |

<a id="mp-note"></a>

## MP — Note

The rule being checked is

$$
\frac{\Gamma\vdash A\qquad\Gamma\vdash A\longrightarrow B}{\Gamma\vdash B}.
$$

**Context and valid starting application.** Fix a flow $\mathscr F$ and $t\in\mathcal I$. Let $\Gamma_{\mathrm{MP}}$ contain: the manifold, interval, gerbe, smoothness and nonvanishing conditions listed above; the displayed definitions of $h,\Theta,U,L,N,q,w,S$; $\operatorname{Sup}(\mathscr F)$ with every equation expanded above; $d_\Sigma^2=0$ and linearity of $d_\Sigma$; and the usual torsion-free, metric-compatible connection and tensor evaluation rules. There are no assumptions $J=0$, $\nabla U=0$, or $\mathcal H=\mathcal W=\mathcal M=0$ in this context.

The first clause of [line 3749](../paper/paper.tex#L3749) uses the universally quantified implication

$$
\forall r\in C^\infty(\Sigma,\mathbb R)\,
\forall\alpha,\beta\in\Omega^1(\Sigma),\qquad
\bigl(d_\Sigma r=-\alpha+\tfrac12\beta\bigr)
\ \Longrightarrow\ d_\Sigma\alpha=\tfrac12d_\Sigma\beta.
$$

The substitution is $(r,\alpha,\beta)=(\mathfrak a_t,q,w)$. Thus

$$
A_0:\ d_\Sigma\mathfrak a_t=-q+\tfrac12w,
\qquad
B_0:\ d_\Sigma q=\tfrac12d_\Sigma w.
$$

$A_0$ is an actual equation of `eq:susyevol`. The implication is available because

$$
0=d_\Sigma^2\mathfrak a_t=-d_\Sigma q+\tfrac12d_\Sigma w.
$$

The conclusion $C_0$ actually printed in that clause is exactly $B_0$. This MP application is sound.

**Component evaluation and the first failed obligation.** The evaluation implication is

$$
\forall\omega,\zeta\in\Omega^2(\Sigma)\,
\forall X,Y\in\mathfrak X(\Sigma),\qquad
\omega=\zeta\ \Longrightarrow\ \omega(X,Y)=\zeta(X,Y).
$$

Substituting $\omega=d_\Sigma q$, $\zeta=\tfrac12d_\Sigma w$, $X=U$, $Y=L$ gives

$$
A_1:\ d_\Sigma q=\tfrac12d_\Sigma w,
\qquad
B_1:\ d_\Sigma q(U,L)=\tfrac12d_\Sigma w(U,L).
$$

The types and the antecedent are established. The actual displayed conclusion after the advertised component calculation is

$$
C_1:\ (\nabla_U\Theta)(U,L)-(\nabla_L\Theta)(U,U)
=\tfrac12d_\Sigma w(U,L).
$$

The local proof fragment is therefore the valid inference $A_0\Rightarrow B_0=A_1\Rightarrow B_1$, followed by a claimed computational identification of the left sides of $B_1$ and $C_1$. Expanding that identification gives instead

$$
d_\Sigma q(U,L)=D+\Theta(\nabla_UU,L)-\Theta(\nabla_LU,U)
=D-\tfrac12J.
$$

The first failed obligation is this equality conversion, demonstrated in the CONV Note. $C_1$ is not the unexpanded consequent of component evaluation. Recasting the entire calculation as an implication $A_1\to C_1$ would give an unavailable implication, but that is a **symbolic reconstruction of the failed calculation**, not a separate theorem invoked by the manuscript. The manuscript invokes a valid antecedent and performs a false tensor expansion; it supplies no distinct conditional theorem with a missing hypothesis. That is the direct CONV failure, rather than a second direct MP violation.

**The nearby cited Ricci identity.** The actual theorem-like application in this part of the proof is [lines 3729–3745](../paper/paper.tex#L3729). For a smooth Riemannian three-manifold, its Levi-Civita connection, any orthonormal frame $(E_i)$, $\beta\in\Omega^1(\Sigma)$, and $Y\in\mathfrak X(\Sigma)$, its consequent is

$$
\sum_{i=u,l,n}(\nabla_{E_i}\nabla\beta)(Y,E_i)
-d_\Sigma\bigl(\operatorname{Tr}_h\nabla\beta\bigr)(Y)
=\operatorname{Ric}^h(Y,\beta^{\sharp_h}).
$$

For each application the antecedent consists of these smoothness, Riemannian, Levi-Civita, orthonormal-frame, one-form, and vector-field conditions. The substitutions are respectively

$$
(\beta,Y,E_u,E_l,E_n)=(e_{tu},L,U,L,N)
\quad\text{and}\quad
(e_{tl},U,U,L,N).
$$

All conditions hold. The resulting right sides are exactly $\operatorname{Ric}^h(L,U)$ and $\operatorname{Ric}^h(U,L)$ as printed. Symmetry of Ricci for this Levi-Civita connection permits their comparison. Neither application asserts that the contracted one-form $q$ can be differentiated while holding $U$ parallel.

**Downstream failure of antecedent establishment.** Let

$$
K_t:\ \mathcal H_t e_{tu}=2\mathcal W_t+*_{h_t}\mathcal M_t.
$$

The final assertion [at line 3772](../paper/paper.tex#L3772) has instantiated antecedent and consequent

$$
\begin{aligned}
A_{\mathrm d}&:=K_t\ \land\ \mathcal M_t=0\ \land\ \mathcal W_t(U)=0,\\
B_{\mathrm d}&:=\mathcal H_t=0\ \land\ \mathcal W_t=0\ \land\ \mathcal M_t=0.
\end{aligned}
$$

Let $\Gamma_{\mathrm d}$ consist of $\Gamma_{\mathrm{MP}}$, the displayed definitions of the scalar $\mathcal H_t$, one-forms $e_{tu},\mathcal W_t$, two-form $\mathcal M_t$, and Hodge operator, together with the temporary assumptions $\mathcal M_t=0$ and $\mathcal W_t(U)=0$ for this direction of the equivalence. The identity $e_{tu}(U)=1$ follows from the orthonormal coframe. $K_t$ is an earlier internal claim whose proof must be checked; it is not an assumption of $\Gamma_{\mathrm d}$.

From $A_{\mathrm d}$, evaluation on $U$ gives $\mathcal H_t=2\mathcal W_t(U)=0$; substitution into $K_t$ gives $2\mathcal W_t=0$. Consequently the implication premise

$$
\Gamma_{\mathrm d}\vdash A_{\mathrm d}\longrightarrow B_{\mathrm d}
$$

is valid, and the printed conclusion $C_{\mathrm d}$ equals $B_{\mathrm d}$. The reverse implication follows directly from vanishing of the three constraints. The forward MP application also requires

$$
\Gamma_{\mathrm d}\vdash K_t\land(\mathcal M_t=0)\land(\mathcal W_t(U)=0).
$$

The submitted argument has not established this antecedent: its derivation of the $K_t$ conjunct contains the demonstrated CONV error. This is a failed proof obligation in the submitted derivation, even though $K_t$ has a valid proof after restoring the omitted term. Thus MP is **violated, downstream** at this later application. The local MP applications checked above remain valid. The later use of the same transverse identity to rewrite the mixed Einstein defect [at lines 4247–4258](../paper/paper.tex#L4247) likewise relies on that unestablished internal claim and inherits the same failure of premise establishment. These downstream uses introduce no additional direct label.

<a id="g1-note"></a>

## G1 — Note

The rule is

$$
\frac{\Gamma\vdash A\to B(x)}{\Gamma\vdash A\to\forall x\,B(x)},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(A).
$$

Here the relevant quantified variable is **time**, $x=s\in\mathbb R$. Let $\Gamma_1$ contain the fixed manifold $\Sigma$, interval $\mathcal I$, gerbe, smooth field families $\mathscr F$, their types and the definitions in the first section, together with the differential and tensor identities used in the proof. Unlike $\Gamma_{\mathrm{MP}}$, it does not yet assume $\operatorname{Sup}(\mathscr F)$. Put

$$
A:=\operatorname{Sup}(\mathscr F),\qquad
B(s):=\bigl(s\in\mathcal I\ \Longrightarrow\ K_s\bigr),
$$

where $A$ is the complete displayed first-order system, with its time variable bound, and

$$
K_s:\ \mathcal H_s e_{su}=2\mathcal W_s+*_{h_s}\mathcal M_s
\quad\text{as sections of }T^*\Sigma.
$$

Equality of sections means equality at every point of $\Sigma$. Thus the asserted restricted quantified conclusion [at lines 3659–3662](../paper/paper.tex#L3659) is explicitly

$$
\Gamma_1\vdash
A\ \longrightarrow\ \forall s\bigl(s\in\mathcal I\longrightarrow
\forall\xi\in\Sigma\,
[\mathcal H_s(\xi)e_{su}|_\xi
=2\mathcal W_s|_\xi+(*_{h_s}\mathcal M_s)|_\xi]\bigr).
$$

**The actual pre-generalization derivation.** At [line 3677](../paper/paper.tex#L3677) the proof fixes an arbitrary $s\in\mathcal I$. Under the open assumptions $A$ and $s\in\mathcal I$ it derives the normal-component identity and attempts the following transverse chain:

$$
\begin{aligned}
d_\Sigma\mathfrak a_s=-q_s+\tfrac12w_s
&\ \Longrightarrow\ d_\Sigma q_s=\tfrac12d_\Sigma w_s\\
&\ \Longrightarrow\ d_\Sigma q_s(U_s,L_s)
=\tfrac12d_\Sigma w_s(U_s,L_s),\\
\text{claimed conversion:}\qquad
D(s)&=\tfrac12d_\Sigma w_s(U_s,L_s),\\
\text{claimed Ricci comparison:}\qquad
\mathcal W_s(L_s)&=-\tfrac12(*_{h_s}\mathcal M_s)(L_s).
\end{aligned}
$$

The first two implications are valid. The “claimed conversion” line is the false calculation: already for a single admissible $s=0$ and a single point it omits $\tfrac12J_s$. The proof then obtains the $N_s$ component by transverse rotation and combines it with the normal component to claim $K_s$. This exhibits the precise failure **before** the intended pre-generalization sequent

$$
\Gamma_1\vdash A\longrightarrow(s\in\mathcal I\longrightarrow K_s)
$$

has been established by the submitted argument. It does not assert that $K_s$ itself is false; the failure is in the displayed derivation leading to it.

**Free variables and discharged assumptions.** The free parameters of $\Gamma_1$ are the manifold, interval, gerbe and entire field families. In $A$, all time and coframe-index variables are bound by $\forall r\in\mathcal I$ and $\forall i\in\{u,l,n\}$, and the scale family is existentially bound. In particular $s\notin\operatorname{FV}(\Gamma_1)\cup\operatorname{FV}(A)$. The selected time has only the restriction $s\in\mathcal I$. At the pointwise level, an arbitrary point $\xi$ has only $\xi\in\Sigma$; there is no hypothesis selecting a special point. The restrictions are discharged into the range implications, and the assumption $A$ is discharged into the outer conditional. These are exactly the required scopes.

The coframe fields $U_s,L_s,N_s$ are determined by $\mathscr F$; they are not independent arbitrary vector fields. In particular the argument does not begin with a parallel extension of $U_s$ at a specially chosen point. Its derivative is prescribed by [line 3542](../paper/paper.tex#L3542), including the $w_s$ term. The erroneous omission is a failure to differentiate that prescribed field, not a later extension from a special parallel field to all fields.

**The transverse-component reduction is also legitimate in scope.** At [line 3729](../paper/paper.tex#L3729) the manuscript uses the constant rotation

$$
(e_{su},e_{sl},e_{sn})\longmapsto(e_{su},e_{sn},-e_{sl}),
\qquad (U_s,L_s,N_s)\longmapsto(U_s,N_s,-L_s).
$$

It preserves $h_s$, orientation, $\lambda_s$, $\Theta_s$, $\widehat c_s$, the gerbe and dilaton data, and every equation of $A$: the transverse equations transform linearly, their $\delta_{ui}$ terms remain zero, and the Hodge operator is unchanged. Thus an established formula for the $L_s$ component for arbitrary admissible coframes would give the $N_s$ component for this rotated admissible coframe. No extra condition on $L_s$ is exported or lost.

Consequently, the time and component generalizations have valid range and variable conditions. Their intended premises inherit the fixed-time CONV failure. There is no independently demonstrated direct G1 violation.

<a id="g2-note"></a>

## G2 — Note

The rule is

$$
\frac{\Gamma\vdash A(x)\to B}{\Gamma\vdash(\exists x\,A(x))\to B},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(B).
$$

There is no existential choice in the component computation [at lines 3749–3752](../paper/paper.tex#L3749): it operates on the already fixed $h_t,\Theta_t,U_t,L_t,\widehat c_t$. Nevertheless, the scale function used to obtain its starting equation is supplied existentially by [Proposition `prop:susyevol`](../paper/paper.tex#L3383), so that nearby elimination can be checked concretely.

Let $\Gamma_2$ consist of the fixed manifold, interval, gerbe configuration, coframe family and their types; the formulas for $h_s,\Theta_s,U_s,q_s,w_s$; the coframe evolution and spatial equations; the two algebraic dilatino equations; $d_\Sigma^2=0$ and linearity; and the chosen parameter $t\in\mathcal I$. The two equations involving a scale function are excluded from $\Gamma_2$ and placed in $A(x)$. In particular $\Gamma_2$ contains no selected scale-function name.

The witness variable $x$ ranges over $C^\infty(\mathcal I\times\Sigma,\mathbb R)$. Define its full supplied properties by

$$
A(x):=
\forall s\bigl(s\in\mathcal I\ \Longrightarrow\
[\partial_sx_s=d_\Sigma\lambda_s(U_s)
\ \land\ d_\Sigma x_s=-q_s+\tfrac12w_s]\bigr),
$$

and set

$$
B:=d_\Sigma q_t=\tfrac12d_\Sigma w_t.
$$

The relevant part of the supersymmetry assumption is $\exists x\in C^\infty(\mathcal I\times\Sigma,\mathbb R)\,A(x)$. With a fresh witness $\alpha$, the explicit elimination subderivation is

$$
\begin{array}{ll}
1.& [A(\alpha)]\quad\text{fresh local witness assumption},\\
2.& d_\Sigma\alpha_t=-q_t+\tfrac12w_t
      \quad(1,\ t\in\mathcal I),\\
3.& d_\Sigma^2\alpha_t=-d_\Sigma q_t+\tfrac12d_\Sigma w_t
      \quad\text{differentiate},\\
4.& 0=-d_\Sigma q_t+\tfrac12d_\Sigma w_t
      \quad(d_\Sigma^2=0),\\
5.& B\quad\text{rearrange}.
\end{array}
$$

Discharging line 1 proves $\Gamma_2\vdash A(\alpha)\to B$. Eliminating the existential witness gives

$$
\Gamma_2\vdash(\exists x\,A(x))\longrightarrow B.
$$

The fresh name $\alpha$ occurs only inside the subderivation. In particular,

$$
q_t=\left(-\frac1{2\lambda_t}\partial_t
\sum_i e_{ti}\otimes e_{ti}\right)(e_{tu}^{\sharp_{h_t}},-),
\qquad
w_t=\iota_{e_{tu}^{\sharp_{h_t}}}(\lambda_t^{-1}c_t)
$$

depend on the **fixed configuration and coframe**, not on the witness name. The same holds for $U_t,L_t,D(t)$ and $J_t$ in the local calculation. The scale-dependent quantity $e^{\alpha_t}(\lambda_tdt+e_{tu})$, which represents the spinor's current after choosing its scale, is not exported in $B$. Nor is a new lapse selected as a function of $\alpha$ at this step: $\lambda_t$ was fixed before the witness was selected. Thus $\alpha\notin\operatorname{FV}(\Gamma_2)\cup\operatorname{FV}(B)$, including hidden dependencies.

The witness properties also do not supply $J_t=0$: their spatial content gives precisely $dq_t=\tfrac12dw_t$, which holds in the counterexample below while $J_0=-1$ at the test point. The false display is reached after this sound elimination, through a nonexistential product-rule calculation. There is no witness escape, unsupported witness property used in an elimination subproof, or quantifier-order interchange at the target.

<a id="def-note"></a>

## DEF — Note

The changed passage introduces no new object by an existence claim, quotient, or recursive specification. It evaluates existing smooth tensors and asserts an identity between them. The following are the concrete construction obligations behind those expressions.

| Object and domain/codomain | Defining formula | Obligation and check |
|---|---|---|
| $h_t$, a section of $\operatorname{Sym}^2T^*\Sigma$ | $h_t=\sum_i e_{ti}\otimes e_{ti}$ | Since $(e_{ti})$ is a coframe, $h_t(V,V)=\sum_i e_{ti}(V)^2>0$ for $V\ne0$. It is a smooth positive definite metric. |
| $U_t,L_t,N_t\in\mathfrak X(\Sigma)$ and $\sharp_{h_t}:T^*\Sigma\to T\Sigma$ | $E_{ti}=e_{ti}^{\sharp_{h_t}}$ | Nondegeneracy gives a unique smooth inverse metric; $e_{ti}(E_{tj})=\delta_{ij}$. These are actual moving vector fields. |
| $\Theta_t\in\Gamma(\operatorname{Sym}^2T^*\Sigma)$ | $-\tfrac1{2\lambda_t}\partial_t h_t$ | Smoothness and $\lambda_t\ne0$ ensure existence; differentiation preserves symmetry. This fixes the sign and scale of the shape tensor [at lines 1352–1358](../paper/paper.tex#L1352). |
| $\nabla^{h_t}$ on $T\Sigma$ and its tensor bundles | The unique torsion-free $h_t$-compatible connection | The Riemannian metric supplies the usual Levi-Civita connection. No connection with torsion is substituted for it in this calculation. |
| $c_t,\widehat c_t\in\Omega^2(\Sigma)$ | $\pi^*c_t=\partial_tb_t-d_Ya_t$, $\widehat c_t=\lambda_t^{-1}c_t$ | Gerbe compatibility gives descent, and surjectivity of $\pi$ gives uniqueness. Division by the lapse is legitimate. |
| $\varphi_{\phi_t}\in\Omega^1(\Sigma)$ and $p_t\in C^\infty(\Sigma,\mathbb R)$ | $\phi_t^*\mu$ and $\lambda_t^{-1}\mu_{\phi_t}(\partial_t\phi_t)$ | Pullback and the Maurer–Cartan evaluation define global objects for an actual circle-valued map; no real lift is required. |
| $q_t,w_t\in\Omega^1(\Sigma)$, $w_t^{\sharp}\in\mathfrak X(\Sigma)$, $S_t\in\Gamma(\operatorname{End}T\Sigma)$ | $q_t(V)=\Theta_t(U_t,V)$, $w_t(V)=\widehat c_t(U_t,V)$, $S_t(V)=\Theta_t(V,-)^{\sharp}$ | Each is an ordinary smooth tensor contraction or musical isomorphism. Alternation gives $w_t(U_t)=0$; symmetry makes $S_t$ self-adjoint. Neither condition forces $\Theta_t(w_t^{\sharp},L_t)$ to vanish. |
| $\theta_t\in\Omega^1(\Sigma)$, $f_{b_t},\mathcal H_t\in C^\infty(\Sigma,\mathbb R)$, $\mathcal W_t\in\Omega^1(\Sigma)$, $\mathcal M_t\in\Omega^2(\Sigma)$ | $\theta_t=*_{h_t}\widehat c_t$, $H_{b_t}=f_{b_t}\nu_{h_t}$, and the three constraint formulas above | Orientation and the nonvanishing metric volume define the Hodge operator and scalar coefficient uniquely. Exterior derivatives, covariant derivatives and contractions in the constraint formulas have the displayed tensor types. |

In particular the descent requirement for $c_t$ is not merely presumed. The unchanged construction [at lines 3020–3036](../paper/paper.tex#L3020) uses the curving and connective-structure equations

$$
\delta b_t=F_{\mathcal A_t},\qquad
\delta a_t=\partial_t\mathcal A_t-d_{Y^{[2]}}\Psi_t
$$

to compute

$$
\begin{aligned}
\delta(\partial_tb_t-d_Ya_t)
&=\partial_tF_{\mathcal A_t}
-d_{Y^{[2]}}(\partial_t\mathcal A_t-d_{Y^{[2]}}\Psi_t)\\
&=0.
\end{aligned}
$$

Descent along the surjective submersion therefore yields $c_t$, and injectivity of $\pi^*$ makes it unique. The displayed covariant contractions are coordinate independent tensor operations. They use a fixed coframe in the given flow; the target is not defining a value on a quotient by coframe representatives. The adapted-coframe discussion in [Lemma `lemma:ghcoframe`](../paper/paper.tex#L1398) also fixes the representative relative to the hypersurface. No recursive or inductive definition occurs here.

The admissible flows in the CONV Note exhibit these objects simultaneously, including a genuine gerbe curving and a genuine circle-valued dilaton. In them $q=\tfrac12F'(x)dx$, $w=F'(x)dx$, and $\Theta(w^{\sharp},L)$ is a smooth, generally nonzero scalar. Thus the failure is a later asserted equality of well-defined objects. It is not a failure to construct the coframe, shape tensor, derived form, or their contractions.

<a id="conv-note"></a>

## CONV — Note

### The exact conversion and its missing term

The valid starting expression at [line 3749](../paper/paper.tex#L3749) is

$$
d_\Sigma\bigl(\Theta_t(e_{tu})\bigr)
=\tfrac12d_\Sigma\bigl(\widehat c_t(e_{tu})\bigr).
$$

With the explicitly defined fixed-time notation, this is $dq=\tfrac12dw$. The endpoint [at line 3751](../paper/paper.tex#L3751) claims $D=\tfrac12dw(U,L)$. The material intermediate steps are as follows. Torsion-freeness and the definition of exterior derivative give

$$
\begin{aligned}
dq(U,L)
&=U(q(L))-L(q(U))-q([U,L])\\
&=(\nabla_Uq)(L)-(\nabla_Lq)(U).
\end{aligned}
$$

The covariant product rule for $q(V)=\Theta(U,V)$ gives, for all vector fields $X,Y$,

$$
\begin{aligned}
(\nabla_Xq)(Y)
&=X\bigl(\Theta(U,Y)\bigr)-\Theta(U,\nabla_XY)\\
&=(\nabla_X\Theta)(U,Y)+\Theta(\nabla_XU,Y).
\end{aligned}
$$

Consequently

$$
\begin{aligned}
dq(U,L)
&=(\nabla_U\Theta)(U,L)+\Theta(\nabla_UU,L)\\
&\qquad-(\nabla_L\Theta)(U,U)-\Theta(\nabla_LU,U),\\
D
&=\tfrac12dw(U,L)-\Theta(\nabla_UU,L)+\Theta(\nabla_LU,U).
\end{aligned}
$$

The unchanged [spatial connection formula at line 3542](../paper/paper.tex#L3542) is

$$
\nabla e_{tu}+\Theta=q\otimes e_{tu}-\tfrac12e_{tu}\otimes w.
$$

Raising its second covariant index is allowed because $\nabla h=0$. For every $V\in\mathfrak X(\Sigma)$ this gives

$$
\nabla_VU=-S(V)+\Theta(U,V)U-\tfrac12e_{tu}(V)w^{\sharp}.
$$

In particular $e_{tu}(U)=1$ and $e_{tu}(L)=0$ give

$$
\begin{aligned}
\nabla_UU&=-S(U)+\Theta(U,U)U-\tfrac12w^{\sharp},\\
\nabla_LU&=-S(L)+\Theta(U,L)U.
\end{aligned}
$$

Substitution, keeping every term, yields

$$
\begin{aligned}
-\Theta(\nabla_UU,L)+\Theta(\nabla_LU,U)
={}&\Theta(S(U),L)-\Theta(U,U)\Theta(U,L)
+\tfrac12\Theta(w^{\sharp},L)\\
&-\Theta(S(L),U)+\Theta(U,L)\Theta(U,U)\\
={}&\tfrac12\Theta(w^{\sharp},L).
\end{aligned}
$$

The scalar products cancel in pairs. The other canceled pair satisfies

$$
\Theta(S(U),L)=h(S(U),S(L))=\Theta(S(L),U)
$$

because $S$ is self-adjoint. Symmetry leaves the $w$ contribution intact. The actual result is therefore

$$
\boxed{D=\tfrac12dw(U,L)+\tfrac12J}.
$$

The first incorrect transformation is the identification $dq(U,L)=D$ implicit in the modified component conversion. In fact $dq(U,L)=D-\tfrac12J$. This is the original displayed formula reconstructed by the product rule, not an added hypothesis or an alternative proof substituted for the submitted proof.

The other relevant passages do not supply $J=0$. Closedness of the dilaton gives $dw=-d(pe_{tu})$ [at line 3755](../paper/paper.tex#L3755), which constrains a derivative, not the contraction $J$. The transverse frame is parallel for the induced flat geometry **along leaves**; that does not set its ambient shape tensor or $\nabla_UU$ to zero. The later normalization $\mathfrak f_t=-\mathfrak a_t$ concerns the scale function. Finally, [compact rigidity](../paper/paper.tex#L4776) assumes a supersymmetric solution of the equations of motion with a compact Cauchy hypersurface, whereas the target assumes the first-order flow. The following example satisfies that first-order flow and has $J\ne0$.

### A full admissible flow, including the existing witness

The following common formula verifies both the existing witness and a compact version. On $\Sigma=\mathbb R^3$, let $F=F(x)$ and $G=G(z)$ be smooth real functions. On $\Sigma=(\mathbb R/2\pi\mathbb Z)^3$, use smooth periodic $F,G$ instead. Give $\Sigma$ the orientation $dx\wedge dy\wedge dz$. Take the trivial abelian gerbe with $Y=\Sigma$, $\pi=\operatorname{id}$, and the flat product connective structure, whose local connection potential is zero. Define

$$
\begin{gathered}
\chi_t=z+t e^{-F(x)},\qquad E_t=e^{G(\chi_t)},\\
e_{tu}=e^{F(x)}dz-tF'(x)dx,\qquad
e_{tl}=E_tdx,\qquad e_{tn}=dy,\\
\lambda_t=1,\qquad \mathfrak a_t=\mathfrak f_t=0,
\qquad\phi_t=e^{iF(x)},\qquad a_t=0,\\
c=e^{F(x)}F'(x)\,dz\wedge dx,\qquad b_t=t c.
\end{gathered}
$$

These are the pullbacks of the initial coframe by the complete flow

$$
\Phi_t(x,y,z)=(x,y,z+t e^{-F(x)}),\qquad
U_t=e^{-F(x)}\partial_z.
$$

For the torus, the last coordinate is taken modulo $2\pi$. All forms descend because $F,G$ are periodic. The coframe determinant is everywhere positive:

$$
e_{tu}\wedge e_{tl}\wedge e_{tn}
=e^{F(x)}E_t\,dx\wedge dy\wedge dz.
$$

The other dual fields and two useful scalar coefficients are

$$
\begin{gathered}
L_t=E_t^{-1}\bigl(\partial_x+t e^{-F(x)}F'(x)\partial_z\bigr),
\qquad N_t=\partial_y,\\
k_t=F'(x)E_t^{-1},\qquad r_t=e^{-F(x)}G'(\chi_t).
\end{gathered}
$$

Here $r_t$ is only a coefficient in this example, not the screen-rotation constant of the earlier skew-torsion theory. From the defining metric, directly,

$$
\partial_t e_{tu}=-k_t e_{tl},\qquad
\partial_t e_{tl}=r_t e_{tl},\qquad
\partial_t e_{tn}=0,
$$

and

$$
[\Theta_t]_{(U_t,L_t,N_t)}
=\begin{pmatrix}
0&k_t/2&0\\
k_t/2&-r_t&0\\
0&0&0
\end{pmatrix}.
$$

The spatial derivatives and flux are

$$
\begin{gathered}
d_\Sigma e_{tu}=-k_t e_{tu}\wedge e_{tl},\qquad
d_\Sigma e_{tl}=r_t e_{tu}\wedge e_{tl},\qquad
d_\Sigma e_{tn}=0,\\
d_\Sigma c=0,\qquad H_{b_t}=0,\qquad f_{b_t}=0,\qquad
\widehat c_t=c=k_t e_{tu}\wedge e_{tl},\\
\theta_t=k_t e_{tn},\qquad
\varphi_{\phi_t}=F'(x)dx=k_t e_{tl},\qquad p_t=0,\quad\eta_t=0,\\
w_t=k_t e_{tl}=F'(x)dx,\qquad q_t=\tfrac12F'(x)dx,
\qquad d_\Sigma q_t=d_\Sigma w_t=0.
\end{gathered}
$$

These formulas check **every equation of `eq:susyevol` directly**. For its three temporal coframe equations, the left sides are, respectively,

$$
\begin{aligned}
&-k_t e_{tl}+\tfrac12k_t e_{tl}+\tfrac12k_t e_{tl}=0,\\
&r_t e_{tl}+(\tfrac12k_t e_{tu}-r_t e_{tl})-\tfrac12k_t e_{tu}=0,\\
&0=0.
\end{aligned}
$$

For its spatial coframe equations the right sides are

$$
\begin{aligned}
q_t\wedge e_{tu}-\tfrac12\widehat c_t
&=-k_t e_{tu}\wedge e_{tl}=d_\Sigma e_{tu},\\
\Theta_t(L_t,-)\wedge e_{tu}
&=r_t e_{tu}\wedge e_{tl}=d_\Sigma e_{tl},\\
\Theta_t(N_t,-)\wedge e_{tu}&=0=d_\Sigma e_{tn}.
\end{aligned}
$$

The scale equations are $0=d_\Sigma\lambda_t(U_t)$ and $0=-q_t+\tfrac12w_t$. The algebraic equations are $\varphi_{\phi_t}=0e_{tu}+w_t$ and $f_{b_t}=*(\widehat c_t\wedge e_{tu})=0$.

The gerbe data are genuine curving data: for the identity submersion the simplicial difference vanishes, and the flat connective structure has curvature zero, so $\delta b_t=0=F_{\mathcal A}$. Also $\delta a_t=0=\partial_t\mathcal A-d\Psi_t$ with $\Psi_t=0$. Thus $\bar b=b_t$ is a curving on the product gerbe, $\partial_tb_t-d_\Sigma a_t=c$, and its four-dimensional curvature is $H_{\bar b}=dt\wedge c$. The dilaton is the displayed global map to $S^1$; its curvature is exactly $dF$. This verifies the domain and integrality requirements without selecting a gerbe or a dilaton from arbitrary local forms.

The choice $F(x)=x$, $G(z)=z$ gives exactly the $\mathbb R^3$ witness in the [tricker report](tricker_report.md#an-explicit-supersymmetry-flow-realizing-the-data) and [checker report](checker_report.md). At $t=0$, set $A=e^{-x}$ and $B=e^{-z}$. Then $k_0=B$, $r_0=A$, and the nonzero orthonormal-frame brackets and connection coefficients are

$$
\begin{gathered}
[U,L]=BU-AL,\qquad [U,N]=[L,N]=0,\\
\nabla_UU=-BL,\qquad\nabla_UL=BU,\qquad
\nabla_LU=AL,\qquad\nabla_LL=-AU.
\end{gathered}
$$

These follow from Koszul's formula applied to $h=e^{2z}dx^2+dy^2+e^{2x}dz^2$. Using $U(B)=-AB$, the two derivatives are

$$
\begin{aligned}
(\nabla_U\Theta)(U,L)
&=U(B/2)-\Theta(-BL,L)-\Theta(U,BU)\\
&=-AB/2-AB=-3AB/2,\\
(\nabla_L\Theta)(U,U)
&=L(0)-2\Theta(AL,U)=-AB.
\end{aligned}
$$

Hence

$$
D=-AB/2,\qquad \tfrac12dw(U,L)=0,\qquad
\tfrac12J=\tfrac12\Theta(BL,L)=-AB/2.
$$

In particular, at $t=x=z=0$ the discrepancy is exactly $-\tfrac12$. The $\mathbb R^3$ construction has a globally hyperbolic germ containing the initial slice by restriction to $\operatorname{Int}D(\Sigma)$, using the domain-of-dependence result stated and applied [at line 2142](../paper/paper.tex#L2142): here the initial slice is closed, spacelike, acausal and edgeless because $dt$ is timelike. This restriction retains the point and tensors just calculated. The compact realization below supplies a globally hyperbolic example on the whole product directly.

An independent coordinate calculation gives the same result. At $t=0$,

$$
\Theta_{xx}=-e^{2z-x},\qquad
\Theta_{xz}=\Theta_{zx}=\tfrac12e^x,
\qquad\Theta_{zz}=0.
$$

At $x=z=0$, $h$ is the identity matrix, $U=\partial_z$, $L=\partial_x$, and the nonzero Christoffel symbols are

$$
\Gamma^x_{xz}=\Gamma^x_{zx}=1,\quad\Gamma^x_{zz}=-1,
\quad\Gamma^z_{xx}=-1,\quad\Gamma^z_{xz}=\Gamma^z_{zx}=1.
$$

Thus

$$
\begin{aligned}
(\nabla_z\Theta)_{zx}
&=\partial_z\Theta_{zx}
-\Gamma^a_{zz}\Theta_{ax}-\Gamma^a_{zx}\Theta_{za}
=0-1-\tfrac12=-\tfrac32,\\
(\nabla_x\Theta)_{zz}
&=\partial_x\Theta_{zz}-2\Gamma^a_{xz}\Theta_{az}
=0-1=-1.
\end{aligned}
$$

This verifies the sign and coefficient independently of the disputed contraction formula, in agreement with the [existing exact checker calculation](checker_calculation.py).

### A compact globally hyperbolic realization

Take $\Sigma=(\mathbb R/2\pi\mathbb Z)^3$, $F(x)=\sin x$, and $G(z)=\sin z$ in the same construction. All the preceding first-order and curving checks apply. The metric $g=-dt^2+h_t$ on $\mathbb R\times\Sigma$ has each slice as a Cauchy hypersurface: on every compact time interval, smoothness and compactness give a uniform positive lower bound for $h_t$ relative to a fixed flat metric. A causal curve parametrized by $t$ therefore has bounded spatial speed on that interval. If its time parameter had a finite endpoint, its spatial component would converge and the curve could be extended. Thus every inextendible causal curve crosses every time slice, and the configuration is globally hyperbolic.

At $t=x=z=0$, these functions have the same required jets as $F(x)=x$, $G(z)=z$: $F=G=0$, $F'=G'=1$, $F''=G''=0$. Hence the coordinate metric and tensor derivatives just computed agree, giving again

$$
D=-\tfrac12,\qquad dw(U,L)=0,\qquad J=-1.
$$

This is a witness under the full globally hyperbolic hypothesis of the target theorem, with all fields given explicitly on the whole product. Its construction also confirms that the leafwise geometry and global dilaton or gerbe requirements do not remove the discrepancy.

### The downstream calculation retains a nonzero residual

The failure is used in the proof rather than being an unused side assertion. To check [line 3769](../paper/paper.tex#L3769) explicitly, abbreviate at fixed time

$$
\begin{gathered}
T=\operatorname{Tr}_h\Theta,\quad f=f_{b_t},\quad p=p_t,
\quad w_l=w(L),\quad w_n=w(N),\\
V=(\nabla^{h*}\Theta)(L)+L(T),\qquad
J=w_l\Theta(L,L)+w_n\Theta(N,L),\\
R=N(f)+f\Theta(N,U)+\tfrac12fw_n
+w_l\bigl(T-\Theta(U,U)\bigr).
\end{gathered}
$$

Canceling the common quadratic terms in the two printed Ricci formulas gives

$$
V+D=\tfrac12J-\tfrac12R.
$$

The two expressions in [lines 3757–3758](../paper/paper.tex#L3757), the Maxwell expression [at lines 3764–3765](../paper/paper.tex#L3764), and the definition of $\mathcal W$ read

$$
\begin{aligned}
dw(U,L)&=L(p)+p\Theta(U,L)+\tfrac12pw_l\\
&=U(w_l)-J+\tfrac12fw_n,\\
(*\mathcal M)(L)&=N(f)+f\Theta(U,N)-U(w_l)
+w_l\Theta(N,N)-w_n\Theta(L,N)-fw_n+pw_l,\\
\mathcal W(L)&=V+L(p)+p\Theta(U,L)+J+\tfrac12fw_n.
\end{aligned}
$$

If the **modified** value $D=\tfrac12dw(U,L)$ is substituted, the first equation gives $V=\tfrac12J-\tfrac12R-\tfrac12dw(U,L)$. Therefore

$$
\begin{aligned}
\mathcal W(L)
&=\tfrac12J-\tfrac12R-\tfrac12dw(U,L)
+\bigl(dw(U,L)-\tfrac12pw_l\bigr)+J+\tfrac12fw_n\\
&=\tfrac32J-\tfrac12R+\tfrac12\bigl(U(w_l)-J+\tfrac12fw_n\bigr)
-\tfrac12pw_l+\tfrac12fw_n\\
&=-\tfrac12(*\mathcal M)(L)+\tfrac12J.
\end{aligned}
$$

The final printed claim instead has no $\tfrac12J$. The original product-rule correction removes precisely this residual. Thus the modified proof fails to establish the transverse part of `eq:constraintidentities`, which is later used to identify the mixed Einstein defect [at lines 4254–4258](../paper/paper.tex#L4254) and to reduce the constraint propagation problem. The algebraic and quantified downstream steps inherit this computational gap.

## Final direct labels and comparison

**Final direct labels: CONV only.** This agrees with the [case README](../README.md#error-and-classification), [tricker classification](tricker_report.md#conv-audit-definitions-and-starting-expression), and [original checker report](checker_report.md). No label is added or removed.

The verified direct failure is the conversion of $d_\Sigma(\Theta_t(e_{tu}))$ into covariant derivatives of $\Theta_t$ while omitting the derivative of the contracted moving field. The local MP applications are valid; the later application has a downstream MP failure because its compatibility premise has not been established by the submitted proof. The quantifier scopes and scale-witness elimination are valid, and the geometric objects are well-defined. The proof of the all-time compatibility statement and its subsequent uses inherit the demonstrated CONV error. The explicit witnesses verify the original correction's sign and coefficient, and no unresolved mathematical issue affects this classification.
