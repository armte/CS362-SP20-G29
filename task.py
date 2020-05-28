def conv_endian(num, endian='big'):
    # map decimal nums to hexadecimals
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
