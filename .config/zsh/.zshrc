#!/bin/zsh

#source ./aliases
#source ./functions

source "$ZDOTDIR/zsh-aliases"
source "$ZDOTDIR/zsh-functions"

# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=99999999
SAVEHIST=999999999
setopt autocd beep extendedglob nomatch notify
bindkey -v
# End of lines configured by zsh-newuser-install

# The following lines were added by compinstall

zstyle ':completion:*' completer _expand _complete _ignored _correct _approximate _files
zstyle ':completion:*' matcher-list '' 'm:{[:lower:]}={[:upper:]}' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'l:|=* r:|=*'
zstyle :compinstall filename '/home/silas/.zshrc'
setopt globdots
autoload -Uz compinit
compinit

# End of lines added by compinstall
#
# promt ZSH
autoload -Uz promptinit
zstyle ':completion:*' menu select
zstyle ':completion::complete:*' gain-privileges 1
promptinit
zsh_add_plugin "zsh-users/zsh-autosuggestions"
zsh_add_plugin "zsh-users/zsh-syntax-highlighting"


bindkey "^J" autosuggest-execute
bindkey "^F" autosuggest-accept
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

bindkey "^H" backward-word
bindkey "^L" forward-word
bindkey "^[[3;5~" kill-word
bindkey "\e[3~" delete-char
bindkey "^^?" backward-kill-word 

#plugins=(
#  git
#  bundler
#  dotenv
#  macos
#  rake
#  rbenv
#  ruby
#)
#export JAVA_OPTS='-XX:+IgnoreUnrecognizedVMOptions --add-modules java.se.ee'
export JAVA_HOME='/usr/lib/jvm/default-runtime'
export ANDROID_SDK_ROOT='/home/silas/Android/Sdk'
export ANDROID_HOME='/home/silas/Android/Sdk'
export XCURSOR_PATH=${XCURSOR_PATH}:~/.local/share/icons
export EDITOR='nvim'
#export WLR_NO_HARDWARE_CURSORS=1
export XKB_DEFAULT_LAYOUT=de
#export QT_AUTO_SCREEN_SCALE_FACTOR=1
#export QT_QPA_PLATFORM=wayland
#export QT_WAYLAND_DISABLE_WINDOWDECORATION=1
#export GDK_BACKEND=wayland
#export XDG_CURRENT_DESKTOP=sway
#export SDL_VIDEODRIVER=wayland
#export CLUTTER_BACKEND=wayland
#export GBM_BACKEND=nvidia-drm
#export __GLX_VENDOR_LIBRARY_NAME=nvidia
export MOZ_ENABLE_WAYLAND=1
export WLR_NO_HARDWARE_CURSORS=1

if [ -f ~/.config/nnn/bash_vars.sh ]; then
. ~/.config/nnn/bash_vars.sh
fi

. "$HOME/.cargo/env"
PATH="$PATH:/opt/resolve/bin"
PATH="$PATH$(\find ~/.local/script/ -type d -printf ':%p')"



#bind "TAB:menu-complete"
#bind '"\e[Z": menu-complete-backward'
#bind "set menu-complete-display-prefix on"
#bind "set show-all-if-ambiguous on"
#bind "set completion-ignore-case on"
export PYTHONTRACEMALLOC=1
export LIBVA_DRIVER_NAME=vdpau
export VDPAU_DRIVER=nvidia

eval "$(thefuck --alias)"
# acitvades auto correction for cd
#shopt -s cdspell
#shopt -s dirspell

neofetch 
#starship
eval "$(starship init zsh)" 
source "/usr/share/fzf/key-bindings.zsh"
