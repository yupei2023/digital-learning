# 页眉标识与站点图标 · The header mark and the favicon

`assets/logo.svg` and `assets/favicon.svg` are already wired into the four
top-level pages (`index.html`, `for-mentors.html`, `calendar.html`,
`external-courses.html`). The module pages under `s1/` are **not** done yet:
they are produced by the generators in the project folder's `tools/`
(`build_m*.py`, `build_b*.py`, `revise_m3_r2.py`), so the change belongs in the
generator's page template, not in the built HTML. This note is the exact text
to paste.

Nothing here touches `assets/`. Do not edit the asset files.

---

## Why the mark is pasted inline rather than loaded with `<img>`

`logo.svg` paints itself when it is loaded as an `<img>` or a CSS background,
and it inherits `currentColor` when it is pasted inline. The site ships a single
light palette, but the asset carries its own `prefers-color-scheme: dark` rule —
so a reader whose computer is set to dark mode could be served the pale ink on
the site's light paper and see almost nothing. Pasting the mark inline removes
that risk entirely: inline, `svg:root` never matches, and the mark simply takes
the colour of the text beside it.

The cost is that the inline copies are transcriptions. **If `assets/logo.svg`
ever changes, re-transcribe the paths into this note and re-run the
generators.** The transcription is mechanical: drop the `<title>`, `<desc>` and
`<style>` blocks, hoist the `<g>`'s stroke attributes onto the `<svg>`, keep
every path exactly as it is.

---

## 1 · The favicon

One line in every page's `<head>`. Adjust the depth to match the page:

```html
<!-- top-level page -->
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">

<!-- module page under s1/<module>/ -->
<link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">
```

Put it immediately after the `site.css` link.

## 2 · The style rule

Module pages have no page-scoped `<style>` today, so add this small block to the
`<head>`, after the stylesheet links. (It is deliberately *not* in `site.css`:
`site.css` is a shared asset and needs ShiFu's go-ahead before it is edited. A
later pass can hoist these three lines into `site.css` and delete the block from
every page.)

```html
<style>/* header mark · assets/logo.svg inlined so it inherits currentColor — see tools/HEADER-LOGO.md */
header.site .brand{display:inline-flex;align-items:center;gap:.5rem}
header.site .brand-mark{width:1.75em;height:1.75em;flex:none}</style>
```

`1.75em` on the 17 px bold brand line gives a 30 px box; the drawn mark fills
about 0.61 of that box, so its ink lands at roughly 1.5× the cap height of the
words beside it — present, not shouting.

## 3 · The mark in the header

Replace the brand link. **There is no whitespace between `</svg>` and
`Digital`** — the flex `gap` supplies the space.

Before:

```html
<a class="brand" href="../../index.html">Digital Learning 数字化学习</a>
```

After:

```html
<a class="brand" href="../../index.html"><svg class="brand-mark" viewBox="0 0 64 64" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M5 17 Q18.5 13.5 30.5 19 L30.5 47 Q18.5 52.5 5 45 Z" stroke-width="2.4"/><path d="M59 17 Q45.5 13.5 33.5 19 L33.5 47 Q45.5 52.5 59 45 Z" stroke-width="2.4"/><path d="M5 41.4 Q18.5 48.9 30.5 43.4" stroke-width="1.5"/><path d="M59 41.4 Q45.5 48.9 33.5 43.4" stroke-width="1.5"/><rect x="8.6" y="21.6" width="18.4" height="16" rx="2.2" stroke-width="1.8"/><rect x="37" y="21.6" width="18.4" height="16" rx="2.2" stroke-width="1.8"/><path d="M11.4 27.6 H24.2" stroke-width="1.9"/><path d="M11.4 32.6 H21" stroke-width="1.9"/><path d="M39.8 27.6 H52.6" stroke-width="1.9"/><path d="M39.8 32.6 H49.4" stroke-width="1.9"/><path d="M32 18 V48" stroke-width="2.6"/><path d="M29.6 26 H34.4" stroke-width="1.6"/><path d="M29.6 40 H34.4" stroke-width="1.6"/></svg>Digital Learning 数字化学习</a>
```

