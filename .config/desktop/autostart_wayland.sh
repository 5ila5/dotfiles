#!/bin/sh

if command -v hypridle >/dev/null && pidof Hyprland; then
  hypridle &
elif command -v swayidle >/dev/null && command -v wlopm >/dev/null; then
  swayidle -w timeout 120 'wlopm --off "*"' resume 'wlopm --on "*"' &
fi
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
kanshi &
#setxkbmap de &
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
