REJECT

This verdict assesses the printed arguments under the assignment's no-repair condition. I found an invalid inference in the proof of the full-dimensional polyhedral structure theorem and a separate unjustified extension of an example to arbitrary online algorithms. The first defect concerns a main structural result and its downstream uses. I give a concrete instance in which the property asserted in that inference fails. Neither finding is presented as a counterexample to the paper's main theorem statements.

## 1. Theorem 7.12: enlarging the time horizon invalidates the condition imposed on the chosen block

**References:** Theorem 7.12, proof, PDF pages 40–41; TeX lines 4216–4220, 4225–4233, and 4254–4258. In particular, the sentence following equation (7.76). TeX label: `TB`.

The proof first chooses an integer $N$ using (7.19), then chooses **any** block $B$ of the displayed form (7.64), contained in $\mathcal N_\delta$, such that $T^nB$ is a finite union of good blocks **for $0\le n\le N$**. It subsequently increases $N$ to obtain a cover of the torus by the translates of $\pi(B^\circ)$. After obtaining

\[
K^*=\bigcup_{n=0}^{N}T^nB,
\]

the proof says that, “By the choice of $B$,” every term in this union is a finite union of good blocks.

The imposed condition refers to the original $N$. It supplies no condition on the additional iterates introduced by the enlargement. The rational-independence hypothesis on the widths in Lemma 7.11 is not among the conditions imposed on the arbitrary block chosen here: citing that lemma to show the existence of a block with the stated finite-horizon property does not make every such block satisfy its stronger hypotheses. This is an actual invalid inference, not a change of a dummy index or a harmless typo.

Here is an explicit instance demonstrating the failure within the paper's own system. Take $m=2$, set

\[
p=\sqrt2-1,\qquad \mathbf p=(p,1-p),\qquad \delta=\tfrac12,
\]

and identify $H_0$ with the first coordinate $x$, as in Section 10. This vote vector is ergodic. The projection of $\mathcal N_{1/2}$ is the circle with one point removed, so its translates for $k=0,1$ cover the circle. Thus the original choice $N=1$ meets (7.19).

Put

\[
a=\tfrac52-6p>0,\qquad
B=\{(x,-x):|x|\le a\}.
\]

This is a block of form (7.64), with $\rho_{12}=2a$, and it is contained in $\mathcal N_{1/2}$. Both $B$ and $TB$ are nondegenerate intervals. Hence $B$ satisfies exactly the property required at its selection for $N=1$.

However, direct use of the printed two-party map (10.2) gives, in first-coordinate notation,

\[
T^6B=\{-\tfrac12\}\ \cup\ [12p-\tfrac92,\tfrac12].
\]

Indeed, the initial interval has radius $a\approx0.0147186$, and its right endpoint reaches a tie at step 6. At that endpoint the multi-valued map produces both $1/2$ and $-1/2$; the other points give the interval displayed above. Its left endpoint is approximately $0.470563$. Thus $-1/2$ is an isolated point of $T^6B$. Such a set is not a finite union of good blocks in the one-dimensional space $H_0$.

This failing iterate necessarily occurs within any enlarged covering horizon for this particular $B$. Each translate of $\pi(B^\circ)$ has Haar measure $2a\approx0.0294373$. Covering the circle with the translates indexed by $0,\dots,N$ therefore requires $N\ge33$, in particular $N\ge6$. The problem is consequently not just that an unnecessarily large horizon could be chosen.

**Effect on the proof:** The last inference in Theorem 7.12 is unsupported and can be false for a block allowed by the printed selection. The earlier identity (7.76) does not imply that each individual term has the asserted full-dimensional structure. The proof as printed therefore does not establish Theorem 7.12 by its stated argument.

