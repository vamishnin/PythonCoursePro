import itertools

# Функция должна принимать три массива ([1, 2, 3], [4, 5], [6, 7]), а вернуть лишь один массив ([1, 2, 3, 4, 5, 6, 7])
lst1, lst2, lst3 = [1, 2, 3], [4, 5], [6, 7]
result1 = [el for el in itertools.chain(lst1, lst2, lst3)]
print(result1)

# Функция принимает массив (['hello', 'i', 'write', 'cool', 'code']) и возвращает массив из элементов,
# у которых длина не меньше пяти (['hello', 'write'])
lst4 = ['hello', 'i', 'write', 'cool', 'code']
result2 = [el for el in itertools.filterfalse(lambda x: len(x) < 5, lst4)]
print(result2)

# Функция выдает на строку 'password' все возможные комбинации вида
# ([('p', 'a', 's', 's'), ('p', 'a', 's', 'w'), ('p', 'a', 's', 'o'), ...)
word = 'password'
result3 = [el for el in itertools.combinations(word, 4)]
print(result3)
