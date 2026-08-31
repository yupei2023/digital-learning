# B4 微课素材与录制脚本 Micro-lesson sources & recording scripts

## 现状 Status（2026-08-30）
四个微课位、跟做页、任务页与单元首页全部配有公开 B 站短视频（密码安全漫画、密码泄露科普、密码管理器思路、数据泄露普法、强密码对照、密码全景科普、文件夹分类命名），另有"想学更多"里的 KeePass 入门 / Bitwarden 速览 / Apple 密码 App / 桌面整理。微课与跟做页的短视频计入相应分钟（r2 起微课 2 的 6:15 只计前 3 分钟，页内写明可停点，其余属选看）；首页密码科普与任务页文件夹视频为选看、不计入。**没有找到平台通用、面向中学生的"两步验证"专讲视频**（检索到的均为游戏外服、苹果账号等单一平台教程，或"如何关闭验证"的反向内容）——两步验证靠微课 3 文字版 + 任务第 4 步的寻找指引讲清；下方脚本保留，供教师日后自录替换。
All lesson slots, the follow-along, the task page and the module home carry public Bilibili clips. Lesson/follow-along clips count inside their minutes; the module-home primer and the task page's folder clip are optional. **No platform-neutral "two-step verification for teenagers" video exists on Bilibili** (candidates were game- or Apple-specific, or taught switching verification OFF) — the second door relies on the micro-lesson 3 text and task step 4's search guidance. Scripts below are kept for future self-recorded replacements.

## 素材来源表 Sources

| 位置 Where | 素材 Item | 来源 / 链接 Source / link | 许可依据 Permission basis | 访问状态 Access |
|---|---|---|---|---|
| lesson-1 · w5 §3（复用同一段） | 漫话安全 密码安全篇（3:05，2022） | B 站 BV1BF411s7GX · UP 主 深圳市网络安全协会 | 官方外链播放器嵌入 + 直达链接 | BV 号经 B 站 view API 核实（2026-08-30，code 0，公开，单 P）；大陆播放**待实测**；无简介，内容**待 ShiFu 抽查** |
| lesson-2 | 【柴知道】你的密码是怎么泄露的？（6:15，2020，15.8 万播放） | B 站 BV1hE411G7BL · UP 主 柴知道 | 同上 | view API 核实（2026-08-30）；**待实测**；科普频道，简介与主题一致（泄露链条）；r2 起页面只计前 3 分钟、其余选看（微课 2 kicker 的时间算术校正） |
| lesson-3 | 真正懂安全的人，根本不背密码（密码管理器）（2:41，2026） | B 站 BV1mNE965E1J · UP 主 申看小霜 | 同上 | view API 核实（2026-08-30）；**待实测**；简介与主题一致（为何用密码管理器） |
| lesson-4 | 漫话安全 数据泄露篇（2:50，2020 国家网络安全宣传周作品） | B 站 BV1tf4y1X7Jo · UP 主 青海普法 | 同上 | view API 核实（2026-08-30）；**待实测**；政务普法账号 |
| activity 第一幕 | 什么样的密码最安全？我们应该如何设置密码？（2:15，2022） | B 站 BV18S4y1Y7BR · UP 主 雷雨室长 | 同上 | view API 核实（2026-08-30）；**待实测**；简介与标题一致 |
| index（选看） | 密码科普视频（5:00，2022） | B 站 BV1mS4y1S7xv · UP 主 网络空间安全宣讲团 | 同上 | view API 核实（2026-08-30）；**待实测**；无简介，内容**待 ShiFu 抽查** |
| task（选看） | 【效率】如何给文件夹分类和命名 告别乱糟糟的电脑（5:21，2021，62 万+播放） | B 站 BV1NX4y1T7dt · UP 主 像素队长 | 同上 | view API 核实（2026-08-30）；**待实测**；无简介，内容**待 ShiFu 抽查** |
| want-more（只链接） | 我是如何管理账号密码的，KeePass 入门教程（21:38，2024，4.4 万播放） | B 站 BV1gFaCe1Eiv · UP 主 杨奇的博客 | 只链接 | view API 核实（2026-08-30）；**待实测**；简介含 keepass.info 与坚果云帮助链接 |
| want-more（只链接） | 密码又长又多？试试 Bitwarden 吧（1:53，2023） | B 站 BV1f14y1m7Uh · UP 主 ES文件浏览器 | 只链接 | view API 核实（2026-08-30）；**待实测**；厂商账号但内容为通识介绍；Bitwarden 官网本身亦待实测 |
| want-more（只链接） | 终于不用记密码了！Apple 自带密码管理器（7:52，2024） | B 站 BV1m6miYuEGq · UP 主 最近使用 | 只链接 | view API 核实（2026-08-30）；**待实测**；仅苹果设备适用，页面已注明 |
| want-more（只链接） | 桌面文件如何管理（3:14，2022） | B 站 BV1KF411F7bz · UP 主 瑾程数码 | 只链接 | view API 核实（2026-08-30）；**待实测** |
| index · 情境引入 | "数码世界是一个陌生国度……钓鱼网站可能只与你的生活隔着一'键'；安全第一" ——教师《数码护照，你值得拥有》一文的转述 | `../家长/210613 数码护照，你值得拥有/数码护照，你值得拥有.docx`（纯文字转述，未提"数码护照"名称与家长视角内容） | 教师自有文字 | 站内 |
| lesson-2 · 讲义 | 永不外传清单（与教纲"学习礼仪"第 3、5 条及隐私四条对齐；"不放他人的个人信息"为礼仪原句） | 教纲 v7 学习礼仪 · 个人网站隐私节 | 课程计划文档 | 站内 |
| lesson-4 | 三问判断（B2 微课 4 / 评估 J2 的"能定位到真实的我吗"扩展为三问） | `course-site/s1/b2-screenshots-recording-website/`（B2 r2） | 本课程自制 | 站内 |
| lesson-4 | "安全截图该遮什么"打码示意图（自绘内联 SVG：虚构的账号安全中心界面，绿框留证据、红块遮隐私；双语标签、无品牌、有替代文字） | 页内代码 | 本课程自制 | 站内 |
| task · 命名规则卡 | "课程-周-内容-化名"规则与扩展模板"用途-时间-内容-谁" | B1 README 决定 5 · B1 微课 2（已在 B1 预告 B4 扩展） | 本课程自制 | 站内 |
| media/handouts | 账号安全卡 | `media/handouts/account-security-card.html`（双语网页，可打印；与 B1–B3 讲义同一做法） | 本课程自制 | 站内 |

