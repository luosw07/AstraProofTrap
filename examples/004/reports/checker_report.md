VERDICT: OK

The target meets all three requirements: the error holds under the paper's actual coordinates, pairing, and equivariance conventions; it enters the construction of local realization and flag tests; and the local, formally natural change passes degree, weight, rank, and identity-holonomy checks, requiring the augmentation resolution and a nontrivial unipotent stabilizer to expose it. The core error confuses covariance in the coefficient variable with matrix transposition when dualizing linear generators.

## 1. Scope and exact locations

Read all 5,467 lines of submitted `checker-input/paper.tex`, including hypotheses, all local/global arguments, and references, plus `tricker-log.md`, `mutation.json`, and `verification.md`. Only this round's designated input was used: no original, other trials, other agents' reports, or verification program cited by the log was read; no browsing occurred. Independently written exact-rational checks are in `checker-verification.py`, with `checker-verification-results.json`; all 66 assertions passed.

Locations in submitted TeX:

| Location | Actual text and role |
| --- | --- |
| §6.1, lines 3081–3090, (6.2) | Defines the negative-resonance algebra with \(d\theta_\alpha=\langle\alpha,(\operatorname{Ad}(u)-1)N\rangle\). |
| §6.2, lines 3188–3195, (6.6) | Fixes \(J_u=\operatorname{Ad}(u)|_W-1\), \(dp=x,\ dl=\theta-J_up\), explicitly using vector coordinates \(d\theta=J_ux\). |
| **Lines 3204–3207, (6.7)** | Defines \(B^0=A_0\otimes\operatorname{Sym}(W[-1]\oplus W[-2])\) with the erroneous **\(d\eta=J_u\beta\)**. |
| **Lines 3209–3219** | Adds the rationale that covariance retains the same operator and claims a derivative-operator algebra action and quasi-isomorphism to internal derived endomorphisms. |
| **Lines 3224–3229** | Identifies the sheared equations with the fixed equations for \(u^{-1}\) on \(E_+\), hence the true equation algebra of \(Y\). |

These locations implement one mechanism. The preceding augmentation resolution already fixes the need for transposition; the added explanation expressly adopts an incorrect mathematical rule.

## 2. Recalculation from the paper's augmentation resolution

Let \(w_1,\dots,w_n\) be a basis of \(W\), with \(x_i,\theta_i,p_i,l_i\) using the paired \(W^*\)-basis. In components, (6.6) is

\[
d\theta_i=\sum_jJ_{ij}x_j,\qquad dp_i=x_i,
\qquad dl_i=\theta_i-\sum_jJ_{ij}p_j.
\]

The claimed operators on \(K'\) are

\[
\eta_j=-\partial_{p_j},\qquad\beta_i=\partial_{l_i}.
\]

Since \(|\eta_j|=1\), the endomorphism differential is

\[
\delta(\eta_j)=d\eta_j+\eta_jd.
\]

Evaluating on \(l_i\) gives

\[
\delta(\eta_j)(l_i)
=-\partial_{p_j}\left(\theta_i-\sum_aJ_{ia}p_a\right)
=J_{ij}.
\]

It vanishes on other generators, so the actual differential is

\[
\boxed{\delta(\eta_j)=\sum_iJ_{ij}\beta_i},
\qquad \boxed{d\eta=J^{\mathsf t}\beta}
\]

The transpose comes from linearly dualizing resolution generators; covariance of Hom in its second variable does not alter this calculation. Taking the opposite algebra changes multiplication order, not this component identity.

With the fixed columns and paired bases, the two formulas agree exactly when \(J=J^{\mathsf t}\). Using \(+\partial_p\) changes the overall sign but cannot interchange rows and columns. The zero-row/nonzero-column counterexample below excludes all such sign interpretations.

## 3. Concrete data satisfying the local hypotheses

Use \(k=\overline{\mathbb Q}_3\), \(q=5\), \(L=\operatorname{Sp}_4\), and its split dual \(G=\operatorname{SO}_5\). For

\[
\Omega=\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix}
\]

take

\[
e_0=\begin{pmatrix}0&I_2\\0&0\end{pmatrix},\quad
f_0=\begin{pmatrix}0&0\\I_2&0\end{pmatrix},\quad
h=\operatorname{diag}(I_2,-I_2).
\]

