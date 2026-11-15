VERDICT: OK

Verification conclusion: the reported error is real, substantive, and sufficiently subtle. The modified main theorem makes a false space-membership assertion for admissible fixed \(H^1\) initial data; the modified a priori estimate also fails for a family of smooth exact solutions with uniform initial norms. The error arises from reversing time integration and the frequency supremum at the critical exponent. It enters the a priori proposition, uniform estimates for the actual regularization, and the main theorem, and no other assumption in the paper excludes this case.

**1. Materials checked and exact locations**

This report read the complete `paper.tex` in the designated input directory (10821 lines, including appendices and references), `tricker-log.md`, `verification.md`, and `mutation.json`. Ranges truncated in the first long output were read separately. No original manuscript, other trials, or other agents' reports were read; no network access, agent contact, or agent spawning occurred. The checker independently rederived the proof below from the paper's definitions; independent computations are in `checker-verification.py` and `checker-verification-results.json` in the same directory.

The target appears in two locations; all line numbers refer to the input `paper.tex`:

| Location | Current assertion | Problem |
|---|---|---|
| Line 353, Theorem 1.1, first branch of label `thm:main1` | For \(1/2<\alpha<1,p=2\), \(\nabla u\in L^1_T B^{2\alpha-1}_{\infty,\infty}\) | Ordinary time-integrated membership at the same order is false |
| Line 4748, Proposition 3.2(1), formula (3.1), final term of label `eq:u-Gam-es2` | \(\|\nabla u\|_{L^1_T C^{2\alpha-1}}\leq Ce^{CT}\) is part of the stated a priori estimate | No such uniform bound exists for the specified initial norms |

Both locations implement the same mathematical strengthening. The proof at lines 5054–5055 merely attributes (3.1) to existing literature and supplies no proof of the strengthened version. We construct an exact counterexample to the original equation directly, without relying on what the citation actually states.

**2. Checking the paper's actual assumptions and notation**

The paper fixes \(\nu=1\) and \(\varepsilon=\mathrm{Pr}^{-1}\in(0,1]\). Theorem 1.1, lines 334–345, explicitly allows \(p=2\), requiring only divergence-free velocity in \(W^{1,2}=H^1(\mathbb R^2)\) and temperature in \(L^1\cap L^\infty\). There is no additional \(W^{1,p},p>2\) assumption, nonzero-temperature or positive-temperature-lower-bound condition, or higher initial velocity smoothness. Proposition 3.2 estimates smooth solutions; the appendix applies it to smooth approximations of rough initial data.

Lines 2473–2504 explicitly set \(H^1=W^{1,2}\), \(C^{1/2}=B^{1/2}_{\infty,\infty}\) (equivalent norms), and ordinary \(L^1_T(X)\) means \(L^1([0,T];X)\). Lines 2554–2631 define the inhomogeneous Littlewood–Paley decomposition, Besov norms, and Chemin–Lerner norms separately. Thus the distinction here is precisely

\[
 \|f\|_{\widetilde L^1_T B^s_{\infty,\infty}}
 =\sup_{j\geq-1}2^{js}\int_0^T\|\Delta_j f(t)\|_\infty\,dt,
 \qquad
 \|f\|_{L^1_T B^s_{\infty,\infty}}
 =\int_0^T\sup_{j\geq-1}2^{js}\|\Delta_j f(t)\|_\infty\,dt.
\]

Minkowski bounds the former by the latter. The reverse embedding listed in the paper requires an arbitrarily small strictly positive loss of spatial regularity, or \(r\leq\rho\) at equal order. Here \(r=\infty,\rho=1\), so there is no reverse embedding at equal order.

I also checked the local conditions in Sections 4 and 5, the infinite-Prandtl-number limit section, and the appendix: the stronger \(p,q\) assumptions belong to their respective boundary or limit theorems and do not apply retroactively to Theorem 1.1's \(p=2\) branch. Lines 7253–7254 currently require exactly zero initial temperature integral for each \(\varepsilon\); this concerns a different issue at \(\alpha=1\). This report takes \(\alpha=3/4\), \(\theta_0=0\), and \(\varepsilon=1\), fully within the actual parameter range.

**3. Independent construction using the plateau annulus guaranteed by the paper's decomposition**

To make the counterexample more explicit, take

\[
 a=\frac{11}{8},\qquad b=\frac{23}{16},\qquad
 h(\xi)=K\begin{cases}
 \exp\!\bigl[-1/(1-(32|\xi|-45)^2)\bigr],&a<|\xi|<b,\\
 0,&\text{otherwise},
 \end{cases}
\]

