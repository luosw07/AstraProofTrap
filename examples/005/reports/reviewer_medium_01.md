VERDICT: ACCEPT

After additional continuous chunked reading and mathematical verification, I accept the current mathematical arguments. This report replaces the intermediate record saved because reading was unfinished.

## Actual review scope

The review examined only this directory's paper.tex and paper.pdf. I read the introduction, four main theorems, technical lemmas, global well-posedness proof, proofs of persistence of two boundary orders, the infinite-Prandtl-number limit proof, Appendices A and B, and references. Passages affected by prior truncation were reread in smaller chunks, with particular attention to Section 3, all of Section 6, and both appendices. I also extracted text from the same PDF to check theorem and lemma numbering and viewed rendered images of pages 1 and 67; the mathematical review primarily used complete TeX, with sampled PDF checks. No other paper versions, external review materials, or network were accessed.

The review focused on formula orders, low frequencies, nonempty exponent intervals, cancellation of epsilon factors, initial tangential norms, approximation, and moving-frame limit identification. For explicitly cited standard theorems, I checked that the types of required assumptions match their applications here; cited literature was not separately retrieved.

## Key mathematical checks

### 1. Global estimates and low frequencies

The equation for Gamma=omega-R_(1-2alpha)theta has correct signs and epsilon factors. For alpha=1, p=2, the authors do not incorrectly treat R_-1 theta as L2, but split Gamma into an L2 component with initial data omega0 and an Lp component with initial data -R_-1 theta0 (p>2). The Hardy–Littlewood–Sobolev exponent 2p/(p+2) for R_-1 lies in (1,2), compatible with temperature in L1∩Linfinity.

The high-frequency closure at Section 3, TeX lines 5200–5385, also works: the epsilon^(-1/2) loss in the ordinary vorticity energy estimate combines with epsilon from high-frequency dissipative integration to leave only sqrt(epsilon). A frequency cutoff N depending on T but not epsilon absorbs the vorticity Besov norm. The resulting Chemin–Lerner regularity has strict positive exponent margin, sufficient for the time-integrable Lipschitz norm required by the flow.

For p>2, the Gamma Lp estimate closes through the gradient-type commutator, avoiding reintroduction of a nonuniform zeroth-order velocity norm. The interpolation absorption power 2/p is strictly less than 1. Uniqueness closes through logarithmic interpolation and the Osgood modulus r log(e+1/r), allowing constants to depend on fixed epsilon, as the theorem permits.

### 2. Global velocity norms

The time-integration exponent in eq:u-Lp-es-refined is (1-1/Q)/alpha. In the fractional case, Q>1/(1-alpha) gives large-time integrability exactly. Initial W1,p embedding supplies the required finite Q norm.

For alpha=1 with zero-mean temperature, heat-kernel differences give decay r^(-3/2+1/Q), integrable for Q>2. Growth of the first absolute moment is controlled by integral ||u||Q; substitution in the mild velocity formula gives a genuinely closed Gronwall inequality.

I also checked the test-function argument for the nonzero-mean velocity lower bound: R=L(1+A)^(r/2) both contains temperature support and controls viscosity; the other terms are controlled by epsilon(1+A)^r, giving A>=c epsilon^(-1/r). Its scale agrees with the corresponding upper bound.

### 3. Technical lemmas and boundary regularity

The negative-order kernel is |z|^(-d-sigma) times a smooth angular function. The condition -d<sigma<0 gives local integrability and far-field control; velocity differences in the commutator cancel the first-order kernel singularity. The three integral terms after another tangential derivative match the chain rule. The Holder commutator requires sigma<-1, exactly the condition for local integrability after further kernel differentiation.

The high-exponent boundary C1,gamma case uses sigma=-2alpha∈(-2,-1), and the endpoint uses sigma=1-2alpha∈[-1,0), with correct application ranges. The endpoint does not treat B1_(infinity,infinity) as Lipschitz, but estimates grad W directly; the strict condition mu>2-2alpha makes the required high-frequency geometric series converge.

