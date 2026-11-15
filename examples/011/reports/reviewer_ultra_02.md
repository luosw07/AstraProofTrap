# Independent review of e02

**Verdict: ACCEPT.**

I read the complete 66-page manuscript, including all of Appendix A. I found no substantive mathematical error in its proof of Theorem 1.1. The new geometric estimates, the stratified sieve, the two cubefull estimates, their interpolation with the cube-free estimates, and the final circle-method argument fit together with the stated quantitative savings. The five supplied public references support the delicate sheaf-theoretic steps for which they are used.

This verdict uses the ordinary convention that established, correctly stated results cited from the literature may serve as inputs. The precise scope of my source verification is recorded below, including dependencies whose original articles were not supplied.

## Scope and coverage

The only scientific inputs consulted were `blind/e02/paper.pdf`, `blind/e02/paper.txt`, and Bei16, FK01, HY18, RS22, and Xu20 in `blind/e02/supplement`. I did not consult other manuscripts, reviews, private material, external services, agents, or formalizations.

I read paper.txt lines 1–3857 in nine bounded, untruncated chunks: 1–420, 421–840, 841–1260, 1261–1680, 1681–2100, 2101–2520, 2521–2940, 2941–3360, and 3361–3857. These cover pages 1–66 consecutively. I also inspected rendered PDF page 28 to distinguish a modular inverse from an extraction artifact.

The following is a mathematical assessment of the complete argument, rather than an assessment limited to the introduction or principal theorem statements.

## Main findings

### Geometry: §§2–4, pages 5–17

The uniformity in translated congruence boxes in Lemmas 2.6–2.8 is important and is preserved by the stated integral linear change of coordinates. In Lemma 2.8 the nonvanishing polynomial value bounds the number of available square-free divisors, while the remaining coordinates have boundedly many lifts because the sieving modulus exceeds the box length divided by the existing congruence modulus. Proposition 2.9 then correctly separates the case of a small product of sieving moduli from the first crossing of that scale. Its exponents agree with the number of residue classes and with the large-modulus estimate.

I checked the novel argument in Lemma 3.6 in detail. The minimal Euclidean-norm weight exists because only finitely many monomial supports occur and each feasible weight set is closed. The Bruhat decomposition aligns two weighted flags without introducing negative-weight monomials. For a minimizing weight and its Galois conjugate, equality in the norm comparison forces preservation of the weight vector; this gives a Galois-stable filtration. Splitting that filtration over Q reduces to the rational-coordinate case, where every pure cube coefficient is nonzero. This establishes the semistability consequence needed later without having to assume the desired rational Hilbert–Mumford conclusion.

Lemma 3.8 correctly reduces the maximal incidence dimension to points on the cubic. On each irreducible component of a gradient fibre, Euler's relation gives 3dF=dF, so F is constant. The equal-value fibre product has the same maximal fibre dimension as the full gradient fibre product. The resulting concentration argument is valid.

For Lemma 3.9, the trilinear vanishings and the two choices of weights give exactly the announced inequalities. In the nonsingular case, writing t=dim T and a=dim(T∩L), the calculation yields 0≤−3+a−3t+4r. Combining a≤t−1 and a≤n−r gives t≤2r−2 and t≤r+(n−3)/3. The singular case gives t≤min(n−r,2r−3). These bounds imply (3.6)–(3.8) and the required corollaries. The extra rank improvement when n≡1 mod 3 in Lemma 3.4 is also justified: the linear factor of det H produces a rational Hessian-kernel vector in the appropriate tangent space, contradicting anisotropy.

Proposition 4.1 handles separately the components of the incidence correspondence meeting the smooth locus and those lying entirely over Sing X. The latter case needs, and uses, t≥dim Sing X. The tangent annihilator M_v is rational at the selected rational point, so the earlier singular-locus bound applies to F restricted to M_v. Proposition 4.3 and Corollary 4.4 then supply the geometric dimensions and rational-point improvements used in §10. I found no missing exceptional case in these steps.

### Local and cubefull estimates: §§5–8, pages 17–34

The identities (5.1) and (5.2) and their conversion into Proposition 5.1 have the expected factors of p. Lemma 5.2 correctly bounds the vertex of a conical hyperplane section through the rank-two Hessian locus. The prime-square expansion in Lemma 5.3 gives the stated projective fibre count when v is nonzero modulo p and the affine singular-locus count when it is zero.

The dependence of G_{A,T} only on y modulo gcd(A,T) follows from an actual translation of the summation variable, and Lemma 5.7 retains the correct factor A^{n+1}T. Lemmas 6.1–6.3 properly distinguish primitive smooth residues, primitive singular residues, and the zero residue. The rank-two quadratic lifting estimate in Lemma 6.2 supplies the needed uniform loss at the singular residues.

