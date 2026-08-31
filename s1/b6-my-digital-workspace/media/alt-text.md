# B6 替代文字清单 Alt-text inventory

本单元无图片文件；两张图都是内联的自绘 SVG，按课程图示目录（`assets/DIAGRAM-PATTERNS.md`）绘制，样式来自 `assets/diagrams.css`。表格均为语义化 HTML，读屏器可逐格朗读。
No image files in this module; both figures are inline hand-drawn SVG, built to the course diagram catalogue and styled by `assets/diagrams.css`. All tables are semantic HTML, readable cell by cell.

## 工作台四角图 The workspace map（index.html · `#workspace-map-figure`）

- 位置 Where：单元首页"你的工作台长什么样"一节；`figure class="dl-fig"`，`role="img"` + `aria-labelledby` 指向 SVG 内的双语 `<title>`。任务页第 3 步链接到本图锚点。
- 替代文字（中）：数字工作台的四个角：云盘与同步是文件的家（最新版住云端；没有云盘就发给自己的邮箱），日历与提醒是时间的家（每周一个固定时段，提前十分钟响），笔记是想法的家（每个想法有唯一的落点，抄来的话带着三行来源），备份是后悔药（每次发布后再存一份；同步不是备份）；中间是你自己。
- Alt text (en): The four corners of the digital workspace — cloud and sync as the home of files (the newest copy lives there; no drive, email yourself), calendar and reminders as the home of time (one fixed slot each week, the reminder ringing early), notes as the home of ideas (one landing place for each, copied words keeping their source), backup as the cure for regret (one more copy after publish; sync is not backup) — with you at the centre.
- 双语标签成对 `.zh`/`.en`，随语言开关切换；字号由 `dl-t*` 类控制（手机上自动放大）；颜色全部走 `--dl-*` 变量，不写死色值；宽图包在 `.dl-scroll` 里，在自己的卡片内横向滚动，页面本身不横向滚动。

## 时间带 The timeline strip（w7.html · 收官前）

- 位置 Where：第 7 周页面"这张工作台，接下来要撑到哪里"一节。
- 替代文字（中）：从第 7 周到第 16 周的时间带：第 7 周搭好工作台并写下外部课程的选择，第 11 周外部课程正式开始、每周一小时，第 15–16 周整理学期作品集并回看基本功清单。
- Alt text (en): A strip from Week 7 to Week 16: the workspace assembled and the external course chosen in Week 7, the course itself beginning at an hour a week in Week 11, and the semester portfolio with a revisited Basics inventory in Weeks 15–16.
- 只写相对周次，不写日期（图上也印着这一句）。Relative weeks only, never calendar dates — the figure says so itself.

## 表格 Tables

- `w7.html` 时间预算表：四块分钟 + 合计（微课 25 · 跟做 15 · 任务 60 · 反思/日志 20 = 120）。
- `lesson-1` 云盘诚实选项表：路线 · 注册要什么 · 适合谁。
- `lesson-4` 快捷键小集表：按键（Windows / Mac 对照）· 作用 · 什么时候救你。
- `media/handouts/basics-checklist.html` 自查清单表：B1–B6 六行 + 自查问题 + 回去补的页面链接。
