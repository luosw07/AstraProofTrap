ACCEPT

I found no substantive mathematical error in my review of the supplied current paper. This is a mathematical referee review with the limitations stated below, not formal verification or an independent execution of the computer-assisted certificates.

Reviewed source: `run_20261114/blind/r3n6h8/paper.tex`, 4,102 lines, titled *The Levitt–Yoccoz gasket: dynamics, Hausdorff dimension and norm exponent*.

## Coverage and method

I read the entire supplied TeX source, including the embedded bibliography at lines 13–814, all mathematical text at lines 896–3701, the acknowledgments/tools statement, and the final bibliography through line 4102. I used bounded, numbered extracts; when one extract was truncated, I reread the omitted passage separately. I did not inspect another version, other workspace material, other reviewers' reports, or external references. I did not delegate or use a formal proof assistant. The TeX was the representation used for this review; I did not separately inspect every rendered PDF page.

I checked the actual arguments and their dependencies, rather than treating the stated provenance or cited authors as evidence of correctness. The principal checks were:

- **Geometry and dynamics:** the frame recursion, pairwise-disjoint zone decomposition, cross-product estimates, area formula, diameter decay and growth of matrix norms (lines 1361–1450); the derivative calculation proving strict distance decrease (1498–1520); uniform attraction, uniqueness and the chain-recurrence argument (1533–1602); accumulation of soul points and freeness (1613–1634).
- **Affinity and dimension:** the singular-value estimates and the periodic example (1688–1731); the comparisons between zone diameter, derivative norm and projective singular values (1742–1860); the perimeter/area comparison and the inner-collar argument giving upper box dimension at most the affinity exponent (1862–1921).
- **Transfer-operator certification:** the exact run and derivative cocycles (1932–2050); the positive-test-function criterion (2056–2118); symmetry reduction (2133–2165); the interpolation lemma and the pointwise certificate (2186–2241); and the stated treatment of smooth terms, kinks, blocks and tails (2243–2395).
- **Norm exponents and cut-out gaskets:** the convex inner-collar bounds, including the direction of the Brunn–Minkowski concavity estimate (2449–2464); both parts of the cut-out theorem (2468–2492); the singular-value/norm-exponent comparison (2504–2535); fastness, run pressure and divergence at the critical exponent (2663–2759); the sharp junction bound and uniform contraction (2774–2839); and the cellwise norm-exponent certificate (2859–2915).
- **Counting and higher dimensions:** the permutation bookkeeping for Baragar's tree and the GMR dictionary (2951–3039); the explicit polynomial certificate for the six-variable exponent (3063–3110); the lattice-count example (3114–3134); the three-dimensional zone geometry, volume and surface-area bounds, and the reduction to the norm-exponent certificate (3142–3285).
- **Ergodic theory and diffusion:** the run coding and Hölder roof estimates (3318–3398); application of the stated Gibbs/equilibrium results (3400–3459); the subadditive Lyapunov argument and entropy inequality (3462–3513); the induction/cocycle dictionary (3515–3545); the first-return coding, Gibbs estimates and pressure identification (3547–3677); and the final diffusion deduction (3685–3692).

## Findings

### No substantive error found in the analytic deductions

The main analytic chains of reasoning withstand the checks above. In particular:

1. The comparison used to replace the affinity series by the run operator carries both the norm factor and the directional derivative factor. Proposition `prop:phiD` (1840–1860) and Proposition `cor:certA` (2084–2118) do not silently replace a nonconformal derivative by a scalar contraction ratio. The use of two fixed orthonormal tangent directions is justified by Lemma `lem:DI`.

2. The cut-out proof distinguishes upper box dimension from Hausdorff dimension and uses the quoted dimension/affinity theorem only where needed. The lower-bound argument in Theorem `thm:cutout` (2479–2491) needs only a sequence of sufficiently populated shells, which is enough for upper box dimension. It does not mistakenly infer a lower box-dimension bound from a limsup counting exponent.

