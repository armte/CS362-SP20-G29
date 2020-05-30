# **************************************************************************
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
from task import my_datetime
from task import check_leap_year
from task import calc_month_day
from task import conv_date_to_string
from task import conv_endian


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


class TestMyDateTime(unittest.TestCase):
    # test to check if function returns proper date format when given seconds
    def test2_1(self):
        val = 86400
        expected = '01-02-1970'
        self.assertEqual(my_datetime(val), expected)

    # test if leap year check function works, pass common year
    def test2_2(self):
        val = 1971
        expected = False
        self.assertEqual(check_leap_year(val), expected)

    # test if leap year function works, pass leap year
    def test2_3(self):
        val = 2000
        expected = True
        self.assertEqual(check_leap_year(val), expected)

    # two days
    def test2_4(self):
        val = 172800
        expected = '01-03-1970'
        self.assertEqual(my_datetime(val), expected)

    # test if month and day are calculated correctly
    def test2_5(self):
        is_leap = True
        expected = 3, 30
        self.assertEqual(calc_month_day(90, is_leap), expected)

    # test if ints are converted to formatted string correctly
    def test2_6(self):
        day = 1
        month = 1
        year = 1970
        expected = '01-01-1970'
        self.assertEqual(conv_date_to_string(day, month, year), expected)

    # one year
    def test2_7(self):
        val = 31536000
        expected = '01-01-1971'
        self.assertEqual(my_datetime(val), expected)

    # two years, including leap year
    def test2_8(self):
        val = 63072000
        expected = '01-01-1972'
        self.assertEqual(my_datetime(val), expected)

    # 30 days
    def test2_9(self):
        val = 2592000
        expected = '01-31-1970'
        self.assertEqual(my_datetime(val), expected)

    # 90 days
    def test2_10(self):
        val = 7776000
        expected = '04-01-1970'
        self.assertEqual(my_datetime(val), expected)

    # 183 days, half a year
    def test2_11(self):
        val = 15811200
        expected = '07-03-1970'
        self.assertEqual(my_datetime(val), expected)

    # 0 days
    def test2_12(self):
        val = 0
        expected = '01-01-1970'
        self.assertEqual(my_datetime(val), expected)

    # example from function2 specs
    def test2_13(self):
        val = 123456789
        expected = '11-29-1973'
        self.assertEqual(my_datetime(val), expected)

    # example from function2 specs
    def test2_14(self):
        val = 9876543210
        expected = '12-22-2282'
        self.assertEqual(my_datetime(val), expected)

    # three years
    def test2_15(self):
        val = 94608000
        expected = '12-31-1972'
        self.assertEqual(my_datetime(val), expected)

    # three years and 1 day
    def test2_16(self):
        val = 94694400
        expected = '01-01-1973'
        self.assertEqual(my_datetime(val), expected)


class TestConvEndian(unittest.TestCase):

    def test_endian1(self):
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_endian2(self):
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test_endian3(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_endian4(self):
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')
        # little endian for reversed str

    def test_test5(self):
        self.assertEqual(conv_endian(954786, 'huge'), None)

    def test_test6(self):
        self.assertEqual(conv_endian(954786, ' '), None)

    def test_test7(self):
        self.assertEqual(conv_endian(-954786, 'big'), '-0E 91 A2')

    def test_test8(self):
        self.assertEqual(conv_endian(568944, 'big'), '08 AE 70')  # odd int

    def test_test9(self):
        self.assertEqual(conv_endian(1784345, 'big'), '1B 3A 19')  # even int

    def test_test10(self):
        self.assertEqual(conv_endian(1784345), '1B 3A 19')

    def test_test11(self):
        self.assertEqual(conv_endian(1784345, 'little'), '19 3A 1B')

    def test_test12(self):
        self.assertEqual(conv_endian(-143292, 'little'), '-BC 2F 02')

    def test_test13(self):
        self.assertEqual(conv_endian(-8653819, 'big'), '-84 0B FB')  # even,-


if __name__ == "__main__":
    unittest.main()
