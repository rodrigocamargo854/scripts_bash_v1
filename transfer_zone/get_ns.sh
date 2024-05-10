#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi


SERVERS=$(host -t ns $1 | cut -d " " -f4)

for server in  $SERVERS; do
host -l -a $1 $server

done
