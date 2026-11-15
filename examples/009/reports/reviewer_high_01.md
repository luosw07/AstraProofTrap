REJECT

I found a substantive false tensor identity in the proof of Theorem `thm:compatibilityflows`. It is used to establish the transverse momentum–Maxwell compatibility identity. The missing term is nonzero even on smooth compact supersymmetric initial data. This is a defect in the printed argument, not a counterexample to the final compatibility theorem or to the compact rigidity theorem. Several of the principal conclusions may survive a corrected calculation.

## Scope and method

I read the complete supplied `paper.tex`, lines 1–5440, in consecutive bounded chunks, including all four sections, examples, and bibliography. My mathematical input was this paper alone. I did not inspect another version, another workspace document, another review, or external references. I did not use a formal proof assistant. I reviewed the TeX as the mathematical source; I did not separately inspect the rendered PDF.

I followed the spinorial/coframe reduction, the exterior differential system, the explicit evolution and uniqueness argument, the contact/integrable branches, the gerbe reduction, the supergravity evolution/constraint decomposition, the supersymmetric existence argument, constraint propagation, the leafwise averaging lemma, and all six steps of compact rigidity. I checked selected component calculations independently rather than recomputing every long curvature expansion. Results cited from other works were assessed for their role in the argument but were not independently checked against those works. This is an ordinary mathematical review, not formal verification.

## 1. Substantive omission when differentiating the contraction of the second fundamental form

**Location:** Theorem `thm:compatibilityflows`, proof, TeX lines 3749–3752, particularly the display at line 3751. The preceding covariant coframe formulas are at lines 3542–3544. The erroneous display is used in the final substitution at line 3769.

Fix a time and write

- `U = e_{tu}^sharp`, `L = e_{tl}^sharp`;
- `T = Theta_t`;
- `c = widehat c_t(U, -)`.

The paper correctly has `d(T(U,-)) = (1/2) dc`, obtained by differentiating the equation for `d fra_t`. It then claims

`(nabla_U T)(U,L) - (nabla_L T)(U,U) = (1/2) dc(U,L)`.

This does not follow: differentiation also acts on the vector field U inside the contraction. The exact formula is

`d(T(U,-))(U,L) = (nabla_U T)(U,L) - (nabla_L T)(U,U) + T(nabla_U U,L) - T(nabla_L U,U)`.

The paper's own formula at line 3542 gives

`nabla_U U = -T(U,-)^sharp + T(U,U) U - (1/2)c^sharp`,

`nabla_L U = -T(L,-)^sharp + T(U,L) U`.

Symmetry of T therefore gives

`T(nabla_U U,L) - T(nabla_L U,U) = -(1/2) T(c^sharp,L)`.

Consequently the correct replacement for line 3751 is

`(nabla_U T)(U,L) - (nabla_L T)(U,U) = (1/2) dc(U,L) + (1/2) T(c^sharp,L)`.

The last term is missing in the paper, and no stated constraint makes it zero.

### Explicit compact test data

The omission can be tested within the hypotheses used in this proof, not merely on arbitrary tensors. Take a three-torus with angular coordinates `(z,x,y)` and set

`e_u = exp(sin x) dz`,

`e_l = exp(sin z) dx`,

`e_n = dy`,

`frf = 0`, `phi = exp(i sin x)`, `b = 0`,

`frc = exp(sin x) cos x dz wedge dx`.

Use the trivial bundle gerbe. Its initial curvature is zero, so `f_b = 0`. The dilaton curvature is `varphi_phi = cos x dx`. All supersymmetry constraints (lines 3849–3851) hold:

- `d e_u = varphi_phi wedge e_u`;
- `d e_l wedge e_u = d e_n wedge e_u = 0`;
- `frc = e_u wedge varphi_phi`;
- `U = exp(-sin x) partial_z`, and both terms in the scalar rotation constraint are zero.

These data have an explicit smooth supersymmetry evolution of the type constructed in the paper. The complete flow is

`Phi_t(z,x,y) = (z + t exp(-sin x), x, y)`.

Take `fre_t = Phi_t^* fre`, lapse 1, `phi_t = phi`, and `b_t = t frc`. Here `Phi_t^* frc = frc`, and `d frc = 0`, so these also give the required gerbe curvature. Compactness of the spatial torus ensures a globally hyperbolic product metric, or one may restrict to any finite time interval. Thus the example is in the class of supersymmetric configurations to which the compatibility theorem applies; imposing the equations of motion is not a hypothesis of that theorem.

At time zero the spatial metric is

`h = exp(2 sin x) dz^2 + exp(2 sin z) dx^2 + dy^2`,

and `T = -(1/2) L_U h`. In coordinate components,

`T_zz = 0`,

`T_zx = (1/2) exp(sin x) cos x`,

`T_xx = -exp(2 sin z - sin x) cos z`.

Furthermore `c = i_U frc = cos x dx`, so `dc = 0` identically.

