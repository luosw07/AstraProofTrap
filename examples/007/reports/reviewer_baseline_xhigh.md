VERDICT: ACCEPT

# Review conclusion

Accept the mathematical argument in the current version. The paper establishes two main new comparisons: a global Whittaker–Poincaré identity at irrational exponents, and a local pairing comparison compatible with collisions and insertions. The period formula and localization quotient functors combine them into the stated global equivalence. Taking the explicitly stated external theorems as established inputs, the key hypotheses, parameter conversions, and final categorical composition agree.

# Actual review scope

Read all lines 1–9170 of `paper.tex` in the specified directory, including every proof, the final central-action argument, and the bibliography; then rechecked key dependencies and several basic operations. No other paper versions, historical reviews, or experimental material were read; no network access or paper edits were made. This mathematical review used the complete TeX; it did not independently inspect the PDF page by page. The original external references were outside the supplied input: the review adopted the external results explicitly listed in the paper and checked their uses, hypotheses, and connections to subsequent steps.

The principal checks affecting the conclusion follow. Locations use sections and TeX line numbers, retaining LaTeX equation or proposition labels for precise lookup.

# Key checks

## 1. Levels, twists, and global forms

Section 2, especially `foundations:levels` and `foundations:four-categories`, and the final parameter conversion in Section 13 use consistent conventions. If

\[
a=-c,\qquad d=1/(ra),\qquad k_a=a-h^\vee,
\]

then the source exponent is

\[
-k_a/(2h^\vee)=(c-h^\vee)/(2h^\vee)+1.
\]

Thus the source correction really is tensoring once by the actual adjoint determinant line, while the target has exactly the required exponent. The exponent at the opposite level also differs from the opposite twist by the integer one. These operations work for the given global form without requiring a square root of the basic level line.

For complex irrational parameters, `exp(2πis)` is a root of unity exactly when `s` is rational. Hence “not a root of unity” in the deformation argument matches the main theorem's irrational-exponent condition, including nonreal parameters.

## 2. Irrational inertia weights and finiteness

Section 2, `foundations:cutoff` from line 390, first excludes nontorsion degrees by central weights, then excludes sufficiently unstable directions using the HN stratification. Two conditions require checking: vanishing of `H¹` when the HN root slope exceeds `2g−2`, and a strictly nonzero weight of the chosen central cocharacter on the determinant line. The root-height filtration, positivity of the trace form, and positivity of the inverse Cartan matrix supply both.

The passage from stratumwise vanishing to vanishing on the whole complement uses a finite stratification on bounded HN opens, then detects objects by open exhaustion, avoiding an unsupported inference from infinitely many strata. The proof works for both opposite exponents and external spectators, supporting later duality and kernel operations.

## 3. Structure of the twisted pseudo-identity proof

The induction in Section 3, `pseudo:equivalence` (from line 749), uses actual adjoint functors and their natural maps. Nonzero defects in the boundary decomposition first descend to Levi Hecke data and are excluded by central-inertia vanishing; the remaining terms factor through constant-term and Eisenstein functors for proper Levi subgroups.

Lines 1360–1470 deserve particular attention: an abstract Hom isomorphism is not simply treated as the full-faithfulness map induced by a functor. Enriched Yoneda and the Noetherian property of bounded coherent cohomology verify that the actual comparison map is invertible. The Eisenstein-generated part and its orthogonal then cover the whole category. Descent along finite central isogenies retains both signs and uses conservative pullback in the required degrees.

## 4. Finite deformation and infinite colimits are handled separately

Section 5, `deform:rank` (from line 2445), treats finite geometric calculations only. Its nontorsion-parameter conclusion uses a recording coordinate, quasi-unipotent nearby cycles, and cleanness of Mellin integration. For morphisms, the proof controls ranks of maps, not merely Euler characteristics of objects.

`deform:colimit` (from line 2536) separately treats infinite colimits. Three key points were checked:

- Vanishing for finite logarithm length follows from length-one vanishing and finite extensions.
- Quotients modulo `h^n` of completed cohomology modules acquire mixed Hodge structures through stable images, retaining torsion from the next cohomology group.
- A uniform upper weight bound strengthens “some finite logarithm length is killed” to “a finite generating set for the whole completed module is killed by one later transition.”

Only then does rank constancy of finite transition maps transfer generic vanishing to every non-root-of-unity parameter. This order resolves the crucial logical issue between finite stages and infinite colimits.

## 5. Index control in the uniform weight bound

In Section 6, `planch:vacuum-weight`, `planch:satake-degree`, and `planch:weight-estimate` (the last from line 3800) handle different unbounded indices.

