class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class MealOption():
    def __init__(self, name, price):
        self.mealId = 0
        self.name = name
        self.price = price

class Order():
    def __init__(self, user_name):
        self.orderId = 0
        self.user_name = user_name
        self.meal_option = ''

class BamApplication():


    def __init__(self):

        self.menu_for_the_day = ''
        self.registered_users = []
        self.online_users = []
        self.admin_users = []
        self.meal_options = []
        self.orders_list = []


    def signup_user(self, user):
        if user not in self.registered_users:
            self.registered_users.append(user)
            return 'registered'
        return 'User exists'

    def login_user(self, email, password):
        result = 'error'
        for user in self.registered_users:
            if user.email == email:
                if user.password == password:
                    self.online_users.append(user)
                    result = 'logged_in'
        return result

    def add_meal_option(self, meal):
        result = ''
        if meal.name in [option.name for option in self.meal_options ]:
            result = 'Meal exists'
        else:
            meal.mealId = len(self.meal_options) +1
            print(meal.mealId)
            self.meal_options.append(meal)
            result = 'added'
        return result

    def get_meal_options(self):
        return self.meal_options

    def update_meal_options(self, meal_id, meal_opt):
        result = 'Error'
        for meal in self.meal_options:
            if meal.mealId == meal_id:
                meal.name = meal_opt.name
                meal.price = meal_opt.price
                result = 'Updated'
        return result

    def delete_meal_options(self, meal_id):
        result = 'Error'
        for meal in self.meal_options:
            if meal.mealId == meal_id:
                self.meal_options.remove(meal)
                result = 'Updated'
        return result

    def set_menu(self, meal_ids):
        result = 'Error'
        selected_meals = []
        for id in [int(id) for id in meal_ids]:
            for meal in self.meal_options:
                if meal.mealId == id:
                    selected_meals.append(meal)
        self.menu_for_the_day = selected_meals
        result = 'menu set'
        return result

    def get_menu_for_the_day(self):
        return self.menu_for_the_day

    def select_meal(self, opt_id, username):
        result = ''
        for meal in self.menu_for_the_day:
            if meal.mealId == int(opt_id):
                order = Order(username)
                order.meal_option = meal
                order.orderId = len(self.orders_list) + 1
                
        for order_item in self.orders_list:
            if order_item.user_name == username:
                self.orders_list.remove(order_item)

        self.orders_list.append(order)
        result = 'Sucess'
        return result

    def update_order(self, order_id, option_id):
        result = ''
        meal = self.get_meal_option(option_id)
        for order in self.orders_list:
            if order.orderId == order_id:
                order.meal_option = meal
                result = 'Success'
        return result

    def get_all_orders(self):
        return self.orders_list

    def get_meal_option(self, opt_id):
        for meal in self.meal_options:
            if meal.mealId == opt_id:
                return meal
