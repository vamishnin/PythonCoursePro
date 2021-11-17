ONES = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")
TENS = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
HUNDREDS = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
THOUSANDS = ("", "M", "MM", "MMM", "MMMM", "MMMMM")


def to_roman(arabic_num):

    try:
        if arabic_num < 1 or arabic_num > 5000:
            raise ValueError
    except ValueError:
        return 'Input error'

    first = THOUSANDS[arabic_num // 1000]
    second = HUNDREDS[arabic_num // 100 % 10]
    third = TENS[arabic_num // 10 % 10]
    fourth = ONES[arabic_num % 10]

    return first + second + third + fourth


if __name__ == '__main__':
    print(to_roman(11))
