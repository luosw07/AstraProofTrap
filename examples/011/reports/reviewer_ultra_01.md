# Independent mathematical audit of e02

**Verdict: ACCEPT.**

I find the argument mathematically sound, subject to the ordinary use of its cited results. I found no essential repair to the proof of Theorem 1.1. The numerical margins in the last two sections are positive, and the singular-support argument supplies the arithmetic codimension gain actually used earlier in the paper. There are a few citation and exposition corrections, recorded below; none changes an estimate or requires a new mathematical idea.

## Scope and method

I read the complete 66-page manuscript, including Appendix A and the bibliography, from the supplied text in consecutive, bounded, untruncated chunks. I also inspected rendered PDF pages 28, 36, and 62 to resolve typography and field notation. In particular, the field in Lemma 9.2 is \(K=\overline{\mathbb Q}(T_3,\ldots,T_n)\), and the factor preceding \(p^{t-a}H(y)h\cdot h\) in the proof of Lemma 7.2 is \(\overline 2\), the inverse of 2; neither is an error.

I consulted all five supplied references at the results actually invoked: Beilinson's singular-support properties, Hu–Yang's relative specialization theorem, Raskin–Smith's Gysin construction and exceptional loci, Fouvry–Katz's uniform constructibility theorem, and Xu's virtual trace-function moment theorem. I did not use any other manuscript, review, private report, formalization, internet source, or agent. The review distinguishes checking a quoted theorem's use from re-proving all external literature. The bibliography contains further results whose full texts were not supplied; the material dependency register below identifies them.

## Essential repairs

**None identified.** In particular, the following potentially delicate transitions work:

1. Lemma 3.6 genuinely descends an optimal weighted flag to \(\mathbb Q\); it does not assume that an arbitrary geometric flag is rational.
2. Lemma 3.8 justifies restricting the incidence-dimension calculation to \(F(x)=0\).
3. The second-moment argument in Section 9 uses all finite extensions of a fixed finite field, as required to apply Xu's limsup alternative.
4. Appendix A uses finite coefficients for relative singular support and then separately lifts the Gysin conclusion to \(\mathbb Q_\ell\).
5. The fixed small-prime localization modulus is chosen before the final analytic \(\varepsilon\). Its dependence on a fixed \(\eta\), and hence on the desired saving \(\gamma\), is consistent.
6. The final shifted-box estimate is strong enough for the oscillatory integral estimate, with a strictly positive power saving when \(n=10\).

## Complete coverage and mathematical checks

### Pages 1–5: setup and reduction

The contradiction strategy is coherent: assume the cubic has no rational projective point, derive structural bounds under that assumption, and then obtain a positive localized asymptotic. The reduction from more than ten variables to ten at the end is legitimate; if the restricted cubic were identically zero, any nonzero vector in the restricted coordinate space would already be a zero.

Theorem 1.3 follows from Lemma 3.9. Under the contrary assumption, its bound is \(\dim\operatorname{Sing}X\le\lfloor(2n-6)/3\rfloor\), whereas the singular-codimension hypothesis gives the incompatible lower bound \(n-2-\lfloor(n-1)/3\rfloor\). The nonsingular/empty singular-locus edge cases do not produce an exception.

### Pages 5–8: Section 2

The finite-field point-counting inputs and Zak bound are used in the stated ranges. In Lemma 2.6, linear Noether normalization, clearing denominators, and raising the separate monic relations to a common degree give the required polynomial relations. Possible finitely many bad primes are harmless in the subsequent fixed-scheme implied constants.

Lemma 2.7 is uniform in a translated box and residue class because the normalizing map is fixed. In Lemma 2.8, once the first \(d\) coordinates and one coordinate with a nonzero polynomial value have been selected, the admissible square-free moduli divide a nonzero integer of polynomially bounded size. For each other coordinate, polynomial root-counting modulo the square-free modulus and the coprimality with \(m\) give only \(O(q^\varepsilon)\) choices when \(q\gg L/m\). This gives exactly the \(d+1\) exponent, including the case of shifted boxes.

Proposition 2.9 correctly separates the short total modulus from the first modulus crossing the box scale. In the latter case the tail residue classes contribute \(\prod_{i>j}q_i^{d_i}\), while Lemma 2.8 contributes \((L/(m\prod_{i>j}q_i))^{d_j+1}\); summing the tail moduli gives the displayed powers \(R_i^{d_i-d_j}\). The exclusion of integral points on the sieved varieties is necessary for, and present in, the divisor argument.

