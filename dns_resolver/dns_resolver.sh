#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

while IFS= read -r subdomain; do
    
    if [[ "$subdomain" =~ ^([a-zA-Z0-9][-a-zA-Z0-9]*[a-zA-Z0-9]?)$ ]]; then
        host "${subdomain}.$1" | grep -v "NXDOMAIN"
    fi
done < "brute.txt"

