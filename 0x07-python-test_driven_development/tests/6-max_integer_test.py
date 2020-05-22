#!/usr/bin/python3
"""Unit test for the function max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestingMaxInteger(unittest.TestCase):
    """
    Class Test for the max integer cases
    """
    def no_arguments_test(self):
        """ Test when no arguments is passed """
        self.assertIsNone(max_integer())

    def empty_list(self):
        """ Test when the list is empty """
        list = []
        self.assertIsNone(max_integer(list))

    def negative_numbers(self):
        """ Test for a list with negative numbers """
        list = [-2, -3, -567, -4]
        self.assertEqual(max_integer(list), -2)

    def passed_None(self):
        """ Test for when is passed None """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_for_no_int(self):
        """ Test for look is in the list are numbers or not """
        list = [34, 23, "What", 45, 67]
        with self.assertRaises(TypeError):
            max_integer(list)

    def one_element(self):
        """ Test for when the list only has one element """
        list = [2908]
        self.assertEqual(max_integer(list), 2908)

if __name__ == "__main__":
    unittest.main()