The three oscillatory-integral estimates in Lemma 2.10 are compatible: the frequency scale for support is \(qP^{-1}\max(1,|\theta|P^3)\), while the smaller volume window uses its square-root counterpart. The final support assertion follows from the same volume bound and the size of \(q\theta\nabla F(x)\).

### Pages 8–15: Section 3

Lemma 3.1 correctly differentiates a rank minor at a point of exact rank. The use of the reduced tangent space causes no problem: the determinantal equations still vanish on it.

In Lemma 3.4 the relevant matrix divisibility takes place in the polynomial UFD at the principal prime \((F)\); the manuscript explicitly avoids the invalid greater generality of the cited statement. The exceptional congruence class \(n\equiv1\pmod3\) is handled by the rational hyperplane factor of \(\det H\). Choosing a rational generic-rank point on that hyperplane and a rational kernel vector, and then applying Lemma 3.1, gives the claimed contradiction. Thus the stronger even bound \(r(F)\ge2\lceil n/3\rceil\) is justified.

I checked the flag-descent proof of Lemma 3.6. There are finitely many monomial supports, and each feasible fixed-total-weight polyhedron has a shortest vector. Bruhat decomposition aligns two flags by a permutation and weight-nondecreasing matrices. Averaging the aligned weights remains feasible for the common transformed form. Minimality and strict convexity force the weight permutation to fix the minimizing vector when comparing a matrix with a Galois conjugate. Consequently the entire weighted filtration is Galois-stable. A rational splitting of that filtration provides a rational coordinate matrix preserving nonnegative monomial weights. The coefficients of the pure cubes in those coordinates are nonzero by the no-rational-zero hypothesis. Their weights force the total weight to be nonnegative. This supplies the geometric input without invoking Kempf as an unproved new step.

Lemma 3.8's linear change \((x,y)\mapsto(y+x,y-x)\) is invertible in characteristic zero and gives the two gradient fibers in the proof. On each irreducible component of a fixed-gradient fiber, Euler's identity and differentiation yield \(3,dF=dF\), so \(F\) is constant. The largest component crossed with itself therefore gives the same fiber dimension after imposing equality of the two cubic values. This validates \(\dim J_0=\dim J\), including jumping gradient fibers.

In Lemma 3.9 the singular case has \(T\subseteq\ker H(x)\); the weights \((-4,-1,0,2)\) give \(\dim T\le2r-3\). In the nonsingular case, putting \(a=\dim(T\cap\ker H(x))\) and \(t=\dim T\), the listed trilinear vanishing identities justify all negative-weight exclusions for weights \((-2,0,1,4)\). The resulting inequality is \(0\le-3+a-3t+4r\). Using respectively \(a\le t-1\) and \(a\le n-r\) gives both estimates in (3.10). Optimizing these bounds gives (3.6)–(3.8). Corollary 3.10 and the singular-linear-space bound in Lemma 3.11 follow with the stated integer rounding.

### Pages 15–17: Section 4

In Proposition 4.1 the incidence map may be restricted to a generically smooth dominating component of sufficiently large relative dimension. For the component meeting \(X_{\rm sm}\), differentiating \(F(x)=x\cdot v=0\) gives \(x\perp T_v\widehat Z\). For the component entirely over \(\operatorname{Sing}X\), the dimension inequalities force a product with a top-dimensional singular component, and differentiation in \(v\) gives the same conclusion. Selecting a rational point in the rational-point closure makes the annihilator a rational linear space, so Lemma 3.9 applies to the restricted cubic. This proves the sharper arithmetic dimension bound.

Proposition 4.3 properly separates a jump of the conormal projection from hyperplanes containing a top-dimensional component of the singular locus. Lemma 3.11 excludes a linear singular component of the problematic dimension, giving the extra dimension in its linear span. Corollary 4.4 then gives, for ten variables, singular dimension at most four, finitely many rational hyperplanes with singular-section dimension at least four, and none with dimension at least five. These are the precise facts later required.

### Pages 17–22: Section 5

The identities (5.1) and (5.2) have the correct main-term cancellations. The Hessian calculation at the vertex of a conical hyperplane section puts its affine vertex in \(V_2\cap\widehat X\). Corollary 3.10 bounds that vertex dimension by two, leaving a sufficiently large nonconical base for Lemma 2.1. This yields the claimed prime bounds, including the different exponent at zero frequency.

