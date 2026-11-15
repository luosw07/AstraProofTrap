# Tricker report

## New construction and exact text

The new defect is in the proof of Theorem TB, the assertion that the compact ergodic attractor is a finite union of good blocks.

The original proof chooses a block whose auxiliary widths are jointly rationally independent with the vote vector, as required by Lemma LTB. That supplies good-block decompositions for every iterate of this one block. It then chooses a finite covering horizon that depends on the block. This order is valid.

The new proof first obtains a finite horizon for a larger neighborhood from the distant equation (tinv5a). It then explicitly permits **any** block of form (tb4) whose iterates are good only through that fixed horizon. Such blocks really do exist, so this selection is valid. When the proof later covers the torus by translates of the smaller block interior, it increases the same symbol N while retaining the selected block. Its final inference treats the original finite-range certificate as though it covered the newly chosen, block-dependent horizon.

The following three replacements constitute one coordinated error. They are not three independent faults.

### Replacement 2: choose the finite-range witness

Source: TB, current lines 4218-4222. Candidate: lines 4218-4220. Dependencies: (tinv5a), (tb4), and LTB.

Before:

~~~tex
Let
$B$ be the block in \eqref{tb4}, 
where we choose all $\rho_{ij}$ as in \refL{LTB} and so
small that $B$ is a subset of the neighbourhood
$\cN_\gd$  of $0$ in $\Ho$. 
~~~

After:

~~~tex
Choose $N$ as in \eqref{tinv5a}, and then choose any block $B$ of the form
\eqref{tb4} contained in $\cN_\gd$ such that $T^nB$ is a finite union of
good blocks for $0\le n\le N$. Such blocks exist by \refL{LTB}.
~~~

### Replacement 3: enlarge the parameter after fixing the witness

Source: TB, current line 4234. Candidate: line 4232.

Before:

~~~tex
and thus there exists a finite $N$ such that
~~~

After:

~~~tex
and thus, increasing $N$ if necessary,
~~~

The surrounding, unchanged sentence now says that the projected interior and its translates are open and, increasing N if necessary, their translates through N cover the torus. That compactness assertion itself is true. The error is retaining a witness whose guarantee was made for the earlier value of N.

### Replacement 4: use the old witness through the new range

Source: TB, current lines 4259-4260. Candidate: lines 4257-4258.

Before:

~~~tex
By \refL{LTB}, each $T^nB$ is a finite union of good blocks, and the result
follows.  
~~~

After:

~~~tex
By the choice of $B$, each set $T^nB$ in this union is a finite union of
good blocks, and the result follows.
~~~

This assertion is false for an allowed witness, as shown below. It is used to conclude that the finite union representing K* is a finite union of good blocks. It is not an unused stronger aside.

## Long dependency chain

1. Current/candidate lines 3378-3382 in the proof of Tinv fix 0 < delta <= 1/m and define N_delta in H_0 and its torus neighborhood Nhat_delta.
2. Current/candidate lines 3454-3463, Step Tinv5 and (tinv5a), obtain a finite cover of the torus by translates of **Nhat_delta**. This is roughly 755 lines before the new block selection. That bound depends on the previously fixed larger neighborhood and the translation.
3. Current/candidate lines 4015-4023 define good blocks to have full dimension m-1. Lines 4038-4045 explicitly warn that a tied cut of a good block can produce a lower-dimensional piece.
4. Current/candidate lines 4050-4060, LTB and (tb4), give an all-iterate guarantee when p_1,...,p_m and all widths rho_ij are jointly rationally independent. The proof at lines 4064-4202 uses this independence to rule out a supporting cut throughout the induction. The restriction is on a single choice of widths across all times.
5. Candidate lines 4218-4220 retain only existence of a witness good through the initial finite horizon. This is a valid consequence of LTB, but it allows additional witnesses that are not globally nonresonant.
6. Candidate lines 4231-4233 cover the torus by translates of **pi(interior B)**, a smaller set. The new cover horizon depends on the already selected B, rather than only on delta and p.
7. Candidate lines 4235-4256 keep the original, valid invariant-set and unique-lift argument. It gives K* equal to the union of T^nB through this later horizon. It does not supply goodness of those images.
8. Candidate lines 4257-4258 import the old finite-iterate guarantee into the new range. The distant cover of Nhat_delta does not control the covering time of an arbitrary smaller B.
9. The exact disproof can be read against (T1b), current lines 4894-4906 and candidate lines 4892-4904, in the later two-party section. Example Em=2I, current lines 4975-4985 and candidate lines 4973-4983, confirms that the genuine attractor remains the interval [-1/2,1/2].

