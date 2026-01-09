#!/bin/sh

json="$(klog json)"

start_time="$(
  printf '%s\n' "$json" |
    jq -r '
    .records
    | .[]
    | .entries[]
    | select(.type == "open_range")
    | .start
    ' | head -n1
)"

[ -z "$start_time" ] && exit 1
today="$(date +%Y-%m-%d)"

start_epoch="$(date -d "$today $start_time" +%s)"
now_epoch="$(date +%s)"

# if start time is in the future, assume it was yesterday
if [ "$start_epoch" -gt "$now_epoch" ]; then
  start_epoch="$(date -d "yesterday $start_time" +%s)"
fi

elapsed=$((now_epoch - start_epoch))

hours=$((elapsed / 3600))
minutes=$(((elapsed % 3600) / 60))

printf '%02d:%02d\n' "$hours" "$minutes"
