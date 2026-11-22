"""Entfernt `.sr-only`-Elemente (nur für Screenreader/Suche) aus den Feeds."""
from bs4 import BeautifulSoup

from pelican import signals


def strip_sr_only(html):
    if not html or "sr-only" not in html:
        return html
    soup = BeautifulSoup(html, "html.parser")
    for el in soup.select(".sr-only"):
        el.decompose()
    return str(soup)


def clean_feed(context, feed):
    for item in feed.items:
        for key in ("content", "description"):
            item[key] = strip_sr_only(item.get(key))


def register():
    signals.feed_generated.connect(clean_feed)
