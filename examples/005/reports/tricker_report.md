# Tricker report

## 1. Actual assertion disproved

Fix
\[
 \alpha=\tfrac34,\qquad \varepsilon=1,\qquad p=2,\qquad T=1.
\]
The modified Theorem 1.1 (line 353) and Proposition 3.2(1), (3.1),
`eq:u-Gam-es2` (line 4748), claim that for every divergence-free
\(u_0\in H^1(\mathbb R^2)\), \(\theta_0\in L^1\cap L^\infty\),
\[
 \nabla u\in L^1(0,1;C^{1/2}(\mathbb R^2)).                 \tag{V1}
\]
Here \(C^{1/2}=B^{1/2}_{\infty,\infty}\), as defined at lines 2490–2494.
The original norm is \(\widetilde L^1(0,1;C^{1/2})\). We give:

1. Global smooth exact nonlinear solutions with uniformly bounded initial \(H^1\) norms and diverging (V1) norms;
2. Fixed admissible \(H^1\) initial data whose unique solution has infinite (V1) norm;
3. Failure of a uniform ordinary-time-integrated bound for the appendix's actual smooth approximation.

All temperatures are zero. The counterexample is entirely high-frequency and uses one fixed Prandtl number.

## 2. Radial data compatible with the paper's Littlewood–Paley decomposition

Use the Fourier convention
\[
 \widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx,
 \qquad f(x)=(2\pi)^{-2}\int e^{ix\cdot\xi}\widehat f(\xi)\,d\xi.
\]
Let \(\varphi\) be the nonnegative radial cutoff defining \(\Delta_j\) in the text.
It is nonzero, so there is a compact annulus
\[
 A=\{a\le|\xi|\le b\}\Subset
   \{3/4<|\xi|<8/3,\ \varphi(\xi)>0\}.
\]
Choose nonzero, nonnegative, radial \(h\in C_c^\infty(A)\), and set
\[
 g=\mathcal F^{-1}h,\qquad
 v=\nabla^\perp\Lambda^{-2}g,
 \qquad \nabla^\perp=(\partial_2,-\partial_1).
\]
Then \(g,v\) are real Schwartz functions, \(\operatorname{div}v=0\),
\(\operatorname{curl}v=g\). Their Fourier symbols are respectively
\(h(\xi)\) and \(i(\xi_2,-\xi_1)|\xi|^{-2}h(\xi)\);
the support avoids the origin, so the low-frequency inverse operator is well-defined here.
\(v\) is a radial swirl field: \(v(x)=V(|x|)e_\vartheta\).

Take
\[
 j_n=4n,\qquad \lambda_n=2^{j_n}=16^n,\qquad n\ge1.
\]
For positive \(a_n\), define
\[
 u_0(x)=\sum_{n\ge1}a_n v(\lambda_nx),\qquad \theta_0=0.  \tag{V2}
\]
Also consider arbitrary finite truncations. The annuli \(\lambda_n A\) are pairwise disjoint, and
\(\Delta_{j_n}\) eliminates all other terms exactly: for \(m\ne n\),
\(2^{-j_n}\lambda_m A\) lies outside the support of \(\varphi\).
Indeed, successive scales have ratio 16 and \(A\subset(3/4,8/3)\).

Write \(A_v=\|\nabla v\|_2^2>0\), \(B_v=\|v\|_2^2\).
Two-dimensional scaling and Fourier orthogonality give
\[
 \|u_0\|_{H^1}^2
 =A_v\sum_n a_n^2+B_v\sum_n a_n^2\lambda_n^{-2}.        \tag{V3}
\]
We use an equivalent Hilbert \(H^1\) norm. Thus every \((a_n)\in\ell^2\)
gives divergence-free velocity satisfying all main-theorem initial conditions.

## 3. Exact solutions of the original Boussinesq equation

Define
\[
 u(t)=e^{-t\Lambda^{3/2}}u_0,\qquad \theta(t)=0.          \tag{V4}
\]
Radial Fourier multipliers preserve radial swirl structure, so
\(u(t,x)=V(t,r)e_\vartheta\). Finite sums give globally smooth fields on \(t\ge0\).
Direct calculation gives
\[
 (u\cdot\nabla)u=-\frac{V(t,r)^2}{r}e_r,
 \qquad
 p(t,r)=\int_0^r\frac{V(t,s)^2}{s}\,ds.                \tag{V5}
\]
Since \(V(t,r)=O(r)\) at zero, pressure is smooth there. By (V4)–(V5),
\[
 \partial_tu+u\cdot\nabla u+\Lambda^{3/2}u=-\nabla p,
 \qquad \operatorname{div}u=0,
 \qquad \partial_t\theta+u\cdot\nabla\theta=0.
\]
This is exactly the original system for \(\alpha=3/4,\varepsilon=1,\nu=1\).
Pressure balances convection exactly; no nonlinearity is omitted.

