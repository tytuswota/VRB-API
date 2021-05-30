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

import socket
import threading
import requests

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

HEADER = 140
PORT = 5050
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!/$0"
connected = False

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    global connected
    print(f"[NEW CONNECTION] {addr} connected.")
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = len(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            send_client(conn, addr, ("Msg Recieved"))
            if msg == DISCONNECT_MESSAGE:
                connected = False    
            else:
                print(f"[{addr}] {msg}") 
                messageArray = [float(x) for x in list(msg.split(","))]           
                requests.post('http://localhost:5000/api', json={"message": messageArray})
            #conn.send("Msg received".encode(FORMAT))
           
    #     send_client(conn,addr,"[2,2,3,4]")
    #     send_client(conn,addr,"[4,4,3,4]")
    # send_client(conn,addr,"[3,3,3,4]")     
    # print(connected)
    conn.close()

def send_client(conn, addr, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)
    print(f"gestuurd")
    
def start():
    global connected
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        connected = True
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")    
start()

# send_client("[1,1,1,1]")


