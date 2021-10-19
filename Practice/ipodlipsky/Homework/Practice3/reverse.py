def polindrome(x):
    res = x[::-1]
    return res == x

while True:
    l1 = input("Введите слово: ")
    if polindrome(l1):
        print(f'{l1} = {polindrome(l1)} , данное слово является полиндромом')
    else:
        print(f'{l1} = {polindrome(l1)} , данное слово не является полиндромом')
    continue