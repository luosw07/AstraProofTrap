VERDICT: REJECT

# Mathematical review report (originally in Chinese)

## Conclusion

The current version has a clear substantive mathematical error: the explicit threshold \(\gamma_d(p)\) in (1.8) is not equivalent to the \(L^2\)-preserving scaling second-variation criterion claimed in (1.9). This propagates to the instability region \(q\ge\gamma_d(p)\) and boundary deduction after Theorem 1.3. An exact counterexample fully within the assumptions and the correct formula follow; the verdict is REJECT.

I checked individually the principal arguments for the ODE construction of \(\eta_0\), local zero-frequency convergence, truncated negative directions, Nehari/Lyapunov instability, and appendix shooting, finding no other substantive error of the same kind. Rejection concerns the current false parameter criterion and corollaries; repair can focus on the threshold and related statements.

## Actual scope and method

I read the complete `paper.tex`, including Sections 1–8, Appendix A, acknowledgments, and references; the same directory's `paper.pdf` checked theorem and equation numbers, especially the false expressions on pages 5 and 9–10, confirming they are not merely source comments. Only these two files were used, with no other versions, review records, external materials, network, or other agents, and no modification of the paper.

Checks emphasized allowed dimensions and exponents, fundamental solutions at zero and infinity, Wronskian signs, tail-integral convergence, uniform zero-frequency controls, cutoff-error orders relative to normalization, the Lyapunov energy gap, zero-resonance exclusion, and shooting continuation. External papers were not retrieved; cited standard existence, local well-posedness, and elliptic asymptotic results were used as stated and their specific applications checked.

Local Python rational arithmetic checked the second-variation formula and counterexample. The error follows directly from analytic identities; computations only recheck arithmetic.

## Substantive error: false explicit scaling threshold

### 1. Locations and text

- Section 1.2, equation (1.8), PDF page 5; TeX lines 364–370, especially 369:
  \[
  \gamma_d(p)=\frac{30+d^2+15d-p(d^2+7d-2)}{d^2+7d-2-(d+1)(d-2)p}.
  \]
- Same section, (1.9), TeX lines 373–379: “This condition has the following characterization”, followed by
  \[
  q>\gamma_d(p)\iff
  \left.\frac{d^2}{d\lambda^2}E(\phi_0^\lambda)\right|_{\lambda=1}<0,
  \qquad \phi_0^\lambda(x)=\lambda^{d/2}\phi_0(\lambda x).
  \]
- Section 1.4 after Theorem 1.3, PDF pages 9–10; TeX lines 682–684: “the scaling condition in Theorem ... is equivalent to \(q\ge\gamma_d(p)\)”, then instability is claimed for \(q\ge\gamma_d(p)\), including \(q=\gamma_d(p)\).

### 2. Rigorous derivation

Write
\[
 A=\|\nabla\phi_0\|_2^2>0,\qquad
 B=\|\phi_0\|_{p+1}^{p+1},\qquad
 C=\|\phi_0\|_{q+1}^{q+1}.
\]
The zero-frequency elliptic equation and Pohozaev identity give
\[
 A+B=C,
 \qquad
 \frac{d-2}{2}A+\frac d{p+1}B-\frac d{q+1}C=0.
\]
Thus
\[
 \frac BA=\frac{(p+1)[d+2-(d-2)q]}{2d(q-p)},\qquad C=A+B.
\]
Let
\[
 a=\frac{d(p-1)}2,\qquad b=\frac{d(q-1)}2.
\]
The specified energy and scaling give exactly
\[
 E(\phi_0^\lambda)=\frac A2\lambda^2
 +\frac B{p+1}\lambda^a-\frac C{q+1}\lambda^b.
\]
Its first derivative vanishes at \(\lambda=1\). Eliminating \(C\) with that identity gives
\[
 \begin{aligned}
 \left.\frac{d^2}{d\lambda^2}E(\phi_0^\lambda)\right|_{1}
 &=A+\frac{a(a-1)}{p+1}B-\frac{b(b-1)}{q+1}C\\
 &=(2-b)A+\frac{a(a-b)}{p+1}B\\
 &=\frac A8\bigl[16+d^2+6d-d(d+2)(p+q)+d(d-2)pq\bigr].
 \end{aligned}
\]
The correct explicit threshold is therefore
\[
 \boxed{\displaystyle
 \Gamma_d(p)=
 \frac{16+d^2+6d-d(d+2)p}
 {d(d+2)-d(d-2)p}.}
\]
In the energy-subcritical range, \(d[d+2-(d-2)p]\) is strictly positive (8 for \(d=2\)), so the strict and nonstrict conditions are respectively
\[
 E''(1)<0\iff q>\Gamma_d(p),
 \qquad
 E''(1)\le0\iff q\ge\Gamma_d(p).
\]
This generally differs from current (1.8). They happen to agree at \(d=1,2\); low-dimensional checks do not replace higher-dimensional calculation.