For infinite \(\ell^2\) sums, (V4) holds in \(C([0,T];H^1)\) and
is smooth on every \([\tau,T]\), \(\tau>0\). Finite sums converge in
\(C([0,T];H^1)\). The two-dimensional embedding \(H^1\hookrightarrow L^4\)
gives \(u_N\otimes u_N\to u\otimes u\) in
\(C([0,T];L^2)\), allowing passage to the limit in Definition 3.1's pressure-free weak form.
Linear and initial terms converge strongly too, giving an admissible global weak solution under that definition.

Furthermore, frequency supports and Fourier inversion give
\[
 \|a_n e^{-t\Lambda^{3/2}}v(\lambda_n\cdot)\|_{B^1_{\infty,1}}
 \le C a_n\lambda_n e^{-c t\lambda_n^{3/2}}.
\]
Thus
\[
 \|u\|_{L^1(0,T;B^1_{\infty,1})}
 \le C\sum_n a_n\lambda_n^{-1/2}<\infty
 \quad\text{when }(a_n)\in\ell^2.                         \tag{V6}
\]
It also belongs to \(L^\infty(0,T;H^1)\), and zero temperature belongs to every temperature space of Proposition 3.4,
`prop:uniq`. Thus (V4) is the unique solution named in the main theorem,
independently of the modified ordinary Hölder time-integrated estimate.

## 4. Different frequencies occupy different time windows; ordinary integration accumulates in \(\ell^1\)

Let \(\omega=\operatorname{curl}u\). One initial block has vorticity
\(a_n\lambda_n g(\lambda_nx)\). Since \(\Delta_{j_n}\) eliminates the other blocks,
we have exactly at the origin
\[
 \Delta_{j_n}\omega(t,0)
 =a_n\lambda_n F(t\lambda_n^{3/2}),
 \quad
 F(\tau)=(2\pi)^{-2}\int
   \varphi(\eta)h(\eta)e^{-\tau|\eta|^{3/2}}\,d\eta.      \tag{V7}
\]
\(\varphi h\ge0\) and is nonzero. Hence for \(1\le\tau\le2\),
\[
 F(\tau)\ge c_0:=(2\pi)^{-2}e^{-2b^{3/2}}
                   \int\varphi(\eta)h(\eta)\,d\eta>0.
\]
Consider pairwise disjoint time intervals in \((0,1)\)
\[
 I_n=[\lambda_n^{-3/2},2\lambda_n^{-3/2}]
     =[2^{-6n},2^{1-6n}].                               \tag{V8}
\]
Using \(\omega=\partial_1u_2-\partial_2u_1\) and
norm equivalence of \(C^{1/2}\) and \(B^{1/2}_{\infty,\infty}\), we obtain
\[
 \begin{aligned}
 \|\nabla u(t)\|_{C^{1/2}}
 &\ge c\,2^{j_n/2}\|\Delta_{j_n}\nabla u(t)\|_\infty\\
 &\ge c\,2^{j_n/2}|\Delta_{j_n}\omega(t,0)|
 \ge c_* a_n\lambda_n^{3/2},\qquad t\in I_n.
 \end{aligned}                                         \tag{V9}
\]
Here \(c_*>0\) depends only on the fixed cutoff and \(h\), independently of \(n,N\).
Since \(|I_n|=\lambda_n^{-3/2}\),
\[
 \int_0^1\|\nabla u(t)\|_{C^{1/2}}\,dt
 \ge c_*\sum_n a_n.                                    \tag{V10}
\]

**Smooth solution family.** For each \(N\), take \(a_n=N^{-1/2}\), \(1\le n\le N\),
and zero otherwise. Formula (V3) gives uniform \(H^1\) bounds, all temperature norms vanish, but
\[
 \|\nabla u_N\|_{L^1(0,1;C^{1/2})}\ge c_*\sqrt N\to\infty.
\]
This directly disproves modified (3.1)'s uniform control by the specified initial norms.

**One fixed datum.** Take \(a_n=1/n\). Then
\[
 \sum_n a_n^2=\pi^2/6<\infty,\qquad \sum_n a_n=\infty.
\]
Formulas (V2)–(V6) give an admissible unique global solution, whereas (V10) gives
\[
 \boxed{\ \nabla u\notin L^1(0,1;C^{1/2})\ }.
\]
Every \(T>0\) contains all sufficiently late \(I_n\), so the failure occurs on every
\((0,T)\), disproving the explicitly added main-theorem membership.

## 5. Original norm and all other actual estimates hold

For each block, Fourier-support estimates give
\[
 \|\Delta_{j_n}\nabla u(t)\|_\infty
 \le C a_n\lambda_n e^{-c t\lambda_n^{3/2}}.
\]
A general \(\Delta_j\) meets at most one annulus, and then
\(|j-j_n|\le C\). Thus
\[
 \sup_{j\ge-1}2^{j/2}
  \int_0^T\|\Delta_j\nabla u(t)\|_\infty\,dt
 \le C\sup_n a_n<\infty.                               \tag{V11}
\]
This is precisely the unmodified \(\widetilde L^1_TC^{1/2}\) bound.