The two Satake kernels have weights `d_λ` and `−d_λ`, cancelling label dependence. The spectral cohomological bound uses the coherent complex associated with a fixed compact input; tensoring by any evaluation representation bundle is t-exact, so neither highest weight nor rank enlarges the upper bound. For collision codimension `c′`, the local link degree is `c′−2n`, and the integration dimension is at most `2n′`, yielding `E−c′`. Simplicial degree `l` further lowers this to `E′−c′−l`.

For fixed cohomological degree `j`, only the finitely many nonnegative integer pairs satisfying `c′+l≤E′−j` can contribute. Thus the final weight bound is independent of point count, pole bounds, labels, and finite skeleta. Together with conservativity of finite Whittaker tests, this closes the argument for `planch:identity`.

## 6. Moving divisors and relative W-modules

Sections 7–8 distinguish finite depth, the full formal disk, and crystalline directions. Two divisor equations differing nilpotently are compared through cofinal powers of ideals; compatibility is realized at deeper common levels, without assuming that a fixed jet group stays unchanged under moving parameters.

The free PBW presentation in `walg:vacua` provides concrete objects for residue-field detection and later scalar extension. `walg:ext` (from line 5099) constructs factorizations from finite mode-coefficient differences between two depth vacua, and proves continuity through successive Ext formulas. It does not assume beforehand that all generalized vacua are compact in the ordinary unbounded derived category; compact images in the relative renormalized category and the inclusion of ordinary vacua are treated separately afterward.

The common-target theorem also checks cutoff conditions after replacing homogeneous generators, coordinate actions, and horizontal vacuum vectors. These are the extra data needed to extend pointwise Feigin–Frenkel duality to collision families.

## 7. Collision extension and two-slot insertion

Section 9, `local:point-gap`, uses `H¹_dR(G)=H²_dR(G)=0` for semisimple groups to obtain a low-degree gap. `local:one-slot` (from line 5903) combines it with the `[0,1]` amplitude of divisor `i^!`.

The boundary-surjectivity step was checked particularly closely: degree-zero maps in the common target identify the two boundary morphisms, and the equivalence of closed-stratum hearts detects their cokernels. This retains gluing data beyond merely comparing open- and closed-stratum objects. Realization and generation by images of right adjoints then give a DG equivalence.

`local:two-slot` (from line 6090) separately proves insertion compatibility. After translating an entire color, cross-color collisions are described by a monic polynomial in the translation variable. Constant heart objects have no subobjects or quotients supported on this divisor, so the existing open comparison extends uniquely. Collisions with neutral points also check specialization using actual highest-weight/vacuum periods and torsion-freeness over a DVR. This supplies the insertion data still needed after a one-slot equivalence.

## 8. Periods, Ran integration, and normalization

Localization, arbitrary Grassmannian kernels, and period calculations in Sections 10–12 retain parameter variables throughout. `loc:gauge` includes the logarithmic derivative of moving parameters; Spencer and Lie Poincaré duality calculations on finite quotients give both determinant lines and shifts.

After checking `eq:T9`, the horizontal source, normalized by `[-2δ]`, indeed becomes the fixed `l_N[−δ_N]⊗B_E^0`. Thus auxiliary-depth determinants and dimensions cancel in the final period formula.

The Ran argument first performs incidence/support calculations for principal parts, then treats unipotent and reductive inputs by finite symmetric degrees and finite filtrations. The noncommutative unipotent degeneration uses a bigrading: at fixed first weight, the second weight is bounded below, excluding a residual term with invertible `t` and zero special fiber. The two insertion comparisons then give the two vertical isomorphisms of the reductive square. This proves `loc:period-comparison` while retaining descent under arbitrary finite Grassmannian tests.

## 9. Final categorical composition and central data

In Section 13, `equivalence:factorization` from line 8463 uses essential surjectivity of localization and full faithfulness of its transpose to produce `f,f′`; continuity is detected through a continuous fully faithful embedding.

The two candidate inverses displayed after `eq:G4` have the correct domains and codomains. The Plancherel identities for the two groups give a left and a right inverse, and

\[
\Psi_{\rm left}\simeq\Psi_{\rm left}\Phi\Psi_{\rm right}
\simeq\Psi_{\rm right}
\]

identifies them. This final step requires no additional assumption that the localization right adjoint is continuous.

The central-character/component exchange `(η,p)↦(p,−η)` agrees with the degree sign of the Cartan bundle `T_0(−D)`. Transgression of central torsors is defined at the torsor-groupoid level; automorphisms of the trivial torsor finally check the signs in both formulas. Integral determinant translation arises from the adjoint representation and preserves these central data.

# Substantive issues and typesetting

This review found no item requiring classification as a substantive mathematical error. Infinite colimits, collision gluing, moving parameters, and normalization each have separate arguments that connect to the main conclusion in the checks above.

No TeX typesetting issue affecting mathematical meaning was found; page-by-page PDF layout inspection was outside this mathematical review.
