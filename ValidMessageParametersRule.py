import datetime
class ValidMessageParametersRule():
    def __init__(self):
        #================================
        #1 = volage measurement
        #2 = temperature measurement
        #3 = mebrane resistance
        #================================
        self.VALID_MEASUREMENT_TYPES = [1,2,3]
    
    def validateMeasurementType(self, parameters):
        if parameters[1] in self.VALID_MEASUREMENT_TYPES:
            return True
        return False

    def validateDateFormat(self, parameters):
        
        date_time_string = parameters[3]
        if(isinstance(date_time_string, str)):
            dateTimeFormat = "%d-%m-%Y %H:%M:%M"
            try:
                datetime.datetime.strptime(date_time_string, dateTimeFormat)
                return True
            except ValueError:
                return False
        return False

    def valid(self, parameters):
        print("aaaaaa")
        if self.validateMeasurementType(parameters=parameters):
            return True
        return False            