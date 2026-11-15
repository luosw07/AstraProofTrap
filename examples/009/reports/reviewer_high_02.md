REJECT

I found a substantive incorrect intermediate identity in the proof of Theorem `thm:compatibilityflows`. The error is an omitted frame-derivative term, and an explicit datum satisfying the paper's supersymmetry constraints contradicts the displayed identity. This rejects the argument as written; it is not a counterexample to the compatibility theorem or to the compact rigidity conclusion.

## Scope and coverage

I read the complete supplied `paper.tex`, lines 1–5440, in bounded consecutive chunks, including the preamble, introduction, all mathematical sections and proofs, examples, and bibliography. I used no other version, external source, other workspace document, agent report, or formal proof assistant. The TeX was my mathematical source; I did not separately audit the rendered PDF. I checked the main transformations and their dependency structure, the explicit flow and null-current uniqueness construction, the constraint reductions, and the full leafwise averaging and compact rigidity argument. Long component calculations were checked selectively rather than every component being independently recomputed. References used as background in the paper were not independently verified.

## 1. Substantive error: the differentiated constraint loses a frame-derivative term

**Location:** Proof of Theorem `thm:compatibilityflows`, TeX lines 3749–3752, especially the unnumbered equation at line 3751. This follows the two computations of the mixed Ricci component at lines 3737–3745 and is used in the concluding substitution at line 3769.

Suppress the time index, write U = e_u^sharp, L = e_l^sharp, and put c = i_U(chat), where chat is the paper's two-form widehat c. The constraint supplies

    d(Theta(U, -)) = (1/2) dc.

The paper then claims

    (nabla_U Theta)(U,L) - (nabla_L Theta)(U,U) = (1/2) dc(U,L).

This does not follow. For a symmetric tensor Theta, differentiating its contraction with a nonparallel vector field gives

    d(Theta(U,-))(U,L)
      = (nabla_U Theta)(U,L) - (nabla_L Theta)(U,U)
        + Theta(nabla_U U,L) - Theta(nabla_L U,U).

The covariant coframe equations in the paper itself (line 3542) imply

    nabla_X U = -Theta(X,-)^sharp + Theta(U,X) U - (1/2) e_u(X) c^sharp.

Consequently the last two terms in the previous equation equal

    -(1/2) Theta(c^sharp,L),

not zero. The correct identity is therefore

    (nabla_U Theta)(U,L) - (nabla_L Theta)(U,U)
      = (1/2) dc(U,L) + (1/2) Theta(c^sharp,L).

Symmetry of Theta cancels the quadratic Theta terms but does not cancel the term involving c. None of the hypotheses here requires this term to vanish.

### Explicit countercalculation within the paper's admissible data

On Sigma = R^3 with coordinates (x,y,z), take the positively oriented coframe and data

    e_u = exp(y) dx,
    e_l = exp(x) dy,
    e_n = dz,
    frf = 0,
    phi = exp(i y),
    b = 0 on a trivial gerbe,
    frc = exp(y) dx wedge dy.

Thus varphi_phi = dy and f_b = 0. These satisfy both systems `eq:NSNSsusyconstraintsI` and `eq:NSNSsusyconstraintsII`:

* d e_u = dy wedge e_u;
* d e_l wedge e_u = d e_n wedge e_u = 0;
* frc = e_u wedge varphi_phi;
* the difference of the two screen Lie-derivative components defining f_b is zero.

They are therefore admissible supersymmetry data, not arbitrary tensors unrelated to the theorem. Their flow is also explicit: X = exp(-y) partial_x and Phi_t(x,y,z) = (x + t exp(-y), y, z). The construction in the paper yields the corresponding supersymmetry flow near the initial hypersurface.

At t = 0,

    h = exp(2y) dx^2 + exp(2x) dy^2 + dz^2,
    U = exp(-y) partial_x,
    L = exp(-x) partial_y,
    Theta = (1/2) exp(y) (dx tensor dy + dy tensor dx)
            - exp(2x-y) dy tensor dy,
    c = i_U(frc) = dy.

In particular dc = 0. At the origin, the nonzero relevant Christoffel symbols are

    Gamma^x_xy = Gamma^x_yx = 1,
    Gamma^x_yy = -1,
    Gamma^y_xx = -1,
    Gamma^y_xy = Gamma^y_yx = 1.

Direct covariant differentiation gives

    (nabla_U Theta)(U,L) = -3/2,
    (nabla_L Theta)(U,U) = -1.

