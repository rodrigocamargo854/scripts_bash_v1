portas=(80 443)

# Loop para bloquear cada porta especificada no array
for porta in "${portas[@]}"; do
    iptables -A INPUT -p tcp --dport $porta -j DROP
    echo "Porta $porta bloqueada para tráfego de entrada."
done
