# Tricker report

## 1. Exact claim and failure location

The sole change is in §8.1, Lemma 8.2, “Realization of constant-volume jets” (`lem:volume-jets`), source lines **5154–5158**. At step m, the original algorithm takes the first homogeneous discrepancy between current model and target. The modified algorithm first takes the fixed target jet's formal logarithm

\[
X=\log T=\sum_{m=2}^dX_m,
\]

then retains the procedure at **5181–5188**: decompose each `X_m` into divergence-free shear fields by a fixed linear decomposition and compose their flows, claiming this “correct[s] degree m.”

The new paragraph correctly asserts existence, homogeneous decomposition, and zero divergence of the formal logarithm. The error is treating its fixed components as the actual residuals at each step. The exact constant-volume polynomial target below passes every check below degree four, but the procedure omits the required fourth-degree correction.

The lemma quantifies over **every invertible constant-volume d-jet fixing zero**, without mesh, bad-interval, or clock-growth restrictions. This certificate meets all those conditions. Sections 7–8 also supply a complete manifold of positive bisectional curvature allowed by the paper and a realization by actual normalized atlas transitions.

## 2. Input: an explicit volume-preserving polynomial automorphism

In complex dimension two define

\[
S_a(x,y)=(x+a y^2,y),\qquad
R_b(x,y)=(x,y+b x^3),
\]

and choose the target

\[
\mathcal T=S_{1/2}\circ R_1\circ S_{1/2}.
\tag{1}
\]

This is a specified input, not a change to any composition order in the paper. Every shear fixes the origin, has derivative I and Jacobian identically one, and has inverse `S_{-a}` or `R_{-b}`. Thus `T` is a global polynomial automorphism with derivative I and Jacobian **identically one to all orders**, with inverse

\[
\mathcal T^{-1}=S_{-1/2}\circ R_{-1}\circ S_{-1/2}.
\]

For every `d≥4`, `J_d T` meets all input conditions of the modified lemma. Put

\[
u=x+\tfrac12y^2,\qquad v=y+u^3.
\]

The full exact formula is

\[
\mathcal T(x,y)=(u+\tfrac12v^2,v).
\tag{2}
\]

Its total degree is 12, and its fourth jet is

\[
\boxed{
J_4\mathcal T=
\left(x+y^2+x^3y,\quad
y+x^3+\tfrac32x^2y^2\right).}
\tag{3}
\]

Throughout, `O_j` denotes terms of total degree at least j.

## 3. All local formal-logarithm claims in the replacement are valid

Define the formal pullback by `T* f=f∘T`, and set `Δ=T*−I`. In the finite jet algebra, each application of `Δ` raises total degree by at least one, so

\[
\log(T^*)=\sum_{r\ge1}\frac{(-1)^{r+1}}r\Delta^r
\tag{4}
\]

is finite at every specified order.

This operator is indeed differentiation by a vector field. A direct finite-algebra proof uses the truncated `(T*)^a=Σ_r binom(a,r)Δ^r`, whose coefficients are polynomials in a. For nonnegative integer a it is the pullback of an actual iterate, hence multiplicative. The two parameter polynomials agree at infinitely many integers and therefore for every a. Differentiation at zero gives the Leibniz rule and (4). Applying the same argument to forms, `T*Ω=Ω` implies `log(T*)Ω=0`, where `Ω=dx∧dy`. For the corresponding vector field X this is

\[
\mathcal L_X\Omega=(\operatorname{div}X)\Omega=0.
\]

Thus volume preservation does imply a divergence-free formal logarithm and, degree by degree, `div X_m=0`. This verifies the five changed lines; the certificate does not rely on a false divergence assertion.

For this example, (3) directly gives

\[
\begin{aligned}
\Delta x&=y^2+x^3y+O_5,&
\Delta^2x&=2x^3y+O_5,&
\Delta^3x&=O_5,\\
\Delta y&=x^3+\tfrac32x^2y^2+O_5,&
\Delta^2y&=3x^2y^2+O_5,&
\Delta^3y&=O_5.
\end{aligned}
\]

