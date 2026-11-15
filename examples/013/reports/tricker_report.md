# Tricker report

## Summary of the mathematical defect

For each fixed negative exponent \(t\), the original proof first chooses a finite lag cutoff

\[
n_2(t,\eta)=\left\lceil |t|^{-1}\log(8/\eta)\right\rceil.
\]

The tail beyond that cutoff is harmless for every measure on the band. Only then does it choose a sufficiently fine quadrature to preserve the finitely many strict constraints below the cutoff. Thus the quadrature is an existential witness whose permitted resolution depends on \(t\), hence on \(\varepsilon\) when \(t=\log(1-c\varepsilon)\).

The new passage fixes one partition and then transports its midpoints for each \(\varepsilon\). It retains the correct density weights and a strict minimizer slack. The next invocation of lem:startup nevertheless needs all-lag feasibility, which this fixed partition does not have.

The disproof uses the paper's exact TMM family and a fixed band around \(2\pi/3\). Every finite uniform midpoint grid in the prescribed construction has a common rational period \(P\). As \(\varepsilon\to0\), its upper lag \(P-1\) fails. More strongly, a positive combination of the lower lag-one inequality and the upper lag-\(P-1\) inequality cancels the value constant \(C\) exactly and becomes negative. Consequently **no value constant can make that fixed grid feasible for all sufficiently small \(\varepsilon\)**.

This is not a numerical quadrature error estimate with a wrong constant. Every fixed finite grid fails eventually, however fine it is. Nor is it a failure to normalize the density: the new weights use the original \(1/R\) factor correctly. It is a witness-dependence error.

The unchanged statement of lem:spreadwit still allows \(J=J_\varepsilon\), as the original construction requires. Its existential conclusion and the later rate theorems are not refuted here. The modified proof's actual fixed-grid witness construction is invalid.

## Exact new replacement and locations

Replacement 2 is the only new introduction. It occurs at the end of the “The lag-one constraint” paragraph in the proof of lem:spreadwit. In the supplied current paper it starts partway through line 4336 and ends at line 4338. After the prior repair, it starts partway through output line 4332 and ends at line 4336.

BEFORE:

~~~tex
\Cref{lem:spreadhalf} gives a
pair with finitely many atoms in \(B\), feasible at \(t\), with \(|C'|<\bar g'\), and \Cref{lem:startup} gives \(f\in\cF_{\varepsilon^2,1}(\C^J\oplus\R)\) and \(x_0\)
with \(\norm{x_N}\ge c_0r^N\norm{x_0}\); so \(\rhoz\ge1-c\varepsilon\).
~~~

AFTER:

~~~tex
Fix a sufficiently fine uniform midpoint partition of \([-1,1]\) into \(2J\) cells for the finite-atom step of \Cref{lem:spreadhalf}.
For each \(\varepsilon\), map its midpoints \(a_j\) to \(\omega_j=\omega_0+\mathsf w a_j\), assign normalized weights
proportional to \(\mathsf k(a_j)/R(\omega_j)\), and set \(C'=-(1-\eta)\bar g'\).
The minimizer slack is strict, and \Cref{lem:startup} gives \(f\in\cF_{\varepsilon^2,1}(\C^J\oplus\R)\) and \(x_0\)
with \(\norm{x_N}\ge c_0r^N\norm{x_0}\); so \(\rhoz\ge1-c\varepsilon\).
~~~

Occurrence count: exactly one.

The exact failure is the transition from the fixed partition at output lines 4332–4334 to the startup invocation at output lines 4335–4336. Strict minimizer slack is true, but it is only one of the required hypotheses. The selected pair must also satisfy every lower and upper lag inequality.

There is no added theorem assertion about a common objective or a uniform dimension bound. The loss of dependence is embedded in the construction: one partition is fixed, then its midpoints are used “for each epsilon.” The subsequent use of that pair is part of the existing realization and lower-bound proof.

## Dependency chain through the paper

The following locations describe the cross-context restriction.

