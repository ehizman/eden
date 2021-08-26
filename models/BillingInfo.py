from models import CardType, Address


class BillingInfo:
    def __init__(self, phone_number, address, name, credit_card):
        self.__phone_number: str = phone_number
        self.__address: Address = address
        self.__name: str = name
        self.__credit_card: CardType = credit_card

    @property
    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    @property
    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    @property
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @property
    def get_credit_card(self):
        return self.__credit_card

    def set_credit_card(self, credit_card):
        self.__credit_card = credit_card
        