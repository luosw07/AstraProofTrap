#!/usr/bin/env python3
"""Exact two-party witness for case 010, using Q(sqrt(2)) and both tie branches."""
from dataclasses import dataclass
from fractions import Fraction as F
from functools import total_ordering


@total_ordering
@dataclass(frozen=True)
class Q:
    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        other = other if isinstance(other, Q) else Q(F(other))
        return Q(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.a, -self.b)

    def __sub__(self, other):
        return self + -(other if isinstance(other, Q) else Q(F(other)))

    def __mul__(self, scalar):
        return Q(self.a * scalar, self.b * scalar)

    __rmul__ = __mul__

    def sign(self):
        a, b = self.a, self.b
        if not b:
            return (a > 0) - (a < 0)
        if not a or (a > 0) == (b > 0):
            return 1 if b > 0 else -1
        # Compare rational squares; sqrt(2) is irrational.
        return ((a*a > 2*b*b) - (a*a < 2*b*b)) * (1 if a > 0 else -1)

    def __lt__(self, other):
        return (self - other).sign() < 0


def image(intervals, p):
    """Image under x -> x+p (<=1/2), x+p-1 (>=1/2)."""
    half, one = Q(F(1, 2)), Q(F(1))
    pieces = []
    for lo, hi in intervals:
        lo, hi = lo + p, hi + p
        if lo <= half:
            pieces.append((lo, min(hi, half)))
        if hi >= half:
            pieces.append((max(lo, half) - one, hi - one))
    # Merge overlapping closed intervals, retaining isolated singleton images.
    merged = []
    for lo, hi in sorted(pieces):
        if merged and lo <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
        else:
            merged.append((lo, hi))
    return merged


def main():
    eps, quarter, half, one = Q(F(0), F(1, 1000)), Q(F(1, 4)), Q(F(1, 2)), Q(F(1))
    p = quarter + eps
    assert Q() < p < one and p.b != 0  # Positive irrational vote, hence ergodic.
    B = [(-2*eps, 2*eps)]
    assert -half < B[0][0] < B[0][1] < half
    first, second = image(B, p), image(image(B, p), p)
    assert first == [(quarter-eps, quarter+3*eps)]
    assert second == [(-half, -half+4*eps), (half, half)]
    assert second[0][1] < half  # The second component is an isolated point.
    assert 176*(4*eps) < one < 177*(4*eps)
    # A cover through M contains M+1 intervals of measure 4*eps.
    # M<=175 is impossible; every covering horizon includes the bad n=2.
    print("B and TB are nondegenerate intervals.")
    print("T^2 B = [-1/2, -1/2 + 4*epsilon] union {1/2}; the singleton is isolated.")
    print("176*(4*epsilon) < 1; every covering horizon M is at least 176.")


if __name__ == "__main__":
    main()
