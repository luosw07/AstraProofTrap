VERDICT: REJECT

# Referee report

The manuscript proposes an unramified quantum geometric Langlands equivalence for every connected simple complex group, with its actual global form, and every irrational complex shifted level. I read the complete LaTeX manuscript, including its references, and followed the argument from the boundedness and duality constructions through deformation, the relative local comparison, the period calculation, and the final equivalence. My verdict concerns the current proof: there is a specific error in its construction of infinitesimal transport on the compact presentations. That construction supplies the coherent family comparisons used in the main theorem.

## Substantive issue: the proposed transport of jet representations does not preserve the relations

**Location.** Section “Loop categories over moving divisors,” subsection “Infinitesimal transport and the strong loop action,” Proposition `loop:crystal`, specifically TeX lines 4333–4343. The coefficient convention is introduced at the beginning of the same section.

**Locating quotation.** “Obtain the lifted inducing representations … by retaining their jet-current action matrices in the monic coefficient bases, and then restrict to the common depth. The PBW and group-cobar constructions therefore use identical coefficient diagrams, so the resulting comparisons intertwine induction and their compositions agree there.”

The displayed procedure is not a transport of representations. The monic coefficient identifications are linear identifications, whereas the multiplication in the jet coefficient algebra changes with the divisor. Keeping the matrices in those bases therefore need not preserve the current Lie algebra relations. This already fails for two points and a first-order infinitesimal displacement.

Here is an explicit calculation, entirely in the setting of the proposition. Use the curve coordinate z and a two-point divisor with equation

\[
P_t(z)=z(z-t).
\]

Compare the two lifts t=0 and t=epsilon over

\[
R=\mathbb C[\epsilon]/(\epsilon^2).
\]

Their first jet coefficient algebras are

\[
A_0=R[z]/(z^2),\qquad
A_\epsilon=R[z]/(z^2-\epsilon z).
\]

Both have the prescribed monic basis 1,z. But their multiplication relations are respectively z^2=0 and z^2=epsilon z. Thus the linear map retaining coefficients in this basis is not an algebra homomorphism.

Take G=SL_2. There is an algebraic representation of the first jet group for A_0 on

\[
W=\mathbb C^2\otimes A_0,
\]

namely the standard representation over A_0, viewed as an R-module. Write N for multiplication by z on A_0; in the basis 1,z,

\[
N=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad N^2=0.
\]

Its current Lie action is

\[
x\otimes1\longmapsto x\otimes I,
\qquad x\otimes z\longmapsto x\otimes N.
\]

This is a legitimate locally free algebraic inducing representation of the type allowed in (L2). Retain these jet-current matrices as prescribed. For x,y in sl_2 with [x,y] nonzero, the commutator of the proposed matrices is

\[
[x\otimes N,y\otimes N]=[x,y]\otimes N^2=0.
\]

But in the displaced jet current algebra the bracket is

\[
[x\otimes z,y\otimes z]
 =[x,y]\otimes z^2
 =\epsilon[x,y]\otimes z.
\]

Its proposed action is epsilon[x,y] tensor N, which is nonzero on the free R-module W. The claimed lifted representation therefore fails the Lie relation. The determinant extension does not affect this example: it splits on regular arcs, and the failure is in the ordinary current bracket.

The issue is also visible before taking the first jet quotient. With u_0=z^2 and u_epsilon=z^2-epsilon z, the canonical identification of the full completed rings at fixed z satisfies

\[
u_\epsilon=u_0-\epsilon z.
\]

Consequently, transport by the identity of the absolute formal curve must change the matrix for this mode. It cannot retain all matrices in the two monic bases. Cofinality of the divisor ideals, correctly proved at lines 4298–4309, gives an identification of completed rings; it does not make the coefficient-retention map multiplicative.

**Why the subsequent sentences do not fix this.** Restriction to a common deeper subgroup is a functor on representations that already exist. It does not turn a failed Lie representation of the displaced jet algebra into an inducing representation of that algebra. One can instead transport a module through the identity of the completed absolute algebra and allow its finite level to deepen. In the example, this gives a nonzero action of u_epsilon, namely -epsilon times the action of z. That is a different procedure from retaining the matrices in the monic bases. The assertion that the PBW and cobar coefficient diagrams are identical consequently requires a new verification with these correction terms.

**Consequences.** The quoted paragraph is the asserted construction of compatibility with induction and of the higher cocycle identities on multiple infinitesimal diagonals. The preceding agreement of integrability conditions describes possible essential images; it does not verify the claimed matrix-level construction or its compatibility with the inducing functors. Thus Proposition `loop:crystal` has a substantive gap in the form used subsequently. The strong loop action and parameter-operation assertions depend on it. So do the relative Skryabin comparison, the common target over colliding points, the coherent local pairing comparison, and ultimately the family-compatible global period identity. The final formal equivalence argument uses those comparisons, so the main theorem has not been established by the current argument.

**Possible repair.** Replace coefficient retention by an explicit transport through the identity of the completed absolute curve. On common sufficiently deep levels, construct the transported modules with the resulting changes in all current operators, and prove that this construction preserves the compact presentations. Then construct the comparison for induction and the mapping complexes using these corrected operators, and verify composition on triple and higher infinitesimal diagonals. The example above is a basic required check. It may be possible to use the equality of full completed arc algebras to carry this out, but the finite jet matrices cannot be declared unchanged in the stated bases.

## Other principal checks

I checked the shifted-level arithmetic: with a=-c and d=1/(ra), the source exponent differs from the stated convention by the integral determinant twist, while the target exponent has the required negative reciprocal shifted level. Irrationality also gives non-torsion Kummer monodromy for non-real parameters, as required by the deformation argument.

I examined the HN cutoff and its central-weight test, the role of opposite twists in categorical duality, and the distinction between star and shriek diagonal kernels. I followed the finite-stage rank argument and the logarithm colimit argument, including the use of a common degreewise weight bound rather than merely a zero special-fiber colimit. I checked the structure of the weight estimate through label cancellation, the spectral degree bound, collision codimension, and simplicial degree. I also followed the low-degree unit-gap argument across divisors, the normalization identities for changing semi-infinite lattices, and the two insertion comparisons in the Ran period calculation.

Conditionally on the preceding comparison results, the final construction of the two inverse candidates is formally consistent: one produces a left inverse and the other a right inverse, and their identification follows by composition. The central-sector formula and torsor signs are consistent with the sign convention stated in that final section. These checks isolate the objection above to an indispensable earlier family-construction step rather than to the final inverse-functor manipulation.

The external references were considered only as presented in the manuscript; no external papers, historical versions, other reviews, or experimental materials were consulted. The review was conducted from the full TeX source; I did not perform a separate visual-layout review of the PDF.

## Typographical issues

I have no ordinary typographical issue to report that affects the verdict. The current objection concerns representation relations and the construction of coherent functors, rather than notation or formatting.
