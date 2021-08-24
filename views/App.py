from views.user import User


class App:
    def __init__(self, users=None):
        if users is None:
            self.users = []

    def register(self, first_name, last_name, email, password):
        user = User(first_name, last_name, email, password)
        self.users.append(user)

    def registerUser(self, user):
        self.users.append(user)

    def loginUser(self, user):
        self.users.append(user)

        


