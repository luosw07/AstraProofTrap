# Checker report

**Verdict: OK. Primary category: MP (applying an established result).**

I reviewed the current paper's context, including the counting, entropy, application and appendix arguments, the private taxonomy and injection log, and the altered TeX passage. The injected error is genuine, substantive, subtle, and correctly classified. The witness works under the actual iteration assumptions.

## Exact location

In the current rendered paper, printed page 30, proof of Theorem 4.1, “Validity of the completed stages,” between Claims 4.5 and 4.6, the instruction is: “Use the construction of Lemma 4.2 with Q the least prime power at least max{D_{i+1}, k−1}.” This is `paper/main.tex:1866`, within `subsec:proof-greedycount`. The subsequent paragraph falsely concludes that (4.10) bounds the completed codegrees. The governing recurrences (4.9) and (4.10) are on page 28. The invoked regular-completion lemma (`lem:completion`) and its explicit integer-coordinate construction are on page 21.

## Independent verification of the local fault

The proof of Lemma 4.2 chooses a prime Q and uses auxiliary edges {(j,b+ja):0≤j<k−1}. Its pair uniqueness argument depends on invertibility of j−h for distinct coordinate positions, not merely on the cardinality of the field. The prime hypothesis ensures this because Q≥k−1. The edited rule removes that guarantee.

For k=4 and Q=D=2^r, r≥2, the slope set of size D is necessarily all of F_Q. For each fixed b the D distinct edges are {(0,b),(1,b+a),(2,b)}. Thus the pair {(0,b),(2,b)} has codegree D. Edges remain distinct because their coordinate 1 values differ. Integer scalar multiplication in the printed formula forces 2a=0; choosing a different representation of the field does not repair it.

The lemma appends an old vertex to each auxiliary edge, with different labels using different old copies. This retains the new pair and all D distinct edges. Taking eight disjoint copies retains its codegree. Each new vertex still has degree D, so the completed hypergraph has maximum pair codegree exactly D whenever a deficit stub exists. Simplicity, regularity, the copy counts and the encoding inequality survive. The failed property is the codegree preservation needed for iteration.

## Verification inside the stated ambient hypotheses

Here is the asymptotic witness checked against the actual formulas. Fix the positive constant c in (4.9), put n=8p for primes p>3, and let ell=log(8p+2). Choose Q_p to be the least power of two at least p/32; then p/32≤Q_p<p/16. On integer d in [ceil(p/16),p], let f(d)=d/8+c ell sqrt(d). For sufficiently large p its lower endpoint is less than p/64, its upper endpoint exceeds p/8, and 0<f(d+1)−f(d)<1. Consequently ceil(f(d)) assumes Q_p for some such d. This argument applies for every fixed sufficiently large recurrence constant, rather than requiring a special choice of that constant.

Take two disjoint copies of the four-partite hypergraph with edges {(j,b+ja):j=0,1,2,3}, a in a d-element subset of F_p and b in F_p. Since p is prime and p>3, different positions have invertible differences. Hence this is a simple linear d-regular 4-uniform H_0 on n=8p vertices. Its maximum j-codegrees are exactly 1 for j=2,3,4. In particular 8 divides n and d=Theta(p).

Definition (1.3) gives Gamma(H_0)=d^(−1/2)+d^(−1/3). Thus Gamma(H_0)(log n)^L tends to zero for every fixed L, as required by Theorem 4.1. The activity lambda=1 lies in its polynomial range. The stopping time T=floor(log_2(1/(Gamma(H_0)ell^B))) tends to infinity, so the construction must continue beyond H_1. Even Theorem 1.6's stronger hypotheses hold with epsilon=1/24: d≥n^epsilon, all intersection coefficients vanish, and Gamma(H_0)/(d^(−1/4)n^(−epsilon))=O(p^(−1/24)).

At stage zero Theorem 4.3's actual ratio is (log n)^5/d=o(1). Together with Lemma 4.5 this supplies good prefixes with positive probability. Every good prefix leaves 4p vertices and degrees d/8+O(sqrt(d log n)), using the sharper actual estimate in Theorem 4.3. The prescribed degree is D_1=ceil(d/8+c ell sqrt(d))=Q_p. Since ell/sqrt(log n) tends to infinity, every residual vertex has a strictly positive degree deficit for sufficiently large p. The residual remains simple and linear and has maximum degree at most D_1, so all input conditions of the completion lemma hold and its nontrivial construction is invoked.

The edited least-prime-power rule now selects Q=D_1=Q_p. The local calculation above gives Delta_2(H_1)=Q_p=Theta(p), independently of which good prefix or edge labeling was selected. However (4.10) prescribes L_2^(1)=1/4+C_4 ell^(−2)+C_4 ell^4=O(ell^4)=o(p). This directly contradicts the asserted bound Delta_2(H_1)≤L_2^(1). In addition, the next short-trajectory theorem would require Delta_2(H_1)(log N_1)^5/D_1=o(1), whereas the ratio equals (log N_1)^5. Selecting the prefix minimizing the remainder cannot avoid the failure.

## Instantiated taxonomy audit

The established result being applied is the guarantee for the explicit completion in Lemma 4.2, followed by its codegree-preservation conclusion on page 30. Its instantiated antecedent is: F is the simple 4-uniform residual with Delta(F)≤D_1; D_1 is a positive integer; S=sum_v(D_1−d_F(v))>0; Q is prime and at least max{D_1,3}; A⊆F_Q has size D_1; and the displayed auxiliary-edge, stub-attachment and disjoint-copy recipe is followed. Its instantiated consequent includes Delta_2(H_1)≤max{Delta_2(F),1}=1, and therefore the weaker required bound Delta_2(H_1)≤L_2^(1).

All input conditions concerning F, D_1, S and A hold. The selected Q=2^r, r≥2, fails the construction's prime restriction and the underlying distinct-evaluation-scalar condition. The consequent is explicitly false, with Delta_2(H_1)=D_1. The abstract existence assertion of Lemma 4.2 remains sound; applying its guarantees to this differently prescribed output is the invalid inference. This makes MP the appropriate primary category. DEF is a reasonable secondary description: the finite output exists, but it fails the inductive invariant required of the next-stage object.

## Significance, subtlety, and repair

This is a substantive break in the proof of Theorem 4.1: the first completion destroys the small pair-codegree condition, so the normalized remainder iteration and its use in Proposition 6.2 lack their required stage estimates. It is not a cosmetic change. The edit preserves field existence, the size bound Q=O_k(D), all degrees and the normalization counts. Detecting it requires tracing a construction nine pages earlier and distinguishing characteristic from cardinality; the k=3 illustration does not exhibit the collision.

A repair is to restore the prime choice. Alternatively, explicitly choose k−1 distinct field evaluation elements and replace the integer coefficients j by those elements throughout the auxiliary construction, then reestablish its guarantees. The submitted version does neither. All required checks pass for accepting this injection.
