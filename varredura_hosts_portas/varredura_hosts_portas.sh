#!/bin/bash
if [ "$1"  = "" ];
then
    echo "DESEC SECURITY - PING SWEEP"
    echo "modo de usar :$0"
    echo "Exemplo: $0 192.18.0"

else
for host in {1..254};do
    for port in {13,37,30000,3000,1337};do
       if hping3 -S -p $port -c 1 $1.$host 2> /dev/null | grep -q 'flags=SA'; then
            echo "Host $1.$host tem as portas $port aberta"
        fi
    done
done
fi
