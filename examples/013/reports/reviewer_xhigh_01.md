ACCEPT

# Independent mathematical review

**Paper:** “Exact (Non-)Accelerations of Heavy-Ball Discretizations”  
**Source reviewed:** `run_20261114/blind/x6p9d4/paper.tex`, all 5,295 lines, including the main text, bibliography, and all appendices.

I found no substantive mathematical error in this review. This verdict means that the arguments I examined did not yield a defensible counterexample or an unjustified inference affecting the stated conclusions; it is not a claim of formal verification.

## Coverage and main checks

I read the entire supplied TeX in consecutive, bounded chunks. I did not inspect another version, other workspace material, another review, or the linked formalization, and did not use a formal proof assistant. The following describes the substantive coverage.

### Rate convention and elementary quadratic analysis

- **Definitions and envelope:** Definition `def:rate` (lines 371–383), Lemma `lem:envelope` (385–392), and its proof (2293–2311). The dimension-independent finite-horizon bound, restart argument, submultiplicativity, and comparison with quadratic modes are consistent. The distinction between a uniform rate and a supremum of individual asymptotic rates is maintained.
- **Smooth approximation:** The finite-dimensional restriction and recentered convolution argument at lines 2253–2290 preserves the finite trajectory and approximates it within the same strong-convexity and smoothness constants. It supports the stated finite-horizon, and therefore uniform-rate, claim.
- **Quadratic stability and extrapolation price:** Lemma `lem:qstab` and Theorem `thm:price`, with proofs at lines 2313–2321 and 2337–2349. The Jury inequalities, endpoint evaluations, and equality conditions in the price bound check out.
- **Slow quadratic roots:** Lemmas `lem:cq`, `lem:normal`, `lem:altmode`, and `lem:quadboundary`. I checked the slow-root scaling and the real root near (-1), including the use of the stability margin and the minimum of the slow and alternating constants.
- **Initialization and query representation:** The two-step dictionary (2386–2409), the startup construction (3146–3211), and the generating-function proof for a quadratic started from rest (3213–3245) are consistent. In particular, the extra coordinate in the startup construction supplies a uniform interpolation margin for the specially prescribed initial query.

### Heavy-ball flow

- **Theorem `thm:flow`:** The Lyapunov identity in equation `eq:identity` (555–557; proof 2617–2637) was checked directly. The coefficients of the convex remainder and its supporting-hyperplane slack are correct. The positivity conditions give the required state estimate.
- **Flow interpolation:** I checked the orbit gradient and value formulas (2435–2455), the pairwise slack calculation in Lemma `lem:creduce` (2459–2512), and the reduction of the minimizer condition to ((3c-\theta)\sum_j\nu_j\gamma_j^2\ge c\Delta_c).
- **Spread-spectrum construction:** Lemma `lem:spread` (2535–2615) treats short, intermediate, and long lags separately. The order of choosing the frequency scale and quadrature size avoids a circular choice of constants; the resulting margins are uniform over all positive lags.
- **Smooth extension and sharpness:** Lemma `lem:extend` supplies the stated finite smoothness bound from the strict convexity slack and Lipschitz gradient data. The application at 2643–2666 yields one finite-dimensional objective realizing the entire spiral, and supports the distance, energy, and gap exponents.
- **Single-spiral obstruction:** The incompatible frequency bounds obtained from the minimizer inequality and first full return (2679–2698) correctly exclude one atom near the limiting exponent.

### Spectral closure and certificates

- **Wave interpolation:** The factors, signs, and value constant in Lemma `lem:waves` (2731–2776) agree with the interpolation inequalities. Both minimizer inequalities are retained.
- **Separation and persistence:** The compactness and finite-moment separation arguments (2796–2846) give finitely supported certificate weights and cancellation of the value constant. The explicit adjustment of the minimizer weights preserves cancellation under perturbation.
- **Certificate-to-rate implication:** I followed the weighted IQC calculation, homotopy argument, and stable-filter representation at 2848–2988. The restriction (e^t>r_c) is used where required. The final conversion from a uniform weighted square-summability bound to a strict exponential factor uses restart and is valid.
- **Boundary attainment:** Lemmas `lem:finite`, `lem:strict`, and `lem:count` (3042–3134) correctly use (T\ne0) and (T>\log\rho_q). The analytic limiting certificate gives finite support; the Cesàro argument gives strict minimizer slack; the polynomial zero count then yields the atom bound. The unresolved case (T=0>\log\rho_q) is expressly excluded from finite-dimensional attainment.
- **Lag-one and periodic witnesses:** The certificate weights in the proof of `prop:lagone` (3255–3283), root separation (3285–3299), and the rational-angle conditions (3301–3348) have compatible signs and yield the claimed strict and non-strict conclusions.
- **Lyapunov form:** I checked the state enlargement, telescoping value terms, and use of the strict frequency inequality in `prop:lyap` (3351–3439). The subsequent argument proving positivity of the resulting storage function uses the already-established strict rate, rather than presupposing that positivity.