Substitution into (4) yields

\[
\boxed{X_2=y^2\partial_x,\qquad
X_3=x^3\partial_y,\qquad X_4=0.}
\tag{5}
\]

Every field has zero divergence; the fourth-degree term is **exactly zero**. Higher logarithm terms may remain, but cannot affect the fourth jet in any subsequent step.

## 4. A fixed shear decomposition meeting the paper's requirements

To rule out an inadmissible decomposition, here is a shear basis fixed for all inputs and depending only on m. For every `m≥2`, use

\[
V_\infty=y^m\partial_x,\qquad
V_t=(x+t y)^m(-t\partial_x+\partial_y),
\quad t=0,1,\ldots,m.
\tag{6}
\]

Every field has the required form `l(z)^m v` with `l(v)=0`. Homogeneous degree-m vector fields in complex dimension two form a space of dimension `2(m+1)`. Divergence maps surjectively to homogeneous degree-(m−1) polynomials, so its kernel has dimension `m+2`.

The `m+2` elements in (6) are independent. Under the Hamiltonian correspondence `(−∂_yH,∂_xH)`, they correspond to `−y^{m+1}` and `(x+t y)^{m+1}`. A linear relation, after comparing coefficients of `x^{m+1-r}y^r` for `0≤r≤m`, gives a Vandermonde system at nodes `0,1,…,m`. All finite-node coefficients vanish, then so does the remaining coefficient of `y^{m+1}`. Thus these form a shear basis.

Its coordinate decomposition is an allowed fixed linear decomposition, with a finite operator norm depending only on m, satisfying all quantitative requirements. In particular:

- For m=2, `X_2` is exactly `V_∞`, with one nonzero shear coefficient.
- For m=3, `X_3` is exactly `V_0`, with one nonzero shear coefficient.
- For m=4, `X_4=0`, so all linear-decomposition coefficients vanish.

There is consequently no same-degree ordering choice and no concealed freedom to choose a decomposition depending on the input.

## 5. Rigorous fourth-order failure

Following ordinary degree-by-degree realization, apply the quadratic field and then the cubic field. Through degree four the algorithm gives

\[
\mathcal P=R_1\circ S_1
=\left(x+y^2,\quad y+(x+y^2)^3\right),
\]

hence

\[
J_4\mathcal P=
\left(x+y^2,\quad y+x^3+3x^2y^2\right).
\]

Comparison with (3) gives

\[
\boxed{J_4(\mathcal P-\mathcal T)
=\left(-x^3y,\quad\tfrac32x^2y^2\right)\ne0.}
\tag{7}
\]

This nonzero defect is precisely

\[
\tfrac12[X_2,X_3]
=\left(-x^3y,\quad\tfrac32x^2y^2\right).
\]

Along `(x,y)=(r,r)`, its leading term is `r^4(−1,3/2)`. All coefficients are exact rational numbers.

The actual “correcting degree m” induction at line 5186 works for m=2,3 and fails at m=4: the current residual is nonzero, but the fourth component of the fixed target logarithm is zero, so no correction occurs. Continuing to any `d>4` adds factors `Id+O_5`, which preserve the fourth jet when composed on either side. Thus (7) persists for any high d used in the paper.

The failure is also independent of composition direction. Placing each layer on the other side gives

\[
J_4(S_1\circ R_1)
=(x+y^2+2x^3y,\ y+x^3),
\]

whose error is the nonzero negative of (7). Switching sides only changes its sign. The paper's layer order and the primary change/h_k order in §8.5 were not modified.

Changing the fixed shear decomposition cannot make the procedure valid for all inputs. Let `A_m(X_m)` be the map produced at layer m by any fixed linear decomposition. If it fails for `S₁`, that is already an admissible constant-volume counterexample. If it succeeds, since `S₁` has only `X₂` in its logarithm, it must satisfy `J₄ A₂(X₂)=J₄ S₁`. The same quadratic input gives the same `A₂(X₂)` here. Every product of cubic shears has the form `Id+X₃+O₅`: cubic cross-effects first occur in degree five, so that layer cannot supply a compensating quartic term. Also `A₄(0)=Id`. Hence any fixed linear decomposition passing the single-shear `S₁` check leaves (7) for target (1), or its negative if composed on the other side. The failure is not specific to the basis of §4.

