![Square Words](logo.svg)

# Square Words

Let $w_1$ and $w_2$ be two words, both of length >= 4.

Let $L = \min(\text{len}(w_1), \text{len}(w_2))$.

Then, we say $w_1$ and $w_2$ are _square_ if there exists an integer $i$ where $2 \leq i \lt L-1$ and $w_1[:i] + w_2[:i] = w_1$ and $w_1[i:] + w_2[i:] = w_2$.

To denote one such _square pair_, we'll use the tuple $(w_1, w_2, i)$.

For example, ("best", "styles", 2) is a _square pair_.

![Square Pair Example](square_pair_example.svg)

[
![Best Styles Zaandam](best_styles.png)
📍 Best Styles Zaandam, Netherlands
](https://maps.app.goo.gl/M9aW4FrkTYkj9KKq9)

---

First, I used the MacOS dictionary to get a list of lowercase words of length >= 4

```bash
awk '/.{4,}/ { print tolower($0) }' /usr/share/dict/words | uniq > words.txt
```

Then, I found all _square pairs_ using

```bash
python square_pairs.py
```

This outputs a list of _square pairs_ in `square_pairs.json.gz`. Uncompressed, it looks like

```
[
  ["best", "styles", 2],
  ["mike", "kebab", 2],
  ["atomic", "michael", 3],
  ...
]
```
