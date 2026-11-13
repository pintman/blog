## Zweck des Repositorys

Dies ist Marco Bakeras persönlicher Blog (blog.bakera.de), gebaut mit [Pelican](https://getpelican.com/) (Static Site Generator). Inhalte sind überwiegend auf Deutsch.

## Architektur

- `content/` — alle Quell-Posts und -Seiten in Markdown (`.md`) und reST (`.rst`), flaches Verzeichnis (721+ Dateien, keine Unterordner pro Jahr). `content/pages/` enthält statische Seiten (about, impressum, 404, search, wiki). `content/images/`, `content/media/` enthalten Assets, die von Posts referenziert werden. `content/extra/` enthält Dateien, die per `EXTRA_PATH_METADATA` in `pelicanconf.py` ins Site-Root gemappt werden (CNAME, favicon, custom.css).
- `newpost.sh` — legt einen neuen Markdown-Post in `content/` aus einem Titel an (`./newpost.sh [-p] [-n] "Titel" ["tag1, tag2"]`). Frontmatter-Felder: `title`, `date`, `author`, `tags`, `status`, `slug`.
- `docs/` — **generierte Ausgabe**, ins Repo committet und per GitHub Pages vom Branch `main` ausgeliefert (nicht `gh-pages`). Dateien hier nie von Hand bearbeiten; sie werden von `make publish` überschrieben. Bei jedem Push auf `main` führt der GitHub-Workflow `.github/workflows/deploy.yml` `make publish` aus und committet/pusht `docs/` ("Generated new blog release") — daher `docs/` vor dem Push nicht lokal bauen und danach `git pull`.
- `pelicanconf.py` — Basis-/Dev-Konfiguration (relative URLs, keine Feeds, Theme-Einstellungen).
- `publishconf.py` — Produktiv-Konfiguration, importiert `pelicanconf.py` und überschreibt (`SITEURL`, `RELATIVE_URLS = False`, Atom-Feed, `DELETE_OUTPUT_DIRECTORY = True`).
- `publishconf_beaker.py` — alternative Publish-Konfiguration für einen Hyper/Beaker-Browser-Mirror (importiert `publishconf.py`, setzt `SITEURL` auf eine `hyper://`-Adresse). Ausgabe nach `docs_beaker/` (gitignored).
- Theme: `pelican-themes/pelican-bootstrap3` (Bootswatch "cerulean"), Plugins `tipue_search`, `sitemap`, `tag_cloud`, `i18n_subsites` — alle von `setup.sh` nach `pelican-plugins/` und `pelican-themes/` geklont (beide gitignored, nicht im Repo enthalten). `theme.local/base.html` ist ein lokaler Override, den `setup.sh` über das `templates/`-Verzeichnis des Themes kopiert.

## Setup

über `setup.sh`

## Arbeiten mit Inhalten

- Neuer Post: `./newpost.sh "Titel" "tags"` (Standard `status: draft`, `-p` für `published`, `-n` um das Öffnen in VS Code zu überspringen).
- Tag-Übersicht: `./tags.py` listet alle Tags veröffentlichter Posts, `-c` mit Artikelanzahl (nach Häufigkeit sortiert) – nützlich für Tag-Vorschläge.
- Bei Review-Anfragen: auf Verständlichkeit, Tippfehler, Grammatik und Formatierung achten. Fehlen Tags, Vorschläge auf Basis der Tags anderer Posts machen.
- Mastodon: nach dem Committen eines veröffentlichten Posts `./mastodon_post.py` ausführen (`--dry-run` für Vorschau, `--text "…"` ersetzt den Titel im Toot; nur bei genau einem neuen Post). Es tootet Titel + Link + Tags auf chaos.social für jeden veröffentlichten Post, der noch nicht in `mastodon_posted.txt` steht, hängt den Slug an, schreibt die Toot-URL als `mastodon:`-Metadatum (`:mastodon:` in reST) in den Post und committet beides. Danach `git push`, damit der Artikel den Link „auf Mastodon kommentieren" zeigt (`theme.local/includes/comments.html`). Token in `.env` (`MASTODON_TOKEN=…`, gitignored, Scope `write:statuses`). Bricht ab, wenn mehr als 3 Posts neu sind.
  - Beim Tooten eines neuen Posts: Post lesen, kurze deutsche Zusammenfassung als Toot-Text schreiben, genau 3 passende Hashtags wählen (bevorzugt die Tags des Posts; `#blogpost` wird automatisch angehängt), mit `./mastodon_post.py --dry-run --text "…" --tags "a, b, c"` prüfen, dann ohne `--dry-run` ausführen. Max. 500 Zeichen insgesamt inkl. Link (zählt als 23) und Hashtags — Zusammenfassung ggf. kürzen; das Skript bricht bei Überschreitung ab. `--tags` überschreibt die Tags des Posts (nur bei genau einem neuen Post).
- LinkedIn: `./linkedin_post.py` (`--dry-run` für Vorschau) öffnet per `open` einen vorausgefüllten LinkedIn-Teilen-Dialog für jeden veröffentlichten Post, der noch nicht in `linkedin_posted.txt` steht (gleicher Text wie der Toot; `--text`/`--tags` wie bei `mastodon_post.py`, nur bei genau einem neuen Post); keine Bestätigung im Terminal — der Slug gilt als geteilt, sobald der Dialog geöffnet ist („Posten" selbst klicken). Hängt den Slug an und committet die Datei. Keine API/kein Token (offizielle API würde eine LinkedIn-Page erfordern). Nutzt Hilfsfunktionen aus `mastodon_post.py`.
  - Immer exakt dieselben `--text` und `--tags` wie beim Toot übergeben.
- Ältere Posts nutzen reST (`.rst`) mit Titel + `####`-Unterstreichung und `:field:`-Metadaten; neuere Posts nutzen Markdown mit `---`-Frontmatter. Format der bearbeiteten Datei beibehalten; für neue Posts Markdown verwenden.
