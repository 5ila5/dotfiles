#!/bin/bash
if [ -f "/usr/bin/betterlockscreen" ] && [ -d "/usr/share/backgrounds/archlinux" ]; then
    /usr/bin/betterlockscreen -u /usr/share/backgrounds/archlinux &
fi

exec dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
