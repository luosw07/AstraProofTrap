# Independent mathematical review

**Verdict: ACCEPT.**

I found no substantive mathematical error in the supplied paper. This verdict concerns its mathematical argument, with the explicitly cited external results taken as inputs.

## Coverage

I read the supplied extracted text across the whole paper, including the main results, Sections 3–8 and Appendices A–C. The principal checks were the regular-completion construction and weighted encoding; the stopped higher-codegree martingales; the normalized iteration and its terminal error; the random-priority entropy argument; thinning and the cancellation of the unknown vacancy density; the exponential tilting argument; and the auxiliary hypergraph calculations for the applications. I also examined the concluding discussion and reference list. I did not consult external sources or independently verify the exact formulations of the cited results, particularly the Bennett–Bohman input in Theorem 4.3 and the matroid comparison quoted on page 55. No PDF rendering was needed for the mathematical expressions used in these checks.

## Findings

- **Pages 21–32, Section 4:** The completion has the asserted degrees and preserves higher codegrees: every added edge has one old vertex, and its new-vertex pairs come from a linear auxiliary hypergraph. The weighted encoding is an upper bound for every positive activity. The trajectory variable in Lemma 4.5 continues counting after its distinguished set is removed, avoiding a large jump from that removal. Its drift and quadratic-variation estimates support the stated bound. In the iteration, the coefficient is the completion order divided by the number of copies and the previous order, not the completion order alone. Its product is controlled by the original residual proportion. The sum over codegree levels and the terminal contribution have the asserted order after increasing the logarithmic exponent.

- **Pages 34–43, Sections 5–6:** The exposure probability is correctly based on entire matching blocks. Conditional on the current vertex being first in its block, an alternative meeting m blocks requires all vertices in the other m−1 blocks to have smaller priorities. The substitution y=u^k yields the factor 1/k. Averaged intersection coefficients suffice for the tangent and Jensen steps; no pointwise coefficient bound is silently assumed. The integral error remains uniform when the deletion probability tends to zero, because the truncated nonnegative integral is bounded by the full integral. The thinning calculation retains the original-vacancy contribution and cancels it using the entropy tangent inequality. In the upper bound, the exact lost-degree identity (6.8), together with Shearer's inequality and the chosen subset weights, supplies the coefficient one in the correction.

- **Pages 44–48, Section 7:** The proof obtains concentration and second moments through exponential moments rather than differentiating an uncontrolled asymptotic error. The tail bound is uniform in the deviation threshold, permitting integration. The lower large-deviation bounds use a tilted mean strictly beyond the target threshold, so the concentrated tilted event lies inside the required tail.

- **Pages 49–55 and 65–67:** The pattern-count arguments for set and subspace designs have strict exponent margins in the specified parameter ranges. For the matroid argument, the maximum-degree upper bound accounts for original degree deficits using singleton terms in Shearer's inequality. Its remaining deficit coefficient is negative for large degree. The large-hyperplane sum is dominated by its first term, of order n^((r+1)/2), which is below n^(r−1−1/r) for r≥4. Thus the errors fit the claimed correction scale.

- **Pages 63–65, Appendices A–B:** The counterexample's degree and pair-codegree calculations agree with its construction. The deletion identity gives E[T²]≤q³ and hence the asserted vacancy bound. The regular lifting preserves the stated codegree relation, and its matching projection yields the claimed conditional consequence.

The main qualification in coverage is the use of the external results as stated, rather than a source-level audit of those results. Within the supplied argument, I found neither a counterexample to a claimed assertion nor an unresolved internal step that changes the stated conclusions.
