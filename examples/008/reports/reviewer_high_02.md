# Independent mathematical review

**Verdict: ACCEPT.**

I found no substantive mathematical error in the supplied manuscript. The main counting estimate, its statistical consequences, and the application arguments are supported by the proofs given, subject to the external results explicitly invoked by the paper.

## Coverage

I read the entire supplied 67-page manuscript through its extracted text, including Sections 1–9, the references, and Appendices A–C. I checked the arguments rather than relying on the authorship or publication status. I also consulted the supplied complete Bennett–Bohman reference, especially its Section 2 and the degree and edge-count analyses in Section 3. I rendered and inspected manuscript page 22 and reference page 4 to resolve the scope of the square roots in the degree-error formulas. I used no web sources, other manuscript versions, other reviews, or discussions with other reviewers.

My most detailed checks concern the new arguments in Sections 4–7. I also checked the application encodings, exponent comparisons, and appendix calculations. The other cited external theorems, notably the matroid comparison from [59], were treated as external inputs as stated; their original sources were not supplied for this review.

## Main proof checks

1. **The external random-greedy input is correctly used (page 22, Theorem 4.3).** In the supplied Bennett–Bohman paper, page 4, the degree error is
   \[
   e_d=\sqrt{6rLD\log N}\,(1-r\log p).
   \]
   Thus on the fixed interval \(p\geq 1/2\) it is \(O_r(\sqrt{DL\log N})\), as asserted in the manuscript. Bennett–Bohman's hypothesis is \(L=o(D/\log^5N)\), and their Theorem 2.1 places the stopping fraction at \(O(((L/D)\log^5N)^{1/(2(r-1))})=o(1)\). This indeed covers the half-vertex stopping time. No polynomial lower bound on \(D\) in terms of the current order is needed for this application.

2. **Regular completion and weighted transfer work (page 21, Lemma 4.2).** The auxiliary construction fills each old degree deficit once in every old copy and gives every new vertex degree \(D\). Separate auxiliaries for separate stubs preserve pair codegree at most one on every pair involving a new vertex; added edges contain only one old vertex. Consequently the asserted higher-codegree bounds hold. Recording incident added matching edges at new vertices gives an injective encoding. Its possibly repeated activity charges dominate each added edge's weight for both \(\lambda\leq1\) and \(\lambda>1\).

3. **The short-trajectory higher-codegree estimate is justified (pages 22–25, Lemma 4.5).** Continuing to count edges after the fixed set \(S\) is removed avoids a large jump from removal of \(S\) itself. The survival probabilities for vertices of \(e\setminus S\) still have the stated degree-based estimates. Dividing by \(g_i\) exactly removes the linear drift. The increment bound \(O_k(L_{j+1})\) and total conditional variance \(O_k(L_jL_{j+1})\) give the claimed Freedman threshold and allow a union bound over all fixed sets.

4. **The counting iteration retains the required normalization (pages 25–32, Lemma 4.6 and Theorem 4.1).** The factorial for ordering prefixes and the binomial bound for the number of prefixes contained in a full matching address distinct multiplicities. I checked the main-term cancellation in (4.6)–(4.8), including the remaining \((N/k)\log2\) term. A completion has a larger order, but its normalized remainder enters with coefficient \(N_{i+1}/(a_iN_i)\), whose accumulated product is \(O(2^{-i})\). Thus the large auxiliary orders do not multiply the original error. The deterministic codegree recurrence, stopping scale \(p_T\asymp\Gamma(H)\ell^B\), and bounds \(\log N_i=O_k(\ell^2)\) verify the hypotheses of the cited greedy theorem at every stage. Summing the three cases \(j=2\), \(j=3\), and \(j\geq4\) in (4.12) gives the stated polylogarithmic multiple of \(n\Gamma(H)\).

5. **The entropy reconstruction and refined correction are consistent (pages 34–43).** In Lemma 5.4, conditional on the first-exposed vertex of its own block, an alternative meeting \(m\) blocks requires the other \(m-1\) whole blocks to remain unexposed. This explains the exponent \(k(m-1)\), and the change of variable \(y=u^k\) explains the factor \(1/k\). The intersection incidence identity (5.4) supplies exactly the stated coefficients. Lemma 5.2 controls the singular integral near zero with sufficient polynomial margins. In Lemma 5.6, multiplying by \(\theta\) before changing variables makes the error uniform even for small deletion probability. The tangent bound in Lemma 6.1 cancels the unknown original vacancy density. With \(T=d\) and \(\theta=(\lambda d)^{-1/k}\), the remaining gain is \(n(\lambda d)^{-1/k}\) to first order. For the upper bound, the degree-loss identity (6.8), Shearer's inequality, and the edge weights in (6.10) give the required cancellation with the same coefficient one.

6. **The statistical deductions use adequate error control (pages 44–48).** The proof uses exponential moments rather than differentiation of an asymptotic error. The uniform error in (7.1) is independent of the tail threshold, so integration of the tail bound proves the asserted second-moment convergence. In the large-deviation lower bound, choosing the tilted target strictly beyond the requested threshold ensures containment of the concentration interval in the desired tail event. The probability-ratio calculation has the correct sign and gives rate \(x\log x-x+1\).

## Applications and appendices

The Latin-square, transversal, and toroidal-queens encodings have the claimed degrees, orders, and codegrees. The vacancy-to-deficit factors agree with the displayed constants. For fixed Steiner systems, the coprimality condition provides the strict pattern exponent required in Corollary 2.4. In the set and subspace design applications, the counts of nonsingleton intersections, the bounds obtained by determining a candidate from two intersections, and the stated exponent inequalities provide positive margins in (1.4).

In the matroid argument, the cost of a large hyperplane is charged through the size of its shadow. The first term of the resulting sum has order \(n^{(r+1)/2}\); the ratio estimate in Claim 8.5 makes the whole sum of this order. This is smaller than \(n^{r-1-1/r}\) for every \(r\geq4\). Appendix C supplies the maximum-degree version required after deleting these shadows: the added singleton terms in Shearer's inequality account for the degree deficits, and their final coefficient is negative for sufficiently large \(d\).

Appendix A's marked-edge deletion identity, regularity calculation, and bound \(\mathbb E T^2\leq q^3\) give the asserted counterexample. The lifting construction and vacancy comparison in Appendix B have the stated degrees, orders, codegrees, and direction of inequality.

I have no mathematical correction to request on the basis of this review.
