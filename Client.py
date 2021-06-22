from MethodTypes import MethodTypes
from ClientDataBase import ClientDataBase
from ClientDevice import ClientDevice

class Client():
    def __init__(self):
        self.DATABASE_CLIENT_METHOD_TYPE_ID = 4

    def sendRequest(self, message, msql):
        print(message)
        if message[0] is self.DATABASE_CLIENT_METHOD_TYPE_ID:
            cldb = ClientDataBase()
            cldb.storeData(data=message, mysql=msql)
        else:
            cld = ClientDevice()