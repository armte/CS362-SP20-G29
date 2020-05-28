"""
Description: the function takes in an integer value as num and converts it
to a hexadecimal number. The endian type is determined by the flag endian.
The function will return the converted number as a string. It has the following
specifications:
*It may be assumed that num will always be an integer
*Must be able to handle negative values for num
*A value of big for endian will return a hexadecimal number that is big-endian
*A value of little for endian will return a hexadecimal number that is
little-endian
*Any other values of endian will return None
*The returned string will have each byte separated by a space
*Each byte must be two characters in length"""


def conv_endian(num, endian='big'):
    # map decimal nums to hex values
    mapped_vals = {
        0: "0", 1: "1", 2: "2", 3: "3", 4: "4",
        5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
        10: "A", 11: "B", 12: "C", 13: "D",
        14: "E", 15: "F",
    }
    assert num == int(num)
    _hex = ""
    negative = False
    if num < 0:
        # set negative flag
        negative = True
        # make num positive to proceed to calculation
        num *= -1
    while num > 0:
        # add condition for endian == 'big' or 'little, else return None
        if endian not in ['big', 'little']:
            return None

        while num > 0:
            num, remainder = num // 16, num % 16
            _hex = mapped_vals[remainder] + _hex

        if len(_hex) % 2 == 1:
            _hex = '0' + _hex

        hex_string = ' '.join(_hex[i:i + 2] for i in range(0, len(_hex), 2))

        if endian == 'little':
            # reverse paired string of big endian to create little endian
            hex_bytes = hex_string.split(' ')
            little_endian = ' '.join(hex_bytes[::-1])
            hex_string = little_endian
            # add "-" for negative hex
        if negative:
            hex_string = '-' + hex_string

        return hex_string

        hex_string = ' '.join(_hex[i:i + 2] for i in range(0, len(_hex), 2))
        # format hex string in byte pairs

        return hex_string
        while index > 0:
            _hex += str[index - 1]
            # save the value of str[index-1] in reverseString
            index = index - 1  # decrement index
            print(_hex)  # reversed string
        else:
            return 'None'
        # add "0" to hex to match requirements' format
        _hex = '0' + _hex
        if negative is True:
            # add "-" to the hex value formatted in pair bytes
            print("-" + ' '.join(_hex[i:i + 2]for i in range(0, len(_hex), 2)))
            return "-" + ' '.join(_hex[i:i + 2]for i in range(0, len(_hex), 2))
        if negative is False:
            # otherwise return positive hex formatted in paired bytes
            print(' '.join(_hex[i:i + 2] for i in range(0, len(_hex), 2)))
            return ' '.join(_hex[i:i + 2] for i in range(0, len(_hex), 2))
