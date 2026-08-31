# 图示模式目录 · Diagram pattern catalogue

Seven shapes for turning an abstract idea or a tangle of steps into one picture a
solo learner can read in a few seconds. Every one is hand-authored inline SVG:
no library, no external file request, no raster, nothing to load.

Companion file: `diagrams.css`. The course marks live beside it — `logo.svg`,
`logo-seal.svg`, `favicon.svg` — and `pattern-community.svg` is the decorative
tile for the letters block; those four paint themselves when used as an `<img>`
or a CSS background, and inherit `currentColor` when pasted inline.

Load the stylesheet after `site.css`:

```html
<link rel="stylesheet" href="../../assets/site.css">
<link rel="stylesheet" href="../../assets/diagrams.css">
```

---

## How every diagram is built

**The shell.** One `<figure class="dl-fig">`, one `<svg>`, one `<figcaption>`.

```html
<figure class="dl-fig">
<svg viewBox="0 0 640 300" role="img" aria-labelledby="fig-NAME-t">
<title id="fig-NAME-t">中文一句话说明。One English sentence saying the same thing.</title>
  …
</svg>
<figcaption><span class="zh">中文图注</span><span class="en">English caption</span></figcaption>
</figure>
```

* `role="img"` and the bilingual `<title>` sit on the `<svg>`, and the title's
  `id` is unique on the page. The older hand-drawn figures in `s1/` instead put
  `role` + `aria-label` on the `<figure>` — either is correct, but never both on
  one figure, or a screen reader announces it twice.
* Every skeleton is **640 user units wide**. Keep that width; vary the height.
  The figure scales to whatever column it sits in.
* `viewBox` and nothing else — no `width`/`height` attributes on the `<svg>`.

**Labels.** Two `<text>` elements, one `.zh` and one `.en`, at the same
coordinates. `site.css` hides one of them, exactly as it does for HTML spans, so
the figure follows the page's language toggle with no extra code.

```html
<g class="dl-t dl-b" text-anchor="middle">
  <text class="zh" x="154" y="70">原句</text>
  <text class="en" x="154" y="70">The original</text>
</g>
```

Size labels with the classes `.dl-t-lg` / `.dl-t` / `.dl-t-sm` / `.dl-t-xs` —
**never with a `font-size` attribute**, because an attribute cannot be grown for
phones. English runs about 1.6× the width of the Chinese it translates; when an
English label will not fit its box, add `dl-long` (`class="en dl-long"`) and it
drops one size step rather than spilling over the edge.

**Colour.** Use the helper classes, never a literal colour. They read the site
palette through the `--dl-*` tokens, so one edit re-skins every figure and a
dark theme, when it arrives, needs no change to any drawing.

| shape classes | text classes | line classes |
|---|---|---|
| `dl-node` · `is-key` `is-ok` `is-warn` `is-bad` `is-draft` `is-quiet` | `dl-t-lg` `dl-t` `dl-t-sm` `dl-t-xs` `dl-b` | `dl-link` · `is-key` `is-soft` |
| `dl-field` (a dashed area) | `dl-ink` `dl-muted` `dl-acc` `dl-good` `dl-caution` `dl-alert` | `dl-rule` `dl-axis` |
| `dl-chip` / `dl-on-chip` (a numbered token) | | `dl-head` (arrowhead fill) |

**Arrows.** Paste this `<defs>` inside any figure that needs one, then put
`marker-end="url(#dlArrow)"` on the path:

```html
<defs><marker id="dlArrow" viewBox="0 0 10 10" refX="8.6" refY="5"
  markerWidth="5" markerHeight="5" orient="auto">
  <path class="dl-head" d="M0 0 L10 5 L0 10 Z"/></marker></defs>
```

Several figures on one page will each carry an identical `#dlArrow`; that is
harmless — the browser resolves to the first, and they are the same marker.

**Phones.** A 640-unit figure lands at about 0.55× on a 390 px screen, so
`diagrams.css` grows the label sizes below 600 px. A dense figure still ends up
tight; wrap those in `<div class="dl-scroll">…</div>` so the drawing keeps a
32 rem minimum and scrolls sideways *inside its own card* instead of shrinking
below legibility. Three of the seven below ship wrapped that way. The page body
must never scroll horizontally.