For prime squares, expansion and orthogonality give the factor \(p^{n+1}\). At nonzero frequency the remaining solutions are parametrized by the projective tangency locus, with \(p-1\) choices of affine representative and a uniquely determined unit multiplier. At zero frequency the singular affine cone is the appropriate object. The dimensions yield both (5.9) and (5.10).

For the lifting lemmas, \(q=A^2T\), \(M=AT\), and \(M^2\equiv0\pmod q\) give exactly the two congruence conditions modulo \(A\). The remaining Taylor expansion produces \(Q_y+AF\). Translation in the summation variable proves the claimed \(\gcd(A,T)\)-periodicity of the maximum. The unit-lift count is at most \(T\), giving (5.14). The quadratic differencing estimate has the stated kernel factor.

Theorem 5.4 is an external input, recorded separately below.

### Pages 22–27: Section 6

Lemma 6.1 handles the smooth, zero, and primitive-singular residues separately. In the last case the rank-at-least-two assertion is exactly what Corollary 3.10 provides. Lemma 6.2's binary reduction and induction are sound: nonsingular residues lift with factor \(p^{s-1}\), while the origin reduces the precision by two. The bound \((s+1)p^{s(n-1)}\) is sufficient even for the split rank-two quadratic form.

The functions \(\delta_n\) and \(\gamma_n\) account for the dimensions of Hessian-rank loci and the extra singular weights. The proof of Lemma 6.5 correctly bounds the weighted kernel sum by \(p^{3n/2-\lceil n/3\rceil-1}\). Lemma 6.6 then follows after summing residue classes and applying the root count from Lemma 6.1.

In Lemma 6.7, dropping the congruence from \(c\mid F\) to \(d_1\mid F\) only enlarges a nonnegative majorant. The first CRT factor is controlled by Lemma 6.5; the second uses Cauchy–Schwarz and quadratic differencing. The Hessian symmetry makes the resulting kernel count depend on \(h\). Summing it with goodness gives the factor \((1+r/V^3)^{n/2}\), harmless after enlarging \(V\) to at least \(r^{1/3}\). Translation of the original box contributes only a unit-modulus Fourier factor.

The cubefull Euler product in Lemma 6.8 has thresholds \(1/4,(a_n+1)/3,(b_n+1)/5\). For \(n=10\) these are \(1/4,1/3,2/5\), giving \(R^{32/5+\varepsilon}\), as used in Section 11.

### Pages 27–32: Section 7

The cube-root lifting estimate keeps only congruence information modulo \(A\), which is why its maxima over residue classes can later be combined with a sieve. For \(t\le a\), Lemma 7.2 follows from the Smith-invariant expression for the quadratic kernel. For \(t>a\), averaging translations in the quadratic kernel restricts the allowable residue vector; the number of such vectors is \(p^{\sum\max(0,t-2a+j_\nu)}\). The remaining quadratic bound gives the weights in (7.3), including when \(t\ge2a\).

Lemma 7.4 is justified by projective closure: the locus at infinity is \(V_j\), and the affine dimension is at most its dimension. In Lemma 7.5, after clearing the old pivots, the remaining block has rank \(c_{a-1}-c_{a-2}\). Restoring its deleted rows and columns gives the bound \(c_{a-1}+c_{a-2}\) for the full residual matrix. This produces precisely the sum of \(\tau_n\)'s in (7.6). The exponential-in-precision constant is acknowledged and legitimately absorbed only at sufficiently large primes.

I checked the ten-variable table and the two branches of Lemma 7.7. For \(c_0\ge4\), its three elementary inequalities give the stated \(U\)-bounds. For \(c_0\le3\), \(\tau(c_{i-1}+c_i)\le\min(c_i+5,10)\) gives the asserted bound on \((U+V)/2\). These imply \(\Phi_{10}(e,e)\le7e-2\), \(\Phi_{10}(e,e+1)\le7e-5\), and \(\Phi_{10}(e+1,e)\le7e+7\), with no missing small-\(e\) case. Thus the factors \(z_0^{-2}z_1^{-4}z_2^{-1}\) in (7.12) are correct.

### Pages 32–34: Section 8

Choosing a smooth local zero of maximal Hessian rank and a sufficiently small compact ball gives uniform derivative and minor valuations. Taking its unit orbit preserves these bounds and, crucially, the scalar invariance needed for multiplicativity. The implicit-function arguments give bounded fibers in the rank-many selected gradient coordinates. Equation (8.5) then yields \(g^7\) when \(n=10\) and \(r(F)\ge8\).