### Fixed memory, the wall layer, and the corner

- **Flow ceiling for fixed memory:** The slow normal form, forced value constant, and sampled-flow arguments (3595–3769) preserve a common margin for all sampled lags. They support the claimed fixed-dimensional lower witnesses for each prescribed exponent.
- **Faithful discretization:** The joint expansion in `lem:twoscale` (3792–3824) and the higher-order Taylor estimate in the proof of `thm:faithful` (3826–3883) control intermediate frequency scales as well as slow and fixed frequencies. The root hypothesis is used to control (r_c). The negative-effective-lead argument correctly produces a quadratic root outside the unit circle.
- **Trace formula:** The exterior rational function, Schwarz representation, factor cancellation, and curvature-(\lambda) argument (3894–3957) support the trace identity, (y\le2), and the equality-case transfer function. The possible simple root at (-1) is explicitly canceled.
- **Half-step spread lemma:** I examined `lem:spreadhalf` (3487–3581), including the nonnegative Fourier kernel, the residue-class margin, the separate short- and long-lag bounds, and the finite-atom approximation. The strict minimizer margin controls the infinite lag tail during approximation.
- **Boundary layer:** The symbol expansion, its minimum, the resonant-band selection, and the hypotheses of `lem:spreadwit` are matched in the proof of `thm:layer` (4645–4709). In particular, the frequency scale gives the needed smallness relative to (\xi^{3/2}).
- **TMM and corner classification:** I checked the robust-momentum factorization (4733–4812), corner expansions (4830–4865), the corner upper/lower bounds (4866–4928), and the arbitrary-approach classification (4941–5147). The proof distinguishes the continuous certificate minimum from the discrete resonant minimum and does not claim to close the stated arithmetic gap.
- **Unbounded corner coordinates:** In the necessity proof for `thm:optimal`, the bounded-deficit, moderate-dip, and deep-dip cases cover the failure of the ratio condition. The physical convergence assumptions imply (\varepsilon D_\varepsilon\to0); together with bounded dip depth this supplies the scale separation needed for the spread witness.
- **Finite condition numbers:** The affine dependence of (L_\tau), the lag-two completion of the square, and the construction of the three-cycle region (5154–5231) support the two stated thresholds. The monotonicity and openness argument (5270–5294) uses class inclusion and persistence at the correct points.

## Independent algebra checks

In addition to hand checks of the principal formulas and inequalities, I evaluated three longer identities at 150 deterministic parameter samples using direct complex arithmetic:

1. The lag-one cubic in Lemma `lem:cubic` (3982–4008), compared with the defining complex product.
2. The completion-of-the-square identity for (G(\xi)) in the proof of `thm:tonguefree` (5208–5214).
3. Both endpoint factorizations used to prove strict positivity for robust momentum (4801–4807).

The largest absolute residual in these checks was approximately (3.6\times10^{-15}). These numerical checks are corroborating algebra checks, not substitutes for proofs.

## Issues and limitations

I identified **no substantive issue requiring rejection** and no specific typographical defect that changes a mathematical conclusion.

The report has the following limits:

- I reviewed the complete TeX source; I did not separately inspect the PDF rendering.
- I did not independently re-prove the external Hilbert-space interpolation theorem, the KYP lemma, or the cited oracle-complexity lower bound. I checked their stated uses and the reductions made in this paper.
- Identifications with externally named algorithms and bibliographic claims were reviewed for consistency with the formulas printed here, not checked against the external publications.
- The linked Lean package and the paper’s statements about formal verification were not used as evidence of correctness.
- This was an independent mathematical reading with targeted calculations, not exhaustive symbolic verification of every displayed expansion or a formal verification of the entire manuscript.

Within this coverage, the main conclusions are supported by the supplied arguments.

