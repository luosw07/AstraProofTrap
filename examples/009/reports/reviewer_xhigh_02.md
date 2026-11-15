REJECT

I found an incorrect tensor identity in the proof of the compatibility theorem. The missing term is generally nonzero on admissible supersymmetric data, and the calculation claimed immediately afterward does not follow from the displayed identities. This is a substantive error in the supplied proof, although it appears locally repairable and does not, by itself, disprove the theorem's conclusion.

Review scope

I read the entire supplied paper.tex, lines 1–5440, in bounded, nontruncated chunks, including its introductory claims, all mathematical sections, examples, and bibliography. I used no other version, other workspace documents, other reviewers' reports, external sources, or formal proof assistant. The complete TeX was my mathematical input; I did not separately inspect the rendered PDF. Locations below refer to that TeX file and its internal theorem/equation labels.

I checked the coframe reduction and its relation to metric connections; the constraint/evolution reformulations; the explicit rotated pullback construction and null-current uniqueness argument; the contact/integrable branches; the gerbe-curvature reduction; the supergravity constraint identities and propagation argument; and the leafwise averaging/compact rigidity proof. This was a mathematical review rather than formal verification. I did not independently verify the contents or applicability of every cited external theorem, and I did not reproduce every lengthy curvature expansion component by component.

1. Missing connection term in the proof of the compatibility theorem

Location: Theorem thm:compatibilityflows, proof, lines 3749–3752, especially the unnumbered displayed identity on line 3751. Its use is explicit in the concluding calculation at line 3769. The claimed theorem identity is eq:constraintidentities0, lines 3660–3663.

At a fixed time, abbreviate

    U = e_tu^sharp,  L = e_tl^sharp,
    q = widehat(c)_t(U, -),  K = Theta_t,  nabla = nabla^{h_t}.

The spatial supersymmetry equation indeed implies

    d(K(U, -)) = (1/2) d q.

However, differentiating K(U, -) also differentiates U. For any vector field L one has

    d(K(U, -))(U,L)
      = (nabla_U K)(U,L) - (nabla_L K)(U,U)
        + K(nabla_U U,L) - K(nabla_L U,U).

The paper's own covariant formula (Remark remark:covariantevolution, line 3542) gives, for L perpendicular to U,

    nabla_U U = -K(U,-)^sharp + K(U,U) U - (1/2)q^sharp,
    nabla_L U = -K(L,-)^sharp + K(U,L) U.

Using symmetry of K, the last two terms in the preceding exterior-derivative identity reduce to

    K(nabla_U U,L) - K(nabla_L U,U) = -(1/2) K(q^sharp,L).

Consequently, the correct replacement for line 3751 is

    (nabla_U K)(U,L) - (nabla_L K)(U,U)
      = (1/2) d q(U,L) + (1/2) K(q^sharp,L).

The final summand is missing from the paper. Symmetry of K cancels some quadratic terms, but does not cancel this term.

Concrete check on admissible data

On an oriented coordinate domain in R^3 with coordinates (x,y,z), take

    e_u = exp(x) dz,    e_l = exp(z) dx,    e_n = dy,
    frf = 0,           phi = exp(i x),      H_b = 0,
    frc = exp(x) dz wedge dx.

Use a flat curving on the trivial gerbe. These data satisfy eq:NSNSsusyconstraintsI and eq:NSNSsusyconstraintsII:

- varphi_phi = dx, and d e_u = dx wedge e_u;
- d e_l = dz wedge e_l and d e_n = 0, so both wedge constraints hold;
- f_b = 0, and frc = e_u wedge varphi_phi;
- U = exp(-x) partial_z, and the skew expression involving Lie derivatives of e_l and e_n is zero.

The induced metric and second fundamental form prescribed by the paper are

    h = exp(2x) dz^2 + exp(2z) dx^2 + dy^2,
    K = -(1/2) Lie_U h.

Write a = exp(-z), b = exp(-x). In the orthonormal frame (U,L,N), where L = exp(-z) partial_x and N = partial_y,

    q = dx = a e_l,
    K(U,U) = 0,    K(U,L) = a/2,    K(L,L) = -b,

and all components involving N vanish. The relevant connection coefficients are

    nabla_U U = -a L,    nabla_L U = b L,
    nabla_U L = a U,     nabla_L L = -b U.

Thus

    (nabla_U K)(U,L) = -3ab/2,
    (nabla_L K)(U,U) = -ab,

so the left side of line 3751 is -ab/2, whereas its printed right side is zero because d q = d(dx) = 0. At x = z = 0, the printed identity reads -1/2 = 0. The missing term is exactly (1/2)K(q^sharp,L) = -ab/2.

