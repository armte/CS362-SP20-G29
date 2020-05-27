# map decimal nums to hex values
mapped_vals = {
    0: "0", 1: "1", 2: "2", 3: "3", 4: "4",
    5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
    10: "A", 11: "B", 12: "C", 13: "D",
    14: "E", 15: "F",
}


def conv_endian(num, endian='big'):
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
        if endian == 'big':
            num, remainder = num // 16, num % 16
            _hex = mapped_vals[remainder] + _hex
        elif endian == 'little':
            num, remainder = num // 16, num % 16
            _hex = mapped_vals[remainder] + _hex
            # reverse pairs of str for little endian
            # _hex = ' '.join(reversed(_hex))
            #
            #reversedString = []
            index = len(_hex)  # calculate length of string and save in index
            while index > 0:
                _hex += str[index - 1]  # save the value of str[index-1] in reverseString
                index = index - 1  # decrement index
            print(_hex)  # reversed string
        else:
            return 'None'
    # add "0" to hex to match requirements' format
    _hex = '0' + _hex
    if negative == True:
        # add "-" to the hex value formatted in pair bytes
        print("-" + ' '.join(_hex[i:i + 2] for i in range(0, len(_hex), 2)))
        return "-" + ' '.join(_hex[i:i + 2] for i in range(0, len(_hex), 2))
    if negative == False:
        # otherwise return positive hex formatted in paired bytes
        print(' '.join(_hex[i:i + 2] for i in range(0, len(_hex), 2)))
        return ' '.join(_hex[i:i + 2] for i in range(0, len(_hex), 2))
