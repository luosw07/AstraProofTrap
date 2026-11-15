OK

# Independent mathematical audit — case30, attempt06

The submitted change creates a substantive defect in the proof of `lem:spreadwit`. The supplied primary label **G2 is correct**: a finite quadrature witness whose resolution is permitted to depend on epsilon is selected before the subsequent “For each epsilon” construction and reused without that dependence. Every fixed midpoint resolution fails on an admissible family. The defect is integrated into the realization argument and is sufficiently subtle for the proposed benchmark, though the changed quantifier order is detectable by a careful reader.

## Scope and location

I read all 5,295 lines of the assigned `blind/x6p9d4/paper.tex` in contiguous bounded chunks, and the complete assigned `case30/attempt06/tricker_log.md` in bounded chunks. An initially truncated combined read of the log was replaced by complete chunked reads. I also read the adjacent mutation record. I did not inspect other versions, experiment material, or agents, delegate, or use a formal proof assistant. The original excerpt assessed here is the one supplied in the log; preservation claims about uninspected versions are not independently asserted.

The defect is at paper lines **4332–4336**, at the end of the proof of `lem:spreadwit`: “Fix a sufficiently fine uniform midpoint partition ... into 2J cells,” followed by “For each epsilon” transporting its midpoints and invoking `lem:startup`. The dependency that this changes appears in the finite-atom paragraph of `lem:spreadhalf`, lines **3573–3580**. That paragraph selects

\[
n_2(t,\eta)=\lceil |t|^{-1}\log(8/\eta)\rceil
\]

and only then approximates the strictly feasible continuous measure well enough for all lags below this cutoff. Here \(t=\log(1-c\varepsilon)\), so the finite set to be preserved expands without bound as epsilon tends to zero.

The original excerpt simply takes the finite feasible pair furnished by this lemma at the current exponent, then applies startup. That is valid. The modified weights retain the correct density factor \(1/R\), and the claim of strict minimizer slack is also valid. Neither establishes the missing infinitely many lag inequalities.

## Quantifiers and the G2 classification

Let \(P_\varepsilon\) collect the hypotheses of `lem:spreadhalf` verified in `lem:spreadwit`: an admissible band, nonvanishing symbols and a continuous phase, the two small-defect conditions, and the strict lower lag-one condition. Let \(F_\varepsilon(Q)\) mean that the finite quadrature witness \(Q\) has normalized nonnegative weights supported on the band, a value constant with strict minimizer slack, and both lag inequalities at every integer \(n\ge1\).

The established implication is

\[
P_\varepsilon\Longrightarrow\exists Q_\varepsilon\ F_\varepsilon(Q_\varepsilon).
\]

Its existential variables include resolution, nodes, weights, and the value constant. For the midpoint implementation, after selecting the resolution, the nodes are obtained by the affine band map and the weights and constant are set by the printed formulas. The guarantee is for this member of the family. The resolution may depend on the exponent, band, and strict margins, including the cutoff \(n_2(t,\eta)\).

The legitimate family conclusion is \(\forall\varepsilon\ \exists Q_\varepsilon\ F_\varepsilon(Q_\varepsilon)\), for sufficiently small positive epsilon in the given sequence. The replacement instead needs one finite resolution \(J\) and an eventual interval (or tail of the sequence) on which every transported \(Q_{\varepsilon,J}\) satisfies \(F_\varepsilon\). Independence of the resolution from epsilon is an extra witness property, not a consequence of the established implication.

Although the final lemma statement is existential, the subsequent construction depends on the selected witness: its nodes and weights specify the waves to which startup is applied. Thus it cannot discard the unsuccessful witness while preserving the displayed reasoning. Objectives and initializations may still depend on epsilon; the error does not require a common objective across epsilon.

The final startup invocation also has the visible form of an application with a failed antecedent. Its antecedent is stability plus a finite **feasible** pair (with strict minimizer slack additionally required when \(t>0\)); its consequent is the from-rest objective and all-horizon trajectory bound. In this application stability and finiteness hold, but feasibility does not. G2 is the appropriate primary classification because the missing hypothesis arises from the changed existential-witness dependence, rather than a misstatement of startup. There is no primary conversion or definitional error.

## An admissible counterfamily and independent calculation

Use the exact TMM parameters, for small positive epsilon:

