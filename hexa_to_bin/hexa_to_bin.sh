#!/bin/bash




IFS=' ' read -r -a ip_parts <<< "$1"
printf "%d.%d.%d.%d\n" 0x${ip_parts[0]} 0x${ip_parts[1]} 0x${ip_parts[2]} 0x${ip_parts[3]}


