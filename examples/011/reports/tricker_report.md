# Tricker report

## Single alteration

The edit replaces the fixed cohomological realization in the opening of the proof of Proposition 9.5 by **any** uniformly bounded-rank mixed-lisse realization of its values over `F_p`. It then uses the chosen realization to supply the traces over every `F_(p^a)`, with the same notation `T_(p^a)`.

The chosen object's stated properties are valid and such objects exist. They do not determine its extension-field traces. The later second-moment calculation concerns the original exponential sums, so it cannot be transferred to the selected realization on the strength of the specified properties. A fixed rank-two addition supplies an explicit admissible witness for this failure.

**Primary taxonomy: G2 — showing that existence of a selected realization suffices.** The dependence is carried through the notation `T_(p^a)`. G1 is an equivalent description of extending degree-one trace agreement to all extension degrees. The downstream invocation of Lemma 9.1 is where the missing identification becomes quantitatively fatal.

All theorem statements and assumptions are unchanged. The complete accepted TeX project is preserved, except for this one proof paragraph.

## Exact source and PDF locations

- Accepted source: `/Users/luosw/Desktop/bench/run_20261115/sources/c03/tex/main.tex`.
- Altered source: `/Users/luosw/Desktop/bench/run_20261115/attempts/c03_g203/paper/main.tex`.
- Stable label: `n10:moment-trace`, **Proposition 9.5**.
- Original paragraph: **lines 4340–4343**.
- Replacement paragraph: **lines 4340–4345**.
- The paragraph is on **PDF page 37** in both versions.
- The original function is defined in **(9.1)**, `n10:T`, on **page 35**.
- Its second-moment estimate is **Lemma 9.1 / (9.3)**, `n10:second-moment` and `n10:moment-two`, on **page 35**.
- The canonical Fourier complex and full trace formula are **(9.4)–(9.5)**, `n10:fourier-complex` and `eq : GLT`, on **page 36**.
- The decisive transfer of Lemma 9.1 starts at original source **line 4384**, altered source **line 4386**, **page 37**. The normalized contradiction concludes on **page 38**.
- The low-degree promotion use is on **page 38**, altered source **line 4509**, and in the proof of **Proposition 10.1**, **page 39**, altered source **line 4613**.

PDFs:

- Original: `/Users/luosw/Desktop/bench/run_20261115/sources/c03/paper.pdf`.
- Altered: `/Users/luosw/Desktop/bench/run_20261115/attempts/c03_g203/build/main.pdf`.

Exact original text:

```tex
From \eqref{eq : GLT}, we know that the restriction of
$T_{p^a}$ to $U(\FF_{p^a})$ is an alternating sum of
trace functions of lisse sheaves that are mixed with
integer weights.
```

Exact replacement:

```tex
From \eqref{eq : GLT}, the restriction of
$T_p$ to $U(\FF_p)$ admits a realization as an alternating sum of
trace functions of lisse sheaves that are mixed with
integer weights, with uniformly bounded total rank.
Fix any such realization and write $T_{p^a}$ for its trace on
$U(\FF_{p^a})$, for $a\ge1$.
```

The one-hunk patch is `minimal.diff`. The exact replacement strings are also recorded in `replacement.json`.

## Instantiated G2 obligation

For clarity in this report, write `T_q^can` for the exponential sum in (9.1), and write `τ_E(v;a)` for the trace of a chosen realization `E` over `F_(p^a)`. The altered paper uses `T_(p^a)` for both.

Fix the paper's `F`, a sufficiently large prime `p`, and permitted `V,U`. The new selection specifies a witness `E` satisfying:

1. Its cohomology sheaves on `U_(F_p)` are lisse and mixed with integer weights.
2. Their total rank is bounded independently of `p`.
3. For every `v∈U(F_p)`, its alternating trace satisfies

\[
\tau_E(v;1)=T_p^{\rm can}(v).
\]

In logical form the antecedent is

\[
\exists E\ \exists C<\infty:\quad
\operatorname{rank}_{\rm tot}(E)\le C,
\quad E\text{ has the stipulated lisse/mixed properties},
\quad\forall v\in U(\mathbb F_p),\ \tau_E(v;1)=T_p^{\rm can}(v),
\]

with `C` uniform as `p` varies. The chosen `E` is fixed before the extension degree `a` varies.

The consequent required later, when `d≤r` and `U⊂L\{0}` for a rational linear space of dimension `n−2`, is a second-moment bound for this same chosen witness:

\[
\forall a\ge1:\qquad
\sum_{v\in U(\mathbb F_{p^a})}|\tau_E(v;a)|^2
\ll_{F,L}p^{a(2n-3)}.
\tag{G2-consequent}
\]

Equivalently, the argument needs its normalized limsup, divided by `p^(a(2n−2))`, to be zero. That is what contradicts Xu's alternative and forces the asserted degree consequence.

The existentially selected variables are the realization `E` and a uniform rank bound `C`. The consequent universally quantifies the extension degree `a` and all extension-field points being summed. The geometric conclusion `d≥r+1` is independent of `E`; the extension-field trace sequence used to obtain it is not.

