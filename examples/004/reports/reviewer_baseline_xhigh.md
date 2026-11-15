VERDICT: ACCEPT

# Review conclusion

I accept the paper's mathematical argument. Acceptance concerns Theorem 1.2's stated conditional conclusion: using the finite-level Ramanujan–Arthur decomposition of Theorem 1.1 as spectral input, it constructs a global Arthur enhancement for a given cuspidal excursion character that actually occurs. Full reading and rechecking found no substantive mathematical error or unclosed internal proof step requiring rejection.

The key is to retain invariants of every excursion tuple, build one finite-type cyclic support, and force it to meet the open orbit using simultaneous local boundary tests, rather than choose Arthur decompositions pointwise. The current version supplies the required maps and compatibilities between these levels.

# Actual review scope

Read lines 1–5465 of `paper.tex` paragraph by paragraph, including all proofs and references. Principal checks covered main-theorem quantifiers, coefficient fields and continuity, duality and regrading directions in all local models, uniform lower bounds, Ind-coherent/quasicoherent comparison, and the final vanishing/nonvanishing contradiction. An independent finite-dimensional matrix calculation also checked Lemma 8.2's determinant polynomial and weight.

Only the supplied paper was used; no browsing, other versions, external reviews, or experimental material were consulted. References were used as explicitly specified external theorem inputs without checking their originals. The review primarily used the full TeX and did not visually proofread the PDF page by page.

# Key checks

## 1. Main-theorem scope and retention of global parameters

The conclusion of Theorem 1.2 (from line 180) matches the proof's output: an algebraic `SL_2`, a continuous Weil homomorphism into its full centralizer, and a diagonal-specialization identity after one fixed conjugation over all `W_U`.

Proposition 2.6 (from line 834) uses simultaneous-conjugation invariants of every finite tuple. Appending an identity variable converts them into the left-right-invariant functions used by excursion operators. Choosing an actual joint eigenvector rather than only a generalized eigenvector makes these invariants equal the specified scalars in the cyclic quotient ring, as Lemma 3.3 needs.

Finite type has the required finiteness source: after auxiliary Hecke places are fixed, a finite chosen set of matrix coefficients acting on the generating vector reaches only finitely many isotypic components, whose Hecke eigenspaces are finite-dimensional. Thus the relevant matrix coefficients of all Weil elements span a finite-dimensional space in the cyclic quotient. Adding finitely many Lie coordinates gives a finitely generated algebra without requiring the abstract Weil group to be finitely generated.

## 2. An open-orbit point produces the required enhancement

In Proposition 3.4 (from line 1075), both Levi projections are simultaneous-conjugation degenerations and preserve all tuple invariants. Complete reducibilization of the product image retains the `SL_2` nilpotent orbit. The remaining-image closure is reductive as a normal subgroup of the product-image closure; reductivity of the diagonal-specialization image follows from commuting reductive projections.

Lemma 3.3 uses closed tuple orbits and the finite-intersection property to obtain one conjugating element for the whole group. Lifting `SL_2` through a finite center and defining `tau` from the original continuous parameter avoids first proving continuity of arbitrary abstract support points. The commutator map from connected `SL_2` to the finite center is constant, giving genuine commutativity after lifting.

Purity uses orthogonality and the norm equality in the correct direction. The residual logarithmic-absolute-value direction centralizes the whole triple and is orthogonal to its neutral element; Theorem 1.1 fixes the norm of the same nilpotent orbit, forcing the residual direction to vanish. This treats each good place and each complex embedding and allows disconnected triple centralizers.

## 3. Enhancement and Frobenius comparison

Section 4 separately handles enhancements, Frobenius monoidal defects, and mixed central objects, without equating triangulated equivalence with enhanced monoidal equivalence.

Lemma 4.2 retains full bar mapping complexes of derived modules. The torus test retains the infinite polynomial `Ext` tail, matching Frobenius weights in `H^2(BT)`. Finite bar-approximation comparisons first prove constructible-side boundedness, then control coherent upper bounds through images of finitely many simples, using each side's own `t`-structure.

Lemma 4.6 reduces the monoidal defect to a scalar 2-cocycle on the component group; choosing test-place degrees divisible by `|Omega|` makes its power a coboundary. Lemma 4.7's formality argument allows Jordan blocks in equal-weight Frobenius modules: terms in positive mapping-space homotopy groups either vanish by distinct weights or have negative `Ext` degree. The lift then applies to the full multimorphism diagram of IC words, including coherent multiplication and unit data.

Lemma 4.9 supplies weight-filtration comparison for mixed central objects. Extensions of adjacent weights are determined by graded maps on generators; extension kernels in lower weights have no Frobenius-invariant vectors, making later central-object identification applicable to actual mixed objects.

## 4. Local equations, Koszul transform, and the spherical structure sheaf

Lemma 6.2 proves complete intersection using finitely many orbits, each with solution-space dimension `dim H`; the slice retains the identity, keeping every stabilizer part nonempty. Equation count equals codimension, so the Koszul equation algebra has no unwanted negative cohomology.

