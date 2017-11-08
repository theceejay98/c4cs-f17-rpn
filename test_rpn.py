import unittest

import rpn
import sys
from termcolor import colored, cprint

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
        cprint ("test_add passed", "white", "on_green")
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
        cprint ("test_subtract passed", "white", "on_green")
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
        cprint ("test_multiply passed", "white", "on_green")
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
        cprint ("test_divide passed", "white", "on_green")
    def test_carat(self):
        result = rpn.calculate("2 2 ^")
        self.asserEqual(4, result)
        cprint ("test_carat passed", "white", "on_green")
