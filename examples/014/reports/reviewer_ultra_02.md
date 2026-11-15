REJECT

I found a substantive flaw in the direction-enclosure rule used to justify the computer-assisted dimension certificate. The rule can omit actual image directions even when its stated open-half-plane condition is satisfied. This is a gap in the written proof of the principal numerical dimension bounds, not a counterexample to the bounds themselves.

Paper reviewed: “The Levitt–Yoccoz gasket: dynamics, Hausdorff dimension and norm exponent,” the supplied standalone paper.tex. All line references below refer to that file.

## 1. Substantive issue: the shortest projective arc need not contain the positive cone

**Location.** Section “The computation,” paragraph “Values at the vertices,” TeX lines 2301–2315, especially the direction-enclosure rule in line 2315. The relevant direction coordinates are defined at lines 2169–2173. The resulting bounds are used by the verification at lines 2317–2342 and by the proof of Theorem `thm: dimH` at lines 2393–2395.

The paper correctly observes that the vectors representing the directions of a block are positive combinations of its endpoint vectors, and analogously that the tail vectors are positive combinations of its initial vector and its limiting vector. It then says:

> If the corners of the boxes lie in an open half-plane, we take the shortest closed arc of PT containing their directions; otherwise we take all of PT.

The second step does not follow from the first. A common open half-plane permits one to choose a consistent lift of the directions to the circle of **oriented** vectors. Its positive cone projects to a definite arc of the projective line. That projected arc need not be the shortest projective arc joining the endpoint directions. Identifying opposite vectors can make the complementary arc shorter.

This failure occurs for the actual run formulas in the paper, not just for an unrelated collection of planar vectors.

### Exact counterexample within the stated state space

Take

```
x = (0, 1/2, 1/2) in C_1,
j = 2,
u = 2 x_2 = 1,
c = (1, -1, 0),
e = (1, 0, -1).
```

Here c is exactly the vector in Lemma `lem:contraction`: c = (p_2 - x)/x_2, with p_2 = (1/2, 0, 1/2).

Let K be the first run in a tail, let D = K + 1, and put

```
a = 1/(4D),       w = a e - c.
```

The vector w belongs to T and w_2 = 1. Consequently, the formulas at lines 2303–2315 give

```
p_w = w + w_2 c = a e,
V_k(x) w = (k + 1) a e - c,
U(x) w = a e.
```

In particular,

```
V_K(x) w       = (-3/4, 1, -1/4),
U(x) w         = a (1, 0, -1),
V_(4K+3)(x) w = (0, 1, -1).
```

The third vector is an actual vector from the same tail, since 4K + 3 >= K. It is also an explicit positive combination of the two endpoint vectors:

```
V_(4K+3)(x) w = V_K(x) w + (3/(4a)) U(x) w.
```

Use the paper's coordinates xi = 3v_1 and eta = v_2 - v_3. The endpoint vectors have coordinates

```
(-9/4, 5/4)       and       (3a, a).
```

Both lie in the open half-plane eta > 0. Thus the stated condition for taking the shortest arc is satisfied, even with exact point boxes. Their projective parameters are respectively

```
vartheta(V_K w) = 4/9,
vartheta(U w)   = 4/3.
```

The shorter arc in the parameter circle R/4Z is [4/9, 4/3]. But the attained vector V_(4K+3) w has xi = 0, eta = 2, and hence vartheta = 3. Its direction is outside that arc.

The same failure holds if “shortest” means shortest for the ordinary angular metric on PT rather than for the displayed parameter: the two oriented endpoint vectors make an angle of approximately 106.10 degrees, whereas their shortest projective arc has length approximately 73.90 degrees. The positive combinations travel along the former arc, and not the latter.

The failure also persists if the transposition tau_2 required by the reduced operator is applied before selecting the arc. The transformed endpoint parameters are 5/6 and 3; the attained intermediate parameter is 4/3. The shortest arc between 5/6 and 3 goes through 0 modulo 4 and excludes 4/3. The endpoint vectors still lie in a common open half-plane.

Small sufficiently narrow nondegenerate boxes around the two endpoint vectors have the same defect, so this is not an artifact of allowing point boxes.

### Effect on the proof

The enclosure of h_1 at the images is obtained by considering cells meeting the claimed enclosure of the image (line 2305, and the subsequent block/tail construction). If an actual image direction is omitted, neither the lower nor the upper enclosure of h_1 is justified. The values of the operator at the vertices, as well as the grouped-run bounds, can therefore cease to be enclosures. Proposition `prop:P1` is an otherwise valid implication, but its hypotheses have not been established by this rule.

