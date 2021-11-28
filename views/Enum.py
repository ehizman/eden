import enum


class Users(enum.Enum):
    ADMIN = 2
    CUSTOMER = 4
    SELLER = 3

class Card_Type(enum.Enum):
    MASTER_CARD = ""
    VERVE_CARD = ""
    VISA_CARD = ""


class product_category(enum.Enum):
    GROCERY = ""
    ELECTRONICS = ""
    UTENSILS = ""
    CLOTHING = ""
    SHOES = ""



