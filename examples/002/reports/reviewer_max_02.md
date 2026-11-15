VERDICT: ACCEPT

# Review report

Conclusion: accept the mathematical argument in the current manuscript. Starting from a complete metric with positive holomorphic bisectional curvature, the paper constructs a global flow, establishes joint positivity and completeness, builds contracting coordinates and polynomial models under nonuniform contraction, and finally proves that the coordinate image is all of complex Euclidean space. Full reading and a second focused review found this chain complete, with no substantive mathematical error or key gap requiring additional proof.

## I. Actual review scope

I read all 6,473 lines of `paper.tex`, including the introduction, nine sections, and bibliography, and extracted text from the matching 77-page `paper.pdf` to check section, theorem, and lemma numbers. Review focused on self-contained mathematical steps, hypotheses of standard tools, quantifiers, limit order, parameter dependence, and the final conclusion. As instructed, I used only the paper in this directory and computation drafts created for this review, without external research. References were checked against the standard results invoked in the text, without reading every original source.

Focused checks covered Theorem 3.1, Proposition 3.3, Proposition 4.2, Lemma 5.2, Propositions 5.1 and 6.2, Theorem 6.3, Lemma 7.3, Propositions 7.5 and 7.7, Proposition 8.1, Lemmas 8.3 and 8.4, and convergence and surjectivity in §9.

## II. Main findings

### 1. Initial analytic data and flow construction

Section 2 uses paired real-direction index forms for the Busemann function, with the curvature term controlled exactly by bisectional curvature. A strict lower bound is extracted only on a short initial segment over a specified compact set, consistent with pointwise strict positivity. The three coefficient bundles are \(K^{-1}\), the trivial line bundle, and \(T^{1,0}M\otimes K^{-1}\). Nakano positivity of the last comes from the tensor-determinant construction, rather than identifying Griffiths positivity of the tangent bundle with Nakano positivity. Finite interpolation, the Baire argument, and dimension counts for finite global generators are compatible.

Lemma 2.2 distinguishes zero-boundary heat operators on compact domains from the Hodge semigroup on the complete manifold. Order preservation is first proved on domains; closedness and commutation with \(d\) are handled on the complete semigroup. The complete initial metric, off-diagonal decay, and polynomial volume upper bound justify the cutoff limit without an initial curvature upper bound. Upper Hessian bounds for smoothed distance cutoffs and lower trace bounds from scalar heat flow together yield two-sided complex Hessian control.

The approximating backgrounds in §§3.1–3.3 (TeX 963–1262) are complete Hermitian metrics, with Chern–Ricci flow at that stage. Derivatives of the background conformal factor control non-Kähler errors in the maximum relative-eigenvalue estimate. Only in the limit, where the background equals \(g\) on fixed compact sets, is Kähler–Ricci flow obtained. The differential identity for \(Q\), determinant lower bound, and maximum-eigenvalue upper bound give two-sided metric control for continuation. A canonical-bundle section nonzero at the point under consideration yields local estimates uniform in the exhaustion parameter, sufficient for diagonal extraction over compact sets and time intervals.

### 2. Scalar comparison precedes positive-time completeness

Lemma 3.2 and Proposition 3.3 (TeX 1264–1803) are central to the logical order. The main Hessian term of the correction potential \(H\) is \(g-h_t\), so the negative Hessian term of

\[
\chi=u^{-k}\exp(-AH/u^2)
\]

absorbs cutoff errors measured in the initial metric. The time coefficient \(1+t^{\beta-1}\) is integrable at zero.

I checked the cofactor estimate

\[
|\operatorname{tr}_{h_t}B|\,dV_{h_t}\le C_n|B|_g\,dV_g,
\]

which follows directly from \(0<h_t\le g\), including the empty-product case \(n=1\). Initial volume and the average bound for \(\rho\) then make boundary-shell errors vanish. The nonlinear volume identity

\[
\partial_t[(e^w-1)dV_{h_t}]=(\Delta_{h_t}w)dV_{h_t}
\]

cancels the zeroth-order curvature term, while \((e^w-1)dV_{h_t}\le dV_g\) supplies uniform integrability. Smooth upper envelopes are constructed through compact-domain problems, with boundary-initial compatibility and local limits explained. Thus comparison does not borrow completeness from §7.

### 3. Disc compactness, frames, and deformation estimates