- Lines 899–909, def:feas and eq:feas: feasibility requires both lag inequalities for every \(n\ge1\), together with the minimizer constraints.
- Lines 2731–2744, lem:waves and eq:slacks: these slacks are the actual simultaneous interpolation conditions, with positive scaling factors. A negative upper slack is an interpolation failure.
- Source lines 3150–3158, output lines 3146–3154, lem:startup: a feasible finite pair is the input to the from-rest construction. The lemma does not say strict minimizer slack alone suffices.
- Source lines 3488–3504, output lines 3484–3500: the smooth kernel, band, phase, density proportional to \(\mathsf k/R\), and parameter \(\eta\) are defined.
- Source lines 3513–3575, output lines 3509–3571: Fourier decay of the smooth kernel supplies the continuous-spectrum margins. This part is unchanged.
- Source lines 3577–3584, output lines 3573–3580: the finite-atom step first selects \(n_2=\lceil |t|^{-1}\log(8/\eta)\rceil\), then chooses a grid fine enough for all \(n<n_2\). Its witness choice depends on this finite set.
- Source lines 4294–4306, output lines 4290–4302, lem:spreadwit: the exponent is \(t=\log(1-c\varepsilon)\), and the statement expressly allows a finite \(J=J_\varepsilon\).
- Source lines 4328–4336, output lines 4324–4332: the phase and lag-one hypotheses are checked as \(\varepsilon\to0\), and \(\eta=\min(1/2,\lambda_0/(2c))\) is fixed.
- New output lines 4332–4336: the grid is now fixed before the for-each-\(\varepsilon\) transport and is used in the existing startup construction.
- The wall-layer and corner lower-bound proofs subsequently invoke lem:spreadwit. They need an actual feasible finite pair for each member, not a weak approximation which is accurate only on a previously selected finite collection of lags.

The finite-atom justification and the modified witness selection are separated by approximately 750 source lines and several intervening normal-form, expansion, and stability arguments. Recovering the missing dependence requires combining the lag definition, the tail cutoff, and the later parameter order.

## Why the original proof is valid

Fix one admissible \(\varepsilon>0\), hence one \(t<0\), band, method, and value of \(\eta\). The smooth density constructed by lem:spreadhalf satisfies all constraints strictly.

For every probability measure on the band and \(C'=-(1-\eta)\bar g'\), the bound

\[
\left|\int (g\mp2is)e^{in\omega}\,d\nu'\right|
<4\bar g'
\]

holds. The hyperbolic factor is at least \((\eta/2)e^{n|t|}\). Therefore every lag at or above \(n_2(t,\eta)\) is automatically valid, uniformly over the measure.

Below that cutoff, only finitely many continuous test functions remain. Weak convergence of Riemann sums preserves their finitely many strict inequalities once the grid is sufficiently fine. The density is continuous on the compact band, with \(R>0\), so uniform midpoint quadrature is one legitimate way to implement this step.

The original proof then uses the resulting pair for this \(\varepsilon\) and applies lem:startup. Repeating for each smaller \(\varepsilon\) is valid. It does not require the same quadrature resolution to work at every member of the family.

## Exact in-context counterexample

### 1. The admissible stationary family

Use the exact TMM family already printed in eq:robust and the proof of cor:TMM. Let

\[
L=1,\qquad \mu=\varepsilon^2,\qquad
\beta_\varepsilon=\frac{(1-\varepsilon)^2}{1+\varepsilon},
\qquad y_\varepsilon=h_\varepsilon=2-\varepsilon,
\qquad
\tau_\varepsilon=\frac{(1-\varepsilon)^2}{(2-\varepsilon)(1+\varepsilon)}.
\]

For \(0<\varepsilon<1/2\), these are admissible tunings: \(0<\beta_\varepsilon<1\), \(\tau_\varepsilon>0\), and \(h_\varepsilon>0\). Because \(y_\varepsilon\tau_\varepsilon=\beta_\varepsilon\),

\[
y_\varepsilon(1+2\tau_\varepsilon)-2(1+\beta_\varepsilon)
=y_\varepsilon-2=-\varepsilon<0.
\]

Thus they are stable by lem:qstab, without relying on the theorem being tested.

They have

