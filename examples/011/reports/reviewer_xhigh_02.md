# Independent mathematical audit of e02

**Verdict: ACCEPT.**

I have assessed the entire 66-page paper, including Appendix A, and read all five supplied public references in full. I find the proof of Theorem 1.1 mathematically coherent, including the new geometric bounds, the singular-support construction, the mixed-weight moment argument, the prime-power estimates, and the final interpolation. I found no substantive error requiring rejection. The small points listed below concern an explicit local justification and presentation/source-version alignment; they do not change the theorem or the required estimates.

## Scope and coverage

The permitted inputs used were `blind/e02/paper.pdf`, its accompanying text, and the supplied Bei16, FK01, HY18, RS22 and Xu20 PDFs/texts. The paper was read in bounded page batches covering pp. 1–66, and the references were read completely: Bei16 pp. 1–21; FK01 pp. 1–52, corresponding to printed pp. 115–166; HY18 pp. 1–28; RS22 pp. 1–6; Xu20 pp. 1–34. Critical passages were reread. PDF inspections of paper pp. 28, 36 and 52 resolved notation lost during text extraction. No other version, review, private material, formalization, or internet source was consulted.

This is an assessment of the argument with the ordinary use of its cited literature. The five supplied references were checked directly against their uses. Other cited inputs—particularly Davenport's goodness alternative, Bernert's singular-series theorem, the Pila/Vermeulen point-counting results, the oscillatory-integral estimate from BHB09, the local-solubility result of Pleasants, and the stated delta-method formula—remain external literature inputs. Their precise source texts were outside the permitted material. I found no internal contradiction or demonstrable hypothesis mismatch in their stated applications; their underlying proofs were not independently audited here.

## Points to clarify or correct

