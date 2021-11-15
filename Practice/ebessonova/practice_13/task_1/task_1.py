def to_roman(arabic_num):

    if arabic_num < 1 or arabic_num > 5000:
        return 'Input error'

    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands = ["", "M", "MM", "MMM", "MMMM", "MMMMM"]

    first = thousands[arabic_num // 1000]
    second = hundreds[arabic_num // 100 % 10]
    third = tens[arabic_num // 10 % 10]
    fourth = ones[arabic_num % 10]

    return first + second + third + fourth

if __name__ == '__main__':
    print(to_roman(11))
