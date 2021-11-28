import unittest

from views.address import Address


class MyTestCase(unittest.TestCase):
    address = Address("7", "Lugard ", "Ikoyi", "Lagos")

    def test_attrib(self):
        self.assertEqual("7", self.address.address_No)
        self.assertEqual("Lugard ", self.address.address_street)
        self.assertEqual("Ikoyi", self.address.address_city)
        self.assertEqual("Lagos", self.address.address_state)

    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
