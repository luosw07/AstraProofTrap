# Independent mathematical review

**Verdict: ACCEPT**, with the local correction to the completion construction described below.

I find the main counting and statistical arguments mathematically sound. In particular, the supplied Bennett–Bohman reference supports the fixed-fraction degree estimate used here, including its logarithmic dependence on the order. I found one explicit, readily repairable construction error on page 30. The repair uses the completion lemma already proved in the paper and leaves all theorem statements and estimates intact.

## Scope and method

I read the complete current manuscript, pages 1–67, in successive chunks, including Sections 1–9, all three appendices, and the references. I checked the main proof chain in Sections 4–7, the parameter and intersection-pattern calculations in Section 8, and the arguments in Appendices A–C. I also read the complete supplied Bennett–Bohman text and consulted rendered pages 21, 22, and 30 of the manuscript and page 4 of that reference to resolve the finite-field choice and the scope of square roots in the degree errors. I used only these supplied task-specific sources; I did not consult other versions, reports, agents, or the web.

For external results other than Bennett–Bohman, my review checks their use in the forms stated by this manuscript. I have not independently verified their original sources; this includes the cited paving-to-general-matroid comparison on page 55. The assessment below concerns the mathematical arguments and their deductions, rather than an independent audit of all historical and bibliographic assertions.

## Local mathematical correction

**Page 30, proof of Theorem 4.1, paragraph beginning “Choosing the constant in (4.9)…”:** the instruction to use Lemma 4.2 with “Q the least prime power” is inconsistent with the construction actually proved on page 21, which chooses a **prime** Q.

This distinction matters for the displayed auxiliary edges

\[
\{(j,b+ja):0\le j<k-1\}.
\]

With a nonprime field order, the integer coefficients j need not be distinct field elements. For example, take k = 4 and Q = D = 4. In characteristic two, the coefficients 0 and 2 are equal. For any fixed b, all four auxiliary edges indexed by a in F_4 contain both (0,b) and (2,b). Their pair codegree is four, whereas the construction is supposed to be linear. Appending their respective old vertices does not remove this repeated pair. The same failure occurs for arbitrarily large powers of two when these integer coefficients are used. I also checked the Q = 4 example by direct enumeration.

**Correction:** replace “least prime power” on page 30 by “least prime.” The choice Q = O_k(D_{i+1}) remains available, all coefficients 0 through k−2 are then distinct, and the construction of Lemma 4.2 applies exactly as proved. The degree D_{i+1} remains the same for every prefix, and the order bound and all subsequent error estimates are unchanged. Alternatively, the construction could explicitly use k−1 distinct field elements as its coefficients, but changing the page-30 word is the simplest repair.

I treat this as a minor local correction because the manuscript already proves the required completion lemma with the valid prime choice; no new estimate or hypothesis is needed.

## Checks on the main proof

### The external degree estimate and the iterative counting argument

Theorem 4.3 (page 22) is a valid fixed-fraction consequence of Bennett–Bohman, Theorem 2.1. On page 4 of the supplied reference, the assumptions are

\[
L=o(D/(\log N)^5),
\qquad e_d=\sqrt{6rLD\log N}\,(1-r\log p).
\]

Their stopping estimate places the first failure at a remaining fraction of order
\((L/D)^{1/(2(r-1))}(\log N)^{5/(2(r-1))}=o(1)\).
Thus the process reaches p = 1/2 with the asserted degree control, and throughout that interval the error is O_k(sqrt(D L_2 log N)). In particular, the reference does not impose a polynomial lower bound on D relative to N in this application.

I checked Lemma 4.5's use of the extended codegree variable: continuing to count edges after vertices of the fixed set S are removed avoids the large jump that would invalidate the stated bounded-increment argument. The one-step drift, integrating factor, variance bound O_k(L_j L_{j+1}), and union bound over sets give the displayed codegree estimate.

In Lemma 4.6, both multiplicity divisions are needed and correctly used: m! forgets the prefix ordering, while binomial(N/k,m) controls how many prefixes an extended matching can contain. The prefix and residual main terms leave precisely (N/k) log 2, canceled by this latter factor. The completion encoding gives the claimed weighted transfer inequality, including for activities below one.

