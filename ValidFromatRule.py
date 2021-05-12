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
        methodId = message.pop(0)
        if self.validateHeader(methodType=methodId):
            return message
        return False

