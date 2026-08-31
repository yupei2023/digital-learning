#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the three community documents as pages of THIS site, not as pandoc output.

Why this exists
---------------
resources/*.html used to be raw `pandoc -s` output: no site.css, no lang.js, no
language button, and — worst — no <span class="zh">/<span class="en"> pairs. The whole
site shows one language at a time by hiding the other span. With no spans, a parent
opening the letter to parents read every paragraph twice, Chinese then English. The
letter's persuasive force rests on being easy to read, and it was the hardest-reading
page on the site.

Pandoc cannot emit that structure, so this script does. It reads pandoc's JSON AST
(so it never parses Markdown or HTML by hand) and pairs the two languages:

  * two consecutive headings of the same level, Chinese then English  -> one bilingual heading
  * two consecutive paragraphs, Chinese then English                  -> one bilingual paragraph
  * a run of inlines that is Chinese-then-English inside one table cell
    or list item                                                      -> one bilingual cell / item

Anything it cannot split with certainty (a genuinely interleaved label such as
"日期 Date：【…】") is emitted ONCE, visible in both languages, and reported at the end
of the run. Guessing a split point would silently cut a sentence in half, which is
worse than showing a short bilingual label twice.

  Sources of truth
    tools/documents/letter-to-parents.md               -> resources/letter-to-parents.html
    tools/documents/letter-to-school-administrators.md -> resources/letter-to-school-administrators.html
    for-mentors.html (already a site page)             -> resources/mentor-handbook.html

  Not touched here: the .docx and .pdf downloads. Those stay pandoc/Chrome products
  and keep using assets/community-doc.css; tools/build-documents.sh builds them from
  a throwaway print copy. Run this from the course-site directory, or via that script.

  Requires: pandoc.
"""
import json, subprocess, sys, os, re, html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# ---------------------------------------------------------------- language tests
IDEO = '㐀-鿿豈-﫿々〆'
CJK_PUNCT = '。，、；：？！（）〔〕《》「」『』【】〈〉〜～﹁﹂％＃＠'
CJKCH = re.compile('[' + IDEO + re.escape(CJK_PUNCT) + ']')
IDEOCH = re.compile('[' + IDEO + ']')

def cjkish(ch):  return bool(CJKCH.match(ch))

def node_text(n):
    """plain text of an inline node, for language tests only"""
    if isinstance(n, list): return ''.join(node_text(x) for x in n)
    if not isinstance(n, dict): return ''
    t = n.get('t'); c = n.get('c')
    if t == 'Str': return c
    if t in ('Space', 'SoftBreak', 'LineBreak'): return ' '
    if t in ('Emph', 'Strong', 'Strikeout', 'Superscript', 'Subscript',
             'SmallCaps', 'Underline'): return node_text(c)
    if t == 'Quoted': return node_text(c[1])
    if t in ('Link', 'Image'): return node_text(c[1])
    if t == 'Span': return node_text(c[1])
    if t in ('Code',): return c[1]
    if t in ('RawInline',): return ''
    if t == 'Note': return ''
    return ''

def has_cjk(n):  return bool(CJKCH.search(node_text(n)))

# --------------------------------------------------------------- inline rendering
def esc(s): return html.escape(s, quote=False)

def render(ils):
    out = []
    for n in ils:
        t = n.get('t'); c = n.get('c')
        if t == 'Str': out.append(esc(c))
        elif t == 'Space': out.append(' ')
        elif t in ('SoftBreak',): out.append(' ')
        elif t == 'LineBreak': out.append('<br>')
        elif t == 'Strong': out.append('<b>' + render(c) + '</b>')
        elif t == 'Emph': out.append('<i>' + render(c) + '</i>')
        elif t == 'Underline': out.append('<u>' + render(c) + '</u>')
        elif t == 'Strikeout': out.append('<s>' + render(c) + '</s>')
        elif t == 'SmallCaps': out.append(render(c))
        elif t == 'Superscript': out.append('<sup>' + render(c) + '</sup>')
        elif t == 'Subscript': out.append('<sub>' + render(c) + '</sub>')
        elif t == 'Code': out.append('<code>' + esc(c[1]) + '</code>')
        elif t == 'Quoted':
            q = '“”' if c[0]['t'] == 'DoubleQuote' else '‘’'
            out.append(q[0] + render(c[1]) + q[1])
        elif t == 'Link':
            url = c[2][0]
            ext = url.startswith('http')
            attrs = ' target="_blank" rel="noopener noreferrer"' if ext else ''
            out.append('<a href="%s"%s>%s</a>' % (html.escape(url, quote=True), attrs, render(c[1])))
        elif t == 'Image':
            out.append('<img src="%s" alt="%s">' % (html.escape(c[2][0], quote=True),
                                                    html.escape(node_text(c[1]), quote=True)))
        elif t == 'Span': out.append(render(c[1]))
        elif t == 'RawInline':
            if c[0] in ('html', 'raw_html'): out.append(c[1])
        elif t == 'Note': pass
        else: out.append(esc(node_text(n)))
    return ''.join(out)

# ------------------------------------------------- splitting one bilingual run
def expand_strs(ils):
    """Split every Str into maximal Chinese / non-Chinese runs, so a boundary with no
       space around it ("…（不是软件操作课）Learning how…") becomes a real node boundary."""
    out = []
    for n in ils:
        if not isinstance(n, dict): continue
        t = n.get('t')
        if t == 'Str':
            s = n['c']; run = ''; flag = None
            for ch in s:
                f = cjkish(ch)
                if flag is None or f == flag: run += ch
                else: out.append({'t': 'Str', 'c': run}); run = ch
                flag = f
            if run: out.append({'t': 'Str', 'c': run})
        elif t in ('Strong', 'Emph', 'Underline', 'Strikeout', 'Superscript', 'Subscript'):
            out.append({'t': t, 'c': expand_strs(n['c'])})
        else:
            out.append(n)
    return out

MIN_EN = 10        # an English tail shorter than this is punctuation, not a translation
MIN_ZH_IDEO = 2    # and the Chinese side must be more than a stray bracket

def split_inlines(ils):
    """(zh_inlines, en_inlines) or None. The rule the documents actually follow is
       'Chinese first, then English', so the split is after the LAST Chinese node —
       provided what follows is long enough to be a real translation."""
    ils = expand_strs(ils)
    ils = [n for n in ils if isinstance(n, dict)]
    if not ils: return None

    # a run that is one bold/italic wrapper: recurse into it and re-wrap both halves
    if len(ils) == 1 and ils[0].get('t') in ('Strong', 'Emph', 'Underline'):
        inner = split_inlines(ils[0]['c'])
        if not inner: return None
        t = ils[0]['t']
        return ([{'t': t, 'c': inner[0]}], [{'t': t, 'c': inner[1]}])

    idx = [i for i, n in enumerate(ils) if has_cjk(n)]
    if not idx: return None
    last = idx[-1]
    if last == len(ils) - 1: return None          # Chinese runs to the end: interleaved
    zh, en = ils[:last + 1], ils[last + 1:]
    while zh and zh[-1].get('t') in ('Space', 'SoftBreak'): zh.pop()
    while en and en[0].get('t') in ('Space', 'SoftBreak'): en.pop(0)
    # a bullet or dash that separated the two languages belongs to neither
    while en and en[0].get('t') == 'Str' and en[0]['c'].strip() in ('\u00b7', '\u2014', '\u2013', '-', '|', '/'):
        en = en[1:]
        while en and en[0].get('t') in ('Space', 'SoftBreak'): en = en[1:]
    while zh and zh[-1].get('t') == 'Str' and zh[-1]['c'].strip() in ('\u00b7', '\u2014', '\u2013', '-', '|', '/'):
        zh = zh[:-1]
        while zh and zh[-1].get('t') in ('Space', 'SoftBreak'): zh = zh[:-1]
    if not zh or not en: return None
    if len(IDEOCH.findall(node_text(zh))) < MIN_ZH_IDEO: return None
    # a short run is a label ("\u5b66\u6bb5 Level"); a long one is a sentence, where a
    # two-word tail is far more likely to be punctuation than a translation
    min_en = 3 if len(node_text(ils).strip()) <= 26 else MIN_EN
    if len(node_text(en).strip()) < min_en: return None
    return zh, en

SHARED = []   # runs that could not be split, reported at the end of the run

def strip_fillin(ils):
    """A trailing 【请填写 Fill in：…】 note is deliberately bilingual in one bracket.
       Peel it off so the sentence in front of it can still be split, then show the
       bracket once, after both language versions."""
    txt = node_text(ils)
    if '\u3010' not in txt or not txt.rstrip().endswith('\u3011'): return ils, ''
    depth = 0
    for k in range(len(ils) - 1, -1, -1):
        t = node_text(ils[k])
        depth += t.count('\u3011') - t.count('\u3010')
        if depth <= 0 and '\u3010' in t:
            node = ils[k]
            head, tail = ils[:k], ils[k:]
            if node.get('t') == 'Str' and not node['c'].startswith('\u3010'):
                cut = node['c'].index('\u3010')
                head = head + [{'t': 'Str', 'c': node['c'][:cut]}]
                tail = [{'t': 'Str', 'c': node['c'][cut:]}] + tail[1:]
            while head and head[-1].get('t') in ('Space', 'SoftBreak'): head = head[:-1]
            return head, render(tail)
    return ils, ''

def bi_inlines(ils, where):
    """render a run as a zh/en pair when it can be split, otherwise once"""
    ils = expand_strs(ils)
    ils, tail = strip_fillin(ils)
    if tail:
        head_txt = node_text(ils)
        gap = '' if (head_txt.rstrip()[-1:] in CJK_PUNCT or not head_txt.strip()) else ' '
        s = split_inlines(ils)
        if s: return ('<span class="zh">%s</span><span class="en">%s</span>%s%s'
                      % (render(s[0]), render(s[1]), gap, tail))
        return render(ils) + gap + tail
    s = split_inlines(ils)
    if s: return '<span class="zh">%s</span><span class="en">%s</span>' % (render(s[0]), render(s[1]))
    txt = node_text(ils).strip()
    if txt and has_cjk(ils) and len(txt) > 24: SHARED.append((where, txt[:90]))
    return render(ils)

def bi(zh_html, en_html):
    return '<span class="zh">%s</span><span class="en">%s</span>' % (zh_html, en_html)

# ------------------------------------------------------------- block rendering
def slug(n, used):
    base = re.sub(r'[^a-z0-9]+', '-', node_text(n).lower()).strip('-') or 'section'
    s = base; i = 2
    while s in used: s = '%s-%d' % (base, i); i += 1
    used.add(s); return s

def render_blocks(blocks, where, used=None, level_shift=0):
    if used is None: used = set()
    out, toc = [], []
    i = 0
    while i < len(blocks):
        b = blocks[i]; t = b.get('t')

        if t == 'Header':
            lvl, attr, ils = b['c']
            lvl = min(6, lvl + level_shift)
            nxt = blocks[i + 1] if i + 1 < len(blocks) else None
            if (nxt and nxt.get('t') == 'Header' and nxt['c'][0] == b['c'][0]
                    and has_cjk(ils) and not has_cjk(nxt['c'][2])):
                zh, en = ils, nxt['c'][2]; i += 2
            else:
                sp = split_inlines(ils)
                if sp: zh, en = sp
                else: zh = en = ils
                i += 1
            sid = slug(en, used)
            out.append('<h%d id="%s">%s</h%d>' % (lvl, sid, bi(render(zh), render(en)), lvl))
            if lvl == 2: toc.append((sid, render(zh), render(en)))
            continue

        if t in ('Para', 'Plain'):
            ils = b['c']
            nxt = blocks[i + 1] if i + 1 < len(blocks) else None
            if (nxt and nxt.get('t') in ('Para', 'Plain')
                    and has_cjk(ils) and not has_cjk(nxt['c'])
                    and len(node_text(nxt['c']).strip()) >= MIN_EN):
                out.append('<p>%s</p>' % bi(render(ils), render(nxt['c']))); i += 2; continue
            out.append('<p>%s</p>' % bi_inlines(ils, where)); i += 1; continue

        if t == 'HorizontalRule':
            out.append('<hr>'); i += 1; continue

        if t == 'BlockQuote':
            inner, _ = render_blocks(b['c'], where, used, level_shift)
            out.append('<blockquote class="card note">%s</blockquote>' % inner); i += 1; continue

        if t in ('BulletList', 'OrderedList'):
            items = b['c'] if t == 'BulletList' else b['c'][1]
            tag = 'ul' if t == 'BulletList' else 'ol'
            lis = []
            for it in items:
                if len(it) == 1 and it[0].get('t') in ('Para', 'Plain'):
                    lis.append('<li>%s</li>' % bi_inlines(it[0]['c'], where))
                else:
                    inner, _ = render_blocks(it, where, used, level_shift)
                    lis.append('<li>%s</li>' % inner)
            out.append('<%s>%s</%s>' % (tag, ''.join(lis), tag)); i += 1; continue

        if t == 'Table':
            out.append(render_table(b, where)); i += 1; continue

        if t == 'Div':
            inner, t2 = render_blocks(b['c'][1], where, used, level_shift)
            out.append(inner); toc += t2; i += 1; continue

        if t == 'CodeBlock':
            out.append('<pre><code>%s</code></pre>' % esc(b['c'][1])); i += 1; continue

        if t == 'RawBlock':
            if b['c'][0] in ('html', 'raw_html'): out.append(b['c'][1])
            i += 1; continue

        if t == 'LineBlock':
            out.append('<p>%s</p>' % '<br>'.join(bi_inlines(l, where) for l in b['c']))
            i += 1; continue

        i += 1
    return ''.join(out), toc

def cell_html(cell, where):
    blocks = cell[4]
    if len(blocks) == 1 and blocks[0].get('t') in ('Para', 'Plain'):
        return bi_inlines(blocks[0]['c'], where)
    inner, _ = render_blocks(blocks, where)
    return inner

def render_table(b, where):
    _, _, _, head, bodies, foot = b['c']
    rows = []
    heads = [node_text(c[4][0]['c']) if c[4] and c[4][0].get('c') else '' for r in head[1] for c in r[1]]
    if any(h.strip() for h in heads):
        for r in head[1]:
            rows.append('<tr class="head">' + ''.join('<th>%s</th>' % cell_html(c, where) for c in r[1]) + '</tr>')
    else:
        heads = ['' for _ in heads]
    for body in bodies:
        for r in body[3]:
            tds = []
            for j, c in enumerate(r[1]):
                lab = heads[j] if j < len(heads) else ''
                sp = split_inlines(c[4][0]['c']) if (lab and c[4] and c[4][0].get('t') in ('Para', 'Plain')) else None
                # the mobile card layout labels each cell with its column heading
                zl, el = ('', '')
                if lab:
                    hp = re.match(r'^\s*([%s%s]+)\s+(.+)$' % (IDEO, re.escape(CJK_PUNCT)), lab)
                    if hp: zl, el = hp.group(1), hp.group(2)
                    else: zl = el = lab
                attrs = ' data-zh="%s" data-en="%s"' % (html.escape(zl, quote=True),
                                                        html.escape(el, quote=True)) if zl else ''
                tds.append('<td%s>%s</td>' % (attrs, cell_html(c, where)))
            rows.append('<tr>' + ''.join(tds) + '</tr>')
    for r in foot[1]:
        rows.append('<tr>' + ''.join('<td>%s</td>' % cell_html(c, where) for c in r[1]) + '</tr>')
    cls = ' class="cards"'
    return '<div class="table-wrap"><table%s>%s</table></div>' % (cls, ''.join(rows))

# ------------------------------------------------------------------ page shell
BRAND_SVG = ('<svg class="brand-mark" viewBox="0 0 64 64" aria-hidden="true" focusable="false" fill="none" '
 'stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">'
 '<path d="M5 17 Q18.5 13.5 30.5 19 L30.5 47 Q18.5 52.5 5 45 Z" stroke-width="2.4"/>'
 '<path d="M59 17 Q45.5 13.5 33.5 19 L33.5 47 Q45.5 52.5 59 45 Z" stroke-width="2.4"/>'
 '<path d="M5 41.4 Q18.5 48.9 30.5 43.4" stroke-width="1.5"/>'
 '<path d="M59 41.4 Q45.5 48.9 33.5 43.4" stroke-width="1.5"/>'
 '<rect x="8.6" y="21.6" width="18.4" height="16" rx="2.2" stroke-width="1.8"/>'
 '<rect x="37" y="21.6" width="18.4" height="16" rx="2.2" stroke-width="1.8"/>'
 '<path d="M11.4 27.6 H24.2" stroke-width="1.9"/><path d="M11.4 32.6 H21" stroke-width="1.9"/>'
 '<path d="M39.8 27.6 H52.6" stroke-width="1.9"/><path d="M39.8 32.6 H49.4" stroke-width="1.9"/>'
 '<path d="M32 18 V48" stroke-width="2.6"/><path d="M29.6 26 H34.4" stroke-width="1.6"/>'
 '<path d="M29.6 40 H34.4" stroke-width="1.6"/></svg>')

# The header mark and the long-document rules now live in assets/site.css; nothing
# on these pages is one-off enough to need an inline <style>.
DOC_STYLE = ''

def page(title_zh, title_en, kicker_zh, kicker_en, toc, body, downloads, desc):
    toc_html = ''
    if toc:
        lis = ''.join('<li><a href="#%s">%s</a></li>' % (i, bi(z, e)) for i, z, e in toc)
        toc_html = ('<nav class="doc-toc" aria-labelledby="doc-toc-title">'
                    '<h2 id="doc-toc-title">%s</h2><ol>%s</ol></nav>'
                    % (bi('本文目录', 'Contents'), lis))
    dl = ''
    if downloads:
        dl = '<p class="doc-downloads">' + ''.join(
            '<a href="%s" download>%s</a>' % (h, bi(z, e)) for h, z, e in downloads) + '</p>'
    return """<!DOCTYPE html>
<html lang="zh-CN" data-lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{desc}">
<script>(function(){{var l=null;try{{l=localStorage.getItem("dl:lang")}}catch(e){{}}if(l!=="zh"&&l!=="en"){{var n=(navigator.language||"").toLowerCase();l=n.indexOf("zh")===0?"zh":"en"}}var h=document.documentElement;h.setAttribute("data-lang",l);h.setAttribute("lang",l==="zh"?"zh-CN":"en")}})();</script>
<title data-zh="{tz} · Digital Learning 数字化学习" data-en="{te} · Digital Learning">{te} · Digital Learning</title>
<link rel="stylesheet" href="../assets/site.css">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
{style}
</head>
<body>
<a class="skip" href="#main"><span class="zh">跳到正文</span><span class="en">Skip to content</span></a>
<header class="site"><div class="wrap">
  <a class="brand" href="../index.html">{brand}Digital Learning 数字化学习</a>
  <nav aria-label="Site 站点"><a href="../index.html"><span class="zh">课程首页</span><span class="en">Course home</span></a><a href="../index.html#community"><span class="zh">学习共同体</span><span class="en">Community</span></a><a href="../calendar.html"><span class="zh">日历</span><span class="en">Calendar</span></a></nav>
  <button type="button" class="lang-toggle" data-lang-toggle aria-label="Switch language 切换语言"><span data-l="en">English</span><span class="sep" aria-hidden="true"> / </span><span data-l="zh">中文</span></button>
</div></header>
<main id="main">
<p class="kicker">{kick}</p>
<h1>{h1}</h1>
{dl}
{toc}
{body}
</main>
<footer class="site">Digital Learning 数字化学习 · 公开课程 A public course · 段玉佩 Yupei Duan · 2026–27</footer>
<script src="../assets/lang.js"></script>
</body>
</html>
""".format(desc=html.escape(desc, quote=True), tz=title_zh, te=title_en, style=DOC_STYLE,
           brand=BRAND_SVG, kick=bi(kicker_zh, kicker_en), h1=bi(title_zh, title_en),
           dl=dl, toc=toc_html, body=body)

# ------------------------------------------------------------------ documents
def from_markdown(src, out, title_zh, title_en, kicker_zh, kicker_en, downloads, desc):
    ast = json.loads(subprocess.check_output(['pandoc', src, '-t', 'json']))
    blocks = ast['blocks']
    # the two title headings and the standing subtitle are rebuilt by the shell
    while blocks and blocks[0].get('t') == 'Header' and blocks[0]['c'][0] == 1:
        blocks.pop(0)
    while blocks and blocks[0].get('t') == 'HorizontalRule':
        blocks.pop(0)
    body, toc = render_blocks(blocks, os.path.basename(src))
    open(out, 'w', encoding='utf-8').write(
        page(title_zh, title_en, kicker_zh, kicker_en, toc, body, downloads, desc))
    print('  wrote', os.path.relpath(out, ROOT), '(%d sections)' % len(toc))

def from_site_page(src, out, title_zh, title_en, kicker_zh, kicker_en, downloads, desc):
    """for-mentors.html is already a page of this site: reuse its <main>, fix the
       relative links for resources/, and give the long read a contents list."""
    s = open(src, encoding='utf-8').read()
    body = s[s.index('<main id="main">') + len('<main id="main">'): s.index('</main>')]
    # this page lives one directory down
    body = re.sub(r'href="(?!https?:|#|\.\./|mailto:)', 'href="../', body)
    body = re.sub(r'src="(?!https?:|\.\./|data:)', 'src="../', body)
    # its own kicker and h1 are replaced by the shell's
    body = re.sub(r'^\s*<p class="kicker">.*?</p>\s*', '', body, count=1, flags=re.S)
    body = re.sub(r'^\s*<h1>.*?</h1>\s*', '', body, count=1, flags=re.S)
    toc = []
    used = set()
    def head(m):
        attrs, inner = m.group(1), m.group(2)
        had = re.search(r'\bid="([^"]+)"', attrs)
        zh = re.search(r'<span class="zh">(.*?)</span>', inner, re.S)
        en = re.search(r'<span class="en">(.*?)</span>', inner, re.S)
        zt = zh.group(1) if zh else inner
        et = en.group(1) if en else inner
        sid = had.group(1) if had else (
            re.sub(r'[^a-z0-9]+', '-', re.sub(r'<[^>]+>', '', et).lower()).strip('-') or 'section')
        b = sid; i = 2
        while sid in used: sid = '%s-%d' % (b, i); i += 1
        used.add(sid)
        toc.append((sid, zt, et))
        return '<h2 id="%s">%s</h2>' % (sid, inner)
    body = re.sub(r'<h2([^>]*)>(.*?)</h2>', head, body, flags=re.S)
    open(out, 'w', encoding='utf-8').write(
        page(title_zh, title_en, kicker_zh, kicker_en, toc, body, downloads, desc))
    print('  wrote', os.path.relpath(out, ROOT), '(%d sections)' % len(toc))

def main():
    os.chdir(ROOT)
    print('building the three community documents as site pages')
    from_markdown(
        'tools/documents/letter-to-parents.md', 'resources/letter-to-parents.html',
        '致家长的一封信', 'A Letter to Parents',
        '课程站点 · 公开文件 · 约 5 分钟', 'Course site · Open document · ~5 min',
        [('letter-to-parents.pdf', '下载 PDF', 'Download PDF'),
         ('letter-to-parents-editable.docx', '编辑 Word', 'Edit in Word')],
        '致家长的一封信：这门课怎么运行、孩子每周做什么、我们怎样保护他，以及您能怎样帮忙。 · '
        'A letter to parents: how the course runs, what your child does each week, how we protect them, and how you can help.')
    from_markdown(
        'tools/documents/letter-to-school-administrators.md',
        'resources/letter-to-school-administrators.html',
        '致学校管理者的一封信', 'A Letter to School Administrators',
        '课程站点 · 公开文件 · 约 5 分钟', 'Course site · Open document · ~5 min',
        [('letter-to-school-administrators.pdf', '下载 PDF', 'Download PDF'),
         ('letter-to-school-administrators.docx', '编辑 Word', 'Edit in Word')],
        '致学校管理者的一封信：一页看懂这门课，以及整门开设、嵌入已有课程、开放资源三种落地方式。 · '
        'A letter to school administrators: the course on one page, and three ways to implement it.')
    from_site_page(
        'for-mentors.html', 'resources/mentor-handbook.html',
        '导师手册', 'Mentor Handbook',
        '课程站点 · 公开文件', 'Course site · Open document',
        [('mentor-handbook.pdf', '下载 PDF', 'Download PDF'),
         ('mentor-handbook.docx', '编辑 Word', 'Edit in Word')],
        '导师手册：导师每周做什么、怎么按量规评分、怎么写反馈，以及哪些事导师一概不做。 · '
        'Mentor handbook: what a mentor does each week, how work is scored, how feedback is written, and what a mentor never does.')
    if SHARED:
        print('\n%d run(s) could not be split into zh/en and are shown in both languages:' % len(SHARED))
        for w, t in SHARED: print('   [%s] %s' % (w, t))
    else:
        print('\nevery bilingual run split cleanly')

if __name__ == '__main__':
    main()
