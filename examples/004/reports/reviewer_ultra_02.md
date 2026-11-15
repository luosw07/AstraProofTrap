VERDICT: ACCEPT

# Review conclusion

I accept the mathematical argument in the current *Global Arthur Enhancements of Cuspidal Excursion Parameters*. With Theorem 1.1's finite-level Ramanujan–Arthur decomposition and the explicitly cited external theorems as inputs, the proof of Theorem 1.2 forms a complete logical chain. I found no substantive mathematical error or need for a new hypothesis.

The paper correctly distinguishes pointwise semisimple Frobenius conjugacy classes from a parameter on the whole Weil group. Full excursion-tuple invariants recover the original parameter; local conjugacy classes only determine resonance spaces, nilpotent orbits, and weight directions. The actual proofs implement this distinction.

# Actual review scope

Read lines 1–5467 of the supplied `paper.tex`, including all eight sections, proofs, and references, and rechecked the key steps below. Only this version was reviewed; no historical versions, other reviews, or external literature were accessed. External results were assessed in their explicit formulations and applicability, focusing on new deductions and connections. LaTeX text was the mathematical basis; no page-by-page layout review was performed.

# Key mathematical checks

## 1. Global support and preservation of the original parameter

Section 2, especially Lemmas 2.3–2.5 and Proposition 2.6, retains matrix entries of partial Weil actions, not only traces. Separate legs commute and fusion gives tensor relations, yielding a commutative representation-scheme coordinate-ring action. Degree-two operations scale under their own Frobenius and respect spectator legs, giving

\[
\operatorname{Ad}(\mathbf b(w))\mathbf e=q^{\deg(w)}\mathbf e.
\]

Proposition 2.6 uses a fixed auxiliary Hecke point for finite type, controlling only the finitely many isotypic components reached by matrix entries of generating representations. The submodule killed by a fixed maximal ideal in a finitely generated Hecke module is finite-dimensional, so the whole representation scheme of an infinite group is not mistaken for a finite-type scheme. Appending an identity variable also retains all finite-tuple data when converting conjugation invariants to excursion invariants.

## 2. Global lifting from the open-orbit criterion

Proposition 3.4 is the key return from geometric support to the original parameter. I checked both Levi projections, reductive closure, and finite-center lifting:

- Scaling puts the image in the Jacobson–Morozov parabolic; the first Levi projection gives a residual homomorphism commuting with the triple.
- Complete reducibilization of the product image preserves the triple's orbit and all tuple invariants.
- Lemma 3.3 gives one conjugator for the entire Weil group. After lifting through the finite central cover, the commutator map from connected `SL₂` to the finite center is constant, giving actual commutativity.

Continuity and a finite coefficient field follow after recovering the original parameter from
\(\tau(w)=\sigma(w)\widetilde h(a^{\deg(w)})^{-1}\),
without assuming arbitrary support points represent continuous homomorphisms beforehand.

Purity orthogonality also holds: a residual semisimple element centralizes the triple, so its real absolute-value direction is orthogonal to the neutral element's bracket expression. The orbit norm from Theorem 1.1 forces the residual direction to zero. This allows disconnected triple centralizers and applies at each complex embedding.

## 3. Enhancement, Frobenius, and central objects

I closely read Section 4's unbounded mapping complexes. Full derived-module maps and bar totalization are retained; bounded objects are not assumed to have bounded Ext. The rank-one exterior-algebra calculation at the end of Lemma 4.2 matches the Frobenius convention: scaling the exterior generator induces the corresponding scaling on the degree-two Ext generator.

Lemma 4.7 uses heredity of \(k[u,u^{-1}]\) for purity formality. Hom and Ext between different weights vanish; permitted equal-weight Ext¹ lies outside the positive-homotopy mapping spaces in question. Semisimple Frobenius on pure Weil modules is not silently required.

Lemma 4.6 makes the scalar tensor defect on connected components a finite-group second cohomology class, killed precisely by test-place degrees divisible by \(|\Omega|\). Proposition 4.8 then recovers multimorphisms, composition, tensor products, and units together. Lemma 4.9 separately handles weight filtrations of mixed central objects, filling the step beyond pure-generator comparison.

## 4. Local equations, Koszul transform, and spherical summand

In Sections 5–6, I checked the central correction between holonomy coordinates and duality/regrading between negative and positive resonance.