\[
\theta_\varepsilon=\frac{1-\beta_\varepsilon}{\varepsilon}
=\frac{3-\varepsilon}{1+\varepsilon}\longrightarrow3,\quad
y_\varepsilon\longrightarrow2,\quad
\tau_\varepsilon\longrightarrow\tfrac12.
\]

They are the memory-D=2 stationary method

\[
u_\varepsilon(z)=(1+\tau_\varepsilon)z-\tau_\varepsilon,\qquad
v_\varepsilon(z)=-h_\varepsilon^{-1}(z-1)(z-\beta_\varepsilon).
\]

Their coefficients are smooth in \(\varepsilon\) near zero, though lem:spreadwit does not need that extra regularity.

Choose

\[
c=\frac98,\qquad r_\varepsilon=1-\frac98\varepsilon,\qquad
t_\varepsilon=\log r_\varepsilon,\qquad K=3,\quad \omega_0=\frac{2\pi}3.
\]

The required inequality \(0<c<\theta/2\) holds because \(9/8<3/2\).

Let \(q\) be any integer with

\[
q\ge12,\qquad \frac1q\le\mathsf s_1,
\]

where \(\mathsf s_1>0\) is the kernel constant already supplied by lem:spreadhalf. Set

\[
\mathsf s=\frac1q,\qquad \mathsf w=\frac{\omega_0}{q},\qquad
B=[(1-1/q)\omega_0,(1+1/q)\omega_0].
\]

This is a fixed allowed band. Its constants may depend on the fixed kernel; no explicit numerical value of that kernel constant is needed.

For every \(\omega\in B\),

\[
\frac{11\pi}{18}\le\omega\le\frac{13\pi}{18}<\frac{3\pi}4,
\qquad
1<\xi:=1-\cos\omega<1+\frac{\sqrt2}{2}<\frac{12}7.
\tag{B}
\]

The last inequality follows from \(\sqrt2<10/7\), whose square is \(2<100/49\). These are exact inequalities.

### 2. Every hypothesis of lem:spreadwit holds

At the TMM corner, the limiting parameters are

\[
(\theta,a,b)=(3,5/4,1),\qquad \mathsf N(\xi)=4(3-\xi).
\]

The unchanged corner expansions, source lines 4832–4845 and output lines 4830–4843, give uniformly on the fixed band

\[
\frac{H_{r_\varepsilon}(\omega)}{\varepsilon}
\longrightarrow 4(1-c)\xi(3-\xi)
=-\frac12\xi(3-\xi),
\tag{H}
\]

and

\[
\frac{\mathsf M_{r_\varepsilon}(\xi)}{\varepsilon}
\longrightarrow4(3-\xi)-2c(4-\xi)
=3-\frac74\xi.
\tag{M}
\]

The term \(\mathsf P_0=O(\varepsilon^3)\) does not affect (H).

The band has fixed \(\xi_{\max}>0\), so

\[
\varepsilon=o(\xi_{\max}^{3/2}),\qquad
\max_B|\mathsf M_{r_\varepsilon}|=O(\varepsilon)
=o(\xi_{\max}^{3/2}).
\]

On the interval (B), \(\xi(3-\xi)\ge2\). Hence (H) implies

\[
H_{r_\varepsilon}\le-\tfrac34\varepsilon
\]

for all sufficiently small \(\varepsilon\). At \(\varepsilon=0\),

\[
\chi_\mu(z)=(z-1)^2,\qquad
\chi_L(z)=z(z+1)\qquad(|z|=1).
\]

Their product has modulus at most \(4\cdot2=8\), so by uniform continuity

\[
\Xi_B=\max_B|\chi_\mu\overline{\chi_L}|\le9
\]

for small \(\varepsilon\). Taking

\[
\lambda_0=\frac1{16}
\]

therefore gives

\[
H_{r_\varepsilon}\le-\tfrac34\varepsilon
\le-\lambda_0\varepsilon\Xi_B.
\]

This checks the last hypothesis of lem:spreadwit with the exact specified constant. Its proof then chooses

\[
\eta=\min\left(\frac12,\frac{\lambda_0}{2c}\right)
=\frac1{36}.
\]

