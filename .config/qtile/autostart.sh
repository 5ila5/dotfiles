#!/bin/sh
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#clipmanager &
#sxhkd &
#numlockx &
nm-applet &

if command -v qpwgraph >/dev/null; then
				qpwgraph -m &
fi
