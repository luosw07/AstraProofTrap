VERDICT: ACCEPT

# Mathematical review report

I accept the argument for Theorem 1.2 under the finite-level Ramanujan–Arthur decomposition assumption in Theorem 1.1. After reading the complete version and checking the connections between its parts, I found no substantive mathematical error or unclosed proof step requiring rejection.

## Actual review scope

The materials were the complete `paper.tex` (lines 1–5467) and matching `paper.pdf` in this directory. I read all eight sections and references paragraph by paragraph, using the PDF text layer to check theorem numbers and relevant statements. No other versions, previous reviews, experimental records, or network sources were consulted. Within the restricted research input, cited originals were not retrieved; the assessment adopts the explicitly stated external theorems and checks matching conditions and usage. In particular, Theorem 1.1 is an explicit main-theorem assumption.

Focus areas: full tuple invariants versus individual Frobenius conjugacy classes; finite-type global support; the open-orbit criterion; enhanced, trace, duality, and Koszul comparisons in Sections 4–6; parameter dependence and uniform lower bounds in Section 7; tensor vanishing for nonperfect sources in Section 8; and whether vanishing and nonvanishing concern the same vector and map.

## Principal findings

### 1. Main-theorem quantifiers and global parameter identification

Section 2 retains simultaneous-conjugation invariants of every finite tuple. Proposition 2.6 appends the identity to convert these to excursion left-right invariants, then uses the chosen common eigenvector to give scalar identities on the entire cyclic quotient. Commuting coordinate operators extend identities on the generator to the cyclic module.

Finite type is adequately justified: after fixing an auxiliary Hecke point, matrix coefficients of finitely many chosen representations applied to the generator land in finitely many isotypic components with finite-dimensional Hecke eigenspaces. All matrix coefficients varying over Weil elements reduce to finitely many algebra generators, plus finitely many Lie coordinates. The entire representation scheme of an abstract infinitely generated group is not assumed finite type.

Lemma 3.3 uses a finite generic tuple for closed orbits, an affine quotient to separate them, and the noetherian finite-intersection property for conjugacy conditions, giving one conjugator for all Weil elements. Proposition 3.4 preserves full tuple invariants through two Levi projections, then defines \(\tau_\nu\) from the original parameter after lifting through a finite central cover. This gives continuity, a finite coefficient field, and the specialization identity on the whole Weil group simultaneously.

### 2. Open resonance orbits and purity

Lemma 3.1's place conditions are simultaneous: select Frobenius in an identity congruence neighborhood of a finite quotient, including the constant-field condition modulo \(|\Omega|\). Near the identity, torus logarithms identify Weyl stabilizers with root-reflection-generated stabilizers, yielding connected centralizers and local torsor properties of the central cover.

In Lemma 3.2, the absolute-value direction makes \(m\) central in \(H\) and resonance have \(m\)-weight 2. The raising operator surjects from weight 0 to weight 2 in each \(\mathfrak{sl}_2\)-component; taking invariants of the commuting semisimple factor preserves surjectivity. The specified raising orbit is therefore open and uniquely so.

The final purity argument in Proposition 3.4 correctly uses that the constructed triple remains in the specified nilpotent orbit. In a common torus, the residual parameter's absolute-value direction is orthogonal to the triple's diagonal cocharacter; Theorem 1.1's norm identity forces it to vanish. Applying this at every good place and complex embedding gives the required weight zero at all embeddings.

### 3. Enhanced comparison, Frobenius, and central labels

Section 4 does not treat triangulated equivalence directly as enhanced monoidal equivalence. It separately handles completed monodromic categories, derived zero-monodromy reduction, natural Frobenius comparison, monoidal defect, and enhanced lifting on pure generators.

Two distinctions were checked closely. First, derived module maps use full bar total complexes rather than ordinary chain maps between bounded representatives, retaining the infinite positive-degree tail of torus-equivariant cohomology. The one-dimensional torus test gives \(\operatorname{Ext}^\bullet_{\Lambda(\eta)}(k,k)=k[u]\), \(|u|=2\), matching Frobenius scaling. Second, Lemma 4.7's purity formality does not require semisimple Frobenius on pure Weil modules: spectral separation of weights and heredity of \(k[u,u^{-1}]\) eliminate the relevant higher mapping homotopies; equal-weight \(\operatorname{Ext}^1\) occurs outside the needed degrees.

Equivariant localization first makes the monoidal defect a scalar component-group 2-cocycle; \(|\Omega|\mid d\) then kills it, with a clear role for this hypothesis. Mixed central objects are compared separately by weight filtrations, avoiding identification merely from agreement on pure generators.

Proposition 4.10 reduces the Weil factor to a central element and normalizes tensor maps on neutral labels. Section 5 uses only the established central interchange and specified higher spherical maps. The latter use the unit coend label in the trace, without requiring all higher Satake maps to enter an unconstructed enhanced Drinfeld center.

### 4. Local equations, Koszul duality, and the spherical summand

The positive/negative resonance equations in Section 6 have expected codimension: each stabilizer-associated space over one of finitely many \(H\)-orbits has dimension \(\dim H\), yielding a regular sequence in the smooth ambient space and justifying ordinary complete-intersection schemes later.

Proposition 6.3 retains rational weight decompositions in full faithfulness. Localized reconstruction-cone terms off the zero section have no maps to bounded coherent targets because target weights are uniformly bounded below. This is a graded argument; its Ind-extension is explicitly the Ind-completion of the coherent category, with compatible scopes.

