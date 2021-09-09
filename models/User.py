import abc


class User(abc.ABC):
    def __int__(self, first_name, last_name, email, user_name, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_name = user_name
        self.__email = email
        self.__password = password