Direct multiplication verifies the symplectic Lie condition, \([e_0,f_0]=h\), \([h,e_0]=2e_0\), \([h,f_0]=-2f_0\). Since \(e_0^2=0\) and rank is two, its type is \((2,2)\). The homomorphism and cocharacter are

\[
\phi\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\begin{pmatrix}aI_2&bI_2\\cI_2&dI_2\end{pmatrix},
\qquad m(z)=\operatorname{diag}(zI_2,z^{-1}I_2).
\]

Set \(d=4\cdot3^N\), \(s=25^{3^N}=5^{d/2}\), \(r=s^2\), \(t=m(s)\). These meet the following conditions:

1. **Arthur decomposition and compactness.** In \(t=m(r^{1/2})c\), \(c=1\), so algebraicity and compactness at every complex embedding hold.
2. **Degree and congruence.** The length-zero group of \(G=\operatorname{SO}_5\) has order two, and \(2\mid d\). Since \(v_3(25-1)=1\) and \(v_3(a^2+a+1)=1\) for \(a\equiv1\pmod3\), induction gives \(v_3(s-1)=N+1\). Thus any sufficiently small identity congruence neighborhood used in Lemma 3.1 can be reached.
3. **Full and adjoint centralizers.** Since \(s\ne s^{-1}\),
   \[
   H=Z_L(t)=\{\operatorname{diag}(g,g^{-\mathsf t}):g\in\operatorname{GL}_2\}\simeq\operatorname{GL}_2
   \]
   is connected. Conjugacy of \(t\) and \(-t\) would require \(s^2=-1\), false here. Thus the adjoint centralizer is \(H/\{\pm I\}\), also connected, satisfying the central-torsor conditions used in the paper.
4. **Resonance spaces and open orbit.** \(E_+\) is the upper symmetric \(2\times2\) block and \(W\) the lower symmetric block, of \(m\)-weights \(2,-2\). Actions are \(Y\mapsto gYg^{\mathsf t}\) and \(X\mapsto g^{-\mathsf t}Xg^{-1}\). Symmetric matrices have finitely many rank orbits; the open orbit is invertible matrices. \(e_0\) corresponds to \(I_2\) with reductive stabilizer \(O_2\), whose disconnectedness is permitted.
5. **Neutral and even sectors.** \(Z(L)=\{\pm I_4\}\) and \(m(-1)=-I_4\) act trivially on resonance spaces. Both the \(H/Z(L)\) and even-weight sectors retained in §7 include this example.

Take the nontrivial unipotent element

\[
g=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
u=\operatorname{diag}(g,g^{-\mathsf t})\in H.
\]

Lemma 6.1 (lines 3021–3063) explicitly says allowed saturated slice shrinkings retain the whole unipotent variety: they are neighborhoods of the identity class in the conjugation quotient. This point therefore remains. Central localization in §7 also uses the quotient identity class; §8.1, lines 4753–4756, again allows \(u\) throughout the unipotent variety.

Proposition 6.3 computes the algebra for the entire local category and all coherent inputs; the augmentation object \(A_0\) is an actual input. This example directly tests that local assertion; the truth of the final main theorem is outside the counterexample's conclusion.

## 4. Failures of the chain map, equivariance, and equations

### 4.1 Direct contradiction in the derivative action

Let

\[
X=\begin{pmatrix}x_1&x_2\\x_2&x_3\end{pmatrix}.
\]

Independent conjugation gives

\[
g^{-\mathsf t}Xg^{-1}
=\begin{pmatrix}x_1&x_2-x_1\\x_2-x_1&x_3-2x_2+x_1\end{pmatrix},
\quad
J=\begin{pmatrix}0&0&0\\-1&0&0\\1&-2&0\end{pmatrix}.
\]

The actual resolution has

\[
dl_1=\theta_1,\quad dl_2=\theta_2+p_1,
\quad dl_3=\theta_3-p_1+2p_2.
\]

and endomorphism differential

\[
\delta\eta_1=-\beta_2+\beta_3,\quad
\delta\eta_2=-2\beta_3,\quad\delta\eta_3=0.
\]

The modified paper instead specifies

\[
d_{\rm bad}\eta_1=0,\quad
d_{\rm bad}\eta_2=-\beta_1,\quad
d_{\rm bad}\eta_3=\beta_1-2\beta_2.
\]

In particular, it declares \(\eta_1\) closed, while its claimed image satisfies \(\delta(-\partial_{p_1})(l_2)=-1\). The action and quasi-isomorphism construction at lines 3212–3219 fail. The bad formula alone still has \(d^2=0\) and correct degrees and weights, so coarse dg checks miss it.

