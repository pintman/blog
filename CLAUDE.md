## Repository purpose

This is Marco Bakera's personal blog (blog.bakera.de), built with [Pelican](https://getpelican.com/) (static site generator). Content is mostly in German. 

## Architecture

- `content/` — all source posts and pages, in Markdown (`.md`) and reST (`.rst`), flat directory (721+ files, no per-year subfolders). `content/pages/` holds static pages (about, impressum, 404, search, wiki). `content/images/`, `content/media/` hold assets referenced from posts. `content/extra/` holds files mapped to site root via `EXTRA_PATH_METADATA` in `pelicanconf.py` (CNAME, favicon, custom.css).
- `content/_VORLAGE.md` — template for new Markdown posts; copy it for new articles. Frontmatter fields: `title`, `date`, `author`, `tags`, `status`, `slug`.
- `docs/` — **generated output**, committed to the repo and served via GitHub Pages from the `main` branch (not `gh-pages`). Never hand-edit files here; they're overwritten by `make publish`.
- `pelicanconf.py` — base/dev config (relative URLs, no feeds, theme settings).
- `publishconf.py` — production config, imports `pelicanconf.py` and overrides (`SITEURL`, `RELATIVE_URLS = False`, atom feed, `DELETE_OUTPUT_DIRECTORY = True`).
- `publishconf_beaker.py` — alternate publish config for a Hyper/Beaker Browser mirror (imports `publishconf.py`, overrides `SITEURL` to a `hyper://` address). Output goes to `docs_beaker/` (gitignored).
- Theme: `pelican-themes/pelican-bootstrap3` (Bootswatch "cerulean"), plugins `tipue_search`, `sitemap`, `tag_cloud`, `i18n_subsites` — all cloned into `pelican-plugins/` and `pelican-themes/` by `setup.sh` (both gitignored, not vendored in this repo). `theme.local/base.html` is a local override copied on top of the theme's `templates/` by `setup.sh`.

## Setup

via `setup.sh` 

## Working with content

- New post: copy `content/_VORLAGE.md`, set `title`, `date`, `tags`, `status: published`, `slug`.
- Older posts use reST (`.rst`) with a title + `####` underline and `:field:` metadata; newer posts use Markdown with `---` frontmatter. Match the format of the file you're editing; use Markdown for new posts.