Here \(\Gamma=\omega\). The same support estimates also give
\[
 \begin{gathered}
 \|\nabla u\|_{L^\infty_TL^2}
  +\|\Gamma\|_{L^\infty_TL^2}\le C\|(a_n)\|_{\ell^2},\\
 \|\Gamma\|_{\widetilde L^1_TB^{3/2}_{2,\infty}}
   \le C\sup_n a_n,\qquad
 \|\Gamma\|_{L^1_TB^1_{2,1}}
   \le C\sum_n a_n\lambda_n^{-1/2}.
 \end{gathered}                                         \tag{V12}
\]
For \(a_n=1/n\), the final series is exactly
\(\sum_{n\ge1}4^{-n}/n=\log(4/3)\).
Thus all unmodified terms of (3.1) are finite; only the target fails.

The correct embedding at lines 2610–2631 is
\[
 \widetilde L^\rho_TB^{s+\delta}_{p,r}
 \hookrightarrow L^\rho_TB^s_{p,r},\qquad \delta>0,
\]
or requires \(r\le\rho\) when \(\delta=0\). Here
\(r=\infty,\rho=1,\delta=0\), violating the equal-order condition.
Minkowski gives the equal-order direction
\[
 \sup_j\int f_j(t)\,dt\le\int\sup_j f_j(t)\,dt,
\]
The modification implicitly requires reverse control. Formulas (V8)–(V11) show exactly how it fails.

## 6. Actual appendix approximation exposes the same error

For fixed coefficients \(a_n=1/n\), choose the permitted radial
\(\rho\) and radial \(\chi\) in Appendix A.1. Since \(u_0\) is tangential and \(\nabla\chi_\delta\)
radial,
\[
 \operatorname{div}(\chi_\delta u_0)=0,
 \qquad
 u_{0,\delta}=\rho_\delta*(\chi_\delta u_0).
\]
The Leray projection leaves this field unchanged. The approximations remain radial swirls satisfying
\(u_{0,\delta}\in H^m\) for every \(m\), uniform \(H^1\) bounds, and
\(u_{0,\delta}\to u_0\) in \(H^1\).
The corresponding actual global smooth solution is
\(u_\delta(t)=e^{-t\Lambda^{3/2}}u_{0,\delta}\), \(\theta_\delta=0\),
with pressure still given by (V5).

Heat-semigroup \(H^1\) contraction gives \(u_\delta\to u\) in
\(C([0,T];H^1)\). For every fixed \(j\), Bernstein further gives
\(\Delta_j\nabla u_\delta\to\Delta_j\nabla u\) in
\(C([0,T];L^\infty)\). Thus for fixed \(M\), sufficiently small \(\delta\)
preserves half the lower bound (V9) on the first \(M\) windows:
\[
 \int_0^1\|\nabla u_\delta(t)\|_{C^{1/2}}\,dt
 \ge \tfrac12c_*\sum_{n=1}^M\frac1n.
\]
Letting \(\delta\to0\), then \(M\to\infty\), proves
\[
 \liminf_{\delta\to0}
 \|\nabla u_\delta\|_{L^1(0,1;C^{1/2})}=\infty.          \tag{V13}
\]
This directly disproves Appendix B.1's claimed \(\delta\)-uniformity at lines 9895–9896 for all
relevant Proposition 3.2 estimates and the basis at lines 10052–10057 for passing the added bound
to the limit. The regularization is precisely the paper's specified procedure.

## 7. Scope, local checks, and repair

New (3.1) in Proposition 3.2(1) is cited as established at lines 5054–5055;
Appendix B.1 uses it for uniform smooth-solution bounds and limits, and the main-theorem proof
at lines 5871–5874 passes them to Theorem 1.1. Modified line 353
is exactly what the fixed initial data above directly disprove.

For Section 4 Case I's lower boundary exponent \(\gamma<2\alpha-1\), the original
strict regularity margin remains valid. This certificate targets the added critical ordinary time integral,
without asserting that other boundary-preservation conclusions fail for this example.

Every single-frequency test passes: scaling, heat decay, time-integration order, and spatial Hölder
order match. Frequency-separated \(H^1\) inputs combine in \(\ell^2\), while ordinary
time integration accumulates in \(\ell^1\) over separate heat windows. The adjacent \(p>2\) branch
really has ordinary \(L^1\) estimates because the Sobolev/Bernstein loss is less than one derivative,
leaving positive margin; the \(p=2\) branch has none.

The minimal repair restores both `\widetilde` markers at lines 353 and 4748.
Restoring the original blockwise time norm makes (V11)–(V12) compatible with every retained argument.
