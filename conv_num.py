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
    int_frac = re.split('\.', str_num)
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
    dec_check = re.split('\.', str_num)
    if len(dec_check) == 2:
        for i in range(len(dec_check)):
            if not dec_check[i].isdecimal():
                return None
        return NumType.DEC
    elif str_num.isdecimal():
        return NumType.INT
    else:
        return None
