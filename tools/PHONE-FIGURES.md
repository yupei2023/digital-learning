# 手机上的图与页眉标识 · Phone figures, and the header mark

Written by _xiaobai on 2026-08-31, in the infrastructure pass that followed the
visual upgrade. It is addressed to the two agents revising module content in
parallel (m0–m5 and b1–b6), and it lists **only the things this pass could not
do from `assets/` alone** — everything else is already fixed in
`assets/diagrams.css` and needs no help.

Companion files: `assets/diagrams.css` (the machinery), `assets/DIAGRAM-PATTERNS.md`
(the shapes), `tools/HEADER-LOGO.md` (the mark and the favicon, in full).

---

## 0 · What already changed, so nobody undoes it

`assets/diagrams.css` now does three things it did not do on 2026-08-30.

1. **Every scrolling figure announces itself.** Below 565 px of viewport a
   `.dl-fig` that contains a `.dl-scroll` grows a hint line above the drawing
   (「← 左右滑动查看全图 →」 / "← swipe to see the whole figure →"), a dashed
   cut-rule with a chevron down its right edge, and a visible scrollbar. All
   three disappear on their own the moment the figure fits — 565 px is the exact
   width at which a 32rem drawing stops overflowing the column, not a guess.

2. **Ten figures no longer scroll at all on a phone; they scale to fit.** These
   are the ones whose crop read as a *finished* picture rather than a cut one —
   M4's six-category map showed a tidy 2×2 of four cells under a caption saying
   six. All 17 scrolling figures were rendered in a 390 px iframe and looked at
   one by one; these ten failed the test. The CSS finds them by the
   `aria-labelledby` value already on their `<svg>`:

   | figure | file | id | what the crop hid |
   |---|---|---|---|
   | 六类工具地图 | `s1/m4-digital-learning-technologies/lesson-1-six-categories.html` | `fig-m4six-t` | two of the six categories |
   | 四格判断图 | `s1/m4-digital-learning-technologies/lesson-2-micro-review.html` | `fig-m4keep-t` | the whole "门槛高" column — half the matrix |
   | 四角威胁图 | `s1/b4-accounts-passwords-privacy/index.html` | `fig-b4-threat-t` | two of the four adversaries |
   | 工作台四角图 | `s1/b6-my-digital-workspace/index.html` | `fig-b6-map-t` | two of the four corners |
   | 四角锦囊图 | `s1/m3-meaningful-digital-learning/reading.html` | `fig-m3tips-t` | 锦囊 二 and 四, including one of the two the caption highlights |
   | 内部／外部动机对照 | `s1/m1-what-is-learning/reading.html` | `fig-ch04-motiv-t` | the entire 外部动机 column — the comparison itself |
   | 七扇门 | `s1/m1-what-is-learning/reading.html` | `fig-ch04-doors-t` | two of the seven doors |
   | 导师的下载文件夹 | `s1/b1-email-attachments/lesson-2-attachments-and-filenames.html` | `fig-b1-downloads-t` | the ? / ✓ column — the point of the picture |
   | 五级台阶 | `s1/b2-screenshots-recording-website/lesson-2-five-moves-and-seven-pits.html` | `fig-b2-moves-t` | the ③→② return arrow — the point of the picture |
   | 时间带 | `s1/b6-my-digital-workspace/w7.html` | `fig-b6-time-t` | Weeks 13–16 and the Week-15 marker |

   > **Do not change or remove those ten `aria-labelledby` values, and do not
   > change the `id` on their `<title>`.** The phone fix is keyed to them.
   > If you do need to restructure one of those figures, add
   > `class="dl-fit"` to its `<svg>` **first**, then delete its id from the two
   > `:is(...)` lists in `diagrams.css` §2b/§5. `.dl-fit` is the permanent,
   > markup-side way to say "this figure must never be cropped".

   Fitting a figure does **not** change its internal layout: every coordinate is
   in viewBox units, so a label that sat inside its box still does. Only the
   rendered scale changes, 0.80× → about 0.58×. What *can* change layout is a
   label size, so re-measure after any token edit.

   The twelve figures still scrolling were each looked at and kept deliberately:
   their crop cuts a sentence mid-word or leaves a visible sliver of the next
   column, so it reads as cut, not as finished. `fig-b1-compose-t` (the compose
   window) is the clearest case — every one of its example strings breaks
   mid-word — and it is also the one figure that must not fit: at 0.58× its
   attachment chip would collide with the label beside it.

3. **English labels step down on phones.** English runs about 1.6× the width of
   the Chinese it translates, and the old phone rule grew every label by 29% —
   which is why 15 English labels on 8 pages ran off the 640-unit canvas while
   Chinese was clean everywhere. Scrolled figures now get their own smaller token
   set, plain English labels take `--dl-en-plain`, and `dl-long` takes
   `--dl-en-k`. Thirteen of the fifteen now fit with no markup change. The other
   two are in §2 below.

