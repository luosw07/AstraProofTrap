VERDICT: ACCEPT

# Mathematical review report

## Conclusion

Accept the mathematical argument in the current version. The paper provides a proof chain from local representation-theoretic inputs to an equivalence of full twisted \(D\)-module categories. The passage from finite-stage deformation to infinite colimits, comparison along collision diagonals, and normalization of localization periods each receive supporting arguments. The main theorem's final categorical composition matches the actual conclusions of these inputs.

This review found no substantive mathematical error and left no specific unresolved derivation obstructing this conclusion.

## Actual review scope

Read all 9,170 lines of the current paper.tex, including every proof and the bibliography. Particular attention went to dependencies in Sections 2–13, parameters and quantifiers, unbounded categories, finiteness of geometric operations, duality of the two characters, collisions of marked points, and central data. No paper edits, other versions, historical reviews, experimental records, or external websites were accessed.

The review adopted explicitly stated external theorems as cited inputs, checking the form in which they are used and subsequent deductions. Within the supplied material scope, the cited original papers were not opened separately. Newly supplied internal arguments were the principal focus.

## Key checks

### 1. Level conventions, inertia vanishing, and boundedness

Locations: Section 2, especially foundations:levels, foundations:cutoff at TeX line 390, and the final level conversion in Section 13.

The four-category signs are consistent. With
\[
a=-c,\qquad d=-\frac1{rc},\qquad
s=-\frac{a-h^\vee}{2h^\vee}
 =\frac{c-h^\vee}{2h^\vee}+1
\]
the source needs exactly one tensoring by the actual determinant line; the target exponent already matches the main theorem. This works for the given global form without additional roots of the basic level line.

The inertia-vanishing lemma uses strong Kummer equivariance. Its nonintegral-exponent vanishing calculation remains valid for unbounded complexes because constant-coefficient \(\mathbb G_m\) de Rham cohomology contains the base field as a direct summand. The nonzero integral weights in the HN cutoff multiplied by irrational exponents remain nonintegral. Levi centers, nontorsion-degree components, and external spectators remain included.

The boundary cases \(g(X)=0,1\), with \(b_X=\max(0,2g-2)=0\), were specifically checked: strict inequalities eliminate positively unstable directions, and remaining types still form a finite bounded set.

### 2. Ordinary categorical duality and pseudo-identity

Locations: Section 2, lines 521–726; Section 3, lines 727–1471.

The paper separately constructs ordinary categorical duality using \(\Delta_*\omega_Y\) and pseudo-identity using \(\Delta_!k_Y\), maintaining this distinction in Plancherel and the global construction.

Boundary vanishing in the pseudo-identity proof first descends along unipotent-extension fibers to the Levi Hecke base, then applies central-inertia weights. This places objects in the category required for inertia vanishing. The two parabolic adjunctions, proper-Levi boundary factorization, and simultaneous rank induction for both twisting signs yield the actual continuous-functor identities used later.

The transition from a “natural Hom isomorphism” to the “actual functor-induced Hom map” was also checked: Noetherianity of bounded coherent cohomology makes split-surjective endomorphisms invertible, supplying the needed comparison.

### 3. Whittaker families, duality, and shifts

Locations: Section 4, lines 1472–2180, especially whittaker:strata-properties, whittaker:duality, whittaker:standards.

Finite averaging gives continuous right adjoints, stratum tests, and parameter base change together. Semisimplicity of standard objects is first used pointwise, then transported through local coordinates and coefficient categories to parameter charts of fixed collision type; cross-collision statements are established separately later.

The shifts of standards agree with the pairing:
\[
\dim(q_D)=\delta_N+a_D.
\]
The two \([-a_D]\) shifts cancel \([2(\delta_N+a_D)]\) from integration together with \([-2\delta_N]\) in the pairing. This preserves the transpose relation between closed images and \(!\)-restriction. The limit and colimit presentations of Ran likewise use the corresponding adjoint conversions.

### 4. Finite-rank and logarithmic-colimit tests at nontorsion parameters

Locations: Section 5, deform:rank, and deform:colimit from TeX line 2536.

This is a crucial infinite process. The paper explicitly distinguishes vanishing of a finite complex at \(q=1\) from vanishing of a filtered colimit there, and provides a separate logarithmic-coefficient argument for the latter.

The completed modules
\[
M_i=H^d((K_i)_x\otimes_{A_0}^{L}\mathbb C[[h]])
\]
and their finite-length quotients were rechecked. Finite \(h\)-power torsion in the next degree identifies stable images, providing the required mixed Hodge structures on \(M_i/h^nM_i\); strictness then lifts finitely many homogeneous generators. The uniform upper weight bound promotes vanishing at one finite length to vanishing of that generator at all lengths; finite generation supplies a transition killing all of \(M_i\).

Rank constancy at the generic point and nontorsion parameters finally transfers completed transition vanishing to each non-root-of-unity \(q\). The quantifiers choose a later stage separately for every finite stage and cohomological degree, exactly enough to prove the filtered colimit vanishes.

For nonreal complex levels the required condition still holds:
\[
e^{2\pi i s}\text{ is a root of unity}\quad\Longleftrightarrow\quad s\in\mathbb Q.
\]

