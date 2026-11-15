VERDICT: REJECT

The manuscript contains an exactly verifiable substantive error: the introductory \(\gamma_d(p)\) disagrees with the energy second-derivative criterion under \(L^2\)-preserving scaling. This affects Section 1.4's explicit instability range, especially \(q=\gamma_d(p)\). Correct the threshold and related corollaries before renewed review.

1. Scope and method

I read all 5560 lines of paper.tex, including abstract, introduction, Sections 2–8, Appendix A, and bibliography, then rechecked fundamental solutions, shooting, zero-frequency limits, cutoff directions, Lyapunov arguments, resolvent limits, and scaling. Locations use TeX lines and labels. Only the current manuscript and independent local calculations were used, without full external papers. Exact rational arithmetic and polynomial expansion independently verified the error, without floating-point reliance.

2. Substantive error: the incorrect \(\gamma_d(p)\) invalidates two scaling equivalences

First location: Section 1.2, lines 364–379, eq:gamma and eq:scaling, gives

\[
\gamma_d(p)=
\frac{30+d^2+15d-p(d^2+7d-2)}
{d^2+7d-2-(d+1)(d-2)p},
\]

then claims

\[
q>\gamma_d(p)
\quad\Longleftrightarrow\quad
\left.\frac{d^2}{d\lambda^2}E(\phi_0^\lambda)\right|_{\lambda=1}<0.
\]

Second location: Section 1.4, lines 681–684 after thm:scale, says “the scaling condition in Theorem ... is equivalent to \(q\ge\gamma_d(p)\)”, then deduces instability for \(\phi_0\in L^2\), \(q\ge\gamma_d(p)\), emphasizing the boundary \(q=\gamma_d(p)\).

The rigorous calculation follows. Write

\[
A=\|\nabla\phi_0\|_2^2,\qquad
B=\|\phi_0\|_{p+1}^{p+1},\qquad
C=\|\phi_0\|_{q+1}^{q+1}.
\]

The stationary equation and Pohozaev identity give

\[
A+B-C=0,\qquad
\frac{d-2}{2}A+\frac{d}{p+1}B-\frac{d}{q+1}C=0.
\]

Hence

\[
\frac BA=
\frac{(p+1)\bigl(d+2-(d-2)q\bigr)}{2d(q-p)},
\qquad C=A+B.
\]

Set \(a=d(p-1)/2\), \(b=d(q-1)/2\). The paper actually uses
\(\phi_0^\lambda(x)=\lambda^{d/2}\phi_0(\lambda x)\), giving

\[
E(\phi_0^\lambda)
=\frac A2\lambda^2+
\frac{B}{p+1}\lambda^a-
\frac{C}{q+1}\lambda^b.
\]

Direct differentiation and substitution yield

\[
\boxed{\;
\left.\frac{d^2}{d\lambda^2}E(\phi_0^\lambda)\right|_{\lambda=1}
=\frac A8
\left[
d^2+6d+16-d(d+2)(p+q)+d(d-2)pq
\right].
\;}
\]

Thus the correct threshold is

\[
\boxed{\;
\widetilde\gamma_d(p)=
\frac{d^2+6d+16-d(d+2)p}
{d(d+2)-d(d-2)p}.
\;}
\]

The denominator is positive in the energy-subcritical range: 8 at \(d=2\), and positive for \(d\ge3\) by \(p<(d+2)/(d-2)\). Strict negativity and nonpositivity respectively correspond exactly to
\(q>\widetilde\gamma_d(p)\), \(q\ge\widetilde\gamma_d(p)\).

A concrete counterexample lies in the emphasized mass-subcritical, weighted-integrable region. Let

\[
d=3,\qquad p=\frac32,\qquad q=\frac{23}{12}.
\]

Then

\[
1<p<q<\frac73,\qquad p< p_{\mathrm w}(3)=\frac95,
\]

so \(\phi_0\in\mathcal F(H^1)\) and all basic assumptions hold. The manuscript's threshold is
\(\gamma_3(3/2)=21/11\), and
\[
\frac{23}{12}>\frac{21}{11}.
\]
Yet exact calculation gives

\[
\frac BA=\frac{37}{12},\qquad
\frac CA=\frac{49}{12},\qquad
\left.\frac{d^2}{d\lambda^2}E(\phi_0^\lambda)\right|_{\lambda=1}
=\frac{3}{64}A>0.
\]

This directly contradicts the strict equivalence at lines 364–379.

