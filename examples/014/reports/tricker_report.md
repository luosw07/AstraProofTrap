# Tricker report

## Exact edit

Location: Section `sec:comp`, the paragraph headed “Values at the vertices,” source line **2315**, starting at column **537**. The sentence follows the affine formula for the tail vectors and the assertion that the tail vectors are positive combinations of the initial tail vector and the limiting vector. Both the source and output retain this line number.

Before, occurring exactly once:

```tex
If the corners of the boxes lie in an open half-plane, we take the arc of directions that they span; otherwise we take all of $\PT$.
```

After, occurring exactly once:

```tex
If the corners of the boxes lie in an open half-plane, we take the shortest closed arc of $\PT$ containing their directions; otherwise we take all of $\PT$.
```

This is a single replacement. The half-plane check, the affine formulas, the positive-combination statement, all weights, all numerical tables, and all reported computational results remain unchanged.

## The distant dependency that the edit loses

The difference between a cone-spanned arc and a shortest projective arc depends on several pieces of the paper that are separated in the exposition:

1. Line 1673 defines `\PT` as the set of **unoriented** lines in the tangent plane `T`. Thus opposite nonzero vectors represent the same point of `\PT`.
2. Lines 2169–2173 define the angular coordinate `\vartheta` modulo 4 through `\xi=3v_1` and `\eta=v_2-v_3`. This is a coordinate on the projective line, not an oriented unit-circle coordinate. In particular a genuine directional arc can cross the identification at 0/4.
3. Lemma `lem:contraction`, equations `eq:DR` and `eq:DRB` (lines 2000–2030), gives an actual **signed linear image** of a tangent vector. The sign is irrelevant when evaluating a single direction, but matters when describing positive linear combinations of several such images.
4. Lines 2301–2305 introduce the signed representative

   `V_k(x)w=d_k^2 D_x psi_j^k(w)=d_k p_w-w_j c`, with `p_w=w+w_j c`.

5. Line 2315 uses its affine dependence on `k`: for a tail starting at `K`, the vectors are positive combinations of `V_K(x)w` and `U(x)w=u p_w`. This statement is correct for these particular signed representatives.
6. The replacement then discards the selected signs by passing to endpoint **directions** and choosing the shortest arc between them. That shortest arc may be spanned by `V_K` and **minus** `U`, whereas the actual tail is a positive combination of `V_K` and **plus** `U`.
7. The target enclosures in cases (b) and (c), lines 2251–2256, must contain **all** image points and directions. The point evaluations and grouped-tail evaluations in lines 2305–2315 and 2332–2336 use those enclosures for the test function and its gradient. Proposition `prop:P1`, lines 2220–2240, then needs the resulting bounds to hold at every point of the check set. Its application at lines 2393–2395 proves Theorem `thm: dimH` in the paper.

Thus the subtle change is not a local arithmetic error. It forgets the representative restriction when carrying the earlier positive-cone statement through the antipodal quotient.

## Why the original sentence is valid

Let a finite collection of nonzero signed corner vectors lie in an open half-plane `H` through the origin. Their positive cone has angular width strictly less than pi in the oriented tangent plane. Projectivization is injective on `H`, and the projectivized cone is one definite closed arc `A_H` of `\PT`. Every nonzero positive combination of the original corner vectors has direction in `A_H`.

That arc is the arc the corners **span** with their common half-plane lifts. Its angular length need not be at most pi/2. The circumference of the projective line is pi, so an arc of length between pi/2 and pi is legitimate and can be the longer of the two arcs between its endpoints.

The original rule preserves this cone and these lifts. The fallback to the entire `\PT` covers configurations where the common-half-plane argument is unavailable. The same reasoning applies to boxes: a vector in a box is a convex combination of its corners, and positive combinations of vectors in the boxes are in the positive cone of all their corners.

## G1 classification and quantified inference

### Implication before the invalid generalization

For selected representatives `b_0,b_1` whose positive cone projects onto the chosen short arc `S`, one has

`v=a b_0+b b_1`, `a,b>=0`, `v!=0`  ==>  `[v] in S`.

The universally quantified variables in the consequent are `a,b` (or equivalently the vector `v`); in the application they include every tail index `k>=K`, as well as every allowed base point and input needle under consideration.

The restriction actually used is **positive coefficients with respect to those same selected signed representatives**. For a pair of original representatives, using their shortest projective arc is justified by this argument when their angle is at most pi/2. Merely placing them in a common open half-plane only bounds their angle by pi and does not provide the stronger restriction.

### Target objects after the edit

The target vectors are the actual run images

`V_k=V_K+(k-K)U`, `k>=K`.

