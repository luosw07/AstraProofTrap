# Independent review of e02

**Verdict: ACCEPT.**

I find the argument mathematically coherent and the claimed ten-variable result supported by the manuscript, subject to the ordinary use of its explicitly cited literature inputs. I found no substantive error requiring a new estimate or a new geometric idea. There are several useful clarifications and a citation-version issue, specified below. The literature dependencies whose original sources were not supplied are identified separately rather than counted as established source checks.

## Scope and coverage

I read the complete manuscript, pages 1–66, including all of Sections 1–12, Appendix A, the references, and the final address page. The supplied text was read in the following bounded, untruncated intervals: lines 1–100, 101–520, 521–940, 941–1360, 1361–1800, 1801–2240, 2241–2680, 2681–3120, 3121–3540, and 3541–3857. There are 66 nonempty form-feed-separated pages. I additionally inspected rendered PDF pages 28, 36, and 62 to check mathematical notation that the text extraction obscures. In particular, the symbol preceding the quadratic form identity on page 28 is the inverse of 2, not an erroneous factor 2, and the algebraic closures in Lemma 9.2 are correctly present in the PDF.

The only substantive inputs consulted were this manuscript and the five references supplied in its supplement: Bei16, FK01, HY18, RS22, and Xu20. I read RS22 in full and the relevant statements, hypotheses, and supporting arguments in the other four references. I used no internet, other manuscript version, other review, formalization, or external model. Small computations in my own scratch directory independently check rational exponents and finite cases of the Smith-profile optimization; they supplement the all-parameter mathematical arguments.

## Assessment of the proof

### Sections 1–2: setup, preliminary geometry, and sieves

The contradiction strategy is logically appropriate: assume that the cubic has no rational point, derive geometric restrictions, and prove that a localized counting function has a positive asymptotic main term. The eventual specialization from more than ten variables to ten variables is valid, with an identically zero specialization giving an immediate zero.

The normalization and congruence-counting arguments in Lemmas 2.6–2.8 work uniformly in translated boxes and residue classes. In Lemma 2.8 the decisive step is selecting a nonvanishing normalization equation, applying the divisor bound to its value, and using squarefreeness and coprimality with the ambient congruence modulus to bound the other coordinates. The fixed leading coefficient only contributes a bounded exceptional-prime factor. Replacing the variety by a larger normalized locus is legitimate because the intermediate admissibility count is monotone.

Proposition 2.9 correctly separates the small-product case from the first modulus that makes the product exceed the box scale. Its second-case exponent is

\[
(L/m)^{d_j+1}\prod_{i>j}R_i^{d_i-d_j},
\]

as required. Fibers at the finitely many primes of dimension jump can be absorbed into constants; the generic dimension hypothesis is adequate. The oscillatory-integral input is explicitly attributed to BHB09 and is used later in precisely the gradient-volume form recorded here.

### Section 3: the main geometric innovation

Lemma 3.1 is a correct tangent-space consequence of the determinantal minors, including the reduced-scheme convention. Lemma 3.4 handles the potentially delicate congruence class n = 1 modulo 3: if the Hessian determinant has an additional linear factor, its rational hyperplane produces a kernel vector in the same hyperplane, and Lemma 3.1 forces a rational zero. The caution in Remark 3.5 about the general statement in Zak is appropriate; only a principal prime in a polynomial ring is used.

The elementary descent proof of Lemma 3.6 is sound. The finite collection of closed weight polyhedra has a minimum-norm point. The Bruhat comparison, followed by the parallelogram identity, forces the optimal weighted flag to be Galois invariant. A rational splitting then reduces the assertion to the nonvanishing of the coefficients of the pure cubes. This supplies the semistability consequence directly, without making the main result depend on a black-box rational Hilbert–Mumford argument.

Lemma 3.8 correctly concentrates the largest incidence dimension over the cubic: on each irreducible component of a gradient fiber, Euler's identity gives 3 dF = dF, so F is constant in characteristic zero. The equal-value locus in the fiber product consequently retains the largest fiber dimension.

