#!/bin/sh
kanshi &
setxkbmap de &
wl-paste -t text --watch clipman store &
#clipmanager &
#sxhkd &
#numlockx &
ydotoold &

#export WLR_NO_HARDWARE_CURSORS=1
export XKB_DEFAULT_LAYOUT=de
#export QT_AUTO_SCREEN_SCALE_FACTOR=1
export QT_QPA_PLATFORM=wayland
#export QT_WAYLAND_DISABLE_WINDOWDECORATION=1
#export GDK_BACKEND=wayland
#export XDG_CURRENT_DESKTOP=sway
export SDL_VIDEODRIVER=wayland
export CLUTTER_BACKEND=wayland
#export GBM_BACKEND=nvidia-drm
#export __GLX_VENDOR_LIBRARY_NAME=nvidia
export MOZ_ENABLE_WAYLAND=1
export WLR_NO_HARDWARE_CURSORS=1
export XDG_SESSION_TYPE=wayland

# sleep 3 
