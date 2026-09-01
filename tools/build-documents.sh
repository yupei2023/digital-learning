#!/bin/sh
# Rebuild the three community documents in resources/.
#
# Three products, three shapes, one set of sources:
#
#   .html  the page a parent, a principal or a mentor READS ONLINE. A page of this
#          site — site.css, lang.js, the language button, every unit written as
#          <span class="zh"> + <span class="en"> so the reader sees ONE language.
#          Built by tools/build-community-html.py.
#
#   .docx  the file they EDIT, and
#   .pdf   the file they PRINT. Both are BLOCK format (ShiFu, 2026-09-01): the whole
#          Chinese document first, a page-broken "English version · 英文版" heading,
#          then the whole English document — paper cannot toggle, and interleaving
#          made a parent read everything twice. Built by tools/build-community-print.py,
#          which splits the same interleaved sources the HTML build pairs up; the
#          deliberately bilingual 【请填写 Fill in】 fields appear in both parts.
#
# Sources of truth (interleaved; do NOT restructure them):
#   tools/documents/letter-to-parents.md                 -> letter-to-parents.*
#   tools/documents/letter-to-school-administrators.md   -> letter-to-school-administrators.*
#   for-mentors.html  (the site page itself)             -> mentor-handbook.{docx,pdf}
#                                                           (its online form IS the page;
#                                                            the old second URL redirects)
#
# Run from anywhere. Requires: pandoc, python3, Google Chrome.

set -e
cd "$(dirname "$0")/.."

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
trap 'rm -f resources/.print-*.html resources/.foot-*.html' EXIT

# --- 1. the two letters as online pages, inside the design system --------------
python3 tools/build-community-html.py

# --- 2. the printable editions, block format ----------------------------------
python3 tools/build-community-print.py

# --- 3. PDFs, printed from the block-format print copies ----------------------
for n in letter-to-parents letter-to-school-administrators mentor-handbook; do
  "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
    --virtual-time-budget=10000 \
    --print-to-pdf="$PWD/resources/$n.pdf" "file://$PWD/resources/.print-$n.html" 2>/dev/null
done

echo "documents rebuilt"
