import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class CategoryTests(unittest.TestCase):
    def test_search_by_category(self):
        animation = DigitalVideoDisc("The Lion King", "Animation")
        science = DigitalVideoDisc("Star Wars", "Science Fiction")
        self.assertEqual(search_by_category([animation, science], "animation"), [animation])
        self.assertEqual(search_by_category([animation, science], "Drama"), [])
