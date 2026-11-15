VERDICT: ACCEPT

# Review report

## Conclusion and scope

I accept the argument for Theorem 1.2 under Theorem 1.1's finite-level Ramanujan–Arthur decomposition assumption. This review found no substantive error or logical gap invalidating it.

Read all 5467 lines of `paper.tex`, including proofs, conventions, and references, and extracted text from the matching 69-page `paper.pdf` to cross-check theorem numbers and formulas. Principal checks covered global support, the open-orbit criterion, enhanced/Frobenius comparison, Koszul duality and regrading, uniform lower bounds, and the final tensor-vanishing/nonvanishing chains. No browsing, other versions or reviews, or paper edits occurred. Full cited references were not supplied; the review checked explicitly stated citation inputs, applicability, and new deductions.

The conclusion is a global commuting lift of a specified excursion parameter. Its explicit conditional status and identity over the entire Weil group are maintained throughout the proof.

## Key checks

### 1. Global support retains sufficient parameter information

Locations: Section 2, Lemmas 2.1–2.5, Proposition 2.6, TeX lines 472–883.

Matrix coefficients, quadratic cohomological operations, and conjugation invariants of arbitrary finite tuples must all be retained. Independent Weil actions with spectator labels prove matrix-coefficient commutation; fusion gives group and tensor relations, matching coordinates on the abstract group representation scheme. Quadratic operations commute with spectator legs and scale under Frobenius on their own legs, respectively yielding coordinate commutation and

\[
\operatorname{Ad}(\mathbf b(w))\mathbf e=q^{\deg w}\mathbf e.
\]

Finite type uses one fixed auxiliary Hecke point. After fixing finitely many generating representations, all relevant matrix coefficients applied to \(f\) lie in finitely many isotypic components, whose specified Hecke eigenspaces are finite-dimensional. Finitely many matrix coefficients and Lie coordinates therefore generate the cyclic algebra, without requiring all of \(\operatorname{Hom}(\Gamma,A)\) to be finite type.

Proposition 2.6's full tuple identity is essential: appending the identity converts simultaneous-conjugation invariants into excursion left-right invariants; the actual common eigenvector \(f\) then places in \(R\) exactly the information required to recover the given parameter.

### 2. The open-orbit criterion yields a global commuting pair

Locations: Section 3, especially Lemma 3.3 and Proposition 3.4, lines 1041–1234.

Checked the following:

- Scaling places \(b(\Gamma)\) in the Jacobson–Morozov parabolic. Levi projection and removal of the degree-dependent diagonal factor give a homomorphism commuting with the entire triple.
- Semisimplification acts on the whole commuting product image, retaining commutativity and the given nilpotent orbit. Both Levi projections preserve every finite tuple's invariants.
- The diagonal homomorphism has reductive Zariski closure: embed it in the product of the commuting-factor closure and \(\mathbb G_m\); its unipotent radical projects trivially to both reductive factors.
- Closed tuple orbits and the finite-intersection property in Lemma 3.3 provide one conjugator for all group elements, recovering the specified \(\sigma_{\nu,\mathrm{ad}}\).
- After lifting \(\mathrm{SL}_2\) from the adjoint group, define \(\tau_\nu\) using the actual \(\sigma_\nu\). The commutator map from connected \(\mathrm{SL}_2\) to the finite center is constant, so the homomorphism lies in the full triple centralizer; the definition also gives continuity and a finite coefficient field.

The purity norm argument correctly uses semisimplicity. The logarithmic-absolute-value direction \(\lambda_\tau\) is orthogonal to the triple's diagonal direction; their total has the known local Arthur norm, so \(\lambda_\tau=0\). Applying this separately at every closed point and complex embedding covers Theorem 1.2's quantifiers.

### 3. Objects, maps, and Frobenius data in enhanced comparison

Locations: Sections 4–5, lines 1271–2986.

The paper does not take derived traces merely from a triangulated equivalence. It first compares Frobenius on full graded Hom, then uses purity between IC convolution words to lift multimorphism diagrams with composition and tensor operations.

Lemma 4.7's formality calculation works in its stated range: \(k[u,u^{-1}]\) has homological dimension one; different weights have disjoint spectra; equal-weight \(\operatorname{Ext}^1\) does not enter positive homotopy groups of mapping spaces in this pure-complex subcategory. Nontrivial Jordan blocks in pure Weil modules are compatible with this calculation. The order of finite \(\Omega\) kills its second cohomology class, explaining degree divisibility at test places.

For mixed central objects, adjacent-weight extensions carry the classes to compare, while lower-weight contributions have no Frobenius invariants. Invertibility of \(F-1\) then chooses Frobenius-compatible isomorphisms, extending the pure-generator comparison to actual central objects.

I also checked central scalar \(z\), spherical coordinate \(s_{\mathrm{sph}}=zs\), projector index \(c_K\), and duality directions. Section 5 separately follows higher spherical maps and matrix sliding with neutral spectators, covering later Lie coordinates and internal-algebra reconstruction.

### 4. Koszul duality, the spherical summand, and regrading

Locations: Section 6, especially Propositions 6.3, 6.5, 6.7, lines 3159–3860.

