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
        if parameters[0] in self.VALID_MEASUREMENT_TYPES:
            return True
        return False

    def validateDateFormat(self, parameters):
        date_time_string = parameters[2]
        dateTimeFormat = "%d-%m-%Y %H:%M:%M"
        try:
            datetime.datetime.strptime(date_time_string, dateTimeFormat)
            return True
        except ValueError:
            return False

    def valid(self, parameters):
        if self.validateMeasurementType(parameters=parameters) and self.validateDateFormat(parameters=parameters):
            return True
        return False            