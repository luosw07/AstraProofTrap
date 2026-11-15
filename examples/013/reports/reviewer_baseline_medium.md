ACCEPT

I found no substantive mathematical error in the current paper, *Exact (Non-)Accelerations of Heavy-Ball Discretizations*, in this review. This is a mathematical referee assessment, not a claim of formal verification.

## Materials and coverage

I read the complete supplied standalone TeX file, lines 1–5293, including the abstract, main statements, explanations, figures and tables in source form, bibliography, and all appendices. I used bounded reads and reread the portions affected by output truncation. I also checked the supplied 63-page PDF as the rendered representation: I extracted its opening pages and visually inspected its page 31, containing the spread-spectra argument. My full reading was of the TeX; I did not visually inspect every PDF page. References below use the exact TeX labels and line numbers, so they are independent of potentially confusing rendered cross-reference names.

I did not examine another version, other reports, experiment records, or other agents' work. I did not retrieve external sources or the linked formalization, use a formal proof assistant, or delegate. I treated the formal-verification paragraph as a provenance assertion, not mathematical evidence. Standard interpolation, separation, Fourier, complex-analysis and control-theoretic results invoked in the paper were assessed through their stated uses; their external sources were not independently audited.

## Assessment of the main argument

### Rate conventions and elementary reductions

Definition `def:rate` (lines 371–383) and the envelope proof (2293–2311) consistently place the supremum over objectives before the asymptotic limit. The restart argument establishes submultiplicativity, and the explicit recurrence gives a dimension-independent finite one-step bound. The quadratic waves establish the stated lower bound. The finite-dimensional compression and smoothing argument at 2253–2291 preserves finite-horizon data and the minimizer after recentering; it does not confuse uniform rates with the root rate of a single smooth objective.

The quadratic stability lemma, the extrapolation-price theorem, and the slow quadratic exponent have valid elementary proofs (2313–2384). In particular, the equality case of the extrapolation-price bound forces both endpoint polynomials to have repeated extremal roots, and hence forces tau = 0. The endpoint near minus one is separately accounted for on the limiting stability boundary (4266–4288 and 4348–4379); it is not incorrectly absorbed into the slow exponent.

### Heavy-ball flow and its witnesses

The Lyapunov identity in `thm:flow` (546–577; proof 2617–2667) checks by direct differentiation: the gradient–velocity term cancels and the remaining coefficients are exactly those displayed. Positivity of Delta_c makes the energy coercive in position and velocity. Passing to all c below the limiting constant justifies the exponent assertion, including cases where coercivity at the endpoint itself is unavailable.

The spiral reduction (2435–2512) includes both orientations of each interpolation inequality and both comparisons with the minimizer. The minimizer constraint produces the theta/3 barrier. The spread-spectrum construction (2535–2615) addresses small, intermediate and large lags separately. Its choice of frequency scale before the finite quadrature size is important: the large-lag estimate handles eventual simultaneous returns of a finite spectrum, while the quadrature only needs to control a compact lag interval. I found no missing uniformity in that construction. The smooth-extension lemma converts the positive quadratic margin and the Lipschitz gradient data into the needed C^{1,1} interpolant. The single-spiral obstruction is consistent with the first-return constraint.

### Spectral closure and initialization

The normalization and interpolation conditions (747–780) and the wave-slack calculation (2731–2776) have compatible signs and factors. The value scalar C is retained throughout; discarding it would lose precisely the constraints needed later in the wall layer.

The closure proof combines compactness, finite-constraint separation, and a strict-certificate implication above the middle-curvature radius (2796–3016). The latter uses a stable strictly proper feedback filter, the interpolation IQC for the homotopy, and a weighted square-summability estimate. Restarting that estimate yields a strictly smaller exponential factor, rather than merely an O(r^n) estimate. These steps support the stated one-exponent principle.

The finite-support argument (3018–3144) does not assume finite support at the outset. It obtains an analytic limiting certificate with negative endpoint values, then proves strict minimizer slack and a finite active-lag set. The atom count follows from even multiplicities of interior zeros of a nonpositive polynomial. The exceptions T = 0 and T = log rho_q are explicitly separated.

