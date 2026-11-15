OK

The planted change creates a genuine mathematical defect in the proof of Theorem TB. The supplied primary classification G2 is correct: the proof retains an existentially selected block after increasing the parameter through which that block was certified. The explicit permission to choose any block satisfying the finite condition matters. An admissible choice makes the final assertion false. The construction is sufficiently integrated and moderately subtle for the benchmark, although a reviewer tracking the two horizons carefully has a fairly direct route to detection.

## Scope and reading

I read the complete current `blind/a9c6/paper.tex` (all 9,078 lines, including the preamble, subsequent sections, and bibliography), the complete assigned private log, and the adjacent `mutation.json`. The paper was read in bounded chunks; a chunk that encountered output truncation was reread in smaller untruncated chunks. I did not inspect other experiment files or versions, consult external mathematical sources, delegate, or use a formal proof assistant. The paper's SHA-256 is `3de1e3c37e10f56e16af35e9c6c58e5145a0f74c9fa6fa68073cd37812eaa142`, matching the assigned record. I compared the original excerpts supplied in the record with their current mathematical context; I did not independently obtain an original paper.

## Exact location and original versus modified argument

The defect is in the proof of Theorem TB:

- Lines 4218–4220 first choose N satisfying (tinv5a), then choose **any** block of form (tb4) contained in N_delta whose iterates through N are finite unions of good blocks.
- Lines 4232–4233 increase N after that block has been fixed, to cover the torus by translates of pi(interior B).
- Lines 4257–4258 assert, “By the choice of B,” that every iterate in the resulting union through the enlarged N is a finite union of good blocks.

The final assertion is the precise false inference. Neither the initial existence statement nor the later compactness statement is individually false.

The original excerpt instead chooses the widths as in Lemma LTB. This requires the widths and the vote coordinates to be jointly rationally independent and gives goodness for every iterate of the selected block. Only afterward does the original proof obtain a finite cover horizon for that block. Its final application of LTB is therefore valid. The modified passage replaces this persistent witness property with a finite one and removes the final direct invocation of LTB.

The separate replacement at line 4440 restores pi(A intersect D) in the proof of Tmu. In the current context this is the correct projected exceptional set: nullity of A intersect D and the locally Lipschitz projection give its nullity. It is not a second new defect.

## G2 audit: implication, witnesses, and dependencies

Fix a positive ergodic vote vector p and 0 < delta <= 1/m. Write:

- C_delta(N0): the translates R_p^k(Nhat_delta), 0 <= k <= N0, cover the torus.
- F(B,L): for every integer n with 0 <= n <= L, T^n B is a finite union of good blocks.
- P(B,N0): B has form (tb4), B is contained in N_delta, and F(B,N0).
- C_B(M): the translates R_p^k(pi(interior B)), 0 <= k <= M, cover the torus.

The valid pre-selection implication is

    [p positive and ergodic, 0 < delta <= 1/m, C_delta(N0)]
        => exists B P(B,N0).

LTB proves this by supplying sufficiently small positive widths jointly rationally independent with p; such a stronger choice even satisfies F(B,L) for every L. This validates the modified existence claim. But the modified text selects an arbitrary witness of P(B,N0), not a witness expressly retaining that stronger property.

The existential variables and their actual dependencies are N0, then B (equivalently its widths), then M depending on B. Compactness provides C_B(M), and M can be increased to at least N0. Nothing in that step upgrades F(B,N0) to F(B,M). The proof subsequently uses precisely this extra property for the already selected B.

The desired theorem conclusion, that K* is a finite union of good blocks, does not depend on B. The intermediate proposed decomposition and its upper index do depend on B. Eliminating the existential B by proving a conclusion from its stated properties requires that the argument work for the witness allowed by those properties. It cannot use an additional all-iterate property available only for specially chosen witnesses. In particular, the following compatibility claim is false:

    For every B satisfying P(B,N0), there exists M >= N0
    satisfying both C_B(M) and F(B,M).

This is a G2 witness-dependence error. The enlargement of the universally quantified iteration range is its surface manifestation, not an independent G1 defect. The cited lemma's use to establish existence is valid, so MP is not the primary classification. The definitions and existence of the selected block and the cover remain valid, excluding DEF; no modified algebraic conversion is responsible, excluding CONV.

## Decisive admissible witness

Set

    m = 2, epsilon = sqrt(2)/1000,
    p1 = 1/4 + epsilon, p2 = 3/4 - epsilon,
    delta = 1/2, N0 = 1, rho12 = 4 epsilon.

Identify H_0 with x by (x,-x). Then ell_12(x,-x) = 2x and (tb4) gives B = [-2 epsilon, 2 epsilon].

All actual assumptions are satisfied. Both votes are positive and sum to one. If rational a,b satisfy a p1 + b p2 = 0, then (a-b)p1 + b = 0. Irrationality of p1 forces a=b=0, so p is ergodic in the paper's exact sense. The value delta=1/2 is permitted, and B lies strictly inside N_delta=(-1/2,1/2). Under the first-coordinate identification of the torus, Nhat_delta is the circle minus [1/2]. Its translate by p1 omits a different point, so the two translates cover the circle. Thus N0=1 really satisfies (tinv5a).

