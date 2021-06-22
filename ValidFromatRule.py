from MethodTypes import MethodTypes

class ValidFormatRule():
    def __init__(self):
        self.data = []

    def validateHeader(self, methodType):
        values = [item.value for item in MethodTypes]
        if methodType in values:
            return True
        return False

    def valid(self, message):
        methodId = message[0]
        print(methodId)
        if self.validateHeader(methodType=methodId):
            return message
        return False

