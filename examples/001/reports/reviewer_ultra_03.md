VERDICT: ACCEPT

# Mathematical review report

## Conclusion

I accept the current mathematical argument. Starting from a complete metric with positive holomorphic bisectional curvature, the paper constructs a localized global Kähler–Ricci flow, differential inequalities for disc envelopes, joint semipositivity, completeness and contracting charts, and finally surjective global coordinates through polynomial models with degree control. Actual checks of dependencies and key calculations show that this proof chain closes.

No substantive mathematical error or gap warranting rejection was found. The scope and decisive checks below record actual verification rather than a judgment based solely on the main theorem or citations.

## Actual review scope

I read lines 1–6473 of `paper.tex`, including the text, all proofs, and references, and checked proposition numbering and formula presentation against text extracted from `paper.pdf` in the same directory. Research materials were only these two paper files and a PDF text extraction generated for this review. No historical versions, other reviews, or online materials were accessed.

Emphasis included local versus global constants; maximum principles used before flow completeness; limit order for disc-area penalties and boundary estimates; contact jets with a common base point; noncommuting linear contraction rates; macro-grid parameter order; and forward-composition degrees versus backward-iteration errors. Key algebraic and differential identities were rederived from the manuscript’s definitions.

## Main mathematical checks

### 1. Initial analytic data and localized flow (Sections 2–3)

In Proposition 2.1, paired index forms give the strict complex-Hessian lower bound for signed Busemann functions, with strict constants selected only on specified compact sets. The resulting weights serve finite-jet interpolation without needing to be exhaustions. Coefficient bundles for functions, canonical sections, and tangent fields are (K^{-1}), the trivial bundle, and (T^{1,0}M\otimes K^{-1}); the third indeed uses Nakano positivity after tensoring with the determinant.

Lemma 2.2 builds heat evolution of bounded forms on the initial complete metric. Cone preservation and trace commutation are first proved on bounded domains, then passed to the limit through the full Hodge semigroup and off-diagonal estimates. Closedness separately follows from full-semigroup commutation with (d), supporting later heat-potential identities. Upper complex-Hessian bounds for distance cutoffs, lower heat-evolved trace bounds, and dyadic patching give two-sided complex Hessian control.

Theorem 3.1 uses complete Hermitian approximating metrics; completeness of the positive-time limit is not yet used. Potential calculations give

\[
(\partial_t-\Delta_K)Q
=\operatorname{tr}_K\{\alpha-D\operatorname{Ric}(\alpha)+D\partial\bar\partial\phi\}.
\]

Derivative commutation in the maximal-eigenvalue estimate uses closedness of (K-\alpha). The negative gradient-square term from (J(Q)=aQ+\log(1+aQ)) absorbs conformal errors. Combining this with compact-set potential and determinant lower bounds gives local two-sided metric bounds and (0<h_t\le g) in the limit. Local convergence and later completeness have no circular dependency.

### 2. Control at infinity in scalar comparison (Sections 3.4–3.6)

What is needed is (\partial\bar\partial\chi\le C\chi h_t), not the analogous upper bound relative to initial (g). The heat correction satisfies

\[
\partial\bar\partial H=(g-h_t)+o(1)g
\]

and has sufficiently small relative size and gradient. Thus in the Hessian of (\chi=u^{-k}\exp(-AH/u^2)), the term (-Au^{-2}(g-h_t)) absorbs errors originally controlled only by (g). The coefficient (1+t^{\beta-1}) is integrable at zero.

I checked the cofactor inequality in both mass estimates of Proposition 3.3. In eigenvalue coordinates for (h_t\le g), each coefficient of (\operatorname{tr}_{h_t}B\,dV_{h_t}) is the product of the other (n-1) eigenvalues, hence controlled by initial volume. The shell error is indeed (O(N^{2n-1-k})). The key nonlinear cancellation also holds:

\[
\partial_t\bigl[(e^w-1)dV_{h_t}\bigr]
=(\Delta_{h_t}w)dV_{h_t}.
\]

