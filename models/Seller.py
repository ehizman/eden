import User


class Seller(User):
    def __init__(self, last_name, first_name, email, phone_number, password):
        super(Seller, self).__init__(last_name, first_name, email, phone_number, password)