The left side of the equation at line 3751 is thus -1/2, while its displayed right side is zero. The omitted term is precisely (1/2) Theta(c^sharp,L) = -1/2.

**Impact:** This is a mathematical miscalculation rather than a harmless notational typo. The proof explicitly uses the false identity to derive the transverse momentum/Maxwell relation at line 3769. That derivation is unjustified as written, and the compatibility identities are subsequently used in Theorem `thm:susyflowcompatibility` and the initial-data characterization. The corrected identity may repair the calculation, but the substitution must be redone with its extra term. I have not found a counterexample to the final compatibility identity: indeed, in the datum above, W(L) = -1/2 and (*M)(L) = 1, consistent with the claimed final relation. The demonstrated error therefore concerns the proof, not a demonstrated false theorem.

## 2. Localized incorrect wording concerning flat holonomy

**Location:** TeX line 1251, paragraph after Corollary `cor:torsionflat`.

The paragraph says that vanishing of the class [kappa] direct-sum [rho] implies that the connection preserves a “conformal transformation of every representative.” What the preceding gauge formula actually proves is that it preserves a representative obtained by a **null-frame gauge transformation**, not a conformal scaling.

For example, start with a constant isotropic coframe (u,v,l,n) in Minkowski space and replace it by the permitted gauge transformation with w = x l, where l = dx. Then l' = dx - x u and kappa' = -dx, rho' = 0. The rank-one class vanishes, but a common conformal rescaling cannot make this coframe parallel: parallelity of Omega u forces d Omega = 0, after which nabla(Omega l') remains nonzero. Applying the inverse null rotation does make it parallel.

**Impact:** The asserted triviality of holonomy is correct, since exact kappa and rho can be removed using `eq:kapparhogauge`. This is a localized terminology/statement correction and does not undermine that conclusion or the main theorems. It is not the principal reason for the verdict.

## 3. Minor notation and exposition corrections

These do not independently justify rejection:

* Line 910 has `R^o_{x,y}` where the surrounding discussion calls for `R^g_{X,Y}`.
* Line 961 places the kernel distribution of a one-form in T* M, although the displayed quotient uses tangent vectors; the intended ambient bundle is TM.
* Line 997 uses an h-orthogonal complement before such an h has been specified there; g is intended.
* Line 1162 has exterior derivatives in tensor-factor positions where the Lie derivative expansion requires v and u, respectively. The following expanded line and the Cartan-connection argument make the intended calculation recoverable.
* Line 1201 differentiates the R^2-valued form mathfrak o but writes only kappa on the right; the formula should be read componentwise for both kappa and rho.
* Line 3083 contains an undefined beta_t in the formula for nabla varphi_phi_t; varphi_phi_t is intended.
* Line 3122 uses phi_t for a real potential in a decomposition of its curvature, despite phi_t already being circle-valued. One can choose a fixed closed representative varrho and a separate smooth real potential psi_t, as the later notation at line 3164 indicates.
* Line 5329 uses T in the exponential where the spacetime coordinate is t.

## Other principal arguments reviewed

The flow solution in Theorem `thm:wellposedFinalSkew`, including the obstruction forcing the rotation rate r to be constant, and the null-current straightening proof of local uniqueness are coherent in the computations I checked. The distinction between a maximal flow tube and a globally hyperbolic neighborhood is correctly recognized.

The proof of Corollary `cor:timeindependentdevelopment`, item (3), would benefit from explicitly establishing global hyperbolicity before proving maximality. This missing explanation is readily supplied from its stated hypotheses: for the stationary metric g = h - exp(-frf) dt symmetric-product e_u, a causal curve parametrized by t satisfies |x'(t)|_q <= 2 for q = exp(2frf) h. Completeness of q prevents escape over finite t intervals, and dt is temporal, so all inextendible causal curves meet each slice. I do not regard this omission as a substantive obstruction to the corollary.

I checked Lemma `lemma:leafwiseaveraging` in detail. Its use of the closure of leafwise exact forms, regularization by the commuting measure-preserving R^2 action, and the weak Bochner identity avoids assuming a smooth leafwise Hodge decomposition or compactness of individual leaves. I found no substantive defect there. I also checked the subsequent compact/dense-leaf distinction, the positive basic weight, the determinant averaging, and the symmetric trace-free curvature-matrix argument in Theorem `thm:compactrigidity`. I found no independent counterexample or substantive error in that rigidity argument.

This review is not formal verification, and the absence of additional findings is not a claim that every long component computation has been verified. The decisive finding is the explicit contradiction to the identity at TeX line 3751 and its use in a principal compatibility proof.