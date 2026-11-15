VERDICT: ACCEPT

# Review report

## Conclusion

I accept the current mathematical argument. Reading the complete manuscript revealed no substantive mathematical error or logical gap sufficient to invalidate Theorem 1.1. The main dependency chain closes: initial analytic data and localized flow construction establish scalar comparison before positive-time completeness; disc variation and fiberwise ellipsoid optimization yield joint positivity; Harnack estimates, completeness, simple connectivity, and a uniform contraction exponent follow; forward-degree control of polynomial models and inverse-image ball inclusions finally prove surjectivity.

This conclusion rests on actual review of this version’s text, not on the expected truth of its main theorem.

## Actual review scope

Inputs were `paper.tex` and the corresponding `paper.pdf` in this directory. I read all 6473 TeX lines paragraph by paragraph, including the introduction, every proof, and references. Locations below use theorem numbers, equation labels, and TeX lines. I used no other versions, prior reviews, external experiments, or online materials, and made no changes.

Citation checking covered the mathematical content invoked, its location of use, and required hypotheses; I did not separately retrieve the cited originals. Key calculations and proofs reproduced in the paper were checked directly. Local computation also tested transpose conventions in the symplectic quadratic-form/Schur-complement identity for non-real Hermitian matrices.

## Key checks

### 1. Initial analytic data and flow construction (Sections 2–3)

In Proposition 2.1, the distance second variation sums two real directions, with curvature controlled by bisectional curvature; positive bisectional curvature is not replaced by positive real sectional curvature. The strict lower bound comes from the specified compact set and a short initial segment, with constant dependencies consistent with pointwise positivity. The three interpolation coefficient bundles are the anticanonical bundle, trivial bundle, and tangent bundle tensored with its determinant. The last uses tensor-with-determinant Nakano positivity with matching hypotheses.

Lemma 2.2 distinguishes zero-Dirichlet domain realizations from the Hodge semigroup on the complete manifold. Closedness uses the full semigroup and cutoff errors far from the compact set, avoiding boundary conditions that fail to preserve closedness in the commutation formula. Heat smoothing of distance cutoffs first controls the complex Hessian above, then supplies a lower bound using two-sided scalar trace estimates, sufficient for later cutoffs.

Theorem 3.1 allows approximation-flow constants to depend on the approximating domain. Uniformity on fixed compact sets comes from nonvanishing canonical sections and local potential estimates. I checked the evolution of Q, gradient absorption for the largest eigenvalue, and the role of determinant lower bounds. Positive-time completeness is not used prematurely.

Both mass-integral calculations in Proposition 3.3 hold. In particular, under 0<h≤g, `flow:cofactor` converts inverse-metric coefficients against evolving volume into initial-volume control; the boundary error is O(N^{2n-1-k}). The crucial nonlinear cancellation is

\[
\partial_t[(e^w-1)dV_h]=(\Delta_h w)dV_h.
\]

Together with w≤ρ, e^ρ dV_h=dV_g, and an integrable time coefficient, this gives the tail control needed for the limiting Gronwall argument. Lemma 3.4 extracts smooth upper envelopes on large domains using local uniform parabolicity; distant boundary estimates need not be uniform in the domain.

### 2. Disc compactness, frames, and variation (Sections 4–5)

Proposition 4.2 does not treat the global injective immersion as proper. Area first supplies anchors in a compact set; local L^{3/2} control of the inverse Jacobian gives W^{1,3}-type distance estimates; Lemma 4.3’s extra integrability handles isolated limit punctures. Final trapping at punctures uses compactness of local coordinate boundaries and global injectivity, consistently with the available hypotheses.

The module-theoretic conclusion of Lemma 4.3 is valid: image germs with some positive extra exponent form a submodule of a finite free module. Closedness of every finite-order jet space and the Krull intersection theorem give an extra exponent for the original section, without uniform exponents for approximations.

In Lemmas 4.5–4.6, the half-Sobolev estimate for boundary spectral factorization depends only on spectral upper and lower bounds; central frame-inverse control uses the nondegenerate symplectic bivector. Constants are thereby separated from interior disc-area bounds, as Section 5 needs.

I especially checked constant dependence and limit order in Lemma 5.2 (from TeX line 2737). The deformation radius and Taylor remainder may depend on the interior compact set for fixed ε. The mixed derivative estimate multiplying ε times energy comes from a Stokes boundary formula for a closed form and depends only on boundary data. Testing the infimum first takes the minimizing-sequence limit, then shrinks the deformation radius, and finally removes the auxiliary outer-function loss, in appropriate order.

Frequency selection for removing the negative part satisfies both B_ε/P_ε→0 and εP_ε→0, using εB_ε→0, not merely boundedness. Backward time variation keeps all times below a fixed upper bound, and the negative difference quotient gives the direction required by `var:backward-test`.

Lemma 5.3 retains the extra vertical bivector term from a nonsymplectic shear. Thus

\[
p(\mathcal H)=\operatorname{tr}(S D^{\mathsf T})+\text{nonnegative term}
\]

