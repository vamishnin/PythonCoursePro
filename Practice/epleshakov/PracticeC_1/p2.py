# Написать реализацию функции reversed: функция принимает список, возвращает его же,
# располагая элементы в обратном порядке.
def rever2(lst):
    n = len(lst)
    l2 = []
    for i in range(n):
        i += 1
        l2.append(lst[-i])
    return l2

ll = ['a', 'b', 'c', 'd']
print (rever2(ll))
ll2 = 'abcdef'
print(rever2(ll2))

# Второй вариант, без вспомогательного списка
def reversed(lst: list):
    return lst[::-1]

ll3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print (reversed(ll3))
ll4 = 'abcdef'
print(reversed(ll4))