I checked the two weight assignments in Lemma 3.9. For the singular case the weights (-4,-1,0,2) give t <= 2r-3 in addition to t <= n-r. For the nonsingular case the weights (-2,0,1,4) give

\[
0\le -3+a-3t+4r,
\]

where a = dim(T intersect L). The inequalities a <= t-1 and a <= n-r yield both stated bounds. Their interpolation gives (3.6)–(3.8), including the origin contribution. Corollary 3.10 and the linear-singular-space bound in Lemma 3.11 follow correctly. These are substantial parts of the proof, and I found no gap in their descent or dimension arguments.

### Section 4: singular hyperplane sections

The incidence correspondence and upper semicontinuity assertions are appropriate. In Proposition 4.1 one must choose a component dominating the chosen smooth parameter component with maximal generic fiber dimension; the construction as written permits this. Differentiating the incidence equation gives the required orthogonality when the chosen component meets the smooth locus. If it lies in the singular locus, equality of dimensions forces a product component, giving the same conclusion. A rational parameter then permits application of Lemma 3.9 to the restricted cubic.

The use of conormal fibers in Proposition 4.3 correctly separates the general fiber from genuine jumps. The treatment of components entirely inside Sing X uses Lemma 3.11 to rule out a linear cone of the forbidden dimension. The resulting bounds in Corollary 4.4 have the correct rounding, in particular the finite set of rational directions for n = 10 and its emptiness in the stated larger dimensions.

### Section 5: prime, prime-square, and lifting bounds

The identities relating prime sums to projective point counts have the correct powers of p. Lemma 5.2 gives the required control of a hyperplane section that is a cone: its vertex lies in the rank-at-most-two Hessian locus, so its projective dimension is at most one. This makes the nonconical-base point-count estimate applicable.

For prime squares, stationary congruences give the prefactor p^(n+1), and the remaining scalar/projective conversion contributes p-1. Thus the exponents in (5.9) and (5.10) agree with the dimensions of the corresponding singular loci, including the case p divides v.

The definitions and proofs of Lemmas 5.5–5.7 correctly retain the maximum over linear terms. In particular, translating the cubic-plus-quadratic phase establishes the claimed gcd(A,T)-periodicity. The lifting derivation of (5.14) uses M = AT, M squared divisible by q, and the unit-fiber bound phi(AT)/phi(A) <= T correctly. The quadratic Gauss estimate then has the stated normalization. Absolute convergence and positivity of the unrestricted singular series are an explicitly cited Bernert input; see the dependency list below.

### Sections 6–7: averaged lifting and Smith profiles

The treatment of smooth, zero, and nonzero singular residue classes in Lemma 6.1 is consistent with the claimed gcd losses. The binary induction in Lemma 6.2 gives the factor s+1. Lemma 6.3 correctly uses the singular-locus dimension to avoid a gratuitous p-factor in the high-rank range.

I checked the exponents in Lemmas 6.5–6.8. The Poisson estimate in Lemma 6.7 uses goodness to control the remaining Hessian-kernel count and the incidence bound for its finite-field factor. Its V >= r^(1/3) threshold is exactly what removes the factor (1+r/V^3)^(n/2). The cubefull Euler product has the three relevant convergence constraints 1/4, (a_n+1)/3, and (b_n+1)/5. In ten variables this yields theta_10 = 2/5 and the total exponent 32/5.

Lemma 7.2's t>a argument correctly counts the admissible linear classes after the cubic term becomes constant on the finer cosets. The kernel-image orthogonality uses symmetry, and odd characteristic is properly imposed. The inverse-of-two notation on page 28 is correct. Lemma 7.5's block elimination has sufficient valuation because the old invariant exponents are at most a-2; the new bottom-right rank condition implies the ambient rank bound used in Lemma 7.4.

