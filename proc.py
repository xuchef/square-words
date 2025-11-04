import gzip
import os
from collections import defaultdict
import json
import threading


def download(identifier):
    print(f"Downloading {identifier}")
    os.system(
        f"curl 'https://storage.googleapis.com/books/ngrams/books/20200217/eng/1-{identifier}-of-00024.gz' --output {identifier}.tsv.gz"
    )


def delete(identifier):
    print(f"Deleting {identifier}")
    os.remove(f"{identifier}.tsv.gz")


def process(identifier, match_count_threshold=100):
    print(f"Processing {identifier}")
    ans = defaultdict(int)
    with gzip.open(f"{identifier}.tsv.gz", "rt") as f:
        for line in f:
            parts = line.split("\t")
            word = parts[0].lower()
            word = word.split("_")[0]
            if not (word.isalpha() and word.isascii()):
                continue
            if len(word) < 4:
                continue
            year, match_count, volume_count = parts[-1].split(",")
            if int(match_count) < match_count_threshold:
                continue
            ans[word] += int(match_count)
    print("Found", len(ans), "words")
    with open(f"{identifier}.json", "w") as f:
        json.dump(dict(ans), f)


def run(identifier):
    download(identifier)
    process(identifier, 100)
    delete(identifier)


if __name__ == "__main__":
    threads = []
    for i in range(24):
        identifier = f"{i:05d}"
        t = threading.Thread(target=run, args=(identifier,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    ans = {}
    for i in range(24):
        identifier = f"{i:05d}"
        with open(f"{identifier}.json", "r") as f:
            ans.update(json.load(f))
    print("Found", len(ans), "words")
    with open("freqs.json", "w") as f:
        json.dump(ans, f)
