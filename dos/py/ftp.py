#!/usr/bin/python

import socket

print ("Interagindo com serviços")

ip=input("digite o ip")
port=input("Digite a porta")
port_int=int(port)

my_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.connect((ip,port_int))
banner=my_socket.recv(1024)
print (banner)

my_socket.send("USER user\n")
banner=my_socket.recv(1024)
print (banner)

my_socket.send("PASS pass\n")
banner=my_socket.recv(1024)
print (banner)
