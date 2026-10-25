#!/usr/bin/env python3
"""Neue veröffentlichte Posts halbautomatisch auf LinkedIn teilen.

Aufruf nach dem Commit: ./linkedin_post.py [--dry-run] [--seed]
Öffnet pro Post einen vorausgefüllten Teilen-Dialog im Browser; nach dem
Posten im Terminal bestätigen. Bereits geteilte Slugs stehen in linkedin_posted.txt.
"""

import argparse
import subprocess
import sys
import urllib.parse

from mastodon_post import BASEDIR, is_online, post_url, published_posts, toot_text

STATEFILE = BASEDIR / "linkedin_posted.txt"
MAX_POSTS = 3


def share_url(post):
    return "https://www.linkedin.com/feed/?shareActive=true&text=" + urllib.parse.quote(toot_text(post))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true", help="nur anzeigen, nichts öffnen")
    parser.add_argument("--seed", action="store_true", help="alle veröffentlichten Posts als geteilt markieren")
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

    if args.dry_run:
        for post in new:
            status = "online" if is_online(post_url(post)) else "noch nicht online"
            print(f"--- {post['slug']} ({status})\n{toot_text(post)}\n{share_url(post)}\n")
        return

    shared = 0
    for post in new:
        if not is_online(post_url(post)):
            print(f"Übersprungen, noch nicht online: {post_url(post)}")
            continue
        subprocess.run(["open", share_url(post)], check=True)
        if input(f"{post['slug']}: auf LinkedIn gepostet? [j/N] ").strip().lower() != "j":
            continue
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