In Lemma 6.7, the averaging over the remaining residue classes in the quadratic differencing step is essential. It produces N_{c/d}(h), as stated, rather than a larger kernel count with an additional d-factor. The subsequent substitution of (6.12) gives the scale r^{1/3}. The Euler-product calculation in Lemma 6.8 has the claimed threshold θ_10=2/5 and gives exponent 32/5 for n=10.

The Smith-filtration analysis in §7 is consistent. In particular, when t>a, the quadratic sum vanishes unless its linear coefficient lies in the image of p^{t−a}H(y); counting these classes gives the weights in (7.3). In Lemma 7.5, passing to the final Smith block and adding back the preceding rows and columns yields the rank bound c_{a−2}+c_{a−1}. This explains the precise argument of τ_n in (7.6). I checked the two cases in Lemma 7.7 against its table; they give all three claimed bounds on Φ_10.

The small-prime localization in §8 addresses the dependence exponential in Ω(q), rather than treating it as a divisor-function loss. The unit orbit is what permits the scalar-invariance argument in the multiplicativity formulas. The nonvanishing fixed Hessian minor gives bounded fibres for the local gradient map, yielding (8.5), and the congruence neighbourhood contains a smooth p-adic zero, yielding the positive local densities. For n=10, Lemma 8.4 gives the exponent 28/3 used in §11.

### Second moments and stratification: §§9–10, pages 35–48

Lemma 9.2 addresses the potentially important distinction between irreducibility of the multivariable polynomial and geometric irreducibility of the generic plane fibre. If the latter failed, its three conjugate linear factors would force a repeated direction in the leading binary cubic, contradicting the square-freeness of that irreducible binary cubic. With this input, Parseval and the exceptional specialization locus give the exponent 2n−3 in Lemma 9.1.

I checked the use of FK01 Theorem 2.1 in Lemma 9.3. Its conclusion supplies uniform constructibility and bounded total ranks for the exponential pushforward. Homogeneity permits a homogeneous refinement. Xu20 Theorem 3.5 and Remark 3.6 apply to the mixed lisse complexes after passing to pure constituents; the sum of ranks remains a valid bound. In Proposition 9.5, the high-weight alternative gives a second moment of order at least q^{2n−2} along an extension-field subsequence, whereas containment in a rational codimension-two linear space gives O(q^{2n−3}). This is the needed contradiction, including its uniformity in the sufficiently large prime.

The rearrangement of the strata into P_j and Q_k is consistent with (10.10). The exceptional integer Δ(v) can be selected from a fixed family of equations, which is needed for the divisor estimates later. In the counting argument of Proposition 10.1, translating and rescaling the counting box preserves degree and geometric irreducibility. The explanation excluding cones of degree at least four from being cylindrical over a curve is valid: the projected curve would itself be a geometrically irreducible homogeneous curve, hence a line.

I checked the exponent bookkeeping in Lemmas 10.5–10.8. In the small-radical case, the extra loss K is offset by the codimensions of the relevant strata; at n=10 the K^{-1/2} saving in the (0,0) stratum is obtained. In the large-radical case, the vectors lie outside all the closed varieties to which Proposition 2.9 is applied, a necessary hypothesis explicitly justified in the proof. Combining the resulting terms gives Proposition 10.9, including its interpolation factor ||P||_1^{2/3}||w||_1^{1/3} and exponent T^{20/3}.

### Mixed moduli and circle method: §§11–12, pages 48–58

The separation q=gdr is compatible with the localization and the coprimality hypotheses in the cube-free estimate. Lemma 11.2 has precisely the three Euler-factor types dictated by exponents modulo three. Its convergence threshold is max(0,(α−9)/12).

The two bounds for the error contribution in §11 are

- Q^{10+ε} C^η D^{-1/6} G^{-2/3};
- Q^{10−1/6+ε} G^{1/2}D^{5/2}.

Their 15/16 and 1/16 interpolation cancels the D exponent and yields Q^{10−1/96+ε}G^{-19/32}C^{15η/16}. The remaining Hölder term has the stronger saving 1/30. Choosing η before the arbitrary ε gives a fixed localization modulus W, as required by Proposition 11.1. The covering argument for longer boxes has the correct tenth power.

The main term in Lemma 12.2 follows from the positive localised singular series and the Schwartz decay of the real integral after the stated nonsingular coordinate change. Absolute convergence suffices for the limiting argument; a stronger unproved tail estimate is not being used.

