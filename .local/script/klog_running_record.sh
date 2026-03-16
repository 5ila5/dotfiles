#!/bin/sh

klog bookmarks list | awk -F' -> ' '{print $2}' | sort -u | while read -r path; do
  elapsed_mins=$(klog json "$path" --today -n | jq -r '[.records[].entries[] | .total_mins] | add')
  has_open_range=$(klog json "$path" | jq -r '[.records[].entries[] | select(.type=="open_range")] | length')

  ([ -z "$elapsed_mins" ] || [ "$elapsed_mins" = "null" ] || [ "$has_open_range" = "0" ]) && continue

  hours=$((elapsed_mins / 60))
  minutes=$((elapsed_mins % 60))
  printf -v elapsed -- '%02d:%02d' "$hours" "$minutes"

  name=$(basename "$path" ".klg")

  printf '%s(%s) ' "$elapsed" "$(expr "$name" : '\(.\)')"
done
