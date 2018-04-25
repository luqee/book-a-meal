class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class MealOption():
    def __init__(self, name, price):
        self.name = name
        self.price = price

class BamApplication():


    def __init__(self):
        #list of meal options representing the day's menu
        self.munu_for_the_day = []
        # list of registered users
        self.registered_users = []
        # list of logged in users
        self.online_users = []
        # list of administrators
        self.admin_users = []
        # Available meal options
        self.meal_options = []


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
        if meal not in self.meal_options:
            self.meal_options.append(meal)
            result = 'added'
        return result

    def get_meal_options(self):
        return self.meal_options
