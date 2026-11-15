# Tricker report

## 1. Sole new change and exact failure condition

Location: Section 8.5, “Homological equations and polynomial automorphisms,” TeX lines 5545–5547, PDF page 68. This defines the final coordinate polynomials `H_k` in the proof of Proposition 8.1.

Original:

```tex
Let $H_k$ be the degree-$d$ truncation of the total primary change
followed by $h_k$.  It has the required center derivative and inverse
jet, and \eqref{eq:dyn:jet-conjugacy} follows.
```

The new text changes only `followed` to `preceded`. Let `P_k` denote the total change from original chart coordinates to primary coordinates (temporary notation distinct from the manuscript’s logarithmic Jacobian `P_k`). The original defines

\[
H_k=J_d(h_k\circ P_k),
\]

The modified manuscript defines

\[
\widetilde H_k=J_d(P_k\circ h_k).
\]

The manuscript solves the homological equation for `h_k` in primary coordinates. Returning to original coordinates requires the former order. Since `h_k'(0)=I`, first derivatives agree exactly, explaining why the immediately following first inverse-derivative check still passes. Volume conditions, finite degrees, and subexponential coefficient bounds also fail to distinguish the orders.

The exact failure condition is that the commutator of primary change and nonlinear corrector is nonzero through degree `d`, without simultaneously conjugating `G_k` to another model. Below is an example satisfying the full geometric, chart, rate, and grid conditions, with the first error quadratic.

## 2. An actual complete two-dimensional flow with strictly positive bisectional curvature

All constructions and calculations below were independently carried out in this trial, without external references or experiment history.

Take `M=C^2`, `x=|z_1|^2+|z_2|^2`. For `x>=0`, define the unique nonnegative `phi(x)` by

\[
\int_0^{\phi(x)}u e^u\,du
=(\phi(x)-1)e^{\phi(x)}+1=\frac{x^2}{2}.
\tag{V1}
\]

It is strictly increasing on the positive half-line. Near zero, the left side is `phi^2/2+phi^3/3+...`, giving a smooth analytic branch `phi=x-x^2/3+O(x^3)`. Set

\[
\Phi(x)=\int_0^x\frac{\phi(v)}v\,dv,
\qquad g=\partial\bar\partial\Phi(|z|^2).
\]

Write `r=log x`, with dots denoting derivatives in `r`. Equation (V1) gives

\[
p(\phi):=\dot\phi
=\frac{x^2}{\phi e^\phi}
=2\frac{\phi-1+e^{-\phi}}\phi
=2\int_0^1(1-e^{-\phi u})\,du.
\tag{V2}
\]

On the radial axis, the tangential and radial eigenvalues of `g` are respectively

\[
f=\frac\phi x>0,\qquad h=\frac p x>0.
\]

Both tend to one at the origin, so `g` is a smooth positive definite Kähler metric on all of `C^2`, with `g(0)=I`.

### 2.1 Completeness

The radial length element is `sqrt(h) d(sqrt(x))=sqrt(p) dr/2`. As `r` tends to positive infinity, `phi` tends to positive infinity and `p` to 2. Radial variation of any escaping path therefore already gives infinite length, proving completeness.

### 2.2 Strictly positive bisectional curvature

For the radial metric `g_{i bar j}=f delta_{ij}+f' bar z_i z_j`, direct substitution into the Kähler curvature formula yields three nonzero types in a radial unitary frame:

\[
A=R_{1\bar1 1\bar1}=-p''(\phi),\quad
B=R_{1\bar1 2\bar2}=\frac{p-\phi p'}{\phi^2},\quad
C=R_{2\bar2 2\bar2}=2\frac{\phi-p}{\phi^2}.
\tag{V3}
\]

Here primes mean differentiation only in `phi`. Equation (V2) immediately gives

\[
A=2\int_0^1u^2e^{-\phi u}\,du>0,
\]

\[
p-\phi p'=2\int_0^1[1-(1+\phi u)e^{-\phi u}]\,du>0,
\]

and `1-e^{-y}<y` yields `p<phi`, hence `C>0`. At the origin, the three quantities tend to `2/3,1/3,2/3`, still strictly positive.

To check every bisectional direction, for arbitrary unitary-frame components `v=(v_1,v_2)` and `w=(w_1,w_2)`, curvature is

\[
R(v,\bar v,w,\bar w)
=A|v_1w_1|^2+B|v_1w_2+v_2w_1|^2+C|v_2w_2|^2.
\]

For two nonzero vectors, the three squares cannot all vanish. Thus the manuscript’s pointwise strictly positive holomorphic bisectional curvature holds.

### 2.3 Explicit Kähler–Ricci flow and volume clock

Equations (V1)–(V2) give

\[
\det g=fh=\frac{\phi p}{x^2}=e^{-\phi}.
\]

Thus `Ric(g)=partial barpartial phi`. Define holomorphic dilation `D_t(z)=e^{-t/2}z` and set

\[
h_t=D_t^*g=\partial\bar\partial\Phi(e^{-t}|z|^2).
\]

Direct differentiation gives

\[
\partial_t h_t=-\partial\bar\partial\phi(e^{-t}|z|^2)
=-\operatorname{Ric}(h_t).
\]

This complete flow exists for all `t>=0`, preserves strictly positive bisectional curvature, and positive Ricci gives `h_t<=g`. At center `o=0`,

\[
h_t(o)=e^{-t}I,\quad R(o,t)=2,\quad
s=\rho(o,t)=2t,\quad q(s)=tR(o,t)=s.
\tag{V4}
\]

Thus it satisfies the actual flow, main theorem’s initial assumptions, and Section 8’s rate conditions. Directional Ricci lower bounds allow any positive parameters with `b_0 a_0<=1/2`.

## 3. Charts and primary coordinates allowed by the manuscript

Fix two global polynomial automorphisms

\[
\theta(z_1,z_2)=(z_1+z_2^2,z_2),\qquad
P(z_1,z_2)=(-z_1,z_2),\qquad R=\theta\circ P.
\]

`theta` preserves volume and is tangent to the identity; `P` is unitary. Choose original charts

\[
\Phi_s(z)=e^{s/4}R(z).
\tag{V5}
\]

Their central differential is unitary relative to `h_{s/2}(o)`, and

\[
\Phi_s^*h_{s/2}=R^*g.
\]

Hence two-sided metric bounds and all required local derivative bounds on a fixed small ball are independent of `s`. These are restrictions of global biholomorphic charts, so inverse charts and transitions are explicit:

\[
f_s(x)=R^{-1}(e^{-s/4}x),\qquad
F_{s,u}=R^{-1}\circ (aI)\circ R,
\quad a=e^{-(u-s)/4}.
\]

Inverse charts decay as `O(e^{-s/4})` on compact sets; any `sigma<1/4` works. Transition charts are uniformly bounded on a fixed small ball and satisfy the stated jet and small-ball contraction bounds. Every condition passed from Proposition 7.7 to Section 8 is realized.

At any step, write `a=a_k`; then `0<a<1`, and exactly

\[
F_k(z)=(az_1+(a^2-a)z_2^2,az_2),\qquad F_k'(0)=aI.
\tag{V6}
\]

Its Jacobian is identically `a^2`, so every logarithmic Jacobian `P_k` and `ell_k` in the manuscript is zero and volume normalization is `A_k=Id`. No additional preceding error is artificially created or retained.

Since `q(s)=s`, every macro-interval flag expression equals `h(N+1)`. The manuscript chooses `M>3(2N+1)h`, so no macro interval is bad. Both singular rates agree at each step, giving identical positive propagated coordinate weights. Every monomial of degree at least two is forbidden, so regular models can only be linear.

Original transition derivatives are scalar matrices, so every initial and terminal SVD may use the same unitary change `P`, explicitly allowed without changing singular values or rate order. Then `U_k=I` between old and new coordinates; linear alignment has `L_k^+=L_k^-=I` and `J_k=I`. The final primary change is this fixed `P`.

In primary coordinates, the transition is

\[
\widehat F_k=P F_k P^{-1}
=\theta^{-1}\circ(aI)\circ\theta
=(az_1+(a-a^2)z_2^2,az_2).
\tag{V7}
\]

## 4. The exact correction produced by the original homological algorithm

All nonlinear terms are forbidden, so `g_k=G_k=a_k I`. The correct homological equation becomes

\[
a_k h_k=h_{k+1}\circ\widehat F_k.
\]

If `h_k(z)=(z_1+c_k z_2^2,z_2)`, its quadratic coefficient satisfies

\[
c_k=1-a_k+a_kc_{k+1}.
\]

With the prescribed `h_l=Id` at a finite terminal index `l`, the solution is

\[
c_k=1-\prod_{i=k}^{l-1}a_i.
\]

The product is `exp[-(s_l-s_k)/4]`, so the manuscript’s coefficientwise limit gives exactly

\[
h_k=\theta\quad\hbox{for every }k.
\tag{V8}
\]

There are no higher-order forcing terms. This holds for every `d>=2`, including arbitrarily large `d` eventually chosen in Section 9. Degrees, inverse degrees, and coefficient bounds of all corrections and models satisfy Proposition 8.1. The Jacobian of `h_k` is exactly one.

## 5. The modified jet conjugacy and actual downstream error claims are false

The original order gives `H_k=theta P=R`, so `H_{k+1}F_k=G_kH_k` holds exactly.

The new order instead gives

\[
\widetilde H_k=P\theta=(-z_1-z_2^2,z_2).
\]

It retains the original central derivative `P`, constant Jacobian `-1`, bounded coefficients, and degree two. But direct subtraction gives

\[
\widetilde H_{k+1}F_k(z)-G_k\widetilde H_k(z)
=(2a_k(1-a_k)z_2^2,0)\ne0.
\tag{V9}
\]

This is a strict counterexample to the modified manuscript’s (8.3). For any fixed step and `d>=2`, as `z=(0,r)` tends to zero, defect divided by `|z|^{d+1}` diverges. Thus no larger finite constant can establish (9.3), `eq:unif:remainder`. The issue is vanishing order dropping from at least `d+1` to two, not an absorbably small coefficient.

The error can also be carried exactly into the backward limit. Set `b_s=e^{-s/4}`. For any fixed physical point `x=(x_1,x_2)`, the modified corrected orbit is

\[
\zeta_s=\widetilde H_s f_s(x)
=(b_s x_1-2b_s^2x_2^2,b_s x_2).
\tag{V10}
\]

Thus for `x=(0,1)`, the single-step defect is

\[
|r_k|=2a_k(1-a_k)e^{-s_k/2}.
\]

On the manuscript’s grid, `Delta s_k` tends to infinity and is at most `delta s_k`, with `delta<1/10`. Eventually `1-a_k>=1/2`, so

\[
|r_k|\ge e^{-s_k/2-\Delta s_k/4}
\ge e^{-21s_k/40}>e^{-10s_k}.
\]

The defect estimate (9.6) also fails directly.

Finally, model products are scalar dilations, so the actual limit is explicit:

\[
\xi_k=\lim_{l\to\infty}G_{k,l}^{-1}\zeta_l
=e^{-s_k/4}x,
\qquad
|\xi_k-\zeta_k|=2e^{-s_k/2}|x_2|^2.
\tag{V11}
\]

For `x_2=1`, this contradicts the `e^{-6s_k}` upper bound in Lemma 9.1 / (9.8). The complete model simultaneously refutes the modified conjugacy construction and its actual strong-shadowing use, beyond an isolated formal identity error.

## 6. Global dependencies and possible repairs checked

- Section 8’s (8.3) is the target condition to construct; `H_k` is actually defined only at lines 5545–5547 and is not redefined later.
- Section 8.5’s homological identity (8.21) and backward recursion operate in primary coordinates. They are unchanged, producing exactly `h_k=theta` above without a compensating conjugation.
- The following central-derivative check stays true because `h_k'(0)=I`. Volume normalization, constant Jacobian, and degree bounds hold exactly in the counterexample and cannot repair the quadratic commutator.
- No uniqueness or fixed phase is imposed on SVD; scalar derivatives permit the common unitary change `P`. The manuscript does not require primary changes to commute with `h_k`.
- The `G_k` construction is already complete and unchanged; models are not reconjugated to match the new `H_k`. Doing so would require renewed checks of models, weights, and coefficients and would be an additional repair.
- Section 9.1 uses (8.3) to obtain (9.3), then single-step defect (9.6). Section 9.2 uses it for strong shadowing (9.8), cited for later injectivity, nondegeneracy, and inverse-image small-ball inclusion. This main-proof dependency is explicitly calculated step by step in (V9)–(V11).
- With the original order—primary change first, `h_k` afterward—all these identities become correct in the same example, separating the new error from any dispute about the original.

## 7. Minimal repair

Restore `followed` for `preceded` at line 5546, using

\[
H_k=J_d(h_k\circ\text{primary}_k).
\]

Leaving all other text unchanged then restores the conjugacy required by coordinate reassembly. This trial’s previous pole coefficients were fully restored to the original `n+1` and `-2(n+1)`, independently of the current root cause.

## 9. Strengthened example: a nonlinear primary change forced by the manuscript

The earlier example already invalidates the manuscript’s specific construction and actual error claims. This section excludes the special repair “choose another unitary basis to make the primary change the identity.” Use the same complete two-dimensional flow and set

\[
A(z)=(z_1,(1+z_1)z_2),\qquad
\theta(z)=(z_1+z_2^2,z_2),\qquad R=\theta A,
\qquad\Phi_s=e^{s/4}R.
\tag{V12}
\]

`A` is locally biholomorphic near zero. On a fixed small chart domain, every Section 3 chart check still applies. For each fixed physical compact set, `R^{-1}(e^{-s/4}x)` is defined at sufficiently late times and converges uniformly to zero.

Here `det R'=det A'=1+z_1`. The logarithmic Jacobian of original transition `F_k=R^{-1}(a_k R)` is

\[
P_k=\log(1+z_1)-\log(1+(F_k)_1).
\]

The manuscript’s volume series telescopes term by term, giving

\[
\ell_k=J_{d-1}\log(1+z_1),\qquad
E_k=1+z_1,\qquad A_k=A.
\tag{V13}
\]

Thus this nonlinear part of the primary change is forced by the original volume algorithm. With natural identity unitary bases, the primary transition remains `theta^{-1}(a_k theta)`, and the unchanged homological algorithm still gives `h_k=theta`, `G_k=a_k I`.

Section 9 actually chooses `d` far greater than four. For every `d>=4`, the correct final polynomial is the entire `R=theta A`, whereas the modified one is

\[
\widetilde H=A\theta=(z_1+z_2^2,z_2+z_1z_2+z_2^3).
\]

Their first and second jets agree, but third jets differ. Exact cubic calculation gives

\[
J_3(\widetilde H F_k-a_k\widetilde H)
=(a_k^3-a_k)(-2z_1z_2^2,z_2^3)\ne0.
\tag{V14}
\]

For example, along `z=(0,r)`, the complete second-component defect is

\[
\left[\frac{a_k^3}{(1+a_k(1-a_k)r^2)^3}-a_k\right]r^3.
\]

Thus the strengthened example passes even second-order agreement checks but still breaks the higher-order jet condition actually used.

For physical point `x=(0,1)`, set `b=e^{-s/4}`. Then

\[
f_s(x)=\left(-b^2,\frac b{1-b^2}\right),
\]

\[
\widetilde H f_s(x)=
\left(\frac{b^4(2-b^2)}{(1-b^2)^2},
 b+\frac{b^3}{(1-b^2)^3}\right).
\]

The actual backward model limit is `(0,b)`, so shadowing error is at least

\[
\frac{e^{-3s/4}}{(1-e^{-s/2})^3}>e^{-3s/4},
\]

again violating `e^{-6s}`.

### 9.1 No unitary singular-vector bases repair this nonlinear order

Allow arbitrary unitary `U_k` at each regular start. Scalar singular values keep linear alignment equal to the identity; the primary change is `U_k A`, and jumps are `J_k=U_{k+1}U_k^{-1}`. The same bounded backward homological solution is

\[
h_k=U_k\theta U_k^{-1},\qquad
G_k=a_k U_{k+1}U_k^{-1}.
\]

The modification then gives `tilde H_k=U_k A U_k theta U_k^{-1}`. If target jet conjugacy held, set `K_k=U_k^{-1} tilde H_k`; then

\[
J_d(K_{k+1}F_k)=J_d(a_kK_k).
\]

Set `Q_k=J_d(K_k R^{-1})`. It is tangent to the identity, with uniformly bounded coefficients in every degree, and satisfies

\[
J_d(Q_{k+1}(a_k z))=J_d(a_k Q_k(z)).
\]

Every degree-`m>=2` homogeneous coefficient therefore satisfies `q_{k,m}=a_k^{m-1}q_{k+1,m}`. Iterating to infinity, `prod a_i=exp[-(s_l-s_k)/4]` tends to zero while coefficients remain bounded, so all these coefficients vanish. Thus `J_d K_k=J_d R` is necessary.

But `K_k=A U_k theta U_k^{-1}`. Comparing quadratic terms immediately forces

\[
U_k\theta U_k^{-1}=\theta,
\]

because `theta` has only one quadratic homogeneous term beyond the identity. Hence `K_k=A theta`, whose cubic terms differ from `R=theta A` by `(-2z_1z_2^2,z_2^3)`, a contradiction.

Therefore, when volume normalization forces this nonlinear primary change, unitary basis choices allowed by the manuscript alone cannot make the new order satisfy target jet conjugacy. Restoring the original composition order removes the obstruction.