The original selected class consists of the actual cohomology sheaves of `K_(p,ψ)` or realizations preserving their alternating traces at **all** closed points. The replacement target class specifies agreement only at the degree-one points. The witness below belongs to the latter class and fails the required consequent by a fixed power.

The new operation is explicitly “Fix any such realization,” rather than a changed statement of a cited theorem. Xu's result applies correctly to the chosen realization's full trace sequence. Lemma 9.1 supplies a correct estimate for `T_q^can`. The fault is the asserted sufficiency of the selected realization's properties for identifying those two sequences. The later bad application of Lemma 9.1 is a consequence of that choice-dependence, not the origin of the alteration.

## The independent admissible realization

Keep the paper's `F` and all its standing assumptions. Choose a rational linear space

\[
L\subset\mathbb A^n,\qquad\dim L=n-2,
\]

and set `V=L`. This is an allowed geometrically irreducible affine cone with

\[
r=1,\qquad d=1\le r.
\]

Choose a nonempty smooth open `U⊂L\{0}`, defined over `Q`, on which the cohomology sheaves of `K_(p,ψ)` are lisse for all sufficiently large `p`, with uniformly bounded total rank. Such a choice follows from the unchanged Lemma 9.3, by taking a dense open subset of this linear space in an adapted stratum. Thus this is an actual instance of the geometric objects and hypotheses of Proposition 9.5.

Write

\[
\mathcal K=K_{p,\psi}|_{U_{\mathbb F_p}},\qquad M=n-1.
\]

Let `χ_p` be the geometrically constant rank-one `Q̄_ℓ` sheaf whose geometric Frobenius at the base field acts by `−1`. It is the character of the constant-field quadratic extension `F_(p²)/F_p`, pulled back to `U`. Its existence is independent of the geometry of `U`. In fact, it and the Tate sheaves below are pulled back from `Spec F_p` to the whole punctured ambient affine space. Thus the chosen realization can also be extended as `K_(p,ψ) ⊕ G_p[−(2n−2)]` to `L\{0}`; all traces in the later enlarged sum can be defined there as well.

Define the geometrically constant rank-two sheaf

\[
\mathcal G_p
=\overline{\mathbb Q}_\ell(-M)
\ \oplus\
\bigl(\chi_p\otimes\overline{\mathbb Q}_\ell(-M)\bigr).
\]

Its two Frobenius eigenvalues over `F_p` are

\[
p^M,\qquad -p^M.
\]

Both have weight `2M=2n−2`. For every `a≥1`, every `q=p^a`, and every `v∈U(F_q)`,

\[
t_{\mathcal G_p}(v;q)
=(p^M)^a+(-p^M)^a
=q^M\bigl(1+(-1)^a\bigr).
\tag{1}
\]

In particular the trace is **zero at every base-field point**, and is `2q^(n−1)` at every point over an even-degree extension.

Now take the selected realization to be

\[
\boxed{\displaystyle
\mathcal E=\mathcal K\oplus\mathcal G_p[-(2n-2)].}
\tag{2}
\]

The added cohomology degree is even, so the contribution in the alternating trace has positive sign. Consequently

\[
\boxed{\displaystyle
\tau_{\mathcal E}(v;a)
=T_{p^a}^{\rm can}(v)
+p^{a(n-1)}\bigl(1+(-1)^a\bigr).}
\tag{3}
\]

Every property specified for the new choice is satisfied:

- `E` is a constructible complex with lisse cohomology on the same `U`.
- The additional sheaf is pure of the integer weight `2n−2`; hence `E` is mixed with integer weights.
- The total rank increases by exactly **two**, uniformly over `p` and `ψ`.
- It has exactly the required base-field trace, by (1) with `a=1`.
- It is fixed once `p` is fixed; no new realization is chosen as `a` varies.
- Even the original cohomological weight envelope is respected: the added sheaf is placed in degree `2n−2` and has weight exactly that degree. No degree larger than the canonical compact-support range is introduced.
- The additional summand is geometrically constant, so it is lisse on every stratum and compatible with the homogeneous structure. It does not introduce a hidden stratification or conductor issue.

If the original total-rank bound is `R₀`, take `C=R₀+2`. This is a uniform upper bound both for the original ranks referred to in the statement and for the chosen realization. Thus the witness does not exploit a change in the meaning of the rank constant.

All Frobenius actions here are specified explicitly and their traces are computed correctly. The missing information is that equality of one Frobenius trace does not determine the traces of its powers. There is no use of an abstract cohomology isomorphism as a substitute for equivariance.

## Quantitative failure under the operative hypotheses

Let `q=p^a` with `a` even. For sufficiently large `q`, the open set in the linear space satisfies

\[
N_q:=\#U(\mathbb F_q)\ge\tfrac12q^{n-2}.
\]

This follows because its complement is a fixed proper closed subset of `L`, of dimension at most `n−3`, after spreading out over a sufficiently large base prime.

By the unchanged Lemma 9.1, restricted to `U` by positivity,

