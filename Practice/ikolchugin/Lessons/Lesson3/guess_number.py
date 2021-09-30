from random import randint

LOWER = 0
UPPER = 100


def strict_input(_prompt, _lower=LOWER, _upper=UPPER):
    x = -1
    while not _lower <= x <= _upper:
        x = int(input(f'{_prompt}, от {_lower} до {_upper}: '))
    return x


lower = upper = 0

print(f'Я загадаю число в указанном вами диапазоне целых положительных чисел')
while True:
    lower = strict_input('Нижняя граница')
    upper = strict_input('Верхняя граница', int(lower) + 1)
    if lower < upper:
        break
    else:
        print('значение нижней границы должно быть меньше значения верхней границы')

magic_number = randint(lower, upper)
print(f'Я загадал число в диапазоне от {lower} до {upper},\n'
      f'попробуйте его угадать')

guessed = -1
attempt = 1

while guessed != magic_number:
    print(f'Попытка №{attempt}')
    guessed = strict_input('Введите ваш вариант в диапазоне', lower, upper)
    if guessed > magic_number:
        print('Ваше число больше загаданного мной, попытайтесь еще раз\n')
    elif guessed < magic_number:
        print('Ваше число меньше загаданного мной, попытайтесь еще раз\n')
    else:
        print(f'Ура, Вы угадали число {magic_number} с {attempt} попыток')
    attempt += 1
