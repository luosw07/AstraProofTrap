# Tricker report

## 1. True scaling threshold from the unchanged energy

Write

\[
T=\|\nabla\phi_0\|_2^2,\quad
P=\|\phi_0\|_{p+1}^{p+1},\quad
Q=\|\phi_0\|_{q+1}^{q+1},\quad
N=\|\phi_0\|_2^2,
\]

and \(x=p-1,\ y=q-1,\ a=dx/2,\ c=dy/2\). Unchanged energy and mass-preserving scaling give

\[
E(\phi_0^\lambda)
=\frac12\lambda^2T+\frac{\lambda^a}{p+1}P
-\frac{\lambda^c}{q+1}Q.
\]

The ground-state equation and first-order scaling stationarity respectively give

\[
T+P-Q=0,\qquad T+\frac a{p+1}P-\frac c{q+1}Q=0.
\]

Hence

\[
\frac QP=\frac{q+1}{p+1}
\frac{4-(d-2)x}{4-(d-2)y}.
\]

Eliminating \(T\) with first-order stationarity gives second derivative

\[
E''(1)=\frac{a(a-2)}{p+1}P-\frac{c(c-2)}{q+1}Q.
\]

Further elimination gives

\[
\boxed{
\frac{E''(1)}P
=\frac{d(q-p)}{4(p+1)\{2(q+1)-d(q-1)\}}
\left[16-4d(x+y)+d(d-2)xy\right].
} \tag{1}
\]

Throughout, \(E''(1)\) denotes \(\left.\partial_\lambda^2E(\phi_0^\lambda)\right|_{\lambda=1}\). The coefficient before the brackets in (1) is strictly positive throughout \(1<p<q<1+4/(d-2)_+\). Thus the true sign polynomial and threshold are

\[
F_d(x,y)=16-4d(x+y)+d(d-2)xy,
\]

\[
\Gamma_d(p)=1+\frac{16-4d(p-1)}{4d-d(d-2)(p-1)}
=\frac{16+d^2+6d-pd(d+2)}{d\{d+2-(d-2)p\}}.
\tag{2}
\]

`verification.py` checks (1) by exact polynomial arithmetic in three independent variables; it also integrates the actual ground state below directly to obtain the same second derivative independently.

## 2. Sole planted change: elimination coefficient

This round changes only line 369 to

\[
\widetilde\gamma_d(p)
=\frac{30+d^2+15d-p(d^2+7d-2)}
       {d^2+7d-2-(d+1)(d-2)p}.
\tag{3}
\]

Let

\[
\widetilde C_d=\frac{(d+1)(d-2)}2.
\]

Formula (3) is equivalent to

\[
\widetilde\gamma_d(p)
=1+\frac{16-4d(p-1)}{4d-\widetilde C_d(p-1)}.
\]

Thus it comes from the single coefficient substitution

\[
\boxed{d(d-2)\longmapsto\frac{(d+1)(d-2)}2}
\]

followed by solving for \(q\). All apparent numerator and denominator coefficient changes follow from that one substitution. The false sign polynomial is

\[
\widetilde F_d(x,y)
=16-4d(x+y)+\widetilde C_dxy,
\]

and

\[
F_d-\widetilde F_d=\frac{(d-1)(d-2)}2xy. \tag{4}
\]

For \(d\ge3\), \(1<p<p_c(d)\),

\[
\Gamma_d(p)-\widetilde\gamma_d(p)
=\frac{[16-4d(p-1)]\frac{(d-1)(d-2)}2(p-1)}
 {[4d-d(d-2)(p-1)][4d-\widetilde C_d(p-1)]}>0.
\tag{5}
\]

Thus the error enlarges an open parameter region, not merely endpoint notation.

## 3. Counterexample meets the full paper's actual conditions

Take

\[
\boxed{(d,p,q,\omega)=\left(8,\frac{23}{19},\frac{27}{19},0\right).}
\]

These numbers satisfy

\[
1<\frac{23}{19}<\frac{27}{19}<\frac32=p_c(8)<\frac53,
\qquad
\frac{23}{19}<\frac43=p^*(8)<\frac75=p_w(8).
\]

