# Tricker report

## 1. A permitted local resonance model

Use the coefficient and finite fields

\[
k=\overline{\mathbb Q}_3,\qquad q=5,
\]

and the split dual group \(L=\operatorname{Sp}_4\), with split \(G=\operatorname{SO}_5\). Write the symplectic form and the standard triple as

\[
\Omega=\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix},\quad
e_0=\begin{pmatrix}0&I_2\\0&0\end{pmatrix},\quad
f_0=\begin{pmatrix}0&0\\I_2&0\end{pmatrix},\quad
h=\operatorname{diag}(I_2,-I_2).
\]

Direct multiplication gives \([e_0,f_0]=h\), \([h,e_0]=2e_0\), and \([h,f_0]=-2f_0\). The group homomorphism is

\[
\phi\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\begin{pmatrix}aI_2&bI_2\\cI_2&dI_2\end{pmatrix},
\qquad
m(z)=\operatorname{diag}(zI_2,z^{-1}I_2).
\]

This is the nilpotent orbit of partition \((2,2)\). For

\[
d=4\cdot3^N,\quad s=5^{d/2}=25^{3^N},\quad r=5^d=s^2,
\qquad t=m(s),
\]

the local Arthur compact factor is \(c=1\). Thus algebraicity, compactness at all complex embeddings, and commutation with the triple hold. The length-zero group for the chosen \(G\) has order two, so the degree condition holds. Moreover

\[
v_3(25^{3^N}-1)=N+1.
\]

For completeness, the equality follows from \(v_3(25-1)=1\) and
\(a^3-1=(a-1)(a^2+a+1)\): when \(a\equiv1\pmod3\), the second factor has valuation exactly one. The chosen classes can therefore lie in any of the sufficiently small identity congruence neighborhoods used in Lemma 3.1.

The full centralizer is

\[
H=Z_L(t)=\{\operatorname{diag}(g,g^{-\mathsf t}):g\in\operatorname{GL}_2\}
\simeq\operatorname{GL}_2.
\]

It is connected, and \(m\) is central in it. The nontrivial central translate \(-t\) has a different eigenvalue multiset: coincidence would require \(s^2=-1\), whereas \(s^2=5^d\). Hence the adjoint centralizer is connected as well, and the central-torsor condition does not exclude this model.

The positive and negative resonance spaces are

\[
E_+=\left\{\begin{pmatrix}0&Y\\0&0\end{pmatrix}:Y=Y^{\mathsf t}\right\},
\qquad
W=\left\{\begin{pmatrix}0&0\\X&0\end{pmatrix}:X=X^{\mathsf t}\right\}.
\]

Their \(m\)-weights are \(2\) and \(-2\). The \(H\)-actions are

\[
Y\longmapsto gYg^{\mathsf t},\qquad
X\longmapsto g^{-\mathsf t}Xg^{-1}.
\]

The open orbit in \(E_+\) consists of invertible symmetric matrices, with reductive stabilizer \(O_2\); the paper permits this stabilizer to be disconnected. These resonance representations factor through \(H/Z(L)\), and \(m(-1)=-I_4\) acts trivially on them. Thus the counterexample uses the neutral, even sectors retained by the actual proof. The central holonomy correction in §5 acts trivially in the adjoint representation and leaves all these equations unchanged.

## 2. A residual holonomy that survives every allowed slice shrinking

Take

\[
g=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
u=\operatorname{diag}(g,g^{-\mathsf t})\in H.
\]

This is a nontrivial unipotent element. Every saturated neighborhood of the identity quotient class in Lemma 6.1 contains it. Consequently shrinking the slice, as allowed elsewhere in the argument, cannot remove this counterexample.

Write a negative-resonance vector as

\[
X=\begin{pmatrix}x_1&x_2\\x_2&x_3\end{pmatrix}.
\]

The actual action is

\[
g^{-\mathsf t}Xg^{-1}
=\begin{pmatrix}
x_1&x_2-x_1\\
x_2-x_1&x_3-2x_2+x_1
\end{pmatrix}.
\]

Thus, in the vector-coordinate convention expressly fixed in §6.2,

\[
J=J_u=\begin{pmatrix}
0&0&0\\-1&0&0\\1&-2&0
\end{pmatrix}.
\tag{C1}
\]

In particular, the unchanged negative equation algebra has

