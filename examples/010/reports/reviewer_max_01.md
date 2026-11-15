REJECT

I reviewed the supplied version of *Frege's election method: discrepancy, invariant polygons and Farey geometry* under the stated condition that the printed reasoning must stand without repair. I found two local defects in the written arguments. The first concerns the claimed applicability of a background discrepancy example to every online algorithm; the second is a use of a lemma outside its stated hypotheses in the even-wall proof. These are the reasons for this verdict. I found no further substantive mathematical error in the main discrepancy, attractor, polygon-construction, or wall-classification arguments during this review.

1. Example 2.7 assumes distinct successive winners when extending the example to arbitrary online algorithms.

   Exact references: Example 2.7, PDF page 11, equations (2.28)–(2.29); TeX lines 1596–1614. In particular, the inference at lines 1598–1606 and the final sentence at line 1614 are at issue. The relevant definition of an online algorithm is in TeX lines 1539–1548.

   The example instructs us to split the votes evenly among candidates who have not yet been elected. It then says that, after numbering candidates in their order of election, at round \(t\) there are precisely \(m-t+1\) such candidates, with proportions given by (2.28). This requires that the first \(t-1\) elections have had distinct winners. That condition is valid for the Frege trajectory in this example, but is not a condition in the manuscript's definition of an arbitrary online algorithm.

   A concrete failure of the asserted universal calculation occurs with \(m=4\) and the online algorithm \(E(t)=1\) at every round. Following the example's stated rule of sharing votes among all candidates not yet elected gives
   \[
   \mathbf p(1)=(1/4,1/4,1/4,1/4),\qquad
   \mathbf p(2)=\mathbf p(3)=(0,1/3,1/3,1/3).
   \]
   Candidates 2, 3, and 4 are all still unelected before round 3. Thus each has terminal discrepancy
   \[
   z_j(3)=\frac14+\frac13+\frac13=\frac{11}{12},
   \qquad j=2,3,4,
   \]
   whereas the value asserted by (2.29) is
   \[
   h_4-1=\frac14+\frac13+\frac12=\frac{13}{12}.
   \]
   No renumbering makes the first three elected candidates distinct for this algorithm. In particular, the third-round denominator in the stated procedure is 3, whereas (2.28) uses 2.

   The defect is the universal inference in the example, not a numerical slip in the harmonic sum. Its effect on the written argument is that the displayed construction and calculation do not establish the claimed application to every online algorithm. The calculation for Frege's method remains valid. The cited worst-case lower bound (2.24) and the paper's new fixed-vote sharpness theorem have different logical status: the counterexample above concerns the example's asserted universal finite-time calculation, and the fixed-vote theorem has its own induction proof in Section 4. I have not supplied an amended adversarial construction.

2. The even-wall proof of Theorem 11.41 invokes Lemma 11.40 at an endpoint outside that lemma's parameter domain.

   Exact references: Theorem 11.41, proof for even walls, PDF page 86, paragraph immediately after (11.247); TeX lines 8121–8125. Compare the hypothesis of Lemma 11.40 at TeX lines 7932–7938 and the definition of the open parameter triangle \(\Delta\) at lines 5212–5215. The endpoint formulas are (11.239), (11.246), and (11.247), corresponding to TeX lines 7979–7987 and 8108–8118.

   The paragraph states that the smaller-denominator Farey parent is the unique fraction of smallest denominator in \([\alpha,\beta]\), and concludes, “by Lemma 11.40,” that \(K_{u/v}\) belongs to no open Farey cell. Lemma 11.40 assumes \((p,q)\in\Delta\), hence \(0<q<p<1-p-q\). That hypothesis fails for some even-wall endpoints covered by the theorem.

   For example, take \(u/v=1/4\), with Farey parents \(0/1\) and \(1/3\). The printed endpoint formulas give
   \[
   q(K_{1/4})=\frac{2}{3\cdot4\cdot1}=\frac16,\qquad
   p(K_{1/4})=\frac14-\frac1{3\cdot4\cdot1}=\frac16.
   \]
   Therefore \(K_{1/4}=(1/6,1/6)\), so \(q=p\) and \(K_{1/4}\notin\Delta\). Its Farey coordinates are \((\alpha,\beta)=(0,1/2)\), whose smallest-denominator fraction is \(0/1\); the lemma is expressly formulated for the open parameter domain where \(\alpha>0\). More generally, the same domain failure occurs for the endpoint associated with \(1/v\) when \(v\ge4\) is even.

   Thus the cited lemma does not justify this step for all the endpoints in the even-wall proof. This is a local hypothesis-checking gap, rather than a typographical error: all displayed coordinates are consistent, but they explicitly violate the invoked hypothesis. Its effect is on the printed justification of the endpoint assertion used before the concluding segment/cell argument. I found no conflicting endpoint formula or counterexample to the statement of Theorem 11.41. I have not extended the lemma or inserted a separate boundary-case proof.