Their coefficients are nonnegative relative to `V_K,U`. The modified rule instead constructs `S` from unoriented endpoint directions. When the signed endpoints are obtuse, `S` is the positive cone of `V_K,-U`. For the actual target vectors,

`V_k=V_K-(k-K)(-U)`.

For every `k>K`, the second coefficient in this selected cone is negative. The target vectors therefore do not satisfy the restriction under which membership in `S` was established. The modified instruction nevertheless uses `S` as their universal enclosure.

This is primary **G1**: an inclusion valid for objects with a selected cone/lift restriction is silently extended to target objects lacking that restriction. It is not an algebraic conversion error: the formulas for `V_k`, `U`, the projective coordinates, and the shortest arc all compute correctly. It is not a definition failure: the shortest arc in the witness is unique and exists. No named established theorem is being applied incorrectly. The false inference is the extension of the directional range to all positive combinations after changing the representatives that specify “positive.”

## Exact admissible counterexample

The following is a family entirely within the actual objects and assumptions of the paper. It works for **any integer `K>=1`**, so it also works with `K=2^28+1`, at the scale of the infinite tail described at line 2307. There is no small-run or asymptotic exception.

Take

`x=(0,1/2,1/2)`, `i=1`, `j=2`,

and the nonzero tangent-vector representative

`w_K=(4K+3,-4K-4,1)`.

Admissibility checks:

- `x` is the vertex `pr(1-e_1)` of `C_1`, so `(x,[w_K],1)` is in the operator's state space.
- `j=2` differs from `i=1`, as required for a new run.
- The entries of `w_K` sum to zero, so `w_K` is in `T`. It need not have unit length because the operator explicitly normalizes it to `hat w` when computing weights.
- Its source direction has `vartheta=(8K+4)/(12K+9)`, which lies in `(0,2/3)`. It is an ordinary admissible direction, close to the kernel direction discussed in Remark `rem:fan`.
- All `k>=K` are legitimate run lengths, and any `0<kappa<1` can be used. No condition on the weight exponent is needed for the geometric contradiction.

At this base point, the quantities of Lemma `lem:contraction` are

`u=2x_2=1`, `d_k=k+1`, `c=(1,-1,0)`.

Write `v=(1,0,-1)`. Then `w_K=4(K+1)c-v`, and `w_{K,2}=-4(K+1)`. Consequently

```text
p_w = w_K + w_{K,2} c = -v = (-1,0,1),
U   = u p_w = (-1,0,1),
V_k = d_k p_w - w_{K,2} c
    = 4(K+1)c - (k+1)v
    = (4K+3-k, -4K-4, k+1).
```

In particular,

```text
V_K       = (K+1)(3,-4,1),
V_(2K+1)  = 2(K+1)(1,-2,1),
V_k       = V_K + (k-K)U.
```

The unchanged positive-combination claim is therefore exactly true.

### The unchanged half-plane test passes

Use the half-plane `eta<0`, where `eta=v_2-v_3` is precisely the paper's coordinate. Then

```text
eta(V_K) = -5(K+1) < 0,
eta(U)   = -1 < 0.
```

Thus exact singleton boxes for the two endpoint vectors have all their corners in one open half-plane. These are valid interval boxes. If positive-width boxes are desired, sufficiently small boxes around them still lie in `eta<0` and preserve the strict enclosure failure below.

### The proposed shortest arc excludes a true tail direction

For `V_K`, the paper's coordinates give `xi=9(K+1)` and `eta=-5(K+1)`, hence

`vartheta(V_K)=1-5/9=4/9`.

For `U=(-1,0,1)`, they give `xi=-3`, `eta=-1`, hence

`vartheta(U)=1+1/3=4/3`.

The shortest projective arc between these directions is

`S={vartheta: 4/9 <= vartheta <= 4/3}`.

This is the shorter arc for the usual angle metric on `\PT`, and also for the circle coordinate of period 4. To check the angle without relying on a picture,

```text
V_K dot U = -2(K+1),
|V_K| = sqrt(26)(K+1),
|U| = sqrt(2),
cos(angle(V_K,U)) = -1/sqrt(13).
```

The original signed angle is approximately 106.102 degrees. The shortest projective arc, approximately 73.898 degrees, is spanned instead by `V_K` and `-U`. The coordinate interval above is that arc.

Now take the legitimate tail run `k_*=2K+1`. Since its vector is proportional to `(1,-2,1)`,

`xi(V_(2K+1))=6(K+1)` and `eta(V_(2K+1))=-6(K+1)`.

The first branch of the paper's coordinate formula applies at equality and yields

`vartheta(V_(2K+1))=0 mod 4`.

But `0` is outside `[4/9,4/3]`. This is an exact, finite counterexample to the modified enclosure, not a limiting discrepancy.

