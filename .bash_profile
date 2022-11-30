#!/bin/bash
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc
export PATH=$PATH:$HOME/.local/bin
. "$HOME/.cargo/env"

