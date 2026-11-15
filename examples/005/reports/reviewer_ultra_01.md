VERDICT: ACCEPT

I accept the mathematical arguments in the current paper. Its main conclusions—global well-posedness, velocity-gradient estimates uniform in Prandtl number, preservation of two orders of temperature-patch boundary regularity at Hölder and Lipschitz endpoints, and the whole-space infinite-Prandtl-number limit—form a complete proof chain under the stated assumptions. The review found no substantive mathematical error requiring rejection of the main theorems.

## Actual review scope

I read the complete input `paper.tex` (lines 1–10821, including six main sections, Appendices A–B, and references) and extracted text from the same directory's 70-page `paper.pdf` to cross-check theorem numbers and some formula typesetting. The review used only these two paper files and checking files generated during this run, with no other versions, historical reviews, or online sources. For cited classical tools, I checked exponent ranges, low-frequency treatment, and required assumptions in their use here; I did not separately retrieve the full cited papers.

The following received particular attention.

## 1. Basic estimates and global well-posedness

**The good unknown and parameter placement are correct.** The vorticity and temperature transport equations give
\[
\varepsilon D_t\Gamma+\Lambda^{2\alpha}\Gamma
=\varepsilon[\mathcal R_{1-2\alpha},u\cdot\nabla]\theta,
\qquad \Gamma=\omega-\partial_1\Lambda^{-2\alpha}\theta.
\]
The right-hand \(\varepsilon\) is consistent with \(1/\varepsilon\) in the subsequent smoothing estimates. The choice \(\nabla^\perp=(\partial_2,-\partial_1)\) also matches the paper's vorticity convention.

**The low-frequency obstruction at the classical dissipation endpoint is addressed.** Lemma 2.8's \(q=2\) estimate follows through
\([\mathcal R_{-1},u\cdot\nabla]\theta=\sum_i[\partial_i\mathcal R_{-1},u_i]\theta\)
and \(\dot H^1\hookrightarrow\mathrm{BMO}\); for \(q>2\), the Sobolev exponent \(2q/(q+2)\) lies strictly in \((1,2)\). At \(\alpha=1,p=2\), Proposition 3.2 does not assume \(\mathcal R_{-1}\theta_0\in L^2\), but splits \(\Gamma\) into \(L^2\) and \(L^q\), \(q>2\), parts. The nonuniform vorticity bound in the high-frequency estimate always carries \(\varepsilon\), producing \(\sqrt\varepsilon(1+\sqrt T)\); frequency-cutoff absorption is independent of \(\varepsilon\).

**Global velocity bounds and gradient bounds are correctly distinguished.** The time kernel in `eq:u-Lp-es-refined` is
\(\min\{1,r^{-(1-1/p)/\alpha}\}\). Thus for \(\alpha<1\), the uniform global \(L^Q\) bound requires \(Q>1/(1-\alpha)\). For \(\alpha=1\), zero mean and the first absolute moment improve decay to \(r^{-3/2+1/Q}\), and \(Q>2\) gives integrability exactly. The first-moment transport estimate and velocity estimate form a linear Gronwall inequality, without circularly assuming the uniform velocity bound being proved.

**The nonzero-mean lower-bound scale is valid.** After Remark 3.3 chooses \(R=L(1+A_\varepsilon)^{r/2}\), the test region contains the temperature support, a fixed \(L\) absorbs the viscous term, and both inertial exponents are at most \(r\). This indeed gives \(A_\varepsilon\gtrsim\varepsilon^{-1/r}\).

**Uniqueness matches construction.** Proposition 3.4's logarithmic interpolation gives the Osgood modulus \(r\log(e+1/r)\), whose reciprocal is nonintegrable at zero. Since \(2\alpha>1\), the solution constructed in Theorem 1.1 satisfies \(u\in L^1_TB^1_{\infty,1}\), entering that uniqueness class. Appendix B.1's strong local velocity convergence handles both nonlinear terms, while the global \(L^p\) bound and test-function decay handle fractional dissipation.