Review coverage and checks

I read the entire supplied TeX source, lines 1–9078, including the abstract, introduction, all theorem statements, every proof, examples, remarks, open problems, the final discussion of divisor methods, and the complete bibliography. I also examined all ten figures as rendered in the matching 96-page PDF, on PDF pages 54, 55, 58, 60, 68, and 81. The references above use the theorem and equation numbering in that PDF and exact locations in the supplied TeX source.

My mathematical review covered the following argument chains:

- The lower discrepancy bound, the backward-looking sets \(A_t\) used for the harmonic upper bound, the equality characterization, the fixed-vote strict inequality, the inductive fixed-vote sharpness construction, and the monotone-deficit estimates establishing the restrictions near the supremum. I also checked how the supremum event is passed to a fixed numbering in the random-vote estimate.

- The extension to arbitrary initial conditions, uniform absorption of compact sets, backward invariance for the multi-valued map, the torus projection and subgroup description, and both rational-periodicity results. The rational statement with an arbitrary starting point is correctly limited to an eventual period divisible by \(Q\).

- The ergodic attractor proof, including the small neighborhood with unique lifts, finite covering of the torus, compactness and absorption, uniqueness of the compact invariant set, and the almost-everywhere one-point fibers. I checked the invariant-measure argument and the empirical-measure convergence separately, as well as the finite-branch reduction and the passage from the support of Lebesgue measure to every branch limit set.

- The full-dimensional block argument, particularly the tree of independent difference-form normals and the rational-independence contradiction. I checked its use in the finite union of full-dimensional polytopes and the subsequent support and limit-set conclusions.

- The intermediate-case examples and multiplicity discussion, the asymptotic-bias formulation, the two-party description, and the divisor-method reformulation.

- The planar coordinates and sectors, the first stability domain, Farey rectangles and first-entry word, the ordering of the \(W_j\), the upper and lower polygonal paths, sectional proof of invariance, the separate boundary-invariance argument, area identities, stability domains, vertex counts, explicit \(1/3\)-cell polygons, first-wall equations, even- and odd-wall continuation arguments, endpoint formulas, and adjoint pairing.

I performed independent exact-arithmetic checks using ordinary Python and rational numbers:

- The two ceiling recurrences used in the odd-wall proof, (va9a) and (va9b), and the adjoint endpoint identities were checked for all 3,428 reduced fractions in \((0,1/2)\) with denominator at most 150.

- For all 982 open Farey cells with denominator at most 80, I enumerated the nonempty intersections defined by the printed even- and odd-wall equations. Across 6,909 such intersections, their reduced intercepts, parity, canonical first-wall slope, and extent relative to the stated endpoint agreed.

- At one rational parameter point in each of \(S_{1/2}\), \(S_{1/3}^{(1)}\), \(S_{1/3}^{(2)}\), and \(S_{1/3}^{(3)}\), I computed polygon areas and centroids directly from the printed cyclic vertex lists. The areas had absolute value 1, the listed vertex counts were 11 or 15 as appropriate, and the resulting biases matched the corresponding displayed formulas exactly.

- The discrepancy calculation and endpoint-hypothesis failure in findings 1 and 2 were also checked exactly.

These computations were finite checks; the general arguments were assessed from the manuscript itself. I used no external mathematical sources, other versions, other reviews, private records, or formal proof assistant. Bibliographic and historical claims were read as part of the manuscript; their external sources were not inspected.

The rejection is specifically a judgment of the supplied reasoning under the no-repair condition. The report identifies the two defects and their limited scope without replacing either printed argument.