Proposition 4.2 first obtains an anchor in a compact set from energy, then propagates compactness through inverse-Jacobian control for the globally injective immersion. In Lemma 4.3, approximating sections may have different positive integrability exponents; Krull intersection for a finite local module recovers some positive exponent for the original section. Only finite-jet convergence is needed, not a uniform exponent. At a puncture, a finite-length radial path gives an actual limit point, and the compact boundary of a local coordinate neighborhood traps the image, so nonproperness of the global immersion causes no failure.

In Lemmas 4.5–4.6, boundary Gram factorization produces a normalized holomorphic frame. Gauss area bounds its half-order Sobolev norm; holomorphic components and nondegeneracy of the symplectic bivector control the central frame and inverse. These constants depend only on the boundary compact set and central coordinate region.

Lemma 5.2 (TeX 2737–3068) adequately distinguishes two types of constants: the radius and Taylor remainder needed for holomorphic deformation may depend on interior compact sets and fixed energy bounds, whereas the final coefficient of \(\varepsilon(1+\mathcal E+D(l)^2)\) depends only on boundary data. Stokes' formula reduces area variation of the closed form to a boundary pairing; denominator-cleared logarithmic-wall tensors control the remaining half-order Sobolev terms. Auxiliary outer-function losses vanish after the fixed-parameter sequence and radius limits and do not enter the final energy coefficient.

The negative-part test permits frequencies satisfying

\[
B_\varepsilon/P_\varepsilon\to0,
\qquad \varepsilon P_\varepsilon\to0,
\]

because \(\varepsilon B_\varepsilon\to0\) was already established. Spectral tests and backward-time variations respect this limit order. The latter decrease physical time pointwise and retain \(t<T\).

### 4. Symplectic cost and ellipsoid optimization

I checked the matrix algebra of Lemmas 4.1 and 5.3. For

\[
\mathcal H=\begin{pmatrix}A&B\\B^*&D\end{pmatrix}>0,
\qquad S=A-BD^{-1}B^*,
\]

the shear eliminating the cross block produces an extra vertical bivector whose squared norm must remain. The paper retains it:

\[
p(\mathcal H)=\operatorname{tr}(SD^{\mathsf T})+
\left|\sum_{k,i}(D^{-1}B^*)_{ki}f_k\wedge f_i\right|_D^2.
\]

Thus, for the positive vertical block \(C\) of a lower test, \(p(\mathcal H)\ge\operatorname{tr}(SC^{\mathsf T})\). Only a Schur-complement limit is needed for Proposition 5.1; the entire positive-definite matrix need not be bounded.

The common-base-point argument of Proposition 6.2 also works. The rectangular-determinant Levi form of the product support is nonnegative, and a single column's normalized vertical block is \((1-\alpha_i)I\) at contact. Repeated columns give a uniform positive lower bound. Inf-convolution acts on shared base and time variables; the semiconcave contact set has positive measure, permitting simultaneous choice of second-order expansion points for all factors. Translating tests to their individual source points introduces no coefficient error because the symplectic operator has constant coefficients, even with different source base points and times.

Removing small Hessian losses first, then minimizing independently over vertical directions, gives a positive-semidefinite aggregate matrix. Its positivity makes the final comparison valid even for lower tests with indefinite Levi Hessian. Combined with Proposition 3.3, the determinant gap vanishes. Then \(B\le b_t\) and equal determinants imply \(B=b_t\), giving equality of envelope and norm and joint positivity in Theorem 6.3.

### 5. Completeness, static distortion, and simple connectivity

The matrix and scalar Harnack formulas derived from joint positivity in Proposition 7.1 agree with the curvature-block calculation. Integrated Harnack is first derived along paths approximating the distance infimum; initial compact-ball exit lengths and the exponential form then prove positive-time completeness. The dependency order is correct.

Lemma 7.3 (TeX 4235–4435) deserves emphasis. Besides computing a negative trace of the length Hessian at the moving-ball maximum, it eliminates the trace-free part through a remote holomorphic second jet. The full real quadratic form becomes negative definite, preserving the two-parameter distance constraint. The local-extension cutoff source lies in a single lifted sheet near the center, and its inverse-curvature norm and volume are controlled on a fixed target-coordinate annulus. Thus the constant dependence in \(B\le C(1+A)^C\) matches later use.

For the Harnack equality calculation in Proposition 7.5, I expanded

\[
S=R_z+kR,\quad Q=|\partial R|_{A^{-1}}^2,\quad Z=S-Q.
\]

