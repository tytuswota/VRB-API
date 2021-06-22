import socket
import time

HEADER = 140
FORMAT = 'utf-8'

class ClientDevice():
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect(("95.217.181.53", 5050))
        self.message = ''

    def sendRequest(self, message):
        print('this will send the message=' + str(message))
        x = "A"
        b = "!/$0"

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