The signs \(g>0,s>0\), continuous phase, and bounds in eq:spreadhyp follow either from the unchanged sign/defect argument of lem:spreadwit, whose hypotheses have just been checked, or directly from the limits below. In particular, \(t=O(\varepsilon)\), the phase defect is \(O(\varepsilon)\), while \(\mathsf m,\mathsf w,\eta\) are fixed and positive. The lag-one condition eq:spreadl1 is verified by the unchanged argument for every measure on this band.

Thus this example is inside the precise scope of the modified lemma and the cited half-step lemma. It is not a limiting \(\mu=0\) input: the actual counterexamples use positive sufficiently small \(\varepsilon\), so \(0<\mu<L\).

### 3. The limiting symbols and the mixed term

Write \(g_\varepsilon,s_\varepsilon,R_\varepsilon\) for the symbols on \(z=r_\varepsilon e^{i\omega}\), and

\[
\mathfrak c_\varepsilon
=\frac4{y_\varepsilon^2(1-\varepsilon^2)^2}\longrightarrow1.
\]

By eq:factor,

\[
g_\varepsilon-2is_\varepsilon
=-\mathfrak c_\varepsilon\chi_\mu\overline{\chi_L}.
\]

At the limit this gives, on \(B\),

\[
g_0(\omega)=2\xi(2-\xi)>0,\qquad
2s_0(\omega)=2\xi\sin\omega,\qquad
R_0(\omega)=4\xi\cos(\omega/2)>0.
\tag{G}
\]

For example, \(\chi_\mu=(z-1)^2=-2\xi z\) and
\(\chi_L=z(z+1)\), so
\(-\chi_\mu\overline{\chi_L}=2\xi(1+\bar z)\), which proves (G).

Define the scalar function

\[
b_\varepsilon(\omega)
=g_\varepsilon(1-\cos\omega)-2s_\varepsilon\sin\omega.
\]

This notation is private to the audit; it is not the paper's kernel \(\mathsf b\). Using the mixed-symbol identity,

\[
b_\varepsilon=-\mathfrak c_\varepsilon\,\xi\mathsf M_{r_\varepsilon}.
\]

Therefore (M) gives the uniform limit

\[
\frac{b_\varepsilon(\omega)}{\varepsilon}
\longrightarrow
b_0^\dagger(\omega):=-\xi\left(3-\frac74\xi\right)<0
\qquad(\omega\in B).
\tag{D}
\]

The sign is uniformly strict. From (B),

\[
3-\frac74\xi>
\frac{10-7\sqrt2}{8}>0,
\]

and \(\xi>1\). Thus \(b_0^\dagger\) is bounded above by a negative constant throughout the compact band.

The original smooth spectrum can nevertheless be feasible: the choice of negative \(C\) supplies the lower lag-one correction, and the continuous frequency spread suppresses later returns. The negative value in (D) alone is not a contradiction to the original lemma.

### 4. Every fixed midpoint grid has a late common return

Take any fixed finite uniform midpoint partition with \(2J\) cells as in the new passage, sufficiently fine that its total weight is nonzero. Its midpoints are

\[
a_j=-1+\frac{j-\frac12}{J}
=\frac{2j-1-2J}{2J},
\qquad j=1,\ldots,2J.
\]

The transported frequencies are

\[
\omega_j
=\frac{2\pi}3+\frac{2\pi}{3q}a_j
=\frac{2\pi}{6qJ}\bigl(2qJ+2j-1-2J\bigr).
\]

Hence every nonzero-weight atom has common period

\[
P=6qJ,\qquad e^{iP\omega_j}=1.
\]

No minimal-period assertion is needed. Set

\[
n=P-1\ge2.
\]

Then at every selected atom

\[
\cos(n\omega_j)=\cos\omega_j,\qquad
\sin(n\omega_j)=-\sin\omega_j.
\tag{R}
\]

The prescribed normalized weights are

\[
\nu_{\varepsilon,j}
=\frac{\mathsf k(a_j)/R_\varepsilon(\omega_j)}
{\sum_\ell\mathsf k(a_\ell)/R_\varepsilon(\omega_\ell)}.
\]

