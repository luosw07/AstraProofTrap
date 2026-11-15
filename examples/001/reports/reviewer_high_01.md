VERDICT: ACCEPT

# Mathematical review report

## Conclusion

I accept the mathematical argument in the current manuscript. After reading it in full, I found no substantive calculation error, missing quantifier, circular dependency, or contradictory parameter choice. Its main new mechanisms—scalar comparison before completeness, disc deformation with boundary control, common-base-point treatment of ellipsoid contacts, and forward-degree control under nonuniform contraction—all receive arguments that connect to final surjectivity.

Acceptance concerns the mathematical proof in the current `paper.tex` in the specified directory. The claimed conjecture, author identity, and manuscript length are not grounds for judgment.

## Actual review scope

I read all 6473 lines of `paper.tex`, including the introduction, all proofs, and bibliography, then rechecked the calculations and dependencies below. The complete LaTeX mathematical text was authoritative; I did not visually inspect every PDF page. Under the input restrictions, I did not consult references online or read other versions or reviews. Cited standard theorems were assessed by their stated mathematical content and actual conditions of use. I did not modify the paper.

## Key checks

### 1. Initial analytic data and global flow (Sections 2–3, TeX lines 446–1804)

The initial Busemann function’s strict Levi lower bound comes from a curvature integral near a fixed compact set, not assumed uniform strict positivity throughout the manifold, consistent with the main theorem’s pointwise hypothesis. Finite projective data are constructed by finite-jet interpolation and dimension counting. The result is an injective immersion, which the later disc argument does not mistake for a proper map.

The Hodge heat argument distinguishes the componentwise zero-boundary realization on bounded domains from the self-adjoint realization on the complete manifold. Closedness and the scalar-potential identity are established for the latter by cutoffs, commutation, and off-diagonal decay; the domain Dirichlet heat operator is not incorrectly treated as preserving closed forms.

Flow construction first obtains estimates on complete Hermitian approximations, then takes limits on fixed compact sets. The sources and uses of `h_t≤g`, `P≤0`, and `P_t≤0` are distinguished. Positive-time completeness is not used here.

The key comparison cutoff corrects the logarithmic Hessian with `g-h_t`, rather than directly transferring initial-metric cutoff estimates to the evolving metric. I checked the cofactor estimate: if every eigenvalue of `h_t` relative to `g` is at most one, every coefficient of `tr_h B·dV_h` is a product of the other eigenvalues and is therefore controlled by the initial metric. Combined with the shell integral bound for `ρ`, the error is indeed `O(N^{2n-1-k})`.

For nonlinear comparison, in the identity near TeX line 1620

`∂_t[(e^w-1)dV_h]=(Δ_h w)dV_h`

the curvature terms cancel exactly. Moreover `w≤ρ` gives `(e^w-1)dV_h≤dV_g`, sufficient for the tail and initial limits, followed by Gronwall with an integrable time coefficient. Ellipticity for constructing smooth upper envelopes on bounded domains follows from `0≤w≤ρ+2α`, independently of global completeness.

### 2. Disc compactness, boundary frames, and deformation estimates (Sections 4–5, TeX lines 1805–3404)

Disc compactness uses area to supply compact anchors, local integrability of the inverse Jacobian to propagate control, and the extra-integrability lemma to exclude limit punctures. The closure step uses the Krull intersection theorem for finitely generated local modules, without a common positive exponent for approximating sections. Trapping extended puncture images using local coordinate boundaries and the global injective immersion also uses no properness.

I checked the bounds for `H` and `H^{-1}` and the half-order Sobolev estimate in boundary spectral factorization, and the relationship between Gauss area and frame Dirichlet energy. Control of the central frame inverse uses the nondegenerate canonical symplectic bivector; constants depend on the boundary and central compact sets.

The deformation lemma (`var:deformation-estimate` at TeX line 2757) separates two kinds of constants: its existence radius and Taylor remainder may depend on the interior compact set, whereas the coefficient of `ε(1+E+D(l)^2)` depends only on boundary data. Stokes boundary expressions for closed forms and logarithmic tensors after clearing cutoff denominators establish the latter estimate. This is precisely the uniformity needed to remove the area penalty.

The Fejér test for the negative part uses both `B_ε/P_ε→0` and `εP_ε→0`, ensured by `εB_ε→0`. With `j,δ` fixed, the penalty is removed first, then `δ→0`, and finally `j→∞`. Backward time deformation reduces every boundary time, requiring no uniform gap to the upper time boundary.

The symplectic-cost/Schur-complement algebraic lemma retains the extra vertical bivector term from a nonsymplectic shear. This nonnegative term provides the required Schur-complement compactness without boundedness of the entire positive definite upper-envelope matrix.

