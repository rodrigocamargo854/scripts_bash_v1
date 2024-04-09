import socket
import sys

# Verifica se os argumentos foram passados
if len(sys.argv) < 3:
    print("Uso: python script.py target_host target_port")
    sys.exit(1)

target_host = sys.argv[1]
target_port = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect((target_host, target_port))


client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")


response = client.recv(4096)

print(response.decode())
