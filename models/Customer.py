import User


class Customer(User):
    def __init__(self, first_name, last_name, user_name, password):
        super(Customer, self).__init__(first_name, last_name, user_name, password)
        
