from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

#HEAD,ParamA,ParamB,ParamC
post_args = reqparse.RequestParser()
post_args.add_argument("type", type=str, help="Type of the message was not given...")
post_args.add_argument("paramA", type=str, help="ParamA was not given...")
post_args.add_argument("paramB", type=str, help="ParamB was not given...")
post_args.add_argument("paramC", type=str, help="ParamC was not given...")

class Message(Resource):
    def get(self):
        return 'The api is wip'
    
    def post(self):
        args = post_args.parse_args()
        MessageType = args['type']
        paramA = args['paramA']
        paramB = args['paramB']
        paramC = args['paramC']
        return MessageType, 200

api.add_resource(Message, "/")

if __name__ == "__main__":
    app.run(debug=True)
