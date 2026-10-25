## Repository purpose

This is Marco Bakera's personal blog (blog.bakera.de), built with [Pelican](https://getpelican.com/) (static site generator). Content is mostly in German. 

## Architecture

- `content/` — all source posts and pages, in Markdown (`.md`) and reST (`.rst`), flat directory (721+ files, no per-year subfolders). `content/pages/` holds static pages (about, impressum, 404, search, wiki). `content/images/`, `content/media/` hold assets referenced from posts. `content/extra/` holds files mapped to site root via `EXTRA_PATH_METADATA` in `pelicanconf.py` (CNAME, favicon, custom.css).
- `newpost.sh` — creates a new Markdown post in `content/` from a title (`./newpost.sh [-p] [-n] "Titel" ["tag1, tag2"]`). Frontmatter fields: `title`, `date`, `author`, `tags`, `status`, `slug`.
- `docs/` — **generated output**, committed to the repo and served via GitHub Pages from the `main` branch (not `gh-pages`). Never hand-edit files here; they're overwritten by `make publish`. On every push to `main`, the GitHub workflow `.github/workflows/deploy.yml` runs `make publish` and commits/pushes `docs/` ("Generated new blog release") — so don't build `docs/` locally before pushing, and `git pull` afterwards.
- `pelicanconf.py` — base/dev config (relative URLs, no feeds, theme settings).
- `publishconf.py` — production config, imports `pelicanconf.py` and overrides (`SITEURL`, `RELATIVE_URLS = False`, atom feed, `DELETE_OUTPUT_DIRECTORY = True`).
- `publishconf_beaker.py` — alternate publish config for a Hyper/Beaker Browser mirror (imports `publishconf.py`, overrides `SITEURL` to a `hyper://` address). Output goes to `docs_beaker/` (gitignored).
- Theme: `pelican-themes/pelican-bootstrap3` (Bootswatch "cerulean"), plugins `tipue_search`, `sitemap`, `tag_cloud`, `i18n_subsites` — all cloned into `pelican-plugins/` and `pelican-themes/` by `setup.sh` (both gitignored, not vendored in this repo). `theme.local/base.html` is a local override copied on top of the theme's `templates/` by `setup.sh`.

## Setup

via `setup.sh` 

## Working with content

- New post: `./newpost.sh "Titel" "tags"` (default `status: draft`, `-p` for `published`, `-n` to skip opening in VS Code).
- Mastodon: after committing a published post, run `./mastodon_post.py` (`--dry-run` to preview). It toots title + link + tags to chaos.social for every published post not yet listed in `mastodon_posted.txt`, appends the slug, and commits that file. Token in `.env` (`MASTODON_TOKEN=…`, gitignored, scope `write:statuses`). Aborts if more than 3 posts are new.
- LinkedIn: `./linkedin_post.py` (`--dry-run` to preview) opens a prefilled LinkedIn share dialog via `open` for every published post not yet listed in `linkedin_posted.txt` (same text as the toot); after clicking "Posten", confirm with `j` in the terminal. Appends the slug and commits that file. No API/token (official API would require a LinkedIn Page). Reuses helpers from `mastodon_post.py`.
- Older posts use reST (`.rst`) with a title + `####` underline and `:field:` metadata; newer posts use Markdown with `---` frontmatter. Match the format of the file you're editing; use Markdown for new posts.
