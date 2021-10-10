
while True:
    while not (number := input("Введите 5-ти символьное число: ")).isdigit():
        print(f"Это не число: {number}")
    if len(number) == 5:
        break
    else:
        print("Число должно быть пятизначным")

i = 1
for d in number:
    print(f"{i} цифра равна {d}")
    i += 1