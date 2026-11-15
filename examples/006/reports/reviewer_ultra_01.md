VERDICT: ACCEPT

# Review report (originally in Chinese)

## Conclusion and scope

I accept the current mathematical arguments. Theorem 1.1's zero-frequency derivative construction and instability criterion, Theorem 1.2's mass-slope limit, and Theorem 1.3's scaling criterion including equality all have valid proof chains. The appendix's global analysis of the regular homogeneous solution supports the signs, uniqueness, and nondegeneracy used in the main text.

I read all 5560 lines of `paper.tex`, covering the abstract, Sections 1–8, Appendix A, and references, and extracted text from the same directory's 66-page `paper.pdf` to check theorem and lemma numbering. Only designated paper materials and my generated checking text were used. Explicitly cited established results were treated as foundational inputs, emphasizing their applicability here, new arguments, and dependencies. The paper was not modified.

The main decisive checks follow.

## 1. Parameter ranges, integrability thresholds, and asymptotic notation

I used the paper's explicit definition of `∼`: the ratio tends to some positive number, not necessarily 1. Thus Theorem 1.1's `η₀∼−r²φ₀` and exceptional `η₀∼−1` are signed asymptotics allowing positive proportionality constants.

For noncritical cases, radial integration directly gives

\[
 \phi_0\in L^2\iff 2\alpha>d,
 \qquad \langle x\rangle\phi_0\in L^2\iff 2\alpha>d+2.
\]

At critical `p=p*`, the respective tail integrals are

\[
 \int^\infty r^{3-d}(\log r)^{-(d-2)}\,dr,
 \qquad
 \int^\infty r^{5-d}(\log r)^{-(d-2)}\,dr.
\]

They indeed include the logarithmically improved endpoints `d=4` and `d=6`, respectively. This verifies (1.4), (1.10), and Section 2's integrability ranges, and confirms that later classifications retain both endpoints.

## 2. Fundamental solutions and signs

Section 3's four integral equations agree with

