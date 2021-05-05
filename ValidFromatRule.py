from MethodTypes import MethodTypes

class ValidFormatRule():
    def validateHeader(self, methodType):
        if methodType in MethodTypes:
            return True
        return False

    def valid(self, message):
        methodId = message.pop(0)
        if self.validateHeader(methodType=methodId):
            return message
        return False

