"""Backlinks: ergänzt jeden Artikel um `backlinks` – Artikel, die per {filename} auf ihn verlinken."""
import os
import re

from pelican import signals

LINK_RE = re.compile(r"""\{filename\}(/?)([^"'#?\s<>]+)""")


def add_backlinks(generator):
    by_path = {a.relative_source_path: a for a in generator.articles}
    for article in generator.articles:
        article.backlinks = []
    for source in generator.articles:
        base = os.path.dirname(source.relative_source_path)
        for absolute, target_path in LINK_RE.findall(source._content or ""):
            path = target_path if absolute else os.path.join(base, target_path)
            target = by_path.get(os.path.normpath(path))
            if target and target is not source and source not in target.backlinks:
                target.backlinks.append(source)
    for article in generator.articles:
        article.backlinks.sort(key=lambda a: a.date, reverse=True)


def register():
    signals.article_generator_finalized.connect(add_backlinks)
