# CS 362: Software Engineering II
# Group 29: Tommy Armstrong, Oliver Solorzano, Andre Pestovski
# Assignment: Group Project - Part 2
# Description: This file contains the test suite that our code for functions
# 1-3 will run against.
# Contributions:
#   Tommy Armstrong: Test class for function 1 (TestConvNum)
#   Oliver Solorzano: Test class for function 2 (TestMyDateTime)
#   Andre Pestovski:
# ***************************************************************************

import unittest
from task import conv_num


class TestConvNum(unittest.TestCase):

    def test1(self):
        val = ''
        expected = None
        self.assertEqual(conv_num(val), expected)

    def test2(self):
        val = '12345'
        expected = 12345
        self.assertEqual(conv_num(val), expected)

    def test3(self):
        val = '123.45'
        expected = 123.45
        self.assertEqual(conv_num(val), expected)

    def test4(self):
        val = '.45'
        expected = 0.45
        self.assertEqual(conv_num(val), expected)

    def test5(self):
        val = '123.'
        expected = 123.0
        self.assertEqual(conv_num(val), expected)

    def test6(self):
        val = '0xAD4'
        expected = 2772
        self.assertEqual(conv_num(val), expected)

    def test7(self):
        val = '0xAZ4'
        expected = None
        self.assertEqual(conv_num(val), expected)

    def test8(self):
        val = '12345A'
        expected = None
        self.assertEqual(conv_num(val), expected)

    def test9(self):
        val = '12.3.45'
        expected = None
        self.assertEqual(conv_num(val), expected)

    def test10(self):
        val = '.'
        expected = None
        self.assertEqual(conv_num(val), expected)

    def test11(self):
        val = '0xAd4'
        expected = 2772
        self.assertEqual(conv_num(val), expected)

    def test12(self):
        val = '-12345'
        expected = -12345
        self.assertEqual(conv_num(val), expected)

    def test13(self):
        val = '-0xAD4'
        expected = -2772
        self.assertEqual(conv_num(val), expected)

    def test14(self):
        val = '-123.45'
        expected = -123.45
        self.assertEqual(conv_num(val), expected)

    def test15(self):
        val = '-123.'
        expected = -123.0
        self.assertEqual(conv_num(val), expected)

    def test16(self):
        val = '-.45'
        expected = -0.45
        self.assertEqual(conv_num(val), expected)

class TestMyDateTime(unittest.TestCase):

    def test2_1(self):  # test to check if function returns proper date format when given seconds
        val = 86400
        expected = '01-02-1970'
        self.assertEqual((my_datetime(val), expected))


if __name__ == "__main__":
    unittest.main()