\[
L=1,\quad\mu=\varepsilon^2,\quad
\beta=\frac{(1-\varepsilon)^2}{1+\varepsilon},\quad
h=y=2-\varepsilon,\quad \tau=\beta/y.
\]

These satisfy all tuning restrictions, and
\(y(1+2\tau)-2(1+\beta)=-\varepsilon<0\), establishing stability directly. Their limiting data are \((\theta,y,\tau)=(3,2,1/2)\). Set \(c=9/8<3/2=\theta/2\), \(r=1-c\varepsilon\), and \(t=\log r\). Choose an integer \(q\ge12\) with \(1/q\le\mathsf s_1\), and take

\[
K=3,\quad\omega_0=2\pi/3,\quad\mathsf s=1/q,
\quad\mathsf w=\omega_0/q,\quad B=[\omega_0-\mathsf w,\omega_0+\mathsf w].
\]

This is a permitted fixed band. Throughout it,
\(11\pi/18\le\omega\le13\pi/18<3\pi/4\), hence
\(1<\xi=1-\cos\omega<1+\sqrt2/2<12/7\).

Here is an independent way to check the two crucial expansions, using the exact TMM factors rather than merely trusting the private audit. Write \(\rho=1-\varepsilon\), \(X=\chi_\mu\overline{\chi_L}\). Then
\(\chi_\mu=(z-\rho)(z-\rho^2)\), \(\chi_L=z(z+\rho)\). The exact circle expression printed in the robust-momentum proof gives

\[
H_r=r(r^2-\rho^2)\{(r-\rho^2)(1-r)+\xi[r^2+\rho^2+2r\rho(2-\xi)]\}.
\]

Consequently, uniformly on this compact band,

\[
H_r/\varepsilon\longrightarrow4(1-c)\xi(3-\xi)
=-\tfrac12\xi(3-\xi).
\]

At epsilon zero, \(X_0=-2\xi(1+e^{-i\omega})\), so \(\Re X_0=-2\xi(2-\xi)\). The exact identity
\(H_r=rH_r^{\rm mix}+(1-r)\Re X\) then yields

\[
\mathsf M_r/\varepsilon
\longrightarrow4(1-c)(3-\xi)+2c(2-\xi)
=3-\tfrac74\xi.
\]

This verifies the signs and constants underlying the log's counterexample.

Since the band is fixed, both little-o assumptions in `lem:spreadwit` follow from \(\mathsf M_r=O(\varepsilon)\). Also \(\xi(3-\xi)\ge2\) on the band, so eventually \(H_r\le-3\varepsilon/4\). At the limit, \(|X_0|\le8\), hence eventually \(\Xi_B\le9\). The stated last hypothesis therefore holds with \(\lambda_0=1/16\). The proof selects \(\eta=\min(1/2,\lambda_0/(2c))=1/36\).

The other half-step hypotheses hold as well: \(g_0=2\xi(2-\xi)>0\), \(2s_0=2\xi\sin\omega>0\), \(R_0=4\xi\cos(\omega/2)>0\); the phase tends uniformly to \(\omega/2\), with defect \(O(\varepsilon)\). The positive constants \(\mathsf m,\mathsf w,\eta\) are fixed, so the small-defect inequalities hold eventually. The original lag-one argument is uniform over all probability measures on this band. Thus this example satisfies the actual assumptions with \(0<\mu<L\), not merely at the degenerate limiting value \(\mu=0\).

## Every fixed resolution fails

For any fixed grid with \(2J\) cells, its midpoints and frequencies are

\[
a_j=\frac{2j-1-2J}{2J},\qquad
\omega_j=\frac{2\pi}{6qJ}(2qJ+2j-1-2J).
\]

Thus \(P=6qJ\) is a common period. With \(n=P-1\), every selected frequency satisfies
\(\cos(n\omega_j)=\cos\omega_j\) and \(\sin(n\omega_j)=-\sin\omega_j\).

Use exactly the normalized weights proportional to \(\mathsf k(a_j)/R_\varepsilon(\omega_j)\), discarding zero weights. A sufficiently fine grid has nonzero total weight; its weights converge since \(R_0>0\). Define

\[
G_\varepsilon=\sum_j\nu_{\varepsilon,j}g_\varepsilon(\omega_j),\qquad
D_\varepsilon=\sum_j\nu_{\varepsilon,j}
[g_\varepsilon(1-\cos\omega_j)-2s_\varepsilon\sin\omega_j].
\]