**Motion.** Nothing moves by default. `class="dl-anim"` on a path traces the
flow; `prefers-reduced-motion: reduce` switches it off, along with everything
else inside `.dl-fig`.

**Checklist before shipping a figure**

- [ ] `viewBox="0 0 640 …"`, no `width`/`height` attributes
- [ ] `role="img"` + a bilingual `<title>` with a page-unique `id`
- [ ] every label present twice, `.zh` and `.en`, at the same coordinates
- [ ] sizes set by class, not by attribute; long English carries `dl-long`
- [ ] no literal colours anywhere — helper classes only
- [ ] read it at 390 px; if labels crowd, wrap in `.dl-scroll`
- [ ] the figure says something the paragraph beside it does not

---
## 1 · 回路 The loop

`viewBox="640 × 300"`

**Reach for it when** A sequence whose last station feeds the first, so it can be run again — back-translation (原句 → 译文 → 回译 → 对照), a draft-and-revise cycle, a check you repeat until it stops finding anything.

**How it is built.** Four boxes at the corners, four arrows going one way round, and the name of the loop in the empty middle. Mark the station the learner starts from — and the one they return to — with `is-key`, so the eye can find the entrance.

**Take care.** Do not use it for a sequence that ends. A loop drawn round a list that only runs once tells the learner to repeat work that does not need repeating.

```html
<figure class="dl-fig">
<svg viewBox="0 0 640 300" role="img" aria-labelledby="fig-loop-t">
<title id="fig-loop-t">回译回路：原句 → 译文 → 回译 → 与原句对照，回到起点。The back-translation loop: the original, the translation, the back-translation, then a comparison that returns you to where you started.</title>
<defs><marker id="dlArrow" viewBox="0 0 10 10" refX="8.6" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="dl-head" d="M0 0 L10 5 L0 10 Z"/></marker></defs>
<rect class="dl-node is-key" x="54" y="36" width="200" height="76" rx="10"/>
<rect class="dl-node" x="386" y="36" width="200" height="76" rx="10"/>
<rect class="dl-node" x="386" y="188" width="200" height="76" rx="10"/>
<rect class="dl-node is-key" x="54" y="188" width="200" height="76" rx="10"/>
<g class="dl-link" marker-end="url(#dlArrow)">
  <path d="M262 74 H372"/><path d="M486 120 V178"/><path d="M378 226 H268"/><path d="M154 180 V122"/>
</g>
<g class="dl-t dl-b" text-anchor="middle">
  <text class="zh" x="154" y="70">① 原句</text><text class="en" x="154" y="70">① The original</text>
  <text class="zh" x="486" y="70">② 译文</text><text class="en" x="486" y="70">② The translation</text>
  <text class="zh" x="486" y="222">③ 回译</text><text class="en" x="486" y="222">③ The back-translation</text>
  <text class="zh" x="154" y="222">④ 对照</text><text class="en" x="154" y="222">④ Set them side by side</text>
</g>
<g class="dl-t-sm dl-muted" text-anchor="middle">
  <text class="zh" x="154" y="94">你要读懂的那一句</text><text class="en dl-long" x="154" y="94">the sentence you need to read</text>
  <text class="zh" x="486" y="94">工具给出的中文</text><text class="en dl-long" x="486" y="94">what the tool hands back</text>
  <text class="zh" x="486" y="246">再译回原来的语言</text><text class="en dl-long" x="486" y="246">run it back into the first language</text>
  <text class="zh" x="154" y="246">对不上的地方要查</text><text class="en dl-long" x="154" y="246">where they disagree, look</text>
</g>
<g class="dl-t-sm dl-acc dl-b" text-anchor="middle">
  <text class="zh" x="320" y="146">一个回路</text><text class="en" x="320" y="146">one loop</text>
  <text class="zh" x="320" y="168">走完再走一遍</text><text class="en" x="320" y="168">run it again</text>
</g>
</svg>
<figcaption><span class="zh">回路图：终点接回起点，所以它可以再走一遍。</span><span class="en">The loop: the last station feeds the first, which is why it can be run again.</span></figcaption>
</figure>
```

