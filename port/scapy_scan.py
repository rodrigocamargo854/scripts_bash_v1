


#!/usr/bin/python

import sys
from scapy.all import *


if len(sys.argv) < 3:
    print("Usage: {} <target_IP> <port1> <port2> ... <portN>".format(sys.argv[0]))
    sys.exit(1)

target_ip = sys.argv[1]
ports = map(int, sys.argv[2:])  


pIP = IP(dst=target_ip)

for port in ports:
    pTCP = TCP(dport=port, flags="S")
    packet = pIP / pTCP
    res, nores = sr(packet, timeout=1) 
    res.show()
    
   

