# 课程标识：从模型到页面 · The course mark, from model to page

**几何只有一个来源：项目文件夹的 `tools/gen-mark.py`。** 任何地方都不要手贴、手改
路径数据——包括这份文档。想改标识，改 `gen-mark.py` 的参数；想让改动落到站点上，跑
`tools/apply-mark.py`。这份文档从前贴着"复制即用"的路径范例，谁照着做旧标识就会
回来，所以范例删除了。
**Geometry has exactly one source: `tools/gen-mark.py` in the project folder.** Never
paste or hand-edit path data anywhere — this document included. To change the mark,
change the parameters in `gen-mark.py`; to land the change on the site, run
`tools/apply-mark.py`. This file used to carry copy-paste path data as an example,
which meant anyone following it would resurrect the old mark; the example is gone.

```
python3 tools/apply-mark.py     # run from the project folder
```

## 两个变体，按尺寸分工 · Two variants, matched to size

The mark (variant 4: two laptops facing each other, together an open book) is drawn
by a parametric model. `gen-mark.py` exposes two parameter sets:

| set | strokes | 用在哪 where it lands |
|---|---|---|
| `P` (full) | outline 2.4 · base 2.2 · two screen lines 1.7 · keyboard 1.4 | the 176px seal on the home page, and `assets/logo-seal.svg` |
| `SMALL` | w=1.6 → outline 3.84 · base 3.52 · ONE screen line 3.52 · no keyboard line | the ~30px header of all pages, `assets/logo.svg`, and `assets/favicon.svg` |

Why: at 30px the full mark's screen lines render 0.80px and the keyboard line 0.66px —
sub-pixel, the very defect the old seal was retired for. Measured with the SMALL set:

| stroke | header @30px (viewBox 64) | favicon @16px (viewBox 56) |
|---|---|---|
| screen outline | 1.80px | 1.10px |
| base | 1.65px | 1.01px |
| screen line | 1.65px | 1.01px |

Every stroke stays at or above one device pixel at both sizes. The seal keeps the full
set: at 176px its finest stroke renders ≈2.8px.

`apply-mark.py` writes, in one run:
- the inline `<svg class="brand-mark">` in every page header (SMALL),
- the inline `<svg class="home-brand-mark">` on the course home (SMALL),
- the inline `<svg class="home-seal-mark">` on the course home (full),
- `assets/favicon.svg` (SMALL, fitted square viewBox, dark-scheme hook kept),
- `assets/logo.svg` (SMALL) and `assets/logo-seal.svg` (full), so the standalone
  assets can never drift from the pages.

## 为什么页眉是内联而不是 `<img>` · Why the header mark is inline

`logo.svg` carries its own `prefers-color-scheme` rule for when it is viewed as a
file; loaded via `<img>` that rule could fight the page. Inline, `svg:root` never
matches and the mark simply inherits `currentColor` from the text beside it — which
is also what makes the site's dark mode recolour it for free. `aria-hidden="true"`
is deliberate: the words next to the mark already name the site.

The header sizing rules live in `site.css` (`header.site .brand`,
`header.site .brand-mark{width:1.75em;…}`) — they are shared rules now, not a
page-level `<style>` block. `1.75em` on the 17px brand line gives the 30px box the
SMALL stroke table above is computed against.

## 会咬人的地方 · Things that will bite you

* **The bilingual parity check.** The asset files' `<desc>` elements are long and
  bilingual and would be flagged if pasted into a page — the inline copies carry no
  `<title>`/`<desc>`/`<style>`, and `apply-mark.py` keeps it that way. An SVG
  `<title>` is safe in the standalone assets: the checker skips `title`.
* **The footer check.** `tools/site_checks.py` requires the footer's text to begin
  with the contracted wording. Never put an SVG containing `<text>` inside
  `<footer>` before that line.
* **`diagrams.css` is not needed** for the mark, the favicon or the seal.
* **The pages in `resources/` carry the mark like any other page.** They are built by
  `tools/build-community-html.py`, so a rebuild re-emits the current mark rather than
  erasing it.
* **`for-mentors.html` is both a site page and a document source.** It IS the mentor
  handbook online; `tools/build-documents.sh` runs pandoc over it only to make
  `resources/mentor-handbook.{docx,pdf}` (the old second URL is a redirect page).
  The paper editions are BLOCK format — the whole Chinese document, then the whole
  English one — built by `tools/build-community-print.py`, which also keeps them
  free of the on-screen chrome (mark, contents list, download buttons).

## 印记只用一次 · The seal is used once

| asset | where | how |
|---|---|---|
| `logo.svg` | header of every page | inline via `apply-mark.py`, `aria-hidden`, 1.75em |
| `favicon.svg` | `<head>` of every page | `<link rel="icon">` |
| `logo-seal.svg` | **course home only**, above the instructor's name | inline, `role="img"`, real SVG mask — the knock-out shows the page through, so it adapts to dark mode on its own |
| `pattern-community.svg` | course home only | inline, `aria-hidden`, hidden below 1000px |

The seal signs the course; a mark that appears on every page stops being a seal.

### Not done: the seal on the three downloadable letters

Left for ShiFu to decide. Adding it means a `.doc-seal` rule, an `<img>` at each
letter's signature block (pandoc's DOCX writer cannot carry inline SVG), and a
rebuild of three HTML, four DOCX and three PDF files — but *where* a seal belongs on
a letter, and whether a sealed letter reads differently to a school, are content
decisions that are not this file's to make.
