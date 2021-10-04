word = input('Ваедите слово: ')


def check_pal(w):
    len_str = len(w)
    half_len = int(len_str//2)
    half_1 = w[0:half_len]
    half_2 = w[(half_len+1):len_str]
    if half_1 in half_2[::-1]:     # сравнил первую половину с перевернутой второй
        return True
    else:
        return False


if check_pal(word):
    print(f'Слово "{word}" - является палиндромом')
else:
    print(f'Слово "{word}" - не является палиндромом')



