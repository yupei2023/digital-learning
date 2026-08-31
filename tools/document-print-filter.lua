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