**Effect on statements and dependencies:** The example above concerns the auxiliary block, not $K^*$; in fact the two-party attractor is already explicitly described elsewhere in the manuscript. Theorem 7.16, Corollary 7.17, and the full-support/every-branch-limit-set portions of Theorem B use Theorem 7.12. Their printed proof chain consequently inherits this gap. The existence, absorption, and almost-everywhere injectivity arguments in Theorem 7.5, and the empirical-measure result in Theorem 7.7, precede this step and do not use it. I have not supplied an alternative choice or a repaired proof.

## 2. Example 2.7: the displayed calculation does not extend as written to every online algorithm

**References:** Example 2.7, PDF page 11, equations (2.28)–(2.29); TeX lines 1592–1615. The broader online lower bound is stated at TeX lines 1539–1549, equation `b3`.

The example says to distribute the votes at each time uniformly among candidates who have not yet been elected. It then numbers the candidates “in the order that they are elected” and writes that, at time $t$, the unelected candidates are exactly $t,\dots,m$, each receiving $1/(m-t+1)$. This calculation assumes that the first $t-1$ winners are distinct. It is valid for the Frege trajectory used in the example, but the concluding assertion that this same example applies to **any** online algorithm does not justify that assumption for a general algorithm.

For a concrete failure of the printed extension, take $m=4$ and the deterministic online algorithm that always elects candidate 1. Under the stated instruction to divide votes uniformly among the never-elected candidates, the first three vote vectors are

\[
(1/4,1/4,1/4,1/4),\qquad
(0,1/3,1/3,1/3),\qquad
(0,1/3,1/3,1/3).
\]

Every never-elected candidate then has discrepancy $11/12$ at time $m-1=3$, whereas the equality asserted in (2.29) is $h_4-1=13/12$. No renumbering changes the repeated winner into two distinct winners. The third vote vector also directly disagrees with the claimed formula (2.28).

**Effect on the proof:** The last sentence of Example 2.7 extends a calculation beyond the conditions under which it was derived. Handling repeated elections would require an argument absent from the example.

**Effect on statements:** This finding concerns the supplied demonstration for arbitrary online algorithms. It leaves the Frege-specific equality example and its use to show sharpness of the time-dependent upper bound intact. The general online lower bound is also attributed to earlier literature; I have not checked those external sources and do not treat the defective example as a disproof of that bound.

## 3. Minor notation slips, distinguished from the substantive findings

- TeX lines 4459–4461 in Example 8.2 use $z_j(n)=-2/3$ while naming $z_1(n)=z_3(n)=1/3$ as the other coordinates. The immediately following argument is about coordinate 2; this is an index slip in that sentence.
- TeX lines 7815–7818 in the proof of the first-wall theorem introduce $V_i^0$, although the limiting vertices being enumerated immediately above are denoted $E_i^0$. This is a local notation slip; the counting argument specifies the intended collection.

These slips do not determine the verdict.

## Review coverage

I read the complete supplied `paper.tex`, lines 1–9078, including every proof, example, remark, and the bibliography. I used the matching 96-page PDF to check the printed locations of the findings and inspected all ten figures on PDF pages 54, 55, 58, 60, 68, and 81. I did not consult other manuscripts, previous reviews, workspace records, external mathematical sources, or another reviewer, and did not use a formal proof assistant.

The review covered the discrepancy inequalities and their equality analysis; the fixed-vote induction and near-extremality estimates; boundedness, torus projection, rational and intermediate dynamics; the ergodic attractor and invariant-measure proofs; the full-dimensional-block argument; the bias examples; the two-party formulas; the Farey partition and first-entry argument; the polygon construction, internal walls, vertex counts, boundary invariance, wall continuation and endpoint pairing; and the final divisor-method reformulation.

As independent checks, I evaluated the four displayed bias cases by exact rational polygon-area and centroid calculations, obtaining area 1 and the stated bias formulas at a parameter in each of the four domains. I also checked the two-party auxiliary-block calculation used in finding 1. These computations were diagnostic checks of the printed claims. I found no additional substantive error in the remaining arguments during this review; cited external results and historical/bibliographic attributions were not independently verified.
