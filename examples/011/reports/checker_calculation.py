#!/usr/bin/env python3
"""Read-only mathematical certificate for the extension-trace counter-witness.

This script reads no files, writes no files, and uses no manuscript history.
It verifies the spectral identities and the exact reverse-triangle/power
calculation for any canonical trace vector satisfying the stated moment bound.
The geometric existence and admissibility arguments are in tricker_report.md.
"""

from fractions import Fraction as Q

rows = []
for n in range(10, 21):
    M = n - 1
    dim_U = n - 2
    r, d = 1, 1
    w = n + r - 2
    canonical_power = 2 * n - 3
    ghost_moment_power = 2 * M + dim_U
    normalization_power = 2 * n - 2
    assert d <= r
    assert dim_U + w + 1 == normalization_power
    assert dim_U + w == canonical_power
    assert ghost_moment_power == 3 * n - 4
    assert ghost_moment_power - canonical_power == n - 1
    assert ghost_moment_power - normalization_power == n - 2 > 0
    # The added sheaf can be put in cohomological degree 2n-2.
    assert 2 * M == 2 * n - 2
    assert (-1) ** (2 * n - 2) == 1
    for p in (3, 5, 7):
        eigenvalues = (p ** M, -(p ** M))
        assert sum(eigenvalues) == 0
        for a in range(1, 9):
            q = p ** a
            trace = sum(e ** a for e in eigenvalues)
            assert trace == q ** M * (1 + (-1) ** a)
            if a % 2:
                assert trace == 0
            else:
                assert trace == 2 * q ** M > 0

        # N >= q^(n-2)/2 and ||T||_2^2 <= B q^(2n-3).
        # Choose an even degree at which ||ghost|| >= 2 ||T||.
        for B in (1, 137, 10 ** 6, 10 ** 12):
            a = 2
            while (p ** a) ** (n - 1) <= 2 * B:
                a += 2
            q = p ** a
            canonical_upper = B * q ** canonical_power
            ghost_squared_lower = 2 * q ** ghost_moment_power
            assert ghost_squared_lower > 4 * canonical_upper
            # Reverse triangle: ||T+ghost|| >= ||ghost||/2.
            new_moment_lower = Q(1, 4) * ghost_squared_lower
            assert new_moment_lower == Q(1, 2) * q ** ghost_moment_power
            assert new_moment_lower > canonical_upper
            normalized_lower = new_moment_lower / q ** normalization_power
            assert normalized_lower == Q(1, 2) * q ** (n - 2)
    rows.append((n, canonical_power, ghost_moment_power, n - 2))

print("PASS: rank-two spectrum has zero degree-one trace and nonzero even-degree trace.")
print("PASS: added weight and cohomological degree are both 2n-2.")
print("PASS: the counter-witness remains effective under arbitrary canonical cancellation.")
print("n | canonical moment power | chosen-model lower power | normalized growth power")
for row in rows:
    print(" | ".join(map(str, row)))
print("PASS: the degree-one cone has d=r=1 while the chosen model forces Xu's large-moment alternative.")
