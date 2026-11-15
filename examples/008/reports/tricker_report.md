# Tricker report

## Exact edit and source locations

File: `paper/main.tex`, line 1866.

Stable context: `subsec:proof-greedycount`, proof of Theorem `thm:greedycount` (Theorem 4.1), under “Validity of the completed stages,” between Claim `clm:greedy-orders` (Claim 4.5) and Claim `clm:greedy-remainder-iteration` (Claim 4.6). The affected prescribed degree and codegree sequences are `eq:greedy-degree-recurrence` (4.9) and `eq:greedy-codegree-recurrence` (4.10).

The altered sentence and the resulting false codegree inference are on printed page 30 of the supplied original PDF. The regular-completion construction invoked there is Lemma `lem:completion` (Lemma 4.2), on printed page 21. These are original-PDF page references; the parent handles compilation.

Original quotation:

```tex
Lemma~\ref{lem:completion} fills the deficits to this prescribed integer, so $D_{i+1}$ is the same for all good completions at stage $i$.
```

Altered quotation:

```tex
Use the construction of Lemma~\ref{lem:completion} with $Q$ the least prime power at least $\max\{D_{i+1},k-1\}$ to fill the deficits to this prescribed integer, so $D_{i+1}$ is the same for all good completions at stage $i$.
```

The complete one-line patch is `minimal.diff`.

The distant restriction in the unmodified proof of Lemma 4.2 is:

```tex
Otherwise choose a prime $Q=O_k(D)$ with $Q\ge\max\{D,k-1\}$.
Choose $A\subseteq\mathbb F_Q$ of size $D$.
On $\{0,\ldots,k-2\}\times\mathbb F_Q$, the sets
\[
    \{(j,b+ja):0\le j<k-1\},
\]
indexed by $b\in\mathbb F_Q$ and $a\in A$, form a linear $D$-regular $(k-1)$-uniform hypergraph with $a_0=DQ$ edges.
```

The unchanged inference following the altered sentence, at source line 1881, becomes false for the objects selected by the new rule:

```tex
It also bounds the completed codegrees, since $L_j^{(i+1)}\ge1$ and Lemma~\ref{lem:completion} preserves every upper bound of at least one on the maximum $j$-codegree.
```

## Why the field choice matters

In the original construction, two vertices in distinct coordinate positions j and h give the equations

\[
b+ja=x,\qquad b+ha=y.
\]

Subtracting gives

\[
(j-h)a=x-y.
\]

For a prime Q≥k−1, the distinct integers j,h in {0,...,k−2} have nonzero difference in F_Q, so this equation determines at most one slope a and then one intercept b. This establishes the required linearity.

A field of prime-power cardinality Q can have much smaller characteristic. The inequality Q≥k−1 does not ensure that those integer coordinates are distinct as field scalars.

Specifically, take k=4 and D=Q=2^r with r≥2. The least prime power at least max{D,3} is exactly Q=D. Since the slope set must have size D, it is A=F_Q. The retained expression gives the auxiliary edges

\[
E_{a,b}=\{(0,b),(1,b+a),(2,b+2a)\}
       =\{(0,b),(1,b+a),(2,b)\},
\]

because 2a=a+a=0 in characteristic two. For a fixed b, all Q distinct slopes give distinct edges containing the same pair

\[
\{(0,b),(2,b)\}.
\]

Thus that pair has auxiliary codegree Q=D, rather than at most one.

This uses the paper's actual formula with integer j. The integer scalar 2 denotes repeated addition in the field. No representation of F_Q changes 2a=0. Replacing those scalars with separately chosen distinct field elements would be a different construction; the altered paper retains the original formula.

When the paper appends an old vertex to each auxiliary edge, every one of these Q edges retains the two new vertices. Distinct edge labels append vertices in distinct old copies, so the Q extended edges remain distinct. Taking 2k disjoint copies afterwards also retains the codegree. Each degree-deficit stub therefore creates a new pair of codegree D.

## A witness inside the actual normalized iteration

The preceding collision is a local finite-field calculation. The following family ensures that the new rule selects precisely such a field in an actual first stage satisfying all the paper's ambient assumptions, including even the stronger main-theorem assumptions.

### Choosing an admissible initial hypergraph and its degree

Fix k=4. Let c>0 be the fixed constant used in the degree recurrence (4.9), after the proof has chosen it sufficiently large. The separate constant in the codegree recurrence may be any fixed positive constant as well. Let p tend to infinity through primes, with p>3, and write

\[
n=8p,\qquad \ell=\log(8p+2).
\]

Let Q_p be the smallest power of two at least p/32. Thus

\[
\frac p{32}\le Q_p<\frac p{16}.
\]

For integers d in [ceil(p/16),p], consider

\[
F_p(d)=\frac d8+c\ell\sqrt d.
\]

For all sufficiently large p,

\[
F_p(\lceil p/16\rceil)<p/64<Q_p,
\qquad F_p(p)>p/8>Q_p.
\]

Moreover,

\[
0<F_p(d+1)-F_p(d)
=\frac18+\frac{c\ell}{\sqrt{d+1}+\sqrt d}<1
\]

uniformly in this range for large p. Consequently ceil(F_p(d)) is an increasing integer sequence whose increments are zero or one, and it assumes every integer between its endpoint values. Choose d=d_p in this range such that

\[
\left\lceil\frac d8+c\ell\sqrt d\right\rceil=Q_p. \tag{W1}
\]

This specifies an available degree with d=Θ(p), for every fixed value of the recurrence constant c.

Choose a set A_0⊆F_p of size d, and form a 4-uniform hypergraph on {0,1,2,3}×F_p whose edges are

\[
\{(j,b+ja):0\le j\le3\},
\qquad a\in A_0,\ b\in\mathbb F_p.
\]

Take two vertex-disjoint copies of this hypergraph and call their union H_0. Here the field order p really is prime and p>3. For each vertex and each slope a there is exactly one intercept b, so H_0 is d-regular. Two vertices in different coordinate positions determine at most one edge by the subtraction argument above; two vertices in the same position belong to no edge. Hence H_0 is simple and linear, with n=8p and

\[
\Delta_2(H_0)=\Delta_3(H_0)=\Delta_4(H_0)=1.
\]

All ambient conditions hold:

- k=4 is an allowed fixed uniformity, and 2k divides n.
- d=Θ(n), so the polynomial-degree requirement holds.
- The iteration's initial values are L_j^(0)=1 for j=2,3,4.
- The parameter is Γ(H_0)=d^(−1/2)+d^(−1/3)=O(p^(−1/3)), so Γ(H_0)(log n)^L→0 for every fixed L.
- The intersection coefficients are zero by linearity. For example, with ε=1/24, Γ(H_0)/(d^(−1/4)n^(−ε))=O(p^(−1/24))→0, and d≥n^ε for large p. Thus Theorem 1.6's stronger hypotheses also hold.
- Choose activity λ=1, within the required range for every fixed C_0>0.
- For sufficiently large p the stopping scale T is at least two, so a second completed stage is required by the stated iteration.

### The first residual has genuine degree deficits

At stage zero, the pair-codegree hypothesis of Theorem 4.3 is

\[
\frac{L_2^{(0)}(\log n)^5}{D_0}
=\frac{(\log(8p))^5}{d}\longrightarrow0.
\]

The unchanged Theorem 4.3 and Lemma 4.5 therefore provide good trajectories with probability at least 1/2 for large p. Any good prefix has m=n/(2k)=p edges and leaves a residual F on n/2=4p vertices. It remains linear. The first-stage degree estimate gives, uniformly over its vertices,

\[
d_F(v)=d/8+O(\sqrt{d\log n}).
\]

Equation (W1) makes the prescribed completed degree

\[
D_1=Q_p=\left\lceil d/8+c\ell\sqrt d\right\rceil.
\]

Since ℓ/sqrt(log n)→∞, for every good residual and every vertex v,

\[
D_1-d_F(v)>0
\]

for all sufficiently large p. Therefore the deficit sum S is positive, so the nontrivial auxiliary-field construction is used. All hypotheses on F and D_1 in Lemma 4.2 are satisfied; in particular Δ_2(F)≤1 and max_v d_F(v)≤D_1.

### The newly prescribed completion violates the next codegree bound

The altered instruction chooses the least prime power at least max{D_1,3}. Since D_1=Q_p is a power of two tending to infinity, it chooses

\[
Q=D_1=Q_p.
\]

The slope set is the whole field. The preceding characteristic-two calculation therefore applies to every deficit stub. At least one stub exists, so the produced H_1 has a pair of new vertices contained in D_1 distinct edges. It is still D_1-regular, giving also the reverse upper bound on any pair codegree. Thus

\[
\Delta_2(H_1)=D_1=Q_p=\Theta(p). \tag{W2}
\]

But the unchanged deterministic recurrence (4.10), with k=4 and L_2^(0)=L_3^(0)=1, gives

\[
L_2^{(1)}=\frac14+C_4\ell^{-2}+C_4\ell^4
=O(\ell^4)=o(Q_p). \tag{W3}
\]

Equations (W2) and (W3) contradict the retained claim that the recurrence bounds the completed codegrees. This failure holds for **every** good first prefix, every permitted edge labeling, and every attachment of its deficit stubs. In particular, choosing a prefix attaining the minimum in Lemma 4.6 does not avoid it.

The next invocation of the short-trajectory estimate also fails its actual pair-codegree hypothesis: the produced H_1 has Δ_2(H_1)/D_1=1, whereas that hypothesis requires Δ_2(H_1)(log N_1)^5/D_1→0.

## Instantiated MP audit

**Established result invoked.** Lemma 4.2 supplies a regular completion with controlled higher codegrees, and its proof supplies a particular explicit construction using a prime field order Q. The changed instruction invokes that construction and the unchanged following paragraph applies its codegree-preservation conclusion.

