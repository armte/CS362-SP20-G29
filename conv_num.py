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


def conv_int(str_num):
    int_num = 0
    for digit in str_num:
        int_num *= 10
        int_num += (ord(digit) % constant.ASCII_0)
    return int_num


def conv_dec(int_frac):
    frac_str = int_frac.group('frac')
    exp = -1
    fraction = 0.0
    for digit in frac_str:
        num = ord(digit) % constant.ASCII_0
        fraction += (num * 10**exp)
        exp -= 1
    integral = int_frac.group('int')
    dec_num = conv_int(integral) + fraction
    return dec_num


def conv_hex(hex_match):
    hex_vals = hex_match.group('hvals')
    int_num = 0
    for hex_val in hex_vals:
        int_num *= 16
        if hex_val.isdecimal():
            num = ord(hex_val) % constant.ASCII_0
        else:
            num = ord(hex_val) % constant.ASCII_A10
        int_num += num
    return int_num


def num_type(str_num):
    # check if string is in proper decimal point format
    # dec_check = re.split(r'\.', str_num)
    dec_match = re.match(r'(?P<int>\d*)\.(?P<frac>\d*$)', str_num)
    if dec_match:
        # check that at least one side of decimal point is not empty
        empty = True
        for dec_val in dec_match.groups():
            if dec_val:
                empty = False
        return (NumType.DEC, dec_match) if not empty else None
    # check if string is in the proper hexadecimal format
    hex_match = re.match(r'0x(?P<hvals>[A-F0-9]+$)', str_num)
    if hex_match:
        return NumType.HEX, hex_match
    if str_num.isdecimal():
        return NumType.INT, str_num
    return None
