"""Exact local certificate; see checker_report.md for the admissible stage family."""
from collections import Counter
from itertools import combinations

def max_codegree(edges):
    counts = Counter(pair for edge in edges for pair in combinations(sorted(edge), 2))
    return max(counts.values()), counts

# F_4 is represented additively by two bits. The displayed j*a uses
# integer scalar multiplication, hence (j mod 2)*a in characteristic two.
edges4 = [frozenset((j, b ^ (a if j % 2 else 0)) for j in range(3))
          for b in range(4) for a in range(4)]
m4, counts4 = max_codegree(edges4)
assert len(set(edges4)) == 16
assert counts4[((0, 0), (2, 0))] == 4 and m4 == 4
# With prime Q=5 and the same four slopes, the integer coordinates are distinct.
edges5 = [frozenset((j, (b+j*a) % 5) for j in range(3))
          for b in range(5) for a in range(4)]
m5, _ = max_codegree(edges5)
assert len(set(edges5)) == 20 and m5 == 1
print('Characteristic-two prescribed construction: pair codegree 4 (claimed <=1).')
print('Prime-field construction with the same degree: pair codegree 1.')
