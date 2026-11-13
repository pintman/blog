#!/usr/bin/env python3
"""Liste aller Tags veröffentlichter Posts. Aufruf: ./tags.py [-c]"""

import argparse
from collections import Counter

from mastodon_post import published_posts


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("-c", "--count", action="store_true",
                   help="Anzahl Artikel je Tag ausgeben (sortiert nach Häufigkeit)")
    args = p.parse_args()
    # Groß-/Kleinschreibung zusammenfassen (wie Pelican); Anzeige: häufigste Schreibweise
    counter = Counter()
    variants = {}
    for post in published_posts():
        tags = {t.strip() for t in post.get("tags", "").split(",") if t.strip()}
        for key in {t.lower() for t in tags}:
            counter[key] += 1
        for t in tags:
            variants.setdefault(t.lower(), Counter())[t] += 1
    counter = Counter({variants[k].most_common(1)[0][0]: n for k, n in counter.items()})
    if args.count:
        for tag, n in sorted(counter.items(), key=lambda x: (-x[1], x[0].lower())):
            print(f"{n}\t{tag}")
    else:
        for tag in sorted(counter, key=str.lower):
            print(tag)


if __name__ == "__main__":
    main()
