word = input('Введите слово: ')
word = word.lower()    # все буквы к строчным


def check_pal(w):
    len_str = len(w)
    half_len = len_str // 2
    if len_str % 2 == 0:
        half_1 = w[:half_len]    # от начала до середины
        half_2 = w[half_len:]    # от середины до конца
    else:
        half_1 = w[:half_len]
        half_2 = w[(half_len + 1):]
    return half_1 == half_2[::-1]


if check_pal(word):
    print(f'Слово "{word}" - является палиндромом')
else:
    print(f'Слово "{word}" - не является палиндромом')

