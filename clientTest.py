import socket
import threading
import time


HEADER = 140
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!/$0"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

# # connected = True
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print("in the send")
    time.sleep(0.1)

def receive():  
    while True: 
        # print("in receive")
        # print(client.recv(HEADER).decode(FORMAT))
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            print(f"{msg}")
        # time.sleep(2)

def start():
    print(f"client socket is gestart {SERVER}")
    thread = threading.Thread(target=receive)
    thread.start()
        
start()
# input()

# for i in range(10):
#     send("[1,1,1,0.1]")
send("1,1,1,0.1") 
send(DISCONNECT_MESSAGE)

 # send("[1,1,1,1]")

# # input()

# exit()
# # start()

