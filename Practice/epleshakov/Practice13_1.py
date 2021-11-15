# Тест - tests\test_Practice13_1.py

class NonValidInput(Exception):
    print("Диапазон значений должен быть между 1 и 5000")



def to_roman(arab_number):
    if type(arab_number) != int:
        raise NonValidInput
    if not 0 < arab_number < 5001:
        raise NonValidInput
    roman_dict = {
        1000:'M', 900:'CM', 500:'D',
        400:'CD', 100:'C', 90:'XC',
        50:'L', 40:'XL', 10:'X',
        9:'IX', 5:'V', 4:'IV', 1:'I'
    }
    roman_out = ""
    for key in roman_dict.keys():
        count_roman = int(arab_number / key)
        roman_out += roman_dict[key] * count_roman
        arab_number -= key * count_roman
    print(roman_out)
    return roman_out

# try:
#     print(to_roman(4673))
# except NonValidInput:
#     print("Диапазон значений должен быть между 1 и 5000")
