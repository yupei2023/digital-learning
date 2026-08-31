# B4 图片替代文字清单 Alt-text list

本单元有四张自绘图：微课 4 的打码示意图（下表第一行），以及新增的三张图示（单元首页"四个对手，四把锁"四角图、微课 1 天平图、微课 4 门图，见"图示系统"一节）。四张都是内联 SVG 线框（无品牌，双语标签随语言开关切换，figure 带 role="img" 与双语替代文字，见下表第一行）。其余"图"都是 HTML 表格（两个说法对照表、四种家对照表、账号安全卡、量规、时间表），语言开关可以切换，屏幕阅读器可以直接读。跟做第二幕的分检卡为 details/summary 折叠块，键盘与读屏器可用。学习者自己的截图在他们自己的设备和网站里，本清单不管——但页面反复要求：截图发布前按微课 4 的图打码，且任何截图不含密码。
Four drawn figures exist in this module: micro-lesson 4's redaction guide (first row below) and three new diagrams (the four-corner threat map on the module home, the balance in micro-lesson 1, the gate in micro-lesson 4 — see "The diagram set" below). All four are unbranded inline SVG wireframes (bilingual labels following the language switch; role="img" with bilingual alt text — first row below). Every other "figure" is an HTML table, so the language switch applies and screen readers read them directly. The rehearsal's sorting cards are details/summary blocks, keyboard- and reader-accessible. Learners' own screenshots live on their own devices and sites, outside this list — with the standing requirement that they are masked per micro-lesson 4's figure before publishing and never contain a password.

若日后录制微课视频并配图，按下表填写 `alt`：
If micro-lesson videos are later recorded with figures, fill `alt` from this table:

| 位置 Where | 图 Figure | 替代文字 Alt text |
|---|---|---|
| 微课 4（已上线 live，r2 改竖排手机版：420 视窗、判定标签独立成行加大字号，锚点 #redaction-figure） | 安全截图打码示意（内联 SVG） | 安全设置截图的打码示意：一页虚拟的"账号安全中心"界面。留下（绿色实线框）："登录密码 · 已于本周更新"和"两步验证 · 已开启"两行状态。遮住（红色色块）：绑定邮箱的完整地址、手机号、恢复二维码。注：绿色是恰恰要露出的证据，红色是发布前必须盖住的隐私；密码本身永远不该出现在任何截图里。A redaction guide for a security-settings screenshot: a mock Account Security page. Keep (green outline): the status rows "Password · updated this week" and "Two-step verification · ON". Hide (red blocks): the full linked email address, the phone number, the recovery QR code. Green marks the evidence to show; red marks what must be covered; the password itself belongs in no screenshot. |
| 微课 1 | 两个说法对照表 | 两行对照表：说法（符号越多越安全 / 必须定期换）对实情（长度重要得多 / 泄露才换）Two claim rows set against the reality: length beats symbols; change on leaks, not on a calendar |
| 微课 3 | 四种"家"对照表 | 四行对照表：脑子 · 纸本 · 浏览器 · 密码管理器，各列好处与代价前提 Four home rows — memory, paper, browser, manager app — each with its good and its price |
| 讲义 | 账号安全卡 | 八栏卡片：密码短语四步 · 一号一钥 · 四种家 · 第二道门 · 三问 · 永不外传清单 · 救援卡 · 文件的名字与家 Eight card rows: the passphrase, one key per door, the four homes, the second door, the three questions, the never-share list, the rescue card, files' names and homes |

字幕 Captions：若日后自录，每段导出 `.srt`（中、英各一），存入 `captions/`，命名 `lesson-N.zh.srt` / `lesson-N.en.srt`（N = 1–4）。
目前嵌入的 B 站视频为公开 UP 主的中文视频，字幕以各视频自带为准（多数无正式字幕）。
The embedded Bilibili clips are public uploaders' Chinese videos; captions are whatever each clip carries (most have none).

## 图示系统 The diagram set（`assets/diagrams.css` · `dl-fig`）

三张按课程图示目录（`assets/DIAGRAM-PATTERNS.md`）绘制的新图。每张的双语说明写在 SVG 的 `<title>` 里，`role="img"` + `aria-labelledby` 指向它；标签成对 `.zh`/`.en`，随语言开关切换；颜色一律用 `--dl-*` 变量，不写死色值。
Three new figures drawn to the course's diagram catalogue. Each carries its bilingual description in the SVG `<title>`, referenced by `role="img"` + `aria-labelledby`; labels are paired `.zh`/`.en` and follow the language switch; colours come from the `--dl-*` tokens only.

| 位置 Where | 图 Figure | 替代文字（写在 SVG `<title>` 里）Alt text (in the SVG `<title>`) |
|---|---|---|
| `index.html`「四个对手，四把锁」 | 四角地图 The four-corner map | 四个对手围着你的两个数字之家：猜密码的程序、被偷了数据的网站、打电话来要验证码的人、拿得到你设备的人。四支箭头从四角指向中央，每个角里都写着挡住它的那把锁。Four adversaries around your two digital homes — guessing programs, breached websites, callers after your verification code, and whoever can reach your device. Four arrows point inward from the corners, and each corner names the lock that stops it. |
| `lesson-1` 「程序面前，哪一边更重？」 | 天平 The balance | 天平：左盘放「复杂」，右盘放「长度」，秤杆向右倾——对猜密码的程序来说，长度比花哨重得多。A balance with complexity in the left pan and length in the right, the beam tipping right: to a guessing program, length outweighs decoration by far. |
| `lesson-4` 三个问题之后 | 门 The gate | 一道门，三位守门人：这一格暴露了什么、谁能看到它、拼起来会不会找到真实的我。三问都放行，信息才出门。A gate with three questions standing guard — what does this reveal, who can see it, and pieced together does it locate the real me. Nothing leaves until all three let it through. |
