# Independent mathematical review of e02

**Verdict: ACCEPT.**

I read the complete 66-page manuscript, including Appendix A and the references, using the supplied text in bounded chunks and checking the PDF where overbars affected interpretation. I find no substantive mathematical error or missing argument in the proof of Theorem 1.1. My acceptance is in the ordinary mathematical-review sense: the cited results outside the five supplied references are treated as external inputs, with their required formulations and applications examined, rather than independently reproved.

## Scope and method

Inputs were exclusively `blind/e02/paper.pdf`, `blind/e02/paper.txt`, and the five supplied reference texts/PDFs. I did not consult another manuscript, review, formalization, internet source, private record, or agent. The manuscript's formalization link and AI statement played no evidential role.

The entire manuscript text (lines 1–3857) was covered. An initially overlarge display of lines 501–1000 omitted a short passage; I separately reread lines 745–785, including the omitted proof of Corollary 3.10. The PDF has 66 pages. In particular, I visually checked page 36 to distinguish Q-bar(T) from Q(T) in Lemma 9.2, and page 28 to distinguish the inverse of 2 from an erroneous coefficient 2 in Lemma 7.2. Those are extraction ambiguities, not manuscript errors.

I checked the operative statements and relevant surrounding arguments in all five supplied references. I did not undertake a line-by-line reproof of those entire reference papers.

## Principal checks

### Pages 1–8: setup, sieve and integral input

The contradiction strategy consistently assumes X(Q) is empty, and its later arithmetic-geometric consequences are used only under that assumption. The reduction from n > 10 by restriction to ten variables is valid (if the restriction is identically zero, the conclusion is immediate).

Lemma 2.6 can give a common leading coefficient and common degree by raising degrees with monomials and clearing denominators. Its linear change need not be unimodular: injectivity on integer points and enlargement of the transformed box suffice for the subsequent upper bounds. The squarefree-modulus argument in Lemma 2.8 correctly uses a nonzero polynomial value to restrict the modulus by divisibility and bounds lifts of other coordinates modulo qm. Primes dividing the fixed leading coefficient contribute only a fixed factor. Proposition 2.9 correctly distinguishes the product of local moduli below and above L/m; coprimality permits the simultaneous residue restrictions. The dimensions and denominator exponents in (2.3) agree with those operations.

Lemma 2.10 is a substantive external oscillatory-integral input from BHB09. Its square-root scale V0 and its larger cutoff scale for |v| are different, and the manuscript keeps that distinction in Section 12.

### Pages 8–17: geometric consequences of no rational point

Lemma 3.1 uses the differential of determinantal minors at a point of exact rank r and applies equally to tangent vectors to the reduced rank locus. Lemma 3.4 needs divisibility by the principal prime (F), rather than Zak's more general incorrect formulation; Remark 3.5 explicitly makes this restriction. The n = 1 mod 3 improvement follows from the rational hyperplane factor of det H and the symmetry H(x)y = H(y)x.

The descent proof in Lemma 3.6 is internally sound. Minimization takes place in a finite collection of closed feasible polyhedra, so a norm minimum exists. Bruhat decomposition and convex averaging force each Galois conjugate of the minimizing weighted flag to be the same flag. A rational basis splitting the descended flag then gives the contradiction from the nonzero pure cubic coefficients. This justifies use of nonrational tangent spaces in the weight arguments.

In Lemma 3.8, F is constant on each irreducible component of a gradient fibre: differentiating Euler's identity yields 3 dF = dF. Hence taking the product of a maximal-dimensional component with itself gives the required equal-fibre dimension for J and J0. Lemma 3.9's two weighted flags give respectively t <= min(n-r,2r-3) and t <= min(r+(n-3)/3,2r-2); their incidence consequences have the stated integer bounds. Corollary 3.10 and Lemma 3.11 then follow as written.

