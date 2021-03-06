class ValidVoltageParametersRule():
    def __init__(self):
        self.NUMBER_OF_PARAMETERS = 2
        self.VALID_VOLTAGE_ACTIONS = [1,2]
        self.VALID_VOLTAGE_LIMITS = []
    
    def validateVoltageActions(self, parameters):
        if parameters[0] in self.VALID_VOLTAGE_ACTIONS:
            return True
        return False

    def valid(self, parameters):
        return True