from MethodTypes import MethodTypes
from ClientDataBase import ClientDataBase
from ClientDevice import ClientDevice

class Client():
    def __init__(self):
        self.DATABASE_CLIENT_METHOD_TYPE_ID = 4
        self.SEND_TIME_SYNC_METHOD_TYPE_ID = 5

    def sendRequest(self, message, msql):
        print(message)
        if message[0] is self.DATABASE_CLIENT_METHOD_TYPE_ID:
            cldb = ClientDataBase()
            cldb.storeData(data=message, mysql=msql)
        if message[0] is seself.SEND_TIME_SYNC_METHOD_TYPE_ID:
            #send post request time sync to vrb site php
        else:
            cld = ClientDevice()