They are well-defined for a sufficiently fine grid, nonnegative, and sum to one. Zero weights are discarded. Since \(R_0>0\) on \(B\), the weights have limits
\(\nu_{0,j}\), with the same nonzero support. Put

\[
G_{\varepsilon,J}=\sum_j\nu_{\varepsilon,j}g_\varepsilon(\omega_j),
\qquad
B_{\varepsilon,J}=\sum_j\nu_{\varepsilon,j}b_\varepsilon(\omega_j).
\]

Then

\[
G_{\varepsilon,J}\to G_{0,J}>0,\qquad
\frac{B_{\varepsilon,J}}{\varepsilon}\to
B_{0,J}^\dagger
:=\sum_j\nu_{0,j}b_0^\dagger(\omega_j)<0.
\tag{L}
\]

The strict negative bound in (D) means the last sign holds for every such grid and every set of nonnegative normalized weights on it, not for a special numerical choice of the kernel.

### 5. The selected pair violates its upper lag

For the selected

\[
C_\varepsilon'=-(1-\eta)G_{\varepsilon,J}
=-\frac{35}{36}G_{\varepsilon,J},
\]

the upper lag \(n=P-1\), using (R), is exactly

\[
\upsilon_n
=B_{\varepsilon,J}
+G_{\varepsilon,J}(\cosh(nt_\varepsilon)-1)
+\frac{35}{36}G_{\varepsilon,J}\sinh(nt_\varepsilon).
\]

For this fixed grid, \(n\) is fixed as \(\varepsilon\to0\). Since
\(t_\varepsilon/\varepsilon\to-9/8\), (L) gives

\[
\frac{\upsilon_n}{\varepsilon}
\longrightarrow
B_{0,J}^\dagger-\frac{35}{32}nG_{0,J}<0.
\]

Thus the actual selected pair in the modified proof has a negative upper lag for every sufficiently small positive \(\varepsilon\).

Its minimizer slack remains strictly positive:

\[
G_{\varepsilon,J}-|C_\varepsilon'|
=\frac1{36}G_{\varepsilon,J}>0.
\]

Its lower lag-one slack is also positive for small \(\varepsilon\). Indeed,

\[
\frac{\ell_1}{\varepsilon}
\longrightarrow
B_{0,J}^\dagger+\frac{35}{32}G_{0,J}>0.
\]

To see the latter inequality pointwise, on the band

\[
\frac{b_0^\dagger}{g_0}
=\frac{\frac74\xi-3}{2(2-\xi)}>-\frac58,
\]

because this ratio is increasing in \(\xi\) and \(\xi>1\). Therefore the lower-lag limit is at least
\((35/32-5/8)G_{0,J}=15G_{0,J}/32>0\).

This explicitly separates the locally correct checks from the failed late constraint.

### 6. Stronger conclusion: changing C cannot repair the fixed grid

Let \(C\) be any real number, allowed to depend arbitrarily on \(\varepsilon\). At the same grid and lag \(n=P-1\), the exact identities are

\[
\ell_1
=B_{\varepsilon,J}
+G_{\varepsilon,J}(\cosh t_\varepsilon-1)
+C\sinh t_\varepsilon,
\]

\[
\upsilon_n
=B_{\varepsilon,J}
+G_{\varepsilon,J}(\cosh(nt_\varepsilon)-1)
-C\sinh(nt_\varepsilon).
\]

Set

\[
A_\varepsilon=\frac{\sinh(nt_\varepsilon)}{\sinh t_\varepsilon}>0.
\]

The value constant cancels exactly:

\[
\begin{aligned}
A_\varepsilon\ell_1+\upsilon_n
={}&(A_\varepsilon+1)B_{\varepsilon,J}\\
&+G_{\varepsilon,J}
\left[A_\varepsilon(\cosh t_\varepsilon-1)
+\cosh(nt_\varepsilon)-1\right].
\end{aligned}
\tag{C}
\]

Since \(A_\varepsilon\to n\), the bracket is \(O(\varepsilon^2)\), and (L) gives