The correct cone-spanned arc runs the other way around the projective circle, through `0=4`; it contains this direction. The original sentence handles the example correctly.

## Explicit failure of a permitted test-function enclosure

The error can be seen at the next mathematical operation, not merely as an objection to how an arc is described.

Take any allowed symmetric base mesh, and the allowed angular mesh with nodes `0,3/4,7/8,1,9/8,5/4,2` and the closing node `4`. This node set is preserved by `theta -> 2-theta mod 4`. Define a positive test function, independent of the base coordinates, by

```text
h_1(theta) = 8 theta - 6   for 7/8<=theta<=1,
           = 10 - 8 theta for 1<=theta<=9/8,
           = 1           everywhere else on R/4Z.
```

This is continuous on `R/4Z`, piecewise linear on the paper's cells, bounded between 1 and 2, and invariant under `theta -> 2-theta mod 4`. Hence it satisfies the symmetry and positivity assumptions of Section `ssec:P1`; independence of the base variables gives the required `tau_23` symmetry there as well.

The target direction used to evaluate `h_1` includes the transposition `tau_2` (Lemma `lem:sym`, line 2145, and the definition of `Phi_{j,k}`, line 2246). Since `tau_2` is an isometry of `T`, it preserves the distinction between the long and short projective arcs.

For the two endpoint directions,

```text
tau_2(V_K) is proportional to (-4,3,1), with theta=5/6,
tau_2(U) = (0,-1,1), with theta=3.
```

Thus the false target arc is `tau_2(S)=[3,4] union [0,5/6]`. On it, `h_1=1`. Even if the evaluation uses the entire target cells meeting this false arc, every such cell has `h_1=1`: the last selected cell on its lower branch ends at `7/8`, while the two nonconstant cells lie between `7/8` and `9/8`. The false arc is separated from those cells by the positive gap `7/8-5/6=1/24`.

For the actual tail run `2K+1`, however,

`tau_2(V_(2K+1))` is proportional to `(-2,1,1)`, whose coordinate is `theta=1`,

so its actual test-function value is **2**, strictly larger than the supposed upper bound **1**. The actual base image lies in `C_1` by Lemma `lem:trap`, so the test function is evaluated at an admissible target state. The derivative weight is strictly positive, because the finite-run projective derivative is invertible. Therefore the mistaken arc can exclude actual values of the very factor multiplied by that weight. Selecting whole cells rather than restricting a polynomial to the arc does not rescue this example.

This example is not claimed to be either of the enormous stored numerical test functions. It disproves the mathematical enclosure rule for the class of test functions to which the paper says the rule applies. It also shows why the issue cannot be repaired by silently treating the chosen arc as just another notation for the original one.

## Consequences, subtlety, and detection

The modified direction set is not an enclosure. As a result, selecting target cells using it can omit cells actually reached by long runs. The asserted hull of test-function values can be too small, and the derivative hulls required for the grouped increment bounds can omit relevant pieces. The hypotheses of Lemma `lem:interp` and Proposition `prop:P1` are then not ensured by the described verification procedure. This affects the stated certification route to Theorem `thm: dimH`.

The final dimension theorem is not asserted to be false. Nor have the original external programs or their test functions been changed or inspected. They may implement the original valid cone-spanned-arc rule. The construction establishes a substantive mathematical defect in the modified paper's proof/verification description and supplies an exact admissible witness. Accidental overestimation elsewhere in a particular computation does not make the false range inclusion true.

The edit is subtle because:

- It retains the original half-plane test and all correct affine and positive-combination formulas.
- A shortest arc sounds like a natural, tighter enclosure once only unoriented endpoint directions are mentioned.
- Convex-hull intuition is valid for the base maps and for vectors with consistent signs, and is used correctly elsewhere in the paper.
- Recognizing the error requires remembering that `\PT` identifies opposite vectors and tracing the signed `V_k,U` representatives through the run derivative and symmetry reduction.
- The witness lies near the repelling kernel direction discussed much earlier in Remark `rem:fan`; the defect survives at arbitrarily large tail cutoffs.
- No instruction to the reviewer, bibliographic change, suspicious theorem statement, or explicitly false universal-quantifier sentence was added.

A careful reviewer could find it by checking that the projective arc used after the half-plane test is the image of the original signed positive cone, by testing a needle on either side of the kernel direction for a very long run, or by directly sampling the direction of an intermediate run between the two endpoints. The exact family above makes all three checks decisive. Tracking a continuous angular lift before reducing modulo 4 would also expose the omitted wrap.

The actual repair is to retain the cone-spanned arc determined by the common half-plane lifts, even when it is the longer projective arc, or to use all of `\PT` whenever those lifts are not tracked. This is a change to the enclosure construction and its cell selection, not a harmless relabeling of a symbol.
