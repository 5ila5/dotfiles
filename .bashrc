#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

[[ $- == *i* ]] &&
  source "/usr/share/blesh/ble.sh" --rcfile "$HOME/.blerc"


alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
if [ -f ~/.bash_aliases ]; then
. ~/.bash_aliases
fi

#export JAVA_OPTS='-XX:+IgnoreUnrecognizedVMOptions --add-modules java.se.ee'
export JAVA_HOME='/usr/lib/jvm/default-runtime'
export ANDROID_SDK_ROOT='/home/silas/Android/Sdk'
export ANDROID_HOME='/home/silas/Android/Sdk'
export XCURSOR_PATH=${XCURSOR_PATH}:~/.local/share/icons

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



. "$HOME/.cargo/env"
PATH="$PATH:/opt/resolve/bin"

bind "TAB:menu-complete"
bind '"\e[Z": menu-complete-backward'
bind "set menu-complete-display-prefix on"
bind "set show-all-if-ambiguous on"
bind "set completion-ignore-case on"
export PYTHONTRACEMALLOC=1
export LIBVA_DRIVER_NAME=vdpau
export VDPAU_DRIVER=nvidia

eval "$(starship init bash)"
eval "$(thefuck --alias)"

neofetch
