import socket
import time

HEADER = 140
FORMAT = 'utf-8'

class ClientDevice():
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect(("localhost", 5050))
        self.message = ''

    def sendRequest(self, message):
        print('this will send the message=' + str(message))
        x = "A"
        b = "!/$0"

        # strMsg = str(message)
        # message = strMsg.encode(FORMAT)
        # msg_length = len(message)
        # send_length = str(msg_length).encode(FORMAT)
        # send_length += b' ' * (HEADER - len(send_length))
        # self.clientSocket.send(send_length)
        # self.clientSocket.send(message)
        # print("in the send")
        # time.sleep(0.1)
        # self.clientSocket.send("{quit}")
        name = "api"
        self.clientSocket.send(bytes(name, "utf8"))
        time.sleep(0.1)
        strMessage = str(message)
        print(strMessage)
        self.clientSocket.send(bytes(strMessage, "utf8"))
        time.sleep(0.1)
        self.clientSocket.send(bytes(str("{quit}"), "utf8"))
        time.sleep(0.1)
        self.clientSocket.close()

        return 200