### 3. Counterexample to the strict inequality

Take
\[
 d=3,\qquad p=\frac32,\qquad q=\frac{23}{12}.
\]
Then
\[
 1<p<q<\frac73=p_{\mathrm c}(3)<5,
 \qquad p=\frac32<\frac95=p_{\mathrm w}(3).
\]
Thus the example lies in the emphasized mass-subcritical range and has \(\phi_0\in\mathcal F(H^1)\), satisfying Theorem 1.3's weighted assumption too.

The current paper gives
\[
 \gamma_3(3/2)=\frac{21}{11},\qquad
 \frac{23}{12}-\frac{21}{11}=\frac1{132}>0.
\]
The identities instead give
\[
 \frac BA=\frac{37}{12},\qquad \frac CA=\frac{49}{12},
 \qquad
 \left.\frac{d^2}{d\lambda^2}E(\phi_0^\lambda)\right|_{1}
 =\frac{3}{64}A>0.
\]
This directly disproves (1.9): its left side is true and right side false.

### 4. Counterexample to the boundary deduction after Theorem 1.3

Keep \(d=3,p=3/2\), changing to
\[
 q=\gamma_3(3/2)=\frac{21}{11}.
\]
All exponent and weighted assumptions still hold, but
\[
 \left.\frac{d^2}{d\lambda^2}E(\phi_0^\lambda)\right|_{1}
 =\frac5{88}\|\nabla\phi_0\|_2^2>0.
\]
Thus the nonstrict equivalence at TeX line 683 is false too, and this boundary point fails Theorem 1.3's scaling hypothesis. The true scaling zero is
\[
 \Gamma_3(3/2)=\frac{41}{21}>\frac{21}{11}.
\]

### 5. Impact and repair

This changes the actual parameter region. A rigorous counterexample disproves (1.9), and the deduction after Theorem 1.3 for current \(q\ge\gamma_d(p)\) and its boundary loses its required hypothesis. The example establishes failure of the scaling criterion and deduction; actual orbital stability at these parameters requires separate analysis.

Replace (1.8) by \(\Gamma_d(p)\) above and add a short Nehari/Pohozaev elimination calculation; then consistently correct (1.9), the explicit corollary after Theorem 1.3, boundary discussion, diagrams, and restatements of previous literature's conditions. Retaining the lower higher-dimensional threshold requires an independent argument covering the extra region.

Theorem 1.3 itself assumes actual nonpositive second variation; its Section 8 proof does not need the false \(\gamma_d\) formula. With the explicit threshold corrected, it still applies on the correct boundary curve.

## Review record for the remaining key arguments

### Elliptic asymptotics and fundamental solutions: Sections 2–3

I checked decay for \(p<p^*\), \(p=p^*\), \(p>p^*\), and \(L^2\)/weighted \(L^2\) thresholds. Critical radial integrals are respectively
\[
 \int^\infty r^{3-d}(\log r)^{-(d-2)}\,dr,
 \qquad
 \int^\infty r^{5-d}(\log r)^{-(d-2)}\,dr.
\]
These give the stated \(d=4\) mass endpoint and \(d=6\) weighted endpoint.

In Proposition 3.4's four integral fixed-point constructions, directions match equation signs; logarithmic corrections at zero for \(d=2,4\) and at infinity for \(p=p^*\) match the comparison potential. The identity \(\lambda_++\lambda_-=2-d\) and derivative estimates satisfy later needs.

