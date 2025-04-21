#!/bin/bash

if [[ -z $WAYLAND_DISPLAY ]]; then
  dmenu_run
else
  if command -v bemenu-run &>/dev/null; then
    bemenu-run
  else
    dmenu_run
  fi
fi