\[
\frac{A_\varepsilon\ell_1+\upsilon_n}{\varepsilon}
\longrightarrow(n+1)B_{0,J}^\dagger<0.
\]

For all sufficiently small \(\varepsilon>0\), the left side of (C) is negative. If both required slacks were nonnegative, their positive combination would be nonnegative. Therefore no \(C\), even one different from the proof's \(C_\varepsilon'\), makes this fixed-grid spectrum feasible.

This is an exact asymptotic counterfamily. The sign follows from a strictly negative limiting coefficient of explicit analytic expressions at positive \(\varepsilon\); no numerical approximation or unresolved convergence exchange is used. It applies to every fixed finite J. The threshold in epsilon is allowed to depend on J, which is exactly the dependence relevant to disproving one fixed grid across all sufficiently small epsilon.

### 7. Why this does not contradict the original finite-atom existence theorem

For each fixed \(\varepsilon>0\), the original proof may choose a new and sufficiently fine grid. Our disproof fixes J first and then makes \(\varepsilon\) smaller. The bad lag \(P-1=6qJ-1\) depends on that fixed grid.

Meanwhile

\[
n_2(t_\varepsilon,\eta)
=\left\lceil |t_\varepsilon|^{-1}\log288\right\rceil
\longrightarrow\infty.
\]

For sufficiently small \(\varepsilon\), the bad lag lies below the original tail cutoff. Thus it is one of the constraints the original proof would still have to preserve when selecting its quadrature. It was not automatically covered by the tail estimate.

For any prescribed finite collection of lags, a sufficiently fine midpoint quadrature can approximate the limiting smooth density on those test functions. The strict continuous-spectrum margins for upper lags and lower lags at least two persist for that finite collection; the lower lag-one condition is already checked uniformly over every measure on B. This does not prevent the chosen finite grid from having a later bad lag which moves as J changes.

The distinction is

\[
\forall\varepsilon\ \exists\text{ a sufficiently fine finite grid}
\]

versus the new construction's

\[
\exists\text{ one finite grid}\ \forall\text{ sufficiently small }\varepsilon.
\]

The first is true here. The second is false for the printed midpoint construction.

## Dimension, regularity, and startup audit

The quadrature weights have the correct normalization and the correct \(1/R\) factor. The map from \([-1,1]\) to B is affine; equal cell widths cancel in the normalized midpoint weights. No density or change-of-variables error is used.

Although the new partition has \(2J\) cells, the objective-space notation \(\mathbb C^J\oplus\mathbb R\) does not create a separate dimension defect. The fixed definition of \(\mathsf b_0\) makes it zero for \(|u|\ge1/4\). Therefore \(\mathsf b\) is supported in \([-1/4,1/4]\), and \(\mathsf k=\mathsf b*\mathsf b\) is actually supported in \([-1/2,1/2]\), a stronger fact than the loose support \([-1,1]\) stated later. Among the \(2J\) uniform midpoints, at most J lie in \((-1/2,1/2)\); endpoints have zero weight. Hence the number of nonzero atoms is at most J. If necessary, the startup construction in that smaller dimension can be embedded in \(\mathbb C^J\oplus\mathbb R\) by adding unused quadratic coordinates.

The family is D=2, all positive epsilon inputs have \(0<\mu<L\), and the relevant regularity class is the paper's \(C^{1,1}\) class. No additional \(C^2\) or \(C^\infty\) requirement is introduced. The band is fixed, remains inside \((0,\pi)\), and the phase has the required continuous branch. None of these side conditions fails.

The violated upper slack corresponds, by eq:slacks, to

\[
R_{j,j+n}-T_{j,j+n}
=\tfrac12 e^{(2j+n)t_\varepsilon}\upsilon_n<0.
\]

Thus the selected spectral value and gradient data fail a necessary interpolation inequality. The cited startup lemma cannot be invoked from its hypotheses for this pair.

One can also see the failure propagate through a legitimate choice in the printed startup construction. Choose its extra scalar curvature \(\lambda=1/2\). For TMM and sufficiently small epsilon, this is in \((\mu,L)\) and its scalar query recurrence is uniformly fast. At epsilon zero its characteristic polynomial is

