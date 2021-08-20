import Product


class Items:
    def __init__(self, quantity, product):
        self.__quantity: int = quantity
        self.__product: Product = product

    @property
    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    @property
    def get_product(self):
        return self.__product

    def set_product(self, product):
        self.__product = product