---

## 2 · 台阶 The ladder

`viewBox="640 × 350"`

**Reach for it when** A sequence where each step needs the one below it — the six-step learning story, a skill built over a module, any progression where skipping a rung means the next one has nothing to stand on.

**How it is built.** Bars rising left-to-right, each offset by a fixed step, with a stringer line hugging their left edges so the staircase reads as one structure. A numbered chip, a short title and a one-line gloss per bar. Give the top step `is-key`.

**Take care.** Do not use it for steps that are merely ordered. If a learner could do step 4 before step 2 without harm, the ladder over-claims; use the timeline strip or a plain numbered list.

```html
<figure class="dl-fig">
<svg viewBox="0 0 640 350" role="img" aria-labelledby="fig-ladder-t">
<title id="fig-ladder-t">上升的六级台阶：注意、理解、练习、用出来、回看、讲给别人；每一级都站在下一级上。Six rising steps — notice, make sense, practise, use it, look back, explain it — each one standing on the step below.</title>
<path class="dl-link is-soft" d="M20 318 V276 H52 V230 H84 V184 H116 V138 H148 V92 H180 V46"/>
<g>
  <rect class="dl-node" x="20" y="276" width="420" height="42" rx="8"/>
  <rect class="dl-node" x="52" y="230" width="420" height="42" rx="8"/>
  <rect class="dl-node" x="84" y="184" width="420" height="42" rx="8"/>
  <rect class="dl-node" x="116" y="138" width="420" height="42" rx="8"/>
  <rect class="dl-node" x="148" y="92" width="420" height="42" rx="8"/>
  <rect class="dl-node is-key" x="180" y="46" width="420" height="42" rx="8"/>
</g>
<g class="dl-chip">
  <circle cx="46" cy="297" r="13"/><circle cx="78" cy="251" r="13"/><circle cx="110" cy="205" r="13"/>
  <circle cx="142" cy="159" r="13"/><circle cx="174" cy="113" r="13"/><circle cx="206" cy="67" r="13"/>
</g>
<g class="dl-t-sm dl-b dl-on-chip" text-anchor="middle">
  <text x="46" y="302">1</text><text x="78" y="256">2</text><text x="110" y="210">3</text>
  <text x="142" y="164">4</text><text x="174" y="118">5</text><text x="206" y="72">6</text>
</g>
<g class="dl-t dl-b">
  <text class="zh" x="70" y="294">注意到</text><text class="en" x="70" y="294">Notice it</text>
  <text class="zh" x="102" y="248">看懂</text><text class="en" x="102" y="248">Make sense of it</text>
  <text class="zh" x="134" y="202">练一遍</text><text class="en" x="134" y="202">Practise it</text>
  <text class="zh" x="166" y="156">用出来</text><text class="en" x="166" y="156">Use it</text>
  <text class="zh" x="198" y="110">回看</text><text class="en" x="198" y="110">Look back</text>
  <text class="zh" x="230" y="64">讲给别人</text><text class="en" x="230" y="64">Explain it to someone</text>
</g>
<g class="dl-t-sm dl-muted">
  <text class="zh" x="70" y="311">这件事跟我有关</text><text class="en" x="70" y="311">this one has to do with me</text>
  <text class="zh" x="102" y="265">能用自己的话说一句</text><text class="en" x="102" y="265">I can say it in my own words</text>
  <text class="zh" x="134" y="219">照着做一次，不看答案</text><text class="en" x="134" y="219">do it once without the answer</text>
  <text class="zh" x="166" y="173">放进自己真的作业里</text><text class="en" x="166" y="173">put it into real work of my own</text>
  <text class="zh" x="198" y="127">哪一步当时最卡</text><text class="en" x="198" y="127">which step actually stuck</text>
  <text class="zh" x="230" y="81">讲不清的地方就是没学会</text><text class="en" x="230" y="81">what I can't explain, I don't yet know</text>
</g>
</svg>
<figcaption><span class="zh">台阶图：每一级都比前一级要求更多，而且必须踩着前一级。</span><span class="en">The ladder: each step asks more than the one before, and cannot be reached without it.</span></figcaption>
</figure>
```

