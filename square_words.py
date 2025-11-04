import time
import json
import gzip
from collections import defaultdict


if __name__ == "__main__":
    t = time.time()

    with open("freqs.json", "r") as f:
        freqs = json.load(f)

    words = [word for word, freq in freqs.items() if freq > 5000]

    print(f"Loaded {len(words)} words")

    prefix_index = defaultdict[tuple[str, int], set](set)

    # Build prefix index for quick lookup
    for word in words:
        for i in range(2, len(word) - 1):
            prefix = word[:i]
            prefix_index[(prefix, i)].add(word)

    print(f"Built index, processing...")

    square_words = []

    for processed, w1 in enumerate(words):
        if len(w1) % 2 == 1:
            continue
        i = len(w1) // 2
        matching_words = prefix_index.get((w1[i:], i), set())
        for w2 in matching_words:
            if w1 == w2 or len(w2) <= len(w1):
                continue
            if w1[:i] + w2[:i] == w1 and w1[i:] + w2[i:] == w2:
                square_words.append((w1, w2, i))

        if processed % 1000 == 0:
            print(f"{processed/len(words)*100:.2f}%\r", end="")

    print("matches:", len(square_words))
    print("time:", time.time() - t, "secs")

    print("Done processing. Now sorting...")
    square_words.sort(key=lambda x: freqs[x[0]] + freqs[x[1]], reverse=True)

    print("Done sorting. Now computing shortlist...")
    shortlist = []
    seen_w1 = set()
    seen_w2 = set()
    for w1, w2, i in square_words:
        if w1 in seen_w1 or w2 in seen_w2:
            continue
        if len(shortlist) >= 1000:
            break
        seen_w1.add(w1)
        seen_w2.add(w2)
        shortlist.append((w1, w2, i))

    print(f"Saving shortlist to file...")
    with open("square_words.json", "wt", encoding="ascii") as f:
        json.dump(shortlist, f)

    print("Saving full list to file...")
    with gzip.open("square_words.json.gz", "wt", encoding="ascii") as f:
        json.dump(square_words, f)
