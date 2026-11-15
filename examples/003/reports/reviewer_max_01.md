VERDICT: ACCEPT

# Review conclusion

I accept the mathematical argument in the current version. The main conclusion states that for any smooth projective connected complex curve, any connected simple complex algebraic group of a specified global form, and every complex irrational shifted level, the stated full twisted D-module categories are equivalent at negative reciprocal shifted levels, with the localization, collision, and central-torsor compatibilities specified in the text.

This review read all 9170 lines of `paper.tex`, including references, and rechecked definitions, functor domains and codomains, normalizations, parameter ranges, and key finiteness steps in the proof. It used the mathematical content of the complete TeX; as instructed, there was no browsing or consultation of outside literature, historical manuscripts, or reviews. Cited established theorems were adopted in the explicit input form given in the text; the focus was on the manuscript's new arguments and applicability of those inputs.

# Principal checks

## 1. Levels, global forms, and boundedness

The four-category convention in Section 2 matches the main theorem. From

\[
a=-c,\qquad d=\frac1{ra}=-\frac1{rc},\qquad
-\frac{k_a}{2h^\vee}=\frac{c-h^\vee}{2h^\vee}+1
\]

one sees that the required source transformation tensors by the actual adjoint determinant line. The dual-side exponent already matches the main theorem. No square-root condition on the determinant line is introduced. Irrationality survives these rational affine and reciprocal transformations; for nonreal levels the corresponding Kummer monodromy is likewise not a root of unity.

The unstable-direction cutoff in Proposition 2.2 (from TeX line 390) retains two inertia tests: global central cocharacters detect nontorsion degrees, while Levi centers on split sections of maximal parabolics detect excessively large HN types. The latter first eliminates \(H^1\) using root slopes greater than \(2g-2\), then descends vanishing through smooth covers from unipotent extensions, in the necessary correct order. Finite stratifications inside bounded HN opens followed by open exhaustion treat all objects, not just individual strata.

Proposition 2.3 then establishes ordinary categorical duality and kernel calculus. It explicitly distinguishes the duality kernel \(\Delta_*\omega\) from the pseudo-identity kernel \(\Delta_!k\); these are not subsequently conflated. Restricting the original adjoint representation for Levi subgroups also preserves positivity of the trace form on central directions.

## 2. Twisted pseudo-identity and Whittaker models

Before introducing the first adjunction, Section 3 proves cleanness of the compactification kernel and noncharacteristicity relative to the Levi base, then extends the adjunction from compact objects to all objects. The second adjunction separately supplies units, counits, and triangle identities. Inertia weights in the boundary decomposition test the two Levi degrees separately; once only torsion degrees remain, the rational-degree change of a positive defect forces the defect to vanish, giving a finite proper-Levi decomposition.

The final induction in Theorem 3.1 addresses an easily missed point: the natural Hom isomorphism must agree with the actual functor-induced comparison. Noetherianity of locally bounded coherent cohomology upgrades a split-surjective endomorphism to an isomorphism, completing this identification. Descent through central isogenies of reductive groups uses ambidexterity for finite étale gerbes, consistent with the coefficient characteristic.

The Whittaker projector in Section 4 first stabilizes finite averaging on finite bounded-zero opens, then glues through stratum tests. These finite choices depend on the bounded chart and are not incorrectly treated as a single averaging depth over the entire unbounded model. Proposition 4.3 retains opposite characters and the \([-2\delta_N]\) normalization in duality pairings. Proposition 4.4 proves compactness and orthogonality of pointwise standard objects before using local coordinates and parameter D-module coefficients to obtain decomposition on a fixed collision type; the family statement is not inferred directly from pointwise semisimplicity.

## 3. Deformation, colimits, and uniform weight bounds

Sections 5–6 contain the manuscript's most important new work. I especially rechecked Lemmas 5.2 and 5.3, Proposition 6.6, and Theorem 6.7.

Lemma 5.2 (from line 2445) records the Kummer factor as an independent multiplicative coordinate and uses quasi-unipotence of endpoint nearby cycles for non-root-of-unity parameters. It also treats ranks of morphisms in finite diagrams, making it applicable to later transition maps. Exponential characters are first expressed through algebraic translation on an auxiliary axis; Fourier transform is used after field specialization.

Lemma 5.3 (from line 2536) correctly distinguishes vanishing of the special-fiber colimit from vanishing of a finite term. Its required finiteness is finite generation of completed cohomology modules at a fixed stage. A uniform upper weight bound controls deep-power images in long logarithmic coefficients. After homogeneous generators are chosen, they are first killed at finite logarithm length; strictness of weights then kills the whole completed generators. Rank constancy of finite morphisms at nontorsion parameters is used only afterward. A transition stage may depend on the original stage, degree, and stalk, exactly enough for the desired stalkwise cohomological-colimit vanishing.

