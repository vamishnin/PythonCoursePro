# Написать реализацию встроенной функции len: функция принимает список, возвращает его длину.
def len2(lst):
    n = 0
    for i in lst:
        n += 1
    return n

ll = ['a', 'b', 'c', 'd']
print (len2(ll))
ll2 = 'abcdef'
print(len2(ll2))