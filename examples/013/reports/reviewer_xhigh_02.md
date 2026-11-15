ACCEPT

No substantive mathematical error was found in my independent review of the supplied current paper.

## Scope and method

I read the complete standalone TeX source, lines 1–5295, in consecutive bounded chunks, including the main text, figure and table content, bibliography, and all appendices. My mathematical input was this paper only. I did not consult another version, external sources, other workspace documents, other reviews, or other agents, and I did not use a formal proof assistant.

The review used the TeX source as the authoritative representation; I did not separately inspect the rendered PDF. I checked the mathematical arguments, their hypotheses, their dependencies, and several central algebraic identities. The verdict means that I found no substantive error; it does not assert formal verification or exhaustive independent rederivation of every calculation.

## Findings

I have no substantive issue to report. In particular, I did not find a counterexample to a stated result or an unjustified inference that changes a claimed conclusion. The following describes the actual coverage and the points examined most closely.

### Basic rates, quadratics, and initialization

- Definitions and preliminary claims, lines 340–505 and 2253–2409: I checked the uniform rate convention, finite-horizon compression and smoothing, submultiplicativity, quadratic lower bounds, the Schur stability condition, the price-of-extrapolation argument, and the slow quadratic constant. The distinction between a uniform rate and an individual asymptotic root factor is maintained.
- The from-rest construction in Lemma `lem:startup`, lines 3146–3211, is a substantial part of the lower bounds. Its extra scalar coordinate provides a uniform positive interpolation margin for the modified initial datum. The separate treatment of growing waves correctly uses strict minimizer slack to dominate the cross terms of size exp(kt) by a positive term of size exp(2kt).
- Lemma `lem:restquad`, lines 3213–3245, correctly rules out cancellation of a nonzero quadratic mode in the generating function. The statements using a limsup root factor do not require a scalar oscillatory trajectory to have a positive pointwise lower bound at every horizon. The stronger all-horizon quadratic bound needed in Theorem `thm:B` is instead proved in the real-root regime at lines 4392–4408.

### Heavy-ball flow and sharp witnesses

- Theorem `thm:flow`, lines 546–577, and its proof at lines 2617–2667: the displayed Lyapunov identity follows by direct differentiation. The conditions c ≤ theta/3 and Delta_c > 0 give the required signs and coercivity. The use of exponents strictly below the limiting rate avoids a coercivity assertion at a degenerate endpoint.
- Lemmas `lem:creduce`, `lem:extend`, and `lem:spread`, lines 2459–2615: I checked the forward and reverse convexity residuals, the minimizer condition, and the conversion of a quadratic interpolation margin plus a Lipschitz bound into a finite smoothness bound. The spread-spectrum proof separates short, intermediate, and long lags, choosing the frequency scale before the quadrature size. In particular, it does not infer an all-lag result merely from convergence on a fixed compact time interval.
- The construction provides one finite-dimensional C^{1,1} objective for each prescribed exponent. Its dimension and smoothness bound may depend on that exponent, as the statements allow. The single-spiral obstruction, lines 2679–2718, is consistent with the return-time and minimizer inequalities.

### Spectral closure, certificates, and finite support

- Exact interpolation, lines 2731–2776, correctly retains the scalar function-value parameter C and both minimizer constraints.
- The closure argument, lines 2796–3016, uses compactness/separation for infeasibility, an interpolation-derived IQC, a stable strictly proper feedback system when exp(t) > r_c, and a uniform weighted-square-summability estimate. The restart argument at lines 2977–2987 supplies a strict rate improvement; this is stronger than merely bounding individual trajectories at the tested exponent.
- The finite-support and atom-count arguments, lines 3018–3144, explicitly require T ≠ 0 and T > log(rho_q). The normalized lag functionals have exponential tail control in that regime, which justifies the analytic limiting symbol. Its strict endpoint negativity prevents it from being identically zero. The strict-minimizer-slack argument then excludes infinite active lag tails, and the polynomial zero count gives the stated atom bound. The paper does not claim this argument settles the excluded T = 0 case.
- I checked the lag-one certificate, phase relation, and rational one-atom feasibility calculations at lines 3255–3348. The phase-locking threshold uses the reduced integer period K, with the coprimality hypothesis stated.

### General finite memory and trace identity

- The slow normal form and sampled-flow reduction, lines 3595–3769, use bounded-frequency expansions with a uniform strict margin inherited from the flow. The coefficients multiplying the same nonnegative lag kernels converge uniformly, so the lower witnesses survive all sampled lags simultaneously.
- The faithful-discretization proof, lines 3792–3883, controls both slow and intermediate frequencies using the explicitly required coefficient regularity. The higher-order limiting-symbol term is retained at the half-step boundary.
- The trace argument, lines 3894–3957, handles a possible simple root at -1 by cancellation in Q, uses the paired Schwarz representation, and treats common polynomial factors before applying strict stability at interior curvatures. The nonnegative-symbol hypothesis is retained in the step ceiling and rigidity claims; the paper does not silently extend them to every accelerated method with larger memory.

### Wall layer, corner, and finite condition numbers

- I checked the coefficient expansions and their applications at lines 3978–4451, including the separation of quadratic modes and the sign-alternating endpoint contribution.
- The half-step spread construction, lines 3459–3584 and 4290–4337, controls all upper constraints and all lower constraints of lag at least two before separately verifying lag one. Strict minimizer slack provides a uniform large-lag bound for the finite atomic approximation. This addresses the potential gap between a continuous spectrum and a single finite-dimensional objective.
- The wall-layer proof at lines 4645–4709 checks the spread-construction scale requirements, rather than relying solely on a negative lag-one symbol. It distinguishes an upper certificate bound from the realizable lower bound.
- The corner arguments, lines 4830–5147, preserve the distinction between the continuous minimum and the discrete resonant minimum. The arithmetic gap is disclosed rather than presented as an exact rate. For arbitrary approaches to the corner, the exact identities at lines 4960–4963 explain why the remainder remains uniform even when the rescaled corner parameters are unbounded; the necessity proof separates bounded deficit, moderate dip, and deep dip.
- The robust-momentum factorization and positivity proof, lines 4733–4829, and the lag-two finite-condition-number argument, lines 5154–5231, were checked. The latter uses the explicit nonnegative completed-square identity and affine interpolation in the curvature and step parameters.
- The monotonicity/open-interval conclusion, lines 5270–5294, correctly combines class inclusion with strict-certificate persistence.

## Independent algebra checks

In addition to inspecting the derivations, I directly evaluated the complex expressions and their claimed real-polynomial forms on 50 deterministic parameter samples. I checked:

1. The lag-one cubic in Lemma `lem:cubic`, lines 3982–4008.
2. The mixed symbol and imaginary-part identity in Lemma `lem:mixed`, lines 4009–4045.
3. The completed-square lag-two identity at lines 5210–5214.
4. Both positive-circle endpoint factorizations for robust momentum at lines 4799–4804.

The largest absolute discrepancy was approximately 1.8 × 10^-15 in floating-point arithmetic. These checks corroborate the algebra but are not proofs of the identities.

## Limitations

The review accepts standard background results used explicitly in the paper, including smooth convex interpolation, compact separation, the IQC continuation framework, and the KYP lemma; their original external sources were not independently inspected. I examined the paper's stated hypotheses and its applications of those results. Likewise, bibliographic provenance, claims of formal verification, and exact identifications with algorithms whose original definitions are only cited were not independently authenticated.

No harmless typo or local correction material to the mathematical assessment was identified. The conclusion is limited to this mathematical review of the supplied current text.