---

## 3 · 两栏对照 The two-column contrast

`viewBox="640 × 350 · wrapped in `.dl-scroll`"`

**Reach for it when** Two ways of doing the same thing, where one works better — effective versus limited study strategies, a good filename versus a bad one, a safe screenshot versus an unsafe one.

**How it is built.** Two panels of equal width, each with a coloured header band (`is-ok` on the left, `is-warn` on the right), then matched rows: a dot, a short title, and a one-line reason. Same number of rows on both sides, aligned, so the eye compares across. Close each column with one summary line.

**Take care.** Do not let the right column become a column of shame. Say why the weaker option is tempting, and say what it is still good for — the closing line on the right does that job.

```html
<figure class="dl-fig">
<div class="dl-scroll">
<svg viewBox="0 0 640 350" role="img" aria-labelledby="fig-contrast-t">
<title id="fig-contrast-t">两栏对照：左栏是效果好的学习策略（自测回想、分散练习、交错练习、自我解释），右栏是效果有限的（重读、划重点、抄笔记、临时突击）。A two-column contrast: on the left the strategies that work — retrieval practice, spacing, interleaving, self-explanation; on the right the ones that do little — re-reading, highlighting, copying notes, cramming.</title>
<rect class="dl-node" x="20" y="20" width="290" height="310" rx="10"/>
<rect class="dl-node" x="330" y="20" width="290" height="310" rx="10"/>
<path class="dl-node is-ok" d="M20 74 V30 a10 10 0 0 1 10-10 H300 a10 10 0 0 1 10 10 V74 Z"/>
<path class="dl-node is-warn" d="M330 74 V30 a10 10 0 0 1 10-10 H610 a10 10 0 0 1 10 10 V74 Z"/>
<g class="dl-t-lg" text-anchor="middle">
  <text class="zh dl-good" x="165" y="55">费力，但学得住</text><text class="en dl-good" x="165" y="55">Harder, and it holds</text>
  <text class="zh dl-caution" x="475" y="55">轻松，但留不下</text><text class="en dl-caution" x="475" y="55">Easier, and it fades</text>
</g>
<g class="dl-rule"><path d="M20 128 H310"/><path d="M20 182 H310"/><path d="M20 236 H310"/><path d="M330 128 H620"/><path d="M330 182 H620"/><path d="M330 236 H620"/></g>
<g class="dl-good"><circle cx="46" cy="103" r="5"/><circle cx="46" cy="157" r="5"/><circle cx="46" cy="211" r="5"/><circle cx="46" cy="265" r="5"/></g>
<g class="dl-caution"><circle cx="356" cy="103" r="5"/><circle cx="356" cy="157" r="5"/><circle cx="356" cy="211" r="5"/><circle cx="356" cy="265" r="5"/></g>
<g class="dl-t dl-b">
  <text class="zh" x="64" y="102">合上书自测</text><text class="en" x="64" y="102">Close the book, recall</text>
  <text class="zh" x="64" y="156">分几天练</text><text class="en" x="64" y="156">Spread it over days</text>
  <text class="zh" x="64" y="210">几类题混着练</text><text class="en" x="64" y="210">Mix the problem types</text>
  <text class="zh" x="64" y="264">讲清为什么</text><text class="en" x="64" y="264">Say why it works</text>
  <text class="zh" x="374" y="102">再读一遍</text><text class="en" x="374" y="102">Read it again</text>
  <text class="zh" x="374" y="156">划满重点</text><text class="en" x="374" y="156">Highlight everything</text>
  <text class="zh" x="374" y="210">照抄笔记</text><text class="en" x="374" y="210">Copy the notes out</text>
  <text class="zh" x="374" y="264">考前一晚突击</text><text class="en" x="374" y="264">Cram the night before</text>
</g>
<g class="dl-t-sm dl-muted">
  <text class="zh" x="64" y="120">想不起来才是练习</text><text class="en dl-long" x="64" y="120">the struggle is the practice</text>
  <text class="zh" x="64" y="174">忘一点再捡回来</text><text class="en dl-long" x="64" y="174">forget a little, then recover it</text>
  <text class="zh" x="64" y="228">逼自己先判断类型</text><text class="en dl-long" x="64" y="228">you must first pick the type</text>
  <text class="zh" x="64" y="282">说不通就是没懂</text><text class="en dl-long" x="64" y="282">what won't explain isn't known</text>
  <text class="zh" x="374" y="120">眼熟不等于会</text><text class="en dl-long" x="374" y="120">familiar is not the same as known</text>
  <text class="zh" x="374" y="174">全是重点等于没重点</text><text class="en dl-long" x="374" y="174">all-important means nothing is</text>
  <text class="zh" x="374" y="228">手在动，脑子没动</text><text class="en dl-long" x="374" y="228">the hand moves, the mind doesn't</text>
  <text class="zh" x="374" y="282">考完就还回去了</text><text class="en dl-long" x="374" y="282">it is given back after the test</text>
</g>
<g class="dl-t-sm dl-muted" text-anchor="middle">
  <text class="zh" x="165" y="312">选左边，哪怕当时更难受</text><text class="en dl-long" x="165" y="312">choose the left, even when it feels worse</text>
  <text class="zh" x="475" y="312">右边不是不能用，是不能只用</text><text class="en dl-long" x="475" y="312">the right is not banned, only not enough</text>
</g>
</svg>
</div>
<figcaption><span class="zh">对照图：两栏并排，同一件事的两种做法，差别一眼可见。</span><span class="en">The contrast: two columns side by side, one task done two ways, the difference visible at a glance.</span></figcaption>
</figure>
```

