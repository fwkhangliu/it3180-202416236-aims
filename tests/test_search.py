import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTests(unittest.TestCase):
    def test_search_by_title_case_insensitive(self):
        lion = DigitalVideoDisc("The Lion King")
        items = [lion, DigitalVideoDisc("Star Wars")]
        for keyword in ("lion", "LION", "LiOn"):
            with self.subTest(keyword=keyword):
                self.assertEqual(search_by_title(items, keyword), [lion])
        self.assertEqual(search_by_title(items, "missing"), [])
