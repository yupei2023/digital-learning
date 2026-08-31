# M1 图片替代文字清单 Alt-text list

页面上线前，每张图片按此表填写 `alt`。三张示意图已用纯 CSS 画在页面里（无图片文件、文字可切换语言，容器带 `aria-label`）；其余为计划中的配图。
Fill each image's `alt` from this list before launch. Three figures are drawn in pure CSS on the pages (no image files; text follows the language switch; containers carry `aria-label`); the rest are planned:

| 位置 Where | 图 Figure | 替代文字 Alt text |
|---|---|---|
| 微课 1 / lesson-1 | 孔庙配享牌位（示意）| 孔庙内供奉孔子弟子牌位的殿堂，牌位数量远少于三千弟子 A hall of tablets honouring Confucius's disciples — far fewer than three thousand |
| 微课 1 / lesson-1 | MIT 校徽 | 麻省理工学院校徽，拉丁文 mens et manus（心智与手）MIT seal with the Latin motto mens et manus (mind and hand) |
| 微课 1 / lesson-1 | 《一百年后的学校》1900 年画作 | 1900 年法国想象画：教师把书本放进机器，知识通过电线直接输入学生头戴的装置 A 1900 French illustration: a teacher feeds books into a machine that wires knowledge into students' headsets |
| 微课 2 / lesson-2 | 策略效果对照表 | 七种学习方法的效果对照：提取、间隔为高；自我解释、交错为中；重读、划线、突击为低 Table rating seven study techniques: retrieval and spacing high; self-explanation and interleaving medium; rereading, highlighting, cramming low |
| w8 §5 / task-1（已做，CSS `ol.flow`）| 六步讲述结构图 | 六个相连的方框：场景→方法→方法→条件→结果与认可→学到的事；第 2–4 步为橙色，标"量规只看这里" Six linked boxes: scene → method → method → conditions → result & recognition → lesson learned; steps 2–4 in orange, "all the rubric looks at" |
| lesson-1（已做，CSS `.loop`）| 知行合一环形图 | 四步环：读听看 → 思考实践 → 存回大脑成为经验 → 遇到新问题再拿出来用 A four-step loop: read/listen/watch → think/practise → store as experience → reuse on a new problem |
| lesson-1（已做，CSS `.gate`）| 两个门卫 | 一扇学习之门，门前两个门卫：情绪、动机 A door to learning with two guards: emotion, motivation |

字幕 Captions：每段视频上传后导出 `.srt`（中、英各一），存入 `captions/`，命名 `lesson-1.zh.srt` / `lesson-1.en.srt`。

## 2026-08-31 · 已上线的配图与图示 Shipped images and figures

三张照片与一幅公有领域画作已放入 `assets/img/`，`alt` 已按下表写进页面；表中"图示"一栏为按
`assets/DIAGRAM-PATTERNS.md` 手绘的内联 SVG——SVG 的 `<title>` 本身就是双语替代文字，随语言开关切换。
Three photographs and one public-domain print now live in `assets/img/` with the alt text below already in
the pages. The "figure" rows are hand-authored inline SVG following `assets/DIAGRAM-PATTERNS.md`; each
SVG's `<title>` is its own bilingual alt text and follows the language toggle.

| 位置 Where | 文件 / 图示 File or figure | 类型 | 来源与许可依据 Source & licence basis |
|---|---|---|---|
| `reading.html` 第 02 章（孔庙一段）| `assets/img/confucius-temple-stelae.jpg` | 照片 | 段玉佩本人拍摄的孔庙先贤牌位，画面无人物、无校徽 Instructor's own photograph; no people, no institutional marks |
| `reading.html` 第 02 章（《一百年后的学校》一段）| `assets/img/villemard-1900-a-lecole.jpg` | 画作 | Villemard，《En l'an 2000 — À l'École》，巴黎 1900 年世博会；1900 年发表、作者 1962 年去世，**公有领域** Published 1900, author died 1962 — public domain worldwide |
| `reading.html` 第 02 章（两个门卫一段）| 图示 · 门 gate | 内联 SVG | 依"情绪 → 动机"关系**重画**（原期刊插图有版权，只用其观点）Redrawn from the emotion→motivation relation; the journal's own drawing is not used |
| `reading.html` 第 03 章（外号"乡巴佬"一段之后）| `assets/img/shifu-at-twelve.jpg` | 照片 | 作者本人的家庭照片，主体即作者 Instructor's own family photograph; he is the subject |
| `reading.html` 第 03 章（长笛一段）| `assets/img/shifu-flute.jpg` | 照片 | 作者本人的演出照片，画面只有他一人、无观众面孔、无校徽 Instructor's own performance photograph; only he is identifiable |
| `reading.html` 第 03 章（良性循环一句）| 图示 · 回路 loop | 内联 SVG | 依本章文字自绘 Drawn from this chapter's own sentence |
| `reading.html` 第 04 章（内部/外部动机一段）| 图示 · 两栏对照 contrast | 内联 SVG | 依本章长笛例子**重画**（原商业机构信息图带水印，不使用）Redrawn from this chapter's flute example; the commercial publisher's watermarked infographic is not used |
| `reading.html` 第 04 章（七种动机因素之后）| 图示 · 七扇门 seven doors | 内联 SVG | 依本章"遍敲世界的门"自绘 Drawn from this chapter's own metaphor |
| `lesson-1-what-is-learning.html` 知行合一 | 图示 · 回路 loop | 内联 SVG | 取代原纯 CSS `.loop`；MIT 校徽本身**不使用**（第三方注册商标），只用校训的意思 Replaces the old CSS `.loop`; the MIT seal itself is **not** reproduced — only the motto's meaning |
| `lesson-3-learning-story.html` 六步 | 图示 · 台阶 ladder | 内联 SVG | 依本页六步自绘，第 2–4 级标为量规唯一评分处 Drawn from this page's six steps; rungs 2–4 marked as the only ones the rubric scores |

`lesson-1` 的纯 CSS `.gate` 图保留不动——读本第 02 章已有完整的 SVG 门图，两页各用一种表述，避免同一幅画出现两次。
The CSS `.gate` on `lesson-1` is left as it is: Reader Ch. 02 now carries the full SVG gate, and one drawing twice in one module would earn nothing.
