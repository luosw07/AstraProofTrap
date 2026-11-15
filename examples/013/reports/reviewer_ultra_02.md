ACCEPT

I found no substantive mathematical error in my review of the supplied current paper, “Exact (Non-)Accelerations of Heavy-Ball Discretizations.” This is a review verdict, not a claim of formal verification.

## Scope and method

I read the complete standalone `paper.tex`, lines 1–5295, in bounded, nontruncated chunks, including the theorem statements, surrounding qualifications, bibliography, all appendices, and the final proof. I used no other paper version, external mathematical source, other workspace file, other agent report, or proof assistant. I assessed the TeX directly rather than visually reviewing the rendered PDF.

The review included the flow witnesses, spectral closure, startup from rest, finite-memory ceiling and faithful-discretization theorem, trace identity, two-step asymptotics, wall layer, TMM corner, arbitrary approaches to the optimal corner, robust momentum, and finite-condition-number convergence regions. I also made independent elementary calculations of selected identities. Numerical evaluation of the lag-two square-completion identity gave only floating-point roundoff, and the corner coefficient derivatives agreed with the stated expressions. These calculations were consistency checks, not substitutes for the proof review.

## Principal checks

1. **Heavy-ball flow and smooth witnesses** — Theorem `thm:flow` (lines 546–577), with proofs at lines 2435–2699.

   Differentiating the proposed energy gives the displayed identity: the velocity-gradient terms cancel and the remaining coefficients are ((\theta-2c)\Delta_c), (\theta-c), and (\theta-3c). The positive-definiteness argument has the required condition (\Delta_c>0). The spread-spectrum proof supplies a margin uniform in the lag, rather than merely pointwise feasibility. The conversion of that margin to convex smooth interpolation at lines 2643–2658 correctly controls both the orbit-orbit and orbit-minimizer pairs. The quadratic and spiral witnesses then establish the infimum of the state exponent and the corresponding gap and energy exponents under the stated union over finite smoothness bounds.

2. **Spectral closure and finite support** — Theorem `thm:A` (lines 945–966), proved at lines 2731–3144.

   The wave interpolation slacks, including their signs and the scalar value parameter (C), are consistent with the pairwise interpolation inequalities. The IQC construction cancels the function-value coefficients. The one-exponent proof uses the essential hypothesis (r>r_c) to obtain a stable strictly proper transfer function and then converts a uniform weighted square-summability bound into a strictly smaller exponential rate. The finite-support argument uses (T\ne0) for exponential convergence of the normalized lag kernels and (e^T>\rho_q) to make the limiting certificate strictly negative at the endpoints. The strict-minimizer-slack and atom-count arguments retain those hypotheses. I found no inappropriate extension to the explicitly unresolved case (T=0>\log\rho_q).

3. **Initialization from rest** — Lemma `lem:startup` (lines 3146–3211) and Lemma `lem:restquad` (lines 3213–3245).

   The additional scalar coordinate is not assumed to preserve interpolation automatically: its distinct query values supply positive slack against the changed initial datum. The proof separates the bounded case (t\le0) from (t>0), where strict minimizer slack dominates the growing cross terms. The generating-function argument for quadratic runs correctly excludes cancellation of nonzero characteristic roots. These details support the paper's distinctions between state rates, query rates, and from-rest rates.

4. **Finite-memory ceiling, phase rule, and trace formula** — Theorems `thm:ceiling`, `thm:faithful`, and `thm:trace` (lines 1107–1115, 1238–1259, and 1298–1310), with proofs at lines 3595–3971.

   The slow normal form requires only the stated coefficient continuity. The sampled-flow argument retains uniform margins over all lags after coefficient perturbation. For the upper bound in faithful discretization, the higher regularity assumption is actually used in the joint Taylor expansion: evenness excludes problematic odd-frequency monomials, while the positive cubic slow terms absorb mixed terms of higher degree. The middle-curvature root condition supplies (r_c<1-c\varepsilon). In the trace argument the possible simple root at (-1) is canceled before the Schwarz representation is used. The passage to intermediate curvatures in part (b), after canceling common factors, avoids assuming strict endpoint stability that is not in the theorem.

5. **Two-step rates and the wall layer** — Theorem `thm:B`, Proposition `prop:boundary`, and Theorem `thm:layer` (lines 446–464, 1450–1458, and 1483–1507), with relevant proofs at lines 3982–4723.

   The quadratic stability condition follows from the Schur conditions. The lower witnesses and the lag-one upper bounds match under the stated parameter restrictions. The stability-boundary argument keeps the extra alternating root contribution (c_\pi). In the wall layer, the minimization of the binary quadratic form gives (\Lambda(A)=\theta-yA_+^2/(2-y)). The spread construction controls the infinitely many upper and lower lag constraints, and its hypotheses are checked at the layer scale (\xi\asymp\varepsilon^{1/2}). Thus the proof does not infer feasibility solely from a negative lag-one symbol.

6. **Corner, optimal tunings, and finite-condition-number regions** — Theorems `thm:corner`, `thm:optimal`, `thm:robust`, and `thm:tonguefree` (lines 1786–1806, 1880–1894, 4742–4760, and 1978–1997), with proofs through line 5294.

   The corner bounds preserve the distinction between the continuous minimum (c_{\rm lag}) and the resonant minimum (c_{\rm disc}); the paper does not claim equality throughout the arithmetic gaps. The necessity argument for optimal approaches handles bounded deficits, moderate dips, and deep dips separately, with the required scale estimates before invoking spread witnesses or periodic modes. The robust-momentum factorization and interpolation between the two endpoint symbols give positivity on every circle strictly outside the design radius. The finite-condition-number lag-two multiplier has the stated nonnegative square-completion identity, and the affine interpolation in both curvature and step parameters justifies the claimed convergence region.

## Issues

No substantive error or unjustified inference warranting rejection was found. I also did not identify a harmless typographical error that materially obstructs interpretation of an argument.

## Limitations

This was an independent mathematical reading with selected algebraic checks, not a line-by-line machine verification of every polynomial expansion. I did not inspect the cited papers, the linked formal-verification package, or other versions of the article. In particular, the established interpolation and control-theoretic results invoked in the paper were assessed through their stated formulations and the arguments supplied here, without an external audit of the references. The acceptance verdict is limited to the absence of a substantive mathematical error found in this review.

