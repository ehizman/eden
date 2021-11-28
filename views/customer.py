from views.user import User


class Customer(User):
    def __init__(self, first_name, last_name, email, password, phone_number, billing_info, shopping_cart, home_address):
        super().__init__(first_name, last_name, email, password, phone_number)
        self.billing_info = billing_info
        self.home_address = home_address
        self.shopping_cart = shopping_cart