This sufficiently justifies global comparison before positive-time completeness. Smooth upper control functions are constructed through compact-domain problems; boundary compatibility and regularity for local limits are treated separately.

### 3. Disc compactness, frames, and deformation (Sections 4–5)

Lemma 4.3 allows different positive extra-integrability exponents for approximating sections. Finitely generated local modules and Krull intersection convert finite-jet convergence into membership of the original section in the same integrability module, with no common positive lower bound for exponents. Proposition 4.2 then uses area anchors, (L^{3/2}) inverse-Jacobian control, and puncture removal to obtain compactness of full disc images. The global holomorphic immersion is used only through injectivity and compact local boundaries, not properness.

Lemma 4.5’s central frame-inverse bound follows from the nondegenerate symplectic bivector, with only boundary and center compact-set dependence. In Lemma 4.6, rotational difference identities control half-order Sobolev seminorms of both factor and inverse, using only spectral upper and lower bounds.

Section 5 correctly distinguishes deformation radius and Taylor remainder, which may depend on the interior compact set determined by the area penalty, from actual mixed-energy derivative coefficients, which depend only on fixed boundary data. Stokes turns mixed area derivatives of closed forms into boundary pairings. Logarithmic-wall derivatives are first multiplied by wall weights to clear denominators before estimating seminorms.

Intermediate frequencies for removing the negative part satisfy both

\[
B_\varepsilon/P_\varepsilon\to0,
\qquad \varepsilon P_\varepsilon\to0,
\]

because (\varepsilon B_\varepsilon\to0), not merely bounded energy. The backward-clock test has a negative difference-quotient denominator, giving the time-derivative inequality in Proposition 5.1’s direction. Symplectic cost decomposition retains the extra nonnegative vertical shear term, validating Lemma 5.3’s Schur-complement comparison.

### 4. Ellipsoid comparison and joint semipositivity (Section 6)

Optimal-matrix existence, uniqueness, and determinant lower semicontinuity come from bounded feasibility, strict concavity, and a uniform strict margin on the unit sphere. Repetition of contact weights preserves the decomposition while making individual weights arbitrarily small.

I checked the single-column Levi form of the rectangular-matrix potential: at normalized contact, division by the column weight gives ((1-\alpha_i)I). Base point and time remain shared variables in product regularization. When Alexandrov contact jets translate to the original envelopes, canonical cotangent contraction has constant coefficients, so differing approximate source points create no coefficient errors.

After vertical minimization, the aggregate matrix is nonnegative and dominates (\partial\bar\partial\lambda). Even when the latter is indefinite, one can therefore use, in the correct order,

\[
e^{-F_0}b_t\le I
\]

to derive Proposition 6.2’s scalar inequality. Proposition 3.3 then gives (F_0=0), forcing the optimal matrix to equal the evolving cometric and the original disc infimum to equal (N). Thus the passage from envelope equality to Theorem 6.3’s joint semipositivity is fully justified.

### 5. Completeness, static distortion, and simple connectivity (Section 7)

Proposition 7.1 integrates Harnack only along piecewise smooth paths near the distance infimum, then proves positive-time completeness using shortest exit lengths from initial compact balls. The exit-length differential inequality follows by comparing current minimizing paths to earlier times, with correct direction. Curvature-norm control from nonnegative bisectional curvature is already available.

Lemma 7.3’s moving-ball maximum must preserve the full distance constraint in two parameters. Holomorphic second jets at the distant endpoint remove the trace-free length Hessian, leaving a strictly negative trace and handling active constraints. The weighted (\bar\partial) construction then has (\Psi\ge0) on source support and global upper bound (C+2\log A). Together these bound maximal singular length by a fixed power of minimal singular length, without hiding total distortion in constants.

I recalculated second-order information at Harnack equality in Proposition 7.5. Let (S=R_z+kR), (Q=|\partial R|_{A^{-1}}^2), and (Z=S-Q\ge0). At the center, first

\[
\partial R=0,\qquad R_{j\bar l}=-(A^2+kA)_{j\bar l}.
\]

