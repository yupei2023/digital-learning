-- Remove source-level title headings already represented by Pandoc's title block.
function Header(el)
  local title = pandoc.utils.stringify(el.content)
  local duplicate_titles = {
    ["致家长的一封信"] = true,
    ["A Letter to Parents"] = true,
    ["致学校管理者的一封信"] = true,
    ["A Letter to School Administrators"] = true,
    ["导师工作说明How this course is mentored"] = true,
    ["导师工作说明 How this course is mentored"] = true
  }
  if duplicate_titles[title] then return {} end
  -- Keep English translations visible without duplicating every entry in the TOC.
  if el.level >= 2 and title:match("^%s*[%d%p%s]*[A-Za-z]") then
    return pandoc.Div({pandoc.Para(el.content)}, pandoc.Attr("", {"heading-translation", "level-" .. el.level}))
  end
end

-- The screen page carries an in-page contents list and download buttons for these very
-- files. Both are navigation, and navigation is meaningless once the document is on paper.
-- Pandoc's HTML reader drops the <nav> wrapper, so the heading and its list arrive as two
-- loose sibling blocks; they have to be removed as a pair.
function Blocks(blocks)
  local out = pandoc.List({})
  local skip_list = false
  for _, b in ipairs(blocks) do
    if b.t == "Header" and b.identifier == "doc-toc-title" then
      skip_list = true
    elseif skip_list and b.t == "OrderedList" then
      skip_list = false
    else
      skip_list = false
      out:insert(b)
    end
  end
  return out
end

function Para(el)
  local txt = pandoc.utils.stringify(el.content)
  if txt:match("下载 PDF") and txt:match("编辑 Word") then return {} end
  return el
end
