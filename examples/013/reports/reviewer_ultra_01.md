ACCEPT

I found no substantive mathematical error in my independent review of the supplied current paper, *Exact (Non-)Accelerations of Heavy-Ball Discretizations*. This verdict means that the review below did not uncover a substantive error; it is not a claim of formal verification.

## Input and coverage

I read the entire supplied `paper.tex`, lines 1–5295, in bounded consecutive chunks, including the bibliography, all theorem statements, all appendices, and the mathematical descriptions in the figures and tables. I used this TeX file as the mathematical input. I did not consult another version, external references, the advertised formal proofs, other workspace material, or another review. I did not use a formal proof assistant. I did not separately inspect the rendered PDF, so this report does not assess rendering or discrepancies between the PDF and TeX.

The review covered the definitions of uniform and from-rest rates; the quadratic calculations; the flow estimates and witnesses; spectral feasibility, duality, and closure; finite-dimensional and from-rest realizations; the general-memory ceiling and trace identity; the half-step wall and boundary layer; the corner classification; and the finite-condition-number convergence region.

## Mathematical assessment

### Rate conventions and quadratic facts

The state-envelope definition and the submultiplicative argument are consistent (Definition `def:rate`, lines 371–383; Lemma `lem:envelope` and its proof, lines 2293–2311). Finite-horizon compression and convolution justify the stated equality of uniform rates with finite-dimensional smooth subclasses (lines 2253–2291); this argument does not improperly identify a uniform rate with the asymptotic rate of each fixed smooth objective.

I checked the Jury inequalities used for stability (lines 2313–2321), the endpoint-product proof of the extrapolation price (lines 2337–2349), and the slow quadratic-root expansion (lines 2350–2384). The strict-stability-boundary qualification is used where needed. The sign-alternating root calculation (Lemma `lem:altmode`, lines 4266–4288) supplies the additional endpoint contribution rather than treating the slow root formula as valid without qualification at the boundary.

The generating-function argument in Lemma `lem:restquad` (lines 3213–3245) correctly prevents cancellation of a nonzero quadratic mode from the rest initialization. Its assertion uses a limsup root factor, so oscillatory zeros of an individual scalar trajectory do not invalidate that claim.

### Heavy-ball flow and spiral witnesses

The Lyapunov identity in Theorem `thm:flow` (equation `eq:identity`, lines 549–559; derivation at lines 2617–2637) has the stated signs and coefficients. In particular, the restriction on the exponent and the positive coefficient of the position term give coercivity in both position and velocity.

The flow interpolation reduction keeps both ordered-pair convexity inequalities and both minimizer comparisons (Lemma `lem:creduce`, lines 2459–2512). Its use of the chain rule fixes the function-value data, and the minimizer inequality yields the stated obstruction at the exponent theta/3. The single-spiral obstruction (lines 2679–2699) combines a frequency lower bound with a first-return upper bound; these are incompatible sufficiently near theta/3.

I checked the logic of all three lag regimes in Lemma `lem:spread` (lines 2535–2615): the frequency scale is chosen before the finite quadrature size, the intermediate interval is compact after that choice, and the long-lag estimate remains uniform beyond the quadrature-controlled interval. The resulting strict margins and bounded linear relation between the prescribed gradients and positions meet the hypotheses of the smooth-extension lemma. This supports the finite-dimensional, finite-smoothness witnesses in Theorem `thm:flow`, without asserting that their smoothness bounds remain bounded as the target exponent approaches theta/3.

### Spectral closure and realizations

The wave calculation (Lemma `lem:waves`, lines 2731–2776) correctly reproduces the two lag slacks and the two minimizer slacks, including the value scalar C. I checked the cancellation condition in the certificate and its conversion to the frequency-domain quadratic form (lines 2848–2902).

The proof of the one-exponent implication (lines 2941–2989) respects the necessary condition that the tested radius exceed the middle-curvature root radius. This puts the linear feedback filter in the stable, strictly proper setting required by the continuation argument. The final step uses a uniform weighted square-summability estimate after restarting, so it establishes a strict uniform rate bound rather than merely square summability of each trajectory. The upper/lower closure argument at lines 3000–3016 then gives the claimed exact rate.

The finite-support proof (lines 3042–3081) uses the nonzero boundary exponent to obtain an analytic limiting certificate, and uses separation from the quadratic radius to make the endpoint values strictly negative. The strict-minimizer-slack argument (lines 3083–3107) uses a finite trigonometric sum with zero Cesaro mean and positive mean square; the contradiction is valid. The atom count (lines 3109–3134) follows from even multiplicities of interior zeros of a nonpositive polynomial. The paper appropriately leaves the zero-exponent boundary case outside that finite-attainment conclusion.