Then calculation gives

\[
(\partial_z-\Delta)Z
=\sum_{j,l}\lambda_j^{-1}|R_{jl}|^2.
\]

At this interior spacetime zero of a nonnegative function, the right side must vanish. Thus the pure complex Hessian is zero and the real Hessian strictly negative definite. Intrinsic third derivatives extend this to actual small metric balls; the gradient flow shortens loops, genuinely handling multiple branches of immersion charts. Proposition 7.7 then patches inverse branches using simple connectivity, and the Liouville property for psh functions bounded above gives a common exponent for every fixed compact set, in correct quantifier order.

### 6. Nonuniform contraction and degree control (Section 8)

Endpoint rate comparison uses holomorphic cotangent sections on strips, giving Loewner order in appropriate endpoint coordinates without assuming commutation of Ricci matrices at different times. This supports monotonicity of ordered rates and later linear alignment.

Propagated-weight loss is controlled by new low records along chains. Each ordered index contributes at most once, so loss is independent of macro-interval step count. The forbidden-monomial gap calculation is

\[
\sum_l\beta_l\mu_l-\mu_i>(0.9m-1)\theta_j\ge0.8\theta_j.
\]

Graph-space extension for linear alignment preserves required nesting. After diagonal-step conjugation, off-diagonal adjustments are exponentially small. The backward homological operator therefore contracts by (\exp[-c\sqrt{S_j}/j^2]), paying polynomial losses in fixed-order coefficient spaces. Allowed nonlinear terms strictly use lower-weight variables, making the models triangular polynomial automorphisms.

Growth intervals pay degree losses on bad components: complete components return within weight bounds at the next regular macro interval; unfinished prefixes incur one fixed factor. The argument finally uses an unbounded subsequence with bounded (q(s)/s), matching the actual available hypothesis. The part of (C_d) multiplying macro-step length depends only on dimension and fixed jet order; macro-width and threshold dependence stays in (o(s_k)). Thus Section 9’s order—jet order, smaller macro width, later start—is not circular.

### 7. Coordinate convergence and surjectivity (Section 9)

Backward error propagation simultaneously verifies the error sum and that every comparison segment for inverse Lipschitz estimates remains in the prescribed small ball. The convergence argument therefore has explicit valid domains.

Global injectivity follows by contradicting positive exit distance from an initial compact ball with exponentially small original-coordinate differences. Derivative nondegeneracy is separately proved by Cauchy estimates in fixed compact coordinate neighborhoods. A quantitative contraction construction gives inverse-image ball inclusion.

Final surjectivity uses only a subsequence of forward-composition degrees. Radial growth bounds for vector polynomials follow on each complex line and scalar pairing. Since (\gamma'<\sigma/2) was chosen, radii sufficiently close on either side of an assumed finite maximal contained-ball radius make degree-growth cost smaller than contraction margin; inverse-image ball inclusion yields a contradiction. No unproved inverse-polynomial degree-growth bound is used.

## Boundary cases and hypotheses

- In complex dimension one, the cofactor empty product is one; higher-order one-dimensional constant-volume jets reduce to linear jets, and polynomial realization remains applicable.
- Initial smoothness uses local equations and initial jets; relevant limits do not require all-order compatibility at distant Dirichlet corners.
- Ricci-window selection allows (q_i\to\infty); the corresponding limit (k=0) is included in the equality calculation.
- Strict compact-set curvature lower bounds, local immersion radii, interior disc compact sets, and fixed boundary constants remain distinct in use. None of the former is replaced by an unproved global uniform constant.

## Substantive and typographical issues

Substantive mathematical issues: none found.

Ordinary typography: no error affecting formula meaning or proof connections was found. Physical, logarithmic, and volume-clock conversions are explicit. Reused letters across stages require attention but have determinate meanings in each derivation.

## Review decision

ACCEPT. The current manuscript supplies connected arguments for the analytic, topological, and dynamical steps required by its main theorem; the checked inequalities, quantifiers, and parameter dependencies are consistent.
