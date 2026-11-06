import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class SortTests(unittest.TestCase):
    def test_sort_by_title(self):
        cart = Cart()
        for title in ("Star Wars", "Aladdin", "The Lion King"):
            cart.add_dvd(DigitalVideoDisc(title))
        cart.sort_by_title()
        self.assertEqual([dvd.title for dvd in cart.items], ["Aladdin", "Star Wars", "The Lion King"])

    def test_sort_by_cost(self):
        cart = Cart()
        for cost in (24.95, 18.99, 19.95):
            cart.add_dvd(DigitalVideoDisc(str(cost), cost=cost))
        cart.sort_by_cost()
        self.assertEqual([dvd.cost for dvd in cart.items], [18.99, 19.95, 24.95])
