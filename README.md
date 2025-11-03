# Square Words

Let $w_1$ and $w_2$ be two words, both of length >= 4.

Let $L = \min(\text{len}(w_1), \text{len}(w_2))$.

Then, we say $w_1$ and $w_2$ are "square" if there exists an integer $i$ where $2 \leq i \lt L-1$ and $w_1[:i] + w_2[:i] = w_1$ and $w_1[i:] + w_2[i:] = w_2$.

To denote one such "square" pair, we'll use the tuple $(w_1, w_2, i)$.

For example, ("best", "styles", 2) is a "square" pair.

```
w1 | b e|s t
————————————————
w2 | s t|y l e s
————————————————
i  | 0 1|2 3 4 5
```

[![Best Styles Zaandam](best_styles.png)](https://maps.app.goo.gl/M9aW4FrkTYkj9KKq9)

---

First, I used the MacOS dictionary to get a list of lowercase words of length >= 4

```bash
awk '/.{4,}/ { print tolower($0) }' /usr/share/dict/words | uniq > words.txt
```

Then, I found all "square" pairs using

```bash
python square_pairs.py
```

This outputs a list of "square" pairs in `square_pairs.json.gz`. Uncompressed, it looks like

```
[
  ["aani", "styles", 2],
  ["abac", "acajou", 2],
  ["abac", "acana", 2],
  ...
]
```

For exploring these square pairs, `proc.py` is a good starting point.