The tangent-lifting argument in Proposition 4.1 is valid after choosing a dominating component of maximal generic fibre dimension and restricting to a smooth dense open. In its singular case, equality of dimensions forces a product component, giving the asserted annihilator inclusion. Applying Lemma 3.9 to the rational slice M_v is legitimate. Proposition 4.3 separately handles the conormal part and components of the original singular locus; its nonlinearity argument is supplied by Lemma 3.11. I checked the n = 10 and n = 11 boundary cases in Corollary 4.4.

### Pages 17–27: local sums and squarefull averaging

The orthogonality identities (5.1)–(5.2) have the correct powers of p. In Lemma 5.2 the cone vertex lies in the rank-at-most-two Hessian locus on F = 0, so the bound on its dimension follows from the preceding geometry. The p-squared calculation in Lemma 5.3 includes the extra scaling parameter correctly, including the affine singular cone when v is zero modulo p.

Lemmas 5.5–5.7 preserve the requisite periodicity: translating y by Ah can be absorbed by translating the summation variable and the linear coefficient, and the final number of lifts of a unit is at most T. No assumption T | A is used before Lemma 5.9.

In Lemma 6.1 the singular nonzero residue case reduces to a polynomial with quadratic rank at least two; Lemma 6.2's induction accounts separately for the origin and smooth residues of the conic. The rank tables in (6.4)–(6.6) give the asserted Lemma 6.5 exponent. In Lemma 6.7 the translated real box affects Poisson summation only through a unit-modulus phase. Cauchy–Schwarz over residue classes modulo d2 and quadratic differencing are consistent with the stated kernel-count factor. The summation bound (6.12) follows from goodness and the rank-dependent kernel estimate. The Euler product in Lemma 6.8 yields theta_10 = 2/5, hence R^(32/5+epsilon), as required later.

### Pages 27–35: cube-root lifting and small primes

The t > a calculation of Lemma 7.2 uses averaging over the kernel of p^(t-a)H(y). The Smith-coordinate condition leaves p^max(0,t-2a+j_nu) choices per coordinate for v, giving precisely the two weights in (7.3). The PDF writes the inverse of 2 in the quadratic identity; the plain-text extraction is misleading here.

Lemma 7.5 correctly bounds the number of possible last digits by the rank of a translated Hessian matrix. The top rows and columns increase rank by at most 2c_(a-2). The exponential-in-a constant is explicitly absorbed only after excluding finitely many small primes. The elementary optimization in Lemma 7.7 checks out for x >= 4 and x <= 3, including e = 1 and the zero-weight final index in the pair (e+1,e).

Section 8 supplies the missing treatment of those finitely many primes rather than silently absorbing exponential prime-power losses into q^epsilon. The unit orbit of the local ball preserves multiplicativity. A fixed Hessian minor of bounded valuation gives the pointwise bound (8.5); the gradient equation gives the bounded-fibre assertion with the remaining coordinates fixed. The restricted local density is positive at a smooth local zero. The local singular-series identity is correctly normalized by lcm(p^k,p^M)^(-n). Lemma 8.4 has exponent n+(4-r(F))/6, which is 28/3 or better when n = 10.

### Pages 35–48: moments and stratification

Lemma 9.2 is an important place where the PDF matters: its field is K = Q-bar(T3,...,Tn), and it proves irreducibility over K-bar. Absolute irreducibility of F gives irreducibility over K; a geometrically reducible irreducible cubic would have three conjugate linear factors. Their slopes are constants in Q-bar and hence fixed over K. Transitivity would force equal slopes, contradicting squarefreeness of the binary restriction. Thus the generic fibre needed in Lemma 9.1 is geometrically integral. Parseval then gives q^(2n-3).

FK01 Theorem 2.1 supplies a common finite stratification and a rank bound for the Fourier complexes in Lemma 9.3. Homogeneity gives the scalar equivariance needed to saturate its open strata. Xu20 Theorem 3.5 and Remark 3.6 expressly cover the virtual trace argument, including extension to mixed lisse sheaves. Its second-moment alternative has exponent dim U + w + 1 = 2n-2 in Proposition 9.5. The contradiction with Lemma 9.1 is consequently a full factor q, and the degree/span argument has the correct codimension.

