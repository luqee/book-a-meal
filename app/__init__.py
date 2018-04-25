from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api, reqparse
from webargs import fields
from webargs.flaskparser import use_args

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

login_parser = reqparse.RequestParser()
login_parser.add_argument('email')
login_parser.add_argument('password')
class Login(Resource):
    def post(self):
        data = login_parser.parse_args()
        email = data['email']
        password = data['password']
        result = bam_application.login_user(email, password)
        print(result)
        if result == 'logged_in':
            return make_response(jsonify({"message": "Successfull login"}), 200)

meal_parser = reqparse.RequestParser()
meal_parser.add_argument('name')
meal_parser.add_argument('price')

meal_args = {'mealId': fields.Int(required=True)}
class Meals(Resource):
    def get(self):
        options = bam_application.get_meal_options()
        meals = []
        for option in options:
            meals.append({'name': option.name, 'price': option.price, 'mealId': option.mealId })

        return make_response(jsonify(meals), 200)

    def post(self):
        data = meal_parser.parse_args()
        name = data['name']
        price = data['price']
        meal_option = bamApp.MealOption(name, price)
        result = bam_application.add_meal_option(meal_option)
        print(result)
        if result == 'added':
            return make_response(jsonify({"message": "Successfull addition"}), 201)
        elif result == 'Meal exists':
            return make_response(jsonify({"message": "Meal exists"}), 200)

    @use_args(meal_args)
    def put(self, args):
        # print('args value ; '+ str(args['mealId']))
        data = meal_parser.parse_args()
        name = data['name']
        price = data['price']
        meal_option = bamApp.MealOption(name, price)
        result = bam_application.update_meal_options(args['mealId'], meal_option)
        if result == 'Updated':
            return make_response(jsonify({"message": "Successful update"}), 201)




api.add_resource(SignUp, '/api/v1/auth/signup')
api.add_resource(Login, '/api/v1/auth/login')
api.add_resource(Meals, '/api/v1/meals')