At `x = z = 0`, the coordinate vectors `partial_z, partial_x` equal U,L. The relevant Christoffel symbols are

`Gamma^x_zz = -1`, `Gamma^z_zx = 1`, `Gamma^x_zx = 1`,

and `T_zx = 1/2`, `T_xx = -1`, `T_zz = 0`. Direct covariant differentiation gives

`(nabla_U T)(U,L) = -3/2`,

`(nabla_L T)(U,U) = -1`.

Thus the left side of line 3751 is `-1/2`, whereas its asserted right side is zero. The missing term is exactly `(1/2)T(c^sharp,L) = -1/2`.

**Classification and consequence:** This is a mathematical product-rule omission, not harmless notation. The proof explicitly uses this false identity to relate two Ricci computations and obtain the transverse momentum–Maxwell identity. That derivation must be corrected and the subsequent substitutions rechecked. Theorem `thm:susyflowcompatibility` subsequently invokes these compatibility identities, so the printed chain of proofs is affected. I am not claiming that the compatibility theorem itself is false: the corrected identity may restore the argument, and the displayed final compatibility relation is consistent with the example. The rejection concerns the substantive false step in the current proof.

## 2. Incorrect ancillary assertion about conformal transformations and trivial holonomy

**Location:** Paragraph beginning “Let [u,v,l,n] be a flat torsion isotropic parallelism,” TeX line 1251.

The paragraph claims that if the rank-one class is zero, the connection preserves “a conformal transformation of every representative” of the isotropic parallelism. Exactness of kappa and rho permits a *null-rotation gauge transformation* of a representative making both auxiliary one-forms vanish. It does not in general permit a conformal rescaling of every representative to become parallel.

For example, start with a constant parallel null coframe on Minkowski space and perform a nonconstant allowed null rotation, so that `l' = l - f u` with nonconstant f. Its auxiliary one-form is `kappa' = -df`, and the rank-one class is still zero. If multiplication of this coframe by a common conformal factor Omega made it parallel, parallelity of `Omega u` would force `d Omega = 0`. Parallelity of `Omega l'` would then force `df = 0`, a contradiction.

**Classification and consequence:** The statement as written is false, although this appears to be a confusion between conformal rescaling and the already defined gauge transformation. The conclusion that the connection has trivial holonomy when the rank-one class vanishes is correct after replacing that phrase with the appropriate null rotation. This does not undermine the later Cauchy or rigidity conclusions.

## Other checks and repairable presentation issues

The explicit construction in Theorem `thm:wellposedFinalSkew`, including the derivation that the rotation rate r is constant, is coherent. The null-current flow argument for uniqueness also avoids assuming a common uniform time interval on a noncompact initial hypersurface. The contact-branch frame construction and the mapping-torus construction in the integrable branch are consistent with their stated conclusions.

Corollary `cor:timeindependentdevelopment`, item 3, needs a short global-hyperbolicity argument before its maximality proof: lines 2537–2547 move directly from completeness of `q = exp(2 frf) h` and completeness of X to the maximality discussion. This omission is readily repaired. For the time-independent metric `g = h - exp(-frf) dt odot e_u`, dt is timelike. A causal curve parametrized by t has spatial velocity v satisfying

`|v|_h^2 <= 2 exp(-frf) e_u(v)`, hence `|v|_q <= 2`.

Completeness of q prevents escape at a finite t endpoint. The smooth metric then permits causal extension there, so every inextendible causal curve meets each time slice. This establishes the needed Cauchy property. I do not treat this short omitted argument as an independent substantive rejection reason.

The leafwise averaging lemma is substantially more than an unjustified appeal to averaging over dense leaves. Its proof uses the closure of leafwise exact forms, distributional closedness/coclosedness, smoothing by the commuting measure-preserving R^2 action, and the flat integrated Weitzenbock identity. Those steps are consistent, including the final weighted pairing argument. In the compact-rigidity proof, the compact-fiber/dense-leaf distinction, the positive basic weight, the determinant identity, and the second application to the symmetric trace-free curvature matrix fit together. I found no additional substantive error in those steps.

There are also ordinary typographical issues: for example, line 910 uses `R^o_{x,y}` where the surrounding text calls for `R^g_{X,Y}`; line 1162 places exterior derivatives where the Lie derivative product expansion requires the coframe forms themselves; line 3083 has an undefined beta where the current one-form is intended; and line 5329 uses T rather than the displayed time coordinate t. These are locally recognizable corrections and are not the basis for the verdict. The final rigidity statement should phrase the proportionality as “the dilaton curvature is a constant multiple of the Dirac current,” as actually proved, to include the zero-dilaton case unambiguously.

## Overall assessment

The full current paper contains a demonstrably false, used tensor identity in a major compatibility proof. That warrants REJECT under the requested criterion of a substantive error or unjustified inference. The report does not establish that the main results are unrepairable, and it does not assert a counterexample to their final statements. A revision should correct line 3751, redo the transverse compatibility calculation with the missing contraction term retained, and audit the later defect identities that depend on that calculation.