\[
\|T_q^{\rm can}\|_{\ell^2(U(\mathbb F_q))}^2
\le Bq^{2n-3}
\tag{4}
\]

for a fixed constant `B`. The added trace is the constant vector of value `2q^(n−1)`, whose squared norm is

\[
4q^{2n-2}N_q\ge2q^{3n-4}.
\tag{5}
\]

Once `q^(n−1)≥2B`, its norm is at least twice the norm in (4). The reverse triangle inequality applied to (3) gives

\[
\begin{aligned}
\sum_{v\in U(\mathbb F_q)}|\tau_{\mathcal E}(v;a)|^2
&\ge\left(
2q^{n-1}\sqrt{N_q}
-\|T_q^{\rm can}\|_2
\right)^2\\
&\ge q^{2n-2}N_q\\
&\ge\tfrac12q^{3n-4}.
\end{aligned}
\tag{6}
\]

Thus arbitrary cancellation from the canonical trace has already been accounted for. The mismatch is not based on assuming that the original exponential sum has a favorable sign.

The G2-consequent would bound this by `O(q^(2n−3))`. The lower exponent in (6) exceeds it by `n−1`. For `n=10`, the asserted upper power is `q^17`, whereas the selected realization has lower power `q^26` along every sufficiently large even extension degree.

At the normalization actually used in Proposition 9.5,

\[
\frac1{q^{2n-2}}
\sum_{v\in U(\mathbb F_q)}|\tau_{\mathcal E}(v;a)|^2
\ge\tfrac12q^{n-2}\longrightarrow\infty
\quad(a\to\infty,\ a\text{ even}).
\tag{7}
\]

In contrast, the canonical normalized second moment tends to zero by (4). The same selected realization therefore exhibits exactly the incompatibility that the proof suppresses through its notation.

For `r=1`, Xu's weight parameter is `w=n−1`. Its first alternative for the chosen realization would imply a squared moment `O(q^(2n−3))`, contradicting (6). Consequently the chosen realization falls into the large-moment alternative. But its variety has `d=r=1`. The subsequent claim that this alternative forces `d≥r+1=2` is therefore false for this admissible witness. The displayed contradiction `1≤0` arises by transferring the canonical moment estimate to a different extension-field trace sequence.

This uses the paper's own `F` and the local data already supplied in its contradiction argument. The constructed object is the sheaf realization, not a proposed ten-variable cubic without rational zeros. It is available for every canonical complex, so it introduces no inadmissible arithmetic replacement for `F`.

## The supplied reference and the exact proof obligation

In the permitted `Xu20.txt`, Section 3.3, printed page 19, defines a sheaf's trace function as the collection over **all finite extensions** of the base field. Theorem 3.5 uses that collection. The continuation of Remark 3.6 on printed page 20 permits mixed lisse sheaves on a normal variety; the smooth `U` here satisfies this condition.

The selected `E` satisfies those hypotheses. Xu's theorem legitimately detects its large extension-field moment. The theorem does not assert that arbitrary realizations agreeing only on `U(F_p)` give the same alternative or the same higher traces.

The source's canonical construction (9.4) and trace formula (9.5) establish the necessary compatibility for `K_(p,ψ)`. The replacement discards that construction as a restriction on the selected witness and retains only its degree-one values, lissity, integer weights, and a rank bound. The report's explicit `E` satisfies all these retained properties, including the original weight-degree envelope, while changing the extension sequence.

## Downstream necessity, repair, and subtlety

Proposition 9.5 is used to promote the dense open portions of low-degree components to the preceding frequency level in Section 10. For a component of codimension `j+1` and degree at most `j`, the degree alternative is excluded, so the proposition must supply

\[
S_p(v)\ll p^{(n+j)/2}.
\]

These improved estimates enter the definition and analysis of the partition `P_j`, Proposition 10.1, the weighted cube-free estimate in Proposition 10.9, and the mixed-modulus saving in Proposition 11.1. The high-moment contradiction is the mechanism that establishes this low-degree improvement. A base-field realization whose higher traces differ cannot supply that mechanism through Lemma 9.1.

The minimal repair is to retain the actual canonical cohomology realization, as in the original paragraph. More generally, the selection must preserve its alternating trace on every `U(F_(p^a))`, or be made from its actual pure/semisimple constituents in a way preserving the full virtual sheaf class. Increasing `C`, excluding finitely many primes, or changing a tie in the construction cannot remove (7): the rank increase is already fixed, and the same example works at every permitted base prime.

The fault is substantive: the selected witness changes a moment of order at most `q^(2n−3)` into one of order at least `q^(3n−4)` on the same low-degree linear cone. Its existence and local properties are unproblematic. It is the assertion that these properties suffice for the later choice-independent degree argument that fails.

The implicit aspect is the reuse of `T_(p^a)`. At degree one the identification is exact, and both lissity and weight checks still work. Xu's theorem also applies. The inconsistency appears only when the argument imports the earlier exponential-sum moment for the extension sequence belonging to the newly selected witness.
