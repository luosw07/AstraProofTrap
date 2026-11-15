REJECT

I found a substantive unjustified enclosure in the computer-assisted proof of the dimension bounds. The rule stated for enclosing a block or tail of projective directions can omit actual intermediate directions, even for the run maps and admissible states in this paper. Thus the claimed pointwise certificate is not justified by the algorithm as described. This is not a counterexample to the numerical value of the dimension.

Review scope and limitations

I read the complete standalone paper.tex, lines 1–4102, including both the embedded bibliography and the final bibliography. I read in bounded chunks and reread the portion affected by output truncation. My mathematical input was this paper alone. I did not consult another version, external references, supplementary programs or logs, other workspace material, or other reviewers. I did not use a formal proof assistant. I used a small arithmetic calculation to check the explicit example below. I reviewed the mathematical source; I did not separately inspect the rendered PDF.

The review covered the zone and frame construction, geometric estimates, the dynamical theorem, the singular-value and cut-out arguments, the run and derivative cocycles, the interpolation and certificate arguments, the general norm-exponent arguments, the Markoff–Hurwitz dictionary and counting deduction, the higher-dimensional constructions, and the symbolic, Gibbs, inducing, and Lyapunov arguments. Published results quoted in the paper were treated as inputs with the stated hypotheses; I did not independently check their accuracy against the cited works. The reported large computer runs and their test functions could not be independently reproduced from the supplied mathematical text.

Substantive finding: the shortest projective arc is not a valid enclosure of positive combinations

Location: Section “The computation,” paragraph “Values at the vertices,” TeX lines 2307–2315, especially the last part of line 2315. The same block/tail mechanism is referred to at lines 2332–2338. The affected proof is the theorem labelled “thm: dimH,” stated at lines 1045–1052 and proved at lines 2393–2395.

The paper correctly observes that the direction vectors for a block are positive combinations of the endpoint vectors, and that for a tail they are positive combinations of V_K(x)w and U(x)w. It then says:

“If the corners of the boxes lie in an open half-plane, we take the shortest closed arc of PT containing their directions; otherwise we take all of PT.”

The open-half-plane condition gives a consistent oriented lift of the vectors. It does not imply that the positive cone between them projects to the shortest arc in the unoriented projective line. If the oriented angle between the extreme vectors exceeds a right angle, the shorter projective arc is the other arc and misses positive combinations.

Here is an example using exactly the formulas in the paper, without arbitrary substitute matrices. Let K be the first index in a tail, let d=K+1, and set

    x=(0,1/2,1/2) in C_1,
    j=2,
    a=1/(4d),
    w=(1-a,-1,a) in T.

Normalization of w does not change any direction. The definitions at lines 2001–2006 and 2301–2305 give

    u=2x_2=1,
    c=(1,-1,0),
    alpha_w=w_2 c=(-1,1,0),
    p_w=w+alpha_w=(-a,0,a),
    V_k(x)w=(1-(k+1)a,-1,(k+1)a),
    U(x)w=(-a,0,a).

Consequently,

    V_K(x)w=(3/4,-1,1/4),
    U(x)w=(-a,0,a).

In the paper's coordinates xi=3v_1 and eta=v_2-v_3, these endpoint vectors are

    (9/4,-5/4) and (-3a,-a).

Both lie strictly in the open half-plane -xi-4eta>0. Thus the rule's stated hypothesis holds, even if their enclosures are exact, degenerate boxes; it also holds for sufficiently small nondegenerate enclosures.

Their direction parameters, using the definition at lines 2168–2173, are

    theta(V_K w)=4/9,
    theta(U w)=4/3.

The shortest arc in the parameter circle between these two values is [4/9,4/3]. However, the legitimate tail index k=4d-1 gives

    V_(4d-1)(x)w=(0,-1,1),
    theta(V_(4d-1) w)=3,

which is outside that arc. This intermediate vector is the explicit positive combination

    V_(4d-1) w = V_K w + 3d U w.

The failure is not an artifact of choosing the parameter-circle metric. In the Euclidean metric of T,

    (V_K w) dot (U w) = -a/2,
    cos(angle(V_K w,U w)) = -1/sqrt(13).

The oriented angle is about 106.10 degrees. Its positive-cone arc is therefore the longer of the two arcs of the projective line.

The relabelling required by the operator does not resolve the problem. After applying tau_2, the two endpoint directions have parameters 5/6 and 3, while the same intermediate run has parameter 4/3. The shorter arc from 3 through 4=0 to 5/6 again omits the intermediate direction. The relabelling is also a Euclidean isometry, so the oriented-angle issue is unchanged.

One may take K arbitrarily large, including the beginning of the final tail beyond 2^28. The example therefore applies to the kind of tail explicitly described in this computation.

Why this is substantive

The direction enclosure determines which image cells are included when bounding h and its derivatives. An arc that omits actual image directions can omit necessary cells, so the corresponding upper and lower enclosures of the transfer-operator terms need not be valid. Proposition “prop:P1” requires genuine enclosures on every set Q; the reported finite checks do not establish its hypotheses using the stated rule.

This is a mathematical failure of the enclosure inference, not a rounding typo. It does not by itself establish that the external implementation makes the same mistake, that a specific final tested cell is miscertified, or that the claimed numerical interval is false. Those distinctions matter. The manuscript nevertheless supplies no additional condition that prevents this case, and no error allowance for directions omitted by this rule. Random tests and sampled ratios do not provide such an allowance.

The four-decimal dimension certificate therefore requires correction or further justification. Conclusions that use its numerical bounds, including the numerical diffusion bound and the stated numerical lower bound for the three-dimensional gasket, inherit this unresolved certificate dependency. The independent theoretical relation between the affinity exponent and the Hausdorff/box dimensions, the abstract test-function criteria, and the separately described norm-exponent certificates are not disproved by this example. Some dependent upper bounds might be recoverable by a separate crude bound on the potentially misenclosed contribution, but that recovery is not established in the paper.

A valid repair is to retain the oriented angular interval determined by a common open half-plane and project that interval to PT without replacing it by the shorter projective arc. Taking all of PT whenever the orientation information is insufficient is also safe. The pointwise certificates must then be checked with the repaired enclosures, or the author must establish that the implementation already uses the correct oriented interval and amend the mathematical description accordingly.

Other assessment

I found no further definite substantive error in the analytic arguments examined. In particular, the frame inequalities, singular-value comparisons, derivative cocycle, cut-out estimates, interpolation inequalities, run-pressure argument, and entropy/Lyapunov calculation have coherent internal derivations. The final symbolic argument carefully distinguishes the entropy-per-return-time statement from the additional suspension-flow assertions it does not prove.

This assessment is limited to the supplied paper and is not formal verification or independent certification of the reported computations. The rejection is based on the explicit enclosure failure above, rather than on publication status, provenance, or the mere use of computer assistance.