where \(K>0\) normalizes \((2\pi)^{-2}\int h(\xi)\,d\xi=1\). This is a nonnegative, nonzero, radial \(C_c^\infty\) function.

The paper's decomposition satisfies \(\chi+\sum_{j\geq0}\varphi(2^{-j}\cdot)=1\), with \(\chi\) supported inside radius \(4/3\) and \(\varphi\) in the annulus of radii \(3/4\) to \(8/3\). For \(4/3<|\xi|<3/2\), \(\chi=0\) and all terms with \(j\geq1\) vanish, so **\(\varphi=1\)**. Our \([a,b]\) lies strictly in this interval. The paper's decomposition itself guarantees this choice; no special additional decomposition is needed.

Using Fourier inversion coefficient \((2\pi)^{-2}\), set

\[
 g=\mathcal F^{-1}h,\qquad
 v=\nabla^\perp\Lambda^{-2}g,
 \qquad\nabla^\perp=(\partial_2,-\partial_1).
\]

Since their spectra avoid the origin, \(g,v\) are real-valued Schwartz functions. With the paper's sign convention,

\[
 \operatorname{div}v=0,\qquad
 \operatorname{curl}v
 =-(\partial_1^2+\partial_2^2)\Lambda^{-2}g=g.
\]

\(v\) is a purely tangential radial swirl field. Let \(\lambda_n=16^n\), \(j_n=4n\), and set

\[
 u_0=\sum_{n\geq1}a_n v(\lambda_n\cdot),\qquad \theta_0=0.
 \tag{C1}
\]

The frequency annuli are pairwise disjoint. More precisely, this construction satisfies

\[
 \Delta_{j_n}v(\lambda_m\cdot)
 =\begin{cases}v(\lambda_n\cdot),&m=n,\\0,&m\ne n,\end{cases}
\]

and all other dyadic blocks vanish on these spectra: \(b/2<3/4\), \(2a>8/3\). There is no cancellation across frequency blocks.

Write \(A=\|\nabla v\|_2^2>0\), \(B=\|v\|_2^2>0\). Plancherel and two-dimensional scaling, using a Hilbert norm equivalent to the paper's \(H^1\) norm, give

\[
 \|u_0\|_{H^1,\mathrm{Hilbert}}^2
 =A\sum_n a_n^2+B\sum_n a_n^2\lambda_n^{-2}.
 \tag{C2}
\]

Thus \(a_n=1/n\) gives admissible fixed initial data. These are genuinely endpoint data: for every \(p>2\), their vorticity blocks have \(L^p\) norms

\[
 \|\Delta_{j_n}\operatorname{curl}u_0\|_p
 =\frac1n\lambda_n^{1-2/p}\|g\|_p\longrightarrow\infty.
\]

so these data do not belong to the neighboring \(W^{1,p},p>2\) branch.

**4. Exact nonlinear solution, weak-solution admissibility, and uniqueness**

Fix \(\alpha=3/4\), \(\varepsilon=1\), and define

\[
 u(t)=e^{-t\Lambda^{3/2}}u_0,\qquad \theta(t)=0.
 \tag{C3}
\]

Radial Fourier multipliers preserve the swirl structure. Writing \(u(t,x)=V(t,r)e_\vartheta\), direct calculation gives

\[
 (u\cdot\nabla)u=-\frac{V(t,r)^2}{r}e_r,
 \qquad
 P(t,r)=\int_0^r\frac{V(t,s)^2}{s}\,ds,
 \qquad
 \nabla P=\frac{V^2}{r}e_r.
\]

Also \(\partial_tu+\Lambda^{3/2}u=0\). Hence

\[
 \partial_tu+u\cdot\nabla u+\Lambda^{3/2}u=-\nabla P,
 \quad\operatorname{div}u=0,
 \quad\partial_t\theta+u\cdot\nabla\theta=0.
\]

This is exactly the paper's original system, including the pressure sign. Finite truncations produce global smooth solutions; \(V(t,r)=O(r)\) at the origin ensures smooth pressure.

For the infinite sum, semigroup contraction gives \(u\in C([0,T];H^1)\), with finite truncations converging strongly there; the solution is smooth at every strictly positive time. In two dimensions, \(H^1\hookrightarrow L^4\) ensures \(u_N\otimes u_N\to u\otimes u\) in \(C([0,T];L^2)\). Thus each term passes to the limit in the pressure-free weak formulation of Definition 3.1 at lines 4694–4736. The additional global \(L^1_TL^p\) condition also holds, taking \(p=2\).

For each annulus, Fourier inversion directly gives