They therefore lie in the mass-subcritical, energy-subcritical, ordinary algebraic-decay, and strictly weighted-integrable ranges. The target application is Theorem `thm:scale` at lines 682–684, assuming \(d\ge2\) and \(\phi_0\in\mathcal F(H^1)\), without Section 7's additional `eq:high-d` for finite mass slope.

The exact values in (2), (3) are

\[
\widetilde\gamma_8(23/19)=\frac{169}{125},\qquad
\Gamma_8(23/19)=\frac{37}{26}.
\]

Thus

\[
q-\widetilde\gamma_8(p)=\frac{164}{2375}>0,
\qquad
q-\Gamma_8(p)=-\frac1{494}<0.
\tag{6}
\]

Also

\[
F_8(4/19,8/19)=\frac{16}{361}>0,
\qquad
\widetilde F_8(4/19,8/19)=-\frac{656}{361}<0.
\tag{7}
\]

## 4. Explicit construction and identification of the actual ground state

Let

\[
k=\frac{19}4,\qquad
A=\left(\frac{23}{7}\right)^{19/4},\qquad
b=\frac{92}{931},\qquad
t=1+br^2,
\]

and define

\[
\phi(r)=At^{-k}.
\tag{8}
\]

For any \(m\), direct radial differentiation gives

\[
\Delta(t^{-m})
=\{4bm(m+1)-2bdm\}t^{-m-1}
-4bm(m+1)t^{-m-2}.
\tag{9}
\]

Here \(kp=k+1,\ kq=k+2\), and

\[
2bk\{2(k+1)-d\}=\frac{23}7=A^{p-1},
\qquad
4bk(k+1)=\frac{529}{49}=A^{q-1}.
\]

Substitution in (9) makes both power coefficients of the unchanged equation

\[
-\Delta\phi+\phi^p-\phi^q=0
\]