### 4.2 Stabilizer obstruction excludes a coordinate explanation

The stabilizer of \(u\in U_H\) contains \(u\) itself. Both \(\eta,\beta\) are specified as \(W\)-generators, so

\[
u\beta_1=\beta_1-\beta_2+\beta_3,\quad
u\beta_2=\beta_2-2\beta_3,\quad
u\beta_3=\beta_3.
\]

The sheared bad algebra's derived fiber at this point has zeroth cohomology

\[
k[\beta_1,\beta_2,\beta_3]/(\beta_1,\beta_2).
\]

The boundary ideal \((\beta_1,\beta_2)\) is unstable since \(u\beta_2=\beta_2-2\beta_3\). Thus the differential fails even stabilizer equivariance. The correct ideal \((\beta_2,\beta_3)\) is stable.

Equivalently, for \(R=I+J\) on \(W\), the bad formula corresponds on basis vectors to differential \(J^{\mathsf t}\), with defect

\[
R J^{\mathsf t}-J^{\mathsf t}R
=\begin{pmatrix}-2&2&0\\2&-3&-1\\0&-1&5\end{pmatrix}\ne0.
\]

Changing basis, pairing, and action together preserves whether a map is equivariant. This failure therefore cannot be repaired merely by renaming generators or switching to row vectors.

### 4.3 True fixed points lost, nonfixed points admitted

Use the permitted \(L\)-invariant trace pairing to identify \(W^*=E_+\). For

\[
Y_+=\begin{pmatrix}a&b\\b&c\end{pmatrix},
\]

the pairing is \(x_1a+2x_2b+x_3c\), so \(\beta=(a,2b,c)^{\mathsf t}\). The true equation is

\[
gY_+g^{\mathsf t}-Y_+
=\begin{pmatrix}2b+c&c\\c&0\end{pmatrix}=0,
\]

equivalent to \(b=c=0\). Correct \(J^{\mathsf t}\beta=0\) gives this; bad \(J\beta=0\) gives \(a=b=0\).

- \(Y_+=\operatorname{diag}(1,0)\) is truly fixed and satisfies \(\operatorname{Ad}(tu)e=re\), but is excluded by the bad equations.
- \(Y_+=\operatorname{diag}(0,1)\) satisfies the bad equations, while \(gY_+g^{\mathsf t}=\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)\ne Y_+\), so is not a point of \(Y\).

Both lie on the rank-one boundary. In paired coordinates, \(\rho_+(u^{-1})=\rho_W(u)^{\mathsf t}\), explaining why transposition supplies the \(u^{-1}\) equation needed at line 3225. Multiplying equations by invertible \(-\operatorname{Ad}(u)\) preserves zero sets and cannot turn the wrong line into the true fixed line.

## 5. Additional independent check of the downstream flag calculation

Beyond the appendix, I checked a concrete flag component. Define a Borel \(\mathcal B\) by positive root directions for

\[
\lambda(z)=\operatorname{diag}(z^2,z^{-1},z^{-2},z).
\]

Its weights on the three symmetric \(W\)-basis vectors are \(-4,-1,2\), hence

\[
W_{\mathcal B}=W\cap\mathfrak n_{\mathcal B}=k w_3.
\]

All nonzero entries of \(u-I\) have positive weight \(3\), so \(u\in\mathcal B\cap H\). Since \(J|_{W_{\mathcal B}}=0\), the small flag-dual algebra \(B^0_{\mathcal B}\) has \(d\eta_3=0\). Proposition 6.5 (lines 3472–3479) uses the inclusion \(W_{\mathcal B}\subset W\) to give

\[
B^0_{\mathcal B}\longrightarrow(B^0)_{U_b}.
\]

But the bad large algebra has \(d\eta_3=\beta_1-2\beta_2\ne0\). The claimed dg algebra map fails, and the specified derived scalar extension cannot be performed. This directly shows propagation into an actual downstream calculation.

Line 3548 still says “induced differential is the transpose equation.” It refers to the same \(B^0\) and scalar-extension calculation, without redefining the differential or constructing a corrected map. The concrete flag above shows its conflict with (6.7); it indicates a repair direction but does not implement one.

## 6. Exclusions and downstream dependencies

No condition in the paper excludes this example or replaces the bad differential:

