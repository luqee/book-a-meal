class User():
    """A class that model's a user."""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class MealOption():
    """A class that models a meal option."""
    def __init__(self, name, price):
        self.mealId = 0
        self.name = name
        self.price = price

class Order():
    """A class that models an order."""
    def __init__(self, user_name):
        self.orderId = 0
        self.user_name = user_name
        self.meal_option = ''

class BamApplication():
    """Book-a-meal application.

    This class models the Book-a-meal application.
    """
    def __init__(self):

        self.menu_for_the_day = ''
        self.registered_users = []
        self.online_users = []
        self.admin_users = []
        self.meal_options = []
        self.orders_list = []


    def signup_user(self, user):
        """Sign up method.

        This method checks if the passed in user is already registered
        and if not, the user is registered.
        """
        if user not in self.registered_users:
            self.registered_users.append(user)
            return 'registered'
        return 'User exists'

    def login_user(self, email, password):
        """Login method.

        This method recieves an email and password then checks if
        the email exists and the password matches.
        """
        result = 'error'
        for user in self.registered_users:
            if user.email == email:
                if user.password == password:
                    self.online_users.append(user)
                    result = 'logged_in'
        return result

    def add_meal_option(self, meal):
        """Add meal method.

        This method recieves e meal item and checks if it already exists
        before adding it to the meal_options list
        the email exists and the password matches.
        """
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
        """Get meal method.

        This method returns the meal_options list.
        """
        return self.meal_options

    def update_meal_options(self, meal_id, meal_opt):
        """Update meals method.

        This method recieves the meal id and meal option object
        and check the id aginst the available options then updates
        the matched meal.
        """
        result = 'Error'
        for meal in self.meal_options:
            if meal.mealId == meal_id:
                meal.name = meal_opt.name
                meal.price = meal_opt.price
                result = 'Updated'
        return result

    def delete_meal_options(self, meal_id):
        """Delete meal option method.

        This method uses the meal id argument to check for a matching
        meal in the meal_options list and removes it.
        """
        result = 'Error'
        for meal in self.meal_options:
            if meal.mealId == meal_id:
                self.meal_options.remove(meal)
                result = 'Deleted'
        return result

    def set_menu(self, meal_ids):
        """Set menu method.

        This method recieves a list of meal ids which are used
        to check which meal options to add to the menu.
        """
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
        """Get menu_for_the_day method.

        Returns the menu for the day.
        """
        return self.menu_for_the_day

    def select_meal(self, opt_id, username):
        """Select meal method.

        This method takes in option id and username variables.
        It checks if the meal with the given id exists in the
        menu_for_the_day. If so it creates an order object which is
        placed in the orders list replacing the previous order by the user.
        """
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
        """Update order method.

        This method recieves an order id and an option id.
        It updates the order with the given order using
        the meal option with the given id.
        """
        result = ''
        meal = self.get_meal_option(option_id)
        for order in self.orders_list:
            if order.orderId == order_id:
                order.meal_option = meal
                result = 'Success'
        return result

    def get_all_orders(self):
        """Get all orders method."""
        return self.orders_list

    def get_meal_option(self, opt_id):
        """Get meal option method."""
        for meal in self.meal_options:
            if meal.mealId == opt_id:
                return meal
