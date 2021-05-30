import socket
import threading
import requests

#==========================
#motor control
#fractional power the float can varry in size
#[int, int, float]
#==========================
#timer control
#[int, int]
#header size is 5 bytes
#==========================
#==========================
#valid voltage rule 
#[int, float]
#the float can varry
#==========================

HEADER = 140
PORT = 5050
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!/$0"
URL = 'http://localhost:5000/'

headers = {'Content-Type': 'application/json'}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
            
            obj = {'message' : msg}
            try:
                x = requests.post(url=URL, json=obj, headers=headers)
                print(x.text)
            except requests.exceptions.ConnectionError:
                print("big error")
    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("server is starting")
start()