For m=2 every good block is a nondegenerate compact interval. By the unchanged formula (T1b), the multivalued scalar map is

    T1(x) = x+p1       when x+p1 <= 1/2,
            x+p1-1     when x+p1 >= 1/2,

with both values included at equality. The first shifted interval is

    B+p1 = [1/4-epsilon, 1/4+3 epsilon].

Since epsilon < 1/12, its upper endpoint is strictly below 1/2. Hence

    TB = [1/4-epsilon, 1/4+3 epsilon],

which is a good block. B and TB establish F(B,N0). The next shifted interval is exactly

    TB+p1 = [1/2, 1/2+4 epsilon].

The endpoint 1/2 has both branch values 1/2 and -1/2; every other point uses the subtract-one branch. Therefore

    T^2 B = [-1/2, -1/2+4 epsilon] union {1/2}.

Because 4 epsilon < 1, the point 1/2 is isolated. A union of nondegenerate intervals cannot have an isolated point: any interval containing that point also contains other arbitrarily nearby points. Consequently T^2 B is not a finite union of good blocks.

This witness does not satisfy LTB's stronger joint independence hypothesis: rho12 = 3p1-p2. That is not a violation of the modified selection, which requires the block's form and finite goodness condition, not joint independence. This distinction is exactly what the mutation changes.

No later admissible covering choice avoids the failed iterate. The projected interior of B has normalized Haar measure 4 epsilon. If its translates through M cover the circle, subadditivity requires

    1 <= (M+1) 4 epsilon.

In particular M cannot be 0 or 1. The sharper bound in the private log also checks out: 176(4 epsilon) = 88 sqrt(2)/125 < 1 because 15488 < 15625, so every cover has M >= 176. This is a necessary lower bound, not a claim that 176 suffices. Some finite M exists by the irrational rotation and compactness, and all such M include the bad n=2.

The counterexample uses the full multivalued map explicitly specified in TB. Removing the isolated branch as a null set, or choosing a tie rule that removes it, would change the asserted pointwise statement.

## Could an innocent interpretation repair it?

No interpretation preserving the modified arbitrary witness and its stated properties justifies the final sentence. “Of the form (tb4)” specifies the displayed block construction; it does not itself incorporate LTB's separate rational independence hypothesis. The next explicit finite condition and “any block” reinforce this reading. “Such blocks exist by LTB” proves existence, but does not impose every sufficient condition in LTB on every permitted witness.

One can certainly repair the proof by restoring a choice with jointly independent widths, as in the original excerpt. That is a short textual repair, but a substantive mathematical strengthening of the chosen witness. Merely renaming the original horizon N0 and the later one M does not prove the missing property. Reselecting B after M also changes the set whose translates were proved to cover, and would require a new compatibility argument.

Nor is this a lost fixed constant. For any initial finite N0 >= 1, let L=N0+1, take irrational positive epsilon smaller than both 1/[2L(2L-1)] and 1/(2L^2), and choose

    p1=1/(2L)+epsilon, p2=1-p1,
    B=[-L epsilon,L epsilon], delta=1/2, rho12=2L epsilon.

Through time L-1 the images are the intervals B+kp1: their largest upper endpoint before time L is (L-1)/(2L)+(2L-1)epsilon < 1/2. At time L the image is [-1/2,-1/2+2L epsilon] union {1/2}. The first L projected intervals have total measure at most 2L^2 epsilon < 1, so every cover includes that bad iterate. Thus enlarging an initial finite bound once cannot validate the asserted compatibility for all permitted witnesses.

The unchanged geometric argument still proves K* = union from n=0 to M of T^n B. It is possible for additional terms to fill neighborhoods of the isolated point in the total union. This does not make each individual term good, which is the actual assertion used. Any alternative proof exploiting cancellation or absorption of lower-dimensional pieces would require a new argument; it is not the stated inference.

## Downstream significance and prospective subtlety

The defect invalidates the supplied proof of TB's full-dimensional decomposition. TX then invokes TB and the polytope-support lemma to identify support of invariant Lebesgue measure with K*, and hence identify all branch limit sets with K*. CTX and later general-theory consequences inherit this missing justification. The earlier existence, invariance, absorption, and measure results are not contradicted by the witness.

The theorem itself need not be false. For this two-party vector the paper's explicit later example correctly gives K*=[-1/2,1/2], and the original stronger witness selection proves the general theorem. The audit concerns a real false intermediate assertion in the submitted proof, not a false headline theorem.

Prospectively the mutation is sufficiently subtle and integrated. It borrows a legitimate finite cover from an earlier proof, makes a legitimate existence choice from a stronger lemma, leaves the intervening invariant-set argument intact, and uses the familiar phrase “increasing N if necessary.” The trap is the unretained witness property and the change from the larger neighborhood's cover to the smaller block interior's cover. On the other hand, the modified choices and enlargement are close enough within TB that a careful reader can spot the dependency issue without reading hundreds of intervening lines. The lemma's preceding warning about lower-dimensional tied cuts also offers a clue. I therefore assess the subtlety as moderate, not exceptionally deep. I have no independent blind-review outcome and make no nondetection claim.

There is no unresolved mathematical issue affecting this verdict: the explicit witness satisfies the stated assumptions and falsifies the exact final per-iterate assertion for every covering horizon available to that witness.