\[
 \|e^{-t\Lambda^{3/2}}a_n v(\lambda_n\cdot)\|_\infty
 \leq C a_n e^{-c t\lambda_n^{3/2}}.
\]

Therefore

\[
 \|u\|_{L^1_TB^1_{\infty,1}}
 \leq C\sum_n a_n\lambda_n^{-1/2}
 =C\sum_n\frac{4^{-n}}n<\infty.
 \tag{C4}
\]

Together with \(L^\infty_TH^1\) and zero temperature, this places the solution in every uniqueness space of Proposition 3.4 at lines 5618–5644. We also have

\[
 \|u\|_{\widetilde L^1_TB^{3/2}_{\infty,\infty}}
 \leq C\sup_n a_n<\infty.
\]

Thus this exact solution is the solution described by Theorem 1.1, rather than an unrelated solution in a different weak class. This identification uses only the retained uniqueness conditions and the finite norms obtained directly above.

**5. Divergence of the target norm; finiteness of the original norm and other terms**

Write \(\omega=\operatorname{curl}u\). Exact frequency isolation gives at the origin

\[
 \Delta_{j_n}\omega(t,0)
 =a_n\lambda_n F(t\lambda_n^{3/2}),\qquad
 F(\tau)=(2\pi)^{-2}\int h(\eta)e^{-\tau|\eta|^{3/2}}\,d\eta.
 \tag{C5}
\]

Since \(h\geq0\) and \(F(0)=1\), for \(1\leq\tau\leq2\) there is a strictly positive lower bound

\[
 F(\tau)\geq e^{-2b^{3/2}}>0.
\]

Let \(I_n=[\lambda_n^{-3/2},2\lambda_n^{-3/2}]=[2^{-6n},2^{1-6n}]\). These intervals lie in \((0,1)\) and are pairwise disjoint. The component relation between curl and gradient and the paper's Hölder–Besov norm equivalence yield \(c>0\), independent of \(n\), such that

\[
 \|\nabla u(t)\|_{C^{1/2}}
 \geq c\lambda_n^{1/2}|\Delta_{j_n}\omega(t,0)|
 \geq c a_n\lambda_n^{3/2},\qquad t\in I_n.
\]

Each time window has length \(\lambda_n^{-3/2}\), so

\[
 \int_0^1\|\nabla u(t)\|_{C^{1/2}}\,dt
 \geq c\sum_n a_n.
 \tag{C6}
\]

For \(a_n=1/n\), the initial energy in (C2) is finite, whereas (C6) is the divergent harmonic series. This rigorously disproves the modified Theorem 1.1. Every \(T>0\) contains all sufficiently late \(I_n\), so the same solution fails on every \((0,T)\).

For the smooth solutions required by the proposition, take an equal-amplitude finite sum over \(1\leq n\leq N\), with

\[
 a_n=b_N:=\left(AN+B\sum_{n=1}^N\lambda_n^{-2}\right)^{-1/2}.
\]

Then the initial Hilbert \(H^1\) norm is **exactly 1**, while the target norm is bounded below by \(cNb_N\asymp\sqrt N\to\infty\). All initial temperature norms are zero. This also directly tests the actual setting of the a priori estimate.

On the other hand, integrating the blockwise upper bounds above gives

\[
 \sup_j 2^{j/2}\int_0^T\|\Delta_j\nabla u(t)\|_\infty\,dt
 \leq C\sup_n a_n<\infty.
 \tag{C7}
\]

This is precisely the Chemin–Lerner norm with the tilde restored. Here \(\Gamma=\omega\). The other terms of (3.1) satisfy

\[
 \|\nabla u\|_{L^\infty_TL^2}+\|\Gamma\|_{L^\infty_TL^2}
 \leq C\|(a_n)\|_{\ell^2},
\]
\[
 \|\Gamma\|_{\widetilde L^1_TB^{3/2}_{2,\infty}}
 \leq C\sup_n a_n,
 \qquad
 \|\Gamma\|_{L^1_TB^1_{2,1}}
 \leq C\sum_n a_n\lambda_n^{-1/2}.
\]

Thus the failure occurs precisely in the modified term.

For the explicit \(h\) selected here, the independent script computes \(F(1)\approx0.1886980350\), \(F(2)\approx0.0356243437\), and \(\int_1^2F(\tau)\,d\tau\approx0.0918157309>0\). Frequency isolation and disjointness of time windows are checked exactly using rational numbers. Numerical integration only checks constants and scaling; divergence follows from the analytic lower bound and harmonic series above.

**6. Actual regularization and downstream effects**

