#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Release gates for course-site that need no browser. Run from anywhere:

    python3 tools/check-release.py            # everything except the network check
    python3 tools/check-release.py --bilibili # also resolve every BV id through the API

Gates
  1  every <input type=checkbox> inside ul.checklist has a stable id, and every list
     has an id. checklist.js keys saved ticks by that id; with no id it does not save,
     because a positional key silently shifts every tick when an item is inserted.
  2  every [data-module-progress] declares data-total and data-pages, and data-total
     equals the number of checkboxes actually present in that module.
  3  every page has a <meta name="description">.
  4  every teaching page (not rubric / quiz / want-more / self-check / statement)
     carries a Bilibili embed or a marked ［placeholder］.
  5  every Bilibili embed has danmaku=0 and autoplay=0; no YouTube, no Google-hosted asset.
  6  every non-Bilibili external link is marked 待实测 inside its own list item or paragraph.
  7  no duplicate id anywhere in one page.
  8  with --bilibili: every BV id resolves through api.bilibili.com/x/web-interface/view.

The browser gates (console errors, horizontal overflow at 320/390/600/900) are not here;
they need Chrome, and are documented in the site-wide review's re-run checklist.
"""
import collections, glob, json, os, re, subprocess, sys, time, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

EXEMPT = ('rubric.html', 'quiz.html', 'want-more.html', 'self-check.html', 'statement.html')
BLOCK = re.compile(r'</?(?:li|p|td|th|h[1-6]|summary)\b')

pages = [f for f in sorted(glob.glob('**/*.html', recursive=True)) if f != 'assets/page-template.html']
fail = []

def bad(gate, msg):
    fail.append((gate, msg))

# ---- 1 & 2 ------------------------------------------------------------------
counts = collections.defaultdict(lambda: [0, 0])
for f in pages:
    s = open(f, encoding='utf-8').read()
    for m in re.finditer(r'<ul\b[^>]*class="[^"]*\bchecklist\b[^"]*"[^>]*>(.*?)</ul>', s, re.S):
        tag = m.group(0)[:m.group(0).find('>') + 1]
        if not re.search(r'\bid="', tag):
            bad(1, '%s: a ul.checklist has no id' % f)
        boxes = re.findall(r'<input\b[^>]*type=["\']?checkbox["\']?[^>]*>', m.group(1))
        for b in boxes:
            if not re.search(r'\bid="', b):
                bad(1, '%s: a checklist checkbox has no id -> its ticks would not be saved' % f)
        d = os.path.dirname(f)
        counts[d][0] += len(boxes); counts[d][1] += 1

for f in pages:
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<div\b[^>]*data-module-progress[^>]*>', s)
    if not m: continue
    tot = re.search(r'data-total="(\d+)"', m.group(0))
    pgs = re.search(r'data-pages="(\d+)"', m.group(0))
    d = os.path.dirname(f)
    if not tot or not pgs:
        bad(2, '%s: [data-module-progress] needs data-total and data-pages' % f); continue
    if int(tot.group(1)) != counts[d][0]:
        bad(2, '%s: data-total=%s but %d checkboxes exist in %s' % (f, tot.group(1), counts[d][0], d))
    if int(pgs.group(1)) != counts[d][1]:
        bad(2, '%s: data-pages=%s but %d pages carry a list' % (f, pgs.group(1), counts[d][1]))

# ---- 3..7 -------------------------------------------------------------------
bvids = set()
for f in pages:
    s = open(f, encoding='utf-8').read()
    if 'name="description"' not in s:
        bad(3, '%s: no <meta name="description">' % f)

    if f.startswith('s1/') and os.path.basename(f) not in EXEMPT and '/media/handouts/' not in f:
        if 'player.bilibili.com' not in s and 'placeholder' not in s:
            bad(4, '%s: a teaching page with neither a video nor a marked placeholder' % f)

    for m in re.finditer(r'player\.bilibili\.com/player\.html\?([^"\']+)', s):
        q = urllib.parse.parse_qs(m.group(1).replace('&amp;', '&'))
        if q.get('danmaku', ['1'])[0] != '0': bad(5, '%s: an embed does not switch danmaku off' % f)
        if q.get('autoplay', ['1'])[0] != '0': bad(5, '%s: an embed does not switch autoplay off' % f)
        bvids.update(q.get('bvid', []))
    for pat, what in (('youtube.com', 'YouTube'), ('youtu.be', 'YouTube'),
                      ('googleapis.com', 'a Google-hosted asset'), ('gstatic.com', 'a Google-hosted asset'),
                      ('fonts.google', 'a Google-hosted font')):
        if pat in s: bad(5, '%s: links to %s, unreachable from the mainland' % (f, what))

    for m in re.finditer(r'<a\b[^>]*href="(https?://[^"]+)"[^>]*>.*?</a>', s, re.S):
        if 'bilibili.com' in m.group(1): continue
        starts = [x.end() for x in BLOCK.finditer(s, 0, m.start())]
        st = starts[-1] if starts else 0
        e = BLOCK.search(s, m.end()); en = e.start() if e else len(s)
        if '待实测' not in s[st:en]:
            bad(6, '%s: external link not marked 待实测 — %s' % (f, m.group(1)))

    ids = re.findall(r'\sid="([^"]+)"', s)
    for k, v in collections.Counter(ids).items():
        if v > 1: bad(7, '%s: id "%s" appears %d times' % (f, k, v))

# ---- 8 ----------------------------------------------------------------------
if '--bilibili' in sys.argv:
    UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
          '(KHTML, like Gecko) Chrome/126.0 Safari/537.36')
    jar = os.path.join(ROOT, '.bili-cookies.tmp')
    subprocess.run(['curl', '-s', '-m', '30', '-c', jar, '-H', 'User-Agent: ' + UA,
                    '-o', os.devnull, 'https://www.bilibili.com/'])
    # Bilibili rate-limits an unauthenticated client hard; one call every 2s clears it.
    for bv in sorted(bvids):
        for attempt in range(4):
            try:
                out = subprocess.check_output(
                    ['curl', '-s', '-m', '30', '-b', jar, '-c', jar, '-H', 'User-Agent: ' + UA,
                     '-H', 'Referer: https://www.bilibili.com/',
                     'https://api.bilibili.com/x/web-interface/view?bvid=' + bv])
                d = json.loads(out)
                if d.get('code') == -799 or '频繁' in str(d.get('message', '')):
                    time.sleep(6 * (attempt + 1)); continue
                break
            except Exception:
                d = None; time.sleep(4 * (attempt + 1))
        time.sleep(2)
        try:
            if d is None: raise ValueError('no response after retries')
            if d.get('code') != 0:
                bad(8, 'BV id does not resolve: %s (%s)' % (bv, d.get('message')))
            else:
                print('   %s  %d:%02d  %s' % (bv, d['data']['duration'] // 60,
                                              d['data']['duration'] % 60, d['data']['title'][:56]))
        except Exception as e:
            bad(8, 'BV id could not be checked: %s (%s)' % (bv, e))
    try: os.remove(jar)
    except OSError: pass

# ---- report -----------------------------------------------------------------
print('\npages: %d   Bilibili ids in use: %d' % (len(pages), len(bvids)))
if not fail:
    print('all gates pass')
    sys.exit(0)
by = collections.defaultdict(list)
for g, m in fail: by[g].append(m)
for g in sorted(by):
    print('\ngate %d — %d problem(s)' % (g, len(by[g])))
    for m in by[g][:25]: print('   ' + m)
sys.exit(1)