3. The three-dimensional application does not apply the lower collar argument where zone boundaries fail to lie in the gasket. The obstruction is explicitly recognized in Remark `rem:octfaces` (3284–3286), and the claimed lower Hausdorff bound instead comes from a face copy of the two-dimensional gasket.

4. The pressure-zero argument is accelerated by maximal runs. Proposition `prop:runpressure` (2715–2759) correctly derives its lower bound on generation weights from submultiplicativity and Fekete's lemma, and separately supplies a strictly decreasing pressure estimate. It does not assume exponential decay for the unaccelerated parabolic system.

5. The diffusion inequality follows from a genuine entropy/singular-value inequality. Dividing the inequality at lines 3502–3508 by the number of runs and using convergence in mean gives
   `s_N lambda_1 + (2-s) lambda_2 + (1-2s) lambda_1 <= 0`,
   hence the displayed bound at 3510. The limiting passage, parameter monotonicity and numerical endpoint at 3512 are consistent.

6. The induced symbolic system is not simply asserted to be a full shift. Lemma `lem:inducedshift` (3581–3601) handles possible overlaps of the prescribed complete path, including return words shorter than that path. Its subsequent Gibbs estimate uses cylinders with the terminal return prefix, rather than identifying an induced cylinder with an unrestricted original cylinder. This distinction is essential, and the proof accounts for it.

### Explicit computational spot checks

Using only formulas and coefficients in the supplied paper, I independently evaluated the polynomial from Table `tab:h5` and truncated its run-operator sum at 3,000 terms per generator. At the simplex origin, a vertex, the face barycenter, the center `(0.2,0.2,0.2,0.2)`, an edge midpoint and a three-coordinate face center, the computed ratios `(tilde L_3 h)/h` were approximately 1.00438–1.00521. These checks are consistent with, but do not prove, the interval certificate at lines 3095–3103.

I also checked:

- The number of ordered grid cubes described at line 3095 is 38,097.
- The partial sum through 999,999 terms of the positive series `S` at 3107 is approximately 0.70453439819, consistent with the stated bound 0.7046. This finite sum alone is not a rigorous upper bound for the infinite series.
- The numerical comparison at 3109 is valid: its left side is 0.0008416447 and its right side is 0.0008602389.
- The diffusion endpoint is `0.2443/0.3146 = 0.776541640178...`, so it is indeed less than 0.7766.

These are diagnostic calculations, not substitutes for directed-rounding verification over the full domains.

### Minor wording point; no effect on a conclusion

At lines 1049–1051, the interval `1.6853 < dim_H N < 1.6854` proves that the first four digits after the decimal point are 6853, as correctly represented by `1.6853...`. The phrase “correct to four decimal places” can instead be read as a claim about rounding to the nearest four-decimal number. The proved interval straddles the rounding threshold 1.68535 and therefore does not establish that rounding. Writing “the first four digits after the decimal point are 6853” would remove the ambiguity. This is a presentation issue, not a substantive error in the theorem or its bounds.

## Limitations material to interpreting this verdict

The sharp numerical dimension bounds in Section 6 (especially 2373–2395), the norm-exponent bounds at 2904–2915 and 3268–3272, and the domain-wide polynomial inequality at 3095–3103 depend on computations whose source code, full test-function data and logs are referred to an external deposit. Those objects are not present in the allowed mathematical input, and I did not retrieve or inspect them. I reviewed the written mathematical certification method and checked the stated numerical consequences, but did not independently establish the reported pointwise certificate inequalities or audit their implementations. In particular, the tiny margins in the sharp dimension certificate make implementation verification consequential.

Likewise, I assessed applications of external theorems as they are stated in this paper. I did not check their numbering, precise original hypotheses, or the faithful representation of the external induction and cocycle against the cited publications. The conditional assertions about suspension-flow entropy at lines 3679–3680 are expressly separated in the paper from the proved base-map result and from the diffusion bound; I have not promoted those conditional assertions to proved results.

Subject to these ordinary review limitations, I found no substantive mathematical error or unjustified inference in the supplied arguments that warrants rejection. The verdict does not claim that every numerical certificate or cited theorem has been independently verified.

