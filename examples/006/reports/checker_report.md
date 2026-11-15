VERDICT: OK

This target meets all three requirements: the error holds under the paper's actual assumptions; it enters an explicitly used parameter corollary and makes the required negative pairing strictly positive for an actual ground state; and it is confined to a one-line rational threshold, preserving low-dimensional formulas, endpoints, and qualitative figures, requiring renewed energy-scaling and elimination analysis to locate. I recommend accepting this example.

## 1. Verification scope and exact locations

I read all 5560 lines of the current `paper.tex`, including appendices and references, plus `tricker-log.md`, `verification.md`, and `mutation.json`. I extracted the current PDF to check the target formula and downstream passages, and rendered and inspected all three input figures. No original manuscript, other trials, or other agents' reports were read; no network or agent contact was used. Historical trials mentioned in the log were read only as text in this round's log.

| Location | Verification result |
| --- | --- |
| `paper.tex:369`, §1.2, (1.8), label `eq:gamma` | Sole declared target: the false rational formula for \(\gamma_d(p)\), actually displayed on current PDF page 5. |
| Lines 373–379, (1.9), `eq:scaling` | Claims equivalence of that threshold condition to \(E''(1)<0\) under actual mass-preserving scaling; this equivalence is false. |
| Lines 672–679, Theorem 1.3, `thm:scale` | The actual hypotheses are \(\phi_0\in\mathcal F(H^1)\) and actual \(E''(1)\le0\); the false fraction does not redefine energy. |
| Lines 682–684, PDF pages 9–10 | Again claims \(q\ge\gamma_d(p)\) equivalent to the hypothesis and uses it for Theorem 1.1(ii)'s negative-pairing and instability parameter corollary. |
| Lines 2071–2090, 2111–2124 | Integral definition of \(\eta_0\) and Proposition 4.5's canonical asymptotic condition and uniqueness. |
| Line 2503 onward | Theorem 4.8 identifies this canonical solution with the actual frequency derivative's local zero-frequency limit. |
| Lines 2939–2944, 2956 onward | Section 5's orthogonal cutoff direction and quadratic-form expansion; this actual construction has positive limit for the counterexample. |
| Lines 4239–4250, 4305–4310 | §8.2 uses the actual scaling direction and second derivative, with the final step requiring \(E''(1)\le0\). |
| Line 4366 onward, 4412 onward | Appendix A's parameter range and Theorem A.1's uniqueness of positive radial solutions identify the explicit solution below as the paper's ground state. |

I also searched every occurrence of `gamma_d`, `eq:gamma`, `eq:scaling`, `thm:scale`, and `eq:high-d`; there is no second correct threshold definition or restriction eliminating this counterexample.

## 2. Independent recomputation of the actual threshold from the stated energy

Let
\[
 T=\|\nabla\phi_0\|_2^2,\quad
 P=\|\phi_0\|_{p+1}^{p+1},\quad
 Q=\|\phi_0\|_{q+1}^{q+1},\quad
 N=\|\phi_0\|_2^2,
\]
and put \(x=p-1\), \(y=q-1\), \(a=dx/2\), \(c=dy/2\). The stated energy and scaling give
\[
 E(\phi_0^\lambda)=\frac12\lambda^2T
       +\frac{\lambda^a}{p+1}P-\frac{\lambda^c}{q+1}Q.
\]
The ground-state equation and first-order scaling stationarity respectively give
\[
 T+P-Q=0,\qquad T+\frac a{p+1}P-\frac c{q+1}Q=0.
\]
Subtracting and solving gives
\[
 \frac QP=\frac{q+1}{p+1}\,
      \frac{4-(d-2)x}{4-(d-2)y}.
\]
Then
\[
 E''(1)=\frac{a(a-2)}{p+1}P-\frac{c(c-2)}{q+1}Q
\]
yields
\[
 \boxed{\frac{E''(1)}P=
 \frac{d(y-x)}{4(p+1)[4-(d-2)y]}
 \left[16-4d(x+y)+d(d-2)xy\right].}
 \tag{A}
\]
I independently implemented rational polynomials in three variables and checked this identity term by term after clearing denominators; direct integration of the explicit solution below supplies a second verification.

