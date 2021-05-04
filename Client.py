from MethodTypes import MethodTypes
from ClientDataBase import ClientDataBase
from ClientDevice import ClientDevice

class Client():
    def __init__(self):
        self.DATABASE_CLIENT_METHOD_TYPE_ID = 4

    def sendRequest(self, message):
        if message[0] is self.DATABASE_CLIENT_METHOD_TYPE_ID:
            ClientDataBase.storeData(data=message)
        else:
            ClientDevice.sendRequest(message=message)