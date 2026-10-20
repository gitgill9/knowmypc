# Know My PC website

Static site for Know My PC, served by GitHub Pages. Downloads are attached to this repository's Releases.

- Edit content and settings (support email, site URL, price, links) in `build.py`, styles in `site.css`.
- Fix guides (served at `/fix/<slug>/`) live in `guides.py`. Add a guide to the `GUIDES` list and it appears on `/fix/`, on the home page, in every guide's "More fixes" list and in the sitemap.
- Run `python build.py` to regenerate the HTML, sitemap and robots.txt, then commit.
- New app version: replace `download/KnowMyPC-Setup.exe` with the new installer and `download/update.json` with the `update.json` that BUILD.cmd writes (installed copies on 0.2.1 and later read it to find updates), and commit both together. `download/latest.json` is only read by 0.2.0 and older, which trust an update key that was lost: keep it as the notice telling them to download the new version by hand, and bump its version to the newest one. Every Download button points at the installer. Update the "New in version" list (`NEW` in `build.py`) from the app's CHANGELOG.md.