---

## 4 · 门 The gate

`viewBox="640 × 300"`

**Reach for it when** Two conditions that must both be met before anything else can start — emotion and motivation before study, or any pair of prerequisites the learner cannot argue past.

**How it is built.** An arch on a ground line with a gatekeeper block either side, a small arrow from each gatekeeper toward the door, and one arrow passing up through the opening. Each gatekeeper carries the question it asks, in quotation marks, in the learner's own voice.

**Take care.** Two gatekeepers, at most three. A gate with five guards is a checklist wearing a costume — draw the checklist instead.

```html
<figure class="dl-fig">
<svg viewBox="0 0 640 300" role="img" aria-labelledby="fig-gate-t">
<title id="fig-gate-t">一扇门，两位守门人：情绪和动机。两个都放行，学习才开始。A door with two gatekeepers — emotion and motivation. Learning starts only after both let you through.</title>
<defs><marker id="dlArrow" viewBox="0 0 10 10" refX="8.6" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="dl-head" d="M0 0 L10 5 L0 10 Z"/></marker></defs>
<path class="dl-node is-key" d="M256 236 V148 A64 64 0 0 1 384 148 V236 Z"/>
<rect class="dl-node is-warn" x="44" y="126" width="180" height="110" rx="10"/>
<rect class="dl-node is-warn" x="416" y="126" width="180" height="110" rx="10"/>
<path class="dl-axis" d="M20 236 H620"/>
<g class="dl-link" marker-end="url(#dlArrow)"><path d="M232 222 H250"/><path d="M408 222 H390"/></g>
<path class="dl-link is-key" marker-end="url(#dlArrow)" d="M320 228 V142"/>
<g class="dl-t-lg dl-acc" text-anchor="middle">
  <text class="zh" x="320" y="70">学习</text><text class="en" x="320" y="70">Learning</text>
</g>
<g class="dl-t dl-b" text-anchor="middle">
  <text class="zh" x="134" y="166">情绪</text><text class="en" x="134" y="166">Emotion</text>
  <text class="zh" x="506" y="166">动机</text><text class="en" x="506" y="166">Motivation</text>
</g>
<g class="dl-t-sm dl-muted" text-anchor="middle">
  <text class="zh" x="134" y="190">「我现在能坐下来吗」</text><text class="en dl-long" x="134" y="190">"can I sit down right now?"</text>
  <text class="zh" x="134" y="210">紧张、烦躁、怕做错</text><text class="en dl-long" x="134" y="210">nerves, irritation, fear of error</text>
  <text class="zh" x="506" y="190">「我为什么要做这个」</text><text class="en dl-long" x="506" y="190">"why am I doing this at all?"</text>
  <text class="zh" x="506" y="210">值不值、有没有用</text><text class="en dl-long" x="506" y="210">worth it, or not worth it</text>
</g>
<g class="dl-t-sm dl-muted" text-anchor="middle">
  <text class="zh" x="320" y="268">学不进去，先看这两位，不要先怪方法。</text><text class="en" x="320" y="268">When learning will not start, check these two before blaming the method.</text>
</g>
</svg>
<figcaption><span class="zh">门图：两位守门人各自放行，通道才打开；方法再好也排在它们后面。</span><span class="en">The gate: the passage opens only when both gatekeepers let you through — however good the method, it queues behind them.</span></figcaption>
</figure>
```

