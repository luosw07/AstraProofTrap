ACCEPT

I found no substantive mathematical error or unjustified inference affecting a claimed conclusion in the current paper.

Scope and independence

I read the complete supplied paper.tex, lines 1–9078, including its definitions, proofs, examples, remarks, figure source, and bibliography, in sequential bounded chunks without output truncation. I also opened the matching 96-page paper.pdf, checked its title and contents and selected passages, and visually inspected page 68, containing the two explicit polygon illustrations. The TeX was the primary source for the mathematical review; I did not visually inspect every PDF page. I used no other version, external mathematical source, other review, or formal proof assistant.

Main mathematical assessment

1. Discrepancy and sharpness (Sections 3–4; lines 1693–2440).
The moving sets A_t and their average-score induction establish the harmonic upper bound. The equality analysis correctly propagates equality backward through the inequalities. The fixed-vote sharpness construction preserves the older candidates’ relative scores, delays the new candidate until the prescribed complete tie, and then recovers the earlier large discrepancy with the additional harmonic increment. Its preliminary perturbation argument is valid for the finite itinerary: conditional on the same previous winners, the score perturbation at time t is t times the perturbation of the vote vector, so ties are broken in the prescribed direction. The loss function L(t), the lower bound on the elapsed time between last wins, and the accumulated leakage into excluded candidates justify the near-equality restrictions. The probability estimate and the strict fixed-vector supremum follow from these restrictions.

2. General dynamics, rational parameters, and torus factor (Sections 5–6; lines 2444–3104).
The boundedness and uniform absorption arguments use positivity of every vote proportion, which is expressly imposed at lines 2452–2453. The backward-invariance argument for the multivalued limit set correctly uses compactness and finitely many possible predecessors rather than assuming continuity of the map. The description of the torus orbit closure and its dimension is consistent with rational independence and the identity sum p_i = 1. The rational-case theorem proves exact period Q only for the specified initial region. For arbitrary initial states the paper correctly retains the weaker divisibility statement and labels period Q as an open problem; it does not incorrectly infer it from the torus factor.

3. Ergodic attractor and invariant measure (Section 7; lines 3107–4372).
The multiplicity lemma correctly discards the projected null set of ties before comparing fibre sizes. The small neighbourhood of zero has a unique lift in the absorbing set, which supplies the synchronization and finite-time absorption used in the attractor proof. The uniqueness-of-measure argument establishes concentration on the compact attractor and then uses almost-everywhere uniqueness of the lift; it does not assume that a factor map alone determines the measure. The weak-convergence argument uses compact sets and the Portmanteau inequalities in the correct direction.

The good-block lemma deserves particular attention. Its tree of independent difference normals and the final coefficient comparison rule out a supporting cut that leaves a nonempty lower-dimensional piece. The treatment of the integer in the rational relation at lines 4187–4201 correctly uses sum p_i = 1 and the zero sum of the difference coefficients. Consequently the full-dimensional polyhedral result supplies the missing support equality, and the conclusions about every branch limit set then follow.

4. Intermediate parameters, bias, and two parties (Sections 8–10; lines 4375–5023).
The intermediate-case theorem explicitly assumes that ties have zero measure on the limit set. Its proof uses Haar measure on the appropriate coset rather than ambient Lebesgue measure. The examples correctly distinguish backward invariance from forward invariance and do not extend the ergodic conclusion without its hypotheses. The bias theorem applies weak convergence to a bounded continuous extension of the coordinate function, justified by boundedness of the orbit. The two-party reduction and rounding description agree with the one-dimensional update.

5. Planar construction and Farey geometry (Section 11; lines 5024–8743).
I checked the planar change of variables and the winner-sector inequalities, the Farey rectangle coordinates, the first-entry coding, the permutation ordering the orbit points, and the construction of the upper and lower paths. The invariant-domain argument uses the g-line sections and treats the middle piece separately. The boundary assertion at lines 6869–7036 does not rely on an invalid blanket claim that set-valued forward invariance survives Hausdorff limits: it separately verifies the extra tied segments and obtains backward invariance by convergent preimages.

The wall equations follow from the lower-path vertices, with the exceptional vertices handled explicitly. The vertex count accounts for whether the cut occurs on an edge or a vertex. In the global wall theorem, the even-wall denominator cutoff and the odd-wall parity/determinant argument justify the endpoint formulas. The adjoint pairing then follows by direct substitution into those formulas.

6. Other divisor methods (Section 12; lines 8747–8887).
The uniform shift by beta and the weighted winner rule give the stated recursion. The later planar change of variables and its three linear forms are algebraically consistent. The remaining statements about its invariant polygons are expressly presented as expectations or questions, not established conclusions.

Supplementary calculations

These were checks derived solely from the formulas in the supplied paper, not substitutes for the proofs.

- I constructed 414 sample polygons across all reduced fractions with denominators 3–30. At these parameters, their computed areas were 1, their vertex counts were 4v+3, and the images of every constructed vertex under every applicable winner branch remained in the polygon.
- I independently computed polygon centroids and the resulting bias at one parameter in each of S_{1/2}, S_{1/3}^{(1)}, S_{1/3}^{(2)}, and S_{1/3}^{(3)}. They agreed with the displayed formulas at lines 4779–4829 to floating-point roundoff (maximum errors below 9 × 10^-17).
- With exact rational arithmetic, I checked 3652 active wall descriptions across every Farey cell with denominator 3–60 against the stated first-wall slope, parity, and endpoint cutoff.
- With exact rational arithmetic, I checked 364 odd-fraction/even-child pairs through odd denominator 59 and obtained the claimed common endpoints.

Issues and limitations

I have no substantive issue to report and found no mathematical typo requiring a correction to a claimed result. Some geometric verifications are abbreviated in the text, especially in the introductory S_{1/2} construction, but the explicit coordinates and the later general construction supply enough information to check those steps; I did not regard these abbreviations as an unjustified inference.

This is an independent mathematical review, not formal verification. The finite calculations above do not establish the unrestricted results. I did not independently verify bibliographic or historical assertions against the cited works, and I did not inspect every rendered PDF page. My acceptance means that no substantive mathematical error was found within this review.
