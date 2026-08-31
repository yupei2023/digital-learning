# B3 微课素材与录制脚本 Micro-lesson sources & recording scripts

## 现状 Status（2026-08-30）
四个微课位、跟做页、任务页与单元首页全部嵌入公开 B 站短视频（微信内置翻译、回译精读法、查英语词典、机器翻译一分钟科普、有道截屏翻译、搞笑误译标志），另有微课 3 的 Edge 朗读补充链接与"想学更多"里的回译进阶 / 人工对比 / 拍照翻译 / DeepL 入门。微课与跟做页的短视频计入相应分钟；首页搞笑标志与全部补充链接为选看、不计入。**没有找到"平台无关的翻译工具入门"或"面向中学生的回译核对"专讲视频**——回译核对靠微课 2 文字版 + 自绘回译环 SVG + 跟做第二幕讲清；下方脚本保留，供教师日后自录替换。
All lesson slots, the follow-along, the task page and the module home carry public Bilibili clips, with an Edge read-aloud extra link and Want-more items. Lesson/follow-along clips count inside their minutes; the module-home clip and all extra links are optional. **No dedicated "translation tools for beginners" or "back-translation checking for teenagers" video exists on Bilibili** — the check relies on the micro-lesson 2 text, the drawn loop SVG and follow-along Act 2. Scripts below are kept for future self-recorded replacements.

## 素材来源表 Sources

| 位置 Where | 素材 Item | 来源 / 链接 Source / link | 许可依据 Permission basis | 访问状态 Access |
|---|---|---|---|---|
| index（选看） | 10 大中文错误翻译成英文的搞笑标志（4:11，2015，14.6 万播放） | B 站 BV1ws41127VF · UP 主 柚子木字幕组 | 官方外链播放器嵌入 + 直达链接 | BV 号经 B 站 view API 核实（2026-08-30，code 0，公开，单 P）；大陆播放**待实测**；简介含字幕组 QQ 群与微博信息，页面未提及 |
| w4 §3 · lesson-1（复用同一段） | 别再只用来聊天，原来微信才是被低估的翻译神器（2:34，2026，2.1 万播放；与 B2 微课 1 同一 UP 主） | B 站 BV1nvXUBMEM6 · UP 主 焱火同学 | 同上 | view API 核实（2026-08-30）；**待实测**；无简介，内容**待 ShiFu 抽查** |
| lesson-2 | 封神英语学习方法！回译精读法！（3:15，2023，3.7 万播放） | B 站 BV1Ba4y1U7dm · UP 主 糯米花花花 | 同上 | view API 核实（2026-08-30）；**待实测**；视频主旨为回译学英语，页面说明文字已如实注明与本课出发点的差异 |
| lesson-3 | 教你学会查英语词典（2:43，2023，4.2 万播放） | B 站 BV1s54y1K7Ze · UP 主 荒荒荒猫灵 | 同上 | view API 核实（2026-08-30）；**待实测** |
| lesson-3（只链接） | 英语文章朗读神器 Microsoft Edge（3:13，2022，4.5 万播放） | B 站 BV1w3411e7n6 · UP 主 香槟集市 | 只链接 | view API 核实（2026-08-30）；**待实测** |
| lesson-4 | 【知智一分钟】一分钟了解机器翻译（1:40，2018，1.5 万播放） | B 站 BV1RW411C7Nv · UP 主 KnowingAI知智 | 官方外链播放器嵌入 + 直达链接 | view API 核实（2026-08-30）；**待实测**；2018 年视频，讲机器翻译发展史（三阶段），不含聊天机器人内容 |
| activity · task（task 选看复用） | 超实用的截屏翻译功能，网易有道词典（2:31，2021，2.6 万播放） | B 站 BV1V64y1D7cg · UP 主 潜心专研的小张同学 | 同上 | view API 核实（2026-08-30）；**待实测**；承接 B2 截图技能 |
| want-more（只链接） | 学英语，必须要做回译！（8:54，2024，13 万播放） | B 站 BV13K421v7Pr · UP 主 Larry想做技术大佬 | 只链接 | view API 核实（2026-08-30）；**待实测**；无简介，内容**待 ShiFu 抽查** |
| want-more（只链接） | 机器翻译的缺点，就是人工翻译的亮点，第四集（0:49，2021） | B 站 BV1PM4y1F7f5 · UP 主 译神来了 | 只链接 | view API 核实（2026-08-30）；**待实测** |
| want-more（只链接） | 怎么用手机拍照翻译？分享两种拍照翻译方法（1:21，2023） | B 站 BV1384y1p7Bj · UP 主 香菜摸鱼日记 | 只链接 | view API 核实（2026-08-30）；**待实测** |
| want-more（只链接） | 如何用 Deepl 进行翻译（1:17，2024） | B 站 BV11S421w7j3 · UP 主 元始天尊的生涯 | 只链接 | view API 核实（2026-08-30）；**待实测**；DeepL 本身亦待实测 |
| lesson-1 情境引入 | "曾经，英文对我只是一门考试的名称，但现在它变成了我获取更广泛知识的工具"——教师校本教材自述章节的转述 | `../校本教材-在线学习/210710 ….docx`（纯文字转述；未使用旧图；原文中 Google/YouTube 等站名未复用） | 教师自有文字 | 站内 |
| lesson-1 · 工具清单 | 翻译工具清单五件（DeepL 待实测、百度、有道、腾讯交互翻译、微信内置；Google 翻译不列）与一条规则原文 | 年计划 v2.1 §3a"翻译工具清单" | 课程计划文档 | 站内 |
| lesson-2 | 回译核对环示意图（自绘内联 SVG：原句 → 译文 → 回译句 → 对照；双语标签、无品牌、有替代文字） | 页内代码 | 本课程自制 | 站内 |
| activity | 练习英文段（含 not rocket science、Barbara Oakley、一个长句三个陷阱） | 本课程自写（data-neutral 英文引文块） | 本课程自制 | 站内 |
| media/handouts | 翻译核对卡 | `media/handouts/translation-check-card.html`（双语网页，可打印；与 B1/B2 讲义同一做法） | 本课程自制 | 站内 |
| task 阅读材料 | 外部课程菜单中语言含英文的九门课的介绍页（均已标"待实测"）；兜底：菜单页自带英文介绍 | `course-site/external-courses.html` | 学习者自行访问外部公开页面 | 外链**待实测**（菜单页已逐条标注） |