The subsequent normalization addresses the increase in the auxiliary orders correctly. Claims 4.3–4.5 give log N_i = O_k((log n)^2), while the stronger bound on L_2^(i)/D_i makes the Bennett–Bohman hypothesis valid at every stage. The product of remainder coefficients is O(2^(−i)), independent of the large absolute order N_i. The final sum in (4.12) has the right three cases: a bounded geometric sum for j = 2, a factor T for j = 3, and a terminal-scale bound for j >= 4. Together with p_T asymptotic to Gamma(H) times a fixed logarithmic power, this proves the stated error in Theorem 4.1 after the prime-choice correction above.

### Exposure, reconstruction, and the refined partition function

I checked the random-order argument in Lemma 5.4. Conditional on v being the highest-priority vertex of its own matching block, an alternative meeting m matching blocks is available with probability u^(k(m−1)). The substitution y = u^k, including its 1/k factor, is correct. The incidence identity in (5.4) justifies replacing vertexwise pattern counts by their averaged coefficients.

The integral estimate in Lemma 5.2 has the required o(d^(−1/k)) precision. Both the q = 1 logarithmic case and the q >= 2 power case are absorbed by the polynomial margin on b_pi. Lemma 5.5 correctly retains the degree-loss term. In Lemma 5.6 the deletion probability is theta^m for a pattern with m blocks, and the substitution in (5.13) makes the reconstruction error uniform even when theta tends to zero.

The thinning calculation in Lemma 6.1 retains the source-vacancy contribution (np/k) log T. The binary-entropy tangent bound controls the unknown p with the correct sign. Setting theta = (lambda d)^(−1/k) and T = d, and applying Theorem 4.1 at activity lambda d, gives the claimed lower correction.

For the upper bound, the identity S_W = k times the number of edges meeting W minus d|W| is exact. Shearer's inequality and the chosen subset weights give the cancellation in Claim 6.2, with error O(n(lambda d)^(−2/k)). I found no missing assumption about the vacancy law in this step.

### Matching statistics

Section 7 uses activity changes instead of differentiating an uncontrolled asymptotic error. The uniform exponential-moment estimate yields a deviation bound with an error independent of the tail threshold, which is sufficient for the second-moment integration. The large-deviation lower bounds correctly tilt to a value strictly beyond the desired threshold and then shrink the neighborhood. The rate x log x − x + 1 and the normalization n d^(−1/k) follow with the stated constants.

## Applications and appendices

The Latin-square, transversal, and toroidal-queens encodings have the stated orders, degrees, uniformities, and vacancy conversion factors. The toroidal-queens pair codegree bound of two handles even orders as well.

For fixed Steiner systems, the higher-codegree estimates give the claimed Gamma bound, and coprimality supplies the strict margin in the intersection-pattern exponent. For partial set designs with block size t+2 or t+3, I checked the restrictions on nonsingleton intersections, the candidate-block counting bounds, and the strict exponent inequalities. The corresponding subspace argument uses spans and annihilators appropriately; its Gaussian-binomial inequalities provide the required strict margins in the stated parameter ranges.

The paving-matroid upper bound correctly deletes the shadows of large hyperplanes and applies the maximum-degree result rather than assuming residual regularity. The ratio estimate in Claim 8.5 makes the additional sum O_r(n^((r+1)/2)), which is smaller than n^(r−1−1/r) for r >= 4. The final expansions have errors of smaller order than the displayed correction. The passage to all matroids uses the external comparison identified in the coverage statement.

Appendix A's regular construction, marked-edge identity, second-moment bound, and symmetry argument establish its counterexample. Appendix B's lifting has the claimed degrees, pair codegrees, order, and matching-number inequality. Appendix C correctly supplements Shearer's cover with singleton copies for degree deficits; the resulting extra coefficient tends to −1/k, giving the required uniform maximum-degree bound.

Overall, the supplied reference verifies the crucial external input, and the internal deductions support the principal results. The identified prime-power slip should be corrected as specified.
