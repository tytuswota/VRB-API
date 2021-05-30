from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from ValidFromatRule import ValidFormatRule
from ValidMotorParametersRule import ValidMotorParametersRule
from ValidTimerParametersRule import ValidTimerParametersRule
from ValidVoltageParametersRule import ValidVoltageParametersRule
from ValidMessageParametersRule import ValidMessageParametersRule
from Client import Client

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
api = Api(app)


#========================================================
#the request parser checks if the json or post arg is valid
#========================================================
parser = reqparse.RequestParser()
parser.add_argument('message')

#class JsonDecode:
    #this class isn't needed the json decoding and validating is already done by the RequestParser
#    def validateJsonFormat()
#        return True
#    def decodeJsonMessage(jsonMessage):
#        retrun {}



class Request(Resource):
    def post(self):

        data = request.get_json(force=True)

        messageArray = data['message']

        V = ValidFormatRule()
        VPV = ValidVoltageParametersRule()
        VPTR = ValidTimerParametersRule()
        VPMM = ValidMessageParametersRule()
        VPM = ValidMotorParametersRule()
        
        client = Client()
        parameters = V.valid(messageArray)
        if parameters is not False:
            #TODO change this big if statement in a switch statement or something better
            if VPM.valid(parameters=parameters) or VPV.valid(parameters=parameters) or VPTR.valid(parameters=parameters) or VPMM.valid(parameters=parameters):
                client.sendRequest(message=messageArray)
                return {'message': data['message']}, 201
            return 400
        return 400

api.add_resource(Request, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

