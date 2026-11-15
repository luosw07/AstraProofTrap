ACCEPT

No substantive mathematical error was found in my independent review of the supplied current paper. This verdict means no error was found in this review; it is not formal verification, nor an independent certification of the external formalizations mentioned in the paper.

## Scope and method

I read all 7,270 lines of the standalone paper.tex, in bounded consecutive chunks, including the introductory statements, all appendix arguments, the figure source and captions, the bibliography, and the final supplementary and methodology sections. The mathematical source was exclusively this paper. I did not consult another version, external sources, other workspace materials, other agents, or a formal proof assistant. I used the TeX rather than separately inspecting the PDF rendering.

I checked the actual arguments, including parity conditions, the dependence of the final constants on earlier estimates, and the distinctions between an integral tour construction and a fractional certificate. I also performed finite calculations on the explicit example specified in the paper, as described below.

## Findings on the principal arguments

1. **Degree-bounded joins and the two LPs** (Theorem `thm:bounded-T-join`, lines 1774–1831; appendices on the two LPs, lines 1879–2440). The slack-loop reduction correctly uses parity-compatible degree bounds. The singleton blossom inequality supplies the lower bound needed at odd-demand vertices when filling the degree deficit with loops. Contracting the star connectors correctly transfers odd-degree parity back to G. The reconnection argument retains a connected spanning subgraph after adding two copies of one edge from each fully selected star. Maximizing the loop variables gives precisely the displayed maximum-of-two-affine-terms objective; its tour guarantee follows from integrality of the extended polytope, not from an unwarranted assertion that minimizing a convex function over the join polytope attains an integral point.

2. **DFS removable stars** (`lem:DFS-removability`, lines 2851–2969). The minimum-depth back-edge argument correctly forces a second cycle edge into the same star. Keeping one edge of each star and all nonremovable edges then leaves an acyclic graph with n−1 edges, so the connectivity conclusion and the counting identities follow.

3. **Circulation comparisons** (lines 2974–3564). The support-restoration accounting and the parity extension by omitted edges are consistent. In the comparison with optimized MS parity correction, each fully selected star is charged to a distinct selected tree edge that is removable in the star construction but unpaired in the MS construction. The two-unit saving on each such edge pays for the possible reconnection. I found no reversal of an optimization inequality or conflation of optimized parity cost with the circulation estimate in these proofs.

4. **The 13/10 bound for quartic, 4-vertex-connected graphs** (`thm:quartic-thirteen-tenths`, lines 3744–3757; proof material through line 5213). I checked the suppression argument, classification of cuts of size at most three, identification of the deficient singleton and triangle cuts, and the matching-based correction count. In particular, deleting s connector centers and at most 3−s original edges leaves a connected graph by the stipulated vertex connectivity, which justifies the small-cut classification. The three sharing cases give an acyclic correction graph. The independent-set estimate and the disjoint vertex/edge counts give 5ρ≤n−2, and the resulting objective arithmetic is 5n/4−1/2+(n−2)/20=13n/10−3/5.

5. **The 4/3 bound for k-connected graphs of maximum degree k+1** (`thm:k-connected-four-thirds`, lines 5244–5432). The reciprocal back-edge assignments satisfy the auxiliary degree bounds. For a blossom cut with one edge outside F, the expanded-tree cases provide the needed complement-capacity bound. The use of connectivity of G−u for a connector cut has two nonempty shores because u is nonroot. The resulting objective is 4n/3−2/3.

6. **The general 89/64 bound** (`s12pair:theorem`, lines 5477–5493, with supporting arguments through line 7011). I checked the minimum-cut connector completion, its cut-symmetric-difference argument, the connector estimates, the lift of the half-subtour point, and the local charge calculation. The cut-exchange argument removes a connector without removing the offending edge because the latter has strictly larger complement than every edge of the witness cut other than that connector. The scalar estimate uses the identity (t+1)^2−16(t−3)=(t−7)^2. In the successor-star case the residual 1/64 is correctly absorbed by t_S/64 since every star has at least one back edge; the successor need not be positive. The per-vertex additional charge is bounded by η_v, including when several stars share the center. Finally the root contribution is bounded by 1+5η_r/8, and its η_r terms cancel against the nonroot aggregate, giving exactly 89n/64+9(L−n)/8−13/16. The L=n specialization follows from the stated formulas.

## Independent finite checks of the comparison example

For the 23-vertex, 30-edge graph specified in lines 2458–2506 and 2551–2699, I reconstructed the edges, fractional values, stars, and retained MS support directly from the paper's TeX.

- Enumerating all 256 elements of its eight-dimensional cycle space, and taking complements to obtain all odd(G)-joins, gave StarDeletionLP optimum 28 and StarReconnectionLP optimum 27.
- Restricting to the stated MS support and fixed pairs gave optimized MS parity cost 29.
- I checked all 4,194,303 nontrivial cuts with a fixed vertex excluded. The displayed vector has minimum cut value 2, total value 26, and 35 tight cuts whose incidence vectors have rank 30. Thus these computations corroborate its feasibility and extremality as well as the stated LP comparison values.

These are finite arithmetic checks, not formal certificates. I did not separately derive an exact dual certificate for the claimed subtour optimum 26 or independently optimize the circulation cost.

## Limitations and supplementary claims

The paper invokes standard external results, notably the b-factor description, circulation integrality, sparse extreme support, the support-preserving box-constrained subtour reduction, and the standard block reduction. I checked their use and compatibility with the hypotheses in this paper, but did not read or reprove the cited literature. In particular, the reduction used at lines 790–793 and 5463–5475 is taken as the cited supporting fact, rather than independently established here.

The stronger numerical ratios in the discussion and Table `tab:discussion-results` (lines 1339–1377) depend on external Lean material. The paper expressly states that their complete proofs and combined analysis are not supplied. I read the supplementary circulation and laminarity material at lines 7017–7235 and found no contradiction in the displayed constructions or estimates, but I have not independently established the stronger ratios 14524/10481, 9/7, and 41944/31181 from the supplied text. They are not used to prove the main 89/64, 13/10, or 4/3 results reviewed above. My acceptance should not be read as certification of those external formalizations or stronger ratios.

There are no substantive issues to locate or classify as affecting a claimed main conclusion. The review does not claim exhaustive detection of every typographical or expository defect.