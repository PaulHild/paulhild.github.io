# paulhild.github.io

Personal website of Paul Ergün Hild, served by GitHub Pages at <https://paulhild.github.io>.

It is a plain static site: HTML pages, one stylesheet, and a few lines of JavaScript.
There is no Jekyll build step, so what you see locally is exactly what GitHub Pages serves.

## Preview locally

Double-click **`preview.bat`**, or run:

```
python preview.py
```

This serves the site at <http://localhost:8000> and opens your browser. Edits show up when you reload.
Press Ctrl+C in the window to stop.

## Where things are

| What | File |
|---|---|
| Home page: bio, photo, working papers with abstracts, work in progress | `index.html` |
| Old research URL (redirects to the homepage's research section) | `research/index.html` |
| CV page | `cv/index.html` (embeds `files/Hild_CV.pdf`) |
| Contact page | `contact/index.html` |
| Colors, fonts, spacing | `assets/css/style.css` (the `:root` block at the top) |
| Paper PDFs | `files/papers/` |
| Old project pages (kept at their old URLs) | `projects/…/index.html` |

## Common edits

**Update the CV:** replace `files/Hild_CV.pdf` (keep the file name).

**Update a paper draft:** replace the PDF in `files/papers/` (keep the file name).

**Add a working paper:**
1. Put the PDF in `files/papers/`.
2. In `index.html`, copy one `<li class="paper" …> … </li>` block, paste it where it belongs,
   and change the title, coauthors, PDF link, abstract, and the three ids
   (`id="new-paper"`, `aria-controls="new-paper-abs"`, `id="new-paper-abs"`).

**Move a project from "Work in progress" to "Working papers":** cut its block from one list and paste it
into the other, replacing the status label with a PDF link.

**Change the menu:** the header is repeated at the top of each page (`<nav class="site-nav">`).

## Publishing

Commit your changes and push to the `master` branch. GitHub Pages updates the live site within a
minute or two. The `.nojekyll` file tells GitHub Pages to serve the files as they are.

The previous academicpages/Jekyll version of the site is kept on the `old-site` branch.

## URLs kept from the old site

`/`, `/research/` (redirects to `/#research`, and `/research/#deduct` to `/#deduct`), `/cv/`,
`/contact/`, `/resume` (redirects to `/cv/`), all `/files/…` PDFs,
`/projects/032024Why-dont-you-deduct/`, `/projects/17092024Stereotypes/`, and the Google
verification file.

## Note on fonts

The fonts (Source Serif 4 and Inter) load from Google Fonts. Some German courts have treated loading
Google Fonts from Google's servers as a GDPR issue; if that matters to you, the font files can be
downloaded into `assets/fonts/` and served from the site itself.