Lemma 6.2 uses finitely many resonance orbits: each stabilizer-associated solution space has dimension \(\dim H\), giving expected codimension, complete intersection, and the required Koszul vanishing.

The two augmentation differentials in Proposition 6.3 satisfy \(d^2l=d\theta-J_u dp=0\). Changing transformed equations from dual-action \(u^{-1}\) to \(u\) is an invertible change of equation generators. Full faithfulness uses vanishing of positive-weight localization telescopes against bounded coherent targets, without claiming augmentation reconstruction for all unbounded modules.

In Proposition 6.5, zero-section and equation-Koszul self-duality determinant factors and shifts cancel; \(W_B^\perp=E_+\cap\mathfrak n_B\) matches the invariant pairing.

Proposition 6.7 retains representation-valued maps and spectators to reconstruct the internal endomorphism algebra of the spherical summand. Complete-intersection self-intersection filtration and positive self-Ext vanishing give perfectness; minimal local complexes and commutative endomorphisms give rank one. Invariant endomorphisms alone would not suffice to infer a line bundle; the text uses the stronger internal-algebra comparison, handling the distinction.

## 5. Simultaneous multipoint bounds and parameter dependence

Section 7 places selected points in one fiber of a second curve, then uses Weil restriction and one-leg nearby-cycle comparison for simultaneous degeneration. Finite-group invariants recover original level after adding infinity level; characteristic-zero coefficients make this exact, retaining arbitrary original multiplicities.

Proposition 7.4 only needs which irreducible constituents occur; it does not improperly upgrade local Hecke characters to equality of full excursion parameters. A uniform power of the nilradical lifts pointwise constituent results on the finite-type algebra back to modules, explaining why pointwise multiplicity control is unnecessary.

In Theorem 7.7 the dual label's Frobenius modulus is \(q^{-D_*w/2}\) and the regraded degree \(b+w\). Comparison with arithmetic bound \(q^{D_*b/2}\) gives \(b+w\geq0\). Dependence of \(D_*\) on finite test sets and labels does not affect uniformity of the final lower bound zero in place count and representations. Signs agree with later uses.

Proposition 7.8 maps the least nonzero comparison-cone degree to a perfect-source comparison cone using the complete-intersection self-intersection filtration; other pieces strictly raise the lowest degree by positive shifts. This establishes exactly the Ind-coherent/ordinary-quasicoherent mapping comparison required for final finite tests.

## 6. Final vanishing and nonvanishing concern the same class

Proposition 8.1 preserves coordinate-algebra comparison direction and explicitly allows arbitrary unipotent residual holonomy on the support. Projection to degree zero after regrading is \(B\)-linear and preserves \(f\), giving the final map \(R_n\to H^0(F_n^{\mathrm{qc}})\).

Lemma 8.2's bad flag accommodates both the unipotent element and raising operator. The determinant semi-invariant weight
\[
\operatorname{Tr}(\operatorname{ad}m\,\operatorname{ad}\delta)
=\operatorname{Tr}((\operatorname{ad}\delta)^2)>0
\]
conflicts with nonpositive \(\delta\)-weights in the selected flag subspace, correctly detecting the boundary.

Lemma 8.4's successive tensor-vanishing argument works. Bounded-above pseudocoherent sources and bounded coherent targets suffice for Hom localization. Generic-point finite-length devissage gives a finite initial product; the multiplication triangle reduces to strictly smaller closed support. Different places may use different maps, and source perfectness is unnecessary.

Finally, Lemma 8.5 uses semisimplicity of the finite-dimensional cuspidal Hecke module to choose a simple quotient detecting the same \(f\). Bad-flag summands lack support on the open orbit, while spherical-corner endomorphisms depend only on residual-group conjugation invariants, so bad-flag idempotents act by zero on that simple quotient. Proposition 8.6's finite total complex yields \(q_\Pi^*f\ne0\), directly contradicting zero from the same support in the preceding subsection.

# Boundary cases and issue classification

I specifically checked the zero nilpotent orbit, zero resonance space, empty boundary, `D=0`, nonreduced level divisors, finite centers, and disconnected triple centralizers. The proofs match these main-theorem quantifiers. The infinite test-place sequence only supplies a finite initial segment; no Frobenius degree common to all test sets is required.

Substantive mathematical issues: none found.

Ordinary typesetting issues: no separately reportable item was recorded.

The current manuscript gives an effective proof from the stated finite-level decomposition input to global Arthur enhancement. Verdict: ACCEPT.