\[
d\theta_1=0,\qquad d\theta_2=-x_1,
\qquad d\theta_3=x_1-2x_2.
\tag{C2}
\]

These three scalar equalities eliminate any ambiguity about whether a displayed matrix acts on coordinate columns or coefficient columns.

## 3. The advertised algebra action is not a chain map

The augmentation resolution (6.6), lines 3189–3193, is unchanged. It has

\[
dp_i=x_i,\qquad dl=\theta-Jp.
\]

In the present example this reads

\[
dl_1=\theta_1,\qquad
dl_2=\theta_2+p_1,\qquad
dl_3=\theta_3-p_1+2p_2.
\tag{C3}
\]

Here \(p_i\) have degree \(-1\), and \(l_i\) have degree \(-2\). Set

\[
\eta_i=-\partial_{p_i},\qquad \beta_i=\partial_{l_i}.
\]

The differential on the endomorphism complex is the graded commutator. Both \(d\) and \(\eta_i\) are odd, so \([d,\eta_i]=d\eta_i+\eta_i d\). Applying it to the generators in (C3) gives

\[
\begin{aligned}
[d,\eta_1]&=-\beta_2+\beta_3,\\
[d,\eta_2]&=-2\beta_3,\\
[d,\eta_3]&=0.
\end{aligned}
\tag{C4}
\]

For example, \([d,\eta_1](l_2)=-1\), while \([d,\eta_1](l_3)=1\). In general the identical calculation gives

\[
[d,-\partial_{p_j}]=\sum_iJ_{ij}\partial_{l_i},
\qquad\text{that is,}\qquad d\eta=J^{\mathsf t}\beta.
\tag{C5}
\]

The modified algebra instead requires

\[
d\eta_1=0,\qquad d\eta_2=-\beta_1,
\qquad d\eta_3=\beta_1-2\beta_2.
\tag{C6}
\]

