class ValidTimerParametersRule():
    def __init__(self):
        self.NUMBER_OF_PARAMETERS = 2
        self.VALID_TIMER_IDS = [1,2,3]
        self.VALID_TIMER_ACTIONS = [1,2,3]
    
    def validateTimerIDS(self, parameters):
        if parameters[0] in self.VALID_TIMER_IDS:
            return True
        return False
    
    def validateTimerActions(self, parameters):
        if parameters[1] in self.VALID_TIMER_ACTIONS:
            return True
        return False

    def valid(self, parameters):
        if len(parameters) is self.NUMBER_OF_PARAMETERS and self.validateTimerIDS(parameters=parameters) and self.validateTimerActions(parameters=parameters):
            return True
        return False
    

        
