# функция reverse возвращает обратную строку
def reverse(x):
    return x[::-1]

# фукнция polindrome проверяет на совпадение исходную и переверную строку
def polindrome(x):
    res = reverse(x)

    if res == x:
        return True
    return False

while True:
    l1 = input("Введите слово: ")
    if polindrome(l1) == True:
        print(f'{l1} = {polindrome(l1)} , данное слово является полиндромом')
    else:
        print(f'{l1} = {polindrome(l1)} , данное слово не является полиндромом')
    continue