Lemmas 12.3–12.5 use the Hessian rank near the real zero in the required way. The supremum over nearby frequency vectors in Lemma 12.5 still permits the chosen order of integration and counting, because a=a(v) is fixed before that calculation. The averaging identity leading to (12.16) is valid for nonnegative summands.

In Proposition 12.7 the choices L≈R^{1/3}, the lower cutoff from P^εV≥1, and the two endpoint estimates in ϕ give the advertised saving. The piecewise-linear optimization over R has breakpoints at 1, P and P^{3/2}. For n=10, ρ≥8 and b=20/3−γ, so the positive saving can be taken to be γ. The small-ϕ factor permits the infinite dyadic tail toward ϕ=0 to be summed. Finally, restricting an n-variable form to ten variables proves the result for n>10; an identically zero restriction already supplies a nontrivial zero.

### Appendix A: pages 58–64

I checked this appendix in full, including its exact external inputs.

The trace identity of Lemma A.3 and the weight bound of Lemma A.4 match the degree of the Gysin map. For Proposition A.7, RS22 constructs its exceptional sets from the projectivized singular support itself, so the manuscript is entitled to use these particular loci rather than merely unspecified loci of the same dimension. RS22's parameter r is n−2 for the closed immersion X→P^{n−1}, giving exactly the threshold a>n−2+i.

Lemma A.8's coefficient induction is sound. At a=t+1 the preceding vertical map is only required to be surjective, which is why surjectivity at the threshold is retained. Finiteness supplies the Mittag–Leffler condition needed for the inverse limit. Thus the passage from finite coefficients to Q_l has been addressed rather than assumed.

The supplied HY18 text allows an excellent Noetherian base and supplies both relative existence and equality with the singular supports of the fibres after shrinking. It applies to Spec Z[1/N]. The required result is present in the supplied preprint as Theorem 5.8, together with its existence results, even though its numbering differs from the manuscript's citation to the published version. Consequently the fixed integral strata and their good-prime specializations are justified.

Bei16 supplies equidimensionality, support, field-extension compatibility, and the characteristic-zero Lagrangian assertion used here. The inclusions Γ⊂Σ⊂S in (A.10) then give the required comparison with singular hyperplane sections.

Finally, the rational-point codimension gain is valid for components integral over Q, including components that are not geometrically integral. Biduality identifies the conormal fibre over a smooth rational dual point with a rational projective linear space contained in the original variety. Lemma A.11 gives the extra dimension loss for an actual fibre jump, while Lemma A.12 supplies it at the generic fibre dimension. These are the three cases in Proposition A.13. This establishes (A.3), the arithmetic improvement central to the proof.

## Corrections and presentation points

**Substantive repairs required:** none identified.

The following are minor precision or editorial improvements, not obstructions to the result:

1. **Lemma 12.5, page 56, equations (12.13)–(12.14):** explicitly say that the neighbourhood U is chosen small enough that the coordinate map and its inverse are uniformly bi-Lipschitz on the relevant region. The displayed lower Lipschitz estimate is locally available by shrinking around x_0; smoothness of an inverse on an arbitrary open set alone is not the most precise justification for a global pairwise inequality. The proof already allows this shrinking, and all estimates use the fixed smaller box.
2. **Lemma 9.3, page 37:** remove the duplicated wording “again let us again”.
3. **Reference-version concordance for HY18, page 62:** for readers using the supplied arXiv version, add the corresponding Theorem 5.8 citation for specialization and Theorem 5.3/5.4 for existence. I found the required statement in that version; this is a numbering/concordance point, not a missing theorem.

The apparent “2” in the quadratic identity in Lemma 7.2 is an inverse of 2 modulo p^a in the PDF. It is correct and should not be reported as a coefficient error.

## Literature dependencies and limits of source verification

I directly checked the relevant statements, and the relevant proof passages where needed, in all five supplied references: Bei16, FK01, HY18, RS22 and Xu20. I found no unresolved mismatch in these applications.

Other inputs are ordinary cited dependencies whose original sources were not in the authorized supplement: Davenport's goodness theorem; finite-field point-count bounds and the hyperplane singular-locus bound; the oscillatory-integral estimate; Bernert's singular-series theorem and kernel estimate; existence of smooth local zeros; the uniform integral-point estimates of Pila and Vermeulen; the smooth delta-method formula; and the standard duality/dimension facts cited elsewhere. I checked their role and the stated hypotheses within this manuscript, but did not perform an independent source-by-source verification of these unavailable articles. The most quantitatively consequential such dependencies are Theorem 5.4, Proposition 10.1(ii), and Proposition 12.1.

The manuscript's new arguments provide the missing steps between these inputs and the announced ten-variable conclusion. On the complete evidence reviewed, acceptance is warranted.
