#!/usr/bin/python

from scapy.all import *
import sys

conf.verb = 0 

host = sys.argv[1]  # Espera algo como "192.168.0"

for ip in range(1, 255):
    iprange = f"{host}.{ip}"  # Constrói o endereço IP completo
    pIP = IP(dst=iprange)
    pacote = pIP / ICMP()
    resp, noresp = sr(pacote, timeout=1)
    print("Hosts Ativos")
    for resposta in resp:
        print(resposta[1][IP].src)
        print(resposta[1][IP].ttl+" ttl")
        #aqui podemos capturar as informações que precisamos resgatar dos pacotes.