嵌入方式：B 站官方外链播放器 `player.bilibili.com/player.html?bvid=…&high_quality=1&danmaku=0&autoplay=0`，关闭弹幕、不自动播放，并附直达链接与时长。所有 BV 号 2026-08-30 经 `api.bilibili.com/x/web-interface/view`（浏览器 UA + Referer）核实存在、公开、单 P。
Embeds use Bilibili's official external player with danmaku off and no autoplay, plus a direct link and duration. Every BV id was checked against the Bilibili view API (browser UA + Referer) on 2026-08-30: exists, public, single part.

## 刻意不用的素材 Deliberately NOT used
- **AI 框架的翻译视频**（"AI 翻译神器""沉浸式翻译 + 大模型"等）——第一学期禁 AI 主题（披露控制），全部未选。
- **腾讯交互翻译演示视频**（BV12v4y1d7q6）——内容合适但 UP 主已注销账号，来源不稳，只在工具表里给官网链接（待实测），不嵌视频。
- **翻译软件横评类视频**（多以谷歌翻译为主角）——Google 翻译不在课程工具清单（大陆打不开），未选。
- 校本教材与读本的旧截图配图——旧界面、出处混杂，不复用；本单元的"图"为自绘 SVG。

## 未找到 Not found
- B 站没有"平台无关的翻译工具入门"专讲（各视频都绑定单一产品）；工具全家福靠 lesson-1 表格讲清。
- 没有面向中学生的"回译核对翻译质量"专讲（检索到的回译视频均为英语学习向）；核对术靠微课 2 文字版 + SVG + 跟做第二幕，或按下方脚本自录。

## 录制脚本（中文，≤ 5 分钟/段，供日后自录）Recording scripts (for future self-recording)

### 微课 1 · 你的翻译工具箱
开场（30 秒）：教师自述——英文从"一门考试的名称"变成获取知识的工具。五件工具过一遍（2.5 分钟）：百度 / 有道网页版（免登录演示）、腾讯交互翻译、微信三个入口（长按 / 扫一扫 / 整页）、DeepL"如果打得开"。收尾（30 秒）：全部不用注册——能不给的信息就不给（B4 伏笔）。

### 微课 2 · 回译核对
开场（30 秒）：看不懂原文，怎么核对译文？悖论与解法。四步演示（2.5 分钟）：挑关键句 → 取译文 → 换工具译回 → 并排找不同（拿真实课程介绍句演示一处走样）。收尾（40 秒）：报警器不是判决书——两点诚实说明。

### 微课 3 · 单词与整段
开场（20 秒）：一件兵器不够用。三种时刻各演示（3 分钟）：单词进词典模式（🔊 发音、词性、例句）、整段粘贴与整页翻译、Edge 大声朗读。收尾（20 秒）：口诀——一个词查词典，一段话用翻译，想听声用朗读。

### 微课 4 · 两个局限与一条规则
开场（20 秒）：知道边界，工具才是你的。局限一演示（1 分钟）：a piece of cake、课程名人名硬译。局限二演示（1 分钟）：长句丢否定，拆短句找回。一条规则逐条讲（1.5 分钟）：帮读不替写 / 关键句回译 / 不粘贴个人信息。收尾（20 秒）：为什么它不算生成式 AI——课程的界定。
