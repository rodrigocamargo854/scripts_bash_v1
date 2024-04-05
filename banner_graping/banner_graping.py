import socket
import sys

def banner_grabbing(port, host):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((host, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        # Note que a indentação abaixo usa 4 espaços
        return f"Não foi possível conectar ou receber o banner: {e}"
    finally:
        s.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python banner_graping.py <host> <port>")
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    banner = banner_grabbing(port, host)
    print(banner)

