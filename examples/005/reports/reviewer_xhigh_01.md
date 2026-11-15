VERDICT: REJECT

I read the complete current `paper.tex`, including main text, appendices, and bibliography, and checked dependencies among the main estimates. The manuscript has a substantive mathematical error admitting an exact-solution counterexample: for $p=2$, $1/2<\alpha<1$, Theorem 1.1's claimed ordinary time-space regularity $L^1_t B^{2\alpha-1}_{\infty,\infty}$ fails. The same problem occurs in Proposition 3.2's basic a priori estimate. Zero temperature and radial vorticity make the counterexample directly applicable to this paper's nonlinear equation.

## 1. Substantive error: the critical ordinary $L^1_t$ estimate for $p=2$ is false

### Locations in the text

- Theorem 1.1, label `thm:main1`, TeX lines 348–354, states

  > `L^\infty([0,T],L^2) \cap L^1([0,T],B^{2\alpha-1}_{\infty,\infty}), ... if ... p=2`.

- Proposition 3.2(1), label `prop:ap-es-basic`, formula `eq:u-Gam-es2`, TeX lines 4744–4749, writes, assuming only $u_0\in H^1$, $\theta_0\in L^1\cap L^\infty$,

  > `+ \Vert \nabla u\Vert _{L^1_T(C^{2\alpha-1})} \leq C e^{C T}`.

- The corresponding proof at TeX lines 5053–5055 says directly

  > `For ... estimate ... follows from ... [Proposition 3.2]{LXY25}`.

Here $0<2\alpha-1<1$, and the paper's own definition gives $C^{2\alpha-1}=B^{2\alpha-1}_{\infty,\infty}$. Both locations therefore assert the same critical time-integrated regularity.

### Rigorous counterexample

Fix any $\alpha\in(1/2,1)$, and take $\varepsilon=1$, $\theta_0=0$. Denote the radial nonnegative symbol of the paper's high-frequency Littlewood–Paley blocks by $\varphi$. Choose a nonzero, nonnegative, radial function

\[
 \widehat\psi\in C_c^\infty(\mathbb R^2\setminus\{0\}),
\]

supported in a small annulus where $\varphi>0$. Then $\psi$ is a real radial Schwartz function with spectrum avoiding the origin.

Let $j_n=10n$, $a_n=1/n$, and define

\[
 \omega_0(x)=\sum_{n\ge1}a_n2^{j_n}\psi(2^{j_n}x),
 \qquad
 u_0=\nabla^\perp\Lambda^{-2}\omega_0.
\]

The spectra are pairwise disjoint. Two-dimensional scaling and Plancherel give

\[
 \|\omega_0\|_2^2=\|\psi\|_2^2\sum_{n\ge1}a_n^2<\infty,
 \qquad
 \|u_0\|_2^2=C_\psi\sum_{n\ge1}a_n^22^{-2j_n}<\infty.
\]

Also $\|\nabla u_0\|_2=\|\omega_0\|_2$. Thus $u_0\in H^1(\mathbb R^2)$ and $\operatorname{div}u_0=0$, satisfying the theorem's $p=2$ initial-data conditions exactly.

Now take

\[
 \omega(t)=e^{-t\Lambda^{2\alpha}}\omega_0,
 \qquad
 u(t)=\nabla^\perp\Lambda^{-2}\omega(t),
 \qquad \theta(t)=0.
\]

This is both a linear-equation example and an exact solution of the paper's Boussinesq equation: $\omega(t)$ is radial and $u(t)$ circumferential, so

\[
 u\cdot\nabla\omega=0.
\]

Thus the vorticity equation reduces exactly to the fractional heat equation. Equivalently, writing $u=v(t,r)e_\vartheta$ gives

\[
 (u\cdot\nabla)u=-\frac{v(t,r)^2}{r}e_r,
\]

a radial gradient absorbed by pressure. Finite truncations yield global smooth exact solutions converging in $L^\infty_tH^1_x$, so the infinite sum also defines a weak solution with the specified initial data. It is smooth for every positive time.

