# 自评清单的 id 契约 · The checklist id contract

`assets/checklist.js` · `assets/progress.js` · 发布前检查 `tools/check-release.py`
最后核对 Last verified: 2026-08-31 — 16 页、16 个清单、161 个复选框，**全部有 id**。

---

## 1. 规则 The rule

> **`ul.checklist` 里的每一个 `<input type="checkbox">` 必须有一个稳定的 `id`，
> 每一个 `ul.checklist` 本身也必须有 `id`。**
>
> Every `<input type="checkbox">` inside a `ul.checklist` **must** carry a stable `id`,
> and every `ul.checklist` **must** carry an `id` of its own.

`checklist.js` 用复选框**自己的 id** 作为保存键。缺 id 时它**不保存**，并在控制台
告警——它不会退回到按位置编号。

Why this is a rule and not a preference: the old code fell back to positional keys
(`c0, c1, c2 …`). Insert one item at the top of a list and every saved tick shifts
down by one place. Nothing errors. The learner returns to a self-review that looks
filled in, wrongly. In a course with no teacher standing beside the learner, that
list *is* the feedback, so a silently wrong list is worse than a list that admits it
cannot save.

不保存也不是理想结果——但它**说出来了**，而错位不会。

---

## 2. id 的形状 The required id shape

```
清单 list      <ul class="checklist" id="<页面词干>-selfreview">
条目 checkbox  <input type="checkbox" id="<页面词干>c<序号>">
标签 label     <label for="<同一个 id>">…</label>
```

`<页面词干>` = 页面文件名去掉扩展名（`w8.html` → `w8`）。序号从 1 开始，**按当前
顺序连续编号即可**，但见下面的第 4 节。

现行全站唯一形状：`w#c#`（161/161）。例如 `s1/m1-what-is-learning/w8.html`：

```html
<ul class="checklist" id="w8-selfreview">
<li><input type="checkbox" id="w8c1"><label for="w8c1"><span class="zh">…</span><span class="en">…</span></label></li>
<li><input type="checkbox" id="w8c2"><label for="w8c2">…</label></li>
</ul>
```

保存键的完整形状是 `dl:check:v2:<pathname>#<list-id>`，值是 `{"w8c1":true,…}`。
路径已经在键里，所以 **id 只需在本页内唯一**，跨页可以重名。

---

## 3. 插入、删除、改写条目时怎么做 What to do when a list changes

| 你做的事 | 对已保存状态的影响 | 你要做的 |
|---|---|---|
| 在**末尾**追加一条 | 无 | 用下一个未用过的序号 |
| 在**中间**插入一条 | 无（id 是稳定键，不是位置） | 给新条目一个**未用过**的序号（例如已有 c1–c9，新条目用 c10，即使它排在第 3 位）。**不要重排既有 id** |
| 删除一条 | 该 id 的旧值成为孤儿，被忽略 | 直接删。**不要把它的 id 让给别的条目** |
| **改写某条的意思** | 危险：旧的 ✓ 会恢复到新措辞上 | 见下 |

改写含义时有两条路：

1. 给这一条一个**新 id**（`w8c1` → `w8c10`）。只有这一条的状态作废，其余保留。**推荐**。
2. 若整份清单重写，把 `assets/checklist.js` 与 `assets/progress.js` 里的
   `VERSION` / `PREFIX` 从 `v2` 提到 `v3`。**全站**所有旧勾选一次性作废。

> 一个比喻，附带它的破绽：id 像书页边上贴的便签——你在中间插进一页，贴过的便签
> 还跟着原来那页走。破绽在于，便签认的是纸，而 id 认的只是一个字符串：**把同一个
> id 给了另一段文字，便签就贴到了错的话上**，而浏览器不会察觉。所以第 4 行那句
> "不要把它的 id 让给别的条目"才是真正吃紧的地方。

---

## 4. 同时要更新的地方 What must be updated alongside

模块首页的进度条**声明**分母，不再从 localStorage 推断：

```html
<div data-module-progress data-total="18" data-pages="2"></div>
```

- `data-total` = 本模块**所有**页面上的自评条目总数
- `data-pages` = 本模块中**带清单的页面数**（一页有两个清单也只算一页——`progress.js`
  按路径去重后再报"你已打开 M / N 页"，`check-release.py` 用同一口径核对）

