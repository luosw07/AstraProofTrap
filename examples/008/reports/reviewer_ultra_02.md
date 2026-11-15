# Independent mathematical review

**Verdict: ACCEPT.**

I find the main counting theorem, its statistical consequences, and the application arguments mathematically sound. There is one minor construction specification that should be corrected: the choice of a “prime power” on page 30 should remain a choice of a prime, as in Lemma 4.2. The correction is immediate and preserves every estimate. I explain the precise issue below.

## Scope and sources

I read the entire supplied 67-page manuscript, including the introduction, all proofs in Sections 3–8, the concluding discussion, references, and Appendices A–C. I also read the supplied complete 12-page Bennett–Bohman reference and checked the precise theorem and error function used by the manuscript. I inspected rendered manuscript pages 21, 22, 30, 46, 53, and 57, and rendered page 4 of Bennett–Bohman, to resolve mathematical notation and verify the relevant displays.

The review used only the current manuscript and the supplied Bennett–Bohman reference. Other externally cited results were assessed as quoted inputs; in particular, I checked the use and error size of the Pendavingh–van der Pol comparison in the matroid application, but did not independently verify that comparison against its original source. I did not browse, consult other manuscript versions, or communicate with other reviewers.

## Minor correction: the field used for regular completion

**Location:** page 30, proof of Theorem 4.1, the paragraph following the verification of the Bennett–Bohman hypothesis, beginning “Choosing the constant in (4.9)…”; compare Lemma 4.2 on page 21.

Lemma 4.2 correctly chooses a **prime** $Q\geq\max\{D,k-1\}$. Its auxiliary edges are

\[
\{(j,b+ja):0\leq j<k-1\},\qquad b\in\mathbb F_Q,\ a\in A.
\]

With prime $Q$, the elements $0,\ldots,k-2$ are distinct in the field, so two different coordinate classes determine at most one pair $(a,b)$. This proves the required linearity and hence preservation of the higher-codegree bounds.

Page 30 instead says to use “$Q$ the least **prime power** at least \(\max\{D_{i+1},k-1\}\).” The construction written in Lemma 4.2 does not work with arbitrary prime powers if $ja$ has its usual integer-scalar meaning. For example, for $k=4$ in characteristic two, $0a=2a=0$. For a fixed $b$, all $D$ auxiliary edges indexed by the slopes $a\in A$ then contain both $(0,b)$ and $(2,b)$. Their pair codegree is $D$, rather than at most one. Thus the literal prime-power prescription can lose the codegree control asserted in the subsequent paragraph.

The simplest correction is to replace “least prime power” by “least prime.” This is exactly the construction already proved in Lemma 4.2, still has $Q=O_k(D_{i+1})$, and leaves the bounds $a_i=O_k(D_{i+1}^2)$, \(\log N_i=O_k((\log n)^2)\), and all later arguments intact. Alternatively, one can use prime powers while explicitly replacing the integer evaluation points by $k-1$ distinct elements of the field. I regard this as a local specification error with a complete repair already available within the paper, rather than a defect in the theorem or its mathematical strategy.

## Main proof checks

### Bennett–Bohman and the short stages

Theorem 4.3 on page 22 is a valid fixed-fraction consequence of the supplied reference. Section 2 of Bennett–Bohman, page 4, explicitly assumes

\[
L=o(D/(\log N)^5)
\]

and gives the degree error

\[
e_d=\sqrt{6kLD\log N}\,(1-k\log p).
\]

On $p\geq1/2$, this is $O_k(\sqrt{DL\log N})$, exactly as used in the manuscript. Its Theorem 2.1 puts the first failure at a remaining fraction

\[
O_k\left(((L/D)(\log N)^5)^{1/(2(k-1))}\right)=o(1),
\]

so the whole half-vertex interval is covered. The stronger superpolylogarithmic assumption in the reference's introduction and Theorem 1.1 is not needed for this application of its Theorem 2.1.

In Lemma 4.5, defining $Y_S(i)$ by survival of the vertices outside $S$, even after a vertex of $S$ is removed, correctly avoids a large deletion jump. The drift in (4.1), its removal by the factor $g_i$, and the stopped martingale in (4.3) are consistent. The bounds on increments and conditional variance give respectively $O_k(L_{j+1})$ and $O_k(L_jL_{j+1})$, which justify Claim 4.1 and its union bound.

### Counting and iterating regular completions

The encoding in Lemma 4.2 is injective, and the use of \(\max\{1,\lambda\}\) gives a valid weight upper bound both above and below activity one. The prefix count in Claim 4.2 and the multiplicity bound in (4.6) account for two distinct kinds of overcounting. I checked the leading terms: the remaining $N\log2/k$ is exactly canceled by the binomial multiplicity.

The normalization in Lemma 4.6 and Claim 4.6 is essential and is handled correctly. The coefficient propagated to stage $i$ is

