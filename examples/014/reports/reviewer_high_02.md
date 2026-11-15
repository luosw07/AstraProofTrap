REJECT

I found a substantive error in the stated direction-enclosure procedure used to justify the computer-assisted affinity-exponent bounds. This is an error in the proof of the certificates, not a counterexample to the asserted numerical value of the dimension.

Review scope

I read all 4,102 lines of the supplied standalone `paper.tex`, including its embedded bibliography, the full mathematical text, figure captions, and final bibliography. I read the source in bounded chunks and reread the passage lost in one truncated output. My mathematical input was this paper alone. I did not consult another version, external references, numerical-program files, other workspace papers, or another review. I did not use a formal proof assistant. I used elementary arithmetic to check the counterexample below. I reviewed the TeX rather than separately inspecting the rendered PDF.

The principal issue

Location: Section “The computation,” paragraph “Values at the vertices,” TeX lines 2301–2315, specifically the final direction-enclosure prescription at line 2315. This prescription is also invoked for enclosures on prisms or boxes at lines 2332–2336. The conclusions relying on these enclosures are the certificate table at lines 2373–2383 and the proof of Theorem `thm: dimH` at lines 2391–2396.

The paper correctly observes that the vectors for a block of runs, or for a tail, are positive combinations of the endpoint vectors (the tail uses its first vector and the limiting vector U(x)w). It then says that, when the corners of the enclosing boxes lie in an open half-plane, it takes the shortest closed arc of the projective line containing their directions.

That rule does not enclose the directions of the positive combinations. An open half-plane selects an oriented cone of angular width less than pi in the vector plane. Its projection to the projective line may have length greater than half the circumference of the projective line. The shortest projective arc containing its endpoint directions can then be the other arc. It omits interior directions of the cone. The half-plane test does not prevent this.

Here is a counterexample using the paper's own run formulas, rather than an arbitrary pair of vectors. Let K be the first run in a tail, let q=1/(4K), and take

    j=2,  x=(0,1/2,1/2) in C_1,
    vartheta=2/3 - 1/(12K),
    w=(2,-2-q,q).

The formula for w in line 2173 gives exactly this w. The quantities in Lemma `lem:contraction` and line 2303 are

    u=1,  c=(1,-1,0),
    p_w=w+w_2 c=(-q,0,q),
    U(x)w=p_w,
    V_k(x)w=(2-kq,-2-q,(k+1)q).

In the paper's coordinates xi=3v_1 and eta=v_2-v_3 (line 2169), these become

    V_k: (xi,eta)=(6-3kq, -2-(k+2)q),
    U:   (xi,eta)=(-3q,-q).

Every one of these vectors lies in the open half-plane eta<0. In particular the half-plane condition holds for the exact, degenerate endpoint boxes, and continues to hold for sufficiently small enclosing boxes. At the start of the tail,

    V_K: (xi,eta)=(21/4, -9/4-2q).

Its projective direction is approximately 156.8 degrees in R/(180 degrees Z), while the direction of U is approximately 18.4 degrees. The shortest projective arc between them crosses the horizontal direction, through 180 degrees/0 degrees. It does not contain the vertical direction, 90 degrees. But the actual tail includes k=8K, for which

    V_(8K): (xi,eta)=(0,-4-2q),

which is precisely vertical. Thus the proposed enclosure misses a direction of an actual run in that tail.

The example also fails if the coordinate permutation tau_2 is applied before taking the boxes, as is appropriate when bounding the argument of h_1. In that case

    tau_2 V_k: (xi,eta)=(-6-3q, 2-(2k+1)q),
    tau_2 U:   (xi,eta)=(0,-2q).

For K=2^28+1, the projective endpoint directions are approximately 165.96375655 degrees and 90 degrees. Their shortest arc has length approximately 75.96375655 degrees. The actual vector tau_2 V_(4K) has projective direction approximately 0.0000000089 degrees, outside that arc. These endpoint vectors also lie in a common open half-plane. Consequently undoing or implementing the permutation does not resolve the problem.

Why this is substantive

The function h_1 is piecewise polynomial on direction cells. If an enclosure omits image directions, taking the hull of values and gradients over only the selected cells need not bound h_1 or its derivatives at the actual images. The bounds on grouped-run terms, and hence the interpolation margins in Proposition `prop:P1`, then have no established validity. This is a mathematical failure in an enclosure rule, not merely a typographical sign error or a matter of numerical precision.

A valid replacement is to retain the arc swept out by the positive cone in a common oriented half-plane, and then project that entire arc to the projective line, even when it is longer than the other projective arc. Returning all of the projective line is also safe. Simply asking for the shortest projective arc of the corner directions is insufficient.

The provided paper does not include the implementation or its full input data. Therefore I cannot determine whether the deposited verifier actually uses the erroneous rule as written, uses a correct oriented-cone rule despite the description, or avoids the problematic case for every box and point in the particular reported run. I have not established a failure of a particular logged cell. What I have established is that the general enclosure step presented as the justification of those certificates is false, including on the stated run system. To restore the claimed proof, the author must supply and justify the stronger enclosure rule or establish that the problematic cases cannot occur in the actual verification; if the code uses the stated rule, the certificates need rechecking after correction.

Effect on conclusions

This leaves the claimed rigorous interval 1.6853 < dim_H N = dim_B N < 1.6854 unjustified by the supplied argument. It also affects numerical consequences that use these precise bounds, including the stated 0.7766 diffusion bound and the explicit 1.6853 lower bound for the three-dimensional gasket. It does not by itself refute those inequalities, the equality of Hausdorff and box dimensions, or the independent norm-exponent certificates. The analytic reduction to a positive transfer-operator inequality remains useful; the issue is the claimed rigorous verification of that inequality.

Other review findings and limitations

I found no additional substantive error in the arguments I checked. In particular, I examined the zone decomposition and frame estimates; weak contraction and chain recurrence; singular-value, diameter, and derivative comparisons; the cut-out upper and lower bounds; the run decomposition and pressure estimates; the norm-exponent discretization; the Markoff–Hurwitz word dictionaries and counting deduction; the higher-dimensional geometric estimates; and the symbolic Gibbs, inducing, entropy, and Lyapunov arguments. The proof of the diffusion inequality from the entropy relation and the affinity series is algebraically consistent, conditional on its stated inputs.

The review accepts explicitly quoted external results as inputs only to the extent of the statements reproduced in this paper. I did not independently verify the source statements or their bibliographic attribution. The dimension equality, counting asymptotic, and identification with the Avila–Hubert–Skripchenko setting rely on such inputs. I also did not rerun any of the large computer-assisted calculations, inspect their checksums against actual data, or audit the floating-point code. Even apart from the identified flaw, those are genuine limits of a paper-only review, not evidence that the reported calculations are wrong.

No harmless typo is used as a basis for the verdict. The rejection rests on the explicit, mathematically invalid projective-direction enclosure and its role in certifying a main theorem.