The two covers have the same formal appearance, and most of the intervening proof is unchanged and correct. Detecting the mistake requires distinguishing their sets, tracking when B was chosen, retaining its original certified range, and checking the multivalued boundary dynamics. It is not resolved by renaming the two occurrences of N.

## Required G2 audit

Write:

- C_delta(N0): the translates R_p^k(Nhat_delta), 0 <= k <= N0, cover the torus.
- F(B,n): T^kB is a finite union of good blocks for every integer 0 <= k <= n.
- P_delta,N0(B): B has form (tb4), B is contained in N_delta, and F(B,N0).
- C_B(M): the translates R_p^k(pi(interior B)), 0 <= k <= M, cover the torus.

**Implication before generalization.** Under the stated assumptions that p is ergodic, 0 < delta <= 1/m, and N0 is a finite witness for C_delta(N0), Lemma LTB gives

    C_delta(N0)  ==>  exists B: P_delta,N0(B).

One proves this valid implication by choosing sufficiently small positive widths jointly rationally independent with p; LTB even gives F(B,n) for every n for those particular witnesses. The existential conclusion used in the new text, however, specifies only P_delta,N0. The text expressly says to choose **any** such block. It does not retain the stronger all-iterate property or joint independence as a condition on that selected witness.

**Existential variables in the antecedent/choice chain.** The earlier compactness step supplies N0. With N0 fixed, the next existential variables are B, or equivalently its auxiliary positive widths rho_ij. After B is fixed, a further compactness argument supplies a cover horizon M depending on B. Taking M >= N0 is legitimate. These dependencies are ordered N0, then B, then M(B).

**Specified witness properties.** The selected B has form (tb4), lies in N_delta, and has F(B,N0). No all-time independence or F(B,M) is among these stated properties.

**Desired conclusion.** The proof wants K* to be a finite union of good blocks. Its valid geometric argument identifies K* with the union of T^nB for 0 <= n <= M(B).

**Extra witness property used.** The final sentence requires F(B,M(B)). The proof has only F(B,N0), and M(B) can be much larger than N0. It does not reselect B or establish that this particular witness has the stronger property.

**Dependence through notation.** The conclusion of the theorem is independent of B, but the intermediate decomposition is not. Its upper index M(B) depends on B. Reusing the letter N for both the initial certificate bound and the later covering bound hides that dependence. Merely having some suitable witness for every fixed finite range does not authorize keeping an arbitrary previously chosen witness when the range is changed in response to it.

A precise false assertion used by the revised proof is:

    For every B satisfying P_delta,N0(B), one can choose a cover horizon
    M >= N0 with C_B(M) and F(B,M).

The counterexample below satisfies P_delta,N0 but has no such M. Thus this is a falsifiable witness-dependence failure, not an absence of explanation. The quantifier error is not a claim that no globally suitable block exists: LTB correctly proves that such blocks do exist. It is the unsupported use of an arbitrary weaker existential witness as a stronger compatible one.

## Decisive admissible counterexample

Use the multi-valued map required by TB and let

    m = 2,
    epsilon = sqrt(2)/1000,
    p_1 = 1/4 + epsilon,
    p_2 = 3/4 - epsilon,
    delta = 1/2,
    N0 = 1,
    rho_12 = 4 epsilon.

Identify H_0 with the scalar x by (x,-x). Then ell_12(x,-x) = 2x, so formula (tb4) gives

    B = [-2 epsilon, 2 epsilon].

