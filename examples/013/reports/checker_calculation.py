"""Exact first-order identities underlying the fixed-grid counterfamily.

The paper's checker supplies the analytic admissibility/tail argument.
Here X=chi_mu*conj(chi_L) is differentiated using its exact TMM factors.
Coefficients are rational; an imaginary coordinate means coefficient of sin(w).
"""
from fractions import Fraction as F

def expansion(x):
    # x=1-cos(w), sin(w)^2=x(2-x).
    ss=x*(2-x)
    def add(a,b):return (a[0]+b[0],a[1]+b[1])
    def mul(a,b):return (a[0]*b[0]-ss*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    def scale(a,b):return (a[0]*b,a[1]*b)
    def conj(a):return (a[0],-a[1])
    z=(1-x,F(1));zp=scale(z,-F(9,8));zm=add(z,(-1,0));zplus=add(z,(1,0))
    A=mul(zm,zm)
    Ap=add(mul(add(zp,(1,0)),zm),mul(zm,add(zp,(2,0))))
    B=mul(z,zplus)
    Bp=add(mul(zp,zplus),mul(z,add(zp,(-1,0))))
    X=mul(A,conj(B));Xp=add(mul(Ap,conj(B)),mul(A,conj(Bp)))
    assert X[0]*x+X[1]*ss==0
    return X[0],Xp[0]*x+Xp[1]*ss

# Both expressions are polynomials in x of degree <=6. Seven distinct
# rational points therefore certify these polynomial identities exactly.
for x in map(F,[0,F(1,4),F(1,2),F(3,4),1,F(3,2),2]):
    real,d=expansion(x)
    assert real==-2*x*(2-x)
    assert d==x*(3-F(7,4)*x)
# On the entire permitted band: 1 < x < 1+sqrt(2)/2 < 12/7.
assert F(2)<F(10,7)**2
assert 3-F(7,4)*F(12,7)==0
# Consequently D/epsilon is a strictly negative weighted average, for
# every nonzero nonnegative kernel weighting, regardless of grid size.
for q in [12,24,100]:
    for J in [1,4,16,100]:
        P=6*q*J
        for j in range(1,2*J+1):
            a=F(2*j-1-2*J,2*J)
            turns=F(1,3)*(1+a/q)
            assert (P*turns).denominator==1
print('Exact TMM first-order identities and strict band sign verified.')
print('P=6qJ is a common period; n=P-1 reverses the lag-one sine phases.')
print('For every fixed J, the positive slack combination / epsilon tends to (n+1)D_* < 0.')
