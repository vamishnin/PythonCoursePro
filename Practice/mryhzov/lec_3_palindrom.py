word = input('Введите слово: ')
word = word.lower()    # все буквы к строчным


def check_pal(w):
    len_str = len(w)
    half_len = len_str // 2
    half_1 = w[:half_len]    # 1я половина в любом случае от начала до half_len
    half_2 = w[half_len:] if len_str % 2 == 0 else w[(half_len + 1):]  # 2я половина срезается взависимости от условия
    return half_1 == half_2[::-1]


if check_pal(word):
    print(f'Слово "{word}" - является палиндромом')
else:
    print(f'Слово "{word}" - не является палиндромом')

