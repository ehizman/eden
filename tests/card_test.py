import unittest

from views.card import Card


class MyTestCase(unittest.TestCase):
    card = Card("1234567889", "07/23", "", "234", "")

    def test_attrib(self):
        self.assertEqual("1234567889", self.card.PAN_No)
        self.assertEqual("07/23", self.card.expiring_date)
        self.assertEqual("", self.card.card_type)
        self.assertEqual("234", self.card.cvv)
        self.assertEqual("", self.card.PIN)

    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