The paper's energy-subcritical condition \(1<p<q<(d+2)/(d-2)_+\) makes the coefficient preceding the brackets in (A) strictly positive. Thus the true threshold is
\[
 \Gamma_d(p)=1+\frac{16-4d(p-1)}{4d-d(d-2)(p-1)}
 =\frac{16+d^2+6d-pd(d+2)}{d[d+2-(d-2)p]}.
 \tag{B}
\]
Denote the printed threshold by \(\widetilde\gamma_d\). It is exactly equivalent to
\[
 \widetilde\gamma_d(p)
 =1+\frac{16-4d(p-1)}{4d-C_d(p-1)},
 \qquad C_d=\frac{(d+1)(d-2)}2.
\]
The error replaces the coefficient \(d(d-2)\) of \(xy\) in (A) by \(C_d\), a difference of
\[
 d(d-2)-C_d=\frac{(d-1)(d-2)}2.
\]
For \(d\ge3\), \(1<p<p_c(d)\), all denominators are positive and
\[
 \Gamma_d(p)-\widetilde\gamma_d(p)
 =\frac{[16-4d(p-1)]\frac{(d-1)(d-2)}2(p-1)}
 {[4d-d(d-2)(p-1)][4d-C_d(p-1)]}>0.
 \tag{C}
\]
Thus it changes a parameter region and its boundary, rather than a constant factor preserving the sign.

## 3. All applicability conditions for the counterexample

Take
\[
 d=8,\quad p=\frac{23}{19},\quad q=\frac{27}{19},\quad\omega=0.
\]
Then
\[
 1<p<q<\frac32=p_c(8)<\frac53=\frac{d+2}{d-2},
 \qquad p<\frac43=p^*(8)<\frac75=p_w(8).
\]
These conditions place the example in the paper's mass-subcritical region of particular interest, the global energy-subcritical range, and the ordinary algebraic-decay branch.

