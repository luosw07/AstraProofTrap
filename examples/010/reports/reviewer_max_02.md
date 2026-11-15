REJECT

I found two local mathematical defects in the supplied manuscript: an unjustified extension of Example 2.7 to arbitrary online algorithms, and an unqualified zero-bias assertion that is false for the fixed tie conventions permitted in the paper. Under the required no-repair condition, these must be reported even though they are peripheral to the three main results. The first concerns a printed argument; the second concerns the statement of a remark. My review of the remaining proofs did not identify a substantive error in the fixed-vote discrepancy results, the ergodic attractor results, or the planar Farey classification.

I read all of `paper.tex`, lines 1–9078, in bounded consecutive chunks, including every proof, example, remark, and bibliography entry. I also inspected all eight supplied external figure assets, read the two embedded TikZ figures in the source, and cross-checked the passages discussed below against the matching 96-page PDF. I used only the assigned manuscript and its assets as mathematical input. I did not consult external sources, other versions, other reviewers, or a formal proof assistant. References below give the printed numbering where checked, together with exact TeX locations or labels.

1. **Example 2.7 does not justify its final extension to every online algorithm.**

   Reference: Example 2.7, TeX label `E1`, lines 1595–1614, especially the renumbering at lines 1598–1599 and the sentence at line 1614; displayed equation (2.29), lines 1610–1612. The preceding general lower-bound claim is equation (2.24), TeX label `b3`.

   The example prescribes, at times $t=1,\ldots,m$, equal votes among candidates who have not yet been elected. It then numbers candidates in election order and writes the number of unelected candidates as $m-t+1$. This calculation uses the fact that a new candidate is elected in every round. That holds for the greedy Frege rule on this input, but an arbitrary online algorithm may repeatedly elect an already elected candidate. Renumbering does not turn repeated wins into wins by distinct candidates. Thus the displayed vote formula and harmonic-sum calculation do not extend to the full class asserted in the final sentence.

   A concrete check exposes the failure of the finite experiment as stated. Take $m=6$, and let the online algorithm elect party 1 in each of the first six rounds. Following the example's adaptive instruction, the first-round vote vector is $(1/6,\ldots,1/6)$; in rounds 2–6 it is $(0,1/5,1/5,1/5,1/5,1/5)$. For any other party $j$,

   $$
   z_j(t)=\frac16+\frac{t-1}{5}\qquad(1\le t\le6).
   $$

   Consequently the largest positive discrepancy anywhere in the prescribed six rounds is $7/6$, whereas $h_6-1=29/20$. In particular, the harmonic equality at time $m-1$ does not hold. Party 1 has negative discrepancy throughout, so it does not supply the missing positive discrepancy.

   Effect on the written argument: the final generalization in Example 2.7 omits the case of repeated winners and is invalid as printed. Effect on the statements: this is not a counterexample to the cited supremum-over-all-inputs theorem (2.24); it shows that this particular finite construction, with its printed reasoning, has not established that theorem for arbitrary online algorithms. The example remains valid as a sharpness example for Frege's greedy rule, and its later use in the Frege equality analysis is unaffected. I have not supplied a replacement argument for the arbitrary-online assertion.

2. **Remark 10.2 states zero asymptotic bias without hypotheses that exclude its counterexamples.**

   Reference: Remark 10.2, TeX label `RFrege2`, lines 4954–4970, particularly lines 4968–4970: the largest-remainder and Sainte-Laguë methods are said to have asymptotic bias $0$ “for any $m$.” The relevant definition is the fixed-vote Cesàro bias in Section 9, equation with TeX label `bias`; compare the paper's own Example 9.2, lines 4744–4761, especially equation (9.5), label `bias2`.

   With the paper's allowed fixed tie conventions, the unqualified assertion is false. Let $m=2$, $p_1=p_2=1/2$, and give party 1 priority at ties. For both named methods,

   $$
   r_1(n)=\lceil n/2\rceil.
   $$

   Its seat excess is $1/2$ for odd $n$ and $0$ for even $n$, so its asymptotic bias, in the paper's definition, is $1/4$. This also agrees with the paper's own formula $1/(2Q)$ at $Q=2$, combined with the two-party identification in the same Remark 10.2. The issue is not confined to two parties: equal votes for three parties and fixed priority give party 1 excesses $2/3,1/3,0$ in successive residue classes, with mean $1/3$, for both named methods.

   Effect on the written text: the comparison with other methods in Remark 10.2 asserts a false general conclusion under the manuscript's stated conventions. It is a missing mathematical qualification, not a harmless typo. Effect on the main results: the ergodic bias theorem explicitly assumes ergodicity, and this counterexample does not affect that theorem or its polygon-integral calculation. I have assessed the remark as printed rather than adding an unstated restriction on votes or tie handling.

