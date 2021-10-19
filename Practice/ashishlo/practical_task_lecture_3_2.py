# 2. Написать и вызвать функцию, проверяющую, что слово является палиндромом (примеры: “Топот”, “Довод”).
# Сначала реализовал по тупому, потом подсмотрел как еще можно в интернете.

def check_palindrome(a: str):
    if a == a[::-1]:
        print("palindrome detected ")
    else:
        print("not palindrome")


check_palindrome(input("enter the candidate for palindrome: "))
