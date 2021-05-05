from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from ValidFromatRule import ValidFormatRule
from ValidMotorParametersRule import ValidMotorParametersRule
from ValidTimerParametersRule import ValidTimerParametersRule
from ValidVoltageParametersRule import ValidVoltageParametersRule
from ValidMessageParametersRule import ValidMessageParametersRule
from Client import Client

app = Flask(__name__)
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

#json = message: [int:header, int:params..]
class Request(Resource):
    def post(self):
        args = parser.parse_args()
        data = json.loads(args['message'])
        messageArray = data['message']

        parameters = ValidFormRule.valid(message=messageArray)

        if parameters is not False:
            #TODO change this big if statement in a switch statement or something better
            if ValidMotorParametersRule.valid(parameters=parameters) or ValidTimerParametersRule.valid(parameters=parameters) or ValidVoltageParametersRule.valid(parameters=parameters) or ValidMessageParametersRule.valid(parameters=parameters):
                Client.sendRequest(message=messageArray)
                return {'message': args['message']}, 201
            return 400
        return 400

api.add_resource(Request, '/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
