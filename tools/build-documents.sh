#!/bin/sh
# Rebuild the three community documents (HTML + DOCX + PDF) in resources/.
#
# Sources of truth
#   tools/documents/letter-to-parents.md                 -> resources/letter-to-parents.{html,docx}
#                                                           resources/letter-to-parents-editable.docx
#   tools/documents/letter-to-school-administrators.md   -> resources/letter-to-school-administrators.{html,docx}
#   for-mentors.html  (the site page itself)             -> resources/mentor-handbook.{html,docx}
#
# PDFs are printed from the generated HTML by headless Chrome (A4 comes from
# @page in assets/community-doc.css). Run from the course-site directory.
#
# Requires: pandoc, Google Chrome.

set -e
cd "$(dirname "$0")/.."

F=tools/document-print-filter.lua
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FOOT='Digital Learning 数字化学习 · 公开课程 A public course · 段玉佩 Yupei Duan'
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

footer () { printf '<footer class="site">%s · %s</footer>\n' "$FOOT" "$1" > "$TMP/foot.html"; }

# --- 1. Letter to Parents -----------------------------------------------------
footer '致家长的一封信 A Letter to Parents'
pandoc tools/documents/letter-to-parents.md -s --toc --toc-depth=3 \
  --lua-filter=$F --include-after-body="$TMP/foot.html" \
  -c ../assets/community-doc.css -o resources/letter-to-parents.html
pandoc tools/documents/letter-to-parents.md -s --lua-filter=$F \
  -o resources/letter-to-parents-editable.docx
pandoc tools/documents/letter-to-parents.md -s -o resources/letter-to-parents.docx

# --- 2. Letter to School Administrators ---------------------------------------
footer '致学校管理者的一封信 A Letter to School Administrators'
pandoc tools/documents/letter-to-school-administrators.md -s --toc --toc-depth=3 \
  --lua-filter=$F --include-after-body="$TMP/foot.html" \
  -c ../assets/community-doc.css -o resources/letter-to-school-administrators.html
pandoc tools/documents/letter-to-school-administrators.md -s --lua-filter=$F \
  -o resources/letter-to-school-administrators.docx

# --- 3. Mentor handbook (rendered from the site page) -------------------------
footer '导师工作说明 How this course is mentored'
pandoc for-mentors.html -s --lua-filter=$F --include-after-body="$TMP/foot.html" \
  -M title="导师工作说明" -M subtitle="Mentor Handbook · Digital Learning 数字化学习" \
  -c ../assets/community-doc.css -o resources/mentor-handbook.html
# for-mentors.html lives at the site root; its relative links need one level up here.
/usr/bin/sed -i '' \
  -e 's|href="s1/|href="../s1/|g' \
  -e 's|href="calendar.html"|href="../calendar.html"|g' \
  -e 's|href="index.html"|href="../index.html"|g' \
  resources/mentor-handbook.html
pandoc for-mentors.html -s --lua-filter=$F \
  -M title="导师工作说明" -M subtitle="Mentor Handbook · Digital Learning 数字化学习" \
  -o resources/mentor-handbook.docx

# --- 4. PDFs ------------------------------------------------------------------
for n in letter-to-parents letter-to-school-administrators mentor-handbook; do
  "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
    --virtual-time-budget=10000 \
    --print-to-pdf="$PWD/resources/$n.pdf" "file://$PWD/resources/$n.html" 2>/dev/null
done

echo "documents rebuilt"
