import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class DiscountTests(unittest.TestCase):
    def test_total_cost_with_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD", cost=100))
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80)

    def test_invalid_discount_percent(self):
        for percent in (-1, 150):
            with self.subTest(percent=percent), self.assertRaises(ValueError):
                Cart().total_cost_with_discount(percent)
