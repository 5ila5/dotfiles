#!/bin/sh

libinput-gestures &
swayidle -w timeout 120 "$HOME/.local/script/dpms-off" timeout 300 "betterlockscreen -l" &