The abstract existence statement of Lemma 4.2 remains valid. Its existence conclusion provides a completion satisfying its listed properties. It does not designate every modification of the construction as such a completion. The present issue is applying the proven construction's guarantees to the specifically selected, modified output H_1.

**Objects.** In the family above, F is any good first residual of H_0; D=D_1=Q_p; S=sum_v(D_1−d_F(v))>0; Q is now the least prime power at least max{D_1,3}, namely Q_p=2^r; A=F_Q. H_1 is obtained by labeling the DQ auxiliary edges, appending the designated old vertex for every stub, and taking the final 2k copies.

**Instantiated antecedent of the construction guarantee.**

\[
\begin{gathered}
k=4,\quad F\text{ simple and 4-uniform},\quad
\Delta(F)\le D_1,\quad D_1\in\mathbb Z_{>0},\quad S>0,\\
Q\text{ prime},\quad Q\ge\max\{D_1,3\},\quad
A\subseteq\mathbb F_Q,\ |A|=D_1,\\
\text{the auxiliary edges and attachments follow the displayed recipe.}
\end{gathered}
\]

For the constructed objects, all these conditions except “Q prime” hold. The selected Q is a power of two with exponent at least two, and hence has characteristic two while Q>2. The original reason that distinct coordinate positions give distinct field scalars fails at the pair of positions 0 and 2.

**Instantiated consequent being used.** The output is supposed to be a simple D_1-regular 4-uniform hypergraph containing a=O(D_1^2) copies of F, with w/a=3S/D_1 and 8 dividing its order, and in particular

\[
\Delta_2(H_1)\le\max\{\Delta_2(F),1\}=1.
\]

That last conclusion is false: the exact value in (W2) is D_1>1. The further invoked consequent Δ_2(H_1)≤L_2^(1) is also false by (W3).

For completeness, the other structural conclusions do survive in this witness. The auxiliary edges are distinct because their coordinates 0 and 1 determine b and a. Each new vertex has degree D_1, and the stub rule makes every old vertex have degree D_1. Each added edge contains exactly one old vertex. The original counts of copies and new vertices, the divisibility operation, and the matching encoding remain valid. The loss of pair-codegree control is the single root fault.

## Secondary DEF audit

**Introduced object and defining construction.** The iteration defines each next hypergraph by the earlier completion recipe, now with Q explicitly prescribed as the least eligible prime power. The degree and codegree sequences remain the original deterministic sequences (4.9)–(4.10).

Required conditions have the following status:

- **Existence and uniqueness of Q: established.** Prime powers are positive integers with an eligible least member. A power of two between the lower threshold and twice that threshold also shows Q=O_k(D_{i+1}).
- **Existence of the field and slope set: established.** A field exists for a prime-power order, and Q≥D_{i+1} allows a slope set of that size. In the witness Q=D_1, so that set is forced to be the entire field.
- **Well-definedness of field expressions: established.** Integer scalar multiplication j a is repeated field addition. The expression 2a=0 is well-defined and is exactly the source of the collision.
- **Existence of the finite output: established.** The auxiliary edges, edge labels, copies, and stub attachments can all be formed. No failure of existence or ambiguity is needed for the witness.
- **Uniqueness of the entire output: not required by the paper.** Its construction permits labels and other choices. No assertion of a canonical isomorphism type is used.
- **Independence of the diagnosis from those choices: established.** Each fixed intercept b gives the same shared new pair for every slope, and appending old vertices cannot remove that pair. Relabeling the auxiliary edges and taking disjoint copies preserve its codegree.
- **Required output codegree property: failed.** The constructed H_1 has Δ_2(H_1)=D_1, exceeding both the purported preservation bound and L_2^(1).
- **Validity of the inductive invariant: failed at the first completion.** H_0 satisfies every initial bound, but H_1 fails the codegree invariant needed to repeat the stage. The later numerical estimates for the deterministic sequences remain estimates of sequences; they do not bound the actual constructed hypergraph.

## Significance and subtlety

The normalized iteration requires completions whose pair codegrees stay small relative to their regular degrees. The edit preserves the degree, size, deficit count, activity range, and normalization calculations, while the produced first completion has a pair codegree equal to its full degree. The stated application of the next short greedy stage therefore loses a central hypothesis. This is also a direct false local bound, rather than only an unsupported applicability concern.

The hidden distinction is between field cardinality and field characteristic. Using a least prime power still gives an existing field and the same O_k(D) size control. The lost restriction is nine pages earlier in the explicit completion recipe, and the degeneracy is invisible in the displayed k=3 illustration, whose coordinate positions are only 0 and 1. It appears at k=4, where position 2 is used. The restored martingale argument remains untouched and valid.

The correction would be to retain the original prime choice, or to redesign the recipe using explicitly chosen distinct field evaluation points. The supplied altered paper makes neither change; it continues to use the integer-coordinate formula.