The two issues above are the reasons for the verdict. They do not concern a numerical slip, an alternate convention for a polygon boundary, or the manuscript's explicitly announced shorthand of treating a singleton as a point.

The following describes the substantive coverage of the rest of the review.

The discrepancy proofs in Sections 3–4 were checked through the future-winner sets $A_t$, the two cases in the induction, the equality analysis, the periodic induction constructing nearly extremal fixed votes, and the monotone loss $L(t)$. The arithmetic producing $C_m=2m(m-1)$, the passage from a supremum to a fixed numbering in the random-vote corollary, and the strict fixed-vote supremum argument are consistent. The repeated-winner issue above belongs to the arbitrary-online comparison, not to these greedy-rule arguments.

For Sections 5–8, I checked the boundedness and compact absorption arguments, backward invariance of the multivalued limit set, the torus projection and finite-component structure, and the rational-period statements. In the rational case the paper proves exact period $Q$ for the stated small initial states and divisibility by $Q$ for a general eventual period; the stronger claim is correctly left as an open problem. In the ergodic case, the small-neighborhood lifting argument is used consistently to obtain finite absorption and uniqueness. The invariant-measure proof explicitly treats exceptional projection fibers, and the empirical-distribution proof uses compact sets and the Portmanteau inequalities in the correct direction. The proof of the good-block lemma includes the integer term in its rational-independence argument and the restriction on the final edge of the marked-tree path. These steps support the stated full-dimensional polyhedral structure and the passage from measure support to every branch limit set. The intermediate-case theorem uses Haar measure on the whole compact coset, including its finite components, and the examples distinguish multivalued from fixed-priority invariance.

For Section 11, I checked the coordinate change, the first stability domain, the Farey rectangle description, the no-small-denominator argument, first entry of the distinguished orbit, the ordering of the $W_j$, and the upper and lower zig-zag construction. The invariant-polygon proof uses the $g$-sections to account for the side-piece images, and separately accounts for the middle piece. The boundary proof expressly checks the extra tied segments that can arise in a limit, rather than relying solely on continuity of the discontinuous map. The classification of internal walls follows from the specified cut vertex or cut segment, and the vertex count distinguishes cutting at a vertex from cutting inside an edge.

I also checked both parity cases in the global wall argument, including the closest-small-denominator comparison for even walls, the determinant/parity deductions for odd walls, preservation of the relevant parent and word entries at a cell crossing, the endpoint calculations, and the adjoint-fraction pairing. I found no invalid inference in those printed arguments. The final divisor-method reformulation follows from the displayed weighted maximization and uniform shift.

As independent arithmetic checks, I reconstructed the invariant polygons with exact rational coordinates at the four parameter examples $(321/1000,262/1000)$, $(17/50,3/50)$, $(7/25,1/25)$, and $(1/5,2/25)$, and at the displayed $4/11$-cell example $(9/25,1/200)$. Their areas are $1$, their vertex counts are respectively $11,15,15,15,47$, and the polygon first moments agree with each of the four printed bias formulas at the corresponding test point. I also checked the two ceiling identities in the odd-wall proof for all reduced $u/v\in(0,1/2)$ with $v\le100$, and checked the printed determinant/parity conclusions at all 5,344 candidate odd-wall equations intersecting those open Farey rectangles. Those checks produced no discrepancies. These were finite arithmetic checks alongside the reading of the general proofs.

The bibliography was read as part of the manuscript; the historical claims and cited sources were not externally verified, in accordance with the assignment. The report identifies the two mathematical defects found in the supplied version and leaves their correction to the authors.
