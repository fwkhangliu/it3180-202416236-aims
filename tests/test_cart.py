import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for number in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(str(number))))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("21st DVD")))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_remove_dvd(self):
        cart = Cart()
        dvd = DigitalVideoDisc("The Lion King", cost=19.95)
        self.assertTrue(cart.add_dvd(dvd))
        self.assertAlmostEqual(cart.total_cost(), 19.95)
        self.assertTrue(cart.remove_dvd(dvd))
        self.assertFalse(cart.remove_dvd(dvd))
        self.assertEqual(cart.total_cost(), 0)
