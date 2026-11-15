#!/usr/bin/env python3
"""Exact pointwise check of the moving-frame term in case 009.

The full admissible flow is in reports/checker.md. At t=x=z=0 use
U=exp(-x)*partial_z, L=exp(-z)*partial_x, N=partial_y, orthonormal for
h=exp(2*x)*dz^2+exp(2*z)*dx^2+dy^2. Write A=exp(-x), B=exp(-z).
Then [U,L]=B*U-A*L, Theta_UL=B/2, Theta_LL=-A, w=B*e_l.
U(A)=0, U(B)=-A*B, L(A)=-A*B, L(B)=0. The tables below evaluate
these functions and their derivatives at A=B=1; the connection is
computed from the brackets, rather than taken from the disputed identity.
"""

from fractions import Fraction as F


def main():
    n = 3
    # C[i][j][k] = <[E_i,E_j],E_k>, E=(U,L,N).
    C = [[[F(0) for _ in range(n)] for _ in range(n)] for _ in range(n)]
    C[0][1] = [F(1), F(-1), F(0)]
    C[1][0] = [F(-1), F(1), F(0)]
    connection = [[[F(C[i][j][k] - C[j][k][i] + C[k][i][j], 2)
                    for k in range(n)] for j in range(n)] for i in range(n)]
    theta = [[F(0), F(1, 2), F(0)], [F(1, 2), F(-1), F(0)], [F(0)] * n]
    derivative = [[[F(0) for _ in range(n)] for _ in range(n)] for _ in range(n)]
    derivative[0][0][1] = derivative[0][1][0] = F(-1, 2)
    derivative[1][1][1] = F(1)

    def covariant(i, j, k):
        return derivative[i][j][k] - sum(
            connection[i][j][a] * theta[a][k]
            + connection[i][k][a] * theta[j][a] for a in range(n))

    # q=Theta(U,-)=dx/2, w=dx; compute exterior derivatives in this frame.
    q = theta[0]
    w = [F(0), F(1), F(0)]
    dq_ul = derivative[0][0][1] - derivative[1][0][0] - sum(
        C[0][1][a] * q[a] for a in range(n))
    dw_ul = F(-1) - sum(C[0][1][a] * w[a] for a in range(n))
    actual = covariant(0, 0, 1) - covariant(1, 0, 0)
    modified = dw_ul / 2
    correction = sum(w[a] * theta[a][1] for a in range(n)) / 2
    assert dq_ul == dw_ul == 0
    assert covariant(0, 0, 1) == F(-3, 2)
    assert covariant(1, 0, 0) == -1
    assert actual == correction == F(-1, 2)
    assert actual != modified
    assert actual == modified + correction
    print(f"actual {actual}; modified {modified}; corrected {modified + correction}")


if __name__ == "__main__":
    main()