---

## 5 · 四角地图 The map with four corners

`viewBox="640 × 400 · wrapped in `.dl-scroll`"`

**Reach for it when** A small territory with four parts and a person in the middle — the digital workspace (云端 · 日历 · 笔记 · 备份), the four places a file can live, four habits that hold one practice together.

**How it is built.** A dashed field holds four tiles, one per corner, each with a title and one or two short lines. A small compass in the middle carries `我 / me`, with four short ticks reaching toward the corners. The corners are peers: none is numbered, none comes first.

**Take care.** Exactly four. Three corners leave the field lopsided and five stop reading as corners at all; if the content will not sit in four, it is a list, not a map.

```html
<figure class="dl-fig">
<div class="dl-scroll">
<svg viewBox="0 0 640 400" role="img" aria-labelledby="fig-map-t">
<title id="fig-map-t">数字工作台的四个角：云端、日历、笔记、备份，中间是你自己。The four corners of a digital workspace — cloud, calendar, notes, backup — with you at the centre.</title>
<rect class="dl-field" x="20" y="20" width="600" height="360" rx="18"/>
<rect class="dl-node" x="42" y="48" width="230" height="126" rx="10"/>
<rect class="dl-node" x="368" y="48" width="230" height="126" rx="10"/>
<rect class="dl-node" x="42" y="226" width="230" height="126" rx="10"/>
<rect class="dl-node" x="368" y="226" width="230" height="126" rx="10"/>
<g class="dl-link is-soft"><path d="M302 186 L286 174"/><path d="M338 186 L354 174"/><path d="M302 214 L286 226"/><path d="M338 214 L354 226"/></g>
<circle class="dl-node is-key" cx="320" cy="200" r="25"/>
<path class="dl-acc" d="M320 181 L326.5 193.5 L339 200 L326.5 206.5 L320 219 L313.5 206.5 L301 200 L313.5 193.5 Z"/>
<g class="dl-t-lg" text-anchor="start">
  <text class="zh" x="64" y="100">云端</text><text class="en" x="64" y="100">Cloud</text>
  <text class="zh" x="390" y="100">日历</text><text class="en" x="390" y="100">Calendar</text>
  <text class="zh" x="64" y="278">笔记</text><text class="en" x="64" y="278">Notes</text>
  <text class="zh" x="390" y="278">备份</text><text class="en" x="390" y="278">Backup</text>
</g>
<g class="dl-t-sm dl-muted">
  <text class="zh" x="64" y="126">文件在网上有一份</text><text class="en dl-long" x="64" y="126">a copy of the file lives online</text>
  <text class="zh" x="64" y="148">换一台电脑也打得开</text><text class="en dl-long" x="64" y="148">it opens on any other machine</text>
  <text class="zh" x="390" y="126">什么时候做这件事</text><text class="en dl-long" x="390" y="126">when the work actually happens</text>
  <text class="zh" x="390" y="148">提醒替你记住</text><text class="en dl-long" x="390" y="148">the reminder remembers for you</text>
  <text class="zh" x="64" y="304">想法落在一个地方</text><text class="en dl-long" x="64" y="304">thinking lands in one place</text>
  <text class="zh" x="64" y="326">找得回来才算记过</text><text class="en dl-long" x="64" y="326">a note you can find is a note</text>
  <text class="zh" x="390" y="304">丢了还能找回来</text><text class="en dl-long" x="390" y="304">a lost file can still come back</text>
  <text class="zh" x="390" y="326">一份不算备份</text><text class="en dl-long" x="390" y="326">one copy is not a backup</text>
</g>
<g class="dl-t-sm dl-acc dl-b" text-anchor="middle">
  <text class="zh" x="320" y="252">我</text><text class="en" x="320" y="252">me</text>
</g>
</svg>
</div>
<figcaption><span class="zh">四角地图：四个角各管一件事，中间是使用它们的人。</span><span class="en">The four-corner map: each corner holds one job, and the person using them stands in the middle.</span></figcaption>
</figure>
```

