#!/bin/bash
sleep 2
padId=$(xsetwacom list | grep PAD | awk -F 'id: ' '{print $2}' | awk -F ' ' '{print $1}')
stylusId=$(xsetwacom list | grep STYLUS | awk -F 'id: ' '{print $2}' | awk -F ' ' '{print $1}')

echo "found padId=$padId and stylusID=$stylusId"

xsetwacom set $padId Button 1 5 
xsetwacom set $padId Button 2 21
xsetwacom set $padId Button 3 4
#xsetwacom set $padId Button 4 23

xsetwacom set $stylusId MapToOutput HEAD-0
