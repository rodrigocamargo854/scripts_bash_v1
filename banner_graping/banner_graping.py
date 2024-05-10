import socket
import sys
import os

def check_connectivity(host, port):
    response = os.system(f"ping -c 1 {host}")
    if response == 0:
        print(f"{host} is up.")
        os.system(f"nmap -p {port} {host}")
    else:
        print(f"{host} is down or not reachable.")

def banner_grabbing(host, port):
    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect((host, port))
        banner = s.recv(2048)
        s.close()
        return banner
    except Exception as e:
        return f"Não foi possível conectar ou receber o banner de {host}:{port}: {e}"

def process_hosts_ports(hosts_ports_str):
    hosts_ports = hosts_ports_str.split(',')
    banners = []
    for host_port in hosts_ports:
        host, port = host_port.strip().split(':')
        check_connectivity(host, port)
        banner = banner_grabbing(host, int(port))
        banners.append((host, port, banner))
    return banners

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python banner_grabbing.py 'host1:porta1,host2:porta2,...'")
        sys.exit(1)
    hosts_ports_str = sys.argv[1]
    banners = process_hosts_ports(hosts_ports_str)
    for host, port, banner in banners:
        print(f"Banner para {host}:{port}: {banner.decode('utf-8', 'ignore') if isinstance(banner, bytes) else banner}")
