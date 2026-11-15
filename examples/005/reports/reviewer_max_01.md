VERDICT: REJECT

The current version contains a main-theorem assertion rigorously disproved by an exact solution: for \(p=2\), \(\tfrac12<\alpha<1\), \(u_0\in H^1(\mathbb R^2)\) does not imply \(\nabla u\in L^1(0,T;B^{2\alpha-1}_{\infty,\infty})\). The paper strengthens the critical Chemin–Lerner time norm to an ordinary Bochner \(L^1\) time norm. The counterexample below takes \(\theta_0=0\) and makes the velocity equation's nonlinear term a pure gradient, so it applies directly to the full equation. This issue determines the verdict.

**Actual review scope.** I read all 10821 lines of this directory's `paper.tex`, including the main theorems, technical lemmas, all proofs, both appendices, and references; locations use this TeX's lines and labels. I then rechecked the good-unknown equation, main commutator estimates, exponent conditions in each tangential-regularity branch, low-frequency velocity estimates, moving-frame normalization, limit-equation identification, strong temperature convergence, and closure of smooth approximation. Verification used analytic derivations, without numerical experiments. Applicability of citations was checked against the results stated here; their full texts were not consulted. No network, other versions, or other review materials were accessed, and no paper files were modified.

**Substantive issue: Theorem 1.1's critical fractional-dissipation time-regularity assertion for \(p=2\) is false.**

Locations:

- Section 1, theorem `thm:main1`, TeX lines 348–359, especially 352–354, states
  \[
  \nabla u\in L^\infty([0,T],L^2)
  \cap L^1([0,T],B^{2\alpha-1}_{\infty,\infty}),
  \qquad \tfrac12<\alpha<1,\quad p=2.
  \]
- Section 3, Proposition `prop:ap-es-basic`, item (1), formula `eq:u-Gam-es2`, TeX lines 4744–4749, includes
  \[
  \|\nabla u\|_{L^1_T(C^{2\alpha-1})}\leq Ce^{CT}.
  \]
  Here \(0<2\alpha-1<1\), and the paper's Hölder/Besov equivalence gives this the same problem as the preceding assertion.
- The corresponding proof at lines 5053–5055 says only: “For \(\frac12<\alpha<1\), estimate … follows from … [Proposition 3.2]”. This citation cannot supply the false strengthening.

Here is a rigorous counterexample. Fix any \(\alpha\in(\tfrac12,1)\), take \(\varepsilon=1\), \(\theta_0=0\), and write \(s=2\alpha-1\). Let \(\varphi\) be the nonnegative radial annular multiplier in the paper's Littlewood–Paley decomposition. Choose a nonzero, nonnegative, radial function
\[
\widehat h\in C_c^\infty(\mathbb R^2\setminus\{0\}),
\qquad \operatorname{supp}\widehat h\Subset\{\varphi>0\}.
\]
Then \(h\) is a real radial Schwartz function. Let
\[
j_n=4n,\qquad a_n=\frac1n,\qquad
\omega_0(x)=\sum_{n=1}^\infty a_n2^{j_n}h(2^{j_n}x),
\qquad u_0=\nabla^\perp\Lambda^{-2}\omega_0.
\]
These annuli are disjoint and stay away from zero frequency. Plancherel and scaling give
\[
\|\omega_0\|_2^2
=\|h\|_2^2\sum_{n=1}^\infty a_n^2<\infty,
\]
and
\[
\|u_0\|_2^2
\lesssim\sum_{n=1}^\infty a_n^2 2^{-2j_n}<\infty,
\qquad
\|\nabla u_0\|_2\lesssim\|\omega_0\|_2.
\]
Thus \(u_0\in H^1\), \(\operatorname{div}u_0=0\), and \(\theta_0=0\in L^1\cap L^\infty\), satisfying precisely these initial-data conditions of Theorem 1.1.

Define
\[
\omega(t)=e^{-t\Lambda^{2\alpha}}\omega_0,
\qquad
u(t)=\nabla^\perp\Lambda^{-2}\omega(t),
\qquad \theta(t)=0.
\]
Radial symmetry is preserved, so \(u(t,x)=V(t,|x|)e_\vartheta\) is purely rotational. Thus
\[
(u\cdot\nabla)u
=-\frac{V(t,r)^2}{r}e_r.
\]
Take the pressure
\[
\pi(t,r)=\int_0^r\frac{V(t,\rho)^2}{\rho}\,d\rho,
\]
Then \((u\cdot\nabla)u=-\nabla\pi\). Also, \(\partial_tu+\Lambda^{2\alpha}u=0\). Hence \((u,\theta,\pi)\) is an exact solution of the full Boussinesq system for \(\varepsilon=1\), not merely a test of the linearized equation. It is smooth for every \(t>0\) and converges strongly to the prescribed \(H^1\) initial velocity.

