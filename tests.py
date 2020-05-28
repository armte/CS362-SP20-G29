# CS 362: Software Engineering II
# Group 29: Tommy Armstrong, Oliver Solorzano, Andre Pestovski
# Assignment: Group Project - Part 2
# Description: This file contains the test suite that our code for functions
# 1-3 will run against.
# Contributions:
#   Tommy Armstrong: Test class for function 1 (TestConvNum)
#   Oliver Solorzano:
#   Andre Pestovski:
# ***************************************************************************

import unittest

from task import conv_endian


class TestConvEndian(unittest.TestCase):

    def test_endian1(self):
        self.assertTrue(True)
        self.assertEqual(conv_endian(954786), '0E 91 A2')

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

    def test17(self):
        val = '--123.45'
        expected = None
        self.assertEqual(conv_num(val), expected)

    def test18(self):
        val = '--12345'
        expected = None
        self.assertEqual(conv_num(val), expected)

    def test19(self):
        val = '--0xAD4'
        expected = None
        self.assertEqual(conv_num(val), expected)

    def test_endian2(self):
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test_endian3(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_endian4(self):
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_test5(self):
        self.assertEqual(conv_endian(954786, 'huge'), None)

    def test_test6(self):
        self.assertEqual(conv_endian(954786, ' '), None)

    def test_test7(self):
        self.assertEqual(conv_endian(-954786, 'big'), '-0E 91 A2')

    def test_test7a(self):
        self.assertEqual(conv_endian(568944, 'big'), '08 AE 70') # odd int to hex

if __name__ == "__main__":
    unittest.main()
