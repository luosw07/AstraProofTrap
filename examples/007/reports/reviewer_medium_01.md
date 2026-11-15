VERDICT: UNCERTAIN

Referee report on “Global quantum geometric Langlands at irrational level”

Scope

I have now read the complete LaTeX manuscript, including the references. I returned to the portions omitted by truncated tool output and read them in bounded chunks. This report supersedes my preliminary, incomplete report. My research input was paper.tex alone; I did not consult the cited papers, browse, inspect historical material, or modify the manuscript. Reading the complete argument has not resolved the specific verification issues below. I do not have a demonstrated counterexample to the main theorem or to a numbered lemma.

Summary and assessment

The proposed proof has two substantial new bridges: a deformation argument for the global Whittaker–Poincare identity, and a passage from pointwise W-algebra comparisons to coherent equivalences across collisions. Localization and the two Plancherel identities then imply the stated equivalence by a clear formal argument. The manuscript pays considerable attention to actual global forms, opposite characters, determinant exponents, relative lattices, and the distinction between ordinary and renormalized categories. These distinctions are necessary and are carried through the final construction.

I cannot yet accept the mathematical argument because I have not established the full relative interchange statement underlying the non-torsion rank test, or the compactness and base-change inputs used to upgrade the point Skryabin theorem to its stated family version. These are substantive verification questions at indispensable steps, rather than typographical objections or assertions that the conclusions are false.

1. Relative recording-coordinate interchange in the deformation argument

Location: Section 5, Lemma “Non-torsion rank test,” label deform:rank, especially the proof following equation (P2).

Locating quotation: “This criterion holds relatively, with charts and spectators retained. The argument of Lemma ... therefore moves [the recording integral] past either pullback, either direct image, and their geometric comparison maps.”

The point calculation is persuasive: for a mixed-origin perverse object on G_m, quasi-unipotence at the endpoints excludes invariant nearby cycles after a non-torsion Kummer twist; cleanness and Artin vanishing then make the Mellin calculation exact on perverse objects and control ranks. The proof needs more than this point calculation. It replaces an entire finite diagram containing mixed operations by a single final recording integral, including natural transformations. My unresolved issue is verifying the relative cleanness and the exchange transformations throughout that reduction, particularly when the recorded complex has singular support meeting the endpoint over a special output locus. One needs the precise relative comparison to remain compatible with taking output stalks and with the geometric maps whose ranks are compared. The terse reference to the Fourier proof leaves this verification insufficiently explicit for me to certify it.

Consequence: the last step in the logarithm colimit lemma uses this rank statement to transfer the vanishing of a transition over C((h)) to every non-torsion complex parameter. The finite Vinberg comparison also invokes it directly. These are essential dependencies of the Plancherel identity in Section 6.

Possible resolution: supply the relative compactification and exchange lemma explicitly, specifying the extension functors, the boundary nearby-cycle calculation, and the natural exchange maps for the permitted diagrams. Then check its application to the finite Vinberg and tested-cone diagrams. I am recording an unresolved verification issue, not claiming that quasi-unipotence or the point rank calculation fails.

2. Family upgrade in the relative Skryabin comparison

Location: Section 8, Lemma “Ext continuity,” label walg:ext, and Proposition “Relative Skryabin comparison,” label walg:relative-skryabin; also their reliance on Proposition loop:hc-renormalization in Section 7.

Locating quotations: “All the associated-graded modules involved are finitely presented over the polynomial ring in the mode variables below depth m”; and “Their source mapping complex commutes with the allowed scalar extensions ... and the continuous linear averaging adjunctions.”

The proposed argument is carefully structured: resolutions of differences between depth vacua establish Ext continuity, which supplies target mapping base change; source mapping base change then allows the point equivalence to be tested at residue fields. I checked the formal bootstrap after these hypotheses, including the use of finite Tor dimension and the distinction between compact objects in the renormalized category and arbitrary ordinary modules.

The unresolved part is the claimed control of the source and target mapping complexes in the moving-divisor category. In particular, I have not verified that the filtered resolutions at every successive kernel have exactly the stated finite-presentation property for the nonlinear W-mode action, nor that averaging to a common adolescent stage retains the specific source mapping base-change comparison invoked in the proposition. The coherence of the polynomial associated-graded ring is useful, but its application requires checking strictness and the finite-depth presentation throughout the inductively constructed resolutions. These are the hypotheses on which the residue-field argument depends.

Consequence: without this verification the common target over collision schemes, and hence the subsequent extension of the local comparison, remains unconfirmed. Pointwise Feigin–Frenkel and Skryabin statements alone do not supply this family identification.

Possible resolution: give an explicit filtered presentation for one general inductive kernel, proving the strict surjection and associated-graded finite presentation, and spell out the source mapping base-change square after passage to a common adolescent stage. This would isolate the family upgrade from the imported point theorem.

Principal checks performed

I checked the following connections and calculations while reading the complete manuscript:

* The level conversion a=-c and d=-1/(rc), with the integral determinant transport on the source, is algebraically consistent. Non-real irrational parameters satisfy the nonintegrality test used for every nonzero integral inertia weight.
* In the HN cutoff, dominance supplies the displayed lower root-slope bound, and the remaining simple-root inequalities give a bounded region independent of the irrational exponent. The spectator formulation is used consistently later.
* The logarithm colimit argument distinguishes finite-stage vanishing from colimit vanishing. Its universal-coefficient transition multiplies the torsion quotient by h to the appropriate power, accounting for the stabilized images. Conditional on its mixed-lift and uniform-weight hypotheses, the generator-killing argument has the indicated direction of the weight inequality.
* The configuration estimate combines the link bound c'-2n with the compact-support cost 2n' to obtain E-c'. Adding the simplicial shift gives the finite inequality c'+l <= E'-j. This addresses an otherwise serious dependence on the number of marked points.
* The collision argument uses the low-degree unit gap together with the [0,1] amplitude of divisor restriction. Its boundary epimorphism and its comparison through the common target are the relevant steps; the proof does not simply assume that pointwise equivalences glue.
* The level determinant formulas give l^{lv} tensor B^{lv}[-delta] = l_N tensor B^0[-delta_N]. The finite-period calculation also gives 2delta-z+a=delta+e_l, as required. These normalizations agree with the cancellation in the period comparison.
* The Ran proof retains the added marking operations when forgetting the old parameter connection. The principal-parts incidence map, its tensor-power form, and the two-insertion comparison are used in the correct dependency order.
* The final categorical construction has well-typed left and right inverse candidates. Given the two period factorizations and two Plancherel identities, their displayed composites prove the equivalence. The final central-character/component exchange and the torsor automorphism checks agree with the manuscript’s chosen negative modification-component convention.

Ordinary typographical issues

No independent typographical issue is offered as a reason for the verdict.

Conclusion

The full manuscript has been read and its overall dependency structure reviewed. The verdict remains UNCERTAIN because the two specified relative/family verification issues are unresolved. The report does not classify either issue as a proved substantive error; a rejection would require a demonstrated gap or counterexample beyond what I have established here.
