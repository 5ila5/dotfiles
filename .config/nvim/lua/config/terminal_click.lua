local function locate_file(filename)
  local cwd = vim.fn.getcwd()
  local full_path = cwd .. "/" .. filename
  if vim.fn.filereadable(full_path) == 1 then
    return full_path
  end

  -- Check if the file exists in the current working directory.
  if vim.fn.filereadable(filename) == 1 then
    return filename
  end

  local search_parents = { "./", "../", "../../", "../../../", "../../../../" }
  for _, prefix in ipairs(search_parents) do
    local path = prefix .. filename
    if vim.fn.filereadable(path) == 1 then
      return path
    end
  end

  -- Check file exists uniquly in subdirectories
  local files = vim.fn.glob("**/" .. filename, false, true)
  if #files == 1 then
    return files[1]
  end

  return nil
end

local function open_terminal_file()
  print("open_terminal_file called")

  local mouse = vim.fn.getmousepos()
  if mouse.winid == 0 or mouse.line == 0 then
    return
  end
  local lines = vim.api.nvim_buf_get_lines(0, mouse.line - 1, mouse.line, false)
  local line = lines[1]

  local col = mouse.column - 1

  local WORD_PATTERN = "[%w%._%-%/\\:~]"
  local PATH_PATTERN = "[%w%._%-%/\\~]"

  local word_start = col
  while word_start > 0 and line:sub(word_start, word_start):match(WORD_PATTERN) do
    word_start = word_start - 1
  end

  local word_end = col
  while word_end <= #line and line:sub(word_end, word_end):match(WORD_PATTERN) do
    word_end = word_end + 1
  end

  local word = line:sub(word_start + 1, word_end - 1)
  print("word under cursor =", word)

  local file, lnum, cnum = word:match("(" .. PATH_PATTERN .. "+):?(%d*):?(%d*)")
  print("found file1 =", file, "lnum =", lnum, "cnum =", cnum)

  if not file then
    print("No file found under cursor")
    return
  end

  local actual_file = locate_file(file)
  print("actual_file =", actual_file)
  if not actual_file then
    print("File not found: " .. file)
    return
  end

  vim.cmd("wincmd p")

  vim.cmd("edit " .. vim.fn.fnameescape(file))

  local set_line = mouse.line
  local set_col = mouse.column - 1

  if lnum ~= "" then
    local last_line = vim.api.nvim_buf_line_count(0)
    local lnum_num = tonumber(lnum)
    if lnum_num then
      set_line = math.min(math.floor(lnum_num), last_line)
    end
  end

  if cnum ~= "" then
    local last_col = vim.api.nvim_buf_get_lines(0, set_line - 1, set_line, false)[1]:len()
    local cnum_num = tonumber(cnum)
    if cnum_num then
      set_col = math.min(math.floor(cnum_num) - 1, last_col)
    end
  end

  vim.api.nvim_win_set_cursor(0, {
    set_line,
    set_col,
  })
end

vim.api.nvim_create_autocmd("TermOpen", {
  callback = function()
    print("termOpen")
    vim.keymap.set("n", "<C-LeftMouse>", open_terminal_file, { buffer = true, silent = true })
  end,
})
