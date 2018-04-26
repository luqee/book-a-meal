class Order():
    """A class that models an order."""
    def __init__(self, user_name):
        self.order_id = 0
        self.user_name = user_name
        self.meal_option = ''
