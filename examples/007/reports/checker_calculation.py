"""Independent exact current-action checks; standard library only.

Scalars are Q[t,epsilon]/epsilon^3 (all coefficients here are integers).
Coefficient basis: z^r U^j, r=0,1, 0<=j<n, with z^2=U+parameter.
No tricker computation or report is imported.
"""

ZERO = {}
ONE = {(0, 0): 1}
A = {(2, 0): 1}
B = {(2, 0): 1, (1, 1): 2, (0, 2): 1}

def add(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, 0) + v
        if not out[k]:
            del out[k]
    return out

def scale(p, c):
    return {k: c*v for k, v in p.items() if c*v}

def mul(p, q):
    out = {}
    for (i, j), v in p.items():
        for (k, l), w in q.items():
            if j+l < 3:
                out = add(out, {(i+k, j+l): v*w})
    return out

def put(m, key, p):
    v = add(m.get(key, ZERO), p)
    if v:
        m[key] = v
    else:
        m.pop(key, None)

def madd(m, n, sign=1):
    out = dict(m)
    for k, p in n.items():
        put(out, k, scale(p, sign))
    return out

def mmul(m, n):
    out = {}
    rows = {}
    for (i, j), p in n.items():
        rows.setdefault(i, []).append((j, p))
    for (i, k), p in m.items():
        for j, q in rows.get(k, []):
            put(out, (i, j), mul(p, q))
    return out

def mscale(m, p):
    return {k: v for k, q in m.items() if (v := mul(p, q))}

# Root indices e=0,h=1,f=2; tuple is (output root, coefficient).
ROOT_BRACKET = {
    (0, 1): (0, -2), (1, 0): (0, 2),
    (0, 2): (1, 1), (2, 0): (1, -1),
    (1, 2): (2, -2), (2, 1): (2, 2),
}

def basis(n):
    return [(x, r, j) for j in range(n) for r in range(2) for x in range(3)]

def product(r, j, s, k, n, parameter):
    if r+s < 2:
        return [((r+s, j+k), ONE)] if j+k < n else []
    out = []
    if j+k < n:
        out.append(((0, j+k), parameter))
    if j+k+1 < n:
        out.append(((0, j+k+1), ONE))
    return out

def bracket(x, y, n, parameter):
    a, r, j = x
    b, s, k = y
    if (a, b) not in ROOT_BRACKET:
        return []
    c, v = ROOT_BRACKET[a, b]
    return [((c, R, J), scale(p, v))
            for (R, J), p in product(r, j, s, k, n, parameter)]

def matrices(n, parameter):
    bs = basis(n)
    index = {b: i for i, b in enumerate(bs)}
    result = {}
    for x in bs:
        m = {}
        for col, y in enumerate(bs):
            for z, p in bracket(x, y, n, parameter):
                put(m, (index[z], col), p)
        result[x] = m
    return result

def defect(x, y, n, parameter, actions):
    out = madd(mmul(actions[x], actions[y]), mmul(actions[y], actions[x]), -1)
    for z, p in bracket(x, y, n, parameter):
        out = madd(out, mscale(actions[z], p), -1)
    return out

def scalar_terms(p):
    return [{"t_degree": i, "epsilon_degree": j, "coefficient": c}
            for (i, j), c in sorted(p.items())]

def run(n, minimum_depth, x, y, expected_row):
    src, dst = matrices(n, A), matrices(n, B)
    currents = [b for b in basis(n) if b[2] >= minimum_depth]
    count = 0
    for u in currents:
        for v in currents:
            assert not defect(u, v, n, A, src), ("source", u, v)
            assert not defect(u, v, n, B, dst), ("target", u, v)
            count += 1
    failed = defect(x, y, n, B, src)
    expected = {(1, 1): -4, (0, 2): -2}
    assert failed.get((expected_row, 0)) == expected
    collision = {mon: c for mon, c in expected.items() if mon[0] == 0}
    assert collision == {(0, 2): -2}
    return {
        "jet_order": n,
        "representation_rank": len(basis(n)),
        "minimum_current_depth": minimum_depth,
        "genuine_source_relations_verified": count,
        "genuine_target_relations_verified": count,
        "copied_action_is_representation": False,
        "test_currents": [list(x), list(y)],
        "nonzero_defect_entry_row_column": [expected_row, 0],
        "defect_entry": scalar_terms(expected),
        "collision_defect_entry": scalar_terms(collision),
        "first_order_collision_defect": "zero",
        "full_family_first_order_defect": "-4*t*epsilon",
    }

results = {
    "ring": "Q[t,epsilon]/(epsilon^3)",
    "basis": "e*z^r*U^j, h*z^r*U^j, f*z^r*U^j; j then r then root",
    "defect_convention": "[rho(x),rho(y)] - rho([x,y]_target)",
    "arc_jet": run(1, 0, (0, 1, 0), (2, 1, 0), 0),
    "positive_congruence": run(4, 1, (0, 1, 1), (2, 1, 1), 12),
    "all_assertions_passed": True,
}
print("PASS: exact algebra certificate")
for name in ("arc_jet", "positive_congruence"):
    result = results[name]
    print(f"Rank {result['representation_rank']}: "
          f"{result['genuine_source_relations_verified']} source and "
          f"{result['genuine_target_relations_verified']} target relations verified.")
    print("Copied action fails: defect = -4*t*epsilon - 2*epsilon^2; "
          "at t=0, defect = -2*epsilon^2.")
