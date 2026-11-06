#!/usr/bin/env python3
"""Neue veröffentlichte Posts halbautomatisch auf LinkedIn teilen.

Aufruf nach dem Commit: ./linkedin_post.py [--dry-run] [--seed] [--text TEXT] [--tags TAGS]
Öffnet pro Post einen vorausgefüllten Teilen-Dialog im Browser und trägt den
Slug ohne Rückfrage in linkedin_posted.txt ein ("Posten" klickt man selbst).
"""

import argparse
import subprocess
import sys
import urllib.parse

from mastodon_post import BASEDIR, is_online, post_url, published_posts, toot_text

STATEFILE = BASEDIR / "linkedin_posted.txt"
MAX_POSTS = 3


def share_url(text):
    return "https://www.linkedin.com/feed/?shareActive=true&text=" + urllib.parse.quote(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true", help="nur anzeigen, nichts öffnen")
    parser.add_argument("--seed", action="store_true", help="alle veröffentlichten Posts als geteilt markieren")
    parser.add_argument("--text", help="eigener Text statt Titel (nur bei genau einem neuen Post)")
    parser.add_argument("--tags", help="eigene Tags statt der Post-Tags, z.B. \"a, b, c\" (nur bei genau einem neuen Post)")
    args = parser.parse_args()

    posted = set(STATEFILE.read_text().split()) if STATEFILE.exists() else set()
    new = [p for p in published_posts() if p["slug"] not in posted]

    if args.seed:
        with STATEFILE.open("a") as f:
            for post in new:
                f.write(post["slug"] + "\n")
        print(f"{len(new)} Slugs eingetragen.")
        return

    if not new:
        print("Nichts Neues.")
        return
    if len(new) > MAX_POSTS:
        sys.exit(f"{len(new)} neue Posts (> {MAX_POSTS}) – linkedin_posted.txt prüfen. Abbruch.")
    if (args.text or args.tags) and len(new) > 1:
        sys.exit("--text/--tags nur bei genau einem neuen Post möglich.")

    if args.dry_run:
        for post in new:
            status = "online" if is_online(post_url(post)) else "noch nicht online"
            text = toot_text(post, args.text, args.tags)
            print(f"--- {post['slug']} ({status})\n{text}\n{share_url(text)}\n")
        return

    shared = 0
    for post in new:
        if not is_online(post_url(post)):
            print(f"Übersprungen, noch nicht online: {post_url(post)}")
            continue
        subprocess.run(["open", share_url(toot_text(post, args.text, args.tags))], check=True)
        print(f"Teilen-Dialog geöffnet: {post['slug']}")
        with STATEFILE.open("a") as f:
            f.write(post["slug"] + "\n")
        shared += 1

    if not shared:
        return
    subprocess.run(["git", "add", STATEFILE.name], cwd=BASEDIR, check=True)
    subprocess.run(
        ["git", "commit", "-m", "docs: linkedin_posted.txt aktualisieren", "--", STATEFILE.name],
        cwd=BASEDIR, check=True,
    )


if __name__ == "__main__":
    main()
