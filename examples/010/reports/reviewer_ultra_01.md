REJECT

I reviewed the supplied manuscript as written, under the instruction not to repair its proofs. The principal issue is an invalid inference in Theorem 7.12: the proof enlarges a time bound after selecting a block whose iterates are known to be unions of full-dimensional blocks only up to the original bound. Its final assertion about the newly included iterates is false for some blocks expressly permitted by its selection sentence. This is a local proof defect rather than a counterexample to the theorem's conclusion. I also record a separate local inconsistency in the use of the transition times in Theorem 3.2.

All TeX line references below refer to the supplied `paper/paper.tex`. The theorem numbers were cross-checked against the supplied PDF.

1. Theorem 7.12: enlargement of N invalidates the property imposed on B

References: Theorem 7.12, proof, TeX lines 4216–4220, 4230–4233, and 4254–4258; especially the final sentence at lines 4257–4258. The block is defined by equation (7.64), TeX label `tb4`. The covering condition originally used to select N is equation (7.19), TeX label `tinv5a`.

The proof first selects N from the covering by translates of the projected neighbourhood N_delta. It then says to choose “any block B of the form (7.64)” contained in N_delta such that T^n B is a finite union of good blocks for 0 <= n <= N. After fixing this B, it obtains a cover by translates of the smaller set pi(B°) by “increasing N if necessary.” At the end it asserts that every T^n B in the resulting union, for the enlarged range 0 <= n <= N, is a finite union of good blocks “by the choice of B.”

That implication does not follow from the stated choice, and the property is not automatically preserved at the additional times. Here is an explicit counterexample to that inference using the manuscript's own map.

Take m = 2 and

    p_1 = p = sqrt(2)/4,       p_2 = 1-p,
    delta = 1/2,             r = 2p-1/2,
    B = {(x,-x): -r <= x <= r}.

This is an ergodic vote vector: p is irrational, and p and 1-p are rationally independent. In first-coordinate notation, N_delta is (-1/2,1/2). Its projection to the circle omits just one point, so its translates for k = 0 and k = 1 cover the circle. Thus N = 1 is a valid initial choice under (7.19).

The block B is contained in N_delta and has precisely the form (7.64), with

    rho_12 = 2r = 4p-1 > 0.

Using the map printed in equation (10.2), TeX label `T1b`, direct calculation gives

    B     = [-r,r],
    T B   = [1/2-p,1/2] union [-1/2,3p-3/2],
    T^2 B = [-1/2,4p-3/2] union {1/2}.

Both intervals in T B have positive length. Therefore B satisfies exactly the proof's prescribed condition for the original N = 1. However, 4p-3/2 is approximately -0.085786, so 1/2 is an isolated point of T^2 B. In this one-dimensional setting a good block is a nondegenerate closed interval. A finite union of such intervals cannot have an isolated point. Consequently T^2 B is not a finite union of good blocks.

Moreover, the enlargement of N really is necessary for this B. The two translates of pi(B°) for k = 0,1 have connected lifts whose union has length

    p+2r = 5p-1 < 1,

so they do not cover the circle. The translates for k = 0,1,2 do cover it: consecutive lifted intervals overlap, and their union has length

    2p+2r = 6p-1 > 1.

Thus the proof can enlarge its bound from 1 to 2 exactly as described, and its final claim about each iterate in that enlarged union is then false. Any larger bound still includes the offending second iterate.

Lemma 7.11 gives an all-time statement under an additional rational-independence condition on the radii. Theorem 7.12's selection sentence uses that lemma to assert existence, but explicitly selects any block satisfying the stated finite-time property. It does not impose that additional condition on its selected B. In this example rho_12 = 3p_1-p_2, so that distinction is real. Treating the selected block as satisfying the stronger hypothesis would be a change to the printed proof, which this review was instructed not to make.

Effect: the final inference establishing the finite union of good blocks in Theorem 7.12 is invalid as printed. The example refutes that intermediate inference, not the conclusion about K*. The support identification and the equality of every branch limit set with K* in Theorem 7.16 use Theorem 7.12, so their printed dependency on the polyhedral statement inherits this local gap. The earlier compact-attractor and invariant-measure arguments in Theorems 7.5 and 7.7 do not use this step.

2. Theorem 3.2: the transition time is used with two different meanings

References: Theorem 3.2, proof, TeX lines 1857–1865, and the subsequent Case 2 argument at lines 1865–1878.