Now estimate its critical norm directly. Under the paper's convention \(\nabla^\perp=(\partial_2,-\partial_1)\), the Fourier multiplier from \(\omega\) to \(\partial_1u_2\) is \(\xi_1^2/|\xi|^2\). Frequency separation ensures that \(\Delta_{j_n}\) selects only annulus \(n\). Thus, under the usual Fourier normalization,
\[
\Delta_{j_n}\partial_1u_2(t,0)
=\frac{a_n2^{j_n}}{(2\pi)^2}
\int_{\mathbb R^2}
\varphi(\eta)\frac{\eta_1^2}{|\eta|^2}
e^{-t2^{2\alpha j_n}|\eta|^{2\alpha}}
\widehat h(\eta)\,d\eta.
\]
All integrand factors are nonnegative, and the integral is strictly positive. Set
\[
I_n=[2^{-2\alpha j_n},\,2\cdot2^{-2\alpha j_n}].
\]
For \(t\in I_n\), the scaled time in the integral lies in \([1,2]\), so a constant \(c>0\), independent of \(n,t\), satisfies
\[
\|\Delta_{j_n}\nabla u(t)\|_\infty
\geq c a_n2^{j_n}.
\]
Hence
\[
\|\nabla u(t)\|_{B^s_{\infty,\infty}}
\geq c a_n2^{j_n(s+1)}
=c a_n2^{2\alpha j_n},
\qquad t\in I_n.
\]
These time intervals are pairwise disjoint; for any \(T>0\), all sufficiently large \(n\) satisfy \(I_n\subset(0,T)\). Therefore
\[
\int_0^T\|\nabla u(t)\|_{B^{2\alpha-1}_{\infty,\infty}}\,dt
\geq
\sum_{n\geq n_T}\int_{I_n}c a_n2^{2\alpha j_n}\,dt
=c\sum_{n\geq n_T}\frac1n
=\infty.
\]
This directly disproves the claimed space membership.

The exact solution also has the basic regularity used in the paper's existence and uniqueness argument. Indeed, annular heat decay gives
\[
\|\nabla u_n(t)\|_\infty
\leq C a_n2^{j_n}e^{-ct2^{2\alpha j_n}},
\]
so
\[
\int_0^T\|\nabla u(t)\|_\infty\,dt
\leq C\sum_n a_n2^{-(2\alpha-1)j_n}<\infty.
\]
Moreover, \(u\in L^\infty(0,T;H^1)\cap\widetilde L^1(0,T;B^{2\alpha}_{\infty,\infty})\). Thus the counterexample lies in the theorem's stated basic solution class. Finite partial sums through \(N\) give Schwartz initial velocities and global smooth exact solutions with uniformly bounded initial \(H^1\) norms, while the ordinary \(L^1_t\) norm above grows at least as \(\sum_{n_T\leq n\leq N}1/n\). This also disproves Proposition 3.2's corresponding uniform a priori estimate under its stated initial-norm control.

**Mechanism, impact, and repair.** Each frequency block contributes mainly at its own timescale \(t\simeq2^{-2\alpha j_n}\). Integrating in time before taking the frequency supremum gives a finite Chemin–Lerner norm; reversing the order adds contributions from different timescales, producing a divergent harmonic series. The two critical norms genuinely differ:
\[
\sup_j2^{js}\int_0^T\|\Delta_j\nabla u(t)\|_\infty\,dt
\quad\text{and}\quad
\int_0^T\sup_j2^{js}\|\Delta_j\nabla u(t)\|_\infty\,dt
\]
have different strengths. The Chemin–Lerner embedding at lines 2625–2631 itself permits only a positive spatial-exponent loss here; the lossless condition \(r\leq\rho\) fails for \(r=\infty,\rho=1\).

The most natural repair changes the \(p=2,\alpha<1\) branch of Theorem 1.1 and the corresponding term of `eq:u-Gam-es2` to
\[
\nabla u\in\widetilde L^1(0,T;B^{2\alpha-1}_{\infty,\infty}),
\]
and correspondingly gives
\[
\nabla u\in L^1(0,T;C^\beta),
\qquad 0<\beta<2\alpha-1.
\]
The revision should check which time norm the cited a priori estimate actually provides and update related introductory statements. Retaining the critical ordinary \(L^1_t\) conclusion requires stronger initial data, such as the paper's existing \(p>2\) assumption or a frequency-summability condition suited to this critical time integral.

The affected claims are the current Theorem 1.1's explicit regularity and one basic estimate in Proposition 3.2. Later parameter choices already leave room for repair: Section 4, lines 5928–5931, uses only \(\gamma<2\alpha-1\) for \(p=2\), with critical boundary exponents handled by \(p>2\) estimates; Section 5 assumes \(q>2/(2\alpha-1)>2\), and the infinite-Prandtl-number limit theorems also use velocity exponents strictly greater than 2. After correcting the basic assertions, the dependency chain should be rechecked along these existing strict exponent gaps.

