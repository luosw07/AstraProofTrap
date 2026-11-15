# Tricker report

## Exact replacements and locations

There are two text replacements, constituting one substantive mutation. The first makes the overview agree with the changed detailed procedure. The second changes the procedure and removes its now-inapplicable selected-edge observation. Each before-text occurs exactly once.

### Replacement 1: overview

Source and output lines **1304–1306**; Section 7, label **proc:quartic**, paragraph “Sharing the increases.”

Before:

~~~tex
This graph is a forest. A maximum matching pairs cuts that can be
handled together; each unmatched cut is handled by increasing one
connector.
~~~

After:

~~~tex
This graph is a forest. A maximum matching pairs cuts that can be
handled together; each unmatched cut is handled by increasing one
of its boundary edges.
~~~

### Replacement 2: correction choice and its lost restriction

Source lines **4260–4280** become output lines **4260–4273**. Location: Appendix G, label **subsec:quartic-repair-procedure**, paragraph “Selecting the paid increases.”

Before:

~~~tex
Let $M$ be a maximum matching in $K$. For each $uu'\in M$,
we satisfy both demands by choosing an edge in
$\mathcal E_u\cap\mathcal E_{u'}$ and increasing its value
from $1/4$ to $1/2$. For every demand $u$ not covered by
$M$, we increase $c_{S_u}$ to $1/2$. If an edge is chosen more
than once, we increase its value only once. \\
Let $\bar x$ denote
the vector obtained from $x^{\mathrm{init}}$ after all
objective-preserving and paid increases.

An edge of $N_H$ is increased only when it belongs to the
boundaries of two matched vertex demands. Both endpoints of such
an edge must therefore lie in $\mathcal U$.

Now consider a nonroot vertex $v$ of $G$ with one DFS child. Since every
vertex in $\mathcal U$ has two DFS children, $v\notin\mathcal U$.
Its parent edge cannot therefore join two vertex demands
and is not chosen for such an increase. All other paid
increases are on connectors, so the value on
$\rep{\operatorname{par}(v)v}$ remains unchanged. We will use this observation
later when verifying the Blossom inequalities.
~~~

After:

~~~tex
Let $M$ be a maximum matching in $K$. For each $uu'\in M$,
we satisfy both demands by choosing an edge in
$\mathcal E_u\cap\mathcal E_{u'}$ and increasing its value
from $1/4$ to $1/2$. For every demand $u$ not covered by
$M$, we choose an arbitrary edge of $\mathcal E_u$ and increase
its value to $1/2$. If an edge is chosen more than once,
we increase its value only once. \\
Let $\bar x$ denote
the vector obtained from $x^{\mathrm{init}}$ after all
objective-preserving and paid increases.

Each edge in a demand boundary is a nonroot connector or belongs
to $N_H$, so its increase has cost $1/4$ in
\eqref{eq:quartic-objective}.
~~~

The new last sentence is mathematically correct: every edge in the displayed demand boundaries is a nonroot connector or a nonremovable tree-edge representative, and each actual increase costs 1/4. No explicitly false generalization sentence was inserted. The failure is caused by allowing more repair choices and then silently reusing a later invariant proved only for the original choices.

The figure caption at source line 4970 still illustrates an execution in which unmatched demands use their own connectors. That remains an allowed special case of the changed procedure, so the figure and its caption were preserved.

## Precise G1 classification

Fix a simple, 4-regular, 4-vertex-connected graph G, a DFS tree T, its star system, the demand graph K, and a maximum matching M in K. Let a repair selection specify an edge for every matched pair and every unmatched demand. It determines the vector \(\bar x\).

Let \(\mathcal C_{\mathrm{old}}(G,T,M)\) be the selections satisfying the original rules:

1. The free changes are made only at removable parent edges of vertices in \(B_2\).
2. Each matched pair uses an edge common to its two demand boundaries.
3. Each unmatched demand u uses exactly its own connector \(c_{S_u}\).

The implication before generalization is:

\[
 c\in\mathcal C_{\mathrm{old}}(G,T,M)
 \ \Longrightarrow\
 \begin{cases}
 \text{every degree-two vertex of }H^\circ
     \text{ has both incident coordinates }1/4,\\
 \bar x^{(c)}\in\mathcal P^\circ.
 \end{cases}
\]

The downstream membership conclusion quantifies over **every cut shore \(X\subseteq W\)** and **every subset \(F\subseteq\delta_{H^\circ}(X)\)** satisfying \(|\delta_{H^\circ}(X)\setminus F|\) odd. The procedure's “arbitrary edge” also leaves the conclusion universally applicable to every allowed unmatched-edge selection. G, T, and M retain their stated hypotheses.

Let \(\mathcal C_{\mathrm{new}}(G,T,M)\) retain rules 1 and 2 but replace rule 3 by:

\[
 \text{choose any }e_u\in\mathcal E_u.
\]

This is a strict enlargement of the selected repair family. The later proof is carried forward as though

\[
 c\in\mathcal C_{\mathrm{new}}(G,T,M)
 \Longrightarrow \bar x^{(c)}\in\mathcal P^\circ
\]

and as though the degree-two invariant holds for every target selection.

It does not. A degree-two original vertex can be the child endpoint of an unmatched demand's nonremovable boundary edge. The new selection can increase that parent-edge coordinate while leaving the vertex's connector at 1/4. Such a target object fails an assumption actually used by the suppression argument. The graph below supplies exactly this target selection.

The restriction is not a decorative choice of notation: it is an endpoint condition on edges allowed to change. Changing “own connector” to “arbitrary boundary edge” does not preserve it. This is why **G1**, rather than an algebraic-conversion label, is the primary classification.

## Why the original argument is valid at this step

In the original procedure, a paid increase on \(N_H\) must be shared by two matched vertex demands. Both endpoints therefore belong to \(\mathcal U\subseteq B_2\), and both have two DFS children. The parent edge of a vertex with one DFS child cannot be changed in this way.

The free parent-edge changes also occur only at vertices of \(B_2\), so they cannot change the parent edge of a vertex with one DFS child. An original degree-two vertex in \(H^\circ\) is the split center of a nonroot star of size three. Such a center has one DFS child, its parent edge remains at 1/4, and its connector is not in any demand boundary: all demand connectors come from size-two stars. Its connector therefore also remains at 1/4.

Consequently, suppressing this vertex and replacing its two incident edges by one edge of their common value is legitimate. The argument in Proposition **lem:quartic-reduction** can transfer the relevant cut inequalities, and the later classification of small cuts is used on a vector representing the original cut problem correctly.

The original connector-only unmatched choice has this property even when the unmatched vertex demand has a nonremovable child edge incident with a degree-two vertex. It is precisely that situation which the counterexample uses.

## Exact points at which the lost restriction is used

| Use | Source line(s) | Output line(s) | Label |
|---|---:|---:|---|
| Unmatched repair choice | 4263–4265 | 4263–4266 | subsec:quartic-repair-procedure |
| First false invariant: both incident values at every degree-two vertex are 1/4 | 4316–4317 | 4309–4310 | subsec:quartic-feasibility |
| Replacement edge assigned 1/4 | 4321–4323 | 4314–4316 | subsec:quartic-feasibility |
| Equivalent cut verification proposition | 4372–4404 | 4365–4397 | lem:quartic-reduction |
| Claim that every deficient degree-three vertex cut has been raised in the reduced vector | 4505–4510 | 4498–4503 | lem:quartic-vertex-cuts |
| Claimed membership of the completed vector | 4596–4613 | 4589–4606 | prop:quartic-completed-vector |
| Membership reused in the final 13/10 bound | 5201–5214 | 5194–5207 | thm:quartic-thirteen-tenths |

The graph assumptions, star construction, demand definitions, maximum matching, paid-increase count, and arithmetic of the tour bound are unchanged. In particular, the invalid vector still satisfies the local demand and the cost bound.

## A complete admissible graph

Take \(V=\{0,1,\ldots,12\}\). The complete edge set is:

~~~text
0-1   0-5   0-9   0-12
1-2   1-8   1-11
2-3   2-5   2-9
3-4   3-10  3-12
4-5   4-10  4-11
5-6
6-7   6-11  6-12
7-8   7-9   7-10
8-9   8-10
11-12
~~~

Equivalently, its adjacency lists are:

~~~text
0:  1, 5, 9, 12
1:  0, 2, 8, 11
2:  1, 3, 5, 9
3:  2, 4, 10, 12
4:  3, 5, 10, 11
5:  0, 2, 4, 6
6:  5, 7, 11, 12
7:  6, 8, 9, 10
8:  1, 7, 9, 10
9:  0, 2, 7, 8
10: 3, 4, 7, 8
11: 1, 4, 6, 12
12: 0, 3, 6, 11
~~~

It is simple and 4-regular, with \(n=13\) and \(m=26\). The exact verifier checks that deleting any set of at most three vertices leaves a connected graph. It checks all

\[
 {13\choose0}+{13\choose1}+{13\choose2}+{13\choose3}
 =1+13+78+286=378
\]

such sets by graph traversal, with no failures. Thus G is 4-vertex-connected. This is a finite, reproducible check of the exact hypothesis, not a reliance on edge connectivity in place of vertex connectivity.

The 13/10 theorem imposes no subtour-extremality hypothesis on this graph. Its inputs are exactly the graph class and an arbitrary DFS tree. Uniform edge values 1/2 would also certify subtour value n, but no property of a separately selected subtour solution is needed for the counterexample.

## DFS and star system

Root DFS at 0 and visit available neighbors in increasing numerical order. The preorder is \(0,1,\ldots,12\). The tree edges are:

~~~text
0-1, 1-2, 2-3, 3-4, 4-5, 5-6, 6-7,
7-8, 8-9, 8-10, 6-11, 11-12.
~~~

The parent array, indexed by the vertex labels, is:

~~~text
[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 6, 11]
~~~

Every non-tree edge joins a vertex to one of its ancestors. The verifier constructs this DFS directly and checks this property when forming the stars. Thus the tree is not merely an arbitrarily chosen spanning tree.

There is one star at each center in \(\{0,1,2,3,4,6,7\}\):

| Center | Star |
|---|---|
| 0 | \(\{01,05,09,0\,12\}\) |
| 1 | \(\{12,18,1\,11\}\) |
| 2 | \(\{23,25,29\}\) |
| 3 | \(\{34,3\,10,3\,12\}\) |
| 4 | \(\{45,4\,10,4\,11\}\) |
| 6 | \(\{6\,11,6\,12\}\) |
| 7 | \(\{78,79,7\,10\}\) |

Here each pair of numerals denotes an edge, not an integer. To eliminate any possible ambiguity, the verifier output stores every edge as a two-element array.

The nonremovable edges are exactly

\[
 N=\{56,67,89,8\,10,11\,12\}.
\]

For the local witness, write

\[
 S_6=\{6\,11,6\,12\},\qquad
 S_7=\{78,79,7\,10\},
\]

and let \(z_6,z_7\) and \(c_6=6z_6,c_7=7z_7\) be their auxiliary vertices and connectors.

## Demands and an allowed modified execution

Vertex 6 has parent 5, children 7 and 11, and precisely one entering back edge \(6\,12\). That back edge comes from the subtree rooted at child 11. Thus \(6\in B_2\), its size-two star is \(S_6=S(6,11)\), and its nonremovable child edge is 67.

No other vertex belongs to \(B_2\). In particular, vertex 8 has two DFS children but no entering back edge. Therefore:

\[
 B_2=\{6\},\qquad
 \mathcal U=\{6\},\qquad
 \mathcal D=\varnothing.
\]

The parent edge 56 belongs to N, so there is no free parent-edge correction at 6. There are no other free parent-edge corrections because \(B_2\) contains no other vertices. The correction graph K has one node and no edges. Its unique maximum matching is empty.

In \(H^\circ\), the demand boundary is

\[
 \mathcal E_6=\delta_{H^\circ}(\{6\})
             =\{\operatorname{rep}(56),c_6,\operatorname{rep}(67)\}.
\]

All three coordinates are initially 1/4. The original algorithm increases \(c_6\) to 1/2. The modified algorithm permits instead the selection

\[
 e_6=\operatorname{rep}(67).
\]

Increase that coordinate to 1/2 and make no other change. This execution:

- Uses exactly the specified maximum matching.
- Uses an edge of the unmatched demand's prescribed boundary.
- Makes exactly one paid increase.
- Satisfies the demand at 6, since the new boundary sum is \(1/4+1/4+1/2=1\).
- Obeys every coordinate box bound.
- Obeys the unchanged cost count and correction budget.

The construction is therefore a permitted execution under the modified rule, rather than an arbitrary inadmissible perturbation of a certificate.

## Decisive Blossom disproof

Vertex 7 has parent 6 and exactly one DFS child, 8. Its two entering back edges are 79 and \(7\,10\). It is the center of the size-three star \(S_7\). Splitting \(S_7\) moves all three of those star incidences away from the original copy of 7. Consequently,

\[
 C=\delta_{H^\circ}(\{7\})
   =\{\operatorname{rep}(67),c_7\}.
\]

After the permitted modified repair,

\[
 \bar x_{\operatorname{rep}(67)}=\frac12,\qquad
 \bar x_{c_7}=\frac14.
\]

Choose \(F=\{\operatorname{rep}(67)\}\). Then \(|C\setminus F|=1\) is odd, so this is one of the actual Blossom inequalities of **eq:repair-nonloop-polytope**, also displayed as **eq:quartic-cut-goal**. Its left-hand side is

\[
 \bar x(C\setminus F)+|F|-\bar x(F)
 =\bar x_{c_7}+1-\bar x_{\operatorname{rep}(67)}
 =\frac14+1-\frac12
 =\frac34
 <1.
\]

Thus

\[
 \boxed{\bar x\notin\mathcal P^\circ.}
\]

For a degree-two cut with edges a and b, its two Blossom inequalities require

\[
 y_a+1-y_b\ge1,\qquad
 y_b+1-y_a\ge1,
\]

which together force \(y_a=y_b\). The modified repair destroys that necessary equality. This is not an omitted exposition step which can be filled while keeping the new arbitrary-choice rule.

The original repair \(c_6:1/4\to1/2\) leaves both coordinates in C at 1/4. The verifier independently checks every Blossom cut for the full original vector, rather than merely checking this one cut.

## Cost and downstream consequences

The baseline objective is

\[
 \frac54n-\frac12=\frac{63}{4}.
\]

Both the original connector repair and the allowed modified child-edge repair increase it by exactly 1/4. Both give objective value 16, and

\[
 16\le\frac{13}{10}\cdot13-\frac35=\frac{163}{10}.
\]

The count is also valid:

\[
 \rho=1\le\frac{13-2}{5}=\frac{11}{5}.
\]

These facts isolate the problem: the local repair and numerical budget are correct, but the alleged feasibility certificate is false.

The unchanged source assertion at lines 4316–4317, now output lines 4309–4310, says both incident values at every degree-two vertex are 1/4. It is false at vertex 7. Assigning 1/4 to its replacement edge also discards the paid increase at 67. In the reduced graph Q, the three-edge cut at the surviving demand vertex 6 then has values \(1/4,1/4,1/4\) again. The later claim that its reduced cut has been repaired is therefore false as well. These are two downstream manifestations of the same lost correction restriction.

Proposition **prop:quartic-completed-vector** nevertheless concludes \(\bar x\in\mathcal P^\circ\). The final proof of **thm:quartic-thirteen-tenths** reuses that conclusion to invoke the tour certificate bound. The computed cost of an infeasible vector cannot support that invocation.

No claim is made that this graph lacks a short tour, that the LP optimum exceeds the claimed theorem bound, or that all choices in the widened rule fail. The concrete claim falsified is that the proof's freely chosen repair vector always satisfies its asserted feasibility conditions.

## Independent finite verification

Run the self-contained verifier with Node:

~~~text
node verify_candidate.cjs
~~~

The script uses only the displayed graph, the paper's star and demand definitions, and elementary finite enumeration. It imports no mathematical library. All coordinate calculations are exact integers in units of 1/4.

It checks all 378 vertex-deletion sets needed for 4-vertex-connectivity, reconstructs the actual increasing-neighbor DFS, constructs the star system, verifies \(B_2=\mathcal U=\{6\}\) and \(\mathcal D=\varnothing\), constructs \(H^\circ\), and computes the original and modified vectors.

The auxiliary graph has 20 vertices. Fixing one vertex outside a cut shore leaves \(2^{19}-1=524{,}287\) nontrivial shores up to complementation. For each cut, the script minimizes its Blossom left-hand side over all odd choices of positive-side terms. It first takes the cheaper of \(y_e\) and \(1-y_e\) independently; if the positive-side parity is even, it changes the sign at an edge with minimum absolute difference. This exactly computes the minimum over \(|C\setminus F|\) odd, including equal-cost ties.

The observed results were:

~~~text
Vertex deletions checked by size: [1, 13, 78, 286]
All resulting graphs connected: true
B2 = U = [6]; D = []
K vertices = [6]; K edges = []; maximum matching = []
Original objective = 16
Modified objective = 16
Original: 524287 cut shores, minimum Blossom LHS = 1,
          0 violated cuts
Modified: 524287 cut shores, minimum Blossom LHS = 3/4,
          4 violated cuts
First modified witness shore = [7]
~~~

The single explicit inequality at vertex 7 is sufficient for the disproof. Exhaustive cut checking additionally confirms that the original selection succeeds on this exact instance and that the new selection creates an actual formulation failure.

## Why the defect is subtle and how to find it

The changed rule looks natural because each listed boundary edge initially has value 1/4, raising any one of them repairs that demand, and every listed choice has the same cost. The matching argument and its cardinality bound continue to work. A review focused on local cut repairs and the paid-correction count can therefore accept the replacement without seeing any numerical warning.

The special benefit of the original connector choice is elsewhere: it prevents nonremovable edges from being increased at endpoints outside \(\mathcal U\). That condition protects original vertices with one child when the graph is later reduced. The modified paper no longer announces that restriction, and the later proof continues with the inherited common-value assertion. The resulting global membership claim appears hundreds of source lines after the altered rule and is reused again in the final theorem proof.

A careful reviewer can find the defect by:

1. Tracking exactly which nonremovable edges can increase, including those chosen for unmatched demands.
2. Checking both incident values at every vertex that is about to be suppressed.
3. Writing the two Blossom inequalities on a degree-two cut; they force equality of its incident coordinates.
4. Testing a vertex demand whose nonremovable child is a size-three-star center, as in the explicit graph.
5. Checking whether a correction that is valid before suppression remains represented by the claimed reduced vector.

Restoring the connector-only choice would fix this mutation. Alternatively, a broadened choice rule would need an additional proved condition excluding changes that destroy the degree-two equalities. Either repair changes the substantive allowed selection rule; it is not a harmless notational correction.