\[
\prod_{h<i}\frac{N_{h+1}}{a_hN_h}
=2^{-i}\exp\left(O_k\left(\ell\sum_{h<i}\sqrt{L_2^{(h)}/D_h}\right)\right)
=O_k(2^{-i}).
\]

Consequently, growth of the auxiliary orders does not multiply the original normalized error. Claims 4.3–4.5 also verify the actual theorem hypothesis at those auxiliary orders: \(L_2^{(i)}(\log N_i)^5/D_i=o(1)\). For the final summation in (4.12), the cases $j=2$, $j=3$, and $j\geq4$ have the respective geometric, logarithmic, and terminal-scale behavior stated in the proof. The chosen stopping scale bounds all of them by \(\Gamma(H)\) times a fixed logarithmic power. The activity bounds remain uniform because \(|\log\lambda|+\log(D_i+1)=O_{k,C_0}(\log n)\).

### Entropy, thinning, and the coefficient one

In Lemma 5.4, the conditional entropy vanishes when the current matching edge has already been exposed. Conditional on its highest-priority vertex having priority $u$, an alternative meeting $m$ source blocks requires all vertices in the other $m-1$ blocks to have priority below $u$. The factor $u^{k(m-1)}$ and the change of variables $y=u^k$ are correct, including for nonsingleton intersections. The incidence identity (5.4) correctly matches the definition of $b_\pi(H)$.

Lemma 5.2 integrates the potentially singular small-$y$ error instead of using a pointwise approximation. Its bounds give the necessary $o(d^{-1/k})$ under (1.4). In Lemma 5.6, averaging over whole-edge deletions gives \(\theta^{m(\pi)}\), and dividing by the expected number of deleted vertices gives the stated \(\theta^{m(\pi)-1}\). Equation (5.13) establishes the claimed uniformity even for very small deletion probabilities.

The algebra in Lemma 6.1 retains the source-vacancy term \((np/k)\log T\). The binary-entropy tangent inequality then eliminates the unknown source vacancy with the correct inequality direction. With \(T=d\) and \(\theta=(\lambda d)^{-1/k}\), the error from Theorem 4.1 is below the required correction, proving the lower estimate.

For the upper estimate, the degree-loss identity (6.8) is exact. Shearer's inequality and the edge weights in Claim 6.2 give a first-order term $k(\lambda d)^{-1/k}$ per edge before division by $d$. The vacancy-dependent terms cancel as claimed, leaving coefficient one for \(n(\lambda d)^{-1/k}\). This verifies the delicate matching of the upper and lower corrections in Theorem 1.6.

### Statistical consequences

The activity identity (3.1) gives the limiting normalized log moment-generating function $e^s-1$. Proposition 7.1 controls the second moment by integrating tails with a single uniform partition-function error; it does not differentiate an uncontrolled asymptotic remainder. The tilted-law proof on pages 47–48 gives the matching lower bounds for both tails, with $y$ chosen strictly beyond the desired threshold. The resulting rate $x\log x-x+1$, the $L^2$ conclusion, and the perfect-matching upper bound follow.

## Applications and appendices

I checked the auxiliary orders, degrees, uniformities, and deficit translations for partial Latin squares, partial transversals, and toroidal queens. The bounded pair-codegree argument covers even toroidal orders as stated. The group-table and board symmetries used for pointwise vacancy conclusions preserve the relevant uniform measures.

For Corollary 2.4, the choice of the smallest number of largest intersection parts covering at least $t$ vertices gives $b_\pi=O(n^{h-1})$. The coprimality condition supplies the claimed strict exponent margin. For the set and subspace partial-design applications, I checked both the higher-codegree thresholds and the nonsingleton-pattern counts in Claims 8.1–8.4. In particular, two large intersections determine the candidate block in the stated $s=3$ cases, and the displayed inequalities on pages 51 and 53 give the required strict margins.

The maximum-degree extension in Appendix C correctly introduces singleton copies to complete the cover used in Shearer's inequality. The additional deficit coefficient tends to $-1/k$, so its contribution may be discarded in the required upper bound. This justifies applying Proposition 8.1 after deleting large hyperplanes. In the matroid calculation, the first large-hyperplane term has order $n^{(r+1)/2}$, the ratios in Claim 8.5 tend uniformly to zero, and this error is smaller than $n^{r-1-1/r}$ for every fixed $r\geq4$. The quoted comparison with all matroids has the smaller error $O_r(n^{r-2}\log n)$.

Appendix A's marked-edge deletion identity, exact regularity and pair-codegree calculation, and bound \(\mathbb E T^2\leq q^3\) establish its counterexample. Appendix B's lifting preserves the asserted degree and codegree parameters, and the vacancy-to-maximum-matching inequalities have the correct directions and exponents.

The acceptance judgment rests on these proof checks. The local prime/prime-power correction above should be made in the final text.
