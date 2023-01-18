#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Suite test for max_integer function
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_repetend_numbers(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_float_number(self):
        self.assertEqual(max_integer([3.3, 2.3, 1.5]), 3.3)

    def test_max_operated_num(self):
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    def test_neg_numbers(self):
        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)

    def test_max_start(self):
        self.assertEqual(max_integer([7, 6, 4, 3]), 7)

    def test_zero_num_list(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_big_list(self):
        self.assertEqual(max_integer([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901
        ]), 1000)

    def test_list_with_loop(self):
        self.assertEqual(max_integer([i * 2 for i in [1, 2, 3, 4, 5, 6]]), 12)

    def test_list_with_one_item(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, "one"])

    def test_tuple_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (2, 3)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'one': 1, 'two': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)
