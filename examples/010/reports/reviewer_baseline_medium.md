ACCEPT

I found no substantive mathematical error in the supplied complete paper, “Frege's election method: discrepancy, invariant polygons and Farey geometry.” This is an independent mathematical review, not a claim of formal verification.

## Coverage and findings

I read the entire supplied `paper.tex` (lines 1–9080), including the definitions, proofs, examples, boundary discussion, and bibliography. The paper was my only mathematical source. I did not consult other versions, reports, workspace documents, or online sources, and did not delegate the review. I used the TeX rather than inspecting the rendered PDF.

The discrepancy arguments in Sections 3–4 are consistent. In particular, the normalized deficit used in the proof of Theorem `Tchar` is monotone, the estimates linking the successive last-winning times give the claimed factor (2m(m-1)\varepsilon), and the passage from a supremum to a fixed relabelling in Theorem `Tchar2` is justified by finiteness of the possible relabellings. The induction proving sharpness for fixed votes preserves its simultaneous-tie hypothesis before the final perturbation; the perturbation preserves the finite winner itinerary.

I checked the distinctions between the single-valued and multi-valued maps in Sections 5–8. The proof of Theorem `Tinv` does not assume forward invariance of the limit set prematurely: it obtains a compact invariant set from the forward saturation and finite-time entry into a neighbourhood with unique lifts. The invariant-measure proof establishes uniqueness of lifts of Haar measure using almost-everywhere injectivity, and the empirical-measure argument does not require an unjustified continuity assertion for the discontinuous map. The full-dimensional-block argument in Lemma `LTB` handles the additional cutting hyperplanes through its tree of independent normals and the rational-independence contradiction. The later identification of every branch limit set with the attractor follows from full support, rather than from measure convergence alone.

For Section 11, I checked the Farey rectangle coordinates, the first-entry word, the permutation ordering of the orbit points, and the construction and invariance of the upper and lower polygonal paths. I paid particular attention to the boundary assertion (lines 6871–7038): the proof separately checks additional tied segments of the middle winner region, so it does not infer forward invariance merely from Hausdorff convergence. The vertex count distinguishes cutting at a vertex from cutting in an edge. The wall calculations retain the exceptional index in the odd-wall equation, and the odd-wall continuation proof establishes the needed unchanged parent and index bounds. The endpoint formulas and the pairing of odd fractions with their even children agree algebraically.

I also checked the one-dimensional reduction, the intermediate-case examples, the bias discussion, and the divisor-method reformulation. As a supplementary numerical check, I reconstructed the polygon from its stated path formulas and evaluated its area and centroid at four parameter pairs: ((0.30,0.20)), ((0.35,0.05)), ((0.28,0.04)), and ((0.20,0.08)). These sample the first stability domain and the three displayed domains in the (1/3) Farey cell. Each area was 1 to floating-point precision, and the centroid-derived biases agreed with the respective formulas in Example `Ebias3` (lines 4781–4831). These finite numerical checks are corroboration only, not proofs of the general formulas.

## Minor notation issue

At TeX lines 2962–2963, the inverse-image expression is written as `\pi\qw(\vx)` while its quantified torus point is `\hvx`. The intended expression is `\pi\qw(\hvx)`. This is a harmless missing hat, not a substantive error; it does not affect the finite-fibre argument or any claimed conclusion.

## Limitations

The review assesses the arguments supplied in this paper. I have not independently verified bibliographic accuracy or the precise statements attributed to external references. Standard background facts invoked about torus translations, compact groups, convex polytopes, and weak convergence were assessed mathematically without consulting those references. I did not exhaustively compute every Farey cell or independently render the figures. No substantive error or unjustified inference affecting a claimed conclusion was found within this review.
