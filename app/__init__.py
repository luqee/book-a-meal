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

    @use_args(meal_args)
    def delete(self, args):
        result = bam_application.delete_meal_options(args['mealId'])
        if result == 'Deleted':
            return make_response(jsonify({"message": "Successful removal"}), 201)

menu_parser = reqparse.RequestParser()
menu_parser.add_argument('meal_id', action='append')
class Menu(Resource):
    def get(self):
        result = bam_application.get_menu_for_the_day()
        menu_items = []
        for option in result:
            menu_items.append({'name': option.name, 'price': option.price, 'mealId': option.mealId })

        return make_response(jsonify(menu_items), 200)

    def post(self):
        data = menu_parser.parse_args()
        meal_opt_ids = data['meal_id']
        result = bam_application.set_menu(meal_opt_ids)
        print(result)
        if result == 'menu set':
            return make_response(jsonify({'message': 'Successfull setting of menu'}), 200)
        elif result == 'Error':
            return make_response(jsonify({'message': 'Try again'}), 200)

order_parser = reqparse.RequestParser()
order_parser.add_argument('meal_id')

order_args = {
'username': fields.Str(),
'orderId': fields.Int()
}

class Orders(Resource):
    def get(self):
        result = bam_application.get_all_orders()
        orders = []
        for order in result:
            orders.append({'order_by': order.user_name, 'meal': order.meal_option.name, 'order_id': order.orderId})

        return make_response(jsonify(orders), 200)

    @use_args(order_args)
    def post(self, args):
        data = order_parser.parse_args()
        meal_opt_id = data['meal_id']
        result = bam_application.select_meal(meal_opt_id, args['username'])
        print(result)
        if result == 'Success':
            return make_response(jsonify({'message': 'Order Successfully placed'}), 200)
        elif result == 'Error':
            return make_response(jsonify({'message': 'Try again'}), 200)

    @use_args(order_args)
    def put(self, args):
        data = order_parser.parse_args()
        meal_opt_id = data['meal_id']
        result = bam_application.update_order(args['orderId'], meal_opt_id)
        if result == 'Updated':
            return make_response(jsonify({"message": "Successful update"}), 201)


api.add_resource(SignUp, '/api/v1/auth/signup')
api.add_resource(Login, '/api/v1/auth/login')
api.add_resource(Meals, '/api/v1/meals', methods=['POST', 'GET', 'PUT', 'DELETE'])
api.add_resource(Menu, '/api/v1/menu')
api.add_resource(Orders, '/api/v1/orders')
