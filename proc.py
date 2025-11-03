import json


def render(w1, w2, i):
    l = max(len(w1), len(w2))
    a, b = w1[:i], w1[i:]
    c, d = w2[:i], w2[i:]
    return f"""
{a} | {b}
{"-" * (l+3)}
{c} | {d}
"""


with open("square_pairs.json") as f:
    ans = json.load(f)

for w1, w2, i in ans:
    if "pack" in w1 or "pack" in w2:
        print(render(w1, w2, i))


"""
ka | pa
-------
pa | ck
"""
