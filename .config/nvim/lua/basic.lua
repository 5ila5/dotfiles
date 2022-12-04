vim.opt.tabstop = 2 
vim.opt.ignorecase = true
vim.opt.number = true
vim.opt.spell = true
vim.opt.clipboard = 'unnamedplus'
local Plug = vim.fn['plug#']
vim.call('plug#begin', '~/.config/nvim/plugged')
  Plug 'nvim-tree/nvim-web-devicons' 
  Plug 'nvim-tree/nvim-tree.lua'
  Plug 'dracula/vim'
  Plug 'SirVer/ultisnips'
  Plug 'honza/vim-snippets'
  Plug 'preservim/nerdcommenter'
  Plug 'mhinz/vim-startify'
  Plug('neoclide/coc.nvim', {branch = 'release'})
vim.call('plug#end')


 require("nvim-tree").setup()
require("keymaps")
 if vim.fn.has("termguicolors") == 1 then
		 vim.opt.termguicolors = true
 end

 vim.cmd [[
    colorscheme dracula 
		syntax enable
]]