---

## 6 · 天平 The balance

`viewBox="640 × 270"`

**Reach for it when** A judgment where both sides carry real weight and one wins this time — quick versus durable, private versus convenient, thorough versus finishable.

**How it is built.** A beam tipping toward the heavier side, a fulcrum on a ground line, a pan hanging from each end with a weight in it, and the question stated across the top. The tilt is the whole argument: draw it clearly, not subtly.

**Take care.** Never draw the losing pan as empty. An empty pan says the other side is worthless, which is almost never what the page means; give it a weight and a label, and let the tilt do the arguing.

```html
<figure class="dl-fig">
<svg viewBox="0 0 640 270" role="img" aria-labelledby="fig-scale-t">
<title id="fig-scale-t">天平：左盘放「快」，右盘放「牢」，秤杆向右倾——这一次，学得牢比学得快重要。A balance: speed in the left pan, durability in the right, the beam tipping right — this time, learning that lasts outweighs learning that is quick.</title>
<g class="dl-t-lg dl-acc" text-anchor="middle">
  <text class="zh" x="320" y="34">这一次，哪一边更重？</text><text class="en" x="320" y="34">Which side weighs more, this time?</text>
</g>
<path class="dl-node is-quiet" d="M320 132 L362 224 H278 Z"/>
<path class="dl-axis" d="M232 224 H408"/>
<path class="dl-link is-key" style="stroke-width:5" d="M100 96 L540 152"/>
<circle class="dl-acc" cx="320" cy="124" r="7"/>
<g class="dl-link"><path d="M100 96 V130"/><path d="M540 152 V186"/></g>
<path class="dl-link" d="M52 130 Q100 168 148 130"/>
<path class="dl-link" d="M492 186 Q540 224 588 186"/>
<rect class="dl-node is-warn" x="76" y="126" width="48" height="20" rx="5"/>
<rect class="dl-node is-ok" x="516" y="182" width="48" height="20" rx="5"/>
<g class="dl-t dl-b" text-anchor="middle">
  <text class="zh dl-caution" x="100" y="176">快</text><text class="en dl-caution" x="100" y="176">Quick</text>
  <text class="zh dl-good" x="540" y="232">牢</text><text class="en dl-good" x="540" y="232">Durable</text>
</g>
<g class="dl-t-sm dl-muted" text-anchor="middle">
  <text class="zh" x="100" y="196">今晚就做完</text><text class="en dl-long" x="100" y="196">finished tonight</text>
  <text class="zh" x="540" y="252">下个月还记得</text><text class="en dl-long" x="540" y="252">still there next month</text>
</g>
</svg>
<figcaption><span class="zh">天平图：两边都有分量，图要说的是这一次哪边更重，而不是哪边没用。</span><span class="en">The balance: both sides carry weight; the figure says which one weighs more this time, not which one is worthless.</span></figcaption>
</figure>
```

---

## 7 · 时间带 The timeline strip

`viewBox="640 × 190 · wrapped in `.dl-scroll`"`

**Reach for it when** How work is spread across a stretch of time — a module's weeks, the shape of a semester, when the three things in a unit fall.

**How it is built.** One axis with an arrowhead, evenly spaced ticks, week labels beneath, and event cards hung above on short stems. Three or four events at most; the empty weeks are part of the message.

**Take care.** **Relative weeks only** — `第 3 周 / Week 3`, never a calendar date. The course runs for anyone, starting whenever they start, so a date on the axis would be wrong for most readers.