The all-e argument in Lemma 7.7 is valid. I also independently enumerated the monotone Smith profiles for e=1 through 6 in each of its three cases, obtaining maxima at or below 7e-2, 7e-5, and 7e+7, respectively. No numerical repair is needed. The distinction between exponential dependence on Omega(q) and on omega(q) is handled by the subsequent localization rather than being silently absorbed into q^epsilon.

### Section 8: small-prime localization

The unit orbit of the chosen p-adic neighborhood preserves the smoothness and Hessian-minor conditions and supplies exactly the scalar invariance needed for multiplicativity. Bounded valuation of a fixed nonsingular minor gives a uniformly bounded number of solutions in those coordinates, once the others are fixed. The constants may depend on the fixed prime, which is sufficient.

The localized density identity in Lemma 8.3 has the correct lcm normalization; its partial Euler factor equals the normalized number of solutions in the allowed classes. Smooth local solutions give positivity. Lemma 8.4 uses t <= a, so it legitimately includes p = 2. In ten variables r(F) >= 8 gives the g^(28/3) residue-class maximum sum and the g^7 pointwise bound used later.

### Section 9: second moments and degree restrictions

The Parseval calculation in Lemma 9.1 yields q^(n-2) times the sum of squared errors in binary fibers. The bad-specialization contribution and the good-fiber Lang–Weil contribution both have order q^(2n-3).

Lemma 9.2 is correct with the algebraic closures displayed in the PDF. Reducibility over the algebraic closure of the rational-function field would force three conjugate linear factors. Their leading slopes already lie in the constant algebraically closed field, so conjugacy forces equal slopes, contradicting squarefreeness of the anisotropic binary cubic.

FK01 supplies the required uniform constructibility and rank bounds; homogeneity permits a homogeneous refinement. Xu20 explicitly extends its virtual-trace-function dichotomy to mixed lisse sheaves on a normal variety, so its use here with alternating cohomology traces is justified. In Proposition 9.5 the heavy-weight alternative has normalized second moment exponent

\[
(n-r-1)+(n+r-2)+1=2n-2.
\]

A degree at most r forces containment in a rational codimension-two linear space, whose second moment has only exponent 2n-3. This is a valid contradiction, uniform for all sufficiently large p.

### Section 10: hybrid stratification and the geometric sieve

Appendix A supplies the geometric codimension gain for rational points, and Section 9 supplies the extra degree information. The reassignment of U_j to the preceding level gives a genuine partition and preserves the claimed pointwise prime bounds. The construction of the integer obstruction Delta(v) properly removes the finitely many bad reductions and the relevant closed complement.

The counts in Proposition 10.1 distinguish degree, field of definition, and dimension correctly. An irreducible affine cone of degree at least four cannot be cylindrical over a curve: its image under the defining linear projection would be a homogeneous irreducible curve, hence a line. The application to shifted congruence boxes uses coefficient-uniform counting results, an important cited dependency listed below.

I checked the divisor-bound averaging in Lemma 10.5, including the different power contributed by primes and prime squares. The K-dependent factors cancel in the subsequent interpolation. Lemma 10.7 has the needed stronger contribution at the final two strata; for (j,k)=(0,0), alpha_10=1/2 makes all remaining modulus exponents at most -1. Lemma 10.8 uses Proposition 2.9 only on points outside the deeper strata, as required, and its three cases give precisely the displayed sum.

The compression in Proposition 10.9 is valid. In the main part the interpolation weights 2/3 and 1/3 cancel K_0 and produce T^(20/3). In the exceptional part both the geometric count and the pointwise divisor-count estimate are available, allowing their minimum.

### Section 11: the decisive exponent saving

The decomposition into a fixed-prime part, cube-free part, and cubefull part is compatible with both the modulus of localization and the residue-class norms. Lemma 11.2's Euler product converges under exactly the stated threshold.

I independently checked the rational arithmetic in the final interpolation. The two exceptional estimates become

