# M2 图片替代文字清单 Alt-text list

页面上没有位图。三张示意图都用共享样式的纯 CSS 图形（`.flow`）实现，文字本身就是替代文字，随语言开关切换：
No bitmap images. The three figures are CSS figures (`.flow`) whose text is its own alt text and follows the language toggle:

| 位置 Where | 图 Figure | 内容（即替代文字）Content (= alt text) |
|---|---|---|
| 微课 1 / lesson-1 | 名词四格图 Term walk | 远程教育（信函、电视、广播、电话）→ 在线教育（基于互联网）→ E-learning（靠电子设备）→ 数字化学习（手机、平板、AI 工具都算）Distance education → online education → e-learning → digital learning |
| 微课 3 与任务 1 / lesson-3, task-1 | 信的骨架 Letter skeleton | 五个方框：定义 + 两次经历 + 边界 [① 3 分] → 对方最强理由 + 来源 [②] → 我的立场 + 理由 [② 4 分] → 两优势两风险两对策 [③ 3 分] → 一句话立场 + 预想回音 + AI 说明；第 2、3 框标为量规 ② 行 Five boxes; boxes 2–3 marked as rubric row ② |
| 微课 2 / lesson-2 | 风险 / 样子 / 对策示例 | HTML 表格（手机上一行一卡）HTML table (card layout on phones) |

字幕 Captions：见 `captions/README.md`。

## 2026-08-31 · 新增图示 Added figures

| 位置 Where | 图示 Figure | 内容（SVG `<title>` 即替代文字）Content (the SVG `<title>` is the alt text) |
|---|---|---|
| `reading.html` 第 05 章（小白鼠实验之后）| 两栏对照 contrast | 每天重新布置的房间 vs 空空如也的盒子：学得更快 / 更慢、犯错更少 / 更多、突触多出 20–25%；最后一行把两个笼子换成"一个概念看十种讲法"与"课本读一遍"，落到"你这一周更像哪一个笼子" The rearranged room vs the empty box, closing by swapping the two cages for two ways of studying |
| `reading.html` 第 07 章（"障碍只剩一个"之后）| 门 gate | 一扇教育之门：距离、时间、门槛三位门卫已被"三无"撤走（灰色，虚线离场），门前只剩一位——"你愿不愿意学习？" The door of education: distance, the fixed hour and admission have withdrawn; one gatekeeper left, asking whether you are willing |
| `lesson-3-position-piece.html`（"稻草人"一段之后）| 天平 balance | 左盘"对方最强的理由"、右盘"我的理由"，秤杆向右倾；两侧注明：稻草人＝左盘是空的；量规不看倒向哪边，只看两个盘里各放了什么 The other side's strongest reason in one pan, yours in the other — a straw man is an empty pan, and the rubric reads the weights, not the tilt |

三张图都是按 `assets/DIAGRAM-PATTERNS.md` 手绘的内联 SVG：无图片文件、无外部请求，文字随语言开关切换。
All three are hand-authored inline SVG following `assets/DIAGRAM-PATTERNS.md`: no image files, no external requests, labels follow the language toggle.
