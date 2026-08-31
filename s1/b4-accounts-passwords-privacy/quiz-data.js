/* B4 self-quiz · ungraded · 6 items. Each text is [zh, en]; quiz.js shows the active language. */
window.DL_QUIZ=[
 {
  "q": [
   "四个新密码摆在面前，哪一个最难被猜密码的程序攻破？",
   "Four new passwords on the table — which one gives a password-guessing program the hardest time?"
  ],
  "options": [
   ["P@ssw0rd!（有大写、符号和数字）","P@ssw0rd! (capital, symbol and digit all present)"],
   ["Chen2012!（名字缩写加出生年，好记）","Chen2012! (initials plus birth year, easy to recall)"],
   ["Lvcha7fengzhengTaidengLuotuo（四个不相干的词连成 28 位）","Lvcha7fengzhengTaidengLuotuo (four unrelated words strung to 28 characters)"],
   ["Xk9$（每个字符都很复杂）","Xk9$ (every character maximally complex)"]
  ],
  "a": 2,
  "why": [
   "猜密码的是程序不是人：它一秒试上亿次，还背熟了 a→@、o→0 这类花招和你的生日。真正的墙是长度——每长一位，工作量翻几十倍。四个词的长串好记又难破；短密码再花哨也几分钟出局。（当然，微课 1 的这个示例已经印在公开网页上，不能真用。）",
   "A program does the guessing, not a person: hundreds of millions of tries a second, with a→@ and o→0 memorised along with your birthday. The real wall is length — each added character multiplies the work dozens of times. Four words strung long are memorable and unbreakable; a short fancy password falls in minutes. (And micro-lesson 1's printed example can never be used for real.)"
  ]
 },
 {
  "q": [
   "新闻说某个小论坛的数据被偷了。小航在那里注册过，而且论坛密码和他的邮箱密码是同一个。最该先做什么？",
   "The news reports a small forum's data stolen. Xiao Hang has an account there — and the forum password is the same as his email password. Best first move?"
  ],
  "options": [
   ["先改那个论坛的密码，再把所有共用过这个密码的账号逐个换掉——邮箱最先","Change the forum password first, then every account that shared it — email first of all"],
   ["不用管：他的密码很复杂，程序猜不出来","Do nothing: his password is complex, no program will guess it"],
   ["等论坛发通知再说，也许没偷到他那份","Wait for the forum's notice; maybe his row wasn't taken"],
   ["把论坛账号注销，其他账号就安全了","Close the forum account and the rest are safe"]
  ],
  "a": 0,
  "why": [
   "泄露的数据会被拿去「撞库」：同一对邮箱 + 密码在所有大网站上挨个试。密码强度救不了复用——被偷走的钥匙不需要猜。注销账号也收不回已经泄露的数据。正确顺序：改该账号，再改所有共用过的，邮箱排第一（它能重置其余一切）。",
   "Leaked data feeds credential stuffing: the same email-password pair tried against every major site. Strength cannot rescue reuse — a stolen key needs no guessing. Closing the account cannot recall data already leaked. The right order: change that account, then every account that shared the password, email first (it can reset all the rest)."
  ]
 },
 {
  "q": [
   "电话里的人自称某平台客服，说小雨的账号有风险，需要她读出刚收到的短信验证码来「核实身份」。她该怎么做？",
   "A caller claiming to be a platform's customer service says Xiao Yu's account is at risk and asks her to read out the verification code she just received, \"to confirm her identity\". She should:"
  ],
  "options": [
   ["读给对方——客服是来帮忙的","Read it out — customer service is there to help"],
   ["先要对方的工号，核实了再读","Ask for the agent's staff number first, then read it"],
   ["读一半，留一半，稳妥些","Read half and keep half, to be safe"],
   ["挂断——真客服永远不需要你的验证码","Hang up — genuine customer service never needs your code"]
  ],
  "a": 3,
  "why": [
   "验证码是一把「限时万能钥匙」——正因为对方没有你的密码，才需要骗你亲手把第二道门打开。记死一条：真客服永远不会要验证码；来要的，无论自称是谁、工号多正规，都是骗局。挂断，不解释，然后讲给家里人听。",
   "A verification code is a time-limited master key — it is precisely because the caller lacks your password that they need you to open the second door for them. Memorise it: genuine customer service never asks for a code; whoever asks, however official the staff number sounds, is running a scam. Hang up, explain nothing, then tell your family."
  ]
 },
 {
  "q": [
   "小航要发布安全升级报告了。截图里有「两步验证 已开启」的状态行，也有他的完整邮箱地址。发布前该怎么处理？",
   "Xiao Hang is about to publish his security upgrade report. The screenshot shows the \"two-step verification ON\" status row — and his full email address. Before publishing he should:"
  ],
  "options": [
   ["直接发——邮箱地址不是密码，无所谓","Publish as is — an email address is not a password"],
   ["遮住邮箱地址，留下「已开启」那一行状态","Mask the address, keep the \"ON\" status row"],
   ["把整张图全部打码，包括状态行，最安全","Mask the entire image, status row included — safest"],
   ["不放截图，光写文字就行","Skip the screenshot; words alone will do"]
  ],
  "a": 1,
  "why": [
   "打码就是标注：遮住隐私（邮箱、手机号、二维码、恢复代码），留下证据（「已开启」的状态行）。全遮了证据就没了，不遮又泄露了拼图的一块（三问第 ③ 问：邮箱地址 + 别处的信息 = 撞库的靶子）。红处必遮、绿处恰恰要留——微课 4 那张图就是标尺。",
   "Redaction IS annotation: cover the private (address, number, QR, recovery codes), keep the evidence (the ON status row). Masking everything destroys the evidence; masking nothing hands over a puzzle piece (question ③: an email address plus data from elsewhere = a stuffing target). Red covered, green kept — micro-lesson 4's figure is the yardstick."
  ]
 },
 {
  "q": [
   "注册一个学习网站：邮箱是必填项，真实姓名、学校、生日是选填项。按本周的判断，怎么填？",
   "Signing up for a study site: email is required; real name, school and birthday are optional. By this week's judgment, how to fill it?"
  ],
  "options": [
   ["必填的如实填，选填的默认留空","Fill the required truthfully; leave the optional empty by default"],
   ["全都填上，显得有诚意","Fill everything in, out of good faith"],
   ["姓名填真名，学校和生日不填","Real name in, school and birthday out"],
   ["全部乱填，包括邮箱","Fill everything with nonsense, email included"]
  ],
  "a": 0,
  "why": [
   "三问第 ① 问：这一格暴露了什么？表单要什么不重要，你交出什么才重要——能不给的信息就不给，选填的格子默认留空。真名违反课程的化名原则；而邮箱乱填，验证信就收不到、密码也找不回——必填且有用的信息如实给，仅此而已。",
   "Question ①: what does this field reveal? What the form requests matters less than what you surrender — information you can withhold, withhold, and optional fields stay empty. A real name breaks the course's pseudonym rule; a nonsense email means no verification mail and no password recovery — required, functional information is given truthfully, and nothing more."
  ]
 },
 {
  "q": [
   "四个文件名，三个月后哪一个还能一眼认出「这是什么、何时的、谁的」？",
   "Four filenames — which one will still answer \"what, when, whose\" at a glance three months from now?"
  ],
  "options": [
   ["最终版真的最终版(2).docx","final-version-really-final(2).docx"],
   ["IMG_20260905_133012.png","IMG_20260905_133012.png"],
   ["数字化学习-W5-安全设置截图-晨星.png","DL-W5-security-screenshot-Chenxing.png"],
   ["作业.docx","homework.docx"]
  ],
  "a": 2,
  "why": [
   "「课程-周-内容-化名」答全了三问：这是什么（安全设置截图）、何时的（第 5 周）、谁的（晨星，化名照旧）。相机编号答不了「是什么」，「作业」答不了「哪门什么时候」，「最终版(2)」谁也不信。给文件起名，就是给三个月后的自己留路标。",
   "Course-week-content-pseudonym answers all three: what (a security-settings screenshot), when (Week 5), whose (Chenxing, pseudonym as ever). A camera number can't say what it is, \"homework\" can't say which course or when, and nobody believes \"really-final(2)\". Naming a file is leaving a signpost for the you of three months hence."
  ]
 }
];