The uniform bound in Proposition 6.6 handles four unbounded indices. Opposite Satake kernels contribute \(d_\lambda\) and \(-d_\lambda\), cancelling labels; the classical spectral calculation gives a uniform upper degree on a fixed output chart; collision codimension \(c'\) contributes \(E-c'\) after integration; simplicial degree \(l\) lowers this to \(E'-c'-l\). At fixed degree \(j\), only finitely many integer pairs satisfy

\[
c'+l\le E'-j
\]

The weight bound is therefore independent of pole bounds, labels, mark count, and skeleton truncation, supplying exactly the hypothesis needed by Lemma 5.3.

The two roles of finite Whittaker tests are used separately: at zero level they kill the antitempered remainder; at irrational levels they detect object vanishing. Theorem 6.7 invokes conservativity only after the deformation above, closing the proof chain.

## 4. Relative W-algebras and collision extension

Sections 7–9 preserve distinctions between ordinary module categories, renormalized categories, and underlying quasicoherent categories. Section 8 in particular does not transfer arbitrary unbounded ordinary W-module properties directly to the renormalized category. Lemma 8.3 factors through finite mode differences between vacua of different depths, obtaining filtered-colimit compatibility at fixed Ext degree before applying it to scalar extension. Proposition 8.4 can consequently apply pointwise Skryabin comparison to mapping complexes between generators, not just object fibers.

Theorem 8.6 retains closed-field actions, the same principal degrees, relative vacuum representations, and transport along infinitesimal diagonals. Lemma 8.5 proves compactness of ordinary vacua separately, avoiding an inference of compactness from a potentially infinite decomposition.

In Lemma 9.3, matching-label paired mapping complexes are \(H^\bullet_{\mathrm{dR}}(G)\). What extension uses is \(H^0=\mathbb C\), \(H^1=H^2=0\) for connected semisimple groups, together with the \([0,1]\) amplitude of divisor \(i^!\). Proposition 9.4 explicitly identifies boundary surjectivity and uses it to remove cross-pairing \(H^1\) obstructions; heart realization and continuous right adjoints then yield an equivalence of derived categories, going beyond reconstruction of heart morphisms.

The two-slot insertion compatibility of Proposition 9.5 separately handles potential autoequivalences: it constructs \(\beta_S\), then identifies it with the identity through translation of a whole group of marks, a monic cross-collision equation in the translation coordinate, and unique extension without supported subobjects or quotients. At neutral-point collisions it also checks specialization of actual vacuum generating vectors. These steps supply the insertion and collision compatibility needed by the final Ran operations.

## 5. Period comparison and Ran integration

Sections 10–12 retain moving-parameter derivative terms through localization, arbitrary finite Grassmannian kernels, and periods. The conjugation term occurs together with \(\widetilde g^{-1}\partial_v\widetilde g\), giving comparison at the crystalline level.

I checked the normalization cancellation in Section 11:

\[
\delta=\delta_N+m,\quad
l^{\mathrm{lv}}=l_N\det(h_E^0/h)^{-1},\quad
B_E^{\mathrm{lv}}=B_E^0\det(h_E^0/h)[m]
\]

indeed makes the shifted period-map source \(l_N[-\delta_N]\otimes B_E^0\). The finite-dimensional identity \(2\delta-z+a=\delta+e_l\) agrees with the same normalization.

Proposition 12.1 integrates over an incidence Ran space with a specified point, retaining the actual support-forgetting map. For noncommutative unipotent groups, the lower bound on the second weight after bracket degeneration prevents a nonzero cone from remaining invertible under multiplication by the degeneration parameter, effectively returning from the additive calculation to the original group. For reductive groups, both vertical comparisons are checked separately and the commuting square gives the period isomorphism. This part requires nonzero level structure on original marks; the Grassmannian-test application has already chosen sufficiently deep structures satisfying it.

## 6. Global gluing, centers, and boundary cases

The categorical algebra in Section 13 closes. Proposition 13.1 gives localization, hence full faithfulness of its transpose; Lemma 13.2 constructs \(f,f'\). The two Plancherel identities give the displayed left and right inverses with consistent functor domains and codomains. Comparing left and right inverses identifies a single inverse without additional full-faithfulness assumptions.

Global forms are retained in modification labels, Weyl weights, finite centers, fundamental groups, and components. The component sign comes from \(T_D=T_0(-D)\), and the central-torsor formulas match it on automorphisms of the trivial torsor. The low-genus HN bound uses \(\max(0,2g-2)\); nonreal levels use non-root-of-unity monodromy. All these boundary cases fall within the arguments' stated scope.

# Substantive issues and typesetting

This review confirmed no substantive error requiring withdrawal or alteration of the mathematical conclusions and recorded no typesetting issue affecting formula meaning, theorem hypotheses, or proof dependencies.

The publication version should retain the present scope qualifications, especially distinctions between finite calculations and colimits, ordinary and renormalized W-modules, heart comparisons and derived equivalences, and the nonzero level-structure condition in reductive Ran periods. These are essential parts of the current proof.
