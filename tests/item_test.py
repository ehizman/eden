import unittest

from views.items import Items


class MyTestCase(unittest.TestCase):
    item = Items("00123", 350.00, "consumable", "grocery", "9")

    def test_attrib(self):
        self.assertEqual("00123", self.item.product_id)
        self.assertEqual(350.00, self.item.price)
        self.assertEqual("consumable", self.item.product_description)
        self.assertEqual("grocery", self.item.product_category)
        self.assertEqual("9", self.item.quantity)

    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
