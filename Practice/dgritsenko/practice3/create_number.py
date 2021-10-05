
result_number = ''

while (in_symbols := input("Введите очередное число: ")) != 'stop':
    if in_symbols.isdigit():
        result_number += in_symbols
    else:
        print(f"Это не число - {in_symbols}")

print(f"Итоговое число: {result_number}")