VERDICT: ACCEPT

# Referee report

I accept the mathematical argument in the current manuscript. I found no substantive error in the proof after reading the complete text and checking its principal constructions and the connections between them. The two most demanding parts are the passage from finite deformation calculations to a vanishing colimit, and the extension of the local comparison through collision diagonals. The manuscript supplies arguments addressing both, rather than inferring the global assertions from pointwise equivalences.

## Scope of review

I read all of `paper.tex`, including the introduction, all thirteen sections, and the bibliography. I used the complete TeX manuscript as the primary reading copy. The review concerns this supplied version only. I did not consult external sources, other versions, or other reviews. Named external theorems were assessed in the formulations and conventions stated in the manuscript; I did not independently inspect the cited publications. My substantive checks concentrated on the internal proofs, the hypotheses needed for their applications, the distinction between ordinary and renormalized categories, parameter dependence, normalization, and the final categorical deductions.

The following are the principal checks supporting my verdict.

## 1. Twisting, boundedness, and duality

The shifted-level conversion is consistent. With (a=-c), the source exponent used in the proof is

\[
-\frac{a-h^\vee}{2h^\vee}
=\frac{c-h^\vee}{2h^\vee}+1,
\]

so the final source transport is tensoring by the actual adjoint determinant line. The target exponent agrees directly with the claimed level (-1/(rc)). All four exponents remain irrational. Also, (\exp(2\pi i s)) is a root of unity exactly when (s\in\mathbb Q), including when the parameter is allowed to be complex rather than real.

In the inertia-vanishing and cutoff arguments of Section 2 (TeX lines 364–493), the determinant weight is an integer, and irrationality is applied only to a nonzero such weight. Self-duality removes the Euler-characteristic constant term. For the unstable strata, the strict inequality above (\max(0,2g-2)) is sufficient for the required (H^1)-vanishing. The split-section argument supplies the central inertia used there. The passage from individual strata to the full complement uses finite stratifications inside bounded opens, which is the required step for arbitrary objects. The same argument applies to restricted adjoint representations of Levi subgroups, including their centers.

The proof distinguishes categorical duality, represented by the star diagonal, from pseudo-identity, represented by the shriek diagonal. Section 3 retains this distinction throughout. The parabolic adjunctions, determinant splittings, and boundary filtration have the appropriate opposing parabolics. In the induction proving pseudo-identity, the manuscript also checks that the resulting Hom isomorphism is the actual map induced by the functor: the split-epimorphism argument uses bounded coherent cohomology on charts. This resolves a genuine issue that a merely abstract natural Hom isomorphism would leave open.

## 2. Whittaker categories and deformation

Section 4 constructs the continuous projection at finite bounds and calculates it on relevant and irrelevant strata. Its stabilization uses finitely many strata on each bounded-zero open and a uniform Serre-vanishing bound there. The opposite characters cancel in the duality pairing, and the displayed shifts agree with the stratum dimension (\delta_N+a_D). The later use of the direct-sum description is restricted to irrational exponent or exponent zero, as required by its point inputs.

I checked especially the logical separation between the finite rank test and the logarithm colimit test in Section 5 (lines 2445–2632). A vanishing colimit at (q=1) is never substituted for finite-stage vanishing in the rank test. Instead, the logarithm argument first proves vanishing for every finite logarithm length, then uses the degreewise uniform upper weight bound to kill generators of a completed finite module. The proof accounts for the possible (h)-power torsion in the next cohomological degree by using stabilized images. This is necessary for treating (M_i/h^nM_i) as mixed subobjects. Strictness of the weight filtration and the finite generation of (M_i) then produce a single later transition killing that module. The final comparison of transition ranks, rather than just object dimensions, yields the required colimit vanishing away from roots of unity.

The use of Fourier transform is confined to specialized holonomic calculations. The auxiliary-axis projections allow the weight arguments to remain in ordinary mixed geometric diagrams. The manuscript explicitly retains the dilation action when restricting to a nonzero Fourier parameter; it does not use unrestricted base change for a nonproper star image.

