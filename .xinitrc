#!/bin/sh

# Icons to Use:
export XCURSOR_PATH=${XCURSOR_PATH}:~/.local/share/icons
ERRFILE="$XDG_CACHE_HOME/X11/xsession-errors"

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ "$SHELL" = "zsh" ]; then
  [ -f "$HOME/.zshenv" ] && . "$HOME/.zshenv"
fi

if [ -f $sysresources ]; then
  xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
  xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
  xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
  xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/?*.sh; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

if [ -f ~/.config/alsa/asound.state ]; then
  alsactl restore --file .config/alsa/asound.state
fi

if [ -f ~/.screenlazout/layout.sh ]; then
  ~/.screenlazout/layout.sh
fi

export XDG_SESSION_TYPE=X11

#nvidia-settings --assign CurrentMetaMode="HDMI-0: nvidia-auto-select +0+300 {ForceCompositionPipeline=On},DP-0: nvidia-auto-select +1920+300 {ForceCompositionPipeline=On}, DVI-D-0: nvidia-auto-select +3840+0 {ForceCompositionPipeline=On,Rotation=left}"&

clipmanager &
sxhkd &
picom &
udiskie --tray &
# numlockx &
nextcloud --background &
flameshot &
#nitrogen --restore &
#xidlehook --not-when-fullscreen\
#       	--not-when-audio\
#       	--timer 300 \
#       	"export BRIGHTNESS1=\$(echo \$(xrandr --verbose |grep Brightness |grep -o '[0-9].*')| awk '{print \$2;}') && export BRIGHTNESS0=\$(echo \$(xrandr --verbose |grep Brightness |grep -o '[0-9].*')| awk '{print \$1;}')"\
#	'xrandr --output DVI-D-0 --brightness $BRIGHTNESS0 && xrandr --output DP-0 --brightness $BRIGHTNESS1'\
#	--timer 300 'systemctl suspend' '' &
if [ -d /home/silas/.config/wacom/config.sh ]; then
  bash /home/silas/.config/wacom/config.sh &
fi

glances -w --disable-webui &
exec qtile start