```html
<figure class="dl-fig">
<div class="dl-scroll">
<svg viewBox="0 0 640 190" role="img" aria-labelledby="fig-timeline-t">
<title id="fig-timeline-t">一条七周的时间带：第2周交任务，第4周自测，第6周整理作品集。A seven-week strip: a task due in Week 2, a self-check in Week 4, the portfolio pulled together in Week 6.</title>
<defs><marker id="dlArrow" viewBox="0 0 10 10" refX="8.6" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="dl-head" d="M0 0 L10 5 L0 10 Z"/></marker></defs>
<path class="dl-axis" marker-end="url(#dlArrow)" d="M40 118 H600"/>
<g class="dl-rule"><path d="M60 118 V132"/><path d="M140 118 V132"/><path d="M220 118 V132"/><path d="M300 118 V132"/><path d="M380 118 V132"/><path d="M460 118 V132"/><path d="M540 118 V132"/></g>
<g class="dl-link is-soft"><path d="M140 90 V114"/><path d="M300 90 V114"/><path d="M460 90 V114"/></g>
<rect class="dl-node is-key" x="70" y="42" width="140" height="48" rx="8"/>
<rect class="dl-node" x="230" y="42" width="140" height="48" rx="8"/>
<rect class="dl-node is-ok" x="390" y="42" width="140" height="48" rx="8"/>
<g class="dl-t dl-b" text-anchor="middle">
  <text class="zh" x="140" y="64">交一次任务</text><text class="en dl-long" x="140" y="64">One task in</text>
  <text class="zh" x="300" y="64">自测</text><text class="en dl-long" x="300" y="64">Self-check</text>
  <text class="zh" x="460" y="64">整理作品</text><text class="en dl-long" x="460" y="64">Gather the work</text>
</g>
<g class="dl-t-sm dl-muted" text-anchor="middle">
  <text class="zh" x="140" y="82">约 40 分钟</text><text class="en dl-long" x="140" y="82">about 40 minutes</text>
  <text class="zh" x="300" y="82">不计分</text><text class="en dl-long" x="300" y="82">not graded</text>
  <text class="zh" x="460" y="82">放到自己网站</text><text class="en dl-long" x="460" y="82">onto your own site</text>
</g>
<g class="dl-t-sm dl-muted" text-anchor="middle">
  <text class="zh" x="60" y="152">第1周</text><text class="en" x="60" y="152">W1</text>
  <text class="zh" x="140" y="152">第2周</text><text class="en" x="140" y="152">W2</text>
  <text class="zh" x="220" y="152">第3周</text><text class="en" x="220" y="152">W3</text>
  <text class="zh" x="300" y="152">第4周</text><text class="en" x="300" y="152">W4</text>
  <text class="zh" x="380" y="152">第5周</text><text class="en" x="380" y="152">W5</text>
  <text class="zh" x="460" y="152">第6周</text><text class="en" x="460" y="152">W6</text>
  <text class="zh" x="540" y="152">第7周</text><text class="en" x="540" y="152">W7</text>
</g>
<g class="dl-t-sm dl-muted" text-anchor="end">
  <text class="zh" x="600" y="176">相对周次，不写日期</text><text class="en" x="600" y="176">relative weeks, never calendar dates</text>
</g>
</svg>
</div>
<figcaption><span class="zh">时间带：一条轴，等距的周，事件挂在轴上；只写相对周次。</span><span class="en">The timeline strip: one axis, evenly spaced weeks, events hung on the axis — relative weeks only.</span></figcaption>
</figure>
```

---

## 三条底线 · Three standing rules

1. **A figure that repeats the paragraph beside it earns nothing.** If the words
   already say it in the same order, delete the figure or delete the words.
2. **Nothing lives only in colour.** Green and orange carry the contrast, but so
   do the header wording, the position, and the summary line — a reader who
   cannot separate the two hues still gets the point. The forced-colours rules
   in `diagrams.css` keep the shapes when the palette is taken away.
3. **The Chinese comes first and the English is complete.** Both labels sit at
   the same coordinates, so if the English will not fit, the label is too long
   in both languages — shorten the idea, not the translation.
