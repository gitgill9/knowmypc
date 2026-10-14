# Know My PC website

Static site for Know My PC, served by GitHub Pages. Downloads are attached to this repository's Releases.

- Edit content and settings (support email, site URL, price, links) in `build.py`, styles in `site.css`.
- Fix guides (served at `/fix/<slug>/`) live in `guides.py`. Add a guide to the `GUIDES` list and it appears on `/fix/`, on the home page, in every guide's "More fixes" list and in the sitemap.
- Run `python build.py` to regenerate the HTML, sitemap and robots.txt, then commit.
- New app version: replace `download/KnowMyPC-Setup.exe` with the new installer, add the `latest.json` that BUILD.cmd writes to `download/latest.json` (installed copies read it to find updates), and commit both together. Every Download button points at the installer. Update the "New in version" list (`NEW` in `build.py`) from the app's CHANGELOG.md.
