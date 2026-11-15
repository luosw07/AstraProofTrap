ACCEPT

No substantive mathematical error was found in my independent review of the current paper, *Frege's election method: discrepancy, invariant polygons and Farey geometry*.

## Scope and method

I read the entire supplied standalone `blind/a9c6/paper.tex`, lines 1–9078, in successive bounded, untruncated chunks, including the definitions, all proofs and examples, the figure construction data, and the bibliography. My mathematical input was exclusively this current paper. I did not inspect other versions, other reviews, or outside mathematical sources, and did not delegate or use a formal proof assistant.

I also checked the adjacent 96-page PDF as the rendered representation, extracted text to locate the corresponding results, and visually inspected pages 68–69, including the two explicit polygon examples and the lower-boundary lemmas. The complete mathematical reading was of the TeX; I did not visually inspect every PDF page.

## Mathematical assessment

1. **Discrepancy bounds and fixed-vote optimality (lines 1693–2440).** The shrinking-set induction proves the harmonic upper bound, and its equality analysis is consistent with the strict fixed-vote bound. The construction in the proof of `T>` correctly inserts a new low-weight candidate: the all-candidate tie provides the induction hypothesis, and the subsequent finite itinerary reproduces the old system up to a common offset and a small linear drift. The stated perturbation resolves the finite list of tied comparisons in the prescribed priority order. In `Tchar`, the nonnegative loss increments and the two estimates involving consecutive last-election times give the claimed ratio bound. The passage from a supremum to a fixed numbering in `Tchar2` correctly handles the possibility that the supremum is not attained.

2. **General dynamics and the ergodic attractor (lines 2444–4372).** Boundedness, compact absorption into `K_0`, backward invariance of the multivalued limit set, and the torus factor are justified. The distinction between a branch orbit and the union of all branches is maintained. The proof of `Tinv` has a valid synchronization mechanism: over a sufficiently small torus neighborhood, the coordinate lower bounds and the zero sum force the unique lift in `K_0`. Finite torus covers then supply uniform absorption of compact sets. The invariant-measure proof correctly establishes uniqueness of the lift of Haar measure outside the exceptional fibers; the empirical-measure argument does not require continuity of the discontinuous map at ties.

3. **Polyhedral structure (lines 3956–4372).** I checked the supporting-hyperplane obstruction in `LTB`, including the graph-tree argument and the rational-independence step. The integer in the congruence is legitimately absorbed using the sum of the vote coordinates, and the zero sum of the coefficients then forces that integer to vanish. The final path endpoint has a nonnegative time coefficient, producing the required contradiction. The subsequent finite-union construction and the support argument justify the conclusions about all branch limit sets.

4. **Rational and intermediate cases, bias, and two parties (lines 2952–3104 and 4375–5019).** The rational-case conclusions are limited to the periods actually proved; the stronger general least-period assertion is explicitly left open. The intermediate examples correctly distinguish backward invariance from forward invariance and show why retaining all tied images can change the limit set. The bias theorem follows from weak convergence with boundedness of the orbit. The two-party recurrence and rounding description are consistent with the discrepancy definition.

5. **Planar construction and its boundaries (lines 5024–7703).** The Farey rectangle criterion, the first-entry itinerary, and the ordered zig-zag construction fit together. The monotonicity of the `f`, `g`, and `h` coordinates establishes simplicity of the paths. The section-by-section proof of `TD` gives equality of the constructed domain and its image. Importantly, the boundary argument in lines 6869–7036 does not simply assume that multivalued invariance passes to Hausdorff limits: it separately checks the extra tied segments and obtains backward invariance by taking convergent preimages. The vertex count distinguishes open stability domains from internal walls and does not claim the same count on cell boundaries.

6. **Global wall classification and divisor methods (lines 7708–8887).** I checked the parity calculations, the minimal-denominator criterion, the endpoint calculations for even walls, and the determinant arguments for odd walls. The latter force a fixed Farey parent and justify preservation of the indices across the relevant cells. The endpoint pairing follows from the displayed Farey identities. The final divisor-method recurrence follows from the stated uniform shift and the weighted winner rule.

## Independent arithmetic checks

I supplemented the argument review with exact rational calculations, without importing mathematical data from outside the paper:

- Constructed polygons at 450 interior parameter samples across all reduced cells with denominators 3 through 18. For every sample, the polygon area was exactly 1 and its intersections with the three winner sectors had areas exactly `p`, `q`, and `1-p-q`.
- Enumerated the nonempty wall equations in cells with denominators through 40. All 1,488 wall instances checked had the stated parity, first-wall slope, and an intersection interval contained in the corresponding prescribed wall segment.
- Checked the polygon centroid calculation against the displayed bias formulas at `(p,q)=(7/25,1/25)` in the second `1/3` stability domain and `(1/5,2/25)` in the third. The first two bias coordinates were respectively `(-157/3750,46/625)` and `(-17/625,23/625)`, in agreement with the formulas.

These finite calculations support the algebra and implementation of the construction; they are not substitutes for the general proofs and do not establish the unbounded-denominator claims on their own.

## Issues and limitations

I found no substantive error or unjustified inference requiring rejection, and no harmless typographical issue worth elevating into a mathematical objection. In particular, I found no contradiction affecting the three principal introductory theorems.

This is a human-style mathematical review, not formal verification. Some local geometric matching and routine algebra were checked through the surrounding construction and representative exact calculations rather than by independently expanding every expression for every parameter. I did not externally verify bibliographic or historical claims, or the full statements of cited prior results. The verdict records that no substantive mathematical error was found within this review; it does not certify that none exists.
