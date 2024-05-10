from scapy.all import sr1, IP, UDP, DNS, DNSQR
import sys


if len(sys.argv) != 2:
    print("Usage: python3 scapy_dns_query.py <target-ip>")
    sys.exit(1)


target_ip = sys.argv[1]

query = IP(dst=target_ip)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="version.bind", qtype="TXT", qclass="CH"))

response = sr1(query, timeout=2)

if response:
    response.show()
else:
    print("No response received")
