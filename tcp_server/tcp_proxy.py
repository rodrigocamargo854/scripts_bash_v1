
import socket
import threading
import time

def handle_client(client_socket, remote_host, remote_port):
    remote_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_sock.connect((remote_host, remote_port))


    client_to_remote = threading.Thread(target=forward, args=(client_socket, remote_sock, "client to remote"))
    client_to_remote.start()

   
    remote_to_client = threading.Thread(target=forward, args=(remote_sock, client_socket, "remote to client"))
    remote_to_client.start()

def forward(source, destination, direction):
    start_time = time.time()
    total_data_len = 0
    while True:
        data = source.recv(4096)
        if len(data) == 0:
            break
        total_data_len += len(data)
        process_data(data, direction, start_time, time.time(), total_data_len)
        destination.send(data)
    print(f"Total data {direction}: {total_data_len} bytes, Time taken: {time.time() - start_time} seconds")
    source.close()
    destination.close()

def process_data(data, direction, start_time, end_time, total_data_len):
   
    print(f"Data {direction}: {len(data)} bytes")
    
   
    if b"informacao_sensivel" in data:
        print(f"Alerta! Informação sensível encontrada na direção {direction}")

   

def server_loop(local_host, local_port, remote_host, remote_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((local_host, local_port))
    server.listen(5)
    while True:
        client_socket, addr = server.accept()
        print(f"[*] Recebida conexão de entrada de {addr[0]}:{addr[1]}")
        proxy_thread = threading.Thread(target=handle_client, args=(client_socket, remote_host, remote_port))
        proxy_thread.start()

def main():
    if len(sys.argv[1:]) != 5:
        print("Usage: ./proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]")
        print("Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True")
        sys.exit(0)

    local_host = sys.argv[1]
    local_port = int(sys.argv[2])

    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])

    receive_first = sys.argv[5]

    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False

    server_loop(local_host, local_port, remote_host, remote_port)

if __name__ == "__main__":
    import sys
    main()


     
