import unittest

from views import product
from views.product import Product


class MyTestCase(unittest.TestCase):
    product = Product("00123", 350.00, "consumable", "grocery")

    def test_attrib(self):
        self.assertEqual("00123", self.product.product_id)
        self.assertEqual(350.00, self.product.price)
        self.assertEqual("consumable", self.product.product_description)
        self.assertEqual("grocery", self.product.product_category)

    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
