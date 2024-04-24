#!/bin/bash


if [ -z "$1" ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi


while IFS= read -r subdomain; do
    host "${subdomain}.$1" | grep -v "NXDOMAIN"
done < "brute.txt"
