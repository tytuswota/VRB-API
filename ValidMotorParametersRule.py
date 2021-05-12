class ValidMotorParametersRule():
    def __init__(self):
        self.NUMBER_OF_PARAMETERS = 3
        self.VALID_MOTOR_IDS = [1,2,3]
        self.VALID_MOTOR_ACTIONS = [1,2]
        self.FRACTIONAL_POWER_LIMITS = [0,1]
    
    def validateMotorIDS(self, parameters):
        if parameters[0] in self.VALID_MOTOR_IDS:
            return True
        return False
    
    def validateMotorActions(self, parameters):
        if parameters[1] in self.VALID_MOTOR_ACTIONS:
            return True
        return False
    
    def validFractionalPower(self, parameters):
        if self.FRACTIONAL_POWER_LIMITS[0] <= parameters[2] <= self.FRACTIONAL_POWER_LIMITS[1]:
            return True
        return False
    
    def valid(self, parameters):
        print(parameters)
        if len(parameters) is self.NUMBER_OF_PARAMETERS and self.validateMotorIDS(parameters=parameters) and self.validateMotorActions(parameters=parameters) and self.validFractionalPower(parameters=parameters):
            return True
        return False
    

        
