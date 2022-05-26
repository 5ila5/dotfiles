#!/bin/bash

if [ -f "/usr/bin/betterlockscreen" ] && [ -d "/usr/share/backgrounds/archlinux" ]; then
	/usr/bin/betterlockscreen -u /usr/share/backgrounds/archlinux &
fi