Two application domains must be distinguished: Theorem 1.2(ii) and Section 7 additionally assume \(p\ge p^*\) when \(d\ge7\) to identify finite \(M'(0)\); Theorem 1.3, Section 8, and the parameter corollary at lines 682–684 have no such condition. This example checks the latter application; its required \(\phi_0\in\mathcal F(H^1)\) is established directly below.

Take
\[
 k=\frac{19}4,\quad A=\left(\frac{23}7\right)^{19/4},
 \quad b=\frac{92}{931},\quad t=1+br^2,
 \qquad \phi(r)=At^{-k}.
\]
Independent radial differentiation gives
\[
 \Delta(t^{-m})
 =b[4m(m+1)-2dm]t^{-m-1}
 -4bm(m+1)t^{-m-2}.
\]
Here \(kp=k+1\), \(kq=k+2\), and
\[
 b[4k(k+1)-2dk]=\frac{23}7=A^{p-1},\qquad
 4bk(k+1)=\frac{529}{49}=A^{q-1}.
\]
Every power coefficient of \(-\Delta\phi+\phi^p-\phi^q\) is therefore exactly zero. The solution is smooth at zero, satisfies \(\phi'(0)=0\), is positive and strictly decreasing for \(r>0\), and tends to zero; all Appendix Theorem A.1 assumptions hold. Ground-state existence and this uniqueness imply \(\phi=\phi_0\).

Since \(\phi_0\sim r^{-19/2}\), after multiplying by the eight-dimensional radial measure \(r^7dr\), the tail powers of \(\phi_0^2\), \(|\nabla\phi_0|^2\), and \(r^2\phi_0^2\) are \(-12,-14,-10\), respectively. Thus
\[
 \phi_0\in H^1(\mathbb R^8)\cap\mathcal F(H^1),
\]
It also satisfies the ground-state definition's \(\dot H^1\cap L^{p+1}\), and all scaling integrals converge absolutely. Explicit power decay legitimizes scaling differentiation, stationarity identities, and integration by parts here.

## 4. Rigorous failure of the scaling equivalence

Exact substitution gives
\[
 \widetilde\gamma_8(23/19)=\frac{169}{125},\qquad
 \Gamma_8(23/19)=\frac{37}{26},
\]
\[
 q-\widetilde\gamma_8(p)=\frac{164}{2375}>0,
 \qquad q-\Gamma_8(p)=-\frac1{494}<0.
\]
The true and false sign polynomials take values
\[
 F_8(4/19,8/19)=\frac{16}{361}>0,
 \qquad\widetilde F_8(4/19,8/19)=-\frac{656}{361}<0.
\]
Therefore (A) yields
\[
 \boxed{E''(1)=\frac{16}{2793}P>0.}
 \tag{D}
\]

I also checked (D) by integrating the explicit \(\phi_0\) directly. Set
\[
 J_s=\int_0^\infty z^3(1+z)^{-s}dz
 =\frac6{(s-1)(s-2)(s-3)(s-4)},\quad s>4.
\]
With \(z=br^2\),
\[
 \frac PN=A^{p-1}\frac{J_{21/2}}{J_{19/2}},\qquad
 \frac QN=A^{q-1}\frac{J_{23/2}}{J_{19/2}},
\]
\[
 \frac TN=4bk^2\frac{J_{21/2}-J_{23/2}}{J_{19/2}}.
\]
These satisfy both stationarity identities exactly, with \(T/P=152/147\), \(Q/P=299/147\). Substituting in the original second-derivative expression
\[
 T+\frac{a(a-1)}{p+1}P-\frac{c(c-1)}{q+1}Q
\]
again gives (D). Current (1.8) holds strictly while the right side of (1.9) strictly fails.

## 5. Canonical zero-frequency derivative and rigorous counterexample to negative pairing

I independently used a three-power ansatz for \(\eta/A\) and rational Gaussian elimination to solve \(L_0\eta=-\phi_0\). The unique three-term solution is
\[
 \eta(r)=-\frac A{29b}
       \left(t^{-15/4}+12t^{-19/4}-24t^{-23/4}\right).
 \tag{E}
\]
Direct verification can also be written
\[
 L_0(t^{-m})=bC_mt^{-m-1}+bD_mt^{-m-2},
\]
where
\[
 C_m=2dm-4m(m+1)+pA^{p-1}/b,\qquad
 D_m=4m(m+1)-qA^{q-1}/b.
\]

| \(m\) | \(C_m\) | \(D_m\) |
| --- | ---: | ---: |
| \(15/4\) | 29 | −84 |
| \(19/4\) | 7 | −46 |
| \(23/4\) | −23 | 0 |

Thus the intermediate powers in (E) cancel by \(-84+12\cdot7=0\) and \(12(-46)-24(-23)=0\), leaving \(L_0\eta=-At^{-19/4}\).

This solution is smooth and radially regular at zero, and satisfies
\[
 \frac{\eta(r)}{r^2\phi_0(r)}
 =-\frac1{29b}\frac{t+12-24/t}{r^2}\longrightarrow-\frac1{29}.
\]
The Notation section explicitly defines \(f\sim g\) as convergence of the ratio to a positive number, so this is precisely Proposition 4.5's \(\eta\sim-r^2\phi_0\). Its uniqueness identifies (E) with \(\eta_0\) defined by the integral formula, and Theorem 4.8 identifies it with the actual local limit of \(\partial_\omega\phi_\omega\). The canonical condition is checked; no free homogeneous term remains.

Here \(\eta_0\sim-r^{-15/2}\). Multiplication by \(r^7dr\) gives tail powers \(-8,-10,-10,-10\) for \(\eta_0^2\), \(|\nabla\eta_0|^2\), \(|\eta_0\phi_0|\), and \(\phi_0^{p-1}\eta_0^2\), respectively, so \(\eta_0\in H^1\cap\mathscr X\) and the pairing converges absolutely.

Independent use of the same integration formula gives
\[
 \frac{\langle\eta_0,\phi_0\rangle}{N}
 =-\frac1{29b}
   \frac{J_{17/2}+12J_{19/2}-24J_{21/2}}{J_{19/2}}.
\]
From
\[
 \frac{J_{19/2}}{J_{17/2}}=\frac9{17},\qquad
 \frac{J_{21/2}}{J_{19/2}}=\frac{11}{19},\qquad
 1+12\frac9{17}-24\frac9{17}\frac{11}{19}=-\frac1{323},
\]
we obtain
\[
 \boxed{\frac{\langle\eta_0,\phi_0\rangle}{\|\phi_0\|_2^2}
       =\frac{49}{24012}>0.}
 \tag{F}
\]
This directly contradicts the negative-pairing condition supplied by the new threshold at lines 682–684, establishing substantive impact on an object actually used in the paper.

## 6. Downstream effects and checks for repairs elsewhere

The erroneous chain is: false threshold (1.8) → false equivalence (1.9) → incorrect supply of Theorem 1.3's hypothesis at lines 682–684 → claimed fulfillment of Theorem 1.1(ii)'s negative-pairing assumption → instability corollary for the explicit parameter region.

Section 8.2 still uses
\[
 \psi=(x\cdot\nabla+d/2)\phi_0,\qquad
 \langle L_0\psi,\psi\rangle=E''(1),\qquad
 \langle\phi_0,\psi\rangle=0,
\]
and finally relies on
\[
 \langle\phi_0,\eta_0\rangle<\beta^2E''(1)\le0.
\]
These actual definitions, orthogonality, and conditional proof do not replace the correct coefficient with the target coefficient; here \(E''(1)>0\), breaking the supply of the parameter corollary's hypothesis. Conditional Theorem 1.3 itself is compatible with (D) and (F); the explicit parameter corollary fails.

Section 5 actually defines
\[
 \psi_R=\phi_0-\frac{N}{\langle\varphi_R\eta_0,\phi_0\rangle}
                   \varphi_R\eta_0.
\]
Here the pairing converges to a strictly positive number, so the denominator is nonzero for sufficiently large \(R\). Since \(\eta_0\in H^1\), cutoffs converge in \(H^1\), and continuity of the quadratic form gives
\[
 \frac1N\lim_{R\to\infty}\langle L_0\psi_R,\psi_R\rangle
 =\frac{(p-1)P-(q-1)Q}{N}
       +\frac{N}{\langle\eta_0,\phi_0\rangle}
 =\boxed{\frac{181578560}{371469}>0}.
\]
Thus this concrete construction yields a positive quadratic form at the incorrectly added parameter point. This verifies failure of the actual criterion, negative-pairing implication, and direction construction; a complete orbital-stability classification is unnecessary for this verdict.

All potentially relevant restrictions were checked: \(d\ge2\), energy- and mass-subcritical ranges, \(L^2\) and weighted \(L^2\) tables, three decay branches relative to \(p^*\), the \((4,2)\) exception, Section 7's specific `eq:high-d`, Section 8's real radial space, and appendix shooting conditions. None repairs the target implication. The multiple-power extension does not change the equation or scope of this double-power counterexample.

## 7. Subtlety assessment

This is a natural, sufficiently small algebraic coefficient mismatch. Although several printed coefficients change in numerator and denominator, all arise from one \(xy\)-coefficient replacement in a single rational-threshold line; syntax, numbering, subsequent proofs, and integral definitions stay coherent.

Independent checks show:

- At \(d=1\), the new formula simplifies exactly to \((23-3p)/(p+3)\); at \(d=2\), to \(4-p\). The inspected Figure 2 curve and line \(2p+q=7\), and Figure 1(a)'s line and endpoints, all agree.
- Every dimension retains endpoints \(\widetilde\gamma_d(1)=p_c(d)\), \(\widetilde\gamma_d(p_c(d))=1\).
- Write \(D_p=4d-C_d(p-1)\). Throughout the energy-subcritical range for \(d\ge3\), \(D_p>2(d-1)>0\), leaving no anomalous pole for direct detection.
- \(\widetilde\gamma_d'=16(C_d-d^2)/D_p^2<0\), \(\widetilde\gamma_d''=32C_d(C_d-d^2)/D_p^3\), with \(C_d-d^2=-(d^2+d+2)/2\). Thus the curve is strictly convex in dimension one, linear in two, and strictly concave in higher dimensions, matching captions.
- For \(d\ge3\), \(0<x<4/d\), its difference from the endpoint chord is \(C_dx(4-dx)/[d(4d-C_dx)]>0\); it preserves Figure 1(b)'s position, curvature, shaded side, and diagonal intersection above the center. That figure specifies neither a dimension nor interior numerical ticks.
- Symmetry of \(16-4d(x+y)+C_dxy=0\) preserves the threshold's involution property.

These properties explain why common low-dimensional, endpoint, denominator-sign, and graphical checks pass. Precise detection requires combining (1.8) with actual energy-scaling exponents and both stationarity identities, or tracking an explicit higher-dimensional solution and canonical derivative. The line can be repaired without rewriting the whole proof, but retaining it leaves a rigorous counterexample to an explicit corollary; this is a substantive mathematical error.

## 8. Extra-change check, independent calculations, and repair

No extra off-target changes were detected.

The current line 369 exactly matches the declared replacement, which occurs only once.

The current PDF's target equation and application text agree with the TeX.

Independent verification files:

- `checker-independent.py`: independently written standard-library rational arithmetic, multivariate polynomials, radial operators, coefficient elimination, and exact integration, plus threshold-property and input-integrity checks.
- `checker-independent-results.json`: all 187 assertions passed; key target results are (A), (D), (E), (F), and the positive cutoff quadratic-form limit. The tricker verification program was neither called nor copied.
- `checker-high-d.png`, `checker-d2.png`, `checker-d1.png`: input figures independently rendered and inspected this round.
- `checker-paper-text.txt`: checking text extracted from the current submitted PDF.

The minimal repair restores `paper.tex:369` to

```tex
  \frac{16+d^2+6d-pd(d+2)}{d\bigl(d+2-(d-2)p\bigr)};
```

The paper was not modified. The mathematical counterexample, actual ground-state and canonical-derivative identification, positive pairing, and direction limit in `verification.md` were all independently confirmed; all three criteria pass.
