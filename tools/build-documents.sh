#!/bin/sh
# Rebuild the three community documents in resources/.
#
# Two different products come out of the same sources, and they are built by
# different tools on purpose:
#
#   .html  the page a parent or a principal READS ONLINE. It is a page of
#          this site — site.css, lang.js, the language button, and every unit written
#          as <span class="zh"> + <span class="en"> so the reader sees ONE language.
#          Built by tools/build-community-html.py. Pandoc cannot produce that shape.
#
#   .docx  the file they EDIT, and
#   .pdf   the file they PRINT. Both are pandoc/Chrome products laid out for paper by
#          assets/community-doc.css, and both show the two languages stacked, which is
#          right on paper and wrong on screen. The PDF is printed from a throwaway
#          print copy so that changing the online page never changes the printed one.
#
# Sources of truth
#   tools/documents/letter-to-parents.md                 -> letter-to-parents.*
#   tools/documents/letter-to-school-administrators.md   -> letter-to-school-administrators.*
#   for-mentors.html  (the site page itself)             -> mentor-handbook.{docx,pdf} only —
#                                                           the page itself is the online version
#
# Run from anywhere. Requires: pandoc, python3, Google Chrome.

set -e
cd "$(dirname "$0")/.."

F=tools/document-print-filter.lua
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FOOT='Digital Learning 数字化学习 · 公开课程 A public course · 段玉佩 Yupei Duan'
TMP=$(mktemp -d)
trap 'rm -rf "$TMP" resources/.print-*.html' EXIT

footer () { printf '<footer class="site">%s · %s</footer>\n' "$FOOT" "$1" > "$TMP/foot.html"; }

# --- 1. the two letters as online pages, inside the design system --------------
python3 tools/build-community-html.py

# --- 2. Letter to Parents · editable and printable ----------------------------
footer '致家长的一封信 A Letter to Parents'
pandoc tools/documents/letter-to-parents.md -s --toc --toc-depth=3 \
  --lua-filter=$F --include-after-body="$TMP/foot.html" \
  -c ../assets/community-doc.css -o resources/.print-letter-to-parents.html
pandoc tools/documents/letter-to-parents.md -s --lua-filter=$F \
  -o resources/letter-to-parents-editable.docx
pandoc tools/documents/letter-to-parents.md -s -o resources/letter-to-parents.docx

# --- 3. Letter to School Administrators ---------------------------------------
footer '致学校管理者的一封信 A Letter to School Administrators'
pandoc tools/documents/letter-to-school-administrators.md -s --toc --toc-depth=3 \
  --lua-filter=$F --include-after-body="$TMP/foot.html" \
  -c ../assets/community-doc.css -o resources/.print-letter-to-school-administrators.html
pandoc tools/documents/letter-to-school-administrators.md -s --lua-filter=$F \
  -o resources/letter-to-school-administrators.docx

# --- 4. Mentor handbook (rendered from the site page) -------------------------
footer '导师工作说明 How this course is mentored'
pandoc for-mentors.html -s --lua-filter=$F --include-after-body="$TMP/foot.html" \
  -M title="导师工作说明" -M subtitle="Mentor Handbook · Digital Learning 数字化学习" \
  -c ../assets/community-doc.css -o resources/.print-mentor-handbook.html
# for-mentors.html lives at the site root; its relative links need one level up here.
/usr/bin/sed -i '' \
  -e 's|href="s1/|href="../s1/|g' \
  -e 's|href="calendar.html"|href="../calendar.html"|g' \
  -e 's|href="index.html"|href="../index.html"|g' \
  resources/.print-mentor-handbook.html
pandoc for-mentors.html -s --lua-filter=$F \
  -M title="导师工作说明" -M subtitle="Mentor Handbook · Digital Learning 数字化学习" \
  -o resources/mentor-handbook.docx

# --- 5. PDFs, printed from the print copies -----------------------------------
for n in letter-to-parents letter-to-school-administrators mentor-handbook; do
  "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
    --virtual-time-budget=10000 \
    --print-to-pdf="$PWD/resources/$n.pdf" "file://$PWD/resources/.print-$n.html" 2>/dev/null
done

echo "documents rebuilt"
