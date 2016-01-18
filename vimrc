filetype plugin on
execute pathogen#infect()
syntax on
set tabstop=2
set shiftwidth=2
set expandtab
set smartindent
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:instant_markdown_autostart = 0
let g:vim_arduino_auto_open_serial = 1

set nu
