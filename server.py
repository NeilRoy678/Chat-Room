import socket
import threading
ip ='127.0.0.1'
port  = 55555 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,port))
server.listen()
clients = []
nicknames = []
def broadcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
             message = client.recv(1024)
             broadcast(message)
        except:
             index = clients.index(client)
             clients.remove(client)
             client.close()
             nickname = nicknames[index]
             broadcast(f'{nickname} left the chat!')
             
             nicknames.remove(nickname)
             break
def receive():
    while True:
        client,address = server.accept()
        print(f"CONNECTION ESTABLISIHED {str(address)}")
        client.send("NICK".encode('ascii')) 
        name = client.recv(1024).decode('ascii')
        nicknames.append(name)
        clients.append(client)
        
        print(f"nickname is {name}")
        broadcast(f"{name} has joined the chat!!".encode('ascii'))
        client.send("CONNECTED TO THE SERVER".encode('ascii'))
        thread = threading.Thread(target=handle,args=(client,))
        thread.start()
print("server started") 
receive()   
        