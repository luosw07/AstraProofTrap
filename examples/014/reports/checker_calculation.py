"""Exact actual-run counterexamples to the shortest-projective-arc rule."""
from fractions import Fraction as F

def theta(v):
    x,y=3*v[0],v[1]-v[2]
    return ((1+y/x) if abs(y)<=abs(x) else (3-x/y))%4

def tau(v):return (v[1],v[0],v[2])
for K in [1,1025,2**28+1,10**12]:
    w=tuple(map(F,[4*K+3,-4*K-4,1]));c=(1,-1,0)
    p=tuple(w[i]+w[1]*c[i] for i in range(3))
    assert sum(w)==0 and p==(-1,0,1)
    def V(k):return tuple((1+k)*p[i]-w[1]*c[i] for i in range(3))
    a,b,m=V(K),p,V(2*K+1)
    assert m==tuple(2*(K+1)*v for v in [1,-2,1])
    assert a[1]-a[2]<0 and b[1]-b[2]<0
    assert (theta(a),theta(b),theta(m))==(F(4,9),F(4,3),F(0))
    assert F(4,3)-F(4,9)<2
    assert (theta(tau(a)),theta(tau(b)),theta(tau(m)))==(F(5,6),F(3),F(1))
    assert 4-F(3)+F(5,6)<2
    # Signed endpoint angle is obtuse; squared cosine is exactly 1/13.
    dot=sum(x*y for x,y in zip(a,b))
    assert dot<0 and dot**2*13==sum(x*x for x in a)*sum(x*x for x in b)
assert F(7,8)-F(5,6)==F(1,24)
print('Actual tail vectors, common half-plane, omitted direction and tau_2 verified exactly.')
print('Checked K=1, 1025, 2^28+1, 10^12; signed endpoint angle is obtuse.')
print('The false transformed arc ends at 5/6; a peak starting at 7/8 has gap 1/24.')
