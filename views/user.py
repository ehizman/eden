class User:
    def __init__(self, email, password, first_name=None, last_name=None, phone_number=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def change_password(self, old_password, new_password):
        if old_password == self.password:
            self.password = new_password