The local equation-space dimension calculation uses finitely many centralizer orbits, with each orbit's stabilizer family of dimension \(\dim H\), giving expected codimension and complete intersection. This supports passage from the equation Koszul algebra to an ordinary scheme.

The augmentation differentials \(dp=x\), \(dl=\theta-J_up\) square to zero. Dual generators have original cohomological degrees 1, 2 and weights −2, becoming −1, 0 after regrading. Proposition 6.3 also treats completion-error terms in full faithfulness: on invertible positive-weight coordinates, derived maps from those terms to bounded coherent targets with bounded-below weights vanish. This is a coherent comparison with explicit weight conditions.

Two dualities in the flag transform cancel determinant factors and shifts, yielding \(P_b\) without extra twist. Proposition 6.7 first reconstructs internal endomorphisms using representation-valued tests, then proves the spherical summand a line bundle. Positive self-extension vanishing, complete-intersection self-intersection filtration, minimal local complexes, and commutative endomorphisms establish perfectness, a single degree, and rank one; the central fiber and saturated contraction then yield equivariant trivialization.

The local-coordinate isomorphism only needs to preserve the open orbit and boundary. Contracting unipotent \(u\) inside the open-orbit stabilizer, for both the isomorphism and its inverse, establishes preservation in both directions.

### 5. Parameter dependence in uniform lower bounds is controlled

Locations: Section 7, especially Propositions 7.4–7.5, Theorem 7.7, Proposition 7.8, lines 4305–4642.

The two constituent arguments have different roles, handled correctly. Pointwise Hecke values and Chebotarev here give semisimplifications of linear representations and inclusion of external-tensor constituents; Section 3 uses full tuple invariants to recover the group-valued parameter.

Proposition 7.4 passes from all closed-point specializations to a uniform finite-type-algebra statement using a uniform dimension bound on constituent length and nilpotence of the nilradical, enough to control constituents of \(D_b\).

The full-Frobenius arithmetic bound \(q^{D_*b/2}\) compared with the dual local-label modulus \(q^{-D_*w/2}\) gives \(b+w\geq0\). Although \(D_*\) varies with finite point sets and labels, the lower bound zero does not. Nakayama only needs finite generation, without treating the infinite-tensor-product center as noetherian.

Proposition 7.8 independently compares Ind-coherent and quasicoherent categories. Other complete-intersection self-intersection pieces have form \(Q\otimes W_j[j]\), \(j>0\); contravariant mapping strictly raises their lowest degrees. The uniform lower bound therefore permits contradiction at the least nonzero degree, with the stated shift direction.

### 6. Final vanishing and survival concern the same class

Locations: Section 8, Proposition 8.1, Lemmas 8.2–8.5, Proposition 8.6, lines 4705–5263.

Proposition 8.1 retains frame coordinates and explicitly gives scalar-action direction under the local coordinate-algebra isomorphism. Taking the chosen parity sector and regraded degree-zero source part is \(B\)-linear and preserves the unit's \(f\). Thus \(B\to R_n\to H^0(F_n^{\mathrm{qc}})\to F_n^{\mathrm{qc}}\) is indeed the spherical section for \(f\).

The bad-flag determinant semi-invariant calculation gives

\[
c_\Delta=\operatorname{Tr}(\operatorname{ad}m\,\operatorname{ad}\delta)
=\operatorname{Tr}((\operatorname{ad}\delta)^2)>0.
\]

Relevant flag vectors have nonpositive \(\delta\)-weights, so the polynomial vanishes there; the flag also contains the entire unipotent \(u\). This detects actual local support points. A flag point gives a left inverse to the unit on derived residue fibers, making the fiber arrow \(q_i\) vanish.

Lemma 8.4 was checked separately. Noetherian support induction accommodates pseudocoherent, bounded-above sources that may be unbounded below: each fixed-degree Hom to a bounded coherent target uses finitely many resolution terms and commutes with localization. Finite-length devissage at support generic points kills a finite product; an annihilator \(s\) avoiding these points factors the map through \(\operatorname{fib}(s:K\to K)\), reducing support strictly. Arbitrary starting indices allow subsequent products to continue. This proves vanishing of a finite product of different maps.

In the other chain, a simple Hecke quotient detects \(f\). Every composite through a bad-flag summand back to the spherical summand is an invariant function of local class coordinates alone; it vanishes at an open-orbit point of the central class, hence acts by zero on that simple quotient. The fiber diagram's finite total complex places exactly these images in the denominator of zeroth cohomology, so \(f\) survives. Proposition 7.8 puts vanishing and survival in the same mapping group, closing the contradiction.

## Boundary cases

Checked the zero nilpotent orbit, \(E_t=0\), one test point, nonreduced full-level divisors, possibly disconnected triple centralizers, and parity regrading. For the zero orbit the resonance space is zero, its sole orbit is open, and Section 3 applies directly. Connectedness is used for chosen semisimple-element centralizers \(H_i\); the final theorem still allows disconnected full triple centralizers. Full-level divisor multiplicities remain in finite-level structures and invariant recovery.

## Substantive errors and typesetting

No substantive mathematical error was found, so no error location or repair is proposed. Cross-references in extracted PDF text resolve, with no typesetting issue affecting the argument observed.

Final recommendation: accept the conditional global Arthur lifting theorem proved in the current manuscript.
