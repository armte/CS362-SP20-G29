# CS 362: Software Engineering II
# Group 29: Tommy Armstrong, Oliver Solorzano, Andre Pestovski
# Assignment: Group Project - Part 2
# Description: This file contains the code implementation for the functions:
# conv_num, my_datetime, and conv_endian along with their helper functions.
# Function conv_num: acts as a number converter, taking in string
# representations of numbers in any one of the three formats: integer,
# decimal point or hexadecimal and returning the decimal value as either an
# integer or float datatype value. Negative numbers are accepted and there
# is no case sensitivity regarding numbers in hexadecimal format.
# Contributions:
#   Tommy Armstrong - conv_num function and its associated code/functions
# References:
# regular expression implementation:
#   re syntax:
#   https://docs.python.org/3/library/re.html#regular-expression-syntax
#   re match function:
#   https://docs.python.org/2.0/lib/match-objects.html
#   github re python library source code:
#   https://github.com/python/cpython/blob/master/Lib/re.py
# ***************************************************************************

import constant
import re
from enum import Enum


# This enum class and its values serve to identify the three different number
# formats an input string can be in: integer, decimal point or hexadecimal
class NumType(Enum):
    INT = 0
    DEC = 1
    HEX = 2


def conv_num(str_num):
    """returns either the integer or float datatype representation of the
    input string if it is in any one of the acceptable number formats:
    whole number, decimal point or hexadecimal. Returns None by default"""
    if len(str_num) > 0:
        # try to match the string to an acceptable number format
        str_type_match = num_type(str_num)
        # convert the string to a decimal number and return it
        # if it has an acceptable format
        if str_type_match:
            str_type = str_type_match[0]
            str_match = str_type_match[1]
            if str_type == NumType.DEC:
                return conv_dec(str_match)
            if str_type == NumType.HEX:
                return conv_hex(str_match)
            if str_type == NumType.INT:
                return conv_int(str_match)
    return None


# See the regular expression references in the file header for detailed
# explanation on re syntax and re.match() in function below
def num_type(str_num):
    """Analyzes the input string to see if it matches any of the acceptable
    numeric formats: whole number, decimal point or hexadecimal. If so,
    the enum associated with the numeric format type and the re match object
    is returned as a tuple, otherwise None is returned"""
    # check if string is in acceptable decimal point format
    dec_match = re.match(r'(?P<sign>-*)(?P<int>\d*)\.(?P<frac>\d*$)',
                         str_num, re.ASCII)
    if dec_match:
        # check that at least one side of decimal point is not empty
        empty = True
        for dec_val in dec_match.groups():
            if dec_val and dec_val.isdecimal():
                empty = False
        return (NumType.DEC, dec_match) if not empty else None
    # check if string is in the acceptable hexadecimal format
    hex_match = re.match(r'(?P<sign>-*)0x(?P<hvals>[0-9a-fA-F]+$)',
                         str_num, re.ASCII)
    if hex_match:
        return NumType.HEX, hex_match
    # check if string is in the acceptable integer format
    int_match = re.match(r'(?P<sign>-*)(?P<int>\d+$)', str_num, re.ASCII)
    if int_match:
        return NumType.INT, int_match
    return None


def conv_int(int_match):
    """Returns the integer representation of the whole number input string
    represented by the match object parameter"""
    integral = int_match.group('int')
    int_num = 0
    for digit in integral:
        int_num *= 10
        int_num += (ord(digit) % constant.ASCII_0)
    if int_match.group('sign') == '-':
        int_num *= -1
    return int_num


def conv_dec(dec_match):
    """Returns the float representation of the decimal point number
    input string represented by the match object parameter"""
    frac_str = dec_match.group('frac')
    exp = -1
    fraction = 0.0
    for digit in frac_str:
        num = ord(digit) % constant.ASCII_0
        fraction += (num * 10 ** exp)
        exp -= 1
    dec_num = conv_int(dec_match)
    if dec_match.group('sign') == '-':
        dec_num -= fraction
    else:
        dec_num += fraction
    return dec_num


def conv_hex(hex_match):
    """Returns the integer representation of the hexadecimal number
    input string represented by the match object parameter"""
    hex_vals = hex_match.group('hvals')
    int_num = 0
    for hex_val in hex_vals:
        int_num *= 16
        if hex_val.isdecimal():
            num = ord(hex_val) % constant.ASCII_0
        else:
            hex_val = hex_val.upper()
            num = ord(hex_val) % constant.ASCII_A10
        int_num += num
    if hex_match.group('sign') == '-':
        int_num *= -1
    return int_num


def my_datetime(seconds):
    """Takes seconds since the designated epoch as a positive integer
    value. Returns the date for time passed as a string in the
    format MM-DD-YYYY"""
    # epoch split into int values for easier calculation
    epoch_day = 1
    epoch_month = 1
    epoch_year = 1970

    return '01-01-1971'
