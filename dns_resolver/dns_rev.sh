#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

domain=$1

for ip in $(dig +short $domain | grep -P '^\d+\.\d+\.\d+\.\d+$'); do
    host $ip
done