## 2. Commutators and boundary regularity

**Integrability conditions in the negative-order kernel estimates agree.** In Lemmas 2.9–2.11, behavior near zero and in the far field is controlled by \(-d<\sigma<0\). The kernel representation after one tangential derivative uses two differences, again reducing to \(|z|^{-d-\sigma}\). The Hölder version additionally controls \(|z|^{-d-\sigma-1}\), explicitly requiring \(\sigma<-1\). The cutoff-boundary powers \(\delta^{-\sigma}\) and \(\delta^{-1-\sigma}\) vanish in their respective ranges. The text uses \(\sigma=-2\alpha\) and \(\sigma=1-2\alpha\) in different branches, without directly applying the former kernel lemma at the critical order \(-2\) for \(\alpha=1\).

**Tangential patch derivatives eliminate interface measures.** Lemma 2.5 uses
\(W_0\mathbf1_{D_0}=\nabla^\perp(\varphi_0)_+\)
 to establish a divergence-free structure; a divergence-free product estimate controls the highest negative Hölder norm. The transported commutation relation \([D_t,\partial_W]=0\) agrees with this.

**All decisive exponent intervals are nonempty.** Checked individually:

- \(p>2/(2\alpha-\gamma)\) ensures \(2\alpha-2/p>\gamma\), allowing the Chemin–Lerner smoothing norm to embed in the time-integrated Hölder/Besov norms required in the text.
- In Lemma 5.1, \(q>2/(2\alpha-1)\) gives \(4\alpha-2-2/q>2\alpha-1\), allowing the auxiliary \(\gamma'\).
- For the homogeneous initial-data part in the same lemma, \(\max\{-1,\gamma+2/p-2\alpha\}<s_0<0\) is available, including the permitted \(p<2\) cases.
- At Lemma 5.3's Lipschitz endpoint, one may choose \(1<\gamma'<\min\{2\alpha-2/p,2\alpha-2/q\}\), followed by \(\gamma'-1<\beta<2\alpha-1\). Applying lower-order Proposition 5.2 before estimating the dissipative commutator is a valid progression.
- The temperature endpoint condition \(\mu>2-2\alpha\) gives \(\mu+2\alpha-2>0\), ensuring high-frequency summability and explaining the strict inequality.

**The endpoints do not confuse Zygmund and Lipschitz spaces.** Section 4's \(\gamma=1\) branch directly estimates \(\nabla W\) in \(L^\infty\), and Section 5 further estimates \(\nabla\partial_WW\). The conclusions connect actual Lipschitz norms with derivatives of boundary parametrizations, sufficient for \(W^{2,\infty}\) and \(W^{3,\infty}\) preservation.

**The initial-profile assumptions suffice when using lower-order endpoint estimates.** For example, the profile exponent \(2+\gamma-2\alpha\) in Theorem 1.3's lower-order branch is strictly above \(2-2\alpha\), supplying some \(\mu>2-2\alpha\) required by Section 4. For \(\alpha=1\), \(C^\gamma\), \(\gamma>0\), serves this purpose as well.

## 3. Infinite-Prandtl-number limit

**The moving frame does provide uniform local control.** Proposition 6.1 first constructs the path for each fixed \(\varepsilon\) by Carathéodory's theorem, then obtains relative-velocity bounds through mean normalization and Morrey's estimate. The relative support radius satisfies
\[
R^\varepsilon(t)\le R_0+C_T\int_0^t(1+(R^\varepsilon)^\sigma+\sqrt{R^\varepsilon})\,ds,
\quad 0<\sigma<1,
\]
so it closes independently of \(\varepsilon\). In the translated weak momentum equation, compactly supported divergence-free test functions have zero spatial integral, eliminating acceleration; requiring only absolute continuity of the path is appropriate.

**Weak velocity with strong temperature suffices for the transport term.** Strong temperature convergence in \(C_tH^{-1/2}_{\rm loc}\) pairs with local \(W^{1,p}\), \(p>2\), velocity. The inertial term is \(O(\varepsilon)\) on compact sets. Fractional dissipation uses global \(L^Q\) weak-star convergence, avoiding reliance on local convergence alone for a nonlocal operator.

**Normalization, identification, and uniqueness work.** The Fourier argument for \(w=u-G_\alpha*\theta\) proceeds away from the frequency origin; spatial sublinear growth reduces a possible polynomial difference to a spatial constant. Original-frame \(L^Q\) integrability or the moving-frame mean condition eliminates that constant. The kernel-difference estimate
\[
|G_\alpha(z)-G_\alpha(z')|
\lesssim |z-z'|\bigl(|z|^{2\alpha-3}+|z'|^{2\alpha-3}\bigr)
\]
is locally integrable for \(\alpha>1/2\), allowing ordinary Gronwall uniqueness in Lemma 6.3's flow comparison. Subsequence convergence therefore upgrades to full-family convergence.

**Global strong temperature convergence and inheritance of endpoints are proved.** Corollary 6.4 uses the conserved \(L^2\) norm and compactness of the limiting trajectory in \(L^2\) to upgrade local negative-norm convergence to uniform-in-time global strong convergence. The general fractional case claims only \(1<s<\infty\), while Theorem 1.4's compactly supported patches additionally obtain \(s=1\), with consistent quantifiers. Tangential fields and their second-order boundary derivatives obtain time compactness through divergence form; Hölder and Lipschitz norms survive by lower semicontinuity and weak-star derivative convergence, respectively.

## 4. Regularization and passage to the limit

Separately smoothing temperature and the tangential field in Appendix A does not preserve exact patch structure, but the a priori estimates require only the corresponding initial tangential norms. Lemma A.1 and the subsequent second tangential derivative expansion control these independently of smoothing scale.

Appendix A.3 cuts off velocity then projects it; compact support of the tangential field places projection errors in the far field, with local derivative error decaying as \(\delta^{m+2/q}\). The choice \(r=\min\{p,q\}\) retains \(r>2/(2\alpha-\gamma)\), so smooth data preserve the exponent margin actually used. Appendix B's local strong convergence, uniqueness of the tangential equation, nondegeneracy, and derivative lower semicontinuity connect with these approximations.

## 5. Ordinary notation, typesetting, and exposition suggestions

The following are editorial revisions that can be made directly without changing the main arguments.

1. Section 6, TeX line 7837, contains `\Vert \nabla u^\varepsilon\Vert _{-L^p)}`, also rendered with a corrupted norm subscript in the PDF. State the \(L^\infty([0,T];L^p(\mathbb R^2))\) norm used.
2. Near TeX line 7905 in Section 6, `we have` appears inside the Morrey inequality's math environment; move it outside.
3. Appendix A.2's `Let k=2` near line 9267 and `k=3` at line 9300 use a numbering convention different from boundary order \(k=1,2\) in the text. Say “first tangential derivative” and “second tangential derivative,” or explain that these are Lemma 2.5's indices.
4. Proposition 5.2, formula `eq:parW-the-L1Cgam1`, uses \(C^0\) at \(\gamma=2\alpha-1\). Specify \(B^0_{\infty,\infty}\) or simply use \(L^\infty\); this branch's \(C^{1+\widetilde\mu}\) profile assumption already gives the required bounded tangential derivative.
5. “Notation” describes \(A:B\) as the “usual product of two matrices,” which is imprecise; the weak momentum equation needs the Frobenius inner product \(\sum_{ij}A_{ij}B_{ij}\). Specify this.

Final verdict: ACCEPT. These checks support the paper's mathematical arguments; the listed revisions concern notation, typesetting, or clarification of existing steps.
