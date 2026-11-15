REJECT

Independent mathematical review of *Frege's election method: discrepancy, invariant polygons and Farey geometry*, supplied version dated 10 November 2026.

The verdict concerns the proof as printed under the assignment's no-repair condition. I found one substantive local invalid inference in Theorem 7.12. The defect concerns the block chosen in that proof and the subsequent change of a quantified time bound. I give a concrete example satisfying the printed choice for which the later assertion about that block is false. This finding does not refute the polyhedral-attractor theorem itself.

## 1. Invalid enlargement of the time bound in Theorem 7.12

**References:** Theorem 7.12, TeX label `TB`, proof at lines 4214–4259; specifically the choice at lines 4218–4220, the enlargement at lines 4231–4233, and the concluding inference at lines 4257–4258. In the PDF these passages are on pages 40–41. The relevant preceding result is Lemma 7.11, label `LTB`, lines 4050–4061, and its defining equation (7.64), label `tb4`.

The printed proof first chooses an integer $N$ using the cover in equation (7.19), then chooses **any** block $B$ of the form (7.64), contained in $\mathcal N_\delta$, such that $T^n B$ is a finite union of good blocks for $0\le n\le N$. Later it increases $N$ to make the translates of $\pi(B^\circ)$ cover the torus. After proving

\[
K^*=\bigcup_{n=0}^{N}T^n B,
\]

the proof concludes: “By the choice of $B$, each set $T^nB$ in this union is a finite union of good blocks”. That conclusion uses the enlarged value of $N$, whereas the actual choice of $B$ only supplied the property through the original value.

The finite-time property is not preserved automatically when the time bound is enlarged. The following example shows that this is a genuine false inference under the conditions printed in the proof.

### Concrete example demonstrating the failure

Take $m=2$, identify $H_{\boldsymbol0}$ with the coordinate $x$ via $(x,-x)$, and put

\[
p=\sqrt2-1,
\qquad \mathbf p=(p,1-p),
\qquad \delta=\frac14,
\qquad r=4p-\frac32.
\]

Here $p\approx0.41421356$, $r\approx0.15685425$, and the vote vector is positive and ergodic. The multi-valued map is precisely the one printed in equation `T1b`:

\[
T_1x=
\begin{cases}
x+p,&x+p\le\frac12,\\
x+p-1,&x+p\ge\frac12,
\end{cases}
\]

with both images retained at equality.

Let $B=[-r,r]$. In the manuscript's hyperplane notation this is

\[
B=\{(x,-x): -\rho_{12}\le x-(-x)\le\rho_{12}\},
\qquad \rho_{12}=2r>0.
\]

Thus $B$ has exactly the form of (7.64), and $B\subset\mathcal N_{1/4}$.

The original covering requirement (7.19) allows $N=2$: the points $0,p,2p$ on the circle have successive gap lengths $p,p,1-2p$, all strictly less than $2\delta=1/2$. Therefore the open translates $R_p^k\widehat{\mathcal N}_{1/4}$, $0\le k\le2$, cover the circle.

Direct evaluation of the printed map gives

\[
\begin{aligned}
T_1^0B&=[-r,r],\\
T_1B&=[-\tfrac12,5p-\tfrac52]
       \ \cup\ [\tfrac32-3p,\tfrac12],\\
T_1^2B&=[\tfrac12-2p,6p-\tfrac52],\\
T_1^3B&=[\tfrac12-p,7p-\tfrac52],\\
T_1^4B&=[-\tfrac12,8p-\tfrac72]\ \cup\ \{\tfrac12\}.
\end{aligned}
\]

Every interval in the first three displayed iterates has positive length. Consequently this $B$ satisfies all the conditions expressly placed on the choice at lines 4218–4220 with $N=2$.

However, the later cover by translates of $\pi(B^\circ)$ requires a larger bound. Through $k=3$, there is still a circle gap of length $p>2r$, so these translates do not cover. Through $k=4$, the largest gap is $3p-1<2r$, so they do cover. Thus $N=4$ is an admissible enlargement of exactly the kind used at lines 4231–4233.

At that enlarged time, $T_1^4B$ has the isolated point $1/2$, separated from the interval by a positive gap, since $8p-7/2<1/2$. It is not a finite union of good blocks: in dimension one a good block is a nondegenerate compact interval, and a finite union of such intervals has no isolated point.