\[
z^2-\tfrac12 z+\tfrac12,
\]

with simple complex roots of modulus \(1/\sqrt2\). Its queries from rest satisfy

\[
Q_k=2^{-k/2}
\left[\cos(k\vartheta)-\frac3{\sqrt7}\sin(k\vartheta)\right],
\qquad
\cos\vartheta=\frac1{2\sqrt2}.
\]

Here \(Q_1=-1/2\), and for \(k\ge2\),
\(|Q_k|\le(4/\sqrt7)2^{-k/2}\le2/\sqrt7<1\).
Continuity of the simple roots and coefficients gives, for small positive epsilon, a uniform bound
\(|Q_k|\le(8/5)(3/4)^k\) for \(k\ge2\), while \(Q_1\) remains near \(-1/2\). Thus \(Q_k\ne1\) for every \(k\ge1\), as required by that auxiliary choice.

For a fixed sufficiently small epsilon with \(\upsilon_n<0\), the bad wave slack at pairs \((j,j+n)\) is a negative constant times \(r_\varepsilon^{2j}\). The extra quadratic coordinate contributes a nonnegative \(R\) of order \(Y^2(3/4)^{2j}\) and contributes zero T. Since \(r_\varepsilon>3/4\), no finite Y can offset that negative wave contribution for all large j. Hence the prescribed data in this permitted implementation of the startup construction are not interpolable either.

The main disproof does not need this auxiliary observation: the exact cancellation (C) already proves that the spectral witness required by the invocation does not exist on the fixed grid. Nor is it claimed that no other objective, spectrum, or startup choice can realize the unchanged rate lower bound.

## Required G2 classification audit

### Established implication before the faulty witness selection

For a fixed admissible member \(\varepsilon\), the established half-step argument says:

\[
\mathsf P_\varepsilon
\Longrightarrow
\exists\,\mathcal Q_\varepsilon\
\mathsf F_\varepsilon(\mathcal Q_\varepsilon),
\]

where \(\mathsf P_\varepsilon\) comprises the band, phase, strict-margin, and lower lag-one hypotheses, and \(\mathcal Q_\varepsilon\) is a finite quadrature witness. Its contents include its resolution, nodes, normalized nonnegative weights, and associated \(C_\varepsilon\).

The predicate \(\mathsf F_\varepsilon\) specifies support on the band, strict minimizer slack, and every lower and upper lag inequality. In the original proof the existential quadrature is selected after the cutoff \(n_2(t_\varepsilon,\eta)\) and the finite strict margins are known.

The family application legitimately gives

\[
\forall\varepsilon\in(0,\varepsilon_0)\
\exists\mathcal Q_\varepsilon\
\mathsf F_\varepsilon(\mathcal Q_\varepsilon).
\]

The original proof of lem:spreadwit uses exactly that implication. Its statement explicitly allows \(J_\varepsilon\).

### Existential variables and specified witness properties

The existential variables are the finite partition resolution and the corresponding finite measure, together with the value constant. For the selected midpoint implementation the weights and C are subsequently determined by the nodes, the member's R, and eta.

The witness is guaranteed to work at the selected epsilon and to resolve the finite family of test functions with \(n<n_2(t_\varepsilon,\eta)\). There is no guarantee that its resolution is independent of epsilon, or that a partition chosen for one cutoff resolves a larger cutoff.

The smooth kernel, the rational band in the counterexample, c, and eta are fixed parameters. The objective and initialization produced afterward may still depend on epsilon; the new defect does not incorrectly require a common objective across the family.

### Desired conclusion and additional property silently used

The desired existing conclusion is a finite-dimensional from-rest realization for every sufficiently small epsilon, with the norm bound at every iteration horizon.

The new construction fixes one partition, then forms its transported measures \(\nu_{\varepsilon,J}\). To invoke lem:startup as printed, it needs

\[
\exists J<\infty\ \exists\varepsilon_0>0\
\forall\varepsilon\in(0,\varepsilon_0):
\mathsf F_\varepsilon(\mathcal Q_{\varepsilon,J}).
\tag{U}
\]

