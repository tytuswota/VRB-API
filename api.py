from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from ValidFromatRule import ValidFormatRule
from ValidMotorParametersRule import ValidMotorParametersRule
from ValidTimerParametersRule import ValidTimerParametersRule
from ValidVoltageParametersRule import ValidVoltageParametersRule
from ValidMessageParametersRule import ValidMessageParametersRule
from Client import Client
from flask_cors import CORS
from flask_mysqldb import MySQL
from ClientDataBase import ClientDataBase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Babaman12!'
app.config['MYSQL_DB'] = 'vrb'

mysql = MySQL(app)

CORS(app)
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
        validMessage = V.valid(messageArray)
        if validMessage is not False:
            #TODO change this big if statement in a switch statement or something better
            if VPM.valid(parameters=validMessage) or VPV.valid(parameters=validMessage) or VPTR.valid(parameters=validMessage) or VPMM.valid(parameters=validMessage):
                client.sendRequest(message=messageArray, msql=mysql)
                return {'message': data['message']}, 201
            return 400
        return 400

class Status(Resource):
    def post(self):
        data = request.get_json(force=True)

        messageArray = data['message']

        #message=[1,0] = device 1 is offline
        #message=[1,1] = device 1 is online
        #message=[1,2] = device 1 is running

        cldb = ClientDataBase()
        cldb.updateStatus(data=messageArray, mysql=mysql)

        return 200

api.add_resource(Request, '/api')
api.add_resource(Status, '/update_status')

if __name__ == '__main__':
    app.run(host='95.217.181.53', port='2000', debug=True)