The startup construction (3146–3211) supplies the otherwise nontrivial passage to rest initialization. The additional quadratic coordinate provides a uniformly positive interpolation reserve against the altered initial datum. For growing waves, strict minimizer slack controls the potentially unbounded cross terms. The scalar quadratic argument (3213–3245) checks that the relevant generating-function poles do not cancel. Thus the from-rest assertions do not rely on an unjustified initialization equivalence.

### General memory, wall layer, and corner

The slow normal form and sampled-flow argument (3595–3769) preserve uniform margins at all sampled lags, rather than relying only on convergence at each fixed lag. The ceiling follows with finite dimension independent of epsilon for any fixed strict target exponent.

In faithful discretization (3792–3883), positivity is justified in both the small-frequency and compact-away-from-zero regions. The Taylor remainder is dominated by the positive cubic slow terms and the first nonzero even limiting term under the stated regularity assumption. The middle-curvature root condition supplies the radius condition needed to invoke the certificate result. The negative-effective-lead argument also correctly produces an unstable quadratic root.

The trace formula (3894–3957) has the correct normalization and uses the removable pole at minus one under the stated root hypothesis. In part (b), common factors are cancelled before excluding unit-circle roots at intermediate curvatures. The positivity argument at those curvatures avoids assuming strict endpoint stability and establishes the equality rigidity by a polynomial identity.

The half-step spread lemma (3487–3581) provides explicit control of all upper constraints and all lower constraints beyond lag one. The smoothing kernel has a nonnegative Fourier transform, and the large-lag estimate offsets the possible dip of the hyperbolic factor. Finite atomic replacement is justified by strict margins for a finite initial set of constraints and a measure-independent tail bound. The applications in the wall layer (4643–4707) meet the scale requirements epsilon = o(xi_max^{3/2}). The limit at the nonaccelerated threshold is handled by arbitrarily small positive witness exponents, not by asserting divergence at the equality threshold.

The corner theorem correctly distinguishes the continuous minimum tested by lag one from the discrete resonant minimum supplied by the lower construction. It does not claim to close its stated arithmetic gap. The optimal wedge follows because a deficit beyond its low-frequency edge is detected at accumulating resonant frequencies. The arbitrary-approach classification (4973–5145) separately treats bounded deficit, moderate dip and deep dip; the moderate-dip scaling supplies the needed uniform witness hypotheses even with unbounded corner coordinates.

### Finite condition numbers

The robust-momentum factorization and positive-circle interpolation (4740–4810) establish the exact rate by taking radii down to the design rate. The tongue-free theorem (5173–5229) uses a nonnegative lag-two weight in the stated interval, and its endpoint interpolation argument gives strict positivity for stable parameters. Its converse chooses parameters inside the stability region with a strict three-cycle inequality. The condition-number monotonicity proof (5268–5292) correctly combines class inclusion with persistence of strict certificates to obtain an open upper interval.

## Additional arithmetic checks

I independently checked the signs in the Lyapunov identity, the wave-slack identities, the phase-to-lag-one relation, and the corner optimality inequalities. I also ran 2,000 numerical substitutions into the lag-one cubic and mixed imaginary-part identities (`lem:cubic`, lines 3982–4008; `lem:mixed`, lines 4009–4045), comparing the displayed polynomial expressions with direct complex multiplication. The largest normalized discrepancy was approximately 1.34e-14, consistent with floating-point rounding. These substitutions are supplementary checks, not proofs.

## Issues and limitations

I have no substantive error or unjustified inference to report, and no correction is required by this review. In particular, I did not identify a defect affecting the exact interior rate, the flow ceiling, the boundary-layer constant, or the optimal-tuning classification.

The manuscript is long and technically dense. My assessment is not an independent formal reconstruction of every estimate, nor an audit of the cited literature or the claimed Lean proofs. Numerical checks cannot establish identities universally. The PDF inspection was selective, and this report makes no comprehensive typography or rendering certification. Subject to these explicit limitations, the arguments I reviewed support the stated mathematical conclusions and retain the exceptions and unresolved cases needed for their validity.
