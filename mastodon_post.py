#!/usr/bin/env python3
"""Neue veröffentlichte Posts nach Mastodon tooten.

Aufruf nach dem Commit: ./mastodon_post.py [--dry-run] [--seed]
Token in .env: MASTODON_TOKEN=..., optional MASTODON_INSTANCE=https://chaos.social
Bereits getootete Slugs stehen in mastodon_posted.txt.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata
import urllib.request
from pathlib import Path

BASEDIR = Path(__file__).resolve().parent
STATEFILE = BASEDIR / "mastodon_posted.txt"
ENVFILE = BASEDIR / ".env"
SITEURL = "https://blog.bakera.de"
MAX_TOOTS = 3


def load_env():
    if ENVFILE.exists():
        for line in ENVFILE.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def slugify(text):
    # wie Pelicans Default-Slugify: Akzente entfernen, Nicht-Alphanumerisches -> "-"
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^\w]+", "-", text.lower()).strip("-")


def parse_md(text):
    meta = {}
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip().lower()] = value.strip()
    return meta


def parse_rst(text):
    lines = text.splitlines()
    meta = {"title": lines[0].strip()} if lines else {}
    for line in lines[1:]:
        m = re.match(r"^:(\w+):\s*(.*)$", line)
        if m:
            meta[m.group(1).lower()] = m.group(2).strip()
    return meta


def published_posts():
    files = subprocess.run(
        ["git", "ls-files", "content/*.md", "content/*.rst"],
        cwd=BASEDIR, capture_output=True, text=True, check=True,
    ).stdout.split()
    posts = []
    for name in files:
        if "/" in name.removeprefix("content/"):
            continue  # pages/ etc. sind keine Posts
        path = BASEDIR / name
        text = path.read_text(encoding="utf-8")
        meta = parse_md(text) if path.suffix == ".md" else parse_rst(text)
        if meta.get("status", "published") != "published" or "title" not in meta:
            continue
        meta.setdefault("slug", slugify(meta["title"]))
        posts.append(meta)
    return posts


def toot_text(post):
    tags = [re.sub(r"\W", "", t) for t in post.get("tags", "").split(",")]
    hashtags = " ".join("#" + t for t in tags if t)
    text = f"{post['title']}\n\n{SITEURL}/{post['slug']}.html"
    return f"{text}\n\n{hashtags}" if hashtags else text


def send_toot(text, slug):
    instance = os.environ.get("MASTODON_INSTANCE", "https://chaos.social").rstrip("/")
    data = json.dumps({"status": text, "visibility": "public", "language": "de"}).encode()
    req = urllib.request.Request(
        f"{instance}/api/v1/statuses",
        data=data,
        headers={
            "Authorization": f"Bearer {os.environ['MASTODON_TOKEN']}",
            "Content-Type": "application/json",
            "Idempotency-Key": slug,
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)["url"]


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true", help="nur anzeigen, nichts senden")
    parser.add_argument("--seed", action="store_true", help="alle veröffentlichten Posts als getootet markieren")
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
    if len(new) > MAX_TOOTS:
        sys.exit(f"{len(new)} neue Posts (> {MAX_TOOTS}) – mastodon_posted.txt prüfen. Abbruch.")

    if args.dry_run:
        for post in new:
            print(f"--- {post['slug']}\n{toot_text(post)}\n")
        return

    load_env()
    if not os.environ.get("MASTODON_TOKEN"):
        sys.exit("MASTODON_TOKEN fehlt (.env).")

    for post in new:
        url = send_toot(toot_text(post), post["slug"])
        print(f"Getootet: {post['slug']} -> {url}")
        with STATEFILE.open("a") as f:
            f.write(post["slug"] + "\n")

    subprocess.run(["git", "add", STATEFILE.name], cwd=BASEDIR, check=True)
    subprocess.run(
        ["git", "commit", "-m", "chore: mastodon_posted.txt aktualisiert", "--", STATEFILE.name],
        cwd=BASEDIR, check=True,
    )


if __name__ == "__main__":
    main()
