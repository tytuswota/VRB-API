# import socket
# import threading
# import requests

# #==========================
# #motor control
# #fractional power the float can varry in size
# #[int, int, float]
# #==========================
# #timer control
# #[int, int]
# #header size is 5 bytes
# #==========================
# #==========================
# #valid voltage rule 
# #[int, float]
# #the float can varry
# #==========================

# HEADER = 140
# PORT = 5050
# SERVER = "127.0.0.1"
# ADDR = (SERVER, PORT)
# FORMAT = 'utf-8'
# DISCONNECT_MESSAGE = "!/$0"

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(ADDR)

# def handle_client(conn, addr):
#     print(f"[NEW CONNECTION] {addr} connected.")

#     connected = True
#     while connected:
#         msg_length = conn.recv(HEADER).decode(FORMAT)
#         if msg_length:
#             msg_length = int(msg_length)
#             msg = conn.recv(msg_length).decode(FORMAT)
#             if msg == DISCONNECT_MESSAGE:
#                 connected = False

#             print(f"[{addr}] {msg}")
#             conn.send("Msg received".encode(FORMAT))

#     conn.close()
        

# def start():
#     server.listen()
#     print(f"[LISTENING] Server is listening on {SERVER}")
#     while True:
#         conn, addr = server.accept()
#         thread = threading.Thread(target=handle_client, args=(conn, addr))
#         thread.start()
#         print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
from socket import AF_INET, socket, SOCK_STREAM
from sys import prefix
from threading import Thread

#import requests

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

#starts a client connection



def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("you have been connected", "utf8"))
        #Saves all the client addresses to a list, and sends everything back  
        addresses[client] = client_address
        global clientID
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
    name = client.recv(BUFSIZE).decode("utf8")
    clients[client] = name 
    while True:
        print("=========A==========")
        msg = client.recv(BUFSIZE)
        print("=========B==========")
        if msg != bytes("{quit}", "utf8"):
            prefix = name + ": "
            broadcast(msg, prefix)
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            break

def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)




addresses = {}
clients = {}


HOST = 'localhost'
PORT = 5050
BUFSIZE = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()