The modified P_j partition moves only the low-degree open pieces one level down. P_j intersect Q_k is empty except for the stated diagonal/adjacent cases. The exceptional divisors Delta(v), Theta(v) are nonzero with polynomial size, permitting the divisor-bound summations. Proposition 10.1 uses degree-uniform integral-point estimates after the affine substitution v=b+mu; the cone condition excludes a nonlinear cylinder over a curve.

I checked the local exponents and modulus counts in (10.13)–(10.15), the residue-class factor in Lemma 10.7, and the large-product application of Proposition 2.9 in Lemma 10.8. The low/high-depth dimension improvements enter where required. In Proposition 10.9 the K_0 powers cancel under the 2/3,1/3 interpolation; the error is bounded by the stated minimum of two independently valid estimates.

### Pages 48–58: mixed average and final error

The smooth-prime factor g has only G^epsilon possible values. Lemma 11.2's Euler factors converge for s > max(0,(alpha-9)/12). The moments with alpha = 1,9,10 therefore have the stated powers. Interpolation of the two error estimates gives Q^(10-1/96)G^(-19/32), up to the controllable eta loss. The main interpolation gives Q^(10-1/30)G^(-3/10)D^(-2/15), also up to eta. W is fixed using eta before epsilon is varied, which is essential for the quantifiers of Proposition 11.1.

The main term in Lemma 12.2 uses absolute convergence, positive restricted density, and a Schwartz singular integral; no rate of convergence of the full singular series is needed. The integral estimates use a local inverse Hessian map on a sufficiently small ball. In Lemma 12.5 one may further shrink that ball to obtain the uniform inverse Lipschitz bounds; the counting order v',y'',v'',y' handles the supremum correctly. Averaging over shifted boxes in (12.16) is valid for nonnegative functions.

In Proposition 12.7, the small-phi range forces R >= P^(1-epsilon), giving the b < 2n/3 saving. In the larger range the endpoint optimization yields the stated three positive savings. The phi factor in the small-phi case makes the infinitely many dyadic intervals summable. With n = 10, rho >= 8 and b = 20/3-gamma, a positive saving remains after eta and epsilon are chosen small. This closes the contradiction.

### Pages 58–66: Appendix A and references

The supplied RS22 proof uses exactly the projectivized singular support and its fibre-dimension loci, so Proposition A.7 is justified with r=n-2 and c=i. Lemma A.8's coefficient-sequence induction uses the correct surjectivity in the preceding degree; finite groups give the required Mittag–Leffler condition. The supplied HY18 text proves generic specialization of relative singular support over an excellent Noetherian base, which includes an open subscheme of Spec Z. The supplied Bei16 results give purity of dimension, base-field compatibility, the support property, and characteristic-zero Lagrangian components.

The sandwich Gamma subset Sigma subset S is valid. Lemma A.12 uses biduality at a smooth rational point of the dual; the contact fibre is a rational linear space contained in V. This remains valid for integral but geometrically reducible V, since a smooth point belongs to a single geometric component. The three cases of Proposition A.13 give the extra rational codimension, rather than just geometric codimension. This supplies precisely the rational-point improvement used in Section 10.

## Corrections and external dependencies

No substantive repair is required by my review. Two bibliographic/expository points should be tidied:

1. On page 62, the HY18 citation is to part (2) of Theorem 5.2 and Theorem 5.3. In the supplied preprint, existence is Theorem 5.4 (or the projective Theorem 5.3), while the required specialization equality is Theorem 5.8, equation (5.8.1). The mathematical result is present; the numbering should be reconciled with the version actually cited.
2. On page 59, the statement that RS22 only explicitly discusses coefficient exponent r=1 is unnecessary for the supplied RS22 version: it explicitly permits a prime power modulus. The manuscript's own coefficient argument is valid in any event.

Substantive outside inputs not supplied for independent source verification include Bernert's absolute convergence and positivity result, BHB09's integral and differencing estimates, the Pila and Vermeulen uniform counting theorems, the classical local-solubility/density results, and the stated delta-method formula. I inspected their uses and found no hypothesis mismatch apparent from the manuscript. These are external dependencies, not detected gaps in the new argument.
