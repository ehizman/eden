from views.product import Product


class Items(Product):
    def __init__(self, product_id, price, product_description, product_category, quantity):
        super().__init__(product_id, price, product_description, product_category)
        self.quantity = quantity
