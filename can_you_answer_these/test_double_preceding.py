from unittest import TestCase
from Q32 import double_preceding


class Test(TestCase):
    def test_list_with_second_number_not_double_of_the_first_number(self):
        test_list = [1, 4, 7]
        expected = [0, 2, 8]
        double_preceding(test_list)
        self.assertEqual(expected, test_list)
