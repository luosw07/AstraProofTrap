ACCEPT

I found no substantive mathematical error or invalid inference in the supplied manuscript under the stipulated review-as-written condition.

## Coverage and method

I read the complete `paper.tex` (lines 1–9078), including all theorem statements, proofs, remarks, examples, the introductory summaries, and the bibliography. I inspected the supplied external figure assets, including rasterized versions of the four PDF figures. The mathematical review was based on the full source text; I did not separately reread every page of the matching PDF. I used no external mathematical sources, other versions, private records, other reviews, or formal proof assistant. References below use the manuscript's TeX labels to identify the exact results unambiguously.

I assessed the arguments actually supplied. In particular, I did not replace the compact-invariance argument by a theorem about essential invariance, infer boundary invariance merely from continuity of a discontinuous map, or assume that a rational orbit has the conjectured least eventual period. The manuscript supplies separate arguments where those distinctions matter.

## Discrepancy results

The backwards sets in the proof of `T<`, equations `at` through `qu7`, give the claimed harmonic upper bound. Both possibilities for the change of the backwards set are covered, and the normalization by its cardinality is consistent. The lower-bound induction also works for zero vote proportions.

The equality analysis in `TL=` correctly propagates equality back through the inequalities and extracts the successive last-election times. Its treatment of the possible interval after the last strict decrease of the backwards set is explicit. The time-homogeneous strict inequality in `TR<` then follows by excluding a zero-vote candidate and applying the smaller-dimensional bound.

The induction in `T>` establishes the stronger simultaneous-tie hypothesis as well as the near-optimal discrepancy. The return to zero after the integer period uses both the coordinatewise lower bound and conservation of the sum. The new candidate cannot win prematurely; after its prescribed win, the finite interval used to reproduce the old itinerary is controlled. The initial perturbation argument specifies a perturbation whose ordering agrees with the chosen highest-index tie convention, so it supplies the stated robustness of the strict terminal inequality.

In `Tchar`, the nonnegative loss increments, the estimates at successive last-election times, and the final ratio bound have the required directions. The numerical smallness condition used in `fa5` is consistent with the claimed constant. The supremum issue in `Tchar2` is addressed by applying `Tchar` with epsilon plus eta and taking a subsequence with a fixed numbering. The reduction in `TR<<` likewise handles a supremum rather than assuming its attainment.

## General dynamics

The boundedness and absorption arguments distinguish arbitrary initial states from states of coordinate sum zero. Compact uniform absorption follows from the uniform bound on the first win of each positive-vote party. The multi-valued backward-invariance proof `Lback` uses compactness and finitely many possible immediate preimages correctly.

The torus projection results `LP` and `LG` have the appropriate finite-fibre and compactness ingredients. In the rational section, `TQ` proves exact period for the stated small initial cube. For arbitrary initial states the manuscript proves eventual periodicity and divisibility of its period by the torus period, and explicitly leaves equality of these periods open. I found no use downstream of that stronger conjectural assertion.

For ergodic parameters, `LC` obtains constant multiplicity almost everywhere from backward invariance, conservation of Haar measure, and ergodicity. The exceptional tie projections are null in the relevant full-dimensional torus. The neighbourhood argument in `Tinv` uses the coordinate lower bound and integer coordinate differences to obtain a unique lift near zero. The ensuing finite torus covering yields uniform finite-time absorption of compact sets and uniqueness of the compact invariant set. These arguments retain all allowed images at ties.

The measure theorem `Tgl` includes the required uniqueness-of-lift argument for measures with Haar projection. Its existence direction establishes that the proposed lifted measure gives zero mass to ties before taking its image under the multi-valued map. The empirical-measure proof works for the stated choices of points from the iterates; its compact-set Portmanteau argument does not require continuity of the Frege map at ties.

The full-dimensionality argument in `LTB` was a particular focus. The marked independent normals give a tree; along its path, the only possible coefficient minus one from a current cutting hyperplane is at the first edge. The final edge coefficient consequently has the sign needed for the contradiction. The proof explicitly handles the integer term in the rational-independence argument by using the sum of the vote proportions and the zero sum of the difference coefficients. This supports `TB`, and then `Lpoly-support`, `TsupportK`, and `TX` give the announced equality of every branch limit set with the attractor.

The intermediate-case theorem `Tmu` uses its additional null-tie hypothesis on the orbit coset, rather than assuming ambient Lebesgue nullity suffices. The examples `Einter1` and `Einter2` appropriately distinguish orbit closures from invariant domains and demonstrate the effects of retaining or discarding tied branches.

## Planar construction and parameter classification

I checked the coordinate conventions, the winner inequalities, the translations, the Farey-coordinate transformation, and the relationship between neighbouring fractions and first entry into the middle sector. The endpoint identities for `P_b`, `P_d`, and `P_v` agree with the ceiling convention. The exceptional point `W_0=X`, which differs from `P_1=Z`, is handled explicitly in `LQ4`.

The ordering lemma `Lm3-shadowing` gives the signs needed for the zig-zag construction. The special middle replacement, periodic extension, and lower translation are consistent with the sector geometry. The proof of `TD` uses sections by constant-g lines, including both choices on the zero section, to establish the equality of the domain and the union of its translated pieces. The area argument then establishes disjoint interiors of those images.

The separate proof of the boundary assertion in `Rrand` is important: it first handles strict winner interiors, then treats the limiting middle piece and additional tie segments, and finally establishes backward inclusion by converging preimages with a fixed branch. Thus the claimed boundary invariance is supported by more than Hausdorff convergence alone.

In `TSD`, the cut-point condition becomes strict affine inequalities for a fixed edge, and an affine equality for a fixed vertex. The bounds in `LW1` reduce the periodic offsets to two choices. The even and odd wall formulas in `TW2` include the exceptional peak and middle-piece conventions. The cylinder count in `Tm3-4v+3` accounts for the difference between cutting an edge and cutting a vertex, giving the stated two vertex counts.

I followed both parity cases of `Twalls`. The even case identifies the denominator threshold and the closest qualifying fraction. The odd case uses the determinant and parity constraints to identify the reduced axis intercept and preserve the appropriate Farey parent; the continuation argument tracks the same ceiling data across cell crossings. Its endpoint calculation and the exclusion of further wall continuation use the index bounds. Finally, the two endpoint comparisons in `ConjFarey+lines` agree with the formulas for the adjoint even child.

The explicit examples, the bias discussion, and the final divisor-method change of variables are consistent with the surrounding definitions. The bibliography was read as supplied; historical and bibliographic assertions were not checked against outside publications.

## Findings under the no-repair condition

I identified no substantive incorrect proof step requiring a correction and no counterexample to a stated theorem. I therefore have no defect list or repaired proof to provide. The verdict concerns the supplied mathematical arguments and their stated hypotheses, with the coverage described above.