In particular it declares \(\eta_1\) closed. Its proposed image has nonzero differential by (C4). The purported map to endomorphisms of \(K'\), and hence the specific polynomial-dual map to \(\underline{\operatorname{RHom}}(A_0,A_0)\), fails to commute with differentials. Changing the sign of an odd derivative multiplies a column by a scalar; it cannot turn the nonzero first row of \(J^{\mathsf t}\) into the zero first row of \(J\).

The modified formula does define an ordinary dg algebra after forgetting equivariance: its coefficients and the \(\beta_i\) are closed, so its differential squares to zero. The failure is in the asserted acting algebra, its particular action, and its equivariant identification with the actual fixed-vector model. These are the structures used to define the coherent realization.

## 4. Independent, basis-independent obstruction: equivariance fails

There is an additional obstruction that rules out repairing (C6) by a harmless choice of local bases. The element \(u\) itself centralizes the base point \(u\in U_H\). It must therefore act on the specialized dg algebra with its prescribed \(H\)-equivariant structure. The generators \(\eta_i,\beta_i\) are the copies of \(W\) specified in (6.7). On their basis elements its action is

\[
\begin{array}{lll}
u\beta_1=\beta_1-\beta_2+\beta_3,&
u\beta_2=\beta_2-2\beta_3,&u\beta_3=\beta_3,\\
u\eta_1=\eta_1-\eta_2+\eta_3,&
u\eta_2=\eta_2-2\eta_3,&u\eta_3=\eta_3.
\end{array}
\tag{C7}
\]

After shear, the modified differential gives

\[
H^0(B_{\rm bad,u})
=k[\beta_1,\beta_2,\beta_3]/(\beta_1,\beta_2)
=k[\beta_3].
\]

The ideal of boundaries \((\beta_1,\beta_2)\) is not stable under (C7), since \(u\beta_2=\beta_2-2\beta_3\). Thus the modified differential is incompatible even with the stabilizer action at this one base point. The correct boundary ideal is \((\beta_2,\beta_3)\), which is stable.

Equivalently, the representation matrix on the formal generator column is \((I+J)^{\mathsf t}\). It commutes with \(J^{\mathsf t}\) and does not commute with \(J\). This is checked exactly in `verification.py`.

All equivariant structures, the residual group coordinate, the paired generators in (6.6), and the invariant identification \(W^*=E_+\) are fixed elsewhere in the manuscript. Relabeling the unipotent matrix by its transpose would change that base coordinate and its group action. It is not a coordinate change over the stated \(A_0\) that preserves those data.

## 5. The claimed equation scheme both loses a true point and gains a false point

Use the invariant trace pairing on \(\mathfrak{sp}_4\). If

\[
Y=\begin{pmatrix}a&b\\b&c\end{pmatrix}\in E_+,
\]

then pairing with \(X\) above is \(x_1a+2x_2b+x_3c\). Hence the coordinate identification is

\[
(\beta_1,\beta_2,\beta_3)=(a,2b,c).
\tag{C8}
\]

The true fixed-vector equation is

\[
gYg^{\mathsf t}-Y
=\begin{pmatrix}2b+c&c\\c&0\end{pmatrix}=0,
\]

so the fiber of the paper's \(Y\) consists of \(b=c=0\). The correct equation \(J^{\mathsf t}\beta=0\) gives exactly that result. The modified equation \(J\beta=0\) instead gives \(a=b=0\).

In particular:

* \(Y_{\rm true}=\operatorname{diag}(1,0)\) gives a genuine point \((u,e_{Y_{\rm true}})\) of \(Y\) and satisfies \(\operatorname{Ad}(tu)e_{Y_{\rm true}}=r e_{Y_{\rm true}}\). It is excluded by the modified equation.
* \(Y_{\rm false}=\operatorname{diag}(0,1)\) satisfies the modified equation, but \(gY_{\rm false}g^{\mathsf t}=\begin{pmatrix}1&1\\1&1\end{pmatrix}\ne Y_{\rm false}\). Thus it is not a point of the paper's \(Y\).

These computations directly contradict lines 3225–3229 under the manuscript's specified identification \(W^*=E_+\) and unchanged holonomy coordinate. They do not depend on any assumption that the residual unipotent holonomy is the identity. Both rank-one vectors lie in the boundary of the open resonance orbit, the locus used in the final support argument.

The local algebra computation in Proposition 6.3 is asserted for the entire saturated slice and all coherent input modules. The augmentation \(A_0\) is one of those inputs. It does not impose any additional automorphic support restriction on \(u\), and the chosen unipotent point belongs to every permitted slice. This supplies the exact local conditions for the failure. The certificate does not require a global counterexample to the article's conditional main theorem.

## 6. Downstream use and checks that still pass

The false action in §6.2 is used to regard \(G_0\) as a \(B^0\)-module functor, shear it into \(\operatorname{Coh}^H(Y)\), and extend it to Ind-categories. Proposition 6.5 then performs extension of scalars with this algebra to identify the actual flag test objects. Proposition 6.7 and Theorem 6.8 use the same action for the spherical algebra and representation-valued comparisons. Finally Proposition 8.1 needs that comparison to construct its \(B\)-linear cyclic-support map and to transport the vector \(f\) into \(H^0(F_n^{\rm qc})\). The failure concerns the very algebra action used along this chain.

The following local checks remain valid:

* At \(u=1\), both matrices vanish. The augmentation, polynomial generators, degrees, weights, and zero-section calculation agree.
* For a torus centralizer, a weight basis diagonalizes \(J_u\) throughout. The two displayed matrices agree. In particular rank-one tests and the principal \(\mathfrak{sl}_3\) model do not expose this change.
* At an isolated semisimple point one can diagonalize the matrix, so a pointwise eigenvalue check also misses the obstruction to the family with its specified equivariance.
* A matrix and its transpose have the same rank, determinant, characteristic polynomial, and eigenvalues. In the concrete unipotent fiber both equation complexes even have isomorphic underlying abstract cohomology algebras: one polynomial generator and one exterior generator. The wrong generators and the failure of the stabilizer action distinguish them.
* The complete-intersection statements for the original equation schemes, all Frobenius absolute-value estimates, the bad-flag determinant polynomial, and the restored boundary-test definition are unchanged.

Restoring \(J_u^{\mathsf t}\) in (6.7), removing the added same-operator assertion, and restoring the word “transpose” in the subsequent identification repairs this single mechanism.

`verification.py` uses only exact rational arithmetic and the Python standard library. It executes 58 assertions covering the group and triple, resonance operators, the derivative discrepancy, equivariance, both equation-scheme points, congruence conditions, complete-source difference audit, restoration of the preceding mutation, and byte-identical figures. Its saved output is `verification-results.json`.
