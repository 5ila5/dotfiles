#!/bin/sh

# if hyprpolkitagent systemd user agent exists, use it
if [ -x /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 ]; then
  /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
elif systemctl --user list-unit-files | grep -q hyprpolkitagent.service; then
  if ! systemctl --user is-active hyprpolkitagent.service; then
    systemctl --user start hyprpolkitagent.service
  fi
else
  notify-send "No polkit agent found" "Please install either polkit-gnome or hyprpolkitagent."
fi

#clipmanager &
#sxhkd &
#numlockx &
nm-applet &

if command -v qpwgraph >/dev/null; then
  qpwgraph -m &
fi

HOSTNAME_UPPER=$(hostname | tr 'abcdefghijklmnopqrstuvwxyz' 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

if echo "$HOSTNAME_UPPER" | grep -q "LAPTOP"; then
  if [ -x "$HOME/.config/desktop/autostart_laptop.sh" ]; then
    "$HOME/.config/desktop/autostart_laptop.sh"
  fi
fi
