# Independent checker report

Verdict: **OK**.

I read the complete current 66-page manuscript through its supplied text extraction, revisited the operative TeX passage, read the private injection report and taxonomy, and checked the supplied Xu reference. The defect is real, substantive, and appropriately classified as G2. Historical preservation is the parent's separate responsibility; I did not consult original source or run its preservation program.

## Location and actual obligation

The altered paragraph is in Proposition 9.5, label `n10:moment-trace`, current `paper/main.tex` lines 4340–4345, page 37. Its decisive instruction is: “Fix any such realization and write $T_{p^a}$ for its trace on $U(\mathbb F_{p^a})$, for $a\ge1$.” It retains agreement with (9.1) at degree one only. The false transfer occurs in the sentence “By Lemma 9.1, for every $a\ge1$ we have” at line 4386, page 37, and drives the contradiction on page 38.

Write S_a for the original exponential sum and t_E(a) for the newly chosen trace. The specified antecedent is existence of E (and a uniform finite rank bound C) such that its signed sheaves are mixed lisse with integer weights, total rank at most C, and t_E(1)=S_1 on U(F_p). The needed consequent, under d<=r and U contained in an (n-2)-plane L, is that the second moment of this same E is O(p^{a(2n-3)}) for every a, or at least its normalized limsup at power 2n-2 vanishes. E and C are existential selection data; extension degree and extension points are universally quantified. The properties in the antecedent do not establish that consequent.

## Admissibility checked independently

Keep the standing n>=10, cubic F, and X(Q)=empty assumptions of Section 9. Take any rational linear L of dimension n-2 and V=L. This is an affine cone, geometrically irreducible, degree one and codimension two: r=d=1. No condition requires V to lie in X or a particular bad stratum. A finite partition from Lemma 9.3 has a part meeting L in a dense locally closed subset; its intersection contains an open subset of L. Restricting its lisse sheaves gives the required lissity there. Shrinking produces nonempty smooth U inside L minus zero, over Q, simultaneously for sufficiently large primes and every nontrivial character, with uniform rank. Since L is smooth and geometrically integral, its nonempty open U has those same properties; smoothness and geometric integrality spread to all sufficiently large primes. This verifies the geometric requirements of the proposition and Xu, including normality.

Fix such a prime, and use the original K restricted to U. Pull back the order-two character of Gal(Fbar_p/F_p), with geometric Frobenius -1, to U. This is a legitimate geometrically constant rank-one lisse sheaf chi. For M=n-1 define G=Qbar_l(-M) direct-sum chi tensor Qbar_l(-M). Its geometric Frobenius eigenvalues are p^M and -p^M; their absolute values at every embedding give pure integer weight 2M. Set E=K direct-sum G[-2M]. The additional cohomology occurs in even degree 2M, so its signed contribution is positive. Its rank cost is precisely two, independent of p, character, or a. It is fixed before a varies. Its weight equals its cohomological degree, so even the previously recorded weight <= degree envelope survives, and this degree belongs to the compact-support range 0 through 2(n-1). Its geometrically constant construction also descends along projectivisation and is lisse on every stratum.

The assertion uses an unspecified uniform upper bound on ranks, not a prescribed minimal numeric bound. C can bound both canonical and chosen ranks by taking R_0+2. Thus the later wording about a rank bound in the statement does not prohibit this witness.

At every extension point,

 t_E(v;a)=S_a(v)+q^{n-1}(1+(-1)^a),  q=p^a.

This proves exact degree-one agreement, and a constant additional value 2q^{n-1} for even a. The added object extends to L minus zero, so even the subsequent sum on the larger set can be interpreted; its failure is mathematical, not merely an undefined domain.

These are conditional constructions for the paper's standing contradiction hypothesis, valid for every canonical K furnished there. They do not posit an explicit ten-variable cubic contradicting the theorem being proved.

## Quantitative verification

For fixed permissible p and even a tending to infinity, N_q=#U(F_q)>=q^{n-2}/2 eventually: the excluded closed subset of the linear space has smaller dimension. Lemma 9.1 applies to the canonical S_a (the trace-composed character stays nontrivial), and positivity restricts its estimate to U:

 ||S_a||_2^2 <= B q^{2n-3}.

The added constant vector h has ||h||_2^2=4q^{2n-2}N_q>=2q^{3n-4}. Once q^{n-1}>=2B, its norm is at least twice ||S_a||_2. Hence reverse triangle gives

 ||t_E(a)||_2^2 >= ||h||_2^2/4 >= q^{3n-4}/2.

This argument permits arbitrary complex phases and all cancellation allowed by the canonical moment. The exponent exceeds 2n-3 by n-1. After the proof's normalization by q^{2n-2}, the lower bound is q^{n-2}/2 and tends to infinity. For n=10 the incompatible powers are 26 and 17.

Xu's supplied Section 3.3 defines a trace function over all finite extensions. Theorem 3.5 gives the claimed dichotomy, and Remark 3.6 extends it to mixed lisse sheaves on a normal variety. Those hypotheses hold for E. With r=1, w=n-1 and dim U=n-2, its small alternative would imply moment O(q^{2n-3}); the calculation excludes it. Thus its large alternative holds although d=r=1. The proof's asserted elimination of that alternative therefore fails for the permitted selection.

I inspected `math_verify.py` before execution. It performs only arithmetic, with no file reads/writes or history access. It passed. The sheaf existence and geometric conditions above are separate reasoning, not conclusions inferred from numerical tests.

## Classification, importance, repair, subtlety

G2 is honest as the primary classification: the introduced witness class is claimed sufficient to finish the argument, but the proof uses an additional property (full extension-trace agreement) dependent on which witness is chosen. The downstream application of Lemma 9.1 is also an MP failure, with original sums as its actual input and chosen traces as its unjustified substitution. Xu is not misstated or misapplied. G1 is a useful secondary description of extrapolating degree-one agreement, but G2 captures the selection instruction itself.

The result's statement may be recovered by choosing the canonical K. The current proof explicitly allows any realization, and the example invalidates its central large-moment elimination. Section 10 uses Proposition 9.5 to promote low-degree components to a better frequency level (page 38 example and Proposition 10.1 on page 39). This feeds the cube-free weighted estimate Proposition 10.9, the mixed-modulus saving Proposition 11.1, and the circle-method error estimate in Section 12. It is therefore a substantive proof defect rather than a typography issue.

Repair: select the actual cohomology realization of K from (9.4)–(9.5), or impose equality of the alternating traces over every finite extension (equivalently use an appropriately identical virtual sheaf class). No change of constants fixes the exponent discrepancy.

Subtlety is sufficient: the newly selected object exists, is mixed lisse of bounded rank, preserves the original weight envelope, agrees on every base-field point, and legitimately satisfies Xu's theorem. Detecting the failure requires following the extension sequence across a notation reuse and testing the subsequent moment transfer. The word “any” is an identifiable warning for a specialist, but the failure is not an overt false calculation or a broken formal statement.
