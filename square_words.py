import time
import json
import gzip
from collections import defaultdict


if __name__ == "__main__":
    t = time.time()

    with open("words.txt") as f:
        words = [line.strip() for line in f if line.strip()]

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
        for i in range(2, len(w1) - 1):
            matching_words = prefix_index.get((w1[i:], i), set())
            for w2 in matching_words:
                if w1 == w2 or len(w2) <= i - 1:
                    continue
                if w1[:i] + w2[:i] == w1 and w1[i:] + w2[i:] == w2:
                    square_words.append((w1, w2, i))

        if processed % 1000 == 0:
            print(f"{processed/len(words)*100:.2f}%\r", end="")

    print("matches:", len(square_words))
    print("time:", time.time() - t, "secs")

    print(f"Saving to file")

    with gzip.open("square_words.json.gz", "wt", encoding="utf-8") as f:
        json.dump(square_words, f)