This directly affects the supplied proof of

```
1.6853 < dim_H N = dim_B N < 1.6854.
```

It consequently also leaves the numerical diffusion conclusion < 0.7766 unsupported by the supplied certificate, since that conclusion uses the upper dimension bound at lines 3511–3512. The specific lower bound > 1.6853 for the three-dimensional gasket also depends on the dimension certificate (line 3279).

This objection does **not** disprove the numerical values. Nor have I established that an omitted direction changes any of the reported final numerical margins. The point is that the stated enclosure procedure is mathematically invalid on its stated domain. A correct implementation could instead retain a common oriented half-plane, take the positive conic hull there, and project that entire hull to PT, even when the resulting arc is longer than the shortest projective arc. Alternatively it could use all of PT in ambiguous cases. The paper needs to specify and justify such a safe rule and verify that the reported certificates use it, or rerun the affected certificates with it.

I did not inspect the deposited source code, so I cannot determine whether the code already makes the correct oriented choice and only its description is wrong. On the mathematical material supplied, this remains a substantive unjustified inference in the verification argument.

## 2. Clarification that is not used as a rejection ground

**Location.** Remark `rem:RP2`, TeX lines 1636–1639, compared with the discussion of global attraction at lines 1016 and 1457–1458 and the explicit Hausdorff convergence in Theorem `cor:singlenode`.

The assertion that the full projective plane, respectively the first quadrant Delta, is a global attractor merely because it is Hutchinson invariant needs an attraction convention. It is correct in the standard one-sided, set-attraction convention for a compact invariant ambient phase space. It is false if “attracts every compact subset” means convergence of its Hutchinson iterates in the symmetric Hausdorff distance: the compact invariant set N, contained in the proper triangle T, has H^n(N) = N and cannot converge to RP^2 or Delta.

The paper uses both the global-attractor terminology and symmetric Hausdorff convergence but does not explicitly define their relationship. I initially considered this a possible contradiction, but I do **not** count it as a substantive error, because the one-sided convention resolves it. The statement should be clarified.

## 3. Review coverage and limitations

I read all 4,102 lines of the supplied standalone TeX, in consecutive bounded chunks, including the embedded bibliography, all mathematical sections and proofs, and the final bibliography. I did not consult other paper versions, other workspace files, other reports, online sources, or other agents. The TeX was sufficient for the mathematical review; I did not independently inspect the rendered PDF or audit its figures.

I checked the following parts of the argument in substance:

- The zone recursion, freeness, soul identities, elementary area/diameter estimates, weak contraction, uniform shrinking of cylinders, and the chain-recurrence proof.
- The singular-value comparisons, derivative comparisons, conversion of the affinity series to geometric zone data, and the cut-out proof of equality of box and Hausdorff dimensions conditional on the stated external dimension theorem.
- The run cocycles, positive-test-function criterion, symmetry reduction, interpolation estimates, and the logic of the numerical verifier. I checked the direction-enclosure step by the exact algebra displayed above.
- The general convex-collar estimates and both parts of the cut-out theorem; the norm/affinity inequality; fastness and the pressure-by-runs argument.
- The analytic reductions underlying the norm-exponent bounds, the higher-dimensional geometry, the polynomial certificate construction for six variables, and the stated counting dictionary.
- The symbolic coding, roof function, Gibbs-state argument, induced return system, entropy inequality, Lyapunov comparison, and the conditional deduction of the diffusion bound.

Apart from the direction-enclosure problem and the terminology clarification above, I did not identify a further definite substantive error in these written arguments. In particular, the comparison inequalities for the infinite scalar sums at lines 2311–2314 have the correct orientation for a convex decreasing function, and the interpolation lemma is not the source of my objection.

The paper's large computer-assisted results rely on test-function files, programs, numerical tables and execution logs outside the supplied paper. I did not inspect or rerun them. Accordingly, reported margins and exhaustive coverage counts are not independently verified here. The claimed external theorems were reviewed as stated and their use within the paper was checked; I did not independently verify their source texts or their proofs. Those are limitations of this review, not additional allegations of error.

The rejection is based on the explicit false geometric inference in the written enclosure algorithm, rather than on provenance, publication status, an inability to rerun a large computation, or a claim that every other argument has been formally verified.

