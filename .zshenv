#!/bin/zsh


export ZDOTDIR="$HOME/.config/zsh"

# XDG:
export XDG_DATA_HOME=${XDG_DATA_HOME:="$HOME/.local/share"}
export XDG_CACHE_HOME=${XDG_CACHE_HOME:="$HOME/.cache"}
export XDG_CONFIG_HOME=${XDG_CONFIG_HOME:="$HOME/.config"}
export XDG_MUSIC_DIR=${XDG_MUSIC_DIR:="$HOME/doc/music"}
export XDG_STATE_HOME=${XDG_STATE_HOME:="$HOME/.local/state"}



# CLeanup Home

export CARGO_HOME="$XDG_DATA_HOME"/cargo
export GNUPGHOME="$XDG_DATA_HOME"/gnupg
export GOPATH="$XDG_DATA_HOME"/go
export GRADLE_USER_HOME="$XDG_DATA_HOME"/gradle
export JUPYTER_CONFIG_DIR="$XDG_CONFIG_HOME"/jupyter
export LESSHISTFILE="$XDG_CACHE_HOME"/less/history
export _JAVA_OPTIONS=-Djava.util.prefs.userRoot="$XDG_CONFIG_HOME"/java
export PYTHONSTARTUP="${XDG_CONFIG_HOME}/python/pythonrc"
export RUSTUP_HOME="$XDG_DATA_HOME"/rustup
export STACK_ROOT="$XDG_DATA_HOME"/stack
alias wget=wget --hsts-file="$XDG_DATA_HOME/wget-hsts"
export XINITRC="$XDG_CONFIG_HOME"/X11/xinitrc
export XAUTHORITY="$XDG_RUNTIME_DIR"/Xauthority



# JAVA/ANDROID:

#export JAVA_OPTS='-XX:+IgnoreUnrecognizedVMOptions --add-modules java.se.ee'
export JAVA_HOME='/usr/lib/jvm/default-runtime'
export ANDROID_SDK_ROOT='/home/silas/Android/Sdk'
export ANDROID_HOME='/home/silas/Android/Sdk'



export XCURSOR_PATH=${XCURSOR_PATH}:~/.local/share/icons
export XKB_DEFAULT_LAYOUT=de


# SOME WAYLAND STUFF:

#export WLR_NO_HARDWARE_CURSORS=1
#export QT_AUTO_SCREEN_SCALE_FACTOR=1
#export QT_QPA_PLATFORM=wayland
#export QT_WAYLAND_DISABLE_WINDOWDECORATION=1
#export GDK_BACKEND=wayland
#export XDG_CURRENT_DESKTOP=sway
#export SDL_VIDEODRIVER=wayland
#export CLUTTER_BACKEND=wayland
#export GBM_BACKEND=nvidia-drm
#export __GLX_VENDOR_LIBRARY_NAME=nvidia
#export MOZ_ENABLE_WAYLAND=1
export WLR_NO_HARDWARE_CURSORS=1
export MOZ_USE_XINPUT2=1

export PYTHONTRACEMALLOC=1
export LIBVA_DRIVER_NAME=vdpau
export VDPAU_DRIVER=nvidia

. "$CARGO_HOME/env"
PATH="$PATH:/opt/resolve/bin:/usr/share/scala3/bin"
PATH="$PATH$(\find ~/.local/script/ -type d -printf ':%p')"

# set default editor based if installed and prioritised
for editor in nvim vim vi joe nano; do
    if command -v $editor >/dev/null; then
				export EDITOR=$editor
				break
    fi
done


export BROWSER=firefox


# texlive
export TEXMFHOME=$XDG_CONFIG_HOME/texmf
export TEXMFVAR=$XDG_CONFIG_HOME/texlive/texmf-var
export TEXMFVAR=$XDG_CONFIG_HOME/texlive/texmf-config

