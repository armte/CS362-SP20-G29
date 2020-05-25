import constant
import re
from enum import Enum


class NumType(Enum):
    INT = 0
    DEC = 1
    HEX = 2


def conv_num(str_num):
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


def conv_int(int_match):
    integral = int_match.group('int')
    int_num = 0
    for digit in integral:
        int_num *= 10
        int_num += (ord(digit) % constant.ASCII_0)
    if int_match.group('sign') == '-':
        int_num *= -1
    return int_num


def conv_dec(dec_match):
    frac_str = dec_match.group('frac')
    exp = -1
    fraction = 0.0
    for digit in frac_str:
        num = ord(digit) % constant.ASCII_0
        fraction += (num * 10**exp)
        exp -= 1
    dec_num = conv_int(dec_match)
    if dec_num < 0:
        dec_num -= fraction
    else:
        dec_num += fraction
    return dec_num


def conv_hex(hex_match):
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


def num_type(str_num):
    # check if string is in acceptable decimal point format
    dec_match = re.match(r'(?P<sign>-*)(?P<int>\d*)\.(?P<frac>\d*$)',
                         str_num, re.ASCII)
    if dec_match:
        # check that at least one side of decimal point is not empty
        empty = True
        for dec_val in dec_match.groups():
            if dec_val:
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