The modulus \(\operatorname{lcm}(q,W)\) in (8.9) is the correct Poisson modulus for the congruence restriction. The local density identity in Lemma 8.3 includes the factors for small prime-power exponents below \(M_p\); its normalization is correct. Absolute convergence and positivity survive localization. Lemma 8.4 gives \(p^{k(n+(4-r(F))/6)}\), hence the \(g^{28/3}\) residue-maxima bound used later.

### Pages 35–38: Section 9

Parseval in the last \(n-2\) variables gives the second moment exactly as \(q^{n-2}\sum_{x'}|\nu_F(x')-q|^2\). Lemma 9.2 establishes absolute irreducibility of the generic two-variable fiber: a geometric factorization of an irreducible cubic would consist of three conjugate affine lines; their slopes lie in the algebraically closed constant field, hence would all coincide, contradicting squarefreeness of the restricted binary cubic. The bad specialization locus therefore has codimension at least one. Its contribution and the Lang–Weil contribution both give \(O(q^{2n-3})\).

Fouvry–Katz provides the uniform lisse stratification and total-rank bound required in Lemma 9.3. Scaling the affine cone gives equivariance of the Fourier complex in the frequency variable, so the refinement into homogeneous strata is legitimate.

In Proposition 9.5, Xu applies to the alternating trace of mixed lisse cohomology sheaves, using his explicit mixed-sheaf extension. With \(w=n+r-2\), its second alternative has normalizing exponent \(\dim U+w+1=2n-2\). If \(\deg V\le r\), the minimal-degree/linear-span inequality puts \(V\) in a rational codimension-two linear space. Lemma 9.1 then forces that normalized second moment to tend to zero, a contradiction. The constants in the first alternative are controlled by the uniform total rank. This is a valid degree-sensitive improvement of the prime strata.

### Pages 38–48: Section 10

The exceptional-locus inclusions from Appendix A, together with Corollary 4.4, give the stated geometric dimensions and rational-point-closure dimensions. The redistribution of low-degree top-dimensional components via \(U_j\) removes them from level \(j\) and adds them to level \(j-1\); it preserves a partition. The intersections with the square strata are exactly (10.10).

The polynomial \(\Delta(v)\) is nonzero at the given frequency and records the exceptional reduction primes. In the moved-stratum case the frequency also belongs to the relevant closed component, so excluding the boundary by a polynomial suffices. The finite choice of defining polynomials gives the polynomial size bound needed for the divisor estimate. The rational-frequency counts apply the cited uniform integer-point bounds after a translation and residue-class substitution, preserving degree. The high-degree cones are not cylindrical over a curve: a homogeneous geometrically irreducible curve is a line, which would make the original cone linear.

The estimates (10.13)–(10.15) correctly distinguish the pointwise exceptional-prime factors from their averaged divisor costs. In particular, exceptional primes with small actual exponential sums need not divide \(\Delta(v)\); intersecting with \(\Delta(v)\) is sound because the complementary primes already satisfy the improved global bound.

For Lemma 10.7, the small product \(r\le T\) allows use of residue counts within the box, and the prime exponents \(a_p,b_p\) give the stated \(T\)-powers. The special \((j,k)=(0,0)\) case gains \(K_j^{-1/(n-8)}\); its endpoint inequality remains valid at \(n=10\). For Lemma 10.8 the integral frequencies lie outside every deeper sieved variety, so Proposition 2.9 applies. Its three possible dominant terms give the three alternatives analyzed in the proof, all bounded by (10.22).

In ten variables the error terms in Proposition 10.9 are exactly \(TD^9,T^9D^{13/2},T^8D^7,T^7D^{15/2},T^5D^8,T^4D^{17/2}\). Substituting \(T=xD^{1/3}\) gives the displayed upper envelope. On the main stratum, interpolation of the \(K^{-1/2}\) and \(K\) bounds with powers \(2/3,1/3\) cancels \(K\) and gives \(D^{13/2}T^{20/3}\|P\|_1^{2/3}\|w\|_1^{1/3}\).

### Pages 48–52: Section 11

The separation \(q=gdr\), the two norms of the cubefull weights, and the small-prime maxima are compatible because \(\operatorname{rad}(m_{g,r})=\operatorname{rad}(gr)\). Lemma 11.2's three local series converge for \(s>\max(0,(\alpha-9)/12)\), including \(\alpha=0\) and \(10\).