In contrast, the original residual method selects in degree four

\[
C_4=\left(x^3y,-\tfrac32x^2y^2\right),
\qquad \operatorname{div}C_4=0.
\tag{8}
\]

Realizing (8) with the same shear basis exactly cancels (7). The minimal repair restores the original definition of `X_m`. Alternatively, recompute the logarithm of the **current residual map** at each step and use its first homogeneous component; a fixed target logarithm does not perform this update.

## 6. Local checks that still pass

All of the following hold simultaneously:

1. Input and output are genuine polynomial automorphisms with explicit polynomial inverses.
2. Both fix zero and have central derivative exactly I.
3. Both Jacobians are identically one to all orders.
4. Every homogeneous logarithm field is divergence-free, and the shear decomposition is valid.
5. Quadratic and cubic jets agree exactly.
6. Degrees, inverse degrees, and coefficients have bounds depending only on fixed n,d.

The changed definition also preserves polynomial dependence of coefficients: (4) is a finite rational polynomial at fixed order, (6) is a fixed linear decomposition, and finite shear composition and inversion are polynomial operations. Thus the candidate preserves the commonly checked determinant, low-order terms, invertibility, and coefficient budget. It loses exact compatibility between “some volume-preserving realization” and “the required same d-jet.”

## 7. An explicit manifold satisfying the full geometric hypotheses

Take `M=C²`, base point zero, `q=|z|²`, `a=sqrt(1+q)`, and Kähler potential

\[
\mathcal U(q)=4\bigl(\sqrt{1+q}-\log(1+\sqrt{1+q})-1+\log2\bigr).
\tag{9}
\]

Its tangential and radial eigenvalues are

\[
f(q)=\mathcal U'(q)=\frac2{1+a},
\qquad b(q)=f(q)+qf'(q)=\frac1a.
\tag{10}
\]

Both are positive and smooth everywhere, so `g=∂∂̄ U` is a smooth positive-definite Kähler metric. The radial distance is

\[
\int_0^R(1+r^2)^{-1/4}\,dr\longrightarrow\infty.
\]

Every escaping curve's length bounds increments of this radial distance, proving completeness.

For a direct proof of strictly positive bisectional curvature, set

\[
J(q)=\int_0^q b(v)\,dv=2(a-1),
\qquad \theta(q)=-q(\log b)'=\frac q{2(1+q)}.
\]

In the radial and tangential g-unit complex frame at `(sqrt(q),0)`, the Kähler curvature formula yields

\[
\begin{aligned}
A&=R_{1\bar1 1\bar1}=\frac{\theta'}b=\frac1{2a^3},\\
B&=R_{1\bar1 2\bar2}=R_{1\bar2 2\bar1}
=\frac{q b-(1-\theta)J}{J^2}=\frac1{4a^2},\\
C&=\tfrac12R_{2\bar2 2\bar2}
=\frac{J-q b}{J^2}=\frac1{4a}.
\end{aligned}
\tag{11}
\]

These follow directly by dividing the coordinate components

\[
-b'-q b''+q(b')^2/b,\quad
-f'-qf''+q(f')^2/f,\quad -2f'
\]

by `b²`, `bf`, and `f²`, respectively, taking the continuous limit at q=0. The two nontrivial numerator simplifications are

\[
a^3-a-(a^2+1)(a-1)=(a-1)^2,
\qquad 2a(a-1)-(a^2-1)=(a-1)^2.
\]

For nonzero tangent vectors U,V, the curvature contraction is

\[
R(U,\bar U,V,\bar V)
=A|U_1V_1|^2+B|U_1V_2+U_2V_1|^2+2C|U_2V_2|^2.
\tag{12}
\]

