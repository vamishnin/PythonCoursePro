"""
Написать и вызвать функцию, проверяющую, что слово является палиндромом (примеры: “Топот”, “Довод”).
"""


def palindrome(str):
    if str == str[::-1] and not str.isspace():
        return True
    return False


str = input("Введите строку: ")

if palindrome(str.lower()):
    print("Это палиндром")
else:
    print("Это НЕ палиндром")
