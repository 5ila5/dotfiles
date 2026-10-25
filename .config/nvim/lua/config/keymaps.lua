-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

local map = vim.keymap.set
local opts = { noremap = true, silent = true }

local function smart_resize(direction, amount)
  local is_far_right = vim.fn.winnr("l") == vim.fn.winnr()
  local is_far_bottom = vim.fn.winnr("j") == vim.fn.winnr()

  if direction == "h" then
    -- Move border left (Shrink if left window, Grow if right window)
    local op = is_far_right and "+" or "-"
    vim.cmd("vertical resize " .. op .. amount)
  elseif direction == "l" then
    -- Move border right (Grow if left window, Shrink if right window)
    local op = is_far_right and "-" or "+"
    vim.cmd("vertical resize " .. op .. amount)
  elseif direction == "k" then
    -- Move border up (Shrink if top window, Grow if bottom window)
    local op = is_far_bottom and "+" or "-"
    vim.cmd("resize " .. op .. amount)
  elseif direction == "j" then
    -- Move border down (Grow if top window, Shrink if bottom window)
    local op = is_far_bottom and "-" or "+"
    vim.cmd("resize " .. op .. amount)
  end
end

-- Move windows (Ctrl + Alt + H/J/K/L) using WinShift plugin
map("n", "<C-A-h>", "<cmd>WinShift left<cr>", vim.tbl_extend("force", opts, { desc = "Move window to far left" }))
map("n", "<C-A-j>", "<cmd>WinShift down<cr>", vim.tbl_extend("force", opts, { desc = "Move window to bottom" }))
map("n", "<C-A-k>", "<cmd>WinShift up<cr>", vim.tbl_extend("force", opts, { desc = "Move window to top" }))
map("n", "<C-A-l>", "<cmd>WinShift right<cr>", vim.tbl_extend("force", opts, { desc = "Move window to far right" }))

-- Resize windows (Ctrl + Shift + H/J/K/L)
map("n", "<C-S-h>", function()
  smart_resize("h", 5)
end, vim.tbl_extend("force", opts, { desc = "Decrease window width" }))
map("n", "<C-S-l>", function()
  smart_resize("l", 5)
end, vim.tbl_extend("force", opts, { desc = "Increase window width" }))
map("n", "<C-S-k>", function()
  smart_resize("k", 5)
end, vim.tbl_extend("force", opts, { desc = "Decrease window height" }))
map("n", "<C-S-j>", function()
  smart_resize("j", 5)
end, vim.tbl_extend("force", opts, { desc = "Increase window height" }))

vim.keymap.set("t", "<Esc><Esc>", "<C-\\><C-n>", { desc = "Exit terminal mode" })