Section 6 supplies the uniformity needed for the logarithm argument. The two relative Satake kernels have opposite weight contributions (d_\lambda) and (-d_\lambda). The classical spectral calculation bounds the cohomological degree independently of evaluation representations and their tensor products, since tensoring by a vector bundle is exact and the spectral stack is fixed. The configuration-link estimate gives upper degree (c'-2n); integration over a stratum of dimension (n') gives (E-c'). A simplicial shift ([l]) further gives (E'-c'-l). Thus only finitely many pairs ((c',l)) contribute to a fixed degree. This proves exactly the degreewise uniform bound required earlier, despite unbounded numbers of points and pole bounds. The finite test is applied after this argument, with its ordinary-level vanishing and irrational-level conservativity serving separate roles.

## 3. Moving divisors, the common target, and collisions

Sections 7 and 8 keep finite congruence stages distinct from the full formal curve. In particular, the infinitesimal comparisons use cofinal divisor ideals and common deeper levels; they do not assume that an individual jet group is horizontally constant. The residue pairing on (R[z]/(P)) used in the adolescent calculation remains perfect for repeated roots, which is essential at collisions.

The relative Skryabin construction includes a mapping-complex argument. In the Ext-continuity lemma (lines 5107–5242), the finite difference between depths supplies finitely generated graded kernels, and the induction on Ext degree uses finite diagonals of the resolution spectral sequence. Scalar extension is then justified by flatness and finite Tor dimension. The subsequent fiberwise comparison is applied to these base-change-compatible mapping complexes. The ordinary vacuum is added to the compact image only after its compactness has been established through the pairing adjunction.

The local point calculation produces the precise low-degree gap needed in Section 9: (H^1(G)=H^2(G)=0), while higher cohomology is retained. The argument does not replace this gap with full faithfulness of the unbalanced pairing. Across a divisor, (i^!M) has degrees (0,1); the boundary epimorphism is recovered using the degree-zero mapping comparison, and its transported cokernel is shown to vanish. This is sufficient to propagate the heart equivalence. Derived realization and the retracts supplied by right-adjoint images then establish the DG equivalence.

The two-slot comparison also has an additional argument beyond the one-slot equivalence. Translation of a color produces a free curve factor, the monic equation excludes supported subobjects and quotients on constant heart objects, and the resulting extension is propagated by linearity and realization. The neutral-point collision is checked separately on the generating vacuum cycles. This accounts for the insertion compatibility required later in Ran integration.

## 4. Localization, periods, and the final equivalence

Sections 10–12 retain the parameter derivative in the gauge formula and construct the period map before integrating it. The determinant and dimension identities are compatible:

\[
l^{\mathrm{lv}}=l_N\det(h_E^0/h)^{-1},\quad
\delta=\delta_N+m,\quad
B_E^{\mathrm{lv}}=B_E^0\det(h_E^0/h)[m].
\]

Consequently the normalized period source is (l_N[-\delta_N]\otimes B_E^0), independently of the auxiliary level. The text distinguishes the bounded termwise congruence exhaustion from the continuous derived construction. The incidence/principal-parts calculation and the two-insertion comparison identify the actual maps used in the reductive period square. The nonzero-level requirement for the reductive generation argument is met by the sufficiently deep level chosen for each finite Grassmannian test.

Finally, the formal argument of Section 13 is sound given the preceding results. Essential surjectivity of localization and full faithfulness of its transpose provide the factorization functors. The two displayed inverse candidates have the correct domains; the two separate Plancherel identities give a left and a right inverse, which then agree. This avoids an unwarranted use of (L^RL=\operatorname{Id}). The determinant transport, component/central-character exchange, and the variance in the central-torsor formulas are consistent with the conventions fixed earlier. The construction retains the actual weight and coweight lattices throughout.

## Substantive errors and ordinary typographical issues

I found no substantive error requiring correction, and no ordinary typographical issue that affects a mathematical statement. For readability, the abstract categorical argument extending the low-degree comparison through a divisor could usefully be isolated as a separate lemma, with its exact amplitude and continuity assumptions collected in one place. This is an editorial suggestion, not a condition on the verdict.

The principal reasons for acceptance are the explicit treatment of the finite-to-colimit deformation step, the coherent collision extension, and the compatibility of these results with the finite-level period construction. These are the essential links supporting the final equivalence, and the current text provides them with the needed hypotheses and normalizations.