- \(H\) is required to be connected, not a torus; §§3 and 6 allow this \(\operatorname{GL}_2\).
- \(u\) need not be semisimple or equal \(1\). Slices, central localization, and §8.1 retain unipotent points.
- Central correction \(s=z^{-1}tu\) is trivial in the adjoint representation and leaves resonance equations unchanged.
- The invariant form pairs \(W\) with \(E_+\); no fixed self-dual identification of \(W\) retaining its action is supplied.
- Shearing only reorders degrees; even weights preserve signs and cannot alter the differential coefficients.
- §6.4 allows a final spherical ring isomorphism to change some vector coordinates, but still requires \(H\)-equivariance over \(U_H\), which cannot rescue a nonequivariant input algebra.

Actual dependencies:

| Downstream location | Affected step |
| --- | --- |
| Proposition 6.3, lines 3212–3229 onward | Specified \(B^0\)-module action on \(G_0\) and realization in \(\operatorname{Coh}^H(Y)\); later unit and reconstruction comparisons use the same (6.7). |
| Proposition 6.5, from line 3463 | Flag-dual algebra inclusion, scalar extension, and specified \(B^0\)-module structure; Section 5 above supplies a component counterexample. |
| Proposition 6.7, from line 3692 | Spherical internal endomorphism algebra, representation-valued operations, and \(\mathcal O(Y)\)-action reconstruction call on \(G_0\) and flag calculations. |
| Theorem 6.8, from line 3865 | Packages these into equivariant coherent realization and test objects usable globally. |
| §7, from line 4491 | Forms \(F^{\mathrm{ind}}\), the spherical summand, and simultaneous lower-bound comparison using this realization. |
| Proposition 8.1, from line 4705, especially 4746–4749, 4810–4818, 4831–4844 | Uses the internal ring isomorphism to connect true scaled-equation cyclic support with coherent module actions and construct a \(B\)-linear map and section carrying \(f\). |
| §§8.3–8.4 | Final vanishing/nonvanishing requires the same test and \(B\)-module section on both sides, relying on the failed construction. |

Necessary algebras and maps are therefore broken, as witnessed by a concrete action, flag, and points. The error is substantive.

## 7. Subtlety

The change is confined to three passages in one proposition's proof: a transpose symbol, a covariance explanation, and a later equation description. Generators, degrees, weights, categorical target, theorem numbering, and structure remain; net growth is two lines and 81 bytes.

The confusion is natural because covariant Hom, opposite algebras, linear duality, and shearing occur consecutively. Common checks miss it: \(J=0\) at \(u=1\); \(J\) is diagonal for tori in weight bases; transposition preserves rank, determinant, and characteristic polynomial; the bad differential still squares to zero with correct degrees. Even on this unipotent fiber, abstract Koszul cohomology has the same shape on both sides: one polynomial and one exterior direction.

The distinguishing data are the specified derivative operators, paired generators, stabilizer representations, and points at fixed holonomy. Repair is quick once (6.7) is located, but confirming the error and its downstream role requires following these structures, meeting the round's small, natural, subtle-change requirements.

## 8. Nontarget changes and appendix verification

Independent calculations confirm the core claims in `verification.md` about the triple, resonance operator, congruence, derivative differential, stabilizer ideal, and two fixed-point certificates. My program derives the three-dimensional matrix from four-dimensional conjugation and the derivative differential from the \(p_j\)-coefficients in \(dl_i\), adding the flag-inclusion counterexample above. It does not use the appendix's claimed 58 results as evidence.

Each of the three declared replacement strings occurs once.

`5f336fbfcbaae27332f37dc51ecbbb3fbe7fd45ceb28d42ec57294fcbbf22dd`,

matching the restored-baseline fingerprint in the log; both figure fingerprints also match the manifest. Current lines 349 and 4883 say bad flags “avoid the open orbit,” consistent with the claimed restoration. **No additional nontarget change was detected within the allowed material.** This scope audit uses the log's baseline fingerprint without reading or independently authenticating the original.

## 9. Required repair

Restore \(d\eta=J_u^{\mathsf t}\beta\) in (6.7), remove or correct “covariance retains the same operator,” and explicitly restore “transpose equation” at line 3225. This realigns derivative actions, paired \(u^{-1}\) equations, stabilizer equivariance, and flag-algebra inclusions. The paper remains unmodified; this report delivers only verification and computation files.