This example directly contradicts the sentence at lines 4257–4258 for a block permitted by the proof's stated choice. It also explains why the preceding lemma does not justify that sentence as written. Lemma 7.11 assumes rational independence of the enlarged family containing the parameters $\rho_{ij}$, and concludes the good-block property for **every** iterate. The proof of Theorem 7.12 cites it only to assert existence of blocks with the stated finite-time property; its selection says “any block” of the displayed form with that finite-time property. The additional rational-independence hypothesis is not part of that printed selection. For the block above,

\[
\rho_{12}=8p-3=5p_1-3p_2,
\]

so it illustrates exactly the distinction between the displayed form of a block and the stronger hypotheses of Lemma 7.11.

**Effect on the written proof.** The passage from the finite union (7.76) to a finite union of full-dimensional blocks is not justified by the conditions imposed on the chosen block. It requires an additional choice or argument. The no-repair review condition therefore prevents acceptance of the proof in its current wording. This is a quantifier/dependency error, not a typographical substitution in a formula.

**Effect on the theorem statements and later uses.** The counterexample concerns the intermediate assertion about $T^nB$, not the attractor: in this two-party example the attractor itself is the interval described elsewhere in the manuscript. Theorem 7.16 and the corresponding support/branch-limit conclusions use Theorem 7.12, so their printed chain of justification passes through this gap. The preceding discrepancy estimates, compact-invariant-set construction, uniqueness and equidistribution arguments do not depend on this particular inference. The planar invariance construction is also presented by a separate explicit argument.

## 2. Review coverage and other findings

I read the complete supplied `paper.tex`, lines 1–9078, in bounded, untruncated chunks. This includes the abstract and introduction, every theorem and proof, all examples and remarks, the divisor-method section, and the bibliography. I inspected all eight external figure assets, including rendering the four PDF figures, and read both in-source TikZ figure descriptions and coordinates. I also checked the matching PDF's rendering of the specific Theorem 7.12 passages quoted above. I did not independently re-read every PDF page after reading the complete TeX source.

The mathematical review covered:

- The harmonic discrepancy bounds, equality analysis, fixed-vote sharpness construction, near-extremizer estimates and the random-vote bound.
- Boundedness and absorption, the torus projection, subgroup structure, the rational case and the explicitly stated open problem about eventual period.
- The ergodic compact-attractor construction, almost-everywhere injectivity, invariant measure, weak convergence of empirical measures and branch-limit arguments.
- The generic-block lemma, including its graph/tree argument and use of rational independence; the defect identified above is in its use in the subsequent theorem.
- The intermediate-case examples, asymptotic-bias formulas and the one-dimensional dynamics.
- The planar coordinate change, first stability domain, Farey partition and first entry, zig-zag polygon construction, invariance including boundary ties, vertex counts and explicit $1/3$-cell formulas.
- The even- and odd-wall equations, their continuation through cells, endpoint calculations and pairing into triangles.
- The final reformulation of linear divisor methods.

As supplementary arithmetic checks, using ordinary code rather than a proof assistant, I checked the ceiling identities `va9a` and `va9b` for all 6,115 reduced fractions in $(0,1/2)$ with denominator at most 200. I also checked 3,289 nonempty odd-wall equations from all cells through denominator 80 against their claimed primitive first-wall lines. Exact rational polygon-area and centroid calculations at one parameter in each of the four displayed bias domains agreed with the stated area and bias formulas. These computations support the local formula checks and are not substituted for the printed proofs.

I found no further substantive mathematical error or invalid inference in the remaining reviewed arguments. There are harmless notational slips, such as `\pi^{-1}(\vx)` where the surrounding sentence specifies the torus point `\hvx` at TeX line 2962, and the temporary vertex name `V_i^0` instead of the previously introduced `E_i^0` at lines 7815–7818. The referents are explicit in their surrounding sentences, and these slips do not alter the mathematical reasoning.

I used only the supplied manuscript and its assets as mathematical source material. No external mathematical sources, other versions, other reviews, private records or formal proof assistant were consulted. Bibliographical entries were read as supplied; I did not externally verify their publication metadata or the cited literature's contents.

The final verdict is **REJECT under the no-repair condition**, on the single quantified-choice defect in the printed proof of Theorem 7.12 described above.