This check is not merely an arbitrary tensor assignment. The displayed data meet the supersymmetry constraints used in the proof. They can also be evolved explicitly with the paper's lapse-one construction: the flow is Phi_t(x,y,z) = (x,y,z + t exp(-x)), the coframe is Phi_t^* fre, the dilaton is exp(i x), and the curving can be taken to be t exp(x) dz wedge dx. Thus the error occurs in the class of configurations to which the argument is applied. A local globally hyperbolic neighborhood may be used if needed; the erroneous identity itself is pointwise and spatial.

Impact and distinction from a typo

This is not a harmless index or notation typo: a nonzero, data-dependent quadratic term has been discarded. Equating the two Ricci expressions on lines 3737–3745 and substituting the printed line 3751 leaves an additional (1/2)K(q^sharp,L) in the final relation for the transverse momentum constraint. Therefore the asserted calculation at line 3769 is not justified as written.

The correct term restores the expected cancellation. Indeed, in the concrete example the theorem's final constraint identity itself does hold: at x = z = 0 one obtains H = -4, W = -(3/2)e_u -(1/2)e_l, and star M = -e_u + e_l, hence H e_u = 2W + star M. My finding is therefore a counterexample to the displayed proof identity, not a counterexample to the compatibility theorem's statement. The proof needs correction and rechecking before it can support the later references to this theorem, including thm:susyflowcompatibility and the combined-constraint characterization.

2. Incorrect use of “conformal transformation” in the holonomy paragraph

Location: the paragraph following Corollary cor:torsionflat, line 1251.

The paper says that if [kappa] = [rho] = 0, then the connection preserves “a conformal transformation of every representative” of the isotropic parallelism. The established gauge law only shows that a null rotation can turn a representative into a parallel coframe. A conformal rescaling generally cannot do this.

For example, begin with a parallel Minkowski null coframe (u,v,l,n) and apply a nonconstant null rotation with parameter F:

    u' = u,
    l' = l - F u,
    n' = n,
    v' = v + F l - (F^2/2)u.

For the flat Levi-Civita connection, kappa' = -dF and rho' = 0, so both cohomology classes vanish. If a scalar rescaling Omega of this new coframe were parallel, parallelity of Omega u would force dOmega = 0. Parallelity of Omega l' would then force dF = 0, a contradiction. The same objection holds for the usual conformal null-frame rescalings.

The correct conclusion is that a gauge transformation of the form eq:equivalencerelation produces a parallel representative, and hence that the connection has trivial holonomy. That holonomy conclusion is sound. I regard the word “conformal” here as a secondary terminology/claim correction, not as a failure of the principal Cauchy or rigidity results.

Checks that did not produce a substantive objection

- The null-current flow establishes local uniqueness without assuming a uniform flow interval on a noncompact hypersurface. The argument subsequently uses the Cauchy property to cover an arbitrary development by current-flow coordinates. I found no circularity in that step.
- Corollary cor:timeindependentdevelopment, item (3), moves from completeness to maximality without explicitly giving the short proof that the full product is globally hyperbolic. This claim can be justified directly from the stated metric: for a causal curve parametrized by t, its spatial velocity v satisfies |v|_h^2 <= 2 exp(-frf)e_u(v), hence |v|_{exp(2frf)h} <= 2. Completeness prevents escape at a finite t, so the slices are Cauchy. This omitted explanation is routine and is not a reason for my verdict.
- Lemma lemma:leafwiseaveraging does not assume smoothness of the orthogonal projection without justification. Its leafwise convolution argument supplies the needed derivative regularity in L^2 and uses commuting unitary flows to extend the integrated identity. The limit and weighted pairing steps are valid under the stated hypotheses.
- In the compact rigidity proof, the closed one-form beta and complete transverse field Z justify the compact-fiber/dense-leaf alternatives used to identify the projection. The positive basic weight in Step 4 is then constructed explicitly. The determinant averaging and the final symmetric trace-free curvature-matrix argument are consistent. I did not find a separate error in those steps.

Minor presentational errors

These do not determine the verdict: the curvature notation R^o_{x,y} in line 910 should match R^g_{X,Y}; the first line of the Lie-derivative expansion at line 1162 has differential-form degree mismatches and should use the original coframe one-forms in the symmetric products; line 1201 differentiates the R^2-valued object mathfrak{o} but writes only kappa on the right; beta_t in line 3083 is undefined and evidently denotes varphi_{phi_t}; and T in the final example's dilaton at line 5329 should be t. The compact rigidity statement at line 4777 should say that the dilaton curvature is a constant multiple of the nonvanishing Dirac current, as the proof does, to include the case of zero dilaton curvature.

Overall assessment

The supplied paper contains substantial coherent arguments, and the main local flow and compact rigidity mechanisms withstand the checks described above. Nevertheless, the specific false identity at line 3751 is used essentially in the printed proof of a central compatibility result. On the requested criterion that a substantive mathematical error or unjustified inference warrants rejection, my verdict is REJECT. This verdict is about the current proof as supplied; it is not a claim that the central results are unrepairable or that the compact rigidity conclusion is false.