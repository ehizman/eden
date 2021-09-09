from unittest import TestCase

from models.Address import Address


class TestAddress(TestCase):
    def test_get__city_name(self):
        address: Address = Address(city_name="NewYork", country_name="China", house_number="312",
                                   street="herbert Macaulay way", name="sade")
        city_name: str = address.get__city_name
        self.assertEquals("NewYork", city_name)

    def test_set__city_name(self):
        address: Address = Address(city_name="NewYork", country_name="China", house_number="312",
                                   street="herbert Macaulay way", name="sade")
        address.set__city_name("Gabon")
        self.assertEquals("Gabon", address.get__city_name)

    def test_get__country_name(self):
        address: Address = Address(city_name="NewYork", country_name="China", house_number="312",
                                   street="herbert Macaulay way", name="sade")
        country_name: str = address.get__country_name
        self.assertEquals("China", country_name)

    def test_set__country_name(self):
        self.fail()

    def test_get__house_number(self):
        self.fail()

    def test_set__house_number(self):
        self.fail()

    def test_get__street(self):
        self.fail()

    def test_set__street(self):
        self.fail()

    def test_get__name(self):
        self.fail()

    def test_set__name(self):
        self.fail()
