from views.user import User


class Seller(User):
    def __init__(self, first_name, last_name, email, password, phone_number):
        super().__init__(first_name, last_name, email, password, phone_number)