The emphasized boundary also fails: retain \(d=3,p=3/2\), taking
\(q=\gamma_3(3/2)=21/11\). Then

\[
\left.\frac{d^2}{d\lambda^2}E(\phi_0^\lambda)\right|_{\lambda=1}
=\frac{5}{88}A>0,
\]

Thus the thm:scale application at lines 681–684 lacks its nonpositive-second-derivative hypothesis at this boundary. The actual threshold is
\(\widetilde\gamma_3(3/2)=41/21\).

This difference covers a parameter region. The threshold difference is

\[
\widetilde\gamma_d(p)-\gamma_d(p)
=
\frac{
4(d-1)(d-2)(p-1)\bigl(4-d(p-1)\bigr)}
{
\bigl[d(d+2)-d(d-2)p\bigr]
\bigl[d^2+7d-2-(d+1)(d-2)p\bigr]
}.
\]

Thus for \(d\ge3,\ 1<p<p_{\mathrm c}(d)\), the manuscript's threshold is strictly below the correct one; at \(d=1,2\), both agree exactly.

Impact: Section 1.2's equivalence is false; Section 1.4's explicit parameter range deduced from thm:scale has a proof gap. The theorem itself assumes a nonpositive scaling second derivative, and its Section 8 proof agrees with this calculation. The failure is converting the hypothesis into the stated \(p,q,d\) condition; the additional lower-threshold region needs a separate proof.

Repair: replace relevant thresholds by \(\widetilde\gamma_d(p)\), checking the introduction, comparisons with previous results, and diagrams together. Section 8 then applies at the correct boundary \(q=\widetilde\gamma_d(p)\). Retaining the lower threshold requires a separate proof and removal of the false equivalence.

3. Actual checks of other core arguments

These checks document coverage of the complete proof chain, beyond introductory formulas.

- Sections 2–3: checked mass and weighted-mass thresholds in three decay cases, \(c_p\), \(\lambda_\pm\), and signs and integrability in four integral equations. The critical \(V_0(r)\) leading term \(r^{-2}(\log r)^{-1}\) matches the fundamental solutions' logarithmic exponents.
- Appendix A: checked continuation from openness of \(\mathcal Y_+\) to one zero of the difference function and then \(v_{y^*}\), both Wronskians, \(I_\lambda\)'s sign, and infinite boundary terms excluding the decaying branch. In particular, for \(p>p^*\), only nonpositive upper limit of \(r^{2d-2}u'v'\) is needed, and lem:right's integral estimate allows positive initial tail derivative.
- Section 4: checked \(W_\omega>0\), variation-of-parameters signs, regularity at zero, and \(\lambda_-<2-\alpha<\lambda_+\). At \((d,p)=(4,2)\), the first integral has negative constant order and the second \(O((\log r)^{-1})\). Origin and infinity controls for local \(C^2\) convergence are integrable; uniform tail negativity before Fatou validates mass-slope divergence.
- Section 5: recomputed mixed and quadratic cutoff orders \(R^{d-2\alpha}\), \(R^{d+2-2\alpha}\); checked logarithmic \(2\alpha=d+2\), \(\beta_R=O(R^{-2}\log R)\) at \((4,2)\), and \(\beta_R=O(R^{-1}(\log R)^3)\) at \(d=5,p=p^*\), sufficient for vanishing corrections.
- Section 6: checked phase correction \(a(\phi_0)=\psi\), flow identity \(\dot A=-\mathcal P\), and the Nehari energy-gap estimate. An orbit staying in the neighborhood is \(H^1\)-bounded and extends globally; a bounded Lyapunov functional then contradicts its fixed-sign nonzero derivative.
- Sections 7–8: checked self-adjointness for compact-operator sandwiching, norm convergence from strong convergence and compactness, and zero-resonance exclusion through the regular radial nondecaying branch. At \(d=6,p=p^*=3/2\), logarithms make critical integrals for \(\phi_0\in L^{3/2}\), \(V_0\in L^3\), and \(\nabla\eta_0\in L^2\) converge. Strict positivity on the negative-eigenfunction orthogonal complement and strict negative pairing from linear independence of \(\eta_0\) and scaling direction match Section 8's conditional theorem.

No other substantive error requiring separate listing was found. Rejection rests on Section 2's exact counterexample and its effect on the explicit instability conclusion.

4. Ordinary typesetting issues

None are listed. The threshold changes the mathematical parameter range and requires substantive correction.