I checked the final exponent arithmetic. The two error alternatives are bounded by
\[
 Q^{10+\varepsilon}C^\eta D^{-1/6}G^{-2/3},\qquad
 Q^{10-1/6+\varepsilon}G^{1/2}D^{5/2}.
\]
Taking powers \(15/16\) and \(1/16\) cancels \(D\), leaves \(G^{-19/32}\), and saves \(1/96\) in \(Q\). Hölder applied to the main-stratum term gives
\[
 Q^{10-1/30+\varepsilon}G^{-3/10}D^{-2/15}C^{2\eta/3}.
\]
Choosing \(0<\eta<1/96-\gamma\) and covering larger boxes yields Proposition 11.1 with the stated fixed modulus and saving. There is no dependency cycle between that choice and the arbitrary final \(\varepsilon\).

### Pages 52–58: Section 12

The localized Poisson formula uses exactly the exponential sums from Section 8. The zero-frequency integral becomes the Fourier transform of a smooth compactly supported density in the \(F\)-coordinate. It is Schwartz, and its integral is positive. Absolute convergence of the localized singular series justifies the limiting argument in Lemma 12.2; no rate of convergence is needed.

The maximal-rank gradient coordinates give the volume estimate in Lemma 12.3. Lemma 12.5 correctly controls the supremum over nearby integer frequencies: after fixing the first \(\rho\) frequency coordinates and the remaining real coordinates, the other frequency coordinates lie in a box of radius \(O(P^\varepsilon V_0+L)\); the remaining real volume is bounded by \(\min(1,V_0/(R\phi P^2))^\rho\). This is the uniformity needed in (12.16).

For \(\phi P^3\le1\), the existence of a nonzero frequency implies \(R\gg P^{1-\varepsilon}\), and \(L\asymp R^{1/3}\) gives saving \(2n/3-b\). For \(\phi P^3>1\), the same choice of \(L\) and optimization over the endpoints of the allowed \(\phi\)-range give the two terms displayed on page 58. Their exponents are piecewise affine in \(\log_P R\), with possible maxima at \(R\asymp1,P,P^{3/2}\). The resulting minimum saving is positive. For ten variables, \(\rho\ge8\) and \(b=20/3-\gamma\), so one can take \(\Delta=\gamma\). The factor \(\min(1,\phi P^3)\) makes the infinite tail of small dyadic \(\phi\)-intervals summable. Consequently the total error is \(o(P^7)\), completing the contradiction.

### Pages 58–64: Appendix A

The projective point-count identity removes the issue of varying additive-character sheaves in the relative construction. Raskin–Smith's Gysin map is Frobenius-equivariant. The support of its cone is contained in the projection of the hyperplane fiber of \(\mathbb PSS\). A fiber of dimension at most \(i-2\) gives an isomorphism above degree \(n-2+i\), exactly as Proposition A.7 states.

Lemma A.8 has the correct endpoint hypothesis: surjectivity in degree \(t\) is enough for the first vertical map in the five-lemma argument in degree \(t+1\). Induction handles every finite coefficient exponent. The finite cohomology groups make the kernels Mittag–Leffler, so the inverse-limit map remains surjective; tensoring with \(\mathbb Q_\ell\) preserves the conclusion. Thus the fixed finite-coefficient singular support legitimately controls the rational-coefficient trace estimate.

Hu–Yang's theorem applies over the excellent mixed-characteristic base \(\operatorname{Spec}\mathbb Z[1/N]\) with \(\ell\) inverted. After shrinking, its fiber singular supports are exactly the reductions of the relative support. Upper semicontinuity and properness give closed fiber-jump loci, so the construction produces one family of homogeneous strata valid away from finitely many primes. Beilinson's dimension theorem gives their codimensions. The inclusions \(\Gamma\subseteq\Sigma\subseteq S\) are justified by ordinary conormals over the smooth locus and by the singular-locus equations elsewhere.

For the arithmetic improvement, characteristic-zero singular-support components are conormal closures to integral subvarieties contained in \(X\). Lemma A.12 works also for integral but geometrically reducible varieties: a rational smooth point of the dual has a rational annihilator projective linear space, and biduality puts that entire space in the original variety. It would give a rational point. Lemma A.11 supplies an extra codimension for genuine fiber jumps. Applying these two facts in the three cases \(c_\alpha>i-1\), \(c_\alpha<i-1\), and equality gives \(\dim Y_i(\mathbb Q)\le n-i-2\). Passing to affine cones gives (A.3), including the origin convention. This is the exact additional codimension used in Section 10.

### Pages 64–66

The bibliography and final pages were read. No further mathematical claims or omitted appendices occur there. The supplementary-code and AI statements were not treated as evidence for correctness.

## Editorial corrections and clarifications

