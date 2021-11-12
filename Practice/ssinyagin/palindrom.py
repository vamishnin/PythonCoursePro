def palind(palin):
    #pallist = palin
    d = len(palin)
    j = 0
    i = 0
    if d >= 2:
        for r in palin:
            if palin[i] != palin[d-1-i]:
                print(f'слово {palin} не палиндром!')
                break
            elif j > d / 2:
                print(f'слово {palin} палиндром')
                break
            else:
                j += 1
    else:
        print(f'слово {palin} не палиндром!')


print('Программа проверит слово на палиндром.')
palin = palind(input('введите слово: '))
