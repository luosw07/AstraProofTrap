VERDICT: ACCEPT

## Conclusion and review scope

I accept the mathematical arguments in the current paper. The resumed review reread the main-text and appendix passages affected by earlier output truncation and checked the dependencies among the main theorems, technical lemmas, basic a priori estimates, preservation of the first two boundary orders, the infinite-Prandtl-number limit, regularization, and compactness. This conclusion replaces the earlier UNCERTAIN verdict that only recorded review progress.

The materials were restricted to paper.tex and paper.pdf in this directory. I checked the PDF page count, contents, and body text, and actually rendered and viewed PDF page 46 to verify that endpoint estimate (5.34) and its preceding closure calculation agree with the source. The mathematical review primarily used the complete TeX; bibliography entries were read, but cited papers were not consulted online. Standard harmonic-analysis, transport, and compactness results cited are used in their usual formulations. The paper was not modified.

## Key checks

1. **Basic good unknown and consistency.** In the equation for Γ=ω−∂₁Λ^{-2α}θ, temperature transport turns the forcing into ε times a commutator. For α=1, p=2, R_{−1}θ₀ is not treated as an L² function: Γ is decomposed and estimated separately in L² and L^q (q>2), avoiding the low-frequency problem caused by nonzero total temperature. Subsequent high-frequency estimates retain ε, allowing absorption of the nonuniform vorticity energy bound. For p>2, the interpolation exponent 2/p<1 permits Young absorption.

2. **Low frequencies of velocity.** The fractional heat-semigroup time integral converges for Q>1/(1−α), matching the main theorem's threshold. When α=1, zero mean gives a heat-kernel difference whose decay r^{-3/2+1/Q} is integrable for Q>2; the first moment is controlled by its initial value and the time integral of the velocity L^Q norm, closing Gronwall. In the nonzero-mean lower-bound proof, R=L(1+Aε)^{r/2} both contains the temperature support and controls the viscous term; the inertial-term exponent r/2+r/(r+2)≤r holds for all r>1 and yields the stated ε^{-1/r} lower bound.

3. **Negative-order commutator.** Kernel degree, integration-by-parts signs, and velocity-difference cancellation agree. Basic integrals require −d<σ<0; the Hölder argument for an ordinary spatial derivative uses σ<−1, with small-ball errors δ^{-σ} and δ^{-1−σ}, respectively, both vanishing in their applicable ranges. The second tangential formula includes differences of ∂Wu and W and the ∂Wθ term, with no highest-order term omitted.

4. **First boundary order and Lipschitz endpoint.** For γ>2α−1, γ−2α∈(−1,0), within the negative-order transport estimate range; p>2/(2α−γ) provides the required strict smoothing margin. When γ=1, μ>2−2α makes the high-frequency series for the temperature contribution converge. The highest unknown ∇W appears only in a linear integral term, closing the uniform Gronwall estimate.

5. **Second-order tangential estimate.** In Lemma lem:pGamma, one may choose 2α−1<γ′<min(1,4α−2−2/q), since 2/q<2α−1; the strict threshold on p ensures the choice of s₀ for F^(2). The endpoint interval 1<γ′<min(2α−2/p,2α−2/q) in Lemma lem:pGamma-high is nonempty. After choosing γ′−1<β<2α−1, the lower boundary-exponent result can first be invoked to control W in B^{γ′}_{∞,1}, followed by the dissipative commutator estimate. This order does not use the highest boundary norm being proved. Finally, the equation for ∂W∇W and ∇(∂WW)=∂W∇W+∇W·∇W close the endpoint as a linear Gronwall problem.

6. **Moving frame and limit.** The translation path defined by mean normalization satisfies the ODE conditions used. The relative support radius closes via the sublinear growth estimate. Temperature converges strongly in local negative Sobolev spaces, and velocity weakly in local W^{1,p}; pairing with Uε·∇ζ in H^{1/2} passes the product to the limit. The inertial term has a factor ε and a uniform local bound, so it vanishes; fractional dissipation uses global L^Q convergence to handle nonlocal tails. The Fourier-support argument and sublinear growth restrict the velocity difference to a spatial constant, which vanishes by the L^Q condition in the original frame or the mean condition in the moving frame.

7. **Limit uniqueness and strong convergence.** The gradient kernel |z|^{2α−3} is locally integrable in two dimensions precisely when α>1/2. The kernel-difference estimate with area-preserving flows bounds the velocity difference by the supremum of the flow difference, yielding uniqueness of the normalized system. Temperature-norm conservation and finite-net approximation of compact time trajectories give uniform-in-time strong L² convergence; general data yield only 1<s<∞, while a common compact support adds s=1, agreeing with the main theorem's patch statement.

8. **Regularization and boundary limit.** Appendix A's second tangential temperature expansion retains the divergence correction in D₃; its boundedness uses div(∂WW)=∂ᵢWʲ∂ⱼWⁱ. After velocity truncation, the far-field error of the Leray projection decays as δ^{m+2/q}. The exponent r=min(p,q) remains strictly greater than 2/(2α−γ). Appendix B and Section 6 obtain time compactness of the tangential field and ∂WW through divergence form, identify distributional derivatives by strong local convergence, and pass the endpoint through weak-star derivative bounds. Nondegenerate tangent vectors and the flow preserve regularity of the boundary parametrization.

## Prose and typesetting corrections

The following should be corrected in the final manuscript and do not affect closure of the main proofs above.

- At TeX line 7837, the norm subscript `_{-L^p)}` should be restored to the corresponding L∞([0,T];L^p) norm.
- At line 7906, “we have” should be moved out of the Morrey inequality's math mode.
- At line 7138, “for every μ∈(2−2α,1)” should read “for the μ selected in the initial-profile assumption.” That μ is already fixed at line 7124, and the proof only requires this exponent; arbitrary higher profile exponents are not assumed.
- A few repeated italic commands, spelling errors, and extra periods may be cleaned up together.

This review found no substantive error or unclosed step requiring rejection of the current main mathematical conclusions.
