# B5 图片替代文字清单 Alt-text list

本单元有四张自绘图：微课 4 的三行来源卡示例（下表第一行），以及新增的三张图示（单元首页台阶图、微课 1 回路图、微课 4 两栏对照图，见"图示系统"一节）。四张都是内联 SVG 线框（无品牌，双语标签随语言开关切换，figure 带 role="img" 与双语替代文字，锚点 `#source-card-figure`，见下表第一行）。其余"图"都是 HTML 表格（换词四招表、四根绳子表、讲义速查表、量规、时间表），语言开关可以切换，屏幕阅读器可以直接读。任务与跟做以文字证据为主；学习者若在报告里附截图，页面已要求按第 3、5 周的规矩先打码。
Four drawn figures exist in this module: micro-lesson 4's filled source card (first row below) and three new diagrams (the ladder on the module home, the loop in micro-lesson 1, the two-column contrast in micro-lesson 4 — see "The diagram set" below). All four are unbranded inline SVG wireframes (bilingual labels following the language switch; role="img" with bilingual alt text; anchor `#source-card-figure` — first row below). Every other "figure" is an HTML table, so the language switch applies and screen readers read them directly. Evidence this week is textual; any screenshot a learner adds to the report must first be masked by Weeks 3 and 5's rules.

若日后录制微课视频并配图，按下表填写 `alt`：
If micro-lesson videos are later recorded with figures, fill `alt` from this table:

| 位置 Where | 图 Figure | 替代文字 Alt text |
|---|---|---|
| 微课 4（已上线 live · 竖排手机版：420 视窗、行标签独立成行，锚点 #source-card-figure） | 三行来源卡示例（内联 SVG） | 三行来源卡示例：一张卡片，三行正文加一行选写。第 ① 行 标题：青少年睡眠时间建议。第 ② 行 作者或机构：某省疾病预防控制中心（示意，非真实页面）。第 ③ 行 网址 + 访问日期：example.org/sleep-teens · 2026-10-15 访问。底部虚线框为选写句："第一眼可信，因为是疾控机构发布、有日期、页尾给了参考文献。" An example three-line source card: title; author or institution (a mock CDC page); URL + access date; and, in a dashed box, the optional first-glance sentence with its reasons. |
| 微课 1 | 换词四招表 | 四行对照表：同义词替换 · 放大或缩小 · 换角度重新问 · 换一种语言，各配做法 Four move rows — synonyms, zooming, re-asking, switching language — each with its how |
| 微课 2 | 四根绳子表 | 四行对照表：引号 · site: · filetype: · 时间筛选，各列含义与使用时机 Four operator rows — quotes, site:, filetype:, time filter — each with meaning and moment |
| 讲义 | 三行来源卡速查 | 八栏卡片：想词三步 · 四根绳子 · 收藏三步 · 三行来源卡 · 一眼三看 · 摘要不是来源 · 搜索框守则 · 每月自检 Eight card rows: choosing words, the drawstrings, saving, the card, the glances, summary-not-source, search-box rules, the monthly check |

字幕 Captions：若日后自录，每段导出 `.srt`（中、英各一），存入 `captions/`，命名 `lesson-N.zh.srt` / `lesson-N.en.srt`（N = 1–4）。
目前嵌入的 B 站视频为公开 UP 主的中文视频，字幕以各视频自带为准（多数无正式字幕）。
The embedded Bilibili clips are public uploaders' Chinese videos; captions are whatever each clip carries (most have none).

## 图示系统 The diagram set（`assets/diagrams.css` · `dl-fig`）

| 位置 Where | 图 Figure | 替代文字（写在 SVG `<title>` 里）Alt text (in the SVG `<title>`) |
|---|---|---|
| `index.html`「本周的三级台阶」 | 台阶 The ladder | 三级上升的台阶：找得到、存得住、追得回；每一级都站在下一级上。Three rising steps — find it, keep it, trace it — each standing on the step below. |
| `lesson-1`「一次搜索，不是搜一次」 | 回路 The loop | 搜索回路：想好词 → 搜一次 → 读结果标题、捡回行话 → 换词收紧 → 回到起点再搜一次。The search loop — choose the words, run one search, read the result titles and harvest the trade words, swap and tighten, then return to the start and search again. |
| `lesson-4` 一眼三看之后 | 两栏对照 The contrast | 两栏对照：左栏是第一眼可以信的迹象——有署名的机构或个人、页面写着日期、页尾一排参考文献；右栏是第一眼要打问号的迹象——查不到署名、"最新研究"却没有日期、除了"专家表示"什么都不引。A two-column contrast: on the left the signs that earn first-glance trust — a named institution or person, a date on the page, references at the foot; on the right the signs that earn a question mark — no traceable byline, a "latest study" with no date, nothing cited but "experts say". |

三张图的双语说明写在 SVG 的 `<title>` 里，`role="img"` + `aria-labelledby` 指向它；标签成对 `.zh`/`.en`，随语言开关切换；颜色一律用 `--dl-*` 变量。
Each carries its bilingual description in the SVG `<title>`, referenced by `role="img"` + `aria-labelledby`; labels are paired `.zh`/`.en`; colours come from the `--dl-*` tokens only.
