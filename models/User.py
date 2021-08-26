import abc


class User(abc.ABC):
    def __init__(self, first_name, last_name, email, user_name, password, home_address, phone_number):
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__user_name: str = user_name
        self.__phone_number: str = phone_number
        self.__email: str = email
        self.__password: str = password
        self.__home_address: str = home_address

    @property
    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    @property
    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    @property
    def get_user_name(self):
        return self.__user_name

    def set_user_name(self, user_name):
        self.__user_name = user_name

    @property
    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    @property
    def get_email(self):
        return self.__email

    def set__(self, email):
        self.__email = email

    @property
    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    @property
    def get_home_address(self):
        return self.__home_address

    def set_home_address(self, home_address):
        self.__home_address = home_address
