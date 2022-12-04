"call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')
"  Plug 'nvim-tree/nvim-web-devicons' 
"  Plug 'nvim-tree/nvim-tree.lua'
"  Plug 'dracula/vim'
"  Plug 'SirVer/ultisnips'
"  Plug 'honza/vim-snippets'
"  Plug 'preservim/nerdcommenter'
"  Plug 'mhinz/vim-startify'
"  Plug 'neoclide/coc.nvim', {'branch': 'release'}
"call plug#end()


lua require('basic')
set splitright
set splitbelow



" move line or visually selected block - alt+j/k
inoremap <A-j> <Esc>:m .+1<CR>==gi
inoremap <A-k> <Esc>:m .-2<CR>==gi
vnoremap <A-j> :m '>+1<CR>gv=gv
vnoremap <A-k> :m '<-2<CR>gv=gv " move split panes to left/bottom/top/right
 nnoremap <A-h> <C-W>H
 nnoremap <A-j> <C-W>J
 nnoremap <A-k> <C-W>K
 nnoremap <A-l> <C-W>L" move between panes to left/bottom/top/right
 nnoremap <C-h> <C-w>h
 nnoremap <C-j> <C-w>j
 nnoremap <C-k> <C-w>k
 nnoremap <C-l> <C-w>l
 

"nnoremap <A-g> :NvimTreeToggle<cr>

" Press i to enter insert mode, and ii to exit insert mode.
:inoremap ii <Esc>
:inoremap jk <Esc>
:inoremap kj <Esc>
:vnoremap jk <Esc>
:vnoremap kj <Esc>


if has("autocmd")
  au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$")
    \| exe "normal! g'\"" | endif
endif
