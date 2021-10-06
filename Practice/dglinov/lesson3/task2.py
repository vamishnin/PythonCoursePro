"""
Написать и вызвать функцию, проверяющую, что слово является палиндромом (примеры: “Топот”, “Довод”).
"""
data = {
    'довод',
    'топот',
    'питон',
    1999994,
    'ДоВОД',
    '     ',
}

def check_pali(a):
    if isinstance(a, str) and not a.isspace():
        x = a.lower()
        if x == x[::-1]:
            print(f"'{a}' is a palindrome")
        else: 
            print(f"'{a}' is not a palindrome")
    else:
        print("Bad input!")

for w in data:
    check_pali(w)