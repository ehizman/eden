class Address:

    def __init__(self, city_name, country_name, house_number, street, name):
        self.__city_name = city_name
        self.__country_name = country_name
        self.__house_number = house_number
        self.__street = street
        self.__name = name

    @property
    def get__city_name(self):
        return self.__city_name

    def set__city_name(self, city_name):
        self.__city_name = city_name

    @property
    def get__country_name(self):
        return self.__country_name

    def set__country_name(self, country_name):
        self.__country_name = country_name

    @property
    def get__house_number(self):
        return self.__house_number

    def set__house_number(self,house_number):
        self.__house_number = house_number

    @property
    def get__street(self):
        return self.__street

    def set__street(self, street):
        self.__street = street

    @property
    def get__name(self):
        return self.__name

    def set__name(self, name):
        self.__name = name
