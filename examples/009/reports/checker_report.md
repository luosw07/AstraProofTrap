OK

Independent checker report: checker_1503

Scope and verdict

I read the specified current paper in full, in bounded chunks, together with the complete specified tricker log and adjacent mutation.json. I used no other experiment material, external source, agent, or formal proof assistant. The third recorded replacement creates a genuine substantive mathematical defect. Its primary classification is CONV, as supplied. The defect is sufficiently integrated and plausibly subtle for this benchmark, although an auditor who expands the contraction carefully can detect it readily. This assessment is prospective and uses no blind-review outcome.

Location and comparison with the original excerpt

The defect is in paper.tex lines 3749–3752, the unnumbered display in the proof of Theorem thm:compatibilityflows. The display follows the two computations of the mixed spatial Ricci component and precedes the calculation using closedness of the dilaton curvature. Its asserted justification is “Taking its ... component and using the symmetry of Theta”. The original excerpt in the log includes the additional term (1/2) Theta(hat(c)(e_u)^sharp,e_l^sharp); the current display omits it. The original term is correct under the unchanged spatial connection identities. The other two recorded replacements restore the curving construction and its verification; the current paper contains those restored expressions. My verdict does not rely on claims about uninspected historical versions or hashes.

Precise hypotheses and quantifiers

The theorem takes any supersymmetric Neveu–Schwarz flow, explicitly defined as a solution of eq:susyevol, and asserts its constraint identity at every time. Its hypothesis is not that the second-order Einstein, Maxwell, and dilaton equations or their constraints vanish. The proof itself fixes an arbitrary time and states that its calculation uses the spatial supersymmetry constraints. Compactness, completeness, vanishing transverse derived two-form, and vanishing transverse second fundamental form are not hypotheses. Later compact rigidity results apply to supersymmetric solutions of the equations of motion and cannot be imported here.

Fix a time and put U=e_u^sharp, L=e_l^sharp, w=i_U hat(c), q=Theta(U,-), and nabla=nabla^h. The conventions identifying one-forms with metric-dual vectors are stated in the introduction and in the second-fundamental-form discussion. Theta is symmetric and U,L are orthonormal, but U is a specified field determined by the coframe, not an arbitrary parallel extension of a vector at one point. All quantities are fixed by the flow. There is no existential choice of a witness, additive constant, lapse, or frame extension that can erase the discrepancy while preserving the asserted identity.

CONV calculation

The unchanged equation d a_fraktur=-q+(1/2)w implies the valid starting expression

    d q = (1/2) d w.

Define

    D=(nabla_U Theta)(U,L)-(nabla_L Theta)(U,U).

The torsion-free exterior-derivative formula and covariant product rule give

    d q(U,L)
      = (nabla_U q)(L)-(nabla_L q)(U)
      = D + Theta(nabla_U U,L)-Theta(nabla_L U,U).

Thus

    D=(1/2)d w(U,L)-Theta(nabla_U U,L)+Theta(nabla_L U,U).

The first unchanged equation in Remark remark:covariantevolution (lines 3541–3542) is

    nabla e_u+Theta=q tensor e_u-(1/2)e_u tensor w.

Raising the final index, with S(V)=Theta(V,-)^sharp, yields

    nabla_V U=-S(V)+Theta(U,V)U-(1/2)e_u(V)w^sharp.

In particular,

    nabla_U U=-S(U)+Theta(U,U)U-(1/2)w^sharp,
    nabla_L U=-S(L)+Theta(U,L)U.

The correction therefore equals

    -Theta(nabla_U U,L)+Theta(nabla_L U,U)
      = Theta(S(U),L)-Theta(U,U)Theta(U,L)
        +(1/2)Theta(w^sharp,L)
        -Theta(S(L),U)+Theta(U,L)Theta(U,U)
      = (1/2)Theta(w^sharp,L).

Symmetry cancels the quadratic S terms and the scalar products, but does not cancel this final term. The actual result is

    D=(1/2)d w(U,L)+(1/2)Theta(w^sharp,L).

The mutation asserts D=(1/2)d w(U,L). This is an incorrect conversion of a contracted exterior derivative to tensor covariant derivatives. CONV is the correct primary category; it is not a theorem-application hypothesis failure (MP), a quantifier generalization/elimination issue (G1/G2), or a failure of existence or well-definedness (DEF).

Admissibility of a decisive witness

The log's example works. On oriented R^3 with coordinates (x,y,z), take

    e_u=e^x dz, e_l=e^z dx, e_n=dy,
    f_fraktur=0, phi=e^(i x), varphi_phi=dx,
    b=0, c=e^x dz wedge dx.

Use the trivial gerbe with identity submersion Y=Sigma and flat connective structure (zero local connection potential). Then H_b=0 and f_b=0. This is legitimate gerbe data; no nonintegral three-form is prescribed. The coframe has positive orientation because dz wedge dx wedge dy=dx wedge dy wedge dz. The actual circle-valued map has curvature dx under the paper's Maurer–Cartan convention.

