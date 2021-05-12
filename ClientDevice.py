class ClientDevice():
    def __init__(self):
        self.message = ''

    def sendRequest(self, message):
        print('this will send the message=' + str(message))
        return 200
