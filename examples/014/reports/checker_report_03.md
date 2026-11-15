OK

Independent audit of checker_4103

Verdict: The planted sentence creates a substantive mathematical defect in the directional enclosure argument. The supplied G1 classification is appropriate: a positive-combination inclusion subject to a fixed signed-lift restriction is extended to combinations not satisfying that restriction after the shortest projective arc selects different lifts. The edit is sufficiently subtle and integrated into the proof. This verdict concerns the submitted mathematical verification procedure, not the truth of the headline dimension theorem or the contents of the uninspected external verifier.

Scope of audit

I read the entire 4,102-line modified paper, including both bibliography regions, in bounded chunks, the entire private tricker log, and mutation.json. I reread the affected context and the portion of an initially truncated read. I did not inspect another paper version, the baseline report cited in the log, other experiment material, external programs, or other agents. No formal proof assistant was used. The original sentence is assessed as supplied in the log and replacement record.

Exact location and original versus modified inference

The defect is on physical source line 2315 of run_20261114/blind/r3n6h8/paper.tex, in Section sec:comp, paragraph “Values at the vertices.” After correctly observing that V_k is affine in k and that tail vectors are positive combinations of V_K and U, the text replaces “the arc of directions that they span” by “the shortest closed arc of PT containing their directions.” The “their” refers to the corners of the enclosing vector boxes. The common-open-half-plane test remains unchanged.

For signed vectors b_1,...,b_m in a common open half-plane H through the origin, every nonzero positive combination has direction in the projectivization of their positive cone. Projectivization is one-to-one on H, and that cone determines a particular arc. Its oriented angular width is less than pi, but it can exceed pi/2. Since PT is the space of unoriented lines (line 1673), its circumference for the Euclidean angle is pi. Consequently the cone arc can be the longer arc between two extreme directions. The original sentence has a valid interpretation as precisely this cone-spanned arc, with the signs supplied by the vector boxes. The modified sentence does not preserve that interpretation.

Exact admissible witness

Fix any integer K >= 1 before choosing the direction. In particular fix the actual infinite-tail cutoff K = 2^28 + 1. Set

  x = (0, 1/2, 1/2), i = 1, j = 2,
  w = (4K+3, -4K-4, 1).

The point x belongs to C_1, including its boundary, and j differs from i. The entries of w sum to zero, so w is a nonzero vector of T. The state space is C_i times all of PT; it is not restricted to directions of actual soul orbits. Unit length is unnecessary because the operator normalizes w in its weight, while the direction is projective. The chosen w is a positive multiple of the representative w(vartheta) specified in the paper for its coordinate vartheta = (8K+4)/(12K+9), so the prescribed representative convention does not remove the example.

Directly from Lemma lem:contraction and the definitions before line 2315,

  u = 2x_2 = 1,
  d_k = k+1,
  c = (pr(1-e_2)-x)/x_2 = (1,-1,0),
  p_w = w + w_2 c = (-1,0,1),
  U = u p_w = (-1,0,1),
  V_k = d_k p_w - w_2 c
      = (4K+3-k, -4K-4, k+1).

Thus

  V_K = (K+1)(3,-4,1),
  V_(2K+1) = 2(K+1)(1,-2,1),
  V_k = V_K + (k-K)U.

These equalities also independently verify that the unchanged positive-combination assertion is true. Every displayed finite-run vector is nonzero, since its second coordinate is the nonzero constant -4K-4.

In the paper's vector coordinates xi=3v_1, eta=v_2-v_3,

  eta(V_K) = -5(K+1), eta(U) = -1.

Exact singleton interval boxes around V_K and U therefore pass the open-half-plane test eta<0. Such boxes are permitted enclosures of exact values. The contradiction persists for sufficiently small boxes of positive width, by its strict angular separation; it is not dependent on the convention about degenerate boxes or on rounding.

The projective coordinates from the paper give

  vartheta(V_K) = 1 - 5/9 = 4/9,
  vartheta(U) = 1 + 1/3 = 4/3,
  vartheta(V_(2K+1)) = 1 - 1 = 0 modulo 4.

The unique shortest arc between the endpoint directions is S=[4/9,4/3], which excludes 0. This is the short arc both for the Euclidean angle on PT and for the period-4 coordinate. For the former assertion, V_K dot U = -2(K+1), |V_K|=sqrt(26)(K+1), |U|=sqrt(2), so the signed angle is obtuse, with cosine -1/sqrt(13). The original signed positive cone follows the other projective arc, through 0=4. The finite integer k=2K+1 belongs to the tail and gives a direction outside the proposed enclosure. All quantities are exact and the example works for every fixed K, including the paper's cutoff.

G1 classification and quantifiers

The valid pre-generalization implication is: for fixed signed representatives b_0,b_1 whose positive cone projects to the selected arc S, for all real a,b >= 0 with a b_0+b b_1 != 0,

  v = a b_0+b b_1  implies  [v] in S.

Equivalently one can universally quantify v restricted to that signed positive cone. This is the restriction on the selected objects, not merely that their individual projective directions belong to S. For the short arc in the witness, usable lifts are b_0=V_K and b_1=-U. The valid universal statement concerns positive combinations of V_K and -U.