1. **Paper p. 56, proof of Lemma 12.5, justification of (12.14): make the local uniform lower-Lipschitz argument explicit.** Smoothness of an inverse map, by itself, is not a sufficient general global argument for the displayed two-point estimate on an arbitrary image domain. Here the desired estimate is available by shrinking the ball $U$, which the setup permits. Let $A_0=D_{y'}\Psi(x_0)$, with $y'=(y_1,\ldots,y_\rho)$. Choose the convex ball $U$ so small that
   \[
   \sup_{y\in U}\|D_{y'}\Psi(y)-A_0\|<\frac{1}{2\|A_0^{-1}\|}.
   \]
   Integration along the segment joining $(s,y'')$ and $(t,y'')$ then proves (12.14), with a uniform constant. This is a routine local clarification, and it supplies exactly what the counting argument on pp. 56–57 needs.

2. **Paper p. 62, Appendix A.2.1, first source citation:** the numbering “Part (2) of Theorem 5.2 and … Theorem 5.3” does not match the supplied HY18 preprint. In that supplied text, the relevant statements are Theorem 5.4 (existence after shrinking), Theorem 5.8 (generic base change), and Theorem 5.9 (agreement with fibre singular supports after shrinking), with introductory counterparts on p. 3. The supplied material supports (A.8), including the use of an excellent Noetherian base such as an open subscheme of Spec Z. Identify the version corresponding to the citation, or give the corresponding preprint numbering. This is a source-version issue, not a missing singular-support theorem.

3. **Paper p. 59, paragraph introducing (A.5), and pp. 60–61:** the supplied RS22 explicitly allows a prime-power coefficient modulus in Theorem 1.2 and Section 2.1. Thus the sentence that RS22 Section 2.1 only explicitly discusses the case of prime coefficients should be corrected or identified as referring to a different version. The extension argument given in the paper is valid, including its surjectivity requirement at the boundary degree and the inverse-limit passage.

4. **Editorial only:** p. 37 has “again let us again”; p. 62 has “and and.” Remove the duplicated words.

Several apparent errors in the extracted text are **not errors in the PDF**. On p. 28 the coefficient in the quadratic identity is the inverse of $2$, written with a bar; on p. 36 the fields in Lemma 9.2 carry the required algebraic-closure bars; on p. 52 both (12.2) and (12.3) already contain absolute values. These should not be reported as mathematical corrections.

## Main logical chain

The contradiction hypothesis $X(\mathbb Q)=\varnothing$ is consistently maintained until the final circle-method argument. It gives goodness and the geometric restrictions used to improve the exponential-sum estimates. The paper then establishes, for ten variables and a fixed localization modulus $W$, the shifted-box estimate
\[
\sum_{q\sim Q}\sum_{\substack{0\ne v\in\mathbb Z^{10}\\|v-v_0|\le L}}
 |S_{q,W}$v$|
 \ll $LQ+|v_0|$^\varepsilon(L+Q^{1/3})^{10}Q^{20/3-\gamma},
 \qquad 0<\gamma<1/96.
\]
The modulus $W$ is fixed before the later analytic epsilon choices. Section 12 combines this saving with local bounds for the gradient map, giving an error $o(P^7)$, while the localized singular series and singular integral produce a positive main term of order $P^7$. The resulting nonzero zero contradicts $X(\mathbb Q)=\varnothing$. Restriction to ten variables then handles all larger numbers of variables.

The following section-by-section record details the checks behind this conclusion.

### Sections 1–2, pp. 1–8

The introduction accurately describes the logical role of the contradiction hypothesis and the separation between cube-free and cubefull moduli. Theorem 1.3 follows from the singular-locus bound proved later in Lemma 3.9. Conjectures 1.2 and 12.6 are not silently assumed in the ten-variable proof: the needed instance of the latter is supplied by Proposition 11.1.

The finite-field point-counting preliminaries are used with their stated singularity conditions. In Lemma 2.6, one can indeed arrange a common integer $C$ as both leading coefficient and degree by clearing denominators, increasing the degrees, and choosing $C$ sufficiently large and divisible. A rationally invertible integral change of variables need not be unimodular for the upper bounds in Lemmas 2.7–2.8: it injects the original lattice set into a bounded enlargement of a suitable congruence box.

In Lemma 2.8, choosing a first nonzero defining polynomial leaves $d+1$ freely chosen coordinates, the admissible squarefree moduli are controlled by the divisor bound, and each remaining coordinate has a bounded number of lifts because $q\gg1+L/m$. The finitely many primes dividing the leading coefficient are correctly absorbed. Proposition 2.9 treats the small-product case by residue classes and the large-product case by the first threshold-crossing modulus; the exponents in (2.3) follow from those counts. The exclusion of the integral exceptional loci supplies the nonzero values needed for the divisor bounds.

Lemma 2.10 is stated in the range subsequently used. Its final frequency cutoff follows from the preceding volume estimate and the bound on the gradient on the fixed enlarged support.

### Section 3, pp. 8–15

I checked the tangent-space identity of Lemma 3.1 and the subsequent rank arguments. The determinant divisibility underlying Lemma 3.4 gives the asserted rank except for the explicitly treated congruence case; the additional linear factor in that case yields a rational kernel vector and the required contradiction. Thus the important bound $r(F)\ge2\lceil n/3\rceil$ is justified.

Lemma 3.6 supplies the semistability statement actually used. Its minimization, comparison of Galois-conjugate flags, and descent of the resulting weight filtration give a rational coordinate system. Nonvanishing of the pure-cube coefficients in such a system under the no-rational-point hypothesis then forces the desired sign of the weight sum.

In Lemma 3.8, $F$ is constant on each irreducible component of a gradient fibre: on that component Euler's identity and differentiation give $3,dF=dF$. Consequently a component paired with itself lies on the extra equation $F(v)=F(w)$, preserving the relevant maximum dimension. This justifies passing to the incidence locus over the cubic hypersurface.

For Lemma 3.9, the two flag constructions and their cubic vanishings give the stated inequalities for the dimension $t$ and Hessian rank $r$. In particular the bounds on the singular incidence locus and the full incidence locus are compatible with all cases and with the small-dimensional alternatives. The resulting bound
\[
\dim\operatorname{Sing}X\le\left\lfloor\frac{2n-6}{3}\right\rfloor
\]
under $X(\mathbb Q)=\varnothing$ yields Theorem 1.3 by taking the contrapositive. The deductions concerning $V_r$, $V_r\cap\widehat X$, and linear spaces in the singular locus in Corollary 3.10 and Lemma 3.11 use the correct affine/projective dimension shifts.

### Section 4, pp. 15–17

The slicing argument in Proposition 4.1 uses rational points of the rational-point closure and generic smoothness to obtain the needed rational tangent subspace. Restricting $F$ to its annihilator preserves the no-rational-point hypothesis; an identically zero restriction would already contradict it. The singular-locus estimates from Section 3 therefore apply to the restricted form.

The conormal interpretation, the dual-dimension relation, and the dimension estimates in Propositions 4.2–4.3 are consistent. Corollary 4.4 correctly specializes them to $n\ge10$, including the exceptional finite set when $n=10$, the empty rational loci in the larger cases, and the dimensions used later for the deepest strata.

### Section 5, pp. 17–22

The conversion of $S_p(v)$ into hyperplane-section point counts has the right factors of $p$ and separate treatment of $v=0$. The possible conical hyperplane sections in Proposition 5.1 are controlled by the bound on $V_2\cap\widehat X$, so that the finite-field estimates apply with the claimed dimensions.

For prime squares, the stationary congruences in Lemma 5.3 have the stated form; the distinction between nonzero $v\bmod p$ and $v\equiv0\bmod p$ gives the claimed powers. The Taylor expansion for $q=A^2T$, the definition of $G_{A,T}$, its translation invariance and multiplicativity, and the quadratic Gauss bound all agree. The Smith-normal-form estimate for $N_d(y)$ is used in a valid upper-bound direction.

The singular-series theorem is explicitly imported as Theorem 5.4, rather than inferred from an insufficient pointwise estimate at zero frequency.

### Section 6, pp. 22–27

The lifting count in Lemma 6.1 distinguishes primitive and imprimitive cases correctly. In Lemma 6.2, the rank-at-least-two quadratic part supplies a nonsingular binary contribution, and the recurrence for the origin gives the stated $(s+1)p^{s(n-1)}$ bound. I checked the rank-dependent functions and their use in Lemma 6.5, including the deepest rank cases.

The transition from the lifting count to Lemma 6.6 keeps both gradient and coordinate gcd factors. In the Poisson-based bound of Lemma 6.7, the use of goodness in (6.12), the incidence sum in (6.13), and the subsequent Cauchy–Schwarz estimate give the asserted modulus exponents. The cube-full summation in Lemma 6.8 yields the stated maximum defining its exponent; for $n=10$ the required value is (2/5), giving the $C^{32/5+\varepsilon}$ average used in Section 11.

### Section 7, pp. 27–32

The local Smith-profile method is valid for both branches of (7.3). For $t>a$, the decomposition $z=v+p^{t-a}x$ removes the cubic dependence on $x$; translation by the quadratic kernel gives the image condition, and Smith normal form gives exactly the displayed number of admissible $v$'s. The odd-prime condition accounts for division by $2$.

The rank bound at infinity in Lemma 7.4 supplies the translated-Hessian count. In Lemma 7.5, elimination in the first $c_{a-2}$ rows and columns leads to a residual rank $c_{a-1}-c_{a-2}$, hence to the bound $c_{a-1}+c_{a-2}$ before applying the translated-Hessian estimate. The exponential-in-valuation constant is tracked explicitly; it is not mistakenly treated as a divisor-type constant at small primes.

For Lemma 7.7 I checked the table and the two cases $c_0\ge4$ and $c_0\le3$. They prove, for every $e\ge1$,
\[
\Phi_{10}$e,e$\le7e-2,\qquad
\Phi_{10}$e,e+1$\le7e-5,\qquad
\Phi_{10}$e+1,e$\le7e+7.
\]
These give the three factors $z_0^{-2},z_1^{-4},z_2^{-1}$ in (7.12). As an additional arithmetic check, I exhaustively evaluated the finite Smith-profile maxima for $1\le e\le6$; all agree with the analytic bounds, including the endpoint $e=1$.

### Section 8, pp. 32–34

A smooth local point can be chosen in the maximal Hessian-rank open locus because the smooth local points are Zariski dense. The fixed local ball and its unit orbit preserve the required homogeneity. The nonzero principal minor gives uniformly bounded fibres in the selected gradient coordinates, leading to the claimed localized pointwise bound.

The coarse residue-class average has exponent $n+(4-\rho)/6$, and specializing \(n=10,\rho\ge8\) gives (28/3), while the pointwise exponent is $7$. These are the two distinct small-prime estimates later used. Absolute convergence and positivity of the restricted singular series are compatible with restriction to the chosen smooth local neighbourhoods. Fixing the exceptional-prime set using a chosen loss parameter removes the earlier dependence on arbitrarily small epsilon.

### Section 9, pp. 35–38

Lemma 9.1 reduces the codimension-two moment to counts on plane slices. Lemma 9.2 proves the needed geometric irreducibility of the generic slice. In its PDF notation $K=\overline{\mathbb Q}(T_3,\ldots,T_n)$, and irreducibility is asserted over \(\overline K\). A geometrically reducible but $K$-irreducible cubic would have three conjugate linear factors; their slopes are constant-field elements and hence fixed by the Galois group. Equality of the slopes contradicts squarefreeness of the leading binary cubic. The exceptional specialization locus is controlled by a nonzero polynomial, so its contribution is of the smaller claimed order.

The FK01 uniform-constructibility theorem applies to the morphism \(\widehat X\times\mathbb A^n\to\mathbb A^n\) and the function $x\cdot v$. Homogeneity gives descent along projectivization, so the subsequent smooth homogeneous refinement in Lemma 9.3 is legitimate and preserves a uniform total-rank bound.

Proposition 9.5 applies the mixed-lisse version of Xu's moment dichotomy to the actual virtual trace realization, not merely to an arbitrary pointwise family. The second-moment alternative has exponent
\[
(n-r-1)+$n+r-2$+1=2n-2.
\]
For degree $d\le r$, the cone is contained in a rational linear space of codimension two. Lemma 9.1 gives exponent (2n-3) there, contradicting that alternative over extensions \(\mathbb F_{p^a}\). This proves the claimed improved trace bound uniformly after finitely many primes are excluded.

### Section 10, pp. 38–48

The construction combines the geometric sandwich and the rational-point closure bound of Appendix A with the deepest-stratum estimates of Section 4. The truncation at $Z_{n-3}=\{0\}$ and the special handling of the last two levels are compatible with the pointwise estimates.

Moving smooth open pieces of low-degree rational components down one trace level is justified by Proposition 9.5. For components not geometrically integral, the rational points lie in the intersection of the geometric conjugates, giving the required dimension drop. The application of affine dimension growth also handles the possible cylinder issue for the homogeneous cones. The resulting point-counting exponents in Lemma 10.1 match the degrees assigned to each level.

The global defining-polynomial factors used in the divisor arguments are nonzero on the selected rational stratum. The local factor $K(d,v)$ tracks only the excess over the globally assigned level. The pointwise and averaged divisor estimates, including the truncated exceptional depths, keep the correct powers for squarefree and square factors.

The small-radical case uses the residue-class count and its $K$-saving; the large-radical case is an application of Proposition 2.9 with the stated dimensions. I checked the combination in Proposition 10.9: it produces the two terms under the minimum and the $2/3,1/3$ interpolated term with powers $D^{13/2}T^{20/3}$. These are precisely the quantities required by Section 11.

### Section 11, pp. 48–52

The decomposition $q=gdr$, the periods for the weight majorants, and the use of $L\le Q^{1/3}$ are consistent. Lemma 11.2 gives the extra $C^{1/12}$ only when the moment exponent is $10$; it does not insert that loss in the moments of orders $1$ and $9$.

The two summed bounds used for the minimum are
\[
Q^{10+\varepsilon}C^\eta D^{-1/6}G^{-2/3},
\qquad
Q^{10-1/6+\varepsilon}G^{1/2}D^{5/2}.
\]
Interpolation with exponents (15/16) and (1/16) cancels $D$ exactly and gives
\[
Q^{10-1/96+\varepsilon}G^{-19/32}C^{15\eta/16}.
\]
The third term, by Hölder, is
\[
Q^{10-1/30+\varepsilon}G^{-3/10}D^{-2/15}C^{2\eta/3}.
\]
I independently recomputed these exponents using exact rational arithmetic. Both yield the required saving after choosing $0<\eta<1/96-\gamma$. The dyadic losses are absorbable, and covering larger frequency boxes gives the full shifted-box statement. The order of choices fixes $W=W_\eta$ independently of the subsequent epsilon.

### Section 12, pp. 52–58

The real localization may be placed at a smooth point where the Hessian has rank \(\rho=r(F)\ge2\lceil n/3\rceil\). The main term uses the localized singular series, the positive real density, and the stated delta-method weight. The decay of the one-dimensional Fourier transform needed in the main-term calculation follows from the nonvanishing selected first derivative.

The gradient-coordinate volume bounds in Lemmas 12.3–12.5 have the required powers of $V,V_0$. Apart from the small local clarification concerning (12.14) recorded above, the supremum over nearby frequencies is controlled correctly. In (12.16), the change of variable involving \(\operatorname{lcm}$q,W$\) makes the gradient-volume parameter common before the modulus average is applied; this avoids an illicit interchange of a modulus-dependent integral supremum.

For $n=10$, Proposition 11.1 supplies Conjecture 12.6 with $b=20/3-\gamma$. Taking $L\asymp R^{1/3}$, the two ranges \(\phi P^3\le1\) and \(\phi P^3>1\) give the claimed saving
\[
\Delta=\min\{\rho/4-3/2,\rho/2-1,2n/3-b\}>0.
\]
The endpoint analysis in $R$ is consistent, and the factor \(\min(1,\phi P^3)\) makes the small-frequency dyadic sum convergent. With \(\rho\ge8\), the analytic loss can be chosen smaller than the fixed positive saving. Thus the error is $o(P^7)$, completing the contradiction. The final restriction argument for $n>10$ is valid, including the harmless case where the restricted form is identically zero.

### Appendix A, pp. 58–64

This appendix supplies the actual stratification used in Section 10. The finite-field trace identity in Lemma A.3 has the correct constant term. The cohomological Gysin criterion gives the required weight bound, with a uniform Betti bound depending on $n,d$. The projectivized singular support has dimension (n-2), so its proper fibre-dimension loci have the codimensions asserted in Lemma A.6.

The use of RS22 in Proposition A.7 has the correct ambient dimension and relative-dimension parameter: the closed immersion has $r=n-2$, and the exceptional fibre threshold (i-1) gives isomorphism for $a>n-2+i$, with surjectivity at equality. The coefficient triangles preserve the needed boundary surjectivity. Finite coefficient groups give the Mittag–Leffler property needed in passing to the l-adic limit.

The supplied HY18 results justify spreading the singular support over an open subset of \(\operatorname{Spec}\mathbb Z\) and comparing its fibres after excluding finitely many primes. The cones and closures constructed over the integers have the asserted generic dimensions. The sandwich \(\Gamma\subset\Sigma\subset S\) follows from ordinary conormal behaviour on the smooth locus and the vanishing of all partial derivatives on the singular locus.

For the stronger rational-point dimension bound, characteristic-zero singular support is Lagrangian, so the components are conormal varieties to subvarieties contained in $X$. Biduality implies that a smooth rational point of a dual variety would give a rational contact linear space inside its original variety, contradicting $X(\mathbb Q)=\varnothing\$. Lemma A.11 supplies the extra codimension for exceptional fibres. The three cases in the final proof, according to the generic fibre dimension relative to (i-1), give \(\dim\overline{Z_i(\mathbb Q)}\le n-i-1\) with the correct projective-to-affine shift.

The bibliography and remaining front matter on pp. 64–66 were read; no inference was drawn from the supplementary formalization link.

## Verification of the five supplied references

- **Bei16:** the dimension theorem, support properties, behaviour under a closed immersion, and characteristic-zero Lagrangian statement support the singular-support construction and conormal decomposition used in Appendix A. The characteristic-zero qualification is present in the supplied source and is respected in the argument.
- **FK01:** Theorem 2.1 provides a fixed algebraic stratification and uniform cohomological-rank bounds as the characteristic and additive character vary. The inputs in Lemma 9.3 match its morphism/function framework. The later homogeneous refinement is supplied by the paper itself.
- **HY18:** the base hypotheses include the excellent Noetherian setting needed here. The existence, generic base-change, and fibre-comparison statements provide (A.8) after shrinking. The only issue found is the preprint/published-version numbering noted above.
- **RS22:** the support-of-the-Gysin-cone argument gives the exact exceptional fibre locus and the degree threshold used in Proposition A.7, for the pushforward from a potentially singular hypersurface. Smoothness of that hypersurface is not an additional missing hypothesis.
- **Xu20:** Theorem 3.5 and its mixed-lisse extension on p. 20 apply to the virtual sum in (9.5). Uniform total rank controls the constant in the pointwise alternative, and the moment alternative is over all finite extensions, exactly as needed in Proposition 9.5.

## Final assessment

Every section and the appendix has been assessed. The principal new estimates fit together with a positive numerical margin, and the supplied sheaf-theoretic references support the two especially sensitive transitions: construction of rationally sparse exceptional strata and conversion of a second moment into an improved pointwise trace bound. The local clarification at (12.14) is immediate within the existing setup. My recommendation is **ACCEPT**, with the minor clarifications and editorial adjustments identified above.