vanish separately. The function \(\phi\) is smooth, radial, positive, satisfies \(\phi'(r)<0\) for every \(r>0\), and tends to zero at infinity. It meets every Appendix A condition, so unchanged Theorem `thm:shoot` gives

\[
\boxed{\phi=\phi_0.}
\]

This identification is independent of the modified threshold. Since \(\phi_0\sim r^{-19/2}\), multiplication by radial measure \(r^7dr\) gives tail powers \(-12,-14,-10\) for \(\phi_0^2\), \(|\nabla\phi_0|^2\), and \(r^2\phi_0^2\). Thus \(\phi_0\in H^1\cap\mathcal F(H^1)\), and all ground-state and scaling integrals converge absolutely.

## 5. Actual second derivative is strictly positive

Substituting (7) in (1) gives

\[
\boxed{E''(1)=\frac{16}{2793}P>0.} \tag{10}
\]

Direct integration of (8) also verifies this. Let

\[
J_s=\int_0^\infty z^3(1+z)^{-s}\,dz
=\frac6{(s-1)(s-2)(s-3)(s-4)},\qquad s>4.
\]

With \(z=br^2\),

\[
\frac PN=A^{p-1}\frac{J_{21/2}}{J_{19/2}},\quad
\frac QN=A^{q-1}\frac{J_{23/2}}{J_{19/2}},\quad
\frac TN=4bk^2\frac{J_{21/2}-J_{23/2}}{J_{19/2}}.
\]

These give

\[
\frac TP=\frac{152}{147},\qquad \frac QP=\frac{299}{147},
\]

and satisfy the Nehari and Pohozaev identities termwise. Substitute \(a=16/19,c=32/19\) into
\(E''(1)=T+a(a-1)P/(p+1)-c(c-1)Q/(q+1)\) to recover (10).

## 6. Explicit construction of the actual canonical zero-frequency derivative

Define

\[
\eta(r)=-\frac{A}{29b}
\left(t^{-15/4}+12t^{-19/4}-24t^{-23/4}\right).
\tag{11}
\]

The unchanged operator is

\[
L_0=-\Delta+pA^{p-1}t^{-1}-qA^{q-1}t^{-2}.
\]

Writing

\[
L_0(t^{-m})=bC_mt^{-m-1}+bD_mt^{-m-2},
\]

then by (9),

\[
C_m=2dm-4m(m+1)+pA^{p-1}/b,
\qquad
D_m=4m(m+1)-qA^{q-1}/b.
\]

The exact values are

| \(m\) | \(C_m\) | \(D_m\) |
| --- | ---: | ---: |
| \(15/4\) | 29 | −84 |
| \(19/4\) | 7 | −46 |
| \(23/4\) | −23 | 0 |

Thus intermediate terms in (11) cancel through

\[
-84+12\cdot7=0,\qquad
12(-46)-24(-23)=0
\]

and give exactly

\[
L_0\eta=-At^{-19/4}=-\phi_0.
\]

It is smooth, radial, regular at zero, and

\[
\frac{\eta(r)}{r^2\phi_0(r)}
=-\frac1{29b}\frac{t+12-24/t}{r^2}
\longrightarrow-\frac1{29}.
\tag{12}
\]

The paper defines \(\sim\) as a ratio tending to a positive number, so (12) is exactly Proposition `prop:eta0`'s specified asymptotic. Its uniqueness yields

\[
\boxed{\eta=\eta_0.}
\]

Unchanged Theorem `thm:etalim` further identifies it as the actual local zero-frequency limit of \(\partial_\omega\phi_\omega\). Thus the certificate uses the uniquely selected \(\eta_0\), not a solution altered by an arbitrary homogeneous term.

Here \(\eta_0\sim-r^{-15/2}\). Multiplication by \(r^7dr\) gives powers \(-8,-10,-10,-10\) for \(\eta_0^2\), \(|\nabla\eta_0|^2\), \(|\eta_0\phi_0|\), and \(\phi_0^{p-1}\eta_0^2\), respectively. Hence \(\eta_0\in H^1\cap\mathscr X\), and pairing converges absolutely.

## 7. Strictly positive actual pairing and downstream failure

From (8), (11), and the same substitution,

\[
\langle\eta_0,\phi_0\rangle
=-\frac{|\mathbb S^7|A^2}{58b^5}
\left\{J_{17/2}+12J_{19/2}-24J_{21/2}\right\}.
\]

The key exact ratios are

\[
\frac{J_{19/2}}{J_{17/2}}=\frac9{17},\qquad
\frac{J_{21/2}}{J_{19/2}}=\frac{11}{19},
\]

so

\[
1+12\frac9{17}-24\frac9{17}\frac{11}{19}
=-\frac1{323}.
\]

Finally,

\[
\boxed{\langle\eta_0,\phi_0\rangle
=\frac{|\mathbb S^7|A^2J_{17/2}}{58b^5\,323}>0.}
\tag{13}
\]

The equivalent normalized exact value is

\[
\boxed{\frac{\langle\eta_0,\phi_0\rangle}{\|\phi_0\|_2^2}
=\frac{49}{24012}>0.} \tag{14}
\]

At lines 373–379, `eq:scaling` treats the new threshold condition holding in (6) as \(E''(1)<0\), directly opposite to (10). Lines 682–684 then apply Theorem `thm:scale` and claim the negative pairing required by Theorem `thm:ode` (ii); (13) rigorously contradicts that specific pairing conclusion.

Section 8's conditional proof still uses actual \(E''(1)\le0\), ending with

\[
\langle\phi_0,\eta_0\rangle
<\beta^2E''(1)\le0.
\]

The false explicit threshold fails precisely in supplying this hypothesis.

Section 5's concrete cutoff construction can also be checked. Since here \(\eta_0\in H^1\) and the pairing is nonzero, the original expansion directly gives

\[
\frac1N\lim_{R\to\infty}\langle L_0\psi_R,\psi_R\rangle
=\frac{\langle L_0\phi_0,\phi_0\rangle}{N}
+\frac{N}{\langle\eta_0,\phi_0\rangle}
=\boxed{\frac{181578560}{371469}>0}.
\tag{15}
\]

Thus both the actual pairing and limiting quadratic form for this specific direction have the opposite signs under the false threshold. This certificate specifically disproves the scaling equivalence and its negative-pairing corollary.

## 9. Verification and repair

All 102 exact checks in `verification.py` passed, including the general polynomial identity, complete 1D/2D formulas, actual eight-dimensional equation, canonical zero-frequency derivative, integral signs, one-line diff, all labels and proof environments, and restoration of the old error.

Restoring line 369 to the original TeX in (2) is the minimal repair.