The full initial constraints eq:NSNSsusyconstraintsI–II hold:

    d e_u=dx wedge e_u=varphi_phi wedge e_u;
    d e_l=e^z dz wedge dx, hence d e_l wedge e_u=0;
    d e_n=0;
    c=e_u wedge varphi_phi=f_b *e_u+e_u wedge varphi_phi.

For U=e^(-x) partial_z, L=e^(-z) partial_x, N=partial_y, one has L_U e_n=0 and L_U e_l=e^(-x)e_l. The scalar constraint is therefore 0-0=f_b. These are all the prescribed initial supersymmetry constraints. A bosonic equation-of-motion constraint is not missing from the admissibility check; none is imposed by the theorem being audited.

One need not rely solely on the later existence theorem to realize the data. The explicit smooth flow is

    Phi_t(x,y,z)=(x,y,z+t e^(-x)),
    lambda_t=1, f_fraktur_t=0,
    e_tu=e^x dz-t dx,
    e_tl=e^(z+t e^(-x)) dx, e_tn=dy,
    phi_t=e^(i x), a_t=0,
    b_t=t e^x dz wedge dx.

The dual U_t remains U. The derived two-form is c_t=partial_t b_t=e^x dz wedge dx, hat(c)_t=c_t, while d_Sigma b_t=0. These fields satisfy eq:NSNSspecializedevolution: the coframe evolves by L_U, the scale and lapse are constant, and both sides of the dilaton transport equation vanish. All spatial constraints are the pullbacks of the initial ones, and c_t=e_tu wedge dx. Therefore the first-order supersymmetry system holds. If a globally hyperbolic configuration is required, the same domain-of-dependence restriction used in the paper gives a globally hyperbolic germ containing the initial slice. No completeness of the displayed spatial metric or global hyperbolicity of the entire flow tube is needed. The discrepancy is already intrinsic to the initial slice and survives that restriction.

Independent numerical tensor check at a point

At t=0 the metric is h=e^(2x)dz^2+e^(2z)dx^2+dy^2. Set A=e^(-x), B=e^(-z). From the definition Theta=-(1/2)partial_t h_t its matrix in (U,L,N) is

    [ 0    B/2   0 ]
    [ B/2  -A    0 ]
    [ 0     0    0 ].

Here w=dx=B e_l and q=(1/2)dx, so d q=d w=0. Directly, [U,L]=B U-A L and the other brackets vanish. Koszul's formula gives

    nabla_U U=-B L, nabla_U L=B U,
    nabla_L U=A L, nabla_L L=-A U,

with all N coefficients zero. Since U(B)=-AB,

    (nabla_U Theta)(U,L)
      =U(B/2)-Theta(-B L,L)-Theta(U,B U)
      =-AB/2-AB=-3AB/2;

    (nabla_L Theta)(U,U)
      =L(0)-2Theta(A L,U)=-AB.

Consequently D=-AB/2, whereas the mutant right-hand side is zero. At x=z=0 it claims -1/2=0. The deleted correction is exactly (1/2)Theta(B L,L)=-AB/2. This directly verifies both the sign and coefficient of the original excerpt independently of the disputed conversion.

Downstream significance and possible repairs

The first mixed-Ricci expression immediately before the altered passage contains D. The second contains (1/2)Theta(w^sharp,L). With the correct conversion those contributions cancel in the comparison; with the mutation an uncancelled term remains. The proof's final “direct computation” of the transverse momentum/Maxwell relation therefore does not follow from its stated intermediate identities. That relation is the second equation of eq:constraintidentities and is used later in thm:susyflowcompatibility to identify the mixed Einstein defect and reduce the constraints for propagation. It also supports the initial-data characterization.

The headline compatibility identity may remain true, as may later theorems after correction. A false intermediate equality on admissible data is nevertheless a real proof defect. Restoring the product-rule correction repairs it. Alternatively imposing Theta(w^sharp,L)=0 would narrow the theorem's hypotheses substantively. Neither a notation change nor a change of connection convention can turn the displayed zero into -1/2. Choosing normal coordinates does not make the geometrically prescribed U parallel; moving its derivative into another term is precisely restoring the missing contribution. This is not a lost fixed constant that an estimate can absorb: it is a nonzero tensor term in an exact equality.

Prospective subtlety assessment

The modification is short and sits inside a long, coherent calculation with unchanged definitions, valid starting closedness, and two mixed-Ricci expressions. Symmetry really does cancel most of the product-rule terms, making the explanation plausible unless the remaining transverse term is tracked. The surviving term depends jointly on the derived field and transverse shape, so fluxless examples and the displayed compact examples with w=0 do not expose it. The paper's preceding spatial connection formula does provide a straightforward route to discovery; thus the error is moderately subtle rather than exceptionally resistant to careful review. It is sufficiently integrated and substantive to approve as a planted CONV defect. There is no unresolved mathematical issue affecting this verdict.