\[
Q^{10+\epsilon}C^\eta D^{-1/6}G^{-2/3},\qquad
Q^{10-1/6+\epsilon}G^{1/2}D^{5/2}.
\]

Taking powers 15/16 and 1/16 cancels D and gives

\[
Q^{10-1/96+\epsilon}G^{-19/32}C^{15\eta/16}.
\]

The Holder estimate for the main part gives

\[
Q^{10-1/30+\epsilon}G^{-3/10}D^{-2/15}C^{2\eta/3}.
\]

Both save more than the chosen gamma after fixing eta. The order of choices is correct: W depends on F and gamma but not on the later epsilon. Covering a larger box gives (11.1) with the stated uniformity in its center.

### Section 12: completion by the circle method

The local and real restrictions remain fixed as P grows. Poisson summation has the correct lcm(q,W) frequency denominator and prefactor. The zero-frequency term converges to the positive product of the localized singular series and singular integral. Absolute convergence, rather than an unstated rate for its tail, is sufficient for Lemma 12.2.

The gradient-volume estimates exploit a nonsingular principal Hessian minor of rank rho; they do not require a fully nonsingular Hessian. Lemma 12.5 retains this rank gain while summing supremums over neighboring frequencies. The shifted-box averaging in (12.16) then fits Proposition 11.1.

The optimization in Proposition 12.7 has the correct breakpoints R approximately 1, P, and P^(3/2). The resulting saving is

\[
\min\{\rho/4-3/2,\rho/2-1,2n/3-b\}.
\]

For n=10, rho>=8 and b=20/3-gamma make this positive. The factor min(1,phi P^3) controls the arbitrarily small dyadic theta intervals, so the final dyadic summation is legitimate. The contradiction and the extension to n>10 follow.

### Appendix A: the singular-support input

This appendix supplies a crucial arithmetic improvement and deserves explicit scrutiny. The projective point-count identity in Lemma A.3, the Tate twist, and the Gysin cohomological degrees are consistent. RS22's construction takes the projectivized singular support itself, so its exceptional locus is the manuscript's fiber-dimension locus, not merely some unrelated locus of the same dimension. With ambient projective dimension n-1 and r=n-2, its threshold is a>n-2+i, precisely Proposition A.7.

Lemma A.8 correctly propagates the isomorphism and the boundary surjectivity through coefficient exact sequences. Finite cohomology groups provide the needed Mittag–Leffler condition for inverse limits. This gives the rational-coefficient estimate without assuming equality of singular supports for different coefficient rings.

HY18 supplies specialization of relative singular support after shrinking the excellent base Spec Z[1/N]. Combined with Bei16's compatibility with extension of the ground field, this gives (A.8) for geometric fibers. The resulting projective fiber loci and their affine cones have the required codimensions. The conormal comparison Gamma subset Sigma subset S is correct on both the smooth and singular loci.

In characteristic zero, Bei16's Lagrangian property and generic smoothness identify components with closures of conormal bundles. The use of components integral over Q avoids a Galois-descent defect in the rational-point argument. Biduality shows that a rational smooth point on the dual produces a rational linear space in the original variety. The three cases in Proposition A.13 are exhaustive: a larger generic fiber gives the codimension directly, a genuine jump gives the extra codimension by Lemma A.11, and equality gives it through the singular locus of the dual. This proves the needed gain by one in the closure of the rational points.

## Corrections and clarifications

1. **Page 62, A.2.1, HY18 citation version.** The supplied HY18 text is arXiv:1702.06752v1. Its relative-support existence is Theorem 5.3 in projective space, or Theorem 5.4 generally; its fiber-specialization statement is Theorem 5.8. It does not have the manuscript's cited “part (2) of Theorem 5.2” in that numbering. Theorem 5.8 supplies exactly the mathematical input needed. Reconcile the numbering with the final published version or identify the preprint theorem explicitly. Also delete the duplicated “and.” This is a citation repair, not a missing theorem.

