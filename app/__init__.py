from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api, reqparse
from app import bamApp

app = Flask(__name__)
api = Api(app)
bam_application = bamApp.BamApplication()

signup_parser = reqparse.RequestParser()
signup_parser.add_argument('username')
signup_parser.add_argument('email')
signup_parser.add_argument('password')

class SignUp(Resource):
    def post(self):
        data = signup_parser.parse_args()
        username = data['username']
        email = data['email']
        password = data['password']
        user = bamApp.User(username, email, password)
        result = bam_application.signup_user(user)
        # print(result)
        if result == 'registered':
            return make_response(jsonify({"message": "Successfull signup",}), 201)

api.add_resource(SignUp, '/api/v1/auth/signup')
