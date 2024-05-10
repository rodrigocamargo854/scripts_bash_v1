#!/usr/bin/python

import sys
from scapy.all import *


conf.verb=0

portas=[21,22,23,25,80,443,110]

pIP=IP(dst=sys.argv[1])
pTCP=TCP(dport=portas,flags="S")
pacote=pIP/pTCP
resp,noresp=sr(pacote)

for resposta in resp:
        port = resposta[1][TCP].sport
	flag = respsota[1][TCP].flags
	print(f"{porta} , {flag}" %(porta,flag))

#print(resp[0][1].show())
#print(resp.show())
#print(resp[0][1][TCP].flags)
