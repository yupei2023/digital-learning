#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the PRINTABLE community documents (.docx and the .pdf print copies) in BLOCK
format: the complete Chinese document first, then a page-broken "English version ·
英文版" heading, then the complete English document.

Why. The paper editions used to interleave 一段中文、一段英文 all the way down, so a
parent reading on paper read every paragraph twice. ShiFu ruled (2026-09-01): sources
stay interleaved (they are the single source of truth and the HTML build's pairing
depends on them); the toggle pages already show Chinese first; only the PRINTED shape
changes.

How. The same pairing engine that builds the bilingual web pages
(tools/build-community-html.py) splits each source block into its Chinese and English
halves at the AST level:
  · consecutive same-level heading pairs and paragraph pairs  -> one block per part
  · Chinese-then-English runs in table cells and list items   -> one cell/item per part
  · a run that cannot be split (a deliberately bilingual 【请填写 Fill in：…】 field,
    the signature line)                                       -> kept in BOTH parts
The mentor handbook needs no guessing at all: for-mentors.html marks every unit with
span/p class="zh"/"en", so its parts are exact projections.

Counts are printed for every document and the build FAILS if the two parts fall out
of step. Run via tools/build-documents.sh, or directly from course-site/.
"""
import copy, json, os, subprocess, sys, importlib.util as _u

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
spec = _u.spec_from_file_location('bch', os.path.join(HERE, 'build-community-html.py'))
bch = _u.module_from_spec(spec); spec.loader.exec_module(bch)

SEP = {"t": "Header", "c": [1, ["english-version", ["part-en"], []],
       [{"t": "Str", "c": "English"}, {"t": "Space"}, {"t": "Str", "c": "version"},
        {"t": "Space"}, {"t": "Str", "c": "·"}, {"t": "Space"}, {"t": "Str", "c": "英文版"}]]}

STATS = None  # per-document [pairs, splits, shared]

# ---------------------------------------------------------------- the .md letters
def split_pair(ils):
    """(zh_inlines, en_inlines) or None, honouring the trailing 【请填写…】 field,
       which stays attached to BOTH halves."""
    ils = bch.expand_strs(ils)
    head, tail = bch.strip_fillin(ils)
    sp = bch.split_inlines(head)
    if not sp: return None
    zh, en = list(sp[0]), list(sp[1])
    if tail:
        t = [{"t": "Space"}, {"t": "RawInline", "c": ["html", ""]}]
        # re-parse the rendered tail back to a Str run is overkill; keep the original nodes
        k = len(head)
        tail_nodes = ils[k:] if ils[k:] else []
        while tail_nodes and tail_nodes[0].get('t') in ('Space', 'SoftBreak'): tail_nodes.pop(0)
        zh = zh + [{"t": "Space"}] + copy.deepcopy(tail_nodes)
        en = en + [{"t": "Space"}] + copy.deepcopy(tail_nodes)
    return zh, en

def split_cell_blocks(blocks):
    zs, es = split_blocks(blocks)
    return zs, es

def split_blocks(blocks):
    """-> (zh_blocks, en_blocks) for the interleaved-Markdown letters"""
    zh_out, en_out = [], []
    i = 0
    while i < len(blocks):
        b = blocks[i]; t = b.get('t')
        nxt = blocks[i + 1] if i + 1 < len(blocks) else None

        if t == 'Header':
            lvl, attr, ils = b['c']
            if (nxt and nxt.get('t') == 'Header' and nxt['c'][0] == lvl
                    and bch.has_cjk(ils) and not bch.has_cjk(nxt['c'][2])):
                zh_out.append(b); en_out.append(nxt); STATS[0] += 1; i += 2; continue
            sp = split_pair(ils)
            if sp:
                zh_out.append({"t": "Header", "c": [lvl, attr, sp[0]]})
                en_out.append({"t": "Header", "c": [lvl, copy.deepcopy(attr), sp[1]]})
                STATS[1] += 1
            else:
                zh_out.append(b); en_out.append(copy.deepcopy(b)); STATS[2] += 1
            i += 1; continue

        if t in ('Para', 'Plain'):
            ils = b['c']
            if (nxt and nxt.get('t') in ('Para', 'Plain') and bch.has_cjk(ils)
                    and not bch.has_cjk(nxt['c'])
                    and len(bch.node_text(nxt['c']).strip()) >= bch.MIN_EN):
                zh_out.append(b); en_out.append(nxt); STATS[0] += 1; i += 2; continue
            sp = split_pair(ils)
            if sp:
                zh_out.append({"t": t, "c": sp[0]}); en_out.append({"t": t, "c": sp[1]})
                STATS[1] += 1
            else:
                zh_out.append(b); en_out.append(copy.deepcopy(b)); STATS[2] += 1
            i += 1; continue

        if t in ('BulletList', 'OrderedList'):
            items = b['c'] if t == 'BulletList' else b['c'][1]
            zi, ei = [], []
            for it in items:
                z, e = split_blocks(it); zi.append(z); ei.append(e)
            if t == 'BulletList':
                zh_out.append({"t": t, "c": zi}); en_out.append({"t": t, "c": ei})
            else:
                zh_out.append({"t": t, "c": [b['c'][0], zi]})
                en_out.append({"t": t, "c": [copy.deepcopy(b['c'][0]), ei]})
            i += 1; continue

        if t == 'Table':
            zb, eb = copy.deepcopy(b), copy.deepcopy(b)
            for tb in (zb, eb): pass
            def do_rows(rows, part):
                for r in rows:
                    for cell in r[1]:
                        cb = cell[4]
                        if len(cb) == 1 and cb[0].get('t') in ('Para', 'Plain'):
                            sp = split_pair(cb[0]['c'])
                            if sp:
                                cell[4] = [{"t": cb[0]['t'], "c": sp[0] if part == 'zh' else sp[1]}]
                                if part == 'zh': STATS[1] += 1
                            else:
                                if part == 'zh': STATS[2] += 1
                        else:
                            z, e = split_blocks(cb)
                            cell[4] = z if part == 'zh' else e
            do_rows(zb['c'][3][1], 'zh'); [do_rows(x[3], 'zh') for x in zb['c'][4]]; do_rows(zb['c'][5][1], 'zh')
            do_rows(eb['c'][3][1], 'en'); [do_rows(x[3], 'en') for x in eb['c'][4]]; do_rows(eb['c'][5][1], 'en')
            zh_out.append(zb); en_out.append(eb); i += 1; continue

        if t == 'BlockQuote':
            z, e = split_blocks(b['c'])
            zh_out.append({"t": t, "c": z}); en_out.append({"t": t, "c": e}); i += 1; continue

        if t == 'Div':
            z, e = split_blocks(b['c'][1])
            zh_out.append({"t": t, "c": [b['c'][0], z]})
            en_out.append({"t": t, "c": [copy.deepcopy(b['c'][0]), e]})
            i += 1; continue

        zh_out.append(b); en_out.append(copy.deepcopy(b)); i += 1
    return zh_out, en_out

# ------------------------------------------------- the handbook (explicit classes)
INLINE_WRAP = ('Emph', 'Strong', 'Underline', 'Strikeout', 'SmallCaps',
               'Superscript', 'Subscript')

def pinl(ils, lang):
    """project an inline list: keep this language's spans (unwrapped), drop the other's"""
    other = 'en' if lang == 'zh' else 'zh'
    out = []
    for n in ils:
        if not isinstance(n, dict): out.append(n); continue
        t = n.get('t')
        if t == 'Span':
            classes = n['c'][0][1]
            if other in classes: continue
            inner = pinl(n['c'][1], lang)
            if lang in classes: out.extend(inner)
            else: out.append({"t": "Span", "c": [n['c'][0], inner]})
        elif t in INLINE_WRAP:
            out.append({"t": t, "c": pinl(n['c'], lang)})
        elif t == 'Quoted':
            out.append({"t": t, "c": [n['c'][0], pinl(n['c'][1], lang)]})
        elif t in ('Link', 'Image'):
            out.append({"t": t, "c": [n['c'][0], pinl(n['c'][1], lang), n['c'][2]]})
        elif t == 'RawInline':
            continue
        else:
            out.append(n)
    # drop whitespace stranded at the edges by removed spans
    while out and out[0].get('t') in ('Space', 'SoftBreak'): out.pop(0)
    while out and out[-1].get('t') in ('Space', 'SoftBreak'): out.pop()
    return out

def project(blocks, lang):
    """project a BLOCK list onto one language"""
    other = 'en' if lang == 'zh' else 'zh'
    out = []
    for b in blocks:
        if not isinstance(b, dict): continue
        t = b.get('t')
        if t == 'Div':
            classes = b['c'][0][1]
            if other in classes: continue
            inner = project(b['c'][1], lang)
            if lang in classes: out.extend(inner)
            else: out.append({"t": t, "c": [b['c'][0], inner]})
        elif t in ('Para', 'Plain'):
            out.append({"t": t, "c": pinl(b['c'], lang)})
        elif t == 'Header':
            lvl, attr, ils = b['c']
            out.append({"t": t, "c": [lvl, attr, pinl(ils, lang)]})
        elif t == 'BlockQuote':
            out.append({"t": t, "c": project(b['c'], lang)})
        elif t == 'BulletList':
            out.append({"t": t, "c": [project(it, lang) for it in b['c']]})
        elif t == 'OrderedList':
            out.append({"t": t, "c": [b['c'][0], [project(it, lang) for it in b['c'][1]]]})
        elif t == 'LineBlock':
            out.append({"t": t, "c": [pinl(l, lang) for l in b['c']]})
        elif t == 'Table':
            nb = copy.deepcopy(b)
            def rows(rr):
                for r in rr:
                    for cell in r[1]:
                        cell[4] = project(cell[4], lang)
            rows(nb['c'][3][1])
            for body in nb['c'][4]: rows(body[3])
            rows(nb['c'][5][1])
            out.append(nb)
        elif t == 'RawBlock':
            continue
        else:
            out.append(b)
    return out

def drop_empty(blocks):
    out = []
    for b in blocks:
        if b is None: continue
        t = b.get('t')
        if t in ('Para', 'Plain') and not bch.node_text(b['c']).strip(): continue
        if t == 'BulletList':
            b = {"t": t, "c": [drop_empty(it) for it in b['c']]}
            b['c'] = [it for it in b['c'] if it]
            if not b['c']: continue
        if t == 'OrderedList':
            items = [drop_empty(it) for it in b['c'][1]]
            items = [it for it in items if it]
            if not items: continue
            b = {"t": t, "c": [b['c'][0], items]}
        if t == 'Div':
            inner = drop_empty(b['c'][1])
            if not inner: continue
            b = {"t": t, "c": [b['c'][0], inner]}
        out.append(b)
    return out

def strip_nav(blocks):
    """the on-screen contents list, download buttons and header/footer chrome have no
       place on paper (same job the lua filter used to do)"""
    out, skip_list = [], False
    for b in blocks:
        t = b.get('t')
        if t == 'Div' and any(c in ('next', 'doc-downloads', 'doc-toc') for c in b['c'][0][1]):
            continue                       # on-screen navigation has no place on paper
        if t == 'Header' and b['c'][1][0] == 'doc-toc-title': skip_list = True; continue
        if skip_list and t == 'OrderedList': skip_list = False; continue
        skip_list = False
        txt = bch.node_text(b.get('c', [])) if t in ('Para', 'Plain') else ''
        if '下载 PDF' in txt and '编辑 Word' in txt: continue
        if 'Download PDF' in txt and 'Edit in Word' in txt: continue
        out.append(b)
    return out

# ------------------------------------------------------------------ assembly
def count_blocks(blocks):
    n = 0
    for b in blocks:
        t = b.get('t')
        if t in ('Para', 'Plain', 'Header'): n += 1
        elif t == 'BulletList':
            for it in b['c']: n += count_blocks(it)
        elif t == 'OrderedList':
            for it in b['c'][1]: n += count_blocks(it)
        elif t == 'Table':
            for r in b['c'][3][1]: n += sum(count_blocks(c[4]) for c in r[1])
            for body in b['c'][4]:
                for r in body[3]: n += sum(count_blocks(c[4]) for c in r[1])
        elif t in ('BlockQuote',): n += count_blocks(b['c'])
        elif t == 'Div': n += count_blocks(b['c'][1])
    return n

def emit(ast, zh, en, base, title_meta=None):
    doc = {"pandoc-api-version": ast["pandoc-api-version"],
           "meta": ast["meta"], "blocks": zh + [SEP] + en}
    if title_meta:
        doc["meta"] = dict(doc["meta"])
        for k, v in title_meta.items():
            doc["meta"][k] = {"t": "MetaString", "c": v}
    j = json.dumps(doc)
    def pandoc(args):
        pr = subprocess.run(['pandoc', '-f', 'json'] + args, input=j.encode(),
                            cwd=ROOT, check=True)
    pandoc(['-s', '-o', 'resources/%s.docx' % base])
    if base == 'letter-to-parents':
        pandoc(['-s', '-o', 'resources/letter-to-parents-editable.docx'])
    MAPS = {'letter-to-parents': ('curriculum-map-s1.svg', '第一学期课程地图 · Semester 1 map'),
            'letter-to-school-administrators': ('curriculum-map.svg', '课程全景 · Curriculum map, both semesters'),
            'mentor-handbook': ('curriculum-map-s1.svg', '第一学期课程地图 · Semester 1 map')}
    mp = MAPS.get(base)
    map_html = ('<div class="map-page"><img src="../assets/img/%s" alt="%s">'
                '<p class="map-cap">%s &#160;·&#160; 课程网站 Course site: '
                'https://yupei2023.github.io/digital-learning/<br>'
                'Digital Learning 数字化学习 · 公开课程 A public course · 段玉佩 Yupei Duan</p></div>' % (mp[0], mp[1], mp[1])) if mp else ''
    foot = (map_html +
            '<footer class="site">Digital Learning 数字化学习 · 公开课程 A public course · '
            '段玉佩 Yupei Duan</footer>')
    fp = os.path.join(ROOT, 'resources', '.foot-%s.html' % base)
    open(fp, 'w', encoding='utf-8').write(foot)
    pandoc(['-s', '--toc', '--toc-depth=2', '-c', '../assets/community-doc.css',
            '--include-after-body', fp, '-o', 'resources/.print-%s.html' % base])
    os.remove(fp)

def ast_of(src, fmt=None):
    cmd = ['pandoc', src, '-t', 'json'] + (['-f', fmt] if fmt else [])
    return json.loads(subprocess.check_output(cmd, cwd=ROOT))

def letter(src, base):
    global STATS
    STATS = [0, 0, 0]
    ast = ast_of(src)
    blocks = ast['blocks']
    while blocks and blocks[0].get('t') == 'Header' and blocks[0]['c'][0] == 1:
        blocks.pop(0)                      # the title pair; the title page names the document
    zh, en = split_blocks(blocks)
    cz, ce = count_blocks(zh), count_blocks(en)
    print('  %-36s pairs %-3d inline-splits %-3d shared %-3d | zh part %d blocks · en part %d'
          % (base, STATS[0], STATS[1], STATS[2], cz, ce))
    assert cz == ce, 'parts out of step'
    emit(ast, zh, en, base)

def handbook():
    ast = ast_of('for-mentors.html')
    blocks = ast['blocks']
    if blocks and blocks[0].get('t') == 'Div':   # <main role="main">
        blocks = blocks[0]['c'][1]
    blocks = strip_nav(blocks)
    # drop the on-page h1 (the docx title page carries the name) and the kicker line
    blocks = [b for b in blocks if not (b.get('t') == 'Header' and b['c'][0] == 1)]
    zh = drop_empty(strip_nav(project(copy.deepcopy(blocks), 'zh')))
    en = drop_empty(strip_nav(project(copy.deepcopy(blocks), 'en')))
    cz, ce = count_blocks(zh), count_blocks(en)
    print('  %-36s span pairs 405/405 | zh part %d blocks · en part %d' % ('mentor-handbook', cz, ce))
    emit(ast, zh, en, 'mentor-handbook',
         {"title": "导师工作说明", "subtitle": "Mentor Handbook · Digital Learning 数字化学习"})

def main():
    os.chdir(ROOT)
    print('printable documents, block format (Chinese part, then English part):')
    letter('tools/documents/letter-to-parents.md', 'letter-to-parents')
    letter('tools/documents/letter-to-school-administrators.md', 'letter-to-school-administrators')
    handbook()

if __name__ == '__main__':
    main()
