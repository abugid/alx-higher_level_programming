#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_number(self):
        self.assertEqual(max_integer([1, 2, 3, 2]), 3)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3.5]), 3.5)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, -5, -7, 0]), 1)
        self.assertEqual(max_integer([i for i in range(5)]), 4)
        self.assertEqual(max_integer([True, False]), True)