### Construction of \(\eta_0\) and zero-frequency limit: Section 4

I checked Propositions 4.4–4.5's variation-of-parameters representations, \(W_\omega>0\), and removal of singular origin terms. The key noncritical inequality comes from
\[
 P(\alpha-d)=P(2-\alpha)=-2(3\alpha+2-2d)<0,
\]
which holds under \(\alpha>d/2\), \(\alpha\ge d-2\) required by \(\phi_0\in L^2\), giving correct tail convergence and growth for the two integrals.

At \((d,p)=(4,2)\), the first term has nonzero negative constant order, the second \(O((\log r)^{-1})\), agreeing with \(\eta_0\sim-1\); later cutoffs handle this case separately too.

Theorem 4.8 normalizes \(w_\omega^-\) at a fixed radius before proving convergence, avoiding treating frequency-dependent far-field asymptotic constants as uniform. Integrable origin controls and tail control \(C\phi_0^2 r^{d-1}\) connect fully. Theorem 4.10 obtains a common nonpositive tail by the maximum principle before Fatou, fulfilling the sign condition.

### Cutoffs and dynamical instability: Sections 5–6

I checked \(\beta_R\) and both cross terms. When the weighted condition fails, \(\beta_R^2\) suppresses potentially growing cutoff errors, including logarithmic \(2\alpha=d+2\), \((4,2)\), and \(d=5,p=p^*\). When it holds, the mass term's sign in the quadratic limit is as stated:
\[
 \langle L_0\phi_0,\phi_0\rangle+
 \frac{\|\phi_0\|_2^4}{\langle\eta_0,\phi_0\rangle}.
\]

Proposition 6.1 derives transversality from Nehari-tangent nonnegativity, then uses the implicit function theorem for energy comparison. Conserved energy bounds \(|\mathcal P|\) below positively, continuity fixes its sign, and bounded \(A\) gives a contradiction. Throughout the energy-subcritical range, bounded \(H^1\) within the orbit neighborhood and the blowup alternative justify continuation.

### Finite-slope limit and abstract scaling criterion: Sections 7–8

I checked compactness of \(B_0\), operator-norm convergence from strong convergence of \(J_\omega\) with compact operators, and inverse limits after excluding radial zero resonance. At \(d=6,p=p^*\), logarithmic factors ensure \(\phi_0\in L^{3/2}\), \(V_0\in L^3\), giving the needed endpoint integrability.

Lemma 8.1 obtains strict positivity from nonnegativity on the negative-eigenfunction orthogonal complement and exclusion of zero solutions; Theorem 1.3's distinct asymptotic orders for \(\eta_0\) and the scaling derivative ensure a nonzero combination. Thus the discovered threshold error is in the introduction's explicit conversion, not this abstract quadratic-form reasoning.

### Shooting: Appendix A

I checked the single sign change of \(I_\lambda\), the one-zero property at the first transition parameter, and Proposition A.12's negative nondecaying coefficient. For \(\omega=0,p>p^*\), I specifically checked treatment of \(r^{2d-2}u'v'\), which need not vanish: a nonpositive upper limit suffices for contradiction.

Lemma A.15 in this range uses
\[
 v_*(R)+\frac R{d-2}(v_*'(R))_+<0,
\]
instead of an inapplicable requirement of negative derivative; integral comparison prevents a new tail zero. Proposition A.16 closes continuation by contradicting \(R_y'<0\) with \(R_y\to\infty\) at a finite parameter endpoint. The main text's use of the appendix's global sign, while the appendix uses only Sections 2–3's basic asymptotics, creates no circular argument.

## Ordinary typesetting and exposition

Ordinary typesetting issues were not grounds for rejection. Formula (1.8) is substantively wrong and confirmed in the typeset PDF. For readability only, give the exact cited theorem number at Proposition 2.5 and explain after Appendix Lemma A.3 how local-energy monotonicity covers zero frequency, to clarify dependencies.

## Final recommendation

Correct the explicit threshold and all associated corollaries before resubmission. The verifiable counterexample to (1.9) and its direct impact on the claimed higher-dimensional instability region require REJECT for the current version.
