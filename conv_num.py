import constant

def conv_num(str_num):
    if len(str_num) > 0:
        return get_int(str_num)
    return None

def get_int(str_num):
    int_num = 0
    for i in range(len(str_num)):
        digit = str_num[i]
        int_num *= 10
        int_num += (ord(digit) % constant.ASCII_0)
    return int_num
