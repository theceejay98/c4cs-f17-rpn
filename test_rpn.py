import unittest

import rpn
import colored

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
        print (stylize("test_add passed", colored.fg("white"), colored.bg("green")))
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
        print (stylize("test_subtract passed", colored.fg("white"), colored.bg("green")))
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
        print (stylize("test_multiply passed", colored.fg("white"), colored.bg("green")))
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
        print (stylize("test_divide passed", colored.fg("white"), colored.bg("green")))
    def test_carat(self):
        result = rpn.calculate("2 1 ^")
        self.asserEqual(2, result)
        print (stylize("test_carat passed", colored.fg("white"), colored.bg("green")))