This is an extra property of the existential quadrature witness: one resolution must suffice as the exponent tends to zero. It is neither stated nor proved in the cited finite-atom step.

The exact counterexample establishes the negation relevant to this construction:

\[
\forall J<\infty\
\exists\varepsilon_J>0\
\forall\varepsilon\in(0,\varepsilon_J)\
\forall C\in\mathbb R:
(\nu_{\varepsilon,J},C)\text{ is infeasible}.
\]

Thus no choice of a finer fixed partition, and no choice of C on that partition, supplies (U).

### Is the conclusion independent of the witness?

The abstract lemma conclusion is existential and remains true with a member-dependent quadrature.

The actual proof conclusion is not independent of the selected witness. The prescribed wave frequencies and normalized values are defined using the fixed midpoint partition; the startup objective is then supposed to interpolate those particular query data. Its all-horizon trajectory claim therefore depends on the grid through the complete infinite family of lag constraints.

The notation keeps the weights and C member-dependent, which makes the construction look adaptive. However, the number and relative positions of the quadrature nodes have already been fixed. The lost dependence is precisely that of the partition resolution, not that of the weights, the density, or the later objective.

### Why G2, rather than another primary category

G2 is primary because the proof reuses an existential witness outside the parameter scope for which its properties were supplied. The correct order is to choose epsilon, determine the finite lag problem, then choose its quadrature. The modified order chooses the quadrature resolution first and expects its feasibility to survive every smaller member.

G1 is a related interpretation: convergence on each fixed finite family of test functions is being used for an expanding family. But the operative edit is the construction and reuse of a finite witness, so G2 more precisely describes the error.

MP describes only the final visible symptom: lem:startup is invoked without a feasible input pair. The referenced lemmas are themselves correctly stated and their legitimate local hypotheses have been checked. The substantive source of the missing antecedent is the changed quantifier and dependency order in the quadrature selection, not a mistaken formula for a theorem's conclusion.

DEF is not primary. The partition, transported nodes, weights, value constant, and dimensions are well-defined. Their existence and normalization are not the issue.

CONV is not primary. The density factor \(1/R\), signs, hyperbolic terms, affine coordinate map, and exact C-cancellation are correct. The original cutoff is also left unchanged. The failure remains for arbitrarily fine fixed grids, so no fixed numerical adjustment to a mesh constant repairs it.

Exactly one primary category, G2, is recorded. No secondary category is recorded.

## Subtlety and downstream significance

The preceding local checks remain valid on the counterexample: the tuning is stable, the band is allowed, the phase defect tends to zero, the smooth spectrum has strict margins, the chosen finite weights are correct, the minimizer slack is strict, and the lower lag-one check succeeds. The false condition is an upper constraint at a grid-dependent later return.

The proof does not explicitly announce a false universal generalization. It changes the stage at which the quadrature is fixed and immediately continues the existing witness construction. The reader must recover the hidden dependence from the finite-atom proof, where the cutoff diverges as the exponent approaches zero.

This is load-bearing in the proof as written. The selected pair supplies the wave component of the proposed objective and initialization; it is not an unrelated stronger assertion appended to an otherwise unchanged argument. The continuous-spectrum part still works, and the original theorem is repaired by allowing the grid to be chosen separately for each epsilon, exactly as its original proof did.

The wall-layer, corner, and arbitrary-rate optimality arguments rely on lem:spreadwit for finite from-rest witnesses. Their statements are not claimed false here; their use of the modified witness proof inherits this unsupported construction.

A careful reviewer can detect the issue by following “Fix a partition” through “For each epsilon” and comparing that order with the earlier \(n_2(t,\eta)\) choice. To establish that it is more than missing exposition, the reviewer can inspect rational midpoint frequencies and combine the two lag constraints at 1 and P-1 as in (C). The exact counterexample rules out every fixed J, so the printed construction cannot be repaired merely by saying the grid was chosen sufficiently fine.

No independent checker or blind reviewer result for attempt06 is available to this tricker. This log does not claim that the candidate will evade detection or that its preferred classification has already been accepted.