All the revised witness assumptions are satisfied:

- The votes are strictly positive and sum to 1.
- p_1 is irrational. If a p_1 + b p_2 = 0 with rational a,b, then (a-b)p_1+b=0, which forces a=b=0. Thus p is ergodic in exactly the paper's sense.
- delta=1/2 is allowed because m=2. B lies strictly inside N_delta=(-1/2,1/2).
- On the scalar circle, Nhat_(1/2) is the circle with [1/2] removed. Its translate by p_1 omits [1/2+p_1], a distinct point. Hence those two open sets cover the circle and N0=1 is a valid choice in (tinv5a).
- B is a nondegenerate closed interval and hence a good block. Its first image is also a nondegenerate closed interval, as calculated next. Therefore F(B,1) holds.
- The revised selection does not require joint rational independence of rho_12 with the votes. Indeed rho_12=3p_1-p_2, so this witness does not have LTB's stronger, all-iterate protection. That omission is intentional in the finite-witness choice, and does not invalidate the legitimate existence claim used to make that choice.

From (T1b), with both branches retained at equality,

    T_1 x = x+p_1       if x+p_1 <= 1/2,
            x+p_1-1     if x+p_1 >= 1/2.

Since 0 < epsilon < 1/12,

    B+p_1 = [1/4-epsilon, 1/4+3 epsilon] < 1/2.

There is no tie at the first iteration, so

    TB = [1/4-epsilon, 1/4+3 epsilon].

At the second iteration,

    TB+p_1 = [1/2, 1/2+4 epsilon].

At its left endpoint the two branch images are exactly 1/2 and -1/2. Every other point uses the subtract-1 branch. Consequently the full multivalued image is exactly

    T^2 B = [-1/2, -1/2+4 epsilon] union {1/2}.

The point 1/2 is isolated, separated by a positive gap from the interval. In one dimension every good block is a nondegenerate closed interval. A finite union of such intervals cannot contain an isolated point: a nondegenerate interval containing that point would contain other points arbitrarily near it. Therefore T^2B is **not** a finite union of good blocks.

This failure necessarily lies inside every covering range that the revised proof can use. Haar measure of pi(interior B) is 4 epsilon. If its translates through M cover the circle, then subadditivity gives

    1 <= (M+1) 4 epsilon.

Already this excludes M <= 1. More sharply, 176 translates have total measure at most

    176 * 4 epsilon = 88 sqrt(2)/125 < 1,

because 2*88^2 = 15488 < 125^2 = 15625. Thus every cover horizon M is at least 176. Ergodicity and compactness ensure that some finite covering horizon exists, but all such horizons include n=2, where the asserted good-block property fails. The number 176 is only a necessary lower bound; no claim is made that it is itself a covering horizon.

This witness respects the multi-valued tie convention exactly. Discarding the isolated branch value as a null set would change the set equality and the topological conclusion. TB is explicitly about the full multi-valued invariant set, not equality modulo Haar-null sets.

## A family ruling out a harmless fixed-bound repair

The defect is not confined to a special bad choice N0=1. Let any integer N0 >= 1 be given and set L=N0+1. Choose an irrational epsilon satisfying

    0 < epsilon < min{1/[2L(2L-1)], 1/(2L^2)}.

Set

    p_1 = 1/(2L)+epsilon,
    p_2 = 1-p_1,
    delta = 1/2,
    rho_12 = 2L epsilon,
    B = [-L epsilon, L epsilon].

Again p is ergodic, and any N0 >= 1 covers Nhat_(1/2). For 0 <= k <= L-1,

    T^kB = B+kp_1
         = [k/(2L)+(k-L)epsilon, k/(2L)+(k+L)epsilon].

The largest upper endpoint before time L is

    (L-1)/(2L) + (2L-1)epsilon < 1/2,

so every certified iterate through N0 is a nondegenerate interval and no earlier tie occurs. At the next iteration,

    B+Lp_1 = [1/2, 1/2+2L epsilon],
    T^LB = [-1/2, -1/2+2L epsilon] union {1/2}.

