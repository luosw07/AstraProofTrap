ACCEPT

Independent mathematical review of “Exact (Non-)Accelerations of Heavy-Ball Discretizations”

Scope and verdict

I read the complete supplied paper.tex, lines 1–5295, in consecutive bounded chunks, including the main text, bibliography, figures expressed in TeX, and all appendix proofs. I found no substantive mathematical error or unjustified inference that warrants rejection. This is a mathematical review, not formal verification.

The sole mathematical input was the supplied current paper. I did not consult other versions, other workspace documents, agent reports, or external references, and did not use a formal proof assistant. I used the complete TeX as the mathematical representation; I did not separately inspect the rendered PDF. The paper’s claim about formal verification played no role in the verdict.

Main arguments examined

1. Rate convention, quadratic bounds, and initialization.

I checked the submultiplicative envelope argument (lines 2293–2311), the Schur/Jury stability calculation (2313–2321), the price-of-extrapolation proof (2337–2349), and the slow-root and endpoint-root analyses (2350–2384, 4236–4288, 4350–4381). The distinctions between uniform rates, individual asymptotic factors, and rates from rest are maintained in the arguments. The from-rest construction (3146–3211) correctly uses an additional decaying coordinate to absorb the finitely bounded deficits introduced by changing the initial gradient. For growing waves, its strict minimizer slack provides the required quadratic domination of cross terms. The generating-function proof that a quadratic’s dominant mode is excited from rest (3213–3245) also handles cancellation explicitly.

2. Heavy-ball flow.

I checked the Lyapunov identity and coercivity calculation in Theorem “Exact decay of the heavy-ball flow” (546–577; proof 2617–2667). The signs and admissible range of c are consistent with the stated exponent. I examined the spiral reduction (2435–2512), smooth extension with a margin (2514–2533), and the three-regime spread-spectrum proof (2535–2615). The construction chooses the frequency scale before the finite quadrature size, and its short-, intermediate-, and long-lag estimates supply a common positive margin. The passage from these margins to a finite-smoothness potential is supported by the stated interpolation condition. The single-spiral obstruction (2679–2699) uses incompatible upper and lower frequency bounds near c = theta/3.

3. Spectral closure and certificates.

I checked the wave interpolation identities (2731–2776), compactness and finite-constraint separation (2796–2822), certificate persistence and the interpolation IQC (2824–2902), and the feedback/continuation argument giving a uniform rate from a certificate (2904–3016). In particular, the requirement r > r_c is used to obtain a stable strictly proper feedback filter, and the subsequent restarted square-summability estimate yields a strict rate below r. The finite-support, strict-minimizer-slack, and atom-count arguments (3018–3144) keep the necessary exclusions T != 0 and T > log rho_q. Their endpoint negativity and analytic zero-set argument support the finite-dimensional boundary conclusion. The phase-locking and Lyapunov-form arguments (3255–3457) were also examined.

4. General finite memory and the trace identity.

I checked the slow normal form and sampled-flow transfer (3595–3777), the low-frequency and two-scale expansions (3779–3824), and the proof of faithful discretization (3826–3889). The Taylor argument uses the stated coefficient regularity to control all intermediate frequency scales; it does not infer uniform positivity solely from a pointwise limit. The trace formula and its equality case (3894–3957) correctly separate the strictly stable case from the closed-disk case, cancel common factors, and use interior curvatures before passing to the limit. I found no defect in the deduction y <= 2 or in the stated rigidity under its nonnegative-symbol hypothesis.

5. Boundary layer, corner, and finite condition numbers.

I checked the half-step spread-spectrum construction (3459–3581), its discrete specialization (4290–4337), the exact-constant proof (4383–4419), and the wall-layer proof (4645–4709). The nonzero value constant, strict minimizer margin, and finite-atom approximation are included where needed. The corner bounds (4830–4928) distinguish the continuous lag-one minimum from the discrete resonant minimum and therefore do not assert equality across the acknowledged arithmetic gap. I also checked the arbitrary-approach optimality classification (4941–5147): bounded deficits, moderate dips, and deep dips are treated separately, and the moderate-dip scale meets the spread-witness hypothesis. Finally, I examined the robust-momentum factorization (4733–4829), the lag-two convergence threshold (5154–5241), and the monotonicity/open-interval argument (5270–5294).

Additional algebra checks

I independently compared the lag-one cubic in Lemma “Lag-one cubic” (3982–4008) with direct complex evaluation at 100 parameter/frequency samples. The largest absolute residual was approximately 8.9e-15. I also checked the completed-square identity for G in the proof of “Tongue-free extrapolations” (5208–5214) at 100 samples; the largest absolute residual was approximately 8.9e-16. These are consistency checks, not substitutes for proofs. The displayed algebra and accompanying derivations were reviewed directly as well.

Issues and limitations

No substantive issue was identified, and I have no correction to propose that changes a claimed conclusion. I did not find a harmless typographical issue worth singling out as a mathematical finding.

The review is limited by the length and technical breadth of the paper. I have not mechanically verified every polynomial coefficient, numerical illustration, or citation. Standard external tools invoked in the proofs—convex C^{1,1} interpolation, finite-dimensional separation, IQC continuation, KYP, and elementary complex-analytic formulas—were assessed as stated and used in this paper; their original sources were not independently audited. Literature priority, bibliographic accuracy, and the advertised formal-proof package were outside this mathematical review. Subject to these limitations, the supplied arguments support the stated conclusions in the cases and under the hypotheses claimed.