All coefficients are strictly positive. Simultaneous vanishing of the squares forces U or V to vanish: if `U₁≠0`, the first term forces `V₁=0`, hence `V₂≠0`; the third forces `U₂=0`, making the middle term nonzero. Other cases are symmetric. Bisectional curvature is therefore strictly positive everywhere. This is an allowed connected, noncompact, smooth, complete, complex two-dimensional example with strictly positive bisectional curvature.

## 8. The target can occur as an actual normalized atlas transition

Use the actual flow `h_t` constructed in §3, requiring only its proved smoothness, positive definiteness, `∂_t h_t=−Ric(h_t)`, and the local atlas of §7. No formal matrix flow is substituted.

At any sufficiently late `t₀`, choose the centrally normalized chart `Φ` at the origin from §7 and put `E=dΦ(0)`. For slightly later `t₁`, define the positive-definite matrix

\[
D=(E^*h_{t_1}(o)E)^{1/2}.
\]

The times can be close enough that D is close to I and the metrics are smoothly close on the small closed chart image. Define

\[
\Phi_0(z)=\Phi(z),\qquad
\Phi_1(w)=\Phi\bigl(\mathcal T^{-1}(D^{-1}w)\bigr).
\tag{13}
\]

On a fixed smaller ball, these are holomorphic locally biholomorphic charts centered at o. Their central derivatives are E and `ED^{-1}`, the latter satisfying

\[
(ED^{-1})^*h_{t_1}(o)(ED^{-1})
=D^{-1}D^2D^{-1}=I.
\]

Thus they are exactly normalized at their respective times. Because `T^{-1}` is a fixed polynomial automorphism with central derivative I and D lies in a fixed small neighborhood of I, one reduction of the radius gives the required two-sided metric and fixed-order derivative bounds. Replacing finitely many chart pairs this way preserves uniform properties of the whole atlas family. `t₀` can be arbitrarily late.

Their actual transition germ at zero is exactly

\[
F=\Phi_1^{-1}\Phi_0=D\mathcal T.
\tag{14}
\]

This follows from uniqueness of the original chart's local inverse, without treating an immersion as globally injective. Its Jacobian is identically `det D`, its central linear part is D, and time monotonicity and the volume clock give

\[
\|D\|\le1,\qquad
\det D=e^{-(s_1-s_0)/2},\qquad
\|D^{-1}\|\le e^{(s_1-s_0)/2}.
\]

Thus (14) satisfies both the actual linear-transition bounds and the constant-volume condition. Normalizing the derivative to I as prescribed gives exactly `J_d T` from (1). Restoring the linear part leaves the nonzero fourth-order defect `D·(-x³y,3x²y²/2)`.

Lines 5149–5150 explicitly make the lemma's bounds independent of grid or h; bad intervals are where this universal realization result is invoked at line 5540. Equation (14) geometrically realizes fully admissible input, without invented curvature data or an enlarged input class.

## 9. Exact route into the later proof

1. **Lines 5185–5188:** fixed target-logarithm components actually generate the shear product; (7) directly refutes “Induction … proves realization.”
2. **Lines 5540–5547:** bad macro-steps invoke this realization and assert `eq:dyn:jet-conjugacy`. Constant Jacobian, central derivative, degree, and coefficient bounds remain valid; realization of the target d-jet is missing.
3. **Lines 5695–5708:** `eq:unif:remainder` requires agreement of two compositions through degree d. For admissible input (14), the current algorithm's model has a nonzero quartic defect. Along `(x,y)=(r,r)`, its leading error is `r⁴D(-1,3/2)`. For any `d≥4` and finite C, the bound `|error|≤C|z|^{d+1}` fails on every full neighborhood of zero because the ratio diverges as `r^{3-d}`.
4. The subsequent orbit defect, backward shadowing error, and inverse-ball inclusion use this high-order remainder. No other realization algorithm replaces the proof invoked at line 5540.

The certificate directly exhibits a conflict between the specified construction and the exact jet condition actually used. Delaying the starting time, narrowing macro-steps, increasing d, or changing coarse coefficient constants cannot remove a nonzero fourth-order Taylor coefficient at a fixed step.