嵌入方式：B 站官方外链播放器 `player.bilibili.com/player.html?bvid=…&high_quality=1&danmaku=0&autoplay=0`，关闭弹幕、不自动播放，并附直达链接与时长。所有 BV 号 2026-08-30 经 `api.bilibili.com/x/web-interface/view`（浏览器 UA + Referer）核实存在、公开、单 P。
Embeds use Bilibili's official external player with danmaku off and no autoplay, plus a direct link and duration. Every BV id was checked against the Bilibili view API (browser UA + Referer) on 2026-08-30: exists, public, single part.

## 刻意不用的素材 Deliberately NOT used
- **游戏 / 单一平台的两步验证教程**（BV1ba4y1w7Ua 保姆级双重身份验证——view API 简介显示为游戏外服场景；各种苹果 ID 双重认证教程）——平台过窄，且与课程"不教具体游戏平台"的口径不合。
- **"关闭二次验证 / 解绑手机号"类教程**——教的方向与本单元相反，全部未选。
- **自建密码库（Vaultwarden / Docker 部署）类视频**——需要自有服务器，远超中学生场景；零度解说的 Bitwarden 长评含部署内容与站外下载链接，一并未选。
- **密码破解演示类视频**（"三分钟破解你的 QQ 密码"等）——猎奇向，未选。
- **AI 框架的安全视频**（"AI 帮你管密码"等）——第一学期禁 AI 主题（披露控制），未选。
- 校本教材与家长讲座的旧配图、幻灯片——旧界面、含前机构信息，不复用；本单元的"图"为自绘 SVG。

## 未找到 Not found
- B 站没有平台通用、面向中学生的"两步验证"入门专讲（均绑定单一平台或游戏）；第二道门靠微课 3 文字版 + 任务第 4 步"找开关"指引 + 讲义速查，或按下方脚本自录。
- 没有"中学生隐私设置巡查"通识专讲（检索到的均为单一 App 的设置教程）；三问判断靠微课 4 文字版 + SVG。

## 录制脚本（中文，≤ 5 分钟/段，供日后自录）Recording scripts (for future self-recording)

### 微课 1 · 长度胜过复杂
开场（30 秒）：P@ssw0rd! 看着强，为什么弱——猜密码的是程序不是人。演示（2 分钟）：在线演示字符数与试错次数的关系（自制图表，不用第三方"测强度"网站）；密码短语四步现场造一把（用完即毁）。收尾（1 分钟）：两个老说法澄清（不必定期换、长度胜符号）；示例密码不能真用。

### 微课 2 · 一把钥匙别开所有门
开场（30 秒）：一把钥匙开家门、储物柜、自行车锁的比喻。讲解（2.5 分钟）：网站端泄露 → 撞库链条（图示）；邮箱为什么排第一（总后台）。收尾（1.5 分钟）：泄露消息传来的三步响应；永不外传清单逐条读一遍，验证码一条放慢讲。

### 微课 3 · 密码放哪里，和第二道门
开场（20 秒）：一号一钥的自然后果——记不住怎么办。四种家（2.5 分钟）：脑子、纸本（放家里）、浏览器（前提演示：锁屏）、管理器（KeePassXC 界面一瞥，不展开安装）。第二道门（1.5 分钟）：在一个邮箱的"账号安全"页现场找到两步验证开关并打开（录屏打码后使用）。收尾（20 秒）：找不到开关就如实记录。

### 微课 4 · 发出之前的三个问题
开场（30 秒）：从 B2 的"能定位到真实的我吗"接过来。三问各配一例（2.5 分钟）：选填留空 / 翻译框上传收不回 / 碎片拼图定位。打码示意（1.5 分钟）：对着一张真实（已处理）设置截图演示红遮绿留。收尾（20 秒）：三问不是不发，是把决定权交回判断。
