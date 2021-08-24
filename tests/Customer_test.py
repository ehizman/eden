import unittest

from views.customer import Customer


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.customer = Customer("babatunde", "kuku", "bkuku@gmail.com", "0700", "09898777", "", "7", "Lagos")

    def test_attrib(self):
        self.assertEquals("babatunde", self.customer.first_name)
        self.assertEqual("kuku", self.customer.last_name)
        self.assertEqual("bkuku@gmail.com", self.customer.email)
        self.assertEqual("0700", self.customer.password)
        self.assertEqual("09898777", self.customer.phone_number)
        self.assertEqual("", self.customer.billing_info)
        self.assertEqual("7", self.customer.shopping_cart)
        self.assertEqual("Lagos", self.customer.home_address)

    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
