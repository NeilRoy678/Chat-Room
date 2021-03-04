'''Socket programming'''
import socket
import threading
nickname =input("ENTER NICKNAME")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = '127.0.0.1'
port = 55555
client.connect((ip, port))
def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "NICK":
                client.send(nickname.encode('ascii'))
                
            else:
                print(message)
        except:
            print("ERROR")
            client.close()
            break
def write():
     while True:
        message = f'{nickname}:{input(" ")}'  
        client.send(message.encode('ascii'))         
r_thread = threading.Thread(target = recieve)
r_thread.start()
w_thread = threading.Thread(target = write)
w_thread.start()

