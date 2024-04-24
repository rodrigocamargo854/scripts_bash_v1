import socket
import sys
from colorama import Fore, Style

def find_refer_value(response):
    lines = response.split('\n')
    for line in lines:
        if line.startswith('refer:'):
            _, value = line.split(':', 1)  # Dividir apenas no primeiro ':'
            return value.strip()  # Remove espaços extras e retorna o valor

if len(sys.argv) < 3 or not sys.argv[1] or not sys.argv[2]:
    print("uso: whois <host> <query>")
    sys.exit(1)

else:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((sys.argv[2], 43))
        s.sendall((sys.argv[1] + "\r\n").encode())

        response = b""
        while True:
            part = s.recv(1024)
            if not part:
                break
            response += part

        #decoded_response = response.decode('utf-8')
        decoded_response = response.decode('ISO-8859-1')
        
        refer_value = find_refer_value(decoded_response)
        if refer_value:
            print(f"{Fore.GREEN}Here is the Refer => {Fore.YELLOW}{refer_value}{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Here is the information about:{Style.RESET_ALL}\n{decoded_response}")

    except Exception as e:
        print(f"um erro ocorreu: {e}")
    finally:
        s.close()
