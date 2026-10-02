# The Key To Insurance website

Static bilingual (EN/ES) site for thekeytoinsurance.com.

- `site/` is the deployable web root (upload its contents to `public_html`).
- `build_site.py` regenerates every page in `site/` (both languages). Run `python3 build_site.py` after editing copy.
- `site/assets/` holds shared CSS/JS. Add the owner photo as `site/assets/agatha-landaetta.jpg`.
- Contact form: set `FORM_ENDPOINT` in `site/assets/script.js` (e.g. a Formspree URL).
