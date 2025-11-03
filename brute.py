import time
import json


def good(w1: str, w2: str) -> (int, bool):
    """
    0 1 2 3 4 5

    b e|s t           a | b
    ------------      -----
    s t|y l e s       c | d
        ^                 ^
        i                 i
    """
    l = min(len(w1), len(w2))
    for i in range(2, l - 1):
        a, b = w1[:i], w1[i:]
        c, d = w2[:i], w2[i:]
        if a + c == w1 and b + d == w2:
            return i, True
    return -1, False


with open("words.txt") as f:
    words = [i.strip() for i in f.readlines()]

answers = []

x = 0

t = time.time()
for w1 in words:
    for w2 in words:
        x += 1
        if x % 1000000 == 0:
            print(f"{x/(len(words)*len(words))*100}%")
        if w1 == w2:
            continue
        l = min(len(w1), len(w2))
        for i in range(2, l - 1):
            a, b = w1[:i], w1[i:]
            c, d = w2[:i], w2[i:]
            if a + c == w1 and b + d == w2:
                answers.append((w1, w2, i))
print("time:", time.time() - t)

with open("square_pairs.json", "w") as f:
    json.dump(answers, f)

print(good("best", "styles"))  # True
print(good("styles", "best"))  # False
print(good("styles", "dest"))  # False
