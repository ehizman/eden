import unittest

from views.seller import Seller


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.seller = Seller("Ayo", "kuku", "ayo@gmail.com","1234","23456")

    def test_attrib(self):
        self.assertEqual("Ayo", self.seller.first_name)
        self.assertEqual("kuku",self.seller.last_name)
        self.assertEqual("ayo@gmail.com",self.seller.email)
        self.assertEqual("1234", self.seller.password)
        self.assertEqual("23456",self.seller.phone_number)






    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
