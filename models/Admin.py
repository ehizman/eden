from models.User import User


class Admin:
    def __init__(self):
        self.__user_name = "Admin"
        self.__password = "0000"

    @property
    def get_user_name(self):
        return self.__user_name

    @property
    def get_password(self):
        return self.__password