By the factor and mixed-symbol identities, the bracket equals
\(-\mathfrak c_\varepsilon\xi\mathsf M_r\), where
\(\mathfrak c_\varepsilon=4/[y^2(1-\varepsilon^2)^2]\to1\). Therefore

\[
G_\varepsilon\to G_0>0,\qquad
D_\varepsilon/\varepsilon\to D_*=
-\sum_j\nu_{0,j}\xi_j(3-7\xi_j/4)<0.
\]

The negative sign is uniform on the band and is independent of any special choice of the allowed kernel.

For the prescribed \(C'=-(35/36)G_\varepsilon\), direct substitution in the definition of the upper slack gives

\[
\upsilon_n=D_\varepsilon+G_\varepsilon(\cosh nt-1)
+\tfrac{35}{36}G_\varepsilon\sinh nt,
\qquad
\frac{\upsilon_n}{\varepsilon}\longrightarrow
D_*-\tfrac{35}{32}nG_0<0.
\]

Strict minimizer slack nevertheless equals \(G_\varepsilon/36>0\). This is a decisive violated constraint, not a missing error estimate.

One can remove the value constant entirely. For arbitrary \(C\), even depending on epsilon, the lower lag-one and upper lag-n slacks are

\[
\ell_1=D_\varepsilon+G_\varepsilon(\cosh t-1)+C\sinh t,
\quad
\upsilon_n=D_\varepsilon+G_\varepsilon(\cosh nt-1)-C\sinh nt.
\]

Let \(A_\varepsilon=\sinh(nt)/\sinh t>0\). Their positive combination is exactly

\[
A_\varepsilon\ell_1+\upsilon_n
=(A_\varepsilon+1)D_\varepsilon+
G_\varepsilon[A_\varepsilon(\cosh t-1)+\cosh nt-1].
\]

For fixed J, \(A_\varepsilon\to n\), the bracket is \(O(\varepsilon^2)\), and the expression divided by epsilon tends to \((n+1)D_*<0\). No choice of C can make both required inequalities true for sufficiently small positive epsilon. In particular, every fixed J fails along any sequence tending to zero. The epsilon threshold can depend on J, exactly as needed to disprove a common resolution.

## Possible repairs, side conditions, and significance

The phrase “sufficiently fine” cannot absorb this failure into a larger fixed constant: the argument applies to every finite resolution. The later bad lag changes with J and eventually lies below the diverging cutoff \(n_2\). Allowing \(J=J_\varepsilon\) does repair the argument, but it changes the order of the selection that the new “Fix ... For each epsilon” passage specifies. The fact that the lemma statement already permits \(J_\varepsilon\) explains how to repair the proof; it does not validate its stronger fixed-grid construction. Reading the partition afresh inside each epsilon application would remove the planted mathematical assertion rather than justify it as printed.

There is no extra dimension defect: the chosen cutoff is supported in \([-1/4,1/4]\), so its convolution is supported in \([-1/2,1/2]\), and at most J of the 2J midpoints have positive kernel weight. Unused coordinates can be added by a quadratic. Normalization, positivity, and the affine change of variables are all valid.

By `lem:waves`, the negative upper slack gives
\(R_{j,j+n}-T_{j,j+n}=\tfrac12e^{(2j+n)t}\upsilon_n<0\). Thus the selected wave data fail a necessary interpolation condition. Startup requires feasibility, not just strict minimizer slack, so its cited implication does not apply. The unchanged existence theorem and headline rate statements need not be false. The defective construction is nevertheless used to prove the finite-dimensional from-rest witnesses, and the wall-layer, corner, and arbitrary-rate optimality arguments invoke that lemma.

## Prospective subtlety assessment

The defect is reasonably subtle and integrated. The changed text supplies plausible quadrature details, preserves the correct density and locally verified slack, and continues directly to an existing realization. The nonuniform cutoff is roughly 750 lines earlier. A reader tracking only fixed lags or weak convergence can miss the late common return. The counterexample requires connecting parameter order, rational midpoint frequencies, and the exact upper/lower lag formulas.

The explicit juxtaposition of “Fix” and “For each epsilon” is also a real clue, so I do not claim that a careful reviewer will necessarily miss it. No blind-review outcome was used. There is no unresolved mathematical issue material to this verdict: the fixed-grid obstruction follows from exact identities and strictly signed limits under all the stated assumptions.
