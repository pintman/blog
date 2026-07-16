# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is Marco Bakera's personal blog (blog.bakera.de), built with [Pelican](https://getpelican.com/) (static site generator). Content is mostly in German. A large share of posts are short film reviews (title, year, star rating, one-line comment, Letterboxd link) plus longer-form technical/teaching posts.

## Architecture

- `content/` — all source posts and pages, in Markdown (`.md`) and reST (`.rst`), flat directory (721+ files, no per-year subfolders). `content/pages/` holds static pages (about, impressum, 404, search, wiki). `content/images/`, `content/media/` hold assets referenced from posts. `content/extra/` holds files mapped to site root via `EXTRA_PATH_METADATA` in `pelicanconf.py` (CNAME, favicon, custom.css).
- `content/_VORLAGE.md` — template for new Markdown posts; copy it for new articles. Frontmatter fields: `title`, `date`, `author`, `tags`, `status`, `slug`.
- `docs/` — **generated output**, committed to the repo and served via GitHub Pages from the `main` branch (not `gh-pages`). Never hand-edit files here; they're overwritten by `make publish`.
- `pelicanconf.py` — base/dev config (relative URLs, no feeds, theme settings).
- `publishconf.py` — production config, imports `pelicanconf.py` and overrides (`SITEURL`, `RELATIVE_URLS = False`, atom feed, `DELETE_OUTPUT_DIRECTORY = True`).
- `publishconf_beaker.py` — alternate publish config for a Hyper/Beaker Browser mirror (imports `publishconf.py`, overrides `SITEURL` to a `hyper://` address). Output goes to `docs_beaker/` (gitignored).
- Theme: `pelican-themes/pelican-bootstrap3` (Bootswatch "cerulean"), plugins `tipue_search`, `sitemap`, `tag_cloud`, `i18n_subsites` — all cloned into `pelican-plugins/` and `pelican-themes/` by `setup.sh` (both gitignored, not vendored in this repo). `theme.local/base.html` is a local override copied on top of the theme's `templates/` by `setup.sh`.

## Setup

```bash
poetry install
./setup.sh          # clones pelican-plugins/ and pelican-themes/ at pinned commits, applies tipue_search hotfix, copies theme.local/base.html over the theme template
```

`setup.sh` pins plugin/theme repo versions via commit hashes at the top of the file — bump these deliberately, not incidentally.

## Common commands

All via `make` (see `Makefile`), or directly with `poetry run`:

```bash
make html            # build with pelicanconf.py -> docs/
make regenerate       # like html, but watches for changes
make devserver [PORT=8000]   # background pelican --autoreload + HTTP server via develop_server.sh
make stopserver       # stop the devserver
make publish          # build with publishconf.py (production settings) -> docs/
make publish_beaker   # build with publishconf_beaker.py -> docs_beaker/
make clean            # remove docs/
```

Prefix with `poetry run` if not inside a poetry shell, e.g. `poetry run make html`.

There is no test suite or linter in this repo.

## Deployment

`.github/workflows/deploy.yml` runs on every push to `main`: installs deps via poetry, runs `setup.sh`, then `make publish`, then commits and pushes the regenerated `docs/` directory back to `main` under the "Github Action" identity. This means **`docs/` will get overwritten and auto-committed shortly after any push** — don't hand-fix generated output there. A `.gitlab-ci.yml` also exists (GitLab Pages target, separate/legacy from the GitHub flow).

## Working with content

- New post: copy `content/_VORLAGE.md`, set `title`, `date`, `tags`, `status: published`, `slug`.
- Film reviews follow a terse convention: star rating line (`⭐ N`), short German comment, `[Auf Letterboxd ansehen](url)` link. Filenames match the film title + year (e.g. `The-Shallows-2016.md`).
- Older posts use reST (`.rst`) with a title + `####` underline and `:field:` metadata; newer posts use Markdown with `---` frontmatter. Match the format of the file you're editing; use Markdown for new posts.
- Helper scripts for images:
  - `addpreviewimage.sh <path>` — creates a shrunk preview copy and prints the reST image snippet with `{filename}` links.
  - `yt_add_video.sh <youtube_id>` — downloads a YouTube thumbnail into `content/images/<year>/<month>/` and prints an embed snippet.
  - `dither.sh <image>` — produces a dithered/resized PNG variant of an image via ImageMagick.