The actual smooth approximation claimed in Section 6 of `verification.md` also works. Appendix A.1, line 9058 onward, permits arbitrary nonnegative smooth mollifiers and spatial cutoffs; take both radial. Since \(u_0\) is purely tangential and \(\nabla\chi_\delta\) radial,

\[
 \operatorname{div}(\chi_\delta u_0)=0,
 \qquad
 u_{0,\delta}=\rho_\delta*(\chi_\delta u_0).
\]

The Leray projection is the identity here. Radial convolution preserves rotational symmetry, divergence freedom, and the purely tangential structure; alternatively, the radial component of a rotationally symmetric divergence-free smooth field must be \(C/r\), and regularity at the origin forces \(C=0\). Hence the corresponding smooth solutions are still exactly

\[
 u_\delta(t)=e^{-t\Lambda^{3/2}}u_{0,\delta},\qquad\theta_\delta=0.
\]

The appendix's cutoff and convolution give \(u_{0,\delta}\to u_0\) in \(H^1\), so \(u_\delta\to u\) in \(C([0,T];H^1)\). For each fixed block, Bernstein gives

\[
 \|\Delta_j\nabla(u_\delta-u)\|_{L^\infty_TL^\infty}
 \leq C2^j\|u_\delta-u\|_{L^\infty_TH^1}\longrightarrow0.
\]

For any fixed \(M\), choosing sufficiently small \(\delta\) preserves half of the lower bound (C6) on the first \(M\) time windows. Thus

\[
 \liminf_{\delta\to0}\|\nabla u_\delta\|_{L^1(0,1;C^{1/2})}
 \geq \frac c2\sum_{n=1}^M\frac1n.
\]

Letting \(M\to\infty\), the target norm of the actual regularized solutions tends to infinity. The counterexample appendix in `verification.md` omits no nonlinearity, projection, or convergence condition in this step.

The specific propagation chain in the paper is:

| Text location | Verified effect |
|---|---|
| Lines 5054–5055 | Cites strengthened (3.1) as an existing a priori result; the exact smooth solution family disproves this strengthening |
| Appendix B.1, lines 9881–9896 | Uses Proposition 3.2 to establish uniform regularization bounds and states uniformity in \(\delta\); the last term diverges along the actual approximation above |
| Appendix B.1, lines 10052–10057 | Claims all remaining estimates pass to the limit by lower semicontinuity; the required uniform ordinary-time-integral bound does not exist |
| Proof of Theorem 1.1, lines 5871–5874 | Explicitly inherits all estimates of Proposition 3.2 |
| Theorem 1.1, line 353 | The unique solution for fixed admissible initial data violates the final claimed space membership |

Lower semicontinuity itself is not the issue; the missing ingredient is exactly the incorrectly strengthened uniform estimate. Nor can the error be fixed by adding an omitted derivation, since an exact solution disproves its conclusion.

The impact is precisely the main theorem's added critical ordinary-time-integrated membership and corresponding a priori and uniform approximation estimates. At lines 5928–5931, the \(p=2\) case actually uses the strictly lower exponent \(\gamma<2\alpha-1\); the restored Chemin–Lerner bound supplies the required embedding there. The critical boundary exponent uses the \(p>2\) branch, and second-order boundary and Section 6 limit results also require stronger velocity exponents. Thus the error affects one main-result component, while repairing it does not require overturning arguments that retain a regularity margin.

**7. Subtlety, extra-change check, and repair**

The subtlety requirement is met. Both edits merely delete tildes, leaving parameters, spatial and temporal orders, and constant forms unchanged; the adjacent \(p>2\) branch genuinely uses ordinary \(L^1\), making the result look naturally consistent. For single-frequency data, both norms have the same order and all heat-decay and scaling checks pass. Detecting the issue requires tracking \(H^1\) frequency square summability, heat time windows dominated by different frequencies, and the order of integration and frequency supremum. Zero temperature does not remove the problem: nonlinear pressure balance preserves this endpoint mismatch.

Although small, the error is not a harmless typo: the main theorem and a priori proposition change together, and the appendix propagates it as an actual uniform estimate. The minimal repair is restoring `\widetilde L^1` at line 353 and `\widetilde{L}^1_T` at line 4748. Retaining ordinary \(L^1\) requires lowering the spatial exponent or strengthening initial frequency summability/regularity, changing the proposition's current scope.

Both have 10821 lines. The exact zero-mean condition at lines 7253–7254 is present. This check detects no off-target source edits beyond the two logged changes; baseline identity comes from the authorized log, and verification did not access the original manuscript.

All three criteria are met: a real error, a substantive error that enters the main argument, and a small natural change requiring mathematical detail to identify. Verdict: **OK**.