**Other key checks.** The main checks actually completed below help locate and delimit the error.

1. The dissipative term, commutator sign, and \(\varepsilon\) coefficient in the evolution equation for \(\Gamma=\omega-\partial_1\Lambda^{-2\alpha}\theta\) agree; the transported tangential field satisfies \([\partial_t+u\cdot\nabla,\partial_W]=0\). Using \(\operatorname{div}(W_0\mathbf1_{D_0})=0\) to remove boundary measures in tangential temperature differentiation matches the level-set setup.

2. With two differences, the kernel integral in `lem:pW` has locally convergent radial integration for \(\sigma<0\); `lem:pW-Cgam` uses \(\sigma<-1\) for a further spatial derivative. Applications take \(\sigma=1-2\alpha\) and \(\sigma=-2\alpha\), respectively, the latter only for \(\alpha<1\), matching the hypotheses.

3. I checked the exponent intervals improving \(\partial_W\Gamma\) regularity in Section 5. The condition \(q>2/(2\alpha-1)\) ensures \(2\alpha-2/q>1\) and a nonempty \(\gamma'\) interval in the low-exponent proof. The condition \(p>2/(2\alpha-\gamma)\) makes the smoothing gain for initial tangential velocity exceed the target exponent. The endpoint choices \(1<\gamma'<\min\{2\alpha-2/p,2\alpha-2/q\}\) and \(\gamma'-1<\beta<2\alpha-1\) are compatible. The strict profile assumption \(\mu>2-2\alpha\) makes the required endpoint sum \(\sum_j2^{j(2-2\alpha-\mu)}\) converge.

4. Both whole-space low-frequency velocity mechanisms were checked. For \(\alpha<1\), \(Q>1/(1-\alpha)\) makes the large-time semigroup decay exponent \((1-1/Q)/\alpha\) greater than 1. For \(\alpha=1\) with zero total temperature, the first moment yields decay \(r^{-3/2+1/Q}\), integrable for \(Q>2\); the first moment closes through \(\int |u\theta|\) and the velocity \(L^Q\) norm. For nonzero total temperature, the lower-bound proof takes \(R\simeq(1+A_\varepsilon)^{r/2}\), with all powers consistent with the claimed \(\varepsilon^{-1/r}\) bound.

5. Section 6 uses the moving frame only for \(\alpha=1\). Its mean normalization, Morrey sublinear growth control, and common support bound for the relative flow connect consistently. Compactly supported divergence-free test functions have zero spatial integral, eliminating the spatial constant from frame acceleration in the weak momentum identity. After Fourier support of the limiting velocity difference is restricted to the origin, sublinear growth reduces the polynomial remainder to a constant vector; the original-frame \(L^Q\) or moving-frame mean condition then fixes it.

6. In the Lagrangian uniqueness proof for normalized Stokes–transport, \(|\nabla G_\alpha(z)|\lesssim|z|^{2\alpha-3}\) is locally integrable in two dimensions exactly for \(\alpha>1/2\). Strong local negative-Sobolev temperature convergence, conservation of the global \(L^2\) norm, and the compact image of \(t\mapsto\theta(t)\) suffice for the stated \(C_tL^2_x\) convergence step; the fixed-support \(L^1\) argument also matches the theorem's cases.

7. The appendix's velocity cutoff, Leray projection, and convolution use compact support of \(W_0\). Replacing the tangential integrability exponent by \(r=\min\{p,q\}\) retains \(r>2/(2\alpha-\gamma)\). The four-term second-order temperature convolution commutator decomposition, the \(C^{\gamma-1}\) remainder in the Hölder case, and the \(L^\infty\) remainder in the Lipschitz case match the required negative regularity exponents. Subsequent tangential-field compactness and weak-star limits of endpoint spatial derivatives use the corresponding uniform spatial bounds and negative-space time-derivative bounds.

**Ordinary typesetting and notation issues, listed separately.** These differ in nature from the counterexample's mathematical error.

- TeX line 7837 contains `\Vert \nabla u^\varepsilon\Vert _{-L^p)}`, a corrupted norm subscript. Context calls for the corresponding \(L^\infty_tL^p_x\) norm.
- At line 7906, “we have” enters the Morrey estimate's math environment; move it outside the formula and correct the syntax.
- Appendix A.2, lines 9267 and 9300, says “Let \(k=2\)” then “We next consider \(k=3\)”, while the main theorem uses boundary orders \(k\in\{1,2\}\). Clarify that this is internal notation shifted up one order, or directly say “first-/second-order tangential temperature estimate” to avoid confusion.

The review verdict is **REJECT**: the current main theorem contains a critical regularity assertion disproved by an exact solution of the full equation. Revise that time norm and the related a priori estimate, then recheck downstream proofs under the strict exponent conditions above.