This again has an isolated point. The projected interior of B has measure 2L epsilon. The first N0+1=L translates have total measure at most 2L^2 epsilon < 1. Therefore every covering horizon is at least L and includes this first bad iterate. No choice of a larger fixed finite initial certificate repairs the inference for all permitted witnesses.

The repair must restore a witness with an all-iterate guarantee, as in the original proof, or establish an additional compatibility argument relating the selected block to its own cover time. Renaming N, choosing a larger constant once, or inserting “sufficiently large” does not establish that compatibility.

## Taxonomy checks and why this is one G2 defect

**G2 is primary.** The causal failure is retaining a particular existential witness B after changing a parameter on which its specified properties depend. The new parameter is selected from that same witness. The exact required implication, existential variables, witness restrictions, extra property, desired conclusion, and dependence through notation are given above.

**MP is not the primary error.** The only new use of LTB is to assert the existence of finite-range witnesses. That is a valid consequence of its stronger conclusion: globally independent widths can be chosen arbitrarily small, and their blocks satisfy the stated finite-range property. No false numerical formula or incorrectly instantiated LTB conclusion is asserted there. The final defective sentence explicitly invokes the earlier choice of B, rather than pretending to apply LTB to arbitrary widths. The old projection/intersection MP error has been removed exactly.

**G1 is not counted as a separate error.** At the surface, the universally quantified iteration range grows from [0,N0] to [0,M(B)]. The substantive reason this is illegitimate is the finite existential witness and the reversed parameter dependence. There is no additional, independent generalization elsewhere in the paper. Counting that surface range growth as a second defect would double-count the same construction.

**DEF does not fail.** The definitions of B, its interior, its projection, the torus rotation, and all multivalued iterates are unchanged and well defined. Positive widths satisfying the initial finite condition exist. The later finite cover also exists. The error is their unjustified compatibility, not a failed definition, existence, uniqueness, or recursion.

**CONV does not fail.** No algebraic transformation is changed in the paper. The explicit endpoint arithmetic above uses the unchanged rule (T1b) and derives the actual image exactly. The false step is the claim that the old witness guarantee covers the enlarged range, not a miscomputed branch formula.

## Downstream consequence and scope

The invariant-set equality K*=union_{n=0}^M T^nB remains valid for the counterexample and for the newly selected blocks, using the unchanged unique-lift and invariance argument. The next sentence is false: not every term in that union is a finite union of good blocks. Other terms can fill the isolated point's neighborhood in the total union, so this does not imply that the ultimate theorem is false.

In fact, the later two-party example correctly gives K*=[-1/2,1/2] for this irrational vote vector. The original proof establishes TB by the stronger witness choice. The candidate therefore contains a real, load-bearing proof error while preserving a true theorem, as expressly allowed by the assignment.

All material outside the prior repair and the three coordinated TB edits is byte-for-byte preserved. No bibliography, figure, stated theorem, or nonmathematical reviewer instruction was changed.

## Why it may be missed, and how to find it

The new passage has a familiar shape: choose a finite bound, make a generic finite construction, enlarge the bound by compactness, and finish a finite-union argument. The earlier fixed-neighborhood cover and the later block-interior cover look almost identical. The preceding lemma supplies much more than finite-range existence, so a reader may silently continue to remember its stronger conclusion even though the revised choice explicitly allows any finite-range witness. The retained proof between selection and conclusion is correct.

A careful reviewer can find the error by:

1. Assigning separate symbols N0 and M(B) to the two horizons and writing the exact properties of the selected B.
2. Checking that the cover in (tinv5a) uses Nhat_delta, not the arbitrarily small pi(interior B).
3. Recalling the supporting-cut warning before LTB and looking for a block whose boundary hits a tie just after its certified range.
4. Using the later two-party formula to compute the second image, including both tied branches.
5. Applying Haar-measure subadditivity to show that no allowable later cover can avoid the bad iterate.

These are plausible detection paths, not a prediction of reviewer behavior. The current benchmark success status remains untested.
