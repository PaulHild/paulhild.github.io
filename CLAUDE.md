# Notes for Claude

Personal academic website of Paul Ergün Hild (economist, Humboldt University of Berlin), served by
GitHub Pages at https://paulhild.github.io from the `master` branch of `PaulHild/paulhild.github.io`.
Plain static HTML/CSS/JS: no Jekyll, no build step (`.nojekyll`). See `README.md` for the file layout.

## Rules

- **Pushing to `master` publishes immediately** (live within about a minute). Preview first with
  `python preview.py` (http://localhost:8000) and let Paul check before committing and pushing.
- **Never rename or move anything in `files/`.** The paper PDFs and the CV are linked from outside
  the site ("latest version" links in papers, CVs, applications). To update a paper or the CV,
  overwrite the PDF under the same name.
- **Keep existing URLs working:** `/`, `/cv/`, `/contact/`, `/research/` and `/resume/` (redirect
  pages), `/projects/...`, and `google83c0c7d8fb20694f.html` (Google Search Console verification).
- Don't introduce a framework, build tool or theme without asking.

## Common tasks

- **Papers** are all in `index.html` (sections "Working Papers" and "Selected Work in Progress").
  Copy an existing `<li class="paper">` block and give it unique ids (`id="x"`,
  `aria-controls="x-abs"`, `id="x-abs"`). Don't change existing ids: they are linked as `/#id` and
  via the old `/research/#id`. Use Paul's abstracts verbatim.
- **Header menu and footer** are repeated in every page (`index.html`, `cv/`, `contact/`, `404.html`,
  `projects/*/`); a change there must be made in all of them. The footer year is hard-coded.
- **Styles** live in `assets/css/style.css` (colors and fonts in `:root`, plus a dark-mode block);
  icons in `assets/icons.svg`. Add new pages to `sitemap.xml`.

## Background

- Paul was formerly known as Argun Hild: keep "Formerly Argun Hild" on the homepage and
  `alternateName` in its JSON-LD.
- Links on `argunhild.github.io` (the old GitHub username) return 404. Fixing them would need a new
  `argunhild` GitHub account hosting a redirect site; not set up as of October 2026.
- The previous academicpages/Jekyll version of the site is on the `old-site` branch.
- Fonts come from Google Fonts; self-hosting them is the option if GDPR becomes a concern.