The proof defines

    T_l = min{t: |A_t| = m-l}.

It then establishes z(T) = z(T_{m-1}) and says that T_{m-1} may be replaced by T. Immediately afterward, it states that if t = T_l for l >= 1, then |A_t| < |A_{t-1}|, and applies Case 2 of the preceding proof. This strict decrease is valid at the original minimum-defined transition times. After the announced replacement of T_{m-1} by T, it need not hold at the last selected time.

For a concrete instance, take m = 3, target party j = 3, final time T = 3, and the three successive vote vectors

    (1/3,1/3,1/3), (0,1/2,1/2), (0,0,1),

with wins by parties 1, 2, and 3, respectively. These are admissible Frege choices. The discrepancy vectors are

    z(1) = (-2/3,1/3,1/3),
    z(2) = (-2/3,-1/6,5/6),
    z(3) = (-2/3,-1/6,5/6).

Thus z_3(3) = h_3-1. For the sets A_t defined in the proof,

    A_0 = {1,2,3}, A_1 = {2,3}, A_2 = A_3 = {3}.

The original T_2 is 2. Its replacement by T gives T_2 = 3, at which |A_3| = |A_2| = 1. Therefore the next paragraph's strict-decrease assertion and its use of Case 2 do not apply to that replacement time. At time 3 the winning score is 11/6, also demonstrating directly that the terminal-round score computation from Case 2 is not the computation applicable there.

Effect and classification: this is a local sequencing/notation inconsistency, not a counterexample to Theorem 3.2. The text has already established equality of the relevant terminal discrepancy vectors. If “we may replace” is intended only as an observation about the final selection of times, while subsequent calculations retain the original minimum-defined times, that intent should be distinguished from performing the replacement. Under the stipulated literal, no-repair review I record the false transition assertion after the replacement. The rejection does not depend on treating this notation issue as a second substantive theorem gap; Issue 1 independently supplies the invalid inference.

Coverage and other checks

I read all 9,078 TeX lines in bounded, untruncated chunks, covering the complete manuscript: definitions, introduction and announced results, all proofs, all examples and remarks, the divisor-method discussion, and the bibliography. I inspected all eight supplied external figure assets, rendering the four PDF assets, and read the two in-source polygon drawings. I used the matching paper PDF to verify the printed theorem and equation references relevant to the findings.

The review included the following mathematical checks:

- The discrepancy induction, equality conditions, fixed-vote sharpness construction and perturbation, near-extremal vote estimates, and their probabilistic and strict-supremum consequences.
- Boundedness and absorption, projection to a torus, the closed-subgroup decomposition, rational periodicity, the fibre-counting lemma, finite ties in the ergodic case, uniqueness of the compact invariant set, and the invariant-measure and empirical-measure arguments.
- The good-block lemma itself, including its independent-normal/tree argument and its use of rational independence to exclude a supporting cut. I found no separate error in that lemma; Issue 1 concerns its subsequent use.
- The intermediate examples, bias statements, the two-party dynamics, planar coordinate changes, Farey partition and first-entry description, ordering of the zig-zag vertices, invariance of the constructed polygon, the separate boundary-invariance argument, stability walls, vertex counts, the global even- and odd-wall endpoint arguments, and the adjoint pairing.
- The final translation of linear divisor methods into the stated recurrence and planar winner sectors.

I independently checked the two diagnostic examples above using ordinary arithmetic code. I also checked, with exact rational polygon-area and centroid calculations, representative points in S_{1/2} and each of the three displayed stability domains in R_{1/3}. All four polygon areas were 1, and their centroid-derived biases agreed with the corresponding displayed formulas. These are additional checks of those examples, not substitutes for the general proofs.

I identified no further substantive mathematical error in the remaining printed arguments. A minor index slip occurs in Example 8.2 at TeX lines 4457–4461: the statement about z_j(n) = -2/3 and the values of coordinates 1 and 3 is plainly being used for coordinate 2, as the immediately following formula (8.1), label `ei1`, makes clear. I treat that as a harmless index slip.

No external mathematical sources, prior manuscript versions, other reviews, private records, or formal proof assistants were consulted. Bibliographic entries and the manuscript's descriptions of prior work were read, but the cited works were not independently verified. The verdict is based on the invalid printed inference in Issue 1 and does not assert that the principal theorem statements are false.
