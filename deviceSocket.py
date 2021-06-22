from socket import AF_INET, socket, SOCK_STREAM
from sys import prefix
from threading import Thread

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
        msg = client.recv(BUFSIZE)
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


HOST = '95.217.181.53'
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

