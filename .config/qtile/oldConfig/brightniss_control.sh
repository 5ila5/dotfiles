var=$2
out=""
if [ $1 -eq 1 ]; then
	out="HDMI-0"
fi
if [ $1 -eq 0 ]; then
	out="DVI-D-0"
fi
if [ $1 -eq 2 ]; then
	out="DP-0"
fi
if [ "$out" = "" ];then
	exit
fi

if (($(echo "$2>1" |bc -l) )); then

	if (($(echo "$2<10" |bc -l) )); then

		var=$(bc  <<< "scale=2;$var*10")
        fi
        var=$(bc  <<< "scale=2;$var/100")
fi

xrandr --output $out --brightness $var



