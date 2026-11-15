# Classification standard

The four benchmark labels are **MP, G, DEF, and CONV**. G has the subtypes **G1** and **G2**. Labels can overlap; each label must identify a specific failed proof obligation.

## Category overview

| Label | Error category | Central question |
|---|---|---|
| **MP** | **Modus ponens (implication elimination)** | From `A` and `A → B`, infer `B`. For a theorem application, instantiate it for the actual objects, establish its antecedent, and preserve its exact consequent. |
| **G** | **Quantifier-rule errors** | Is the derivation valid, and are the variable conditions for universal generalization in the consequent (G1) or existential generalization in the antecedent (G2) satisfied? |
| **DEF** | **Definition and construction errors** | Does the proposed definition or construction actually specify an object satisfying its defining requirements? |
| **CONV** | **Definitional conversion and computation errors** | Does expanding the definitions and carrying out the claimed transformations produce the stated result? |

**DEF concerns the validity of introducing an object; CONV concerns the correctness of expanding and calculating with expressions.** For DEF, the obligations include existence, uniqueness where required, independence of representatives, and valid recursion. For CONV, the obligations concern the actual expansion, substitution, composition, or computation, with each transformation justified by its definitions or applicable rules.

For example, a proposed map on a quotient whose value depends on the representative has a **DEF** failure. Reversing the order when expanding a composition of well-defined maps has a **CONV** failure. A passage may violate both obligations, in which case each label needs its own evidence.

## Logical form of MP

**Modus ponens**, also called conditional or implication elimination, is the rule

`Γ ⊢ A → B`, `Γ ⊢ A` ⇒ `Γ ⊢ B`.

Applying a universally quantified theorem first instantiates it for the chosen objects; MP then uses the resulting implication and its antecedent. For example, from `∀x(P(x) → Q(x))` and `P(t)`, infer `Q(t)`.

In this benchmark an MP error means an unjustified application: the cited implication is misstated or unavailable, its instantiated hypotheses have not been established, or the claimed result differs from its consequent. Record the cited statement, substitution, antecedent, and consequent. An arbitrary false statement is not automatically an MP error; identify the application that fails.

## Logical form of G1 and G2

Let `Γ` denote the undischarged background assumptions and `FV` the set of free variables. The relevant derived inference rules are:

| Benchmark rule | From a proved implication | Infer | Side condition |
|---|---|---|---|
| **G1: universal generalization in the consequent** | `Γ ⊢ A → B(x)` | `Γ ⊢ A → ∀x B(x)` | `x ∉ FV(Γ) ∪ FV(A)` |
| **G2: existential generalization in the antecedent** | `Γ ⊢ A(x) → B` | `Γ ⊢ (∃x A(x)) → B` | `x ∉ FV(Γ) ∪ FV(B)` |

G1 follows by **universal introduction**; G2 follows by **existential elimination** inside a conditional proof. In the fresh-parameter presentation, G1 proves `B(a)` for arbitrary `a`; G2 assumes `A(a)` for a fresh witness and derives the same `B`, then discharges that witness assumption. The parameter must be absent from the remaining open assumptions and the exported conclusion; in G2 it is also absent from the existential premise. G1/G2 are this benchmark's names for the corresponding proof obligations.

For a restricted G1 claim, encode the range in the quantified formula: from a derivation of `D(a) → P(a)` under `a`-independent background assumptions, obtain `∀x(D(x) → P(x))`. A special property of the selected object must be discharged into the claim or established throughout the stated range.

For G2, `A(x)` records the witness properties actually supplied. The derivation of `B` must follow from those properties and the background assumptions. Intermediate constructions may depend on the witness within its scope; the exported conclusion must be independent of its local name. Expand definitions to expose hidden dependencies. For example, from `∀t ∃w P(t,w)`, a witness may depend on `t`; reusing a single witness for all `t` requires an additional argument.

Record the exact implication, open assumptions, quantified variable, and failed derivation or side condition. This connects the operational checks below to a particular inference in the submitted proof.

## Scope of checking