The paper's actual target is: for every allowed x and source w under consideration, and every integer k >= K, the direction of V_k(x)w lies in the chosen enclosure. For our fixed x,w, those targets are positive combinations of V_K and +U. In terms of the short-arc lifts they are

  V_k = b_0 - (k-K)b_1.

For k>K the second coefficient is negative, so they fall outside the restricted class for which the implication is valid. The modified construction nevertheless uses the short arc for that whole target range. The dependency w=w(K) is legitimate: K is fixed first, and the enclosure rule claims validity for all directions thereafter. There is no requirement that one direction work for every K simultaneously.

This is G1 in the supplied sense of illicit generalization from objects satisfying a selection restriction to a wider target class. It can also be described informally as a false projective-convexity inference. The log's G1 label is correct. It is not principally CONV: the displayed algebra, projection coordinate, and shortest-arc computation can all be correct. It is not DEF: the shortest arc is unique and well defined in this example. Nor is it a witness-dependent existential elimination (G2). No named theorem is being misinstantiated here, so MP is less apt than the restriction-loss description.

Effect on the next enclosure operation

There is an admissible positive piecewise-linear test function for which this missing range causes an actual wrong factor bound. Take angular nodes

  0, 3/4, 7/8, 1, 9/8, 5/4, 2, 4,

and any base mesh allowed in Section ssec:P1. The angular node set has the required symmetry vartheta -> 2-vartheta modulo 4. Let h_1 be independent of the base coordinates, equal to 1 outside [7/8,9/8], equal to 8 vartheta-6 on [7/8,1], and equal to 10-8 vartheta on [1,9/8]. This is continuous, positive, symmetric, and affine on the required cells.

The actual operator applies tau_2 to the derivative direction. Direct calculation gives

  vartheta(tau_2 V_K) = 5/6,
  vartheta(tau_2 U) = 3,
  vartheta(tau_2 V_(2K+1)) = 1.

The image of the false short arc under tau_2 is [3,4] union [0,5/6]. The function h_1 is identically 1 there. All complete mesh cells meeting this arc also have value 1: the last cell on the lower branch ends at 7/8, and the increasing part begins only there, with the arc endpoint 5/6 strictly before it. In contrast the actual tail direction has h_1=2. Thus enclosing by whole selected cells does not repair the incorrect directional enclosure. The base target lies in C_1 after tau_2, as required by Lemma lem:trap, and the finite-run derivative weight is positive. The paper's conservative cell-selection tolerance is vastly smaller than the displayed gap 7/8-5/6=1/24.

This example establishes failure of the value enclosure construction for the class to which the method applies. It is not a claim that this h_1 is one of the stored test functions, that its chosen source direction is a stored mesh node, or that the final sum for the actual h^+ or h^- was numerically underestimated. Those stronger assertions have not been established and are unnecessary for locating the false mathematical enclosure rule.

No harmless repair under the existing assumptions

The half-plane condition only enforces angular spread below pi for the signed lifts; it does not enforce spread below pi/2. All source directions are allowed, and the contraction bound on the derivative does not enforce an acute angle between V_K and U. The long-tail cutoff cannot rescue the statement because the counterexample works after that cutoff is fixed. Positive rescaling or normalization of w changes neither the cone geometry nor the projective exclusion. Independently changing the sign of U preserves its direction but destroys the positive-combination restriction, which is exactly the error. Reading “shortest” as shortest within a chosen half-plane lift would require adding that restriction and would return the original cone arc; it is not the ordinary shortest arc of PT specified by the modified text. Taking all of PT, or taking the cone-spanned arc with consistent signed lifts, is a substantive correction to the range construction and cell selection.

Downstream significance and limits

Cases (b) and (c) after Proposition prop:P1 require target sets containing all images; the grouped-run procedure in Section sec:comp invokes the construction again for enclosures on prisms and boxes. A direction set that misses a true run image is not such an enclosure, so the described value and gradient hulls need not bound the relevant functions. Consequently the proof has not justified the hypotheses needed to apply Proposition prop:P1 in the final certificate of Theorem thm: dimH. This is a concrete false inclusion and can produce a false test-function bound, not a lost absorbable constant or a merely unproved estimate.

The external source code and exact stored test functions were outside this audit. They could implement the original valid cone rule, or additional overestimation could happen to cover the relevant values. The headline dimension statement is not disproved. None of those possibilities validates the false mathematical construction stated in the modified paper, and no restriction in its stated method excludes the witness. Dependent numerical uses of the dimension bound, including the diffusion estimate, inherit the need for a valid certificate.

Prospective subtlety assessment

The edit is well integrated: it changes a single natural-sounding geometric instruction within a dense numerical proof while retaining the correct affine formula, positive combinations, and half-plane guard. “Shortest” resembles a routine tightening of an interval enclosure. Detecting its failure requires tracking signed representatives through the quotient by antipodes, linking the earlier definition of PT and the run derivative to the later grouped-tail construction. The vulnerable directions are close to the kernel direction for large K, which also explains why an unguided spot check might not reveal the failure. A reviewer checking that the enclosure contains an intermediate tail vector can find it, so this is not maximally hidden; nevertheless it is a suitably subtle substantive change. This assessment is prospective and uses no blind-review result.