### 5. Index dependence in uniform weight estimates

Locations: Section 6, especially lines 3377–3826 and planch:weight-estimate.

Three independent cancellations of dependence were checked:

- The Satake kernels have complex weights \(d_\lambda\) and \(-d_\lambda\), so label changes do not enlarge the total upper weight bound.
- On the spectral side, Hom from a fixed compact object to evaluation representation bundles becomes quasicoherent cohomology on a fixed QCA stack. Tensoring a vector bundle preserves cohomological amplitude, so the upper degree bound is independent of labels and point count.
- The normal link of a configuration stratum has upper degree at most collision codimension \(c'\). Combining duality shifts and integration yields \(E-c'\), then simplicial degree \(l\) gives \(E'-c'-l\).

Thus fixed final degree \(j\) receives only finitely many pairs with \(c'+l\le E'-j\). This is precisely the degreewise uniform upper weight bound required by the logarithmic-colimit lemma. Finite Whittaker tests kill the antitempered part at zero level and are conservative at irrational levels, completing the Plancherel argument.

### 6. Common \(W\)-module target over moving divisors

Locations: Sections 7–8, especially walg:ext and walg:relative-skryabin from line 5099.

The paper distinguishes relative Harish–Chandra compact generators, ordinary bounded models, and renormalized unbounded categories. The PBW presentation of relative depth vacua agrees with depth multiplication at repeated roots. Mapping-complex base change has a separate Ext-continuity argument using relations generated by finitely many depth-difference modes and finite Tor dimension; fiber detection subsequently applies to actual mapping cones.

The common target retains the full regular lattice, BRST vacuum cycles, and transport on formal diagonals. Thus the comparison includes parameters and connections, allowing later local pairings to use the same underlying-complex functor.

### 7. Collision extension uses the necessary low-degree information

Locations: Section 9, local:point-gap; local:one-slot from line 5903; local:two-slot from line 6090.

The additional pointwise self-Ext is \(H^\bullet_{\mathrm{dR}}(G)\). Semisimplicity gives \(H^1(G)=H^2(G)=0\), placing the unit-map cone in degrees starting at three.

Across a smooth collision divisor, \(i^!M\) has amplitude \([0,1]\). The only degree-one obstruction becomes boundary-map surjectivity, identified using comparison on smaller charts and the unit gap already propagated on the larger space. Direct summands of adjoint images and open–closed triangles then yield DG equivalence; the achieved statement matches what the argument needs.

Two-slot comparison further treats uniqueness of extension from the open configuration space and specialization of vacua at neutral-point collisions. The monic-polynomial argument for whole-color translation works for arbitrary heart objects, without global coherence or a uniform torsion exponent. The DVR calculation of vacuum cycles and torsion-freeness determines the actual comparison on the diagonal.

### 8. Localization, periods, and two insertion comparisons

Locations: Sections 10–12, especially loc:kernel, prop:unipotent-period, prop:ran-integrated-period, and eq:ran-reductive-square.

Localization for arbitrary Grassmannian kernels retains the moving-parameter Maurer–Cartan term; parameter transport uses formal substitution groupoids and transfer bimodules. Later period comparison uses this compatibility.

Auxiliary-level determinants and shifts were recalculated:
\[
l^{\mathrm{lv}}=l_N\otimes\det(h^0/h)^{-1},\qquad
\delta=\delta_N+m,\qquad
B^{\mathrm{lv}}=B^0\otimes\det(h^0/h)[m].
\]
Hence
\[
l^{\mathrm{lv}}[\delta]\otimes B^{\mathrm{lv}}[-2\delta]
 =l_N[-\delta_N]\otimes B^0.
\]
which cancels exactly with \(l_N^{-1}[\delta_N]\) in normalized localization.

The Ran principal-parts calculation uses contraction of the associated support space, retaining the actual support-forgetting map. Passing from unipotent to reductive groups, the paper separately proves restriction–localization and two-insertion comparisons and identifies the final \(G\)-period map by a commuting square covering both required operation orders.

### 9. Global functor construction and central data

Locations: Section 13, equivalence:factorization from line 8463, eq:G3, eq:G4, equivalence:sectors, equivalence:central.

The domains, codomains, and duality directions of the final compositions were checked term by term. Full faithfulness of the localization transpose first provides \(f,f'\); the two Plancherel identities then supply left and right inverses, identified with each other through composition to give the stated equivalence.

The actual global form is retained in lattices, components, and finite-center pairings. The component sign from \(T_D=T_0(-D)\) agrees with
\[
(\eta,p)\longmapsto(p,-\eta)
\]
and both central-torsor formulas. The action of central-torsor automorphisms independently checks these signs. Tensor shifts by integral determinant-line powers arise from the adjoint representation and respect these central operations.

## Substantive errors and required repairs

No substantive-error item or mathematical gap requiring repair is proposed. Acceptance concerns the current complete argument, including all components, nonreal irrational levels, and collision parameters.

## Typesetting and presentation

No typesetting error affecting mathematical understanding was recorded. An optional editorial improvement is an early dependency diagram highlighting the four proof chains: Plancherel deformation, the common \(W\)-target, collision extension, and Ran period comparison. This would improve readability.
