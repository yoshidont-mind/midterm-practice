from unittest import TestCase
from Q14 import median


class Test(TestCase):
    def test_all_numbers_are_different(self):
        expected = 3.3
        self.assertEqual(expected, median(3.3, 4.4, 2.2))

    def test_two_numbers_are_same(self):
        expected = 2.2
        self.assertEqual(expected, median(2.2, 1.1, 2.2))