At equality, \(\partial R=0\) and \(\nabla\bar\nabla R=-A^2-kA\). Substitution into \((\partial_z-\Delta)S\) cancels the mixed-Hessian square against its counterpart in \(\Delta Q\), leaving

\[
(\partial_z-\Delta)Z=\sum_{j,l}\lambda_j^{-1}|R_{jl}|^2.
\]

An interior zero of \(Z\ge0\) forces the pure complex Hessian to vanish and makes the real Hessian strictly negative definite. This includes the \(k=0\) limit. Intrinsic third-derivative estimates extend negative definiteness to actual small balls; gradient flow traps and shortens each fixed loop, proving simple connectivity.

### 6. Contracting coordinates and polynomial models for nonuniform contraction

Proposition 7.7 uses simple connectivity and shortening of compact-set paths to build compatible inverse branches. Compactness for \(s^{-1}\log|f_s|\) and the plurisubharmonic Liouville principle give one common exponent for all fixed compact sets, while their starting times may differ. Transition-jet and small-ball estimates remain uniform for all later endpoints \(u\ge s\).

The constant-volume jet correction in §8 has the correct sign. The Jacobian logarithm has no constant term, and transition-jet decay gives convergence and polynomial coefficient bounds for the correction series. Fixed-degree divergence-free homogeneous fields are generated by shears, so bad-step jets admit polynomial automorphisms with uniform degree bounds.

Section 8.2 uses holomorphic covectors on a complex strip to obtain Loewner order for endpoint rates, beyond ordered eigenvalue comparison. This supports linear alignment in Lemma 8.3. Total descent of propagated weights is counted through first visits to ordered indices, giving at most \(n\epsilon_0\theta_j\), independently of the number of regular steps. Forbidden monomials then have a uniform positive rate gap. The backward homological operator contracts, while allowed terms form triangular automorphisms.

Lemma 8.4 treats complete bad components and terminal bad prefixes separately. Growth of \(q\) pays the degree cost of complete components, which reset to new weights; an unfinished prefix incurs one fixed loss. Macro-endpoints selected using \(\liminf q(s)/s\le2\) suffice to give the required \(\deg G_{0,k}=O(s_k)\). No unproved all-time estimate is inferred from the subsequence.

### 7. Final convergence and surjectivity

Section 9 chooses the decay parameter and jet order first, macro-width \(h\) next, then other fixed parameters and a sufficiently late start. The coefficient directly multiplying \(\Delta s_k\) is independent of \(h\); other costs enter \(o(s_k)\), so choices are noncircular.

Lemma 9.1 simultaneously inducts on the error bound and the region where inverse estimates apply. The error sum is controlled by

\[
\sum_{i\ge k}e^{-10s_i+s_{i+1}-s_k}
\]

and stays within the inverse-map tube margin. Proposition 9.2 separately gives quantitative proofs of injectivity, nondegenerate differential, and inverse-small-ball inclusion.

The final step uses only the subsequential degree bound for forward compositions. If the maximal contained centered-ball radius were finite, nearby inner and outer radii and polynomial growth would extend smallness from inside the image to a larger ball. Inverse-small-ball inclusion would force that ball into the image too. This completes the passage from a biholomorphism onto an open subset to one onto all of \(\mathbb C^n\).

## III. Boundary cases and auxiliary calculations

Checked cases include complex dimension one; no global upper bound on initial curvature; the stage before positive-time completeness; disc boundary times approaching zero or \(T\); interior compact sets varying with area penalties; indefinite horizontal test Hessians in ellipsoid optimization; bounded \(q\) and \(q_i\to\infty\) limits; infinite regular strings and arbitrarily long bad prefixes; and the final use of forward-degree control only on an infinite subsequence. The argument handles these consistently.

The local script `reviewer_checks.py` provided further checks:

- 1,000 random positive-definite complex Hermitian matrices checked the symplectic polynomial's block formula, Schur decomposition, and cost lower bound; maximum identity residual was approximately \(1.82\times10^{-12}\).
- 200 coordinatewise monotone ordered-rate sequences checked the accumulated descent bound for propagated weights in §8.3.
- 1,000 positive Ricci-eigenvalue samples checked the mixed-Hessian cancellation at Harnack equality.

The verdict rests on the stepwise mathematical review; these calculations additionally checked signs, transposes, and indices.

## IV. Errors and typesetting

Substantive mathematical errors or gaps: none found in this review, so no repair requirements are listed.

Ordinary typesetting: none found that impairs reading or formula meaning and warrants separate correction.

Overall verdict: **ACCEPT**.