增删条目后必须同步这两个数字，否则 `check-release.py` 的 gate 2 会失败——它把声明值
和实际数出来的复选框数逐模块比对，所以这两个数**不会悄悄漂移**。

---

## 5. 可以直接跑的扫描 The ready-to-run scan

发布前检查已经内建这条门（gate 1 与 gate 2）：

```bash
cd course-site && python3 tools/check-release.py
```

只想单独查 id、并且要一个非零退出码的话：

```bash
cd course-site && python3 - <<'EOF'
import re, glob, sys, os
bad = []
for f in sorted(glob.glob('**/*.html', recursive=True)):
    if f == 'assets/page-template.html': continue
    s = open(f, encoding='utf-8').read()
    for m in re.finditer(r'<ul\b[^>]*class="[^"]*\bchecklist\b[^"]*"[^>]*>(.*?)</ul>', s, re.S):
        tag = m.group(0)[:m.group(0).find('>') + 1]
        if not re.search(r'\bid="', tag):
            bad.append('%s: a <ul class="checklist"> has no id' % f)
        for b in re.findall(r'<input\b[^>]*type=["\']?checkbox["\']?[^>]*>', m.group(1)):
            if not re.search(r'\bid="', b):
                bad.append('%s: a checklist checkbox has no id — its ticks would not be saved' % f)
for x in bad: print(x)
print('checklist id scan: %d problem(s)' % len(bad))
sys.exit(1 if bad else 0)
EOF
```

退出码 0 = 通过。

---

## 6. 当前状态 Current inventory (2026-08-31)

需要修的页面：**0**。全站 16 个清单、161 个复选框，list id 与 checkbox id 齐全，
形状全部为 `w#-selfreview` / `w#c#`；各模块声明的 `data-total` / `data-pages` 与
实际数量逐一相符。

| 模块 Module | 条目 items | 带清单的页 pages |
|---|---|---|
| `s1/m0-orientation` | 9 | 1 |
| `s1/m1-what-is-learning` | 18 | 2 |
| `s1/m2-what-is-digital-learning` | 12 | 1 |
| `s1/m3-meaningful-digital-learning` | 20 | 2 |
| `s1/m4-digital-learning-technologies` | 20 | 2 |
| `s1/m5-semester-portfolio` | 20 | 2 |
| `s1/b1-email-attachments` | 12 | 1 |
| `s1/b2-screenshots-recording-website` | 10 | 1 |
| `s1/b3-translation-reading-tools` | 10 | 1 |
| `s1/b4-accounts-passwords-privacy` | 10 | 1 |
| `s1/b5-search-save-cite` | 10 | 1 |
| `s1/b6-my-digital-workspace` | 10 | 1 |

新建任何带清单的页面时，把它加进对应模块的 `data-total` / `data-pages`，然后跑
第 5 节的扫描。

---

## 7. 真实浏览器里验过的行为 Verified in a real browser (headless Chrome, 2026-08-31)

| 检查 | 结果 |
|---|---|
| 打开 `m1/w8.html`，未勾选 | `已完成 0 / 9` |
| 勾选 `w8c1`、`w8c3`、`w8c5` | `已完成 3 / 9`；写入 `dl:check:v2:…/w8.html#w8-selfreview => {"w8c1":true,"w8c3":true,"w8c5":true}` |
| 带这份状态重新打开 `w8.html` | 3 项恢复，且恢复在**同样的三条**（w8c1, w8c3, w8c5）上 |
| **在清单第 2 位插入一条新条目后重开** | A、C、E 仍然是勾上的三条，新条目未勾——**按下标存储时会错位成 A、B、D** |
| 模块首页（只打开过 2 页中的 1 页） | `本单元共 18 项自评，你已勾选 3 项（17%） · 含清单的页面已打开 1 / 2 页`，进度条宽 17% |
| 同一时刻，旧算法会显示 | **100%**（分母只有已存在的 3 个键） |
| 再打开 `w9.html` 勾 2 条后回到首页 | `你已勾选 5 项（28%） · 含清单的页面已打开 2 / 2 页`，进度条宽 28% |
| 无 id 的复选框 | 状态行写明 `已完成 3 / 3（其中 2 项本次不会被保存）`；控制台两条 `checklist.js:` 告警；localStorage 里只存了有 id 的那一条 `{"p1":true}` |
| 重开该页 | 只有有 id 的那条恢复为勾上，两条无 id 的均为未勾 |
