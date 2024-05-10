#!/bin/bash

TARGET=$1
LIST=$2

for ip in $(cat $LIST); do
  
    http_code=$(curl -s -H "User-Agent: DesecTool" -o /dev/null -w "%{http_code}" "http://$TARGET/$ip/") 
    
    if [ "$http_code" == "200" ]; then
        echo "Código 200 encontrado: $ip"
    fi
done
