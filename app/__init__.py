from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class SignUp(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        return make_response(jsonify({
                                     "status": "ok",
                                     "username": username ,
                                     "email": email,
                                     "password": password
                                     }), 201)
        # pass

api.add_resource(SignUp, '/auth/signup')
