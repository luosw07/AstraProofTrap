VERDICT: ACCEPT

# Referee report

## Scope and recommendation

I reviewed the complete current `paper.tex`, from the abstract and introductory theorem through Sections 2–13 and the bibliography. I used only the supplied manuscript; I did not consult earlier versions, other reviews, or external sources. The cited results were assessed in the forms stated in the manuscript rather than by separately inspecting the cited publications.

After substantive review, I accept the current mathematical argument. I found no substantive error or missing logical step that warrants rejection. This is a particularly long argument, so the following records the main dependencies and checks behind that recommendation.

The manuscript proves the asserted equivalence by combining three constructions: twisted miraculous duality, a global Whittaker–Poincaré identity obtained by deformation, and a local comparison extended over moving and colliding points. It then supplies the required integrated period identity and passes through the localization quotients. The final categorical deduction is valid given these constructions, and the manuscript supplies arguments for the additional family and finiteness properties it uses.

## Principal mathematical checks

### 1. Twisting, unstable support, and duality

I checked the determinant and level conventions in Section 2, including the distinction between the shifted affine level and the exponent of the adjoint determinant. With (a=-c), the source exponent used in the construction is

\[
-\frac{a-h^\vee}{2h^\vee}
=\frac{c-h^\vee}{2h^\vee}+1.
\]

Thus tensoring by the actual determinant line gives exactly the stated source category. The target exponent gives the shifted level (-1/(rc)). No divisibility assumption on the basic form or root of the determinant is introduced by this transport.

The inertia-vanishing argument uses strong equivariance and the nonzero *integral* weight of the twisting line. Its hypothesis is satisfied for every irrational complex exponent, including non-real ones. The Harder–Narasimhan argument uses (H^1)-vanishing only beyond the stated slope threshold. The bounded-denominator and finite-stratification arguments then explain passage from individual unstable strata to the entire complement. The spectator version is relevant and is carried through to the kernel calculations.

Section 3 separates the star-diagonal duality from the shriek-diagonal pseudo-identity. I checked the role of both parabolic adjunctions, the nonzero-defect inertia calculation, and the finite filtration of the diagonal boundary. The induction uses compact Eisenstein generators together with their orthogonal category. The manuscript also addresses the distinction between an abstract natural Hom isomorphism and the actual map induced by the functor, using the bounded coherent, noetherian calculation. The reductive reduction retains the torus factor and the finite central-isogeny descent.

### 2. Whittaker projection and finite-stage deformation

Section 4 supplies the finite averaging calculation on bounded strata, rather than simply assuming a projection on all objects. The unipotent quotient dimension accounts for the normalization (q_D^*q_{D,*}), and the relevant-stratum criterion is compatible with closed increases of pole bounds. The opposing exponent and opposing character cancel in the duality pairing. These facts support the limit/colimit presentations subsequently used.

I checked the distinction in Section 5 between finite deformation and deformation of a colimit. The non-torsion rank lemma is used for finite geometric diagrams; the proof does not infer vanishing of a finite stage from vanishing of an infinite colimit at (q=1). The recording-coordinate argument retains the geometric morphisms, which is essential for the rank assertion on transition maps.

The logarithm colimit test is the central additional step. Its proof accounts for the torsion correction in the universal coefficient sequence: the completed cohomology modulo (h^n) is obtained as a stabilized image, rather than being incorrectly identified with all cohomology at logarithm length (n). Strictness and the functorial complex splitting of the finite mixed Hodge structures allow homogeneous compatible lifts. Killing such a lift at a sufficiently large finite logarithm length forces its entire completed image to vanish because the remaining ideal has a strictly smaller upper weight. Finite generation then produces a single later transition killing the completed module. The rank lemma transfers this zero transition to every non-torsion specialization. This addresses the quantifier issue inherent in passing from finite stages to a filtered colimit.

The pre-axis device is also used consistently: the manuscript applies the projection modulo constant-axis objects and only then identifies the Fourier-specialized exponential calculation. It does not require an exponential connection itself to underlie an ordinary mixed Hodge module.

### 3. Uniform bounds and the Plancherel identity