Frequency separation ensures that $\Delta_{j_n}$ sees only term $n$. Hence

\[
 (\Delta_{j_n}\omega)(t,0)
 =a_n2^{j_n} b(t2^{2\alpha j_n}),
\]

where, for a positive Fourier-normalization constant $c_F$,

\[
 b(s)=c_F\int_{\mathbb R^2}
 \varphi(\xi)e^{-s|\xi|^{2\alpha}}\widehat\psi(\xi)\,d\xi.
\]

The integrand is nonnegative and nonzero, so some $c>0$ satisfies $b(s)\ge c$ for $1\le s\le2$. Set

\[
 I_n=[2^{-2\alpha j_n},\,2\,2^{-2\alpha j_n}].
\]

These intervals are pairwise disjoint and all lie in $(0,1)$. For $t\in I_n$,

\[
 \|\omega(t)\|_{B^{2\alpha-1}_{\infty,\infty}}
 \ge 2^{(2\alpha-1)j_n}
      \|\Delta_{j_n}\omega(t)\|_\infty
 \ge c a_n2^{2\alpha j_n}.
\]

Since $\omega=\partial_1u_2-\partial_2u_1$, blockwise we have

\[
 \|\Delta_j\omega\|_\infty
 \le C\|\Delta_j\nabla u\|_\infty.
\]

Therefore

\[
 \begin{aligned}
 \int_0^1\|\nabla u(t)\|_{B^{2\alpha-1}_{\infty,\infty}}\,dt
 &\ge c\sum_{n\ge1}
       \int_{I_n}a_n2^{2\alpha j_n}\,dt\\
 &=c\sum_{n\ge1}\frac1n=\infty.
 \end{aligned}
\]

This directly contradicts Theorem 1.1's membership conclusion. For any $T>0$, simply take sufficiently large $n$ so that $I_n\subset(0,T)$.

The solution also has the theorem's basic solution-class regularity: $u\in L^\infty_tH^1_x\cap\widetilde L^1_tB^{2\alpha}_{\infty,\infty}$. The latter follows directly from velocity-block amplitudes $O(a_n)$ and heat-decay times $O(2^{-2\alpha j_n})$. Thus the counterexample lies in the paper's existence and uniqueness framework.

For Proposition 3.2's a priori bound, stated only for smooth solutions, truncate to the first $N$ terms: initial $H^1$ norms are uniformly bounded, while the ordinary $L^1_tC^{2\alpha-1}$ norm on the left is at least $c\sum_{n=1}^N1/n$. This contradicts a uniform a priori bound controlled by the prescribed initial norms.

### Error mechanism

At criticality one must distinguish

\[
 \sup_j2^{j(2\alpha-1)}
       \int_0^T\|\Delta_j\nabla u(t)\|_\infty\,dt
 \quad\text{and}\quad
 \int_0^T\sup_j2^{j(2\alpha-1)}
       \|\Delta_j\nabla u(t)\|_\infty\,dt.
\]

The former is the Chemin–Lerner norm; the latter is the ordinary $L^1_tB^{2\alpha-1}_{\infty,\infty}$ norm. Here different frequencies contribute on disjoint timescales; $H^1$ initial data supply only square summability of frequency coefficients, whereas ordinary time integration accumulates a divergent harmonic series. The embedding with strict regularity loss at TeX lines 2623–2630 agrees with this phenomenon.

### Impact and repair direction

The direct impact is on Theorem 1.1's $p=2$, $\alpha<1$ branch and the last term of Proposition 3.2(1). The assertion fails even at fixed $\varepsilon=1$, so Prandtl-number uniformity is not the problem.

Change this branch to

\[
 \nabla u\in L^\infty_tL^2_x
 \cap\widetilde L^1_tB^{2\alpha-1}_{\infty,\infty},
\]