and the subsequent Schur-complement estimate have the correct sign. Additional checks on 400 random positive definite Hermitian block matrices in complex dimensions 1, 2, 3, and 4 gave a maximum identity residual of about 6.9×10^{-13}; the minimum nonnegative remainder was at rounding scale. The final limit needs only a bounded trace of the positive Schur complement, not compactness of the entire positive definite principal matrix.

### 3. Ellipsoid optimization and joint positivity (Section 6)

Lemma 6.1’s determinant maximizer exists uniquely. Slightly shrinking a feasible matrix and using compactness of the fiber sphere gives lower semicontinuity of the optimal logarithmic determinant. Contact decomposition and weight replication preserve the matrix decomposition and total weight.

Proposition 6.2 retains one common base point and time while varying fiber columns independently. The rectangular-matrix Levi formula includes an orthogonal projection and has correct nonnegativity; each column’s Levi block divided by its contact weight approaches the identity. Translated test functions handle distinct source points of inf-convolution; symplectic contraction has constant coefficients in the chosen coordinates, with no uncontrolled variable-coefficient error.

I checked three particularly sensitive orders: first remove the small test-Hessian decrement at each fixed contact; then take the regularization limit; finally send the Grassmann penalty and maximum contact weight to zero. Aggregation retains a nonnegative principal matrix before comparing with e^{-F_0}b_t, allowing an indefinite horizontal test Levi block. The resulting scalar inequality matches Proposition 3.3, giving Theorem 6.3’s v=N and joint positivity.

### 4. Harnack, topology, and uniform contraction (Section 7)

In Proposition 7.1, tracing the joint curvature block yields scalar Harnack because the Ricci-square term cancels the time derivative of the trace. Integrated Harnack uses nearly minimizing paths, valid before completeness of the slices is known. The subsequent exit-distance differential inequality has coefficient t^{-1/2}, integrable at zero; initial exit lengths transfer to positive time, giving completeness.

Lemma 7.3’s moving-metric-ball maximum proof explicitly treats the two-parameter constraint. Holomorphic second jets at the distant endpoint remove the trace-free length Hessian; the remaining strictly negative trace keeps test endpoints feasible. The weighted-extension source lies in one lift of a fixed initial chart; its integral constants are separated from maximal singular length, exactly the uniformity required for static distortion.

Proposition 7.4 uses only bounded liminf q(s)/s to choose good windows. The rescaled identity turns (log q)'(s_i) into the central Harnack defect with consistent normalization.

I checked the equality calculation in Proposition 7.5 term by term: at S=0, ∂R=0 and the mixed Hessian is H=-A²-kA. Evolution of Z=S-|∂R|²_{A^{-1}} leaves a sum of pure-complex-Hessian squares. An interior zero of Z makes that sum vanish, yielding strict negative definiteness of the real Hessian. Third-derivative estimates extend this to an actual intrinsic small ball; a given loop is then contracted in one fixed rescaled metric. No uniform injectivity radius is needed.

Proposition 7.7 first uses simple connectivity to remove inverse-chart monodromy, then the Liouville property for psh functions bounded above to turn compact-set-dependent exponents into a common exponent. Arbitrary violating sequences and psh compactness prove the all-clock assertion with correct quantifiers.

### 5. Polynomial models, degrees, and surjectivity (Sections 8–9)

Section 8’s volume-jet series obtains an exponential tail from P_l having zero constant term. Jacobian-correction signs agree with the cocycle. Fixed-degree divergence-free shears realize constant-volume jets; restoring the linear part preserves its original constant determinant.

Loewner ordering of endpoint rates follows from comparison of holomorphic covectors on a strip, without commutation of Ricci matrices at different times. Decreasing records of propagated weights visit at most n new ordered indices. Graph extension for linear alignment and positive rate gaps for forbidden monomials together make the backward homological equation contractive.

Lemma 8.4 treats complete bad components and bad prefixes separately. Degree losses of complete components can reset to the next weights; prefixes leave only a fixed factor. Forward degree O(S_j) is ultimately proved only on an unbounded subsequence with q(S_j)=O(S_j), and only that subsequence is used later.

Section 9 chooses decay parameters and jet order before a sufficiently small macro width h. The coefficient of Δs_k depends only on fixed order and dimension; all other parameter dependence remains in o(s_k) after parameters are fixed, avoiding circularity. Inverse Lipschitz estimates are always used inside specified small balls, with simultaneous backward-error induction maintaining these domains.

Global injectivity and differential nondegeneracy follow separately from separation in original coordinates and Cauchy derivative estimates. Final surjectivity uses forward smallness, forward degree O(s_k), and inverse-image ball inclusion on the same subsequence. Choosing R_1<R_*<R_2 leaves positive margin σ/2-γ'. Polynomial growth on balls then sends B(R_2) into a ball known to admit pullback, producing the contradiction.

## Boundary cases and presentation

For n=1, I checked that the empty cofactor product is 1, higher-degree divergence-free homogeneous fields form the zero space, and the symplectic bivector and ellipsoid steps remain applicable. Zero fibers, initial time, nonuniform curvature, potentially multilayer immersion coordinates, and subsequence-only degree estimates are handled in their respective proofs.

There are no substantive errors to list, and I found no typographical issue changing the mathematics. I recommend retaining the current explanations of constant dependencies, parameter order, and local versus global realizations in publication; they are important to making the proof checkable.