Section 5 splits tangential Gamma into F1 and F2 to handle different p,q. The F2 choice max{-1,gamma+2/p-2alpha}<s0<0 is available precisely from p>2/(2alpha-gamma). The low-exponent auxiliary gamma' interval is also nonempty because 2/q<2alpha-1.

At the W3,infinity endpoint, higher gamma' satisfies 1<gamma'<min{2alpha-2/p,2alpha-2/q}, available from the two strict initial exponent assumptions. Choosing gamma'-1<beta<2alpha-1 allows lower-order Proposition prop:pGamma-low first to control W in B^(gamma')_(infinity,1), followed by the dissipative commutator, without circular dependence. Finally, Gronwall on the partial_W grad W equation controls partial_W W in W1,infinity.

### 4. Approximation and limit identification

Appendix A projects then convolves the cutoff velocity, preserving zero divergence; compact support of W0 makes the projection error from distant truncation a smooth far-field term near the tangential support. The derivative estimate delta^(m+2/q) is correct. Reducing the tangential exponent to min{p,q} retains a strict bound above 2/(2alpha-gamma), so approximation preserves the needed margin.

Commutators from separately convolving temperature and the tangential field are explicitly estimated. D3 in the second tangential derivative contains differences of partial_W W; its C^(gamma-1) control and the D1,D2,D4 norms embed together in the target negative-exponent space. At the endpoint W0∈W2,infinity gives direct Linfinity control.

Appendix B first obtains strong local velocity convergence, then local strong tangential-field convergence from spatial regularity and time-derivative bounds in negative-order spaces. It identifies partial_W W through div(W⊗W), and endpoint first derivatives through distributional differentiation and weak-star convergence, avoiding products of two weakly converging factors. Nondegenerate tangents and injectivity of the flow supply the geometry for boundary parametrization.

### 5. Infinite-Prandtl-number limit

Section 6's two coordinate choices match low-frequency velocity properties. For nonzero-mean alpha=1, the mean-normalized translation path satisfies Caratheodory conditions. Translated velocity splits into a Morrey difference term and a Stokes convolution average; the latter grows only logarithmically in support radius, so support and local velocity bounds close together with constants independent of epsilon.

The translated weak momentum equation uses compactly supported divergence-free test fields. Each component has zero spatial integral, removing acceleration. Only absolute continuity of the path is needed; no uniform acceleration bound is implicitly assumed.

Strong negative-order temperature convergence and weak-star local W1,p velocity convergence suffice to pass the transport product. Fourier support and sublinear growth reduce the limiting velocity minus G_alpha*theta to a spatial constant; finite LQ integrability removes it in the original frame, and fixed mean normalization in the moving frame.

Normalized Stokes–transport uniqueness uses |grad G_alpha(z)|<=C|z|^(2alpha-3). The condition alpha>1/2 makes the singularity locally integrable, and the flow-difference integral inequality closes by Gronwall. Global strong L2 temperature convergence follows from conserved norms and compactness of the limiting L2 trajectory, addressing far-field issues left by local convergence alone. Uniform boundedness of patch supports then gives L1 convergence. Identification of tangential fields and second-order quantities follows the appendix's mechanism and preserves both Lipschitz endpoints.

## Typesetting and expression suggestions

These local notation and prose revisions do not change the mathematical conclusions above:

- Near TeX 7838, the norm subscript `_{-L^p)}` should be restored to the corresponding L-infinity-time, Lp-space norm; the PDF's Section 6 also displays this corrupted subscript.
- Near TeX 7907, the Morrey estimate inserts `we have` in math mode; move it outside.
- Correct spelling errors such as familly, limite, dissipatif and repeated punctuation throughout.
- One location in Section 5 calls lem:pGamma-high a Proposition; align it with the Lemma environment.

## Conclusion

The main theorems' parameter ranges, low-frequency treatment, endpoint estimates, and two limit processes form a consistent argument chain. After the full reading and focused calculations above, I found no substantive error requiring rejection of the mathematical arguments. Verdict: ACCEPT.
