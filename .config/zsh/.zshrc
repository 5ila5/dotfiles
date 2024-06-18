#!/bin/zsh

autoload -Uz compinit
compinit
autoload bashcompinit
bashcompinit

compinit -d "$XDG_CACHE_HOME"/zsh/zcompdump-"$ZSH_VERSION"
#source ./aliases
#source ./functions


for file in $ZDOTDIR/zsh-aliases* $ZDOTDIR/zsh-functions*; do
    source "$file"
done

# Lines configured by zsh-newuser-install
HISTFILE=$ZDOTDIR/zsh-history
HISTSIZE=9999999999
SAVEHIST=9999999999
setopt autocd beep extendedglob nomatch notify
setopt HIST_IGNORE_ALL_DUPS 
setopt INC_APPEND_HISTORY
setopt HIST_IGNORE_SPACE
setopt EXTENDED_HISTORY
setopt HIST_FIND_NO_DUPS
setopt NO_CASE_GLOB
setopt INTERACTIVE_COMMENTS 
setopt HIST_REDUCE_BLANKS 
setopt SHARE_HISTORY
setopt menu_complete
bindkey -v
# End of lines configured by zsh-newuser-install

# The following lines were added by compinstall

zstyle ':completion:*' completer _expand _complete _ignored _correct _approximate _files
zstyle ':completion:*' matcher-list '' 'm:{[:lower:]}={[:upper:]}' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'l:|=* r:|=*'

# partiial completion
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

# case insesitive completion
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}'
zstyle ':completion:*' remote-access yes

zstyle :compinstall filename '/home/silas/.zshrc'
setopt globdots

source $ZDOTDIR/python-argcomplete 

# End of lines added by compinstall
#
# promt ZSH
autoload -Uz promptinit
zstyle ':completion:*' menu select
zstyle ':completion::complete:*' gain-privileges 1
promptinit
zsh_add_plugin "zsh-users/zsh-autosuggestions"
zsh_add_plugin "zsh-users/zsh-syntax-highlighting"

bindkey "^k" clear-screen
bindkey "^J" autosuggest-execute
bindkey "^F" autosuggest-accept
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

bindkey "^H" backward-word
bindkey  "^[[H" beginning-of-line
bindkey "^L" forward-word
bindkey  "^[[F"   end-of-line
bindkey "^[[3;5~" kill-word
bindkey "^[d" kill-word
bindkey "^[[3~" delete-char
bindkey "^^?" backward-kill-word 

if [ -f ~/.config/nnn/bash_vars.sh ]; then
. ~/.config/nnn/bash_vars.sh
fi

#bind "TAB:menu-complete"
#bind '"\e[Z": menu-complete-backward'
#bind "set menu-complete-display-prefix on"
#bind "set show-all-if-ambiguous on"
#bind "set completion-ignore-case on"
if command -v thefuck > /dev/null; then 
eval "$(thefuck --alias)"
fi
# acitvades auto correction for cd
#shopt -s cdspell
#shopt -s dirspell


if command -v fastfetch > /dev/null; then
				fastfetch
elif command -v neofetch > /dev/null; then 
				neofetch
fi
#starship
if command -v starship > /dev/null; then
				eval "$(starship init zsh)" 
fi

if [[ -f "/usr/share/fzf/key-bindings.zsh" ]]; then 
source "/usr/share/fzf/key-bindings.zsh"
fi


if command -v zoxide > /dev/null
then
				eval "$(zoxide init zsh --cmd cd)"
fi


