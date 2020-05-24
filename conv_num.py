import constant
import re
from enum import Enum


class NumType(Enum):
    INT = 0
    DEC = 1
    HEX = 2


def conv_num(str_num):
    if len(str_num) > 0:
        str_type = num_type(str_num)
        if str_type == NumType.DEC:
            return get_dec(str_num)
        elif str_type == NumType.INT:
            return get_int(str_num)
    return None


def get_int(str_num):
    int_num = 0
    for digit in str_num:
        int_num *= 10
        int_num += (ord(digit) % constant.ASCII_0)
    return int_num


def get_dec(str_num):
    int_frac = re.split(r'\.', str_num)
    frac_str = int_frac[1]
    exp = -1
    fraction = 0.0
    for digit in frac_str:
        num = ord(digit) % constant.ASCII_0
        fraction += (num * 10**exp)
        exp -= 1
    dec_num = get_int(int_frac[0]) + fraction
    return dec_num


def num_type(str_num):
    # check if string is in proper decimal point format
    dec_check = re.split(r'\.', str_num)
    # if the num string has only 1 decimal point
    if len(dec_check) == 2:
        for digit in dec_check:
            # check that string on both sides of decimal point
            # is not empty and numeric
            if digit and not digit.isdecimal():
                return None
        return NumType.DEC
    elif str_num.isdecimal():
        return NumType.INT
    else:
        return None
