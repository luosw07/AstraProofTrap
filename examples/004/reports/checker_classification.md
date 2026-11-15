# 004: Post-workflow classification review

**Review agent:** GPT 6 Astra

**Reasoning effort:** max

This is a subsequent AI-agent classification review prepared after completion and curation of the original workflow. It is informed by the source and the existing construction/checker materials, rather than being an original workflow report or a blind reviewer run. The audit follows [the classification standard](../../../protocol/classification.md) and [the assigned review template](../../../protocol/checker-classification-template.txt).

The final direct labels are **DEF, CONV**. The missing transpose breaks both the specified equivariant construction and an explicit differential calculation. The later invocation of Lemma 6.2 inherits the false equation identification; it is recorded below as a downstream MP failure.

## Target, actual assumptions, and evidence

The target is Proposition 6.3, especially [equation (6.7) and its verification, modified TeX lines 3202–3233](../paper/paper.tex#L3202). The modification replaces

$$
d\eta=J_u^{\mathsf T}\beta
\quad\text{by}\quad
d\eta=J_u\beta,
$$

adds the claim that covariance keeps the same operator, and changes the ensuing description of the fixed-vector equation. The [original passage](../original/paper.tex#L3187) and [exact patch](../mutation.diff) fix precisely those three changes. A complete comparison of the two source files agrees with the supplied patch; their figures are identical. I read the complete modified manuscript, the original passage together with the common source text, the [tricker report](tricker_report.md), the [existing checker report](checker_report.md), and the [case README](../README.md). The two figures describe the same local-to-global dependency traced below. Reviewer verdicts and detection counts were not used.

The witness was independently recomputed from the defining matrices using exact rational arithmetic. The calculations below verify the symplectic triple, resonance actions, derivative discrepancy, stabilizer obstruction, both equation-scheme points, and the flag-map obstruction.

The actual local data, fixed in [§6.1, lines 3002–3123](../paper/paper.tex#L3002), are:

- $k=\overline{\mathbb Q}_\ell$, of characteristic zero; $L$ is the split semisimple dual group, $r=q^d>1$, and $t=m(r^{1/2})c\in L(k)$ is the selected semisimple element. The algebraic compact factor $c$ commutes with the chosen $\mathrm{SL}_2$.
- $H=Z_L(t)$ is connected, $m:\mathbb G_m\to H$ is central, $W=\ker(\operatorname{Ad}(t)-r^{-1})$, and $E_+=\ker(\operatorname{Ad}(t)-r)$. Their $m$-weights are $-2$ and $2$. The fixed invariant form identifies $W^*=E_+$, and each representation has finitely many $H$-orbits.
- $U_H\subset H$ is a smooth affine saturated neighborhood of the identity class for the conjugation quotient. Every permitted shrinking retains **all unipotent elements**, by [Lemma 6.1, lines 3021–3063](../paper/paper.tex#L3021). Put $A_0=\mathcal O(U_H)$; its differential and $m$-weight are zero.
- In a basis $w_1,\ldots,w_n$ of $W$, the paired generators $x_i,\theta_i,p_i,l_i$ belong to copies of $W^*$. With $J(u)=\operatorname{Ad}(u)|_W-I$, the unchanged formulas are

  $$
  R_-=A_0[x_1,\ldots,x_n]\otimes\Lambda(\theta_1,\ldots,\theta_n),
  \qquad d\theta_i=\sum_jJ_{ij}(u)x_j,
  $$

  $$
  K'=R_-\otimes\Lambda(p_1,\ldots,p_n)\otimes k[l_1,\ldots,l_n],
  \qquad dp_i=x_i,\qquad dl_i=\theta_i-\sum_jJ_{ij}(u)p_j.
  $$

  The degrees of $x,\theta,p,l$ are $0,-1,-1,-2$, all of weight $2$. The augmentation $\epsilon:K'\to A_0$ kills these generators. These are the explicit vector-coordinate conventions of [lines 3187–3200](../paper/paper.tex#L3187).
- The proposed acting algebra is

  $$
  B^0_{\mathrm{bad}}=A_0\otimes\Lambda(\eta_1,\ldots,\eta_n)
                      \otimes k[\beta_1,\ldots,\beta_n],
  \qquad d_{\mathrm{bad}}\eta_i=\sum_jJ_{ij}(u)\beta_j,
  \qquad d\beta_i=0.
  $$

  Both generator spaces are the prescribed representation $W$, with degrees $1,2$ and weight $-2$. The subscript “bad” distinguishes the submitted differential; it changes no manuscript object. Shearing changes these degrees to $-1,0$. The target remains the actual scheme

  $$
  Y=\{(u,e)\in U_H\times E_+:\operatorname{Ad}(u)e=e\}.
  $$

The distinction between a quotient value and an actual group element matters. [§7, lines 4446–4460](../paper/paper.tex#L4446) localizes at the identity **class** in $U_H/\!/H$; [§8.1, lines 4753–4756](../paper/paper.tex#L4753) expressly retains variable unipotent $u$. Neither passage imposes $u=1$. The later occurrence of “transpose equation” at [line 3548](../paper/paper.tex#L3548) uses the already defined $B^0$ and its alleged scalar extension; it supplies no replacement differential or map. The coordinate freedom in [Proposition 6.7, lines 3845–3855](../paper/paper.tex#L3845) still requires equivariance over $U_H$.

### Admissible local witness

Take $k=\overline{\mathbb Q}_3$, $q=5$, $L=\operatorname{Sp}_4$, and the split dual group $G=\operatorname{SO}_5$. With $I=I_2$, put

$$
\Omega_{\mathrm{sp}}=\begin{pmatrix}0&I\\-I&0\end{pmatrix},\qquad
e_0=\begin{pmatrix}0&I\\0&0\end{pmatrix},\quad
f_0=\begin{pmatrix}0&0\\I&0\end{pmatrix},\quad
h=\begin{pmatrix}I&0\\0&-I\end{pmatrix}.
$$

These matrices satisfy the symplectic Lie condition and

$$
[e_0,f_0]=h,\qquad [h,e_0]=2e_0,\qquad [h,f_0]=-2f_0.
$$

Since $e_0^2=0$ and $\operatorname{rank}(e_0)=2$, its nilpotent type is $(2,2)$. The corresponding homomorphism $\phi:\mathrm{SL}_{2,k}\to\operatorname{Sp}_{4,k}$ and cocharacter are

$$
\phi\begin{pmatrix}a&b\\c&d\end{pmatrix}
 =\begin{pmatrix}aI&bI\\cI&dI\end{pmatrix},
\qquad m(z)=\operatorname{diag}(zI,z^{-1}I).
$$

For an arbitrarily large integer $N\geq0$, choose

$$
d=4\cdot3^N,\qquad s_0=25^{3^N}=5^{d/2},\qquad
r=s_0^2,\qquad t=m(s_0),\qquad c=1.
$$

Here $s_0$ is a scalar, not the manuscript's Iwahori holonomy coordinate. The compactness requirement is satisfied by $c=1$; the degree is divisible by the order $2$ of the length-zero group for $G$. Also

$$
v_3(s_0-1)=N+1:
\quad a^3-1=(a-1)(a^2+a+1),\quad
v_3(a^2+a+1)=1\ \text{when }a\equiv1\pmod3.
$$

Thus the congruence neighborhood in Lemma 3.1 imposes no obstruction. Since $s_0\ne s_0^{-1}$,

$$
H=\{\operatorname{diag}(g,g^{-\mathsf T}):g\in\operatorname{GL}_2\}
 \simeq\operatorname{GL}_2.
$$

The only nontrivial central translate is $-t$; its eigenvalue multiset could agree with that of $t$ only if $s_0^2=-1$, which is false. The adjoint centralizer is consequently $H/\{\pm I_4\}$, also connected, with the required central-torsor behavior. The resonance spaces are

$$
W=\left\{\begin{pmatrix}0&0\\X&0\end{pmatrix}:X=X^{\mathsf T}\right\},
\qquad
E_+=\left\{\begin{pmatrix}0&Z\\0&0\end{pmatrix}:Z=Z^{\mathsf T}\right\}.
$$

Their actions are $X\mapsto g^{-\mathsf T}Xg^{-1}$ and $Z\mapsto gZg^{\mathsf T}$. Symmetric matrices have the three rank orbits; the open orbit consists of invertible matrices, and the stabilizer of $I_2$ is reductive $O_2$. Both $Z(L)$ and $m(-1)=-I_4$ act trivially on these spaces, so the retained neutral and even sectors include this model.

Choose

$$
g=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
u_0=\operatorname{diag}(g,g^{-\mathsf T})\in H.
$$

This nontrivial unipotent belongs to every allowed $U_H$. The local assertion of Proposition 6.3 is about the entire category on that slice, including the augmentation module $A_0$; it has no additional support condition on this point. The witness tests that local construction under its stated hypotheses.

For $X=\left(\begin{smallmatrix}x_1&x_2\\x_2&x_3\end{smallmatrix}\right)$, direct conjugation gives

$$
g^{-\mathsf T}Xg^{-1}
 =\begin{pmatrix}x_1&x_2-x_1\\x_2-x_1&x_3-2x_2+x_1\end{pmatrix},
\qquad
J=\begin{pmatrix}0&0&0\\-1&0&0\\1&-2&0\end{pmatrix}.
\tag{1}
$$

Hereafter $J=J(u_0)$. All subsequent countercalculations use this one allowed point and these same paired bases.

## Five-rule audit

| Rule | Status | Role | Location | Note |
|---|---|---|---|---|
| MP | violated | downstream | [Lemma 6.2 applied at lines 3228–3229](../paper/paper.tex#L3228) | The required identification with the genuine equation algebra is false because of the preceding conversion. [Full Note](#mp-note). |
| G1 | not_violated | none | [Generic coordinate calculation, lines 3187–3219](../paper/paper.tex#L3187); [coherent inputs, lines 3235–3260](../paper/paper.tex#L3235); [full faithfulness, lines 3363–3379](../paper/paper.tex#L3363) | The quantified parameters are unrestricted in the asserted range; the failed calculation precedes quantification. [Full Note](#g1-note). |
| G2 | not_violated | none | [Choice of derivative sign and action, lines 3211–3222](../paper/paper.tex#L3211) | The candidate is explicitly specified. Its chain condition is false; no witness escapes its scope and no weaker existential premise is legitimately supplied. [Full Note](#g2-note). |
| DEF | violated | direct | [Acting equivariant algebra and map, lines 3202–3219](../paper/paper.tex#L3202); [target realization, lines 3224–3229](../paper/paper.tex#L3224) | The proposed differential fails the prescribed stabilizer action, and the derivative operators fail to define the required dg action. [Full Note](#def-note). |
| CONV | violated | direct | [Differential computation, lines 3209–3219](../paper/paper.tex#L3209); [fixed-vector conversion, lines 3225–3228](../paper/paper.tex#L3225) | Expansion yields $J^{\mathsf T}$, while the printed $J$ gives different equations at admissible data. [Full Note](#conv-note). |

<a id="mp-note"></a>

## MP — Note

**Status: violated; role: downstream.** The actual cited application is to [Lemma 6.2](../paper/paper.tex#L3125) at [line 3229](../paper/paper.tex#L3229). The original rule is

$$
\frac{\Gamma\vdash A\qquad\Gamma\vdash A\longrightarrow B}
     {\Gamma\vdash B}.
$$

Here $\Gamma_{\mathrm{MP}}$ is a logical context, distinct from the manuscript's Weil group. Its components are: the characteristic-zero field $k$; the split group $L$, scalar $r$, selected $t$, connected centralizer $H$, central cocharacter $m$, paired representations $W,E_+$, and saturated smooth affine $U_H$ specified above; their stated finite-orbit properties; the fixed basis and invariant pairing; $A_0,R_-,K',\epsilon$ with their unchanged formulas; the submitted formula for the underlying dg algebra $B^0_{\mathrm{bad}}$ and its shear; and the actual statement and proof of Lemma 6.2. It contains neither an assumption that $J=J^{\mathsf T}$ nor the false assertion that the submitted equations already define $Y$.

For complete instantiation of the lemma, let $V$ be a finite-dimensional rational $H$-representation, with action $\rho_V$, and write

$$
Z_V=\{(u,v)\in U_H\times V:(\rho_V(u)-I)v=0\},
$$

$$
K_V=A_0\otimes\operatorname{Sym}(V^*)\otimes\Lambda(V^*[1]),
\qquad d\theta_\alpha=\langle\alpha,(\rho_V(u)-I)v\rangle.
$$

The following is a symbolic reconstruction of the lemma's argument, retaining its assumptions. Its antecedent $D(V)$ says that $U_H$ is smooth of dimension $\dim H$, contains $1$, and that $V$ has finitely many $H$-orbits. For each orbit $\mathcal Q$, the solution stratum has dimension

$$
\dim\mathcal Q+\dim Z_H(v)=\dim H,
$$

because $U_H\cap Z_H(v)$ is a nonempty open. Consequently $Z_V$ has dimension $\dim H$, and its $\dim V$ displayed equations in the smooth $U_H\times V$ form a regular sequence. Thus the instantiated implication is

$$
D(E_+)\ \Longrightarrow
\bigl(K_{E_+}\xrightarrow{\sim}\mathcal O(Y)
\text{ by its equation augmentation, with }Y=Z_{E_+}
\text{ a complete intersection}\bigr).
\tag{2}
$$

This application to the shear of $B_{\mathrm{sph}}^0$ is valid: that algebra has exactly the differential $(\operatorname{Ad}(u)-I)e$ in [equation (6.3)](../paper/paper.tex#L3096).

To apply (2) to the submitted shear $B_{\mathrm{bad}}$, the proof first needs $I_{\mathrm{bad}}$: the paired identification $W^*=E_+$, followed by multiplication of the equation vector by $-\rho_+(u)$, identifies $B_{\mathrm{bad}}$ with $K_{E_+}$ as an $H$-equivariant dg $A_0$-algebra, preserving the base and the specified polynomial coordinates. Here $\rho_+(u)=\operatorname{Ad}(u)|_{E_+}$. The complete antecedent and consequent for the attempted application are therefore

$$
A=D(E_+)\land I_{\mathrm{bad}},
$$

$$
B=\bigl(B_{\mathrm{bad}}\longrightarrow\mathcal O(Y)
\text{ is the corresponding equivariant quasi-isomorphism of equation algebras}\bigr).
$$

The actual claimed conclusion $C$ in lines 3228–3230 is this same $B$, with the ensuing identification with the spherical equation scheme. It is not an export stronger than the consequent. The relevant proof fragment is

$$
\Gamma_{\mathrm{MP}}\vdash D(E_+),\qquad
\Gamma_{\mathrm{MP}}\vdash
 (D(E_+)\land I_{\mathrm{bad}})\longrightarrow B,
\qquad
\boxed{\Gamma_{\mathrm{MP}}\nvdash I_{\mathrm{bad}}}.
\tag{3}
$$

The first failed MP obligation is the unestablished antecedent $I_{\mathrm{bad}}$. At the witness (1), the true fixed-vector fiber has paired polynomial coordinates $(\beta_1,\beta_2,\beta_3)=(a,0,0)$, whereas the bad equations require $\beta_1=\beta_2=0$. In particular the proposed equation augmentation to the true fiber would send

$$
d_{\mathrm{bad}}\eta_2=-\beta_1\longmapsto-a\ne0,
$$

although it sends $\eta_2$ to zero. It is not even a chain map there. The CONV Note derives this discrepancy without using the desired conclusion.

The provenance is important for classification: the false antecedent is exactly the preceding failed fixed-vector conversion, not a missing additional geometric hypothesis of Lemma 6.2. The lemma's genuine application to $B_{\mathrm{sph}}^0$ remains intact. Likewise the derivative paragraph does not cite a theorem whose consequent is “covariance preserves the matrix”; it claims to calculate that equality. Thus the target's direct failures are CONV and DEF, while (3), the later reconstruction, and the global uses propagate those failures.

<a id="g1-note"></a>

## G1 — Note

**Status: not_violated; role: none.** The rule to test is

$$
\frac{\Gamma\vdash A\longrightarrow B(x)}
 {\Gamma\vdash A\longrightarrow\forall x\,B(x)},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(A).
$$

There are two concrete quantified structures near this target. First, the coordinate calculation is performed for the universal $u\in U_H$ and each basis index $j\in\{1,\ldots,n\}$. Let $\Gamma_{\mathrm{coord}}$ consist of the fixed local data $k,L,r,t,H,m,U_H,A_0,W,E_+$, their pairing and basis, and the definitions of $R_-,K',J$ and the endomorphism differential. It has no particular $u$ or $j$ as an open assumption. Taking $A=\top$, the *correct* pre-generalization calculation for a fresh $u$ and $j$ proves

$$
u\in U_H\land 1\leq j\leq n
\quad\Longrightarrow\quad
[d,-\partial_{p_j}]=\sum_iJ_{ij}(u)\partial_{l_i}.
\tag{4}
$$

Discharging the two range assumptions gives the legitimate quantified statement

$$
\forall u\,\Bigl(u\in U_H\longrightarrow
 \forall j\in\mathbb Z\,
 \bigl(1\leq j\leq n\longrightarrow
 [d,-\partial_{p_j}]=\sum_iJ_{ij}(u)\partial_{l_i}\bigr)\Bigr).
\tag{5}
$$

The manuscript claims the coefficients $J_{ji}(u)$ instead. That fails already for $u=u_0,j=1$, before any generalization: evaluation on $l_2$ is $-1$, while its claimed value is $0$. No derivation first assumes $u=1$, a diagonalizable $J$, or $J=J^{\mathsf T}$ and then drops that restriction. The failure is in the symbolic computation of the selected case, as detailed in the CONV Note; writing its asserted scope universally supplies no separate quantifier error.

Second, [lines 3235–3260](../paper/paper.tex#L3235) address every coherent input, and [lines 3363–3379](../paper/paper.tex#L3363) export full faithfulness. To make this structure explicit, fix a universe of rational $H$-equivariant dg $R_-$-modules. Define

$$
\begin{aligned}
D(M):\ &M\text{ has a degree-one square-zero differential, compatible}\\
 &R_-\text{- and rational }H\text{-actions, and bounded cohomology}\\
 &\text{finitely generated over }H^0(R_-);\\
P(M):\ &\operatorname{sh}\underline{\operatorname{RHom}}_{R_-}(A_0,M)
\text{ with the specified action is in }\operatorname{Coh}^H(Y).
\end{aligned}
$$

Let $\mathcal C$ denote the earlier, module-independent construction assertion: the specified derivative map supplies the $H$-equivariant dg $B^0$-action, its augmentation comparison is a quasi-isomorphism, and the sheared algebra is the stated equation algebra on $Y$. This is the assertion that fails in this submission. Let $\Gamma_{\mathrm{G1}}$ consist of the fixed local data and formulas above, the definitions of $D,P,\mathcal C$, exact rational invariants, and the usual coherent-module, Hom, and grading operations used in the displayed proof. Its free parameters are $k,L,r,t,H,m,U_H,A_0,W,E_+$, the fixed basis, and the fixed algebras and maps; they do not include $M$ or $M'$.

A symbolic reconstruction isolating the actual dependency, without adding an assumption to the submitted proof, is

$$
\begin{array}{ll}
[\mathcal C]^1;&\text{the previously asserted construction;}\\
\bigl[D(M)\bigr]^2;&M\text{ is an arbitrary coherent input;}\\
&\text{a finite cohomology filtration reduces to a finite }H^0(R_-)
  \text{-module in one degree;}\\
&\operatorname{Hom}_{R_-}(K',M)\text{ has finite cohomology over }A_0[\beta],\\
&\text{since }x_i=[d,p_i]\text{ acts null-homotopically;}\\
&\text{each }\beta_i\text{ has sheared degree }2+(-2)=0,\\
&\text{so finitely many homogeneous generators give bounded coherent shear;}\\
&P(M);\\
&D(M)\to P(M)\quad(\to I,\text{ discharging }2);\\
&\forall M\,(D(M)\to P(M))\quad(\forall I);\\
&\mathcal C\to\forall M\,(D(M)\to P(M))
  \quad(\to I,\text{ discharging }1).
\end{array}
\tag{6}
$$

Thus in the rule as requested, $x=M$, $A=\mathcal C$, and $B(M)=D(M)\to P(M)$. The finite-module-in-one-degree condition is used inside the finite-filtration reduction; it is not silently imposed on the final range. Before universal introduction the open $M$-dependent assumption $D(M)$ has been discharged. The remaining construction assumption $\mathcal C$ is independent of $M$.

For the pair of coherent inputs in the full-faithfulness assertion, $G_0(M)=\underline{\operatorname{RHom}}_{R_-}(A_0,M)$ and $L_0$ is the claimed left adjoint from dg $B^0$-modules to dg $R_-$-modules. Conditional on $\mathcal C$, it is tensoring with the augmentation Koszul bimodule, represented by $K'$ with the right $B^0$-action induced from the derivative action. The displayed fragment is

$$
\operatorname{Hom}^\bullet_{R_-,H}(M,M')
\simeq\operatorname{Hom}^\bullet_{R_-,H}(L_0G_0M,M')
\simeq\operatorname{Hom}^\bullet_{B^0,H}(G_0M,G_0M').
$$

Its stated range is precisely

$$
\forall M\,\forall M'\,
\bigl((D(M)\land D(M'))\to
\text{the displayed comparison is an isomorphism in every degree}\bigr).
\tag{7}
$$

Both inputs remain arbitrary; their coherence assumptions are discharged into (7). The mathematical use of the specified action and of $L_0$ inherits the failed construction $\mathcal C$. Neither (6) nor (7) exports a parameter subject to an undisclosed special choice. This explains the negative G1 finding while recording exactly where the asserted universal functor loses its foundation.

<a id="g2-note"></a>

## G2 — Note

**Status: not_violated; role: none.** The original rule is

$$
\frac{\Gamma\vdash A(x)\longrightarrow B}
 {\Gamma\vdash(\exists x\,A(x))\longrightarrow B},
\qquad x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(B).
$$

The target's phrase “Choosing the sign of the derivative in $p$” supplies an explicit local construction, rather than an arbitrary witness taken from an existence theorem. Its concrete operation can be written as follows. For signs $\varepsilon_j\in\{1,-1\}\subset k$, define the graded algebra map

$$
\rho_{\varepsilon}(\eta_j)=\varepsilon_j\partial_{p_j},
\qquad \rho_{\varepsilon}(\beta_i)=\partial_{l_i},
\qquad \rho_{\varepsilon}|_{A_0}=\text{scalar multiplication}.
$$

Graded commutation of these derivatives establishes the graded algebra map. To be the asserted dg map it additionally requires, for **every** $i,j$,

$$
-\varepsilon_jJ_{ij}(u)=J_{ji}(u).
\tag{8}
$$

The actual sign properties are only membership in $\{1,-1\}$; equation (8) is the computed property the passage claims to verify. At $u_0,i=2,j=1$, (8) would give $\varepsilon_1=0$. Thus even independent sign choices cannot make the specified construction work. This identifies a failed differential calculation, not a witness-variable restriction or a quantifier-order exchange.

For completeness, the existential sufficiency behind obtaining a module action has the following fully scoped formulation. This is a reconstruction of that logical interface, not a substitute construction. Put

$$
E=\underline{\operatorname{End}}_{R_-}(K'),\qquad
\delta(T)=d_{K'}T-(-1)^{|T|}Td_{K'}.
$$

Let $x=\rho$ range over degree-zero unital $A_0$-linear maps of graded algebras $B^0_{\mathrm{bad}}\to E$. Define $A(\rho)$ to include exactly the properties needed for the advertised action:

1. The prescribed rational $H$-action on $B^0_{\mathrm{bad}}$ commutes with its differential.
2. $\rho$ is $H$-equivariant and $\delta\rho(b)=\rho(d_{\mathrm{bad}}b)$ for every homogeneous $b\in B^0_{\mathrm{bad}}$.
3. The scalar map is the specified $A_0$-action. The multiplication and unit conditions are part of the stated domain of $\rho$.

Let $B_{\mathrm{act}}$ be the proposition that there exists a natural family $\mu=(\mu_M)_M$ of unital rational $H$-equivariant dg $B^0_{\mathrm{bad}}$-module structures on the complexes

$$
G_0(M)=\underline{\operatorname{Hom}}_{R_-}(K',M)
$$

for rational equivariant dg $R_-$-modules $M$, preserving their given differentials and compatible with their module maps. This conclusion quantifies the family $\mu$ internally and contains no free $\rho$. The context $\Gamma_{\mathrm{G2}}$ comprises the fixed field, group, local spaces, paired bases, $A_0,R_-,K',B^0_{\mathrm{bad}},E,G_0$, their displayed formulas, and graded composition; it contains no chosen $\rho$, sign, or $\mu$.

The actual existential-elimination subderivation, were the construction premise available, is

$$
\begin{array}{ll}
[\exists\rho\,A(\rho)]^1;&\\
\quad[A(\rho_*)]^2;&\rho_*\text{ a fresh witness;}\\
\quad\mu^{\rho_*}_M(b,f)
 =(-1)^{|b||f|}f\circ\rho_*(b);&\text{a construction inside this witness scope;}\\
\quad d\mu^{\rho_*}_M(b,f)
 =\mu^{\rho_*}_M(db,f)+(-1)^{|b|}\mu^{\rho_*}_M(b,df);&\text{by property 2;}\\
\quad\mu^{\rho_*}\text{ satisfies the unit, multiplication,};&\\
\quad H\text{-equivariance, and naturality conditions};&\text{by properties 1--3;}\\
\quad B_{\mathrm{act}};&\exists I\text{ on the family }\mu;\\
B_{\mathrm{act}};&\exists E\text{ discharging }2;\\
(\exists\rho A(\rho))\to B_{\mathrm{act}};&\to I\text{ discharging }1.
\end{array}
\tag{9}
$$

The dependence of $\mu^{\rho_*}$ on $\rho_*$ remains inside its scope and is packaged into the existentially quantified family. The names $\rho_*,\mu^{\rho_*}$ are absent from the exported proposition. The free-variable side condition is therefore satisfied, and the conditional derivation uses all the actual required witness properties explicitly.

In the manuscript the concrete derivative candidate is supposed to establish this premise, and fails both the differential and equivariance requirements. Replacing $A(\rho)$ by “a graded map exists” or by “a sign exists” would omit those requirements; that is not an established premise or a valid alternative reading of the claimed verification. No separate existential-elimination step introduces the defect. In particular, no passage exchanges $\forall u\exists\varepsilon$ with $\exists\varepsilon\forall u$: the derivative calculation already fails at the single $u_0$, for every sign.

<a id="def-note"></a>

## DEF — Note

**Status: violated; role: direct.** The construction contract is the $H$-equivariant acting dg algebra and its specified action on $G_0$, not merely the existence of an abstract graded algebra with a square-zero derivation.

The objects and their individual obligations are concrete:

1. **The unchanged equation algebra and resolution.** $R_-$, $K'$, and $\epsilon:K'\to A_0$ have the formulas, degrees, and equivariant types recorded above. Their differentials are well-defined. In particular

   $$
   d^2l_i=d\theta_i-\sum_jJ_{ij}dp_j
       =\sum_jJ_{ij}x_j-\sum_jJ_{ij}x_j=0.
   $$

   Replacing $\theta$ by $\widetilde\theta=\theta-Jp$ gives $dp=x$, $dl=\widetilde\theta$, $d\widetilde\theta=0$. The first pairs are the coordinate Koszul contractions. For the second pairs,

   $$
   d(l_i^{a+1})=(a+1)l_i^a\widetilde\theta_i,
   $$

   so division by $a+1$ provides the contraction in characteristic zero. The augmentation is a quasi-isomorphism. The ordinary internal derived Hom $G_0$ consequently exists.
2. **The submitted free algebra.** On the underlying graded free $A_0$-algebra $B^0_{\mathrm{bad}}$, the prescribed generator values extend uniquely to a degree-one derivation. Since $J_{ij}\in A_0$ and all $\beta_j$ are closed,

   $$
   d_{\mathrm{bad}}^2\eta_i
   =\sum_j(dJ_{ij})\beta_j+\sum_jJ_{ij}d\beta_j=0.
   $$

   Thus forgetting the required group action does yield an ordinary dg algebra. There is no recursion issue.
3. **The equivariant algebra and acting map.** The required object lies in rational $H$-equivariant dg $A_0$-algebras, with the two specified copies of $W$. Its proposed action is the graded map

   $$
   \rho_{\mathrm{bad}}:B^0_{\mathrm{bad}}\longrightarrow
      \underline{\operatorname{End}}_{R_-}(K'),
   \qquad \eta_j\mapsto-\partial_{p_j},\quad
          \beta_i\mapsto\partial_{l_i}.
   $$

   It must commute with differentials and with $H$. These are defining requirements of the object and of the module action. They fail below. Composing with $\epsilon$ consequently does not give the claimed map of complexes to $\underline{\operatorname{RHom}}_{R_-}(A_0,A_0)$.
4. **Shear and the target functor.** Shear itself is the specified reindexing $M_w^d\mapsto M_w^{d+w}$ on the even sector. It is well-defined and does not change the coefficients of $d$. The actual $Y\subset U_H\times E_+$ is the well-defined zero locus of $\operatorname{Ad}(u)e-e$. What fails is the construction of $\mathcal K:\operatorname{Coh}^H(R_-)\to\operatorname{Coh}^H(Y)$ by the particular $B^0$-action and equation identification in lines 3202–3229. The ordinary underlying Hom complex does not supply those missing structures.

At the witness (1), the claimed dg map already fails on one generator:

$$
d_{\mathrm{bad}}\eta_1=0,
\qquad
\delta\rho_{\mathrm{bad}}(\eta_1)(l_2)
 =[d,-\partial_{p_1}](l_2)=-1.
\tag{10}
$$

This contradicts a defining chain-map equation. Even independently of the chosen derivative realization, the prescribed $H$-equivariant algebra is invalid. The element $u_0$ fixes the base point $u_0\in U_H$ under conjugation. On the actual basis vectors of either copy of $W$, its action is

$$
\begin{aligned}
u_0\eta_1&=\eta_1-\eta_2+\eta_3,&
u_0\beta_1&=\beta_1-\beta_2+\beta_3,\\
u_0\eta_2&=\eta_2-2\eta_3,&
u_0\beta_2&=\beta_2-2\beta_3,\\
u_0\eta_3&=\eta_3,&
u_0\beta_3&=\beta_3.
\end{aligned}
$$

The bad differential satisfies

$$
d_{\mathrm{bad}}(u_0\eta_3)=\beta_1-2\beta_2,
\qquad
u_0(d_{\mathrm{bad}}\eta_3)=\beta_1-3\beta_2+5\beta_3,
\tag{11}
$$

They differ. Equivalently, put $R=I+J$, the matrix whose $j$th column gives $u_0w_j$. The matrix of the bad differential as a linear map **on basis vectors** is $J^{\mathsf T}$, because $d_{\mathrm{bad}}\eta_j=\sum_iJ_{ji}\beta_i$. Its equivariance defect is

$$
RJ^{\mathsf T}-J^{\mathsf T}R
 =\begin{pmatrix}-2&2&0\\2&-3&-1\\0&-1&5\end{pmatrix}\ne0.
\tag{12}
$$

This distinction between a column of named generators and a matrix on basis vectors fixes the transpose convention explicitly. The correctly computed differential has basis-map matrix $J$, which commutes with $R=I+J$.

After shear, the derived fiber's zeroth cohomology provides the same obstruction:

$$
H^0(B_{\mathrm{bad}}\otimes^{\mathbf L}_{A_0}k(u_0))
 =k[\beta_1,\beta_2,\beta_3]/(\beta_1,\beta_2).
$$

The ideal is not stable, since $u_0\beta_2=\beta_2-2\beta_3$. This is a computation of a derived base fiber, not a claim that the whole family has higher cohomology. It proves that the prescribed action cannot descend even at this stabilizer. A simultaneous change of basis preserves whether the differential is equivariant. Accordingly, basis choices or a reinterpretation of representatives do not define the required quotient-stack object.

There is also a concrete downstream construction failure in [Proposition 6.5, lines 3472–3485](../paper/paper.tex#L3472). Let $\mathcal B$ be the Borel determined by positive weights of

$$
\lambda(z)=\operatorname{diag}(z^2,z^{-1},z^{-2},z).
$$

Its weights on $w_1,w_2,w_3$ are $-4,-1,2$, so $W_{\mathcal B}=k w_3$. The two nonzero entries of $u_0-I$ have weight $3$, so $u_0\in\mathcal B\cap H$. On $W_{\mathcal B}$, $J=0$; hence its small algebra has $d\eta_3=0$. The prescribed inclusion into the large submitted algebra sends it to $\eta_3$, with

$$
d_{\mathrm{bad}}\eta_3=\beta_1-2\beta_2\ne0.
$$

The claimed dg algebra inclusion and the scalar extension along it are therefore unavailable. This demonstrates propagation into an actual flag calculation. It is separate from the direct construction failure (10)–(12), and explains why the later “transpose equation” sentence is not a completed alternate construction.

<a id="conv-note"></a>

## CONV — Note

**Status: violated; role: direct.** The starting expression is the differential of the derivative operators on the unchanged augmentation resolution. The claimed endpoint is the differential in (6.7), $d\eta=J_u\beta$, asserted to follow by a choice of sign in [lines 3211–3219](../paper/paper.tex#L3211).

Take the permitted convention

$$
\eta_j\longmapsto-\partial_{p_j},\qquad
\beta_i\longmapsto\partial_{l_i}.
$$

On the endomorphism complex, $|\partial_{p_j}|=1$, so

$$
\delta(-\partial_{p_j})
 =d(-\partial_{p_j})+(-\partial_{p_j})d.
$$

This is an $R_-$-linear derivation and can be evaluated on the free generators. It vanishes on $A_0,x_i,\theta_i,p_i$. On $l_i$, the material steps are

$$
\begin{aligned}
\delta(-\partial_{p_j})(l_i)
 &=d\bigl(-\partial_{p_j}l_i\bigr)
   -\partial_{p_j}\bigl(dl_i\bigr)\\
 &=0-\partial_{p_j}
       \left(\theta_i-\sum_aJ_{ia}(u)p_a\right)\\
 &=J_{ij}(u).
\end{aligned}
$$

Also $\delta(\partial_{l_i})=0$, since none of the resolution differentials contains an $l$-coefficient. Therefore

$$
\boxed{\delta(-\partial_{p_j})
        =\sum_iJ_{ij}(u)\partial_{l_i}},
\qquad
\boxed{d\eta=J_u^{\mathsf T}\beta}.
\tag{13}
$$

The first incorrect transformation is the replacement of this column-of-coefficients calculation by $\sum_iJ_{ji}(u)\beta_i$ in (6.7). Covariance in the second Hom variable does not change differentiation with respect to the source generators. Taking the opposite algebra changes multiplication conventions; it leaves the differential (13) unchanged. Factorials in the dual of polynomial powers likewise do not interchange these indices.

Explicitly, (1) gives

$$
\begin{array}{lll}
dl_1=\theta_1,&dl_2=\theta_2+p_1,&dl_3=\theta_3-p_1+2p_2,\\[2pt]
\delta\eta_1=-\beta_2+\beta_3,&
\delta\eta_2=-2\beta_3,&\delta\eta_3=0,
\end{array}
$$

where the last line describes the actual derivative images. The paper instead gives

$$
d_{\mathrm{bad}}\eta_1=0,\qquad
d_{\mathrm{bad}}\eta_2=-\beta_1,\qquad
d_{\mathrm{bad}}\eta_3=\beta_1-2\beta_2.
$$

In particular the first generator is declared closed while its image has value $-1$ on $l_2$ after differentiation. Reversing its sign changes that value to $1$, still not zero.

The second explicit conversion is at [lines 3225–3228](../paper/paper.tex#L3225): after shear, the displayed equation is claimed to be the $u^{-1}$-fixed-vector equation on $E_+$, then converted to the $u$-equation by multiplication by $-\operatorname{Ad}(u)$. Expand the invariant trace pairing. For

$$
Z=\begin{pmatrix}a&b\\b&c\end{pmatrix},\qquad
\operatorname{Tr}(XZ)=x_1a+2x_2b+x_3c,
$$

the paired coordinates are $\beta=(a,2b,c)^{\mathsf T}$. With $R=\rho_W(u_0)=I+J$, the positive representation in these coordinates is

$$
P=\rho_+(u_0)=R^{-\mathsf T}
 =\begin{pmatrix}1&1&1\\0&1&2\\0&0&1\end{pmatrix}.
$$

The correct conversion, with every matrix in the actual paired coordinates, is

$$
(\rho_+(u_0^{-1})-I)\beta
 =(R^{\mathsf T}-I)\beta
 =J^{\mathsf T}\beta
 =\begin{pmatrix}-2b+c\\-2c\\0\end{pmatrix},
$$

$$
-PJ^{\mathsf T}\beta
 =(P-I)\beta
 =\begin{pmatrix}2b+c\\2c\\0\end{pmatrix}.
\tag{14}
$$

Direct $2\times2$ multiplication confirms the endpoint:

$$
gZg^{\mathsf T}-Z
 =\begin{pmatrix}2b+c&c\\c&0\end{pmatrix}.
$$

In contrast, the manuscript starts with

$$
J\beta=\begin{pmatrix}0\\-a\\a-4b\end{pmatrix},
\qquad
-PJ\beta=\begin{pmatrix}4b\\-a+8b\\-a+4b\end{pmatrix}.
\tag{15}
$$

Already the first equality identifying $J\beta$ with the inverse fixed-vector equation is wrong. The permitted invertible multiplication cannot change its zero locus. The true equations (14) are $b=c=0$; the bad equations (15) are $a=b=0$.

Two concrete points verify both directions of the discrepancy:

$$
Z_{\mathrm{true}}=\operatorname{diag}(1,0),\qquad
Z_{\mathrm{false}}=\operatorname{diag}(0,1).
$$

The first is fixed by $gZg^{\mathsf T}$, while $J(1,0,0)^{\mathsf T}=(0,-1,1)^{\mathsf T}\ne0$. The second satisfies $J(0,0,1)^{\mathsf T}=0$, while

$$
gZ_{\mathrm{false}}g^{\mathsf T}
 =\begin{pmatrix}1&1\\1&1\end{pmatrix}
 \ne Z_{\mathrm{false}}.
$$

Both vectors have rank one and lie in the boundary relevant to the downstream argument. Since $\operatorname{Ad}(t)$ acts by $r$ on $E_+$, the first also satisfies the exact scaled equation $\operatorname{Ad}(tu_0)e=re$; the second does not. The invariant central correction has trivial adjoint action and does not alter this calculation.

These calculations audit transformations expressly performed in the proof. They establish a direct CONV error independently of the use of a counterexample as a diagnostic tool. The valid square-zero, degree, and weight checks on the bare algebra, and the valid complete-intersection lemma for the true equation scheme, do not change either failed conversion.

## Final direct labels and downstream effect

**Final direct labels: DEF, CONV.** These agree with the existing [case README](../README.md). No direct label is added or removed. The refinement is the explicit separation of the inherited MP failure at line 3229 from the two direct obligations: constructing the specified equivariant dg action, and correctly computing its differential and fixed-vector equations. The G1 and G2 audits identify no additional direct quantifier-rule failure.

The broken $B^0$-action feeds the flag calculation in Proposition 6.5, the representation-valued reconstruction in Proposition 6.7, and the local realization packaged in [Theorem 6.8](../paper/paper.tex#L3865). That realization is used to construct [the localized sheared object in §7](../paper/paper.tex#L4491) and the [$B$-linear cyclic-support map of Proposition 8.1](../paper/paper.tex#L4705), which carries the same cusp vector into the final boundary tests. The explicit flag failure above verifies this dependence within a concrete local calculation.

The admissible $\operatorname{Sp}_4$ witness settles both direct labels. No mathematical issue needed for this classification remains unresolved.
