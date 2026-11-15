VERDICT: ACCEPT

# Review conclusion

I accept the current mathematical argument. Main Theorem 1.2 assumes the finite-level Ramanujan–Arthur decomposition in Theorem 1.1; using cited inputs as explicitly stated, the derivation forms a closed proof chain. This review found no step requiring classification as a substantive error.

This judgment comes from reading and checking the complete proof, focusing on global support retaining full excursion tuples; recovery of the original parameter from an open-orbit point; Frobenius-compatible enhancement and horizontal trace; Koszul duality and regrading; bounds independent of test-place count; and final vanishing/nonvanishing of the same cuspidal class.

# Actual review scope

Read `paper.tex` lines 1–5467, including all eight sections and references; also extracted text from the matching 69-page PDF to check sections, proposition numbers, and main statements. No research outside the input directory, browsing, other versions, reviews, or experimental records were used, and the paper was not edited. Auxiliary work comprised locations, PDF extraction, and the algebraic calculation below.

Cited originals were not supplied. Thus Theorem 1.1 and explicitly invoked Satake, central-sheaf, shtuka smoothness/finite-generation, nearby-cycle, coherent-trace, and purity results were treated as literature inputs. Their applicable objects, required compatibilities, and logical interfaces were checked without reproving them.

# Key checks

## 1. Global support and preservation of the specified parameter: Section 2

Lemma 2.3's matrix-entry construction uses commuting Weil actions on separate legs and tensor relations after fusion, giving the coordinate-algebra action of abstract group homomorphisms. Lemma 2.4 places degree-two operations and spectral coordinates in one commutative algebra, checking Frobenius scaling on their own legs and commutation with spectators. The relation is

\[
\operatorname{Ad}(\mathbf b(w))\mathbf e=q^{\deg w}\mathbf e,
\]

with the direction needed by later positive resonance.

Proposition 2.6 uses a fixed auxiliary Hecke point for finite type. Matrix entries from finitely many representations applied to the cuspidal eigenvector lie in finite-dimensional Hecke eigenspaces of finitely many isotypic components. Entries from arbitrarily many Weil elements thus span a finite-dimensional space; adjoining finitely many Lie coordinates gives finite type without finite generation of the Weil group.

Appending the identity converts simultaneous-conjugation invariants to excursion left-right invariants while retaining all invariants of every finite tuple, as required to recover the same parameter in Section 3.

## 2. Open-orbit criterion: Section 3

Lemma 3.1's test-place selection meets two independent requirements: Frobenius in a sufficiently small identity congruence neighborhood and degree divisible by \(|\Omega|\). Logarithms and Weyl stabilizers explain simultaneous connected centralizers and local central-torsor descriptions.

In Lemma 3.2 the compact factor has zero absolute-value direction, placing \(\Lie H\) in \(m\)-weight zero and \(E_t\) in weight two. The triple's raising operator surjects from weight zero to two, giving the open orbit. Given raising and neutral elements, the lowering element is unique, making its stabilizer reductive.

Both Levi projections in Proposition 3.4 preserve all tuple invariants. The second makes the product-image closure reductive, then the diagonal-specialization closure is reductive too, so Lemma 3.3 applies to it and \(\sigma_{\nu,\mathrm{ad}}\). Noetherianity turns finite-tuple conjugacy conditions into one uniform conjugator. After lifting to \(L\), the finite center and connected \(\mathrm{SL}_2\) ensure actual commutation; defining

\[
\tau_\nu(w)=\sigma_\nu(w)\widetilde h(a^{\deg w})^{-1}
\]

directly gives continuity, a finite coefficient field, and the whole-Weil-group identity.

Purity follows from the correct norm argument: the absolute-value direction centralizing the triple is orthogonal to its neutral cocharacter; the norm fixed by Theorem 1.1 forces the residual direction to vanish. This works for each complex embedding and allows disconnected triple centralizers.

## 3. Enhancement, Frobenius, and transfer: Sections 4–5

I specifically checked whether triangulated equivalence was used directly as enhanced equivalence. Extra lifting steps are supplied: nonzero-degree Hom vanishing on free-monodromic tiltings compares enhancements; full derived-module mapping calculations impose zero monodromy in both Cartan directions; multimorphism diagrams of pure IC words finally lift convolution and Frobenius.

Lines 1708–1818 retain full derived mapping complexes while contracting the intermediate exterior algebra and using finite bar skeleta. Approximation-cone upper bounds tend to negative infinity; boundedness is proved first on the constructible side, then transferred to the coherent side with a fixed finite set of simples. This does not assume the ambient equivalence preserves perverse and ordinary coherent t-structures.

In Lemma 4.7, equality of weight and degree eliminates Hom and Ext between different weights; equal-weight Ext¹ does not enter the relevant positive-homotopy mapping groups. This supplies coherence for multiple compositions and tensor operations. Mixed central objects are separately compared by weight filtrations; extensions below adjacent weights have negative weight, allowing successive Frobenius-invariant comparisons.

Positive polynomial degrees in the central Weil factor are removed successively using invertibility of \(1-r^{-m}\); the remaining scalar gives a finite central element \(z\). Later spherical coordinates use \(s_{\rm sph}=zs\), retaining that factor.