\[
 (r^{d-1}U^2h')'=\rho(1+h)
\]

with correct directions and signs; shrinking the origin neighborhood or enlarging the tail interval makes the contraction constant less than 1. The logarithmic-critical error integral is `O((log r)^(-ε))`, sufficient for the fundamental-solution and derivative estimates.

Lemmas 4.1 and 4.2 correctly use the appendix: the regular solution satisfies

\[
 v_\omega^+=c_1w_\omega^++c_2w_\omega^-,\qquad c_1<0,
\]

The fundamental-solution Wronskian in the specified order is negative at infinity, making the regular/decaying-solution Wronskian constant `Wω` positive. This agrees with negative leading terms in the two later variation-of-parameters integrals.

Lemma 4.3's comparison for the infinite integral also works: on a uniformly chosen exterior domain, `L₀φ₀≥0` and `V₀>0`; the maximum principle gives `0<w₀⁻≤Cφ₀`, so `φ₀∈L²` supplies integrability.

## 3. Construction, critical asymptotics, and uniqueness of η₀

Locations: Propositions 4.4 and 4.5, TeX lines 1971–2314, especially `eq:eta0`, `eq:lam-alpha`, `eq:lam-alpha2`.

Differentiating the variation-of-parameters integrals cancels endpoint terms in the first derivative and produces the correct positive forcing `φ₀` in the second-order equation. The `O(r)` derivative bound and integral form yield `η₀'(0)=0` and a continuous second derivative, enough for a radial extension in `C²(ℝᵈ)`.

The key noncritical algebraic identity is

\[
 P(\alpha-d)=P(2-\alpha)
 =-2(3\alpha+2-2d)<0.
\]

The last inequality holds throughout the permitted `φ₀∈L²` range: use `α>d/2` in low dimensions and also `α≥d−2` in higher dimensions. Both integrals therefore have negative leading order `r^(2−α)`, with compact-interval integrals lower order.

At `(d,p)=(4,2)`, the first term contains

\[
 (\log r)^2\int_r^\infty s^{-1}(\log s)^{-3}\,ds,
\]

and tends to a nonzero constant; the second is `O((log r)⁻¹)`, verifying the exceptional asymptotic. For `p=p*`, `d≥5`, both terms have order `−r²φ₀`.

I checked uniqueness condition `η₀=o(w₀⁺)` in every dimension case. The difference of two regular solutions is a multiple of `v₀⁺`; its nondecaying component is nonzero, so the prescribed asymptotic fixes the solution uniquely.

## 4. Local zero-frequency convergence and divergent mass slope

Locations: Lemma 4.7, Theorem 4.8, Lemma 4.9, Theorem 4.10, TeX lines 2404–2870.

Normalizing the decaying fundamental solution at fixed `R₀` avoids frequency-dependent normalization at infinity. Local uniform derivative bounds followed by uniform tail decay identify each subsequential limit, completing the argument. The normalized Wronskian limit is strictly positive, so division is stable.

Near zero the dominating functions are `r(1+|log r|)` or `r`; at infinity they are `Cφ₀²r^(d−1)`, integrable under the assumptions including logarithmic endpoint `(4,2)`. This supports `ηω(0)→η₀(0)`. Integral equations, Gronwall, and the integral representation of `ηω'(r)/r` then give local `C²` convergence including zero.

The mass-slope divergence proof additionally establishes `ηω≤0` on a uniform exterior domain before applying Fatou to `−ηωφω`. This controls the tail sign, allowing local convergence and the limit's negative-infinite integral to imply `M'(ω)→−∞`.

## 5. Truncated negative direction and dynamical instability

Locations: Theorem 5.1, Lemmas 5.2–5.3, Proposition 6.1, TeX lines 2893–3442.

The cutoff direction is exactly orthogonal. Write `m=‖φ₀‖₂²`, `I=⟨η₀,φ₀⟩<0`. In the finite-pairing case the three limits are

\[
 \beta_R\to-m/I,\quad
 \langle L_0(\varphi_R\eta_0),\phi_0\rangle\to-m,
 \quad
 \langle L_0(\varphi_R\eta_0),\varphi_R\eta_0\rangle\to-I.
\]

Expanding the quadratic form indeed gives limit `⟨L₀φ₀,φ₀⟩+m²/I<0`.

For infinite pairing, I checked these critical errors:

- `2α=d+2`: the denominator grows like `log R`; the quadratic cutoff error vanishes after scaling by `βR²`.
- `(d,p)=(4,2)`: `|βR|=O(R⁻²log R)` and the largest quadratic cutoff error is `O(R²)`, giving `O(R⁻²(log R)²)`.
- `p=p*`, `d=5`: `|βR|=O(R⁻¹(log R)³)`, with product `O(R⁻¹(log R)³)`.
- Finite-pairing endpoint `p=p*`, `d=6`: the unscaled tail error already vanishes by logarithmic factors.

Proposition 6.1's dynamics apply in this energy-subcritical range. Nehari tangent nonnegativity ensures `⟨K₀'(φ₀),ψ⟩≠0`; the implicit function theorem gives a local return parameter to the Nehari manifold; energy comparison gives a lower bound for `|𝒫|` from a fixed positive energy gap. If the orbit remains in the phase neighborhood, its `H¹` norm stays bounded and continuation gives forward global existence; monotone growth of a bounded Lyapunov functional then contradicts this. The required long-time existence is obtained under the contradiction hypothesis.

## 6. Finite mass-slope limit and equality in scaling

Section 7's compactness and operator-norm argument are correct. Strong convergence of `Jω`, compactness of `B₀`, and self-adjointness for the right product upgrade to norm convergence `Bω→B₀`. The kernel is excluded in `Ḣ¹`, applying to functions from the Birman–Schwinger factorization and proving invertibility of `I+B₀`.

In Theorem 1.2(ii)'s additional range, dominating integrals for `φ₀∈L^(2d/(d+2))` and `V₀∈L^(d/2)` converge; in particular, at `d=6,p=p*`, the former radial integral is `r⁻¹(log r)⁻³`. With `η₀∈Ḣ¹` and uniqueness of the inverse, `L₀⁻¹(−φ₀)=η₀` is valid.

Lemma 8.1 proves pointwise strict positivity on the negative-eigenfunction orthogonal complement, without requiring a uniform spectral gap. Polarizing a zero quadratic form gives the weak homogeneous equation, excluded by the regular fundamental solution's nondecaying component, establishing strict positivity.

Theorem 1.3's `η₀+βψ` is nonzero because `ψ=O(φ₀)` whereas `η₀∼−r²φ₀`. Thus strict positivity yields `⟨η₀,φ₀⟩<0` even at zero scaling second derivative. Equality is explicitly and correctly covered.

## 7. Key appendix shooting checks

Locations: Lemmas A.5–A.15, Propositions A.12 and A.16, TeX lines 4551–5240.

Monotonicity of `F(s)=sg'(s)/g(s)` and the single sign change of `Iλ` are correctly derived. Lemma A.10 continues the difference's zero count using persistence of simple zeros on compact intervals and uniform positive lower bounds on the tail; Lemma A.11 transfers the zero count to the shooting derivative.

Proposition A.12 is a key step. I particularly checked the boundary term for `p>p*`:

\[
 R^{2d-2}u'(R)v'(R).
\]

This generally has only a bounded estimate; the paper correctly uses tail `v'>0` for a nonpositive upper limit, comparing with the strictly positive product at the zero to contradict `u(r*)>β`. The subsequent different Wronskian does have vanishing boundary terms; sharper two-dimensional exponents work too. Thus `c₊≠0`, and negativity after the unique zero gives `c₊<0`.

Lemma A.15 for `ω=0,p>p*` uses

\[
 v_*(R)+\frac{R}{d-2}(v_*'(R))_+<0
\]

for tail control. Since `v*→c₊<0` and `rv*'→0`, a fixed `R` can satisfy it. The strict inequality persists for nearby parameters, and integral comparison prevents the difference and shooting derivative from reaching zero again. This proves entry into `𝒴₋` on the right, single-zero continuation, and `Rᵧ'<0`. Finally, `Rᵧ→∞` at a finite boundary parameter contradicts decrease, establishing global uniqueness.

## 8. Multiple-power extension

The stated extension requires positive highest-power coefficient and negative remaining coefficients. This preserves strict increase of `s^(-pN)g(s)` and the signs in its derivative, retaining the appendix's single-sign-change argument. The lowest power determines tail exponents and weighted integrability; the highest determines the energy-subcritical upper bound. With these substitutions, the three main results' structure and proofs remain consistent.

## 9. Nonsubstantive presentation suggestions

These two standard details could improve readability and can be added directly.

1. Section 8.1, TeX line 4147, says “the space … is dense in …”. Add a brief cutoff proof: for `d≥3`, use Hardy to control `R⁻²∫_{R<|x|<2R}|v|²`; for `d=2`, use tail `φ₀^(p−1)≍r⁻²` for the same term, clarifying two-dimensional density.
2. Section 8.2, TeX lines 4287–4294, could explain that substitution of the weak equation in the quadratic form first tests with `ϕRη₀` and `ϕRψ`, then takes limits using Section 5's cutoff bounds. This directly explains pairings with non-`L²` `η₀`.

Ordinary typesetting issues: no specific readability-affecting issue requires separate correction.

Substantive mathematical errors or unresolved issues preventing a conclusion: none. Based on these checks, the final verdict is **ACCEPT**.
