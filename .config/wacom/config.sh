#!/bin/bash
sleep 2
padId=$(xsetwacom --list devices | rg pad |  tr -dc '0-9')
stylusId=$(xsetwacom --list devices | rg stylus |  tr -dc '0-9')




xsetwacom set $padId Button 1 5 
xsetwacom set $padId Button 2 21
xsetwacom set $padId Button 3 4
#xsetwacom set $padId Button 4 23

xsetwacom set $stylusId MapToOutput HEAD-0