2. **Pages 52 and 56, choice of U and (12.14).** A smooth inverse on a general nonconvex image does not alone give a global Euclidean lower-Lipschitz estimate for every pair in the domain. In this local setting the desired estimate is available: shrink the original ball U so that the derivative of the map y -> (Psi(y),y'') stays sufficiently close to its invertible value at x_0. Integrating along line segments in the ball then gives a uniform lower-Lipschitz bound, and hence (12.14) for equal y''. State this shrinking explicitly. This fills a short local-calculus justification and leaves all subsequent estimates unchanged.

3. **Pages 36–37, Lemma 9.3.** Expand the sentence that the cohomology sheaves factor through projectivization. The change of variables (x,v) -> (lambda^(-1)x,lambda v) preserves the incidence family and the phase, gives a compatible G_m-equivariant structure, and hence descent along A^n minus {0} -> P^(n-1). This justifies lissity on scalar saturations uniformly after spreading out. The intended argument is valid; one or two sentences would make it self-contained at the level of the surrounding proof. Delete “again let us again.”

4. **Page 40, Proposition 10.1(ii).** Make the affine change v=b+mz explicit when invoking the uniform Pila and Vermeulen results. The new varieties retain dimension, degree, geometric integrality, and the noncylindrical property, and the translated box is reduced to scale O(1+L/m). The essential point is that the cited constants are uniform in coefficients, not merely in a fixed original variety. This is already the intended use of the cited uniform estimates.

5. **Page 59, discussion of RS22 coefficients.** The supplied RS22 version already states its setup for Z/ell Z with ell a prime power. The manuscript's remark that only the first-power case is explicit should be reconciled with the version cited. The separate coefficient argument in Lemma A.8 is correct and can remain.

These points are local repairs or expository clarifications. None changes the claimed exponent or requires replacing a central argument.

## Supplied-source checks and remaining literature dependencies

The five supplied sources substantiate the delicate sheaf-theoretic inputs:

- **Bei16:** Theorem 1.3 gives existence and pure-dimensionality; Theorem 1.4(iii) gives field-extension compatibility; Lemma 2.3(iii) identifies the base with support; Lemma 2.5(ii) gives the closed-immersion conormal calculation. The characteristic-zero remark after Theorem 1.3, with its explanation, supports the Lagrangian step.
- **HY18:** In the supplied preprint, Theorems 5.3/5.4 and 5.8 give relative existence and generic fiber compatibility over the required excellent base. The hypotheses do not restrict this step to a base over a field of positive characteristic.
- **RS22:** Theorems 1.2 and 2.2, Corollary 2.3, and their proofs supply both the Gysin range and the identification of the relevant exceptional loci.
- **FK01:** Theorem 2.1 applies to the family X-hat times A^n -> A^n, with phase x dot v and constant input coefficients. It supplies one finite stratification and a uniform bound on the total ranks as p and the additive character vary.
- **Xu20:** Theorem 3.5 and Remark 3.6 give the required dichotomy for virtual mixed lisse trace functions. The manuscript's moment exponent and use over all finite extensions are correct.

Several other cited works were not among the authorized supplied references, and their original statements were therefore not independently inspected in this review. The most consequential dependencies are: Davenport's goodness implication; the cubic point-count estimates in Lemma 2.1 and Zak's hyperplane-section bound; Bernert's absolute convergence and positivity result for good ten-variable cubics; the smooth p-adic zero theorem; the uniform Pila and Vermeulen integral-point bounds; the BHB09 oscillatory-integral estimate; and the MV19 form of the smooth delta method. Classical biduality, the low-degree linear-span bound, standard spreading-out results, and Deligne/Katz weight and Betti bounds are also cited. The applications in this manuscript have matching parameters and plausible stated hypotheses, and I found no internal conflict with them. These remain source-verification dependencies, distinct from an identified mathematical gap.

The full argument reaches the required contradiction, including its appendix input and its small-prime treatment. My recommendation is acceptance with the local clarifications above.