The extra-coordinate construction for starting from rest (lines 3146–3211) handles the altered initial query by a uniform interpolation margin. For growing waves, its use of strict minimizer slack is necessary and is explicitly assumed; for decaying or bounded waves the relevant deficits are uniformly bounded. I found no invalid interchange between a separate function at each horizon and one function valid at all horizons in this construction.

### General finite memory and the trace formula

The slow normal form and sampled-flow argument (lines 3595–3769) preserve the lag kernels exactly and perturb only their coefficients. This makes the existing strict flow margins sufficient for all sampled lags simultaneously. It supports the ceiling with a number of atoms independent of the discretization parameter.

The positivity proof in Theorem `thm:faithful` (lines 3826–3845) uses the stated higher coefficient regularity to control intermediate frequency scales. The positive cubic slow terms and the first nonzero positive even term of the limiting symbol absorb the Taylor remainder. The separate middle-curvature root hypothesis is then used to apply the one-exponent criterion. The below-wall and negative-effective-extrapolation conclusions (lines 3847–3883) follow from the phase test and the local quadratic-root expansion, respectively.

For Theorem `thm:trace`, I checked the exterior rational function, its values at infinity and at one, the sign in its boundary imaginary part, and the paired Schwarz representation (lines 3894–3925). The possible simple root at minus one is canceled before using boundary continuity. In part (b), cancellation of common polynomial factors and the curvature interpolation identity exclude uncanceled unit-circle roots for intermediate curvatures (lines 3927–3956). The limiting equality argument gives the claimed transfer-function identity.

### Wall, boundary layer, corner, and finite condition numbers

The direct cubic estimates beyond the wall and at the stability boundary use the correct endpoint signs (lines 4410–4451). The wall-layer proof (lines 4645–4709) separates the positive-definite quadratic-form upper bound from the lower-bound construction. In the latter, the resonance bands have width sufficient to contain an integer period, and their frequency scale satisfies the hypotheses of the spread-spectrum construction.

I checked the kernel-gap argument, upper- and lower-lag estimates, minimizer slack, and finite quadrature step in Lemma `lem:spreadhalf` (lines 3487–3581). The application in Lemma `lem:spreadwit` (lines 4290–4337) controls the phase defect relative to the available lag margin, not only absolutely. This distinction is important when the frequency band approaches zero, and the stated smallness hypotheses provide it.

At the corner, the paper retains the distinction between the continuous minimum and the integer-resonance minimum (Theorem `thm:corner`, lines 1786–1806 and 4866–4928); it does not claim an exact constant in the stated arithmetic gaps. The optimal-wedge conclusion follows because the relevant resonance points accumulate at zero. The arbitrary-approach classification (lines 4975–5147) also treats unbounded corner coordinates: the identities in Lemma `lem:nearcorner` keep the errors uniform in the physical parameters, and the necessity proof separates bounded deficits, moderate dips, and deep dips.

The robust-momentum factorization and positive-circle argument (lines 4762–4812) support the exact finite-condition-number rate. The finite-condition-number lag-two proof (lines 5175–5231) uses an affine endpoint reduction and a nonnegative completed square. Its strictness in the interior of the quadratic stability range follows from the positive other endpoint, including equality at the extrapolation threshold.

## Calculational checks

In addition to hand inspection of the derivations, I made finite-precision algebra checks directly from the displayed formulas. These included 1000 parameter samples for the unit-circle coefficients in equation `eq:Acoef` and the lag-two completed-square identity at lines 5210–5214. Maximum residuals were approximately 2.9e-14 and 2.7e-15. I also checked the robust-momentum design-circle identity at several condition numbers and angles, with a maximum residual of approximately 1.8e-15, and checked the corner first-order coefficient limits numerically. These checks support the algebra but are not substitutes for the arguments.

## Issues and limitations

No substantive mathematical issue was found, and I found no typographical discrepancy that changes a claimed conclusion.

The proof of Corollary `cor:QHM` (lines 5233–5241) explicitly discusses the nondegenerate case beta != tau/(1+tau), while its statement also permits equality. This is an elementary omitted case, not a false conclusion: with QHM's parameter relation, equality occurs when beta = 0 or the quasi-hyperbolic weight is zero. The usual initialization then gives gradient descent, as also explained at lines 4465–4468. Moreover tau = beta/(1-beta) >= beta >= tau_*(beta) >= tau_3(beta), so the asserted threshold is automatically satisfied. Stable gradient descent converges on the stated class. Thus this omission does not affect the corollary or downstream results.

The principal limitations are that this was a human-style mathematical review of a long paper, not formal verification; numerical checks covered selected identities only; and cited interpolation, IQC/KYP, and oracle-complexity results were not checked against their external sources. I examined how the paper uses those results and did not find a mismatch in the stated hypotheses or conclusions. Literature attribution, bibliographic accuracy, and the advertised formal-verification claim are outside this verdict.
