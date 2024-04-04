#!/bin/bash


limit=0


if [ "$1" = "" ]; then
    echo -e "\e[1;35m==================================\e[0m" 
    echo -e "\e[1;32mModo de usar: $0 <arquivo.pcap>\e[0m"
    echo "Exemplo: $0 exemplo.pcap"
    exit 1
fi

if ! command -v tcpdump &> /dev/null; then
    echo "tcpdump não está instalado, tentando instalar..."
    # Tenta instalar o tcpdump
    sudo apt-get update && sudo apt-get install -y tcpdump
else
    echo -e "\e[1;35m========================================\e[0m" 
    echo -e "\e[1;32m[+] Analisando o arquivo: $1\e[0m"
    echo -e "\e[1;35m=========================================\e[0m"

    # awk pega as colunas necessárias, sed aplica regex para remover porta

    #sudo tcpdump -nvr "$1" 'tcp' | grep '\[S\]' | awk '{split($3, a, "."); print a[1]"."a[2]"."a[3]"."a[4]}' | sed 's/\.[0-9]*$//' | sort | uniq -c | sort -nr |
    #sudo tcpdump -nvr "$1" 'tcp' | grep '\[S\]' | wc -l |
    #sudo tcpdump -nvr "$1" 'tcp' | grep '\[S\]' | head -n 1 

    IP_SERVIDOR=$(sudo tcpdump -nvr "$1" 'tcp' | grep '\[S\]' | awk '{split($3, a, "."); print a[1]"."a[2]"."a[3]"."a[4]}' | head -n 1)
    OPEN_PORT=$(sudo tcpdump -nvr "$1" 'tcp' | grep '\[S.\]' | awk -F, '{print $1}')
    sudo tcpdump -nvr "$1" 'tcp' | grep '\[S\]' | awk '{gsub(/:$/, "", $3); print $1, $3}' | sort | uniq -c | sort -nr |
   
     while read COUNT IP_SOURCE IP_DESTINO; do
        if [ "$COUNT" -ge "$limit" ]; then
	        echo "Possível comportamento de malware detectado: $COUNT numero de conexoes suspeitas de $IP_SOURCE a $IP_DESTINO."
        fi
    done
   
    SUBDOMINIO=$(nslookup $IP_SERVIDOR | awk '/name =/ {print $4}' | sed 's/\.$//')
    echo "Subdomínio do servidor: $SUBDOMINIO"
    
    echo -e "\e[1;35mEventos de porta aberta:\e[0m"
    echo "$OPEN_PORT" | while read line; do
    echo -e "\e[1;35m$line\e[0m"
    done


    #IP_ADDRESS=$IP_SERVIDOR
    #API_KEY="apikey"
    #virustotal api
    #RESPONSE=$(curl --request GET \
    #--url "https://www.virustotal.com/api/v3/ip_addresses/${IP_ADDRESS}" \
    #--header "x-apikey: ${API_KEY}"
    # echo "$RESPONSE" | jq -r '.data '

    IP_ADDRESS=$IP_SERVIDOR
    API_KEY=""

    # Solicitação da API do VirusTotal usando wget
    #wget --header "x-apikey: ${API_KEY}" "https://www.virustotal.com/api/v3/ip_addresses/${IP_ADDRESS}" -O response.json
    # Mostrando a resposta com jq

    curl --request GET \
     --url "https://www.virustotal.com/api/v3/ip_addresses/${IP_ADDRESS}/resolutions" \
     --header "x-apikey: ${API_KEY}" \
     -o response.json

     echo jq -r '.data' response.json
     
     echo -e "\e[1;35m========================================\e[0m" 
     echo -e "\e[1;32m[+] Resolvendo hostnames $1\e[0m"
     echo -e "\e[1;35m=========================================\e[0m"

     cat response.json | grep "host_name"


fi

