#!/usr/bin/python

import socket

# Função para criar um novo socket
def create_socket(timeout=10):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.settimeout(timeout)
    return tcp

# Faixa de IPs a verificar
ip_range = range(1, 255)

for ip in ip_range:
    tcp = create_socket()
    try:
        ip_address = f"172.16.1.{ip}"
        tcp.connect((ip_address, 21))
        banner = tcp.recv(1024)
        print(f"Banner from {ip_address}:", banner)

        tcp.send(b"USER ftp\r\n")
        user = tcp.recv(1024)
        print(f"USER response from {ip_address}:", user)

        tcp.send(b"PASS ftp\r\n")
        pw = tcp.recv(1024)
        print(f"PASS response from {ip_address}:", pw)

        tcp.send(b"HELP\r\n")
        cmd = tcp.recv(2408)
        print(f"HELP response from {ip_address}:", cmd)

    except socket.timeout:
        print(f"Timeout or no FTP server at {ip_address}")
    except socket.error as e:
        print(f"Socket error {e} at {ip_address}")
    finally:
        tcp.close()




