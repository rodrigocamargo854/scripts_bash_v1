import socket
import sys

if len(sys.argv) < 3 or not sys.argv[1] or not sys.argv[2]:
    print("uso: whois <host> <query>")
    sys.exit(1)

else:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((sys.argv[2], 43))  
        s.sendall((sys.argv[1] + "\r\n").encode())  

        response = s.recv(1024)
        try:
            
            print(response.decode('utf-8'))
        except UnicodeDecodeError:
            
            print(response.decode('iso-8859-1'))  

    except Exception as e:
        print(f"um erro ocorreu: {e}")
    finally:
        s.close()  
