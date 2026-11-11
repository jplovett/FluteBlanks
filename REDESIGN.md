# Fluteblanks.com redesign (2026)

The original FrontPage site stays on `main`, untouched. Every original page and image lives there, including photos the site no longer shows.

This branch holds the rebuilt, mobile-friendly site:

- `site/` is the deployable static site for Cloudflare Pages. Upload this folder, or a zip of its contents.
- `build.py` regenerates the HTML pages in `site/` (`python3 build.py`). Edit the text and prices there. `site.css`, `fonts/` and `img/` are kept as they are.

Preview: https://fluteblanks-new.pages.dev
