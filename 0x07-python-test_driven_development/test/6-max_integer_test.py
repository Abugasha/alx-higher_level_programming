#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test the function max_integer to get the max value
    of a list of integers
    """

    def test_empty_list(self):
        """ Pass an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_no_list(self):
        """ Pass != to list object"""
        self.assertEqual(max_integer('a'), 'a')
        self.assertEqual(max_integer("This is not a list"), 't')
        self.assertRaises(TypeError, max_integer, 25)

    def test_with_floats(self):
        """ Pass floats"""
        my_test_list = [2.5, 3.2, 4.5, 4.8]
        self.assertEqual(max_integer(my_test_list), 4.8)
        my_test_list = [0.5, 0.7, 0.8, 1.0]
        self.assertEqual(max_integer(my_test_list), 1.0)
        my_test_list = [0.5, 0.55, 0.555, 0.6]
        self.assertEqual(max_integer(my_test_list), 0.6)

    def test_with_ints(self):
        """ Pass ints"""
        my_test_list = [2, 3, 4, 40]
        self.assertEqual(max_integer(my_test_list), 40)
        my_test_list = [5, 2, 5, 8]
        self.assertEqual(max_integer(my_test_list), 8)

    def test_negative_ints(self):
        """ Pass negative ints"""
        my_test_list = [-2, -3, 4, -40]
        self.assertEqual(max_integer(my_test_list), 4)
        my_test_list = [5, -2, -5, 8]
        self.assertEqual(max_integer(my_test_list), 8)

    def same_number(self):
        """ Pass same ints"""
        my_test_list = [20, 20, 20, 20]
        self.assertEqual(max_integer(my_test_list), 20)
        my_test_list = [-5, -5, -5, -5]
        self.assertEqual(max_integer(my_test_list), -5)

    def test_huge_int(self):
        """ Pass huge ints"""
        my_test_list = [float('inf'), 0, 5]
        self.assertEqual(max_integer(my_test_list), float('inf'))
        my_test_list = [10000000000, -2, -5, 8]
        self.assertEqual(max_integer(my_test_list), 10000000000)

    def test_mixed_list(self):
        """ Pass huge ints"""
        my_test_list = ['a', 65, 'z']
        self.assertRaises(TypeError, max_integer, my_test_list)
        my_test_list = [22, -2, -5, 'A']
        self.assertRaises(TypeError, max_integer, my_test_list)

if __name__ == '__main__':
    unittest.main()