Verify any figure you touch with
`python3 tools/figure_fit_check.py <page.html>` (project `tools/`, not the
repo's). It renders the page inside a **real 390 px iframe** and reports every
label that falls off the canvas and every figure that still scrolls. Chrome
silently clamps `--window-size=390` to a wider minimum, which is exactly how the
cropping went unnoticed the first time — do not test that way.

---

## 1 · The header mark and the favicon — HISTORICAL, superseded

This section used to carry the full retrofit recipe for putting the mark on 85
module pages, including a copy of the mark's path data. That recipe did its job
and is now dangerous to follow: the mark has since been redesigned, and anyone
pasting the old paths would resurrect the old mark.

**Geometry's single source is the project folder's `tools/gen-mark.py`; the one
way to (re)apply the mark anywhere is `python3 tools/apply-mark.py`.** It writes
the small variant into every page header and `assets/favicon.svg`/`assets/logo.svg`,
and the full variant into the home-page seal and `assets/logo-seal.svg`. Sizing
rules (`header.site .brand`, `.brand-mark{width:1.75em}`) live in `site.css`.
See `tools/HEADER-LOGO.md` for the current mechanism and measured stroke widths.

## 2 · English labels that still need a markup change

Only two are left after the CSS pass. Both are long sentences inside a 640-unit
canvas; no size step saves them at a readable size, so the fix is fewer words
(preferred — it leaves the geometry alone) or a second `<text>` line.

**(a) `s1/m1-what-is-learning/reading.html` · figure `fig-ch02-gate-t`, the
line at `y="300"`.** English measures 728 units and loses about 44 units off
each end. Chinese is fine.

```html
<!-- now -->
<text class="en dl-long" x="320" y="300">Two keys: the “carrot” — in books there are houses of gold; the “stick” — those who cannot learn have no future.</text>
<!-- suggested (77 characters instead of 111 → about 505 units) -->
<text class="en dl-long" x="320" y="300">Two keys: the “carrot” — gold in books; the “stick” — no future without learning.</text>
```

**(b) `s1/m2-what-is-digital-learning/reading.html` · figure `fig-ch07-gate-t`,
the line at `y="310"`.** English measures 695 units, about 28 off each end.

```html
<!-- now -->
<text class="en dl-long" x="320" y="310">These three used to decide who got an education: too far away, working by day, not qualified — turned back.</text>
<!-- suggested (about 525 units) -->
<text class="en dl-long" x="320" y="310">These three decided who got an education: too far, working by day, not qualified.</text>
```

If you would rather keep the wording, split into two `<text>` elements 20 units
apart and move everything below them down by 20, extending the `viewBox` height
to match. Either way, re-measure with `figure_fit_check.py` afterwards.

**Optional, cosmetic.** In `s1/m4-digital-learning-technologies/lesson-1-six-categories.html`
the English `Knowledge representation` (`dl-t-xs`, `x="438"`) now stays on the
canvas but still runs about 24 units past its own cell border. "Knowledge maps"
or adding `dl-long` to that one `<text>` would tidy it. Chinese 知识呈现型 is fine.

---

## 3 · Optional improvement: a stacked phone drawing

Two of the fitting figures pay for showing everything with small type in
English: the seven doors (`fig-ch04-doors-t`) renders its one-word English door
labels at about 8 px, and M4's map renders its smallest line at about 10 px.
Both are correct now — the count the caption claims is the count on screen — but
a purpose-drawn narrow variant would be better than either.

`diagrams.css` has the mechanism ready (§2b (c)). Add a second `<svg>` as a
direct child of the `<figure>`, after `.dl-scroll` and before `<figcaption>`:

```html
<figure class="dl-fig">
  <div class="dl-scroll"><svg viewBox="0 0 640 250" role="img" aria-labelledby="fig-X-t">…</svg></div>
  <svg class="dl-stack" viewBox="0 0 340 430" aria-hidden="true" focusable="false">…</svg>
  <figcaption>…</figcaption>
</figure>
```

Below 565 px the wide one is hidden and the stacked one shown; above it, the
reverse. Put `role="img"` and the `<title>` on the **wide** one only and
`aria-hidden="true"` on the stacked one — `display:none` keeps the hidden one out
of the accessibility tree, so the description is announced once either way.

For the seven doors, the shape that works is **two rows, 4 + 3**: the door pitch
roughly doubles, so the labels can go back to a comfortable size and the two
sentences underneath stop competing with them for the same 640 units. Adding
`class="dl-stack"` means you can then also drop `fig-ch04-doors-t` from the
`:is(...)` lists in `diagrams.css`.

---

## 4 · Things this pass deliberately did not touch

* **`assets/site.css`.** Finding V8 (the module nav wrapping 「自测」 onto two
  lines at 390 px, fixed by `header.site nav a{white-space:nowrap}`) lives there,
  and `site.css` was not in this pass's scope. It belongs to whoever ShiFu gives
  it to.
* **Figure content.** Findings L1–L5, V4–V7 and J1–J9 other than J9's pattern are
  captions, counts, photographs and task wiring — the content agents' work. This
  pass only made sure the phone stops lying about what a figure contains.
* **The three letters in `resources/`.** See the end of §1.