For every mathematical statement sentence within the current target and submitted proof, construction, or refutation, assess the applicability of MP, G1, G2, DEF and CONV individually and perform every applicable check. No statement may be skipped merely because it is an intermediate claim, a supporting assertion, or described as elementary, standard, or obvious. Check that expressions and operations are meaningful in their stated domains and mathematical structures, using the object correspondences permitted by the selected rigor. Verify the submission as written; do not supply missing arguments or repair gaps. Earlier claims inside the submitted argument must themselves be checked; they are not automatically trusted external inputs.

## MP — Applying an implication or established result

When a sentence applies a theorem, lemma, or earlier result to infer a conclusion, locate the cited result and identify the objects to which it is being applied. Check (1) whether the cited result is correctly stated and has been established under the stated assumptions; supplied dependencies and permitted external results are assumed correct, so do not re-prove them, but check their statement and availability; (2) whether the objects satisfy every hypothesis of the result, with each required hypothesis following from previously established facts or assumptions currently in use; and (3) whether applying the result to those objects yields the claimed conclusion, preserving every restriction and qualification. Do not reverse an implication or strengthen its conclusion without further justification. If any check fails, the application does not justify the conclusion. For each application, log the antecedent and consequent of the implication, instantiated for the objects involved.

## G1 — Generalizing from an arbitrary choice

When a conclusion established for selected objects is claimed for every object in a stated range, call the objects in that range the target objects. Check (1) whether the proof correctly establishes the conclusion for the selected objects; and (2) whether every target object satisfies all assumptions used about the selected objects, including restrictions imposed by how they were chosen. If either check fails, extension to every target object is unjustified without additional conditions. For each application, log the antecedent and consequent of the implication before generalization, and identify the variables being universally quantified in the consequent.

## G2 — Showing that existence would suffice

When a sentence claims that finding an object with specified properties would suffice for a desired conclusion, identify those properties and that conclusion. Check (1) whether the argument correctly derives the desired conclusion for an object satisfying the specified properties; (2) whether every property of the selected object used in the argument follows from the specified properties and background assumptions independent of its choice; and (3) whether the desired conclusion is independent of the particular selected object, including dependencies through notation or definitions. If any check fails, existence with those properties has not been shown sufficient. For each application, log the antecedent and consequent of the implication before generalization, and identify the variables being existentially quantified in the antecedent.

## DEF — Introducing definitions and constructions

When a sentence introduces an object by a definition or construction, check the requirements of that introduction, including existence, uniqueness, independence of representation, and validity of inductive or recursive specifications where relevant. An explicit construction may itself establish existence. Distinguish a definition from an assumption or an unproved existence claim. For each application, log the object introduced, its defining expression or construction, and the required conditions, indicating which are established, fail, or remain unresolved.

## CONV — Expanding definitions and verifying computations

When a submitted step relies on definitions or computation, unfold the relevant definitions and carry out the computation asserted in that step. Check transformations using established equalities or mathematical results under the existing equality rules or MP, as applicable; distinguish them from definitional computation. An intended correspondence between objects is not itself a computational justification. For each application, log the starting expression, the expanded calculation with its intermediate steps and the definitions or rules used, the result obtained, and its comparison with the result claimed in the proof.

## Assigning benchmark labels

1. Identify the submitted step and its actual hypotheses, domains, conventions, and dependencies.
2. Assess MP, G1, G2, DEF, and CONV individually. Perform every applicable check and record its required evidence.
3. Certify the failure with a rigorous counterexample or failure argument under those hypotheses. A failed proof step can be certified by an invalid inference even when the theorem admits a different proof.
4. Assign a top-level label only for a verified direct violation. For G, record G1 and/or G2, the implication before generalization, the quantified variables, and which rule check fails.
5. Record downstream propagation, diagnostic calculations, and unresolved questions separately. A calculation used to expose a problem does not automatically make the planted error CONV; a false universal statement alone does not identify a G1 generalization step.

Multiple labels are appropriate when the submitted passage directly violates multiple obligations. For example, a construction may fail DEF and an accompanying claimed compatibility identity may independently fail CONV. Each label requires its own location and evidence.