The two determinant factors and shifts in Proposition 6.5 are identical and cancel, so the flag transform gives a structure-sheaf direct image without an unhandled line or shift. \(W_B^\perp=E_+\cap\mathfrak n_B\) uses the correct reciprocal-eigenvalue pairing and \(r\ne1\).

Proposition 6.7 reconstructs the internal algebra from representation-coefficient maps, spectator compatibility, and summands of restricted representations, enough to determine the full module action. Complete-intersection self-intersection filtration and positive self-Ext vanishing prove perfectness; local minimal complexes and commutative endomorphism algebras give one rank and degree. Equivariant trivialization and open-orbit preservation at unipotent residual holonomy match the geometry needed in Section 8.

### 5. Simultaneous degeneration and uniform lower bounds

Section 7 first places several degeneration points in one fiber of an auxiliary curve, applying a one-leg nearby-cycle comparison through Weil restriction, then uses ind-smoothness to reach the geometric generic point of independently moving legs. Chosen labels are summands of induced labels, stable under sufficiently divisible Frobenius powers. Characteristic-zero finite-group invariants finally recover the original finite extra level.

The weight bound comes from the constituent arguments of Propositions 7.4–7.5: first impose auxiliary Hecke quotients and away characters, then place remaining finite-dimensional constituents in external tensors of the original parameter representations. Each extends across the selected degeneration points with point-independent pure weight, so generic compactly supported cohomology bounds control Frobenius spectra at degeneration. Nearby cycles are not assumed automatically to preserve the original upper weight bound.

Theorem 7.7's signs check as follows: dual-label \(m_i\)-weights \(w_i\) change original degree \(b\) to \(b+\sum_iw_i\); full Frobenius after central reduction has modulus \(q^{-D_*\sum_iw_i/2}\). Comparing with \(q^{D_*b/2}\) gives \(b+\sum_iw_i\ge0\). \(D_*\) may depend on finite point sets and labels, while zero is independent of both, exactly the needed quantifiers. Nakayama only needs finite generation, without a noetherian assumption on the infinite-tensor central algebra.

Proposition 7.8 limits Ind-coherent/ordinary-quasicoherent comparison to the required thick subcategory. Other regular self-intersection pieces shift to higher degrees; the uniform mapping lower bound permits contradiction at the first nonzero discrepancy. This covers the final \(Q_\Pi\).

### 6. Boundary tests and final contradiction

Proposition 8.1 retains the entire unipotent residual-holonomy fiber. Its local-coordinate conversion matches earlier algebra-isomorphism directions, and the source map to \(H^0(F_n^{\mathrm{qc}})\) need only be a module map. Projecting to regraded degree zero and even parity is \(B\)-linear and preserves \(f\).

Lemma 8.2's bad flag includes \(u\): its Levi and unipotent-radical parts are first handled inside the triple parabolic, then roots are ordered by \((-\delta,m,\epsilon)\). The determinant polynomial's \(\delta\)-weight is \(\operatorname{Tr}((\operatorname{ad}\delta)^2)>0\), while the chosen flag subspace has only nonpositive weights, so the polynomial vanishes there, rigorously excluding the open orbit.

Lemma 8.3 evaluates at a flag point to split the structure-sheaf unit, giving zero for the entire map on derived residue fibers. Lemma 8.4 upgrades fiberwise vanishing to a finite consecutive-product vanishing by noetherian support induction. I checked generic-point finite-length dévissage, derived Hom localization, finite prime avoidance, and support reduction through \(\operatorname{fib}(s:K\to K)\). Sources need only be pseudocoherent and bounded above; perfectness is not used.

Finally, Lemma 8.5 chooses a simple quotient of the finite-dimensional cuspidal Hecke module detecting \(f\). A nonzero bad-flag idempotent would yield a spherical endomorphism through the bad flag by simplicity; spherical endomorphisms depend only on residual-group class coordinates, and the bad flag is empty on the open orbit, forcing zero at the selected central character, a contradiction. In Proposition 8.6's finite total complex, the all-spherical term has degree zero and one-bad-factor terms degree −1, giving exactly the stated zeroth-cohomology quotient. It still detects \(f\), contradicting earlier vanishing of the same \(q_\Pi^*f\).

## Boundary cases and parameter conditions

- For the zero nilpotent orbit, the absolute-value direction and resonance space are zero, and the open orbit is a point; the arguments agree.
- Triple centralizers may be disconnected. Finite-center lifting, residual-parameter definition, and purity use the full centralizer.
- Complex upper bounds, weight lower bounds, finite generation, and compactness are used where individually required; no uniform upper bound on test-place count replaces their infinite supply.
- Arbitrary full finite-level multiplicities are handled by enlarging auxiliary level and taking finite-group invariants; the original divisor need not become reduced.
- \(r=q^d>1\) makes scaling a non-root of unity, supporting nilpotence, removal of nonresonant blocks, and elimination of positive-polynomial-degree Weil defects.

## Substantive errors and typesetting

Substantive errors: none found.

Ordinary typesetting: no issue affecting formulas, numbering, or proofs was found. A notation table for Section 4's derived modules, bar constructions, and two t-structures would help readers; this is a readability suggestion.

## Conclusion

Under the explicit finite-level decomposition assumption, complete excursion data, the open-orbit lifting criterion, uniform lower bounds for simultaneous local tests, and finite tensor vanishing form a closed proof chain. On this review, I accept the current mathematical argument.
