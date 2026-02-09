#!/bin/sh

if command -v doas >/dev/null; then
  doas cp config.conf /etc/keyd/default.conf
  doas systemctl restart keyd
else
  sudo cp config.conf /etc/keyd/default.conf
  sudo systemctl restart keyd
fi