I checked the parameter dependencies in Section 6. The two Hecke kernels have opposite complex weights; their cancellation removes dependence on the Satake labels. The cohomological bound is obtained from a fixed compact kernel and the classical spectral description. Tensoring a bounded coherent target with evaluation representation bundles does not increase its cohomological amplitude as their weights or ranks vary.

The subsequent configuration estimate has the correct direction. A collision stratum of codimension (c') contributes at most (E-c') after integration, and simplicial degree (l) lowers this to (E'-c'-l). Consequently only finitely many pairs ((c',l)) can contribute to a fixed stalk degree. This is the required uniformity for the logarithm lemma, rather than a bound depending on the number of marked points.

The finite Whittaker test is used in two different ways: it kills the classical anti-tempered cone and is conservative at irrational exponent. The argument applies the deformation lemmas to the tested cone and then invokes this conservativity. This order avoids treating the ordinary-level counit as an equivalence on the entire untwisted category.

### 4. Relative loop and W-algebra constructions

In Sections 7–8 I checked the distinctions between the renormalized categories and the ordinary unbounded module categories. Compact-generation and mapping assertions are made in the underlying quasi-coherent presentations where they are needed. The proof uses common deeper congruence levels for infinitesimally different divisors; it does not claim that a fixed positive-depth jet group remains horizontally constant.

The relative residue pairing on (R[z]/(P)) remains perfect when (P) has repeated roots, so the adolescent-stage calculation includes collisions. The depth-vacuum and Ext-continuity arguments supply the needed base-change statements before the point Skryabin theorem is promoted to families. The ordinary vacuum is placed in the compact image by a separate geometric argument. The common-target construction retains the underlying complex, the vacuum cycle, and the conformal coordinate action.

### 5. Extension across collisions and insertion

The point calculation in Section 9 uses (H^1_{\mathrm{dR}}(G)=H^2_{\mathrm{dR}}(G)=0), giving precisely the low-degree gap needed for a divisor whose extraordinary restriction has amplitude ([0,1]). I checked the propagation of this gap through the localization triangle and the argument identifying the boundary epimorphisms. The latter is necessary to construct an exact equivalence of hearts; equality of pointwise simple labels alone would not suffice.

The proof then treats realization, right-adjoint images, and generation separately to obtain a DG equivalence. The two-slot comparison includes an additional extension argument using translation of a color and checks neutral-point specialization on the extending vacuum cycles. Thus insertion compatibility is established beyond the distinct-point locus.

### 6. Periods, Ran integration, and the final equivalence

I checked the normalization in Sections 10–12. The identities

\[
\delta=\delta_N+m,\qquad
l^{\mathrm{lv}}=l_N\otimes\det(h_E^0/h)^{-1},\qquad
B_E^{\mathrm{lv}}=B_E^0\otimes\det(h_E^0/h)[m]
\]

indeed reduce the shifted source of the level period map to (l_N[-\delta_N]\otimes B_E^0). The finite-dimensional chain-to-cochain conversion supplies the stated determinant and shift. The construction distinguishes bounded ordinary calculations using (M[J]) from the derived continuous construction, so it does not rely on exactness or nonflat base change for a fixed invariant submodule.

The incidence computation identifies the actual forget-support map on principal parts. The unipotent deformation has a second-weight lower bound in each fixed positive-height degree, which justifies using its zero-bracket fiber. The reductive argument proves both vertical comparisons in the displayed square before concluding the integrated period identity. Descent from Grassmannian tests uses full faithfulness on continuous functionals and retains parameter operations.

Finally, Section 13 has correctly typed factorizations through the fully faithful transposes of localization. The displayed left and right inverse candidates compose with the constructed functor to the respective identities. Their equality then proves the equivalence. The component/central-character exchange and torsor compatibilities use the same gluing convention and remain consistent with the determinant transport.

## Errors and typographical matters

I found no substantive mathematical error to report. I also found no ordinary typographical issue that changes a mathematical statement or obstructs the argument. The manuscript is lengthy, but the explicit separation of finite, renormalized, and family constructions is relevant to the proof rather than merely expository repetition.
