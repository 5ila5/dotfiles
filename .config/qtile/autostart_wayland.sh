#!/bin/sh

swayidle -w timeout 120 'wlopm --off "*"' resume 'wlopm --on "*"' &

kanshi &
setxkbmap de &
wl-paste -t text --watch clipman store &
#clipmanager &
#sxhkd &
# numlockx &
ydotoold &
udiskie --tray &
numlockx &
nextcloud --background &
# flameshot &
XDG_CURRENT_DESKTOP="sway dbus-run-session qtile" flameshot &


# sleep 3 