Proposition 6.3 explicitly uses rational weight direct sums. Positive weights make inverse powers of localized coordinates tend to negative infinity, so maps to bounded coherent targets vanish, supplying the graded-completeness mechanism for full faithfulness. Zero resonance spaces are treated separately.

In Proposition 6.5, equation-Koszul duality and zero-section duality produce identical determinant lines and shifts, which cancel. The annihilator of `W_B` is the intersection of the positive resonance space with the flag nilradical, giving the correct flag-image direction and structure sheaf.

Proposition 6.7 (from line 3690) reconstructs the internal endomorphism algebra through maps with representation coefficients, then proves the spherical retract is a line. Other graded pieces of the complete-intersection self-intersection filtration are positive shifts; vanishing of positive self-`Ext` splits the unshifted piece as a summand of a perfect object. A minimal local free complex excludes multiple nonzero degrees, and the commutative endomorphism algebra forces rank one. The dense torus locus determines shift and character; invariant sections and saturated shrinking give equivariant trivialization. This supplies the actual identification `B = O_Y` used later.

## 5. Parameter dependence and signs in simultaneous lower bounds

Proposition 7.3 places multiple test places in one degeneration fiber, retaining the specified summand of a finite direct sum, auxiliary Hecke actions, and full Frobenius. After pointwise constituent comparison, Proposition 7.4 uses the finite-type ring's nilradical to lift back to the whole finite-dimensional module; it does not assume fibers automatically determine modules.

The numerical bounds of Theorem 7.7 (from line 4501) agree. A test of weight `w` on the dual label has Frobenius absolute value `q^(-D_* w/2)`, while the cohomological weight bound is `q^(D_* b/2)`. Together they give `b+w >= 0`, exactly the regraded degree. `D_*` may depend on finite place sets and labels, but the lower bound zero is independent of them.

Nakayama applies to a finitely generated module over the localized central ring; the ring's origin in an infinite tensor product does not obstruct this form of Nakayama.

Proposition 7.8 compares Ind-coherent and quasicoherent maps through the complete-intersection self-intersection filtration. Uniform lower bounds for the test object and all representation twists provide a least nonzero comparison-cone degree; positive filtration shifts inject it into a comparison cone from a perfect source, a contradiction. This lower bound is the crucial needed condition.

## 6. Boundary tests and the final contradiction

Proposition 8.1 distinguishes the identity class in the slice quotient from the group coordinate itself being the identity, allowing full unipotent residual holonomy. Local-coordinate comparison and final projection to sheared degree zero remain `B`-linear and preserve `f`.

In Lemma 8.2's bad-flag criterion, `delta = m-h` is nonzero and centralizes the triple. The determinant polynomial's evaluation weight is `Tr((ad delta)^2)>0`; vectors in the constructed flag subspace have only nonpositive `delta` weights, so the polynomial vanishes throughout that subspace, excluding the entire open orbit.

Independent matrix check: in `sl_3`, take `m=diag(2,0,-2)`, `x=aE_12+bE_23`. Direct calculation gives

- `det((ad x)^2 : g_-2 -> g_2) = 3a^2b^2`;
- `(ad x)^4(E_31) = 6a^2b^2 E_13`.

The displayed product with exponents is therefore a nonzero constant times `a^12b^12`. For the boundary vector `e=E_12`, take `h=diag(1,-1,0)`, hence `delta=diag(1,1,-2)`. Both the polynomial's `delta` weight and `Tr((ad delta)^2)` are 36, matching the formula and signs.

Lemma 8.3 splits the structure-sheaf unit using a point of the flag, yielding a zero map on derived residue-field fibers. Noetherian support induction in Lemma 8.4 (from line 5017) allows different test maps and nonperfect sources: finite-length devissage at a support generic point, followed by Hom localization, selects an annihilating scalar and factors the map through a bounded coherent object of smaller support. Including all starting indices permits further products to kill that factor.

Finally, Lemma 8.5's simple quotient detects `f`. A spherical endomorphism factoring through a bad flag is an invariant function independent of the raising vector; it vanishes at identity residual holonomy and an open-orbit vector, hence acts by zero at the selected central character. Proposition 8.6's finite total complex then makes `q_Pi^*f` nonzero, contradicting finite-product vanishing on the support for the same vector in the same mapping space. The contradiction chain is complete.

# Boundary cases and editorial matters

The argument covers zero nilpotent orbit, zero resonance space, disconnected triple centralizers, arbitrary multiplicities in level divisors, and coordinate corrections from finite centers and Satake central signs. Divisibility of test-place degrees serves only to clear monoidal defects of finite component groups and is ensured simultaneously by Chebotarev selection.

No substantive error requiring a separate item or typesetting issue affecting the argument was found. The detailed enhanced compatibilities, duality directions, regrading, and boundedness should be retained: they are needed to close the proof.