Horizontal trace and projector transfer use the same unshifted flag kernel in \(l_Vi_V=c_K\operatorname{id}\) and \(i_Vl_V=\chi_C\); \(c_K\ne0\) is invertible in characteristic zero. Neutral spectators, sliding matrices, and actual higher spherical maps are also compared, providing map-level support for Section 6's internal-algebra comparison.

## 4. Local equations and Koszul calculations: Section 6

Finitely many resonance orbits give dimension \(\dim H\), the expected equation-space dimension. Negative equations and sheared positive equations are therefore ordinary complete intersections; flag-model equations retain derived structure throughout, with distinct later uses.

Proposition 6.3 calculates the augmentation resolution using rational weight direct sums. Positive coordinate weights make localized telescopes eventually reach empty weight spaces when mapping to bounded coherent targets, proving the required full faithfulness. Both duality formulas in Proposition 6.5 contain \(\det(F)[-n]\), whose cancellation explains the absence of extra shifts or character twists in flag images.

For a low-rank check, take \(L=\mathrm{SL}_2\), nonzero resonance, and \(H=T\). The local positive equation is

\[
(\alpha(u)-1)e=0.
\]

The two fixed-flag types give this equation space and the zero-vector section, matching \(P_b\). Cancellation of determinant factors and degrees between coordinate regular sequences and equation Koszul complexes in augmentation duality also agrees with this example.

Proposition 6.7 reconstructs internal endomorphisms first, then uses complete-intersection self-intersection filtration and positive self-extension vanishing to prove the spherical summand a shifted line bundle, removes the shift, and trivializes equivariantly locally. Its final open-orbit preservation contracts unipotent elements to the identity using reductive open-orbit stabilizers, matching the residual unipotent holonomy actually occurring in Section 8.

## 5. Parameters and uniform lower bounds: Section 7

Nearby-cycle comparison uses a finite separable curve map and Weil restriction to place finitely many degenerations at one point. Original finite level is recovered by finite-group invariants at deeper level; characteristic zero preserves summands and comparison isomorphisms.

Proposition 7.4 first obtains continuous representations at points of a finite-type matrix algebra, then uses Chebotarev to compare semisimplifications of algebraic representations. The nilradical lifts pointwise constituent constraints to whole finite-dimensional modules, enough for later weight estimates.

Regrading signs check as follows: original degree \(b\) and total dual-representation \(m_i\)-weight \(w\) give new degree \(b+w\); full Frobenius modulus is \(q^{-D_*w/2}\). Comparing with \(q^{D_*b/2}\) gives \(b+w\ge0\). \(D_*\) may vary by places and labels, while zero remains fixed. Finite generation precedes Nakayama, so the infinite-tensor-product center needs no additional noetherian assumption.

Ind-coherent/quasicoherent comparison is claimed only for the specified thick subcategory. Positive shifts in complete-intersection self-intersection filtration raise the first nonzero comparison-cone degree, giving the contradiction in the correct direction.

## 6. Final contradiction: Section 8

The support map in Proposition 8.1 is affine: one frame eliminates the diagonal \(A\)-action, leaving \(A^{n-1}\times\operatorname{Spec}R\). Projection to regraded degree zero is \(B\)-linear because the local equation ring is concentrated there, and preserves \(f\).

Lemma 8.2 gives the discriminant character for \(\delta=m-h\):

\[
\operatorname{Tr}(\operatorname{ad}m\operatorname{ad}\delta)
=\operatorname{Tr}((\operatorname{ad}\delta)^2)>0.
\]

The selected flag subspace has nonpositive \(\delta\)-weights, so the discriminant vanishes there, supplying bad flags covering boundary points and containing the whole residual unipotent element.

Lemma 8.4's successive tensor vanishing was checked step by step. Pseudocoherent bounded-above sources and bounded coherent targets give Hom localization; generic-point finite-length devissage gives finite-stage vanishing, prime avoidance shrinks support strictly, and a later tensor segment completes induction. Different places may use different maps, and arbitrary starting indices are retained, precisely as the application needs.

Finally, vanishing concerns the same \(q_\Pi^*f\). Conversely, a simple cuspidal Hecke quotient detects \(f\); bad-flag idempotents vanish on it, allowing the same element to survive in the cone's zeroth-cohomology quotient. Objects, local central values, and transfer directions agree, giving the required contradiction.

# Boundary cases

Checked zero nilpotent orbit and \(E_t=0\), the \(W=0\) Koszul case, disconnected triple centralizers, level divisors with multiplicities, any finite number of test points, and changes in Frobenius paths and sufficiently divisible powers. Zero resonance, trivial Koszul cases, finite-center lifting, finite-level invariants, and tuple conjugacy respectively handle these cases, matching the main conclusion's quantifiers.

# Substantive errors and typesetting

Substantive mathematical errors: no correction item is needed.

Typesetting: text/formula location checks found no issue affecting the argument. Figures were not independently inspected pixel by pixel.

# Final recommendation

Accept the conditional argument. Its key advance connects complete excursion-tuple support, map-level local comparisons, uniform regraded lower bounds, and successive tensor vanishing to the same cuspidal eigenvector. These interfaces have concrete arguments, checked in this review.