1. **Page 62, Section A.2.1, citation preceding (A.8).** The text has “and and.” More substantively, the supplied HY18 file is the 2017 preprint: its 5.2 is a lemma, and its Theorem 5.3 proves existence, not the fiber equality by itself. In that supplied version the direct reference for (A.8) is **Theorem 5.8**, with Theorems 5.4 and 5.9 also relevant. The citation should identify the version or give this cross-reference. The needed mathematical theorem is present, so this is a citation correction rather than an unsupported step.
2. **Page 59, Section A.1.1, sentence about RS22 and \(r=1\).** The supplied RS22 text already allows \(\Lambda=\mathbb Z/\ell\mathbb Z\) with \(\ell\) a prime power, both in Theorem 1.2 and Section 2.1. Saying that it only explicitly discusses \(r=1\) is inaccurate for this supplied version. This can simply be corrected; Lemma A.8 remains a useful explicit coefficient argument.
3. **Page 52, equation (12.2).** Write the nonvanishing Jacobian estimate as \(\left|\det(\partial_i\partial_jF(y))_{i,j\le r(F)}\right|\gg1\). A nonsingular real symmetric minor need not have positive determinant. Every subsequent use concerns absolute Jacobian size, so the intended assertion and proof are unaffected.
4. **Pages 36–37, Lemma 9.3.** It would improve readability to state the scaling base-change argument proving descent/equivariance of \(K_{p,\psi}\) on \(\mathbb A^n\setminus\{0\}\). It is available directly by changing the cone coordinate \(x\mapsto\lambda^{-1}x\). This is an explanatory addition, not an essential gap. The repeated “again” near the start of page 37 can also be removed.
5. **Page 56, proof of Lemma 12.5.** The uniform inverse-Lipschitz estimate can be made explicit by choosing the real ball sufficiently small that the selected derivative block is uniformly close to its invertible value at \(x_0\). This is consistent with the existing freedom to shrink \(U\) and \(\ell\), and avoids any impression that bounded inverse derivative alone is being asserted to imply a global estimate on an arbitrary nonconvex image.

## External dependency register

The following sensitive supplied dependencies were verified against their actual statements and hypotheses:

- **Bei16:** Theorems 1.3 and 1.4(iii), Lemmas 2.3 and 2.5, and the characteristic-zero Lagrangian remark support the dimension, base, base-change, smooth-conormal, and characteristic-zero conormal assertions used in Appendix A.
- **HY18:** Theorem 5.8 in the supplied version gives the relative specialization identity over an excellent Noetherian base, which includes the arithmetic base used here. Its hypotheses do not impose an equal-characteristic restriction.
- **RS22:** Theorem 2.2, Corollary 2.3, their construction using \(\mathbb PSS\), and the proof of Theorem 1.2 give precisely the exceptional loci and degree threshold needed in Proposition A.7.
- **FK01:** Theorem 2.1 provides a common finite-type stratification with lisse cohomology and a uniform total-rank bound for the exponential Fourier family. The constant-sheaf input is adapted to a suitable source stratification.
- **Xu20:** Theorem 3.5 and the mixed-lisse extension in Remark 3.6 permit the virtual mixed trace function in Proposition 9.5 and the second moment over all \(\mathbb F_{p^a}\).

The further cited inputs were assessed for compatibility with their stated applications, but their full source texts were outside the supplied materials: Davenport's goodness implication; the Hooley–Katz/Zak and cubic Lang–Weil point bounds; Bernert's absolute convergence and positivity theorem; Pleasants' smooth local solvability; the Pila and Vermeulen uniform integer-point bounds; the cited oscillatory-integral estimate; the smooth delta-method formula; and standard biduality and degree-versus-linear-span results. Of these, **Bernert (Theorem 5.4)** and the **uniformity in the Pila/Vermeulen estimates used in Proposition 10.1** are especially material to the analytic conclusion. I found no hypothesis conflict in their uses. This is the remaining source-verification boundary of the restricted audit, rather than a mathematical counterargument.

## Final judgment

The manuscript's new geometric and analytic arguments fit together and supply the claimed ten-variable contradiction. In particular, the exact chain is: no rational zero gives the Hessian and incidence bounds; singular support plus biduality gives the rational-stratum codimension gain; the second moment improves low-degree strata; cube-root lifting and the stratified sieve yield a shifted-box saving \(\gamma<1/96\); the localized circle method converts that saving into a positive main term with smaller error. I recommend **ACCEPT**, with the localized editorial corrections listed above.