`aria-hidden="true"` is deliberate: the words next to the mark already name the
site, and a screen reader that announced both would say it twice.

---

## Things that will bite you

* **The bilingual parity check.** `tools/parity_check.py` flags any bare text
  node of 8+ CJK characters or 8+ English words that is not inside a `.zh`/`.en`
  pair. The asset files' `<desc>` elements are long and bilingual and *would* be
  flagged — that is the other reason the snippet above drops them. Keep them
  dropped. An SVG `<title>` is safe: the checker skips `title`.
* **The footer check.** `tools/site_checks.py` requires the footer's text to
  begin with the contracted wording. Never put an SVG that contains `<text>`
  elements inside `<footer>` before that line — the checker strips tags and the
  seal's ring lettering would land in front of it.
* **`diagrams.css` is not needed** for the mark, the favicon or the seal. Link
  it only on pages that actually carry a `dl-fig` diagram.
* **The pages in `resources/` now carry the mark and the favicon like any other
  page.** They are no longer pandoc output. `tools/build-community-html.py` writes
  them from `assets/page-template.html`'s shell — header mark, favicon, skip link,
  language button, bilingual `<title>` — so a rebuild puts the favicon back rather
  than erasing it. Nothing here needs a hand-added `<link rel="icon">`, and the
  builder fails the build if one of these pages ever loses it.
* **`for-mentors.html` is both a site page and a document source.** It IS the mentor
  handbook online; `tools/build-documents.sh` runs pandoc over it only to make
  `resources/mentor-handbook.{docx,pdf}`. `resources/mentor-handbook.html` used to be
  a second copy of it at a second URL and is gone. `tools/document-print-filter.lua`
  strips the inline `<svg>`, the in-page contents list and the download buttons from
  the paper editions; check after any rebuild that none of them leaked back in.

---

## Where the other three assets went

| asset | where it is used | how |
|---|---|---|
| `logo.svg` | header of every page | inline, `aria-hidden`, 1.75em |
| `favicon.svg` | `<head>` of every page | `<link rel="icon">` |
| `logo-seal.svg` | **course home only**, at the foot of `<main>`, directly above the instructor's name and the year in the footer | inline, `role="img"` + bilingual `<title>`, 96 px (82 px below 600 px), `opacity:.68` |
| `pattern-community.svg` | **course home only**, a 120 px vertical strip to the left of the three letters | inline, `aria-hidden`, hidden below 1000 px |

The seal is deliberately used **once**. It signs the course; a mark that appears
on every page stops being a seal.

### Not done: the seal on the three downloadable letters

Left for ShiFu to decide, with a reason. The three letters are built by
`tools/build-documents.sh` from `tools/documents/*.md` and `for-mentors.html`;
adding a seal means editing `assets/community-doc.css` (a shared asset), editing
the build script, and regenerating three HTML files, four DOCX files and three
PDFs. Two of those are content decisions that are not mine: *where* on a letter
a seal belongs (it belongs at the signature block, and the letters do not have
one yet), and whether a seal on a letter changes how a school reads it. The
mechanical part, when ShiFu says go:

```html
<!-- in the CSS: -->
.doc-seal{display:block;width:88px;height:88px;margin:2.5rem 0 0;opacity:.7}
<!-- in each document's Markdown, at the end, after the closing: -->
<img class="doc-seal" src="../assets/logo-seal.svg"
     alt="Digital Learning 数字化学习 课程印记 · The seal of the course, 2026">
```

Use `<img>` there rather than inline SVG: pandoc's DOCX writer cannot carry
inline SVG, and the printed PDF is always light, so the dark-mode risk described
at the top does not apply to a printed page.
