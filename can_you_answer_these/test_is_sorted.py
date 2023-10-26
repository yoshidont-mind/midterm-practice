from unittest import TestCase
from Q33 import  is_sorted


class Test(TestCase):
    def test_increasing_order(self):
        test_list = [1, 2, 3]
        expected = True
        self.assertEqual(expected, is_sorted(test_list))

    def test_list_with_decreasing_order(self):
        test_list = [3, 2, 1]
        expected = False
        self.assertEqual(expected, is_sorted(test_list))

    def test_list_with_random_order(self):
        test_list = [3, 2, 3, 4]
        expected = False
        self.assertEqual(expected, is_sorted(test_list))

    def test_list_with_duplicates(self):
        test_list = [1, 2, 2, 3, 3]
        expected = True
        self.assertEqual(expected, is_sorted(test_list))
