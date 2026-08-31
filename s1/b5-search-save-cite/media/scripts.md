# B5 微课素材与录制脚本 Micro-lesson sources & recording scripts

## 现状 Status（2026-08-30）
四个微课位、跟做页、任务页与单元首页全部配有公开 B 站短视频（搜索技巧、限定词、收藏夹整理、辨别网络信息、收藏动作、搜索全景、信息真伪），另有"想学更多"里的 site: 进阶 / 青少年网络素养 / 信息真伪案例 / 引用扫盲。微课与跟做页的短视频计入相应分钟（微课 2 的 5:21 只计前 3 分钟，页内写明可停点，其余属选看）；首页搜索全景（11:05）与任务页信息真伪（5:13）为选看、不计入。**没有找到平台通用、面向中学生的"记录来源 / 引用习惯"专讲视频**（检索到的均为大学论文场景：EndNote、Zotero、查重、参考文献格式）——三行来源卡靠微课 3/4 文字版 + 自绘 SVG + 讲义讲清；下方脚本保留，供教师日后自录替换。
All lesson slots, the follow-along, the task page and the module home carry public Bilibili clips. Lesson/follow-along clips count inside their minutes (of micro-lesson 2's 5:21 only the first 3 minutes count; the page states the stop point); the module-home overview and the task-page clip are optional. **No platform-neutral "record your sources" video for secondary students exists on Bilibili** (candidates were all university-thesis scenes: EndNote, Zotero, plagiarism checks, reference formatting) — the three-line card relies on the lesson texts, the drawn SVG and the handout. Scripts below are kept for future self-recorded replacements.

## 素材来源表 Sources

| 位置 Where | 素材 Item | 来源 / 链接 Source / link | 许可依据 Permission basis | 访问状态 Access |
|---|---|---|---|---|
| lesson-1 | 别眨眼，5 个超实用技巧教你调教百度搜索！（2:33，2023） | B 站 BV1Uk4y1e7vA · UP 主 田同学Tino | 官方外链播放器嵌入 + 直达链接 | BV 号经 B 站 view API 核实（2026-08-30，code 0，公开，单 P）；大陆播放**待实测**；简介注明"其他搜索引擎其实也可以用这些技巧" |
| lesson-2 | 或许有你不知道的！搜索引擎&浏览器的高效搜索小技巧（5:21，2023） | B 站 BV1BX4y1Q7su · UP 主 痕继痕迹 | 同上 | view API 核实（2026-08-30）；**待实测**；页面只计前 3 分钟（后半段浏览器细节属选看） |
| lesson-3 | 如何整理 Edge 浏览器的收藏夹？（2:22，2023） | B 站 BV1bM4y1s7qU · UP 主 阳春-烟景 | 同上 | view API 核实（2026-08-30）；**待实测**；无简介，内容**待 ShiFu 抽查** |
| lesson-4 | 【分辨网络信息真假】你被网络"真相"欺骗了吗？（3:40，2020） | B 站 BV1Np4y1v7hq · UP 主 第一师范新航向梦之队 | 同上 | view API 核实（2026-08-30）；**待实测**；简介为空，内容**待 ShiFu 抽查**（标题与选题对口：师范生团队科普片） |
| activity | 浏览器怎么收藏常用网址（1:11，2022） | B 站 BV12G4y1a7pE · UP 主 电脑知识分享 | 同上 | view API 核实（2026-08-30）；**待实测** |
| index（选看） | 你真的会用搜索引擎吗？高效搜索引擎使用技巧（11:05，2020，26.9 万播放） | B 站 BV1w54y1q7uf · UP 主 TecHour官方频道 | 同上 | view API 核实（2026-08-30）；**待实测** |
| task（选看） | 互联网信息纷杂，你能否辨知真假？（5:13，2022） | B 站 BV1J34y147h7 · UP 主 红星视频（红星新闻） | 同上 | view API 核实（2026-08-30）；**待实测**；新闻媒体账号 |
| want-more（只链接） | site 指定网站搜索，同时搜多个网站（4:54，2022） | B 站 BV1Ta411u7yu · UP 主 孔已乙 | 只链接 | view API 核实（2026-08-30）；**待实测**；简介含各引擎语法对照 |
| want-more（只链接） | 《网络谣言与陷阱》青少年网络素养微视频（6:24，2022） | B 站 BV1sa411i7PB · UP 主 今天也下雨8 | 只链接 | view API 核实（2026-08-30）；**待实测**；无简介，内容**待 ShiFu 抽查** |
| want-more（只链接） | 信息爆炸的时代 你相信过谣言吗？（6:43，2024） | B 站 BV1V142127hR · UP 主 堂吉诃德LEON | 只链接 | view API 核实（2026-08-30）；**待实测**；简介列出三个案例，与页面介绍一致 |
| want-more（只链接） | 论文写作小白扫盲系列——什么是引用？如何引用？（8:20，2025） | B 站 BV1rgxyzyE9C · UP 主 网络硕导 | 只链接 | view API 核实（2026-08-30）；**待实测**；无简介，内容**待 ShiFu 抽查**；页面已注明"大学论文向、本课程不要求" |
| lesson-4 · 自测 4/5 题 | 读本第六讲《我们能相信互联网吗？》——线上百科"随时生长，实时更新"、编辑"必须给出权威的引用文献或资料"、"越是被更多人阅读的文章，其精准度也就越高"、科考船命名（Boaty McBoatface"一颗赛艇"）、小马过河 | `tools/reader-240929.txt` 第六讲（教师读本手稿 240929；英文版文件只含 02–04 章，本单元英文段为课程自译） | 教师自有文字 | 站内 |
| lesson-4 | "三行来源卡"示意图（自绘内联 SVG：虚构的疾控睡眠页面示例卡，三行 + 选写一句；双语标签、无品牌、有替代文字，锚点 #source-card-figure） | 页内代码 | 本课程自制 | 站内 |
| 全单元 | 外部课程菜单（十二门；试学任务、两级兜底、"打不开"数据回路沿 B3 口径） | `course-site/external-courses.html` · 外部课程学习线 v2 触点 1 | 课程计划文档 | 站内；外部课程链接均已标"待实测" |
| lesson-1 / 讲义 | "搜索框也是输入框"（B4 三问与"不粘贴个人信息"规则的延伸） | B3 微课 4 · B4 微课 4（课程自有） | 本课程自制 | 站内 |
| lesson-3 | 收藏夹文件夹命名沿"用途-时间-内容"规则；"门厅不是家"口径 | B4 任务页命名规则卡（B1 决定 5 的扩展） | 本课程自制 | 站内 |

嵌入方式：B 站官方外链播放器 `player.bilibili.com/player.html?bvid=…&high_quality=1&danmaku=0&autoplay=0`，关闭弹幕、不自动播放，并附直达链接与时长。所有 BV 号 2026-08-30 经 `api.bilibili.com/x/web-interface/view`（浏览器 UA + Referer）核实存在、公开、单 P。
Embeds use Bilibili's official external player with danmaku off and no autoplay, plus a direct link and duration. Every BV id was checked against the Bilibili view API (browser UA + Referer) on 2026-08-30: exists, public, single part.

## 刻意不用的素材 Deliberately NOT used
- **EndNote / Zotero / 参考文献格式教程**（BV1uJ8fzzE8m、BV1dL4y1u7dz 等）——大学论文工具与查重场景，远超中学生"来源习惯"的定位；三行卡刻意与学术格式脱钩（"习惯不是论文格式"）。
- **武汉大学《信息检索》整门课的搬运合集**（BV11kbbzEEjF，8 小时+，转载账号已注销）——版权与账号状态不明，且体量与本周 120 分钟不成比例；正版课程已在外部课程菜单第 11 行，走课程线更合适。
- **百度高级搜索长教程**（BV17K4y1g7ye，15:29）——内容扎实但为多 P 视频（3 P），与"单 P 可嵌"的既定核验口径不合；未选。
- **需关注公众号领资源的技巧视频**（BV17T411W7s2 等）——视频内引导站外关注与下载，不进课程页面。
- **搜索排名 / SEO / 养号类**（抖音搜索布局、网站收录教程等）——教的方向与本单元相反（怎么被搜到，而非怎么搜），全部未选。
- **Telegram / 资源群搜索教程**——平台可达性与内容合规均不适合中学生页面，未选。
- **AI 搜索工具类视频**（"用 AI 查资料"等）——第一学期禁 AI 主题（披露控制），未选；页面另以规则口径说明"智能摘要不算来源"。
- 校本教材与旧讲座的幻灯片、截图——含前机构信息，不复用；本单元的"图"为自绘 SVG。

## 未找到 Not found
- B 站没有平台通用、面向中学生的"记录来源 / 为什么要留出处"专讲（均为大学论文引用场景）；三行来源卡靠微课 3/4 文字版 + SVG + 讲义，或按下方脚本自录。
- 没有"中学生搜索引擎入门"的成体系短课（找到的多为单点技巧或成人向长课）；本单元以四段文字版为主干、短视频作补充，正好符合"每段 ≤ 5 分钟文字并列"的课程规范。

## 录制脚本（中文，≤ 5 分钟/段，供日后自录）Recording scripts (for future self-recording)

### 微课 1 · 想好词，再搜索
开场（30 秒）：同一个问题两种搜法的结果页对比（整句客套话 vs 三个关键词）。讲解（2.5 分钟）：拆词三步（删口水 → 留具体名词 → 用作者的词）；现场演示从结果标题里"捡行话"再搜第二次。收尾（1 分钟）：换词四招速览；"搜索框也是输入框"的隐私提醒。

### 微课 2 · 收紧渔网
开场（20 秒）：渔网比喻——选词定水域，限定词收网口。演示（3 分钟）：引号（歌词原句）、site:（教育域名）、filetype:pdf（找讲义）、时间筛选，各一个真实例子；每加一根绳子看一眼结果数变化。收尾（1 分钟）："快捷键不是魔法"——演示一个引擎不认 filetype: 时的兜底（把 pdf 当关键词）。

### 微课 3 · 存住它
开场（30 秒）：打开一个真实的乱收藏夹（已打码）。演示（2.5 分钟）：收藏三步——星号 → 建文件夹（按第 5 周规则命名）→ 改标题；再演示"抄一段话立刻补三行来源"。收尾（1 分钟）："收藏夹是门厅"口径；共用电脑不登录同步。

### 微课 4 · 三行来源卡与一眼三看
开场（30 秒）：同一网址三个月前后的页面对比（存档截图，说明网页会变）。讲解（2.5 分钟）：三行卡逐行填一张（对着虚构页面）；一眼三看各配一例。收尾（1.5 分钟）：读本第六讲两个例子口播（线上百科的引用要求；"一颗赛艇"投票）；"先信不等于永远信，第二学期见"。
