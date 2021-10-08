"""
Написать и вызвать функцию, проверяющую, что слово является палиндромом (примеры: “Топот”, “Довод”).
"""


def palindrome(line):
    if line == line[::-1] and not line.isspace():
        return True
    return False


line = input("Введите строку: ")

if palindrome(line.lower()):
    print("Это палиндром")
else:
    print("Это НЕ палиндром")
