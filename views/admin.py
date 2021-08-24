from views.user import User


class Seller(User):
    def __init__(self,  email, password):
        super().__init__(email, password)