### 3. Ellipsoid optimization and joint positivity (Section 6, TeX lines 3405–3927)

Existence and uniqueness of the optimizer and lower semicontinuity of its logarithmic determinant are compatible with the lower-semicontinuous disc envelope. Repetition of contact columns decreases the maximum weight while preserving the decomposition’s total and normalization.

The rectangular-matrix Levi formula contains the projection `I-M* (MM*)^{-1}M`. At normalized contact, each single-column vertical block is `(1-α_i)I`. The Grassmann penalty controls the equality set while preserving a positive vertical Levi lower bound.

Common-base-point inf-convolution does not duplicate and then identify base variables. The aggregate Levi inequality near TeX line 3701 allows separate minimization over each vertical variable, so the sum of Schur complements controls the base Hessian. Although tests transfer to different source-envelope points, the symplectic contraction has constant coefficients in fixed cotangent coordinates; no variable-coefficient error is omitted. The temporary Hessian decrement is removed at each fixed contact before subsequent limits.

The final normalization `B=I≤b_t` gives `e^{-F_0}b_t≤I`. Using the positive aggregate matrix as an intermediate quantity makes the trace comparison valid even for indefinite `dd̄λ`. The scalar inequality falls exactly within Section 3’s comparison principle, giving `F_0=0` and `v=N`.

### 4. Completeness, topology, and a uniform contraction exponent (Section 7, TeX lines 3928–4998)

Integrated Harnack is first integrated along nearly shortest paths, followed by completeness, in the correct logical order. The exit-length estimate’s `t^{-1/2}` coefficient is integrable near zero, sufficient to deduce completeness of each time slice from initial completeness.

The static distortion lemma’s maximum argument on a moving metric ball explicitly treats active boundary constraints. Holomorphic second jets at the endpoints cancel the trace-free part of the two-dimensional length Hessian, rather than declaring every parameter direction feasible merely from a negative trace. The weighted-extension source lies in an initial compact coordinate annulus, and estimate constants exclude the maximum distortion being estimated.

In the simple-connectivity proof, I recalculated `(∂_z-Δ)S` near TeX line 4655. Substituting `dd̄R=-A²-kA` gives `-tr(A(A+kI)²)`, canceled exactly by the mixed-Hessian-square term of `Δ|∂R|²_{A^{-1}}`. At an interior zero of the nonnegative Harnack quantity, the remaining sum of pure-complex-Hessian squares must vanish. Thus the real Hessian is strictly negative definite, sufficient for subsequent contraction of loops by the gradient flow.

The upgrade from local exponents to a common exponent uses the Liouville property for psh functions bounded above and upper-semicontinuity control for a constant `L¹_loc` limit. The exponent becomes uniform while starting times may vary by compact set, consistently with later uses.

### 5. Polynomial models, degree costs, and final surjectivity (Sections 8–9, around TeX lines 4999–6122)

Matrix ordering of endpoint rates comes from norm comparison on a complex strip, without commutation of Ricci matrices at different times. Propagated weights and linear alignment then control both nonlinear monomials and coordinate jumps; positive weights ensure that allowed nonlinear terms form triangular polynomial automorphisms.

Constant-volume jets are realized by finitely many divergence-free shears. Preservation of volume jets by regular-step coordinate corrections follows backward from the full jet identity, rather than being assumed directly from “projection onto forbidden terms.”

Expanded flags for bad macro intervals, resets of complete components, and unfinished-prefix estimates are treated separately. The flag threshold near TeX line 5580 pays the fixed degree multiplier of each bad step. Ultimately only an infinite subsequence with `q(S_j)=O(S_j)` is needed, consistent with the available `liminf q(s)/s≤2`.

Final parameter order is: contraction parameter, jet order, macro width, flag parameter, sufficiently late start. The coefficient used to choose macro width near TeX line 5736 is independent of that width, with other fixed-parameter effects placed in `o(s_k)`, so the choice is not circular.

Backward iteration checks both error bounds and admissible small balls for inverse maps. Global injectivity, differential nondegeneracy, and inverse-ball inclusion each have quantitative proofs. Finally, a subsequence of forward-composition degrees and a polynomial-growth inequality enlarge the central ball in the image. With `γ'<σ/2`, radii can be chosen sufficiently close to prove surjectivity.

## Boundary cases and typography

I checked the relevant degeneracies in complex dimension one: the cofactor estimate remains valid; the space of higher-degree divergence-free homogeneous vector fields is zero, so constant-volume jet realization reduces to the linear case. Squeezing the envelope handles the zero cotangent fiber; the positive vertical blocks required by the symplectic arguments are ensured where invoked.

I found no ordinary typographical issue requiring separate correction. I recommend acceptance of the current mathematical argument.