and explicitly deduce ordinary $L^1_tC^\gamma$ bounds for every $\gamma<2\alpha-1$. Retaining ordinary $L^1_tC^{2\alpha-1}$ requires additional frequency summability in the initial data, for example $\omega_0\in B^0_{2,1}$ for this initial layer, together with renewed verification of the full nonlinear estimate.

Section 4 Case I (TeX lines 5922–5931) actually uses the strict range $\gamma<2\alpha-1$ for $p=2$, while critical $\gamma=2\alpha-1$ requires $p>2$. The main arguments in Sections 5 and 6 also use velocity exponents above 2. Thus the minimal revision first corrects these two critical time spaces, then checks each citation; the paper's existing strict exponent margins support this repair.

## 2. Actual scope and key checks

The review used the complete TeX source, covering all main theorems in the introduction, technical lemmas, global well-posedness, two orders of boundary regularity, the infinite-Prandtl-number limit, and both appendices. Only designated paper materials were used, with no other versions, full external papers, or experimental materials accessed. The counterexample above is analytic and uses no numerical conjecture.

Key checks included:

1. **Good unknown and endpoint low frequencies.** I checked the equation and signs for $\Gamma=\omega-\partial_1\Lambda^{-2\alpha}\theta$; at $\alpha=1,p=2$, the motivation and estimate dependencies for splitting initial data into $L^2$ and $L^q,q>2$ parts agree. The current manuscript uses $\widetilde L^1$ at this classical dissipation endpoint, consistent with the distinction revealed by the counterexample.
2. **Negative-order kernel estimates.** I checked how difference factors cancel kernel singularities in `lem:pW` and `lem:pW-Cgam`, and the cutoff-boundary exponents $\delta^{-\sigma}$, $\delta^{-1-\sigma}$; the corresponding $\sigma<0$, $\sigma<-1$ conditions match the applications.
3. **Boundary exponents and closure.** I checked profile regularity in all four cases of Sections 4 and 5, strict $p,q$ inequalities, and nonempty auxiliary $\gamma'$ and $\beta$ intervals, particularly closure of the Lipschitz endpoint through $W^{1,\infty}$ rather than integer Hölder–Zygmund spaces.
4. **Low-frequency velocity and moving frame.** I checked heat-kernel time integrability for $Q>1/(1-\alpha)$ when $\alpha<1$, first-absolute-moment closure at $\alpha=1$ with zero mean, and mean normalization, support control, and vanishing inertia with nonzero mean. Scaling exponents in the nonzero-mean $\varepsilon^{-1/r}$ lower bound agree.
5. **Limit identification and uniqueness.** I checked the product limit from strong local negative-Sobolev temperature compactness and weak velocity convergence, elimination of velocity constants through support or $L^Q$, upgrading to global $C_tL^2_x$ convergence by flow representations and conserved norms, and Lagrangian uniqueness supported by radial kernel differences.
6. **Regularization.** I checked the appendix's tangential temperature commutator, $D_1$–$D_4$ decomposition of the second tangential derivative, compactly supported tangential fields and Leray-cutoff far-field estimates, and retention of the threshold after setting $r=\min(p,q)$. The compactness passages use divergence form for tangential nonlinear products with a clear logical connection.

The decisive basis for rejection is the counterexample in Section 1; the other checks describe the argument chains actually reviewed.

## 3. Typesetting and expression issues (listed separately)

- TeX line 7837's `\Vert \nabla u^\varepsilon\Vert _{-L^p)}` is visibly corrupted; restore the corresponding $L^\infty([0,T];L^p)$ norm.
- At TeX lines 7906–7907, `we have` appears inside the Morrey inequality's math environment; move it outside.
- Appendix A.2, lines 9267 and 9300, uses “$k=2$” and “$k=3$,” while the main theorems use $k=1,2$ for boundary differentiation order. This appears to follow the tangential initial-data lemma's index; use another letter or explain it to avoid confusion with the theorem's $k$.

These prose and typesetting issues can be corrected directly. Section 1's critical time-space error requires changing the mathematical statements and corresponding estimates.
