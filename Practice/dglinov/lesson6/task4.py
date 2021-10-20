'''
Часто задача программиста заключается в том, чтоб найти в документации готовую функцию, которая реализует необходимое решение. 
Данное задании предполагает самостоятельное изучение документации к библиотеке itertools (это набор готовых итераторов), 
чтобы подобрать те функции, которые дадут правильные ответы на следующие вопросы (иногда надо будет добавить свои аргументы при вызове функций помимо тех, что указаны в задании):
Функция должна принимать три массива ([1, 2, 3], [4, 5], [6, 7]), а вернуть лишь один массив ([1, 2, 3, 4, 5, 6, 7])
Функция принимает массив (['hello', 'i', 'write', 'cool', 'code']) и возвращает массив из элементов, у которых длина не меньше пяти (['hello', 'write'])
Функция выдает на строку 'password' все возможные комбинации вида ([('p', 'a', 's', 's'), ('p', 'a', 's', 'w'), ('p', 'a', 's', 'o'), ...)
Требуется написать код, который использует указанные входные данные и выводит на экран возвращаемое значение. 
Помните, что функции могут возвращать генератор, который нужно "развернуть" для вывода на экран.
'''

# [evequeen@evequeen-vm lesson6]$ pip list | grep iter
# more-itertools      8.8.0
# # [evequeen@evequeen-vm lesson6]$ pip install more-itertools
# Defaulting to user installation because normal site-packages is not writeable
# Requirement already satisfied: more-itertools in /usr/lib/python3.9/site-packages (8.8.0)

import itertools

#Функция должна принимать три массива ([1, 2, 3], [4, 5], [6, 7]), а вернуть лишь один массив ([1, 2, 3, 4, 5, 6, 7])
def merge_to_array(*args, **kwargs):
    '''
    itertools.chain(*iterables)
    Make an iterator that returns elements from the first iterable until it is exhausted, 
    then proceeds to the next iterable, until all of the iterables are exhausted. 
    Used for treating consecutive sequences as a single sequence.
    '''
    return [x for x in itertools.chain(*args)]

#Функция принимает массив (['hello', 'i', 'write', 'cool', 'code']) и возвращает массив из элементов, у которых длина не меньше пяти (['hello', 'write'])
def filter_by_len(lst):
    '''
    itertools.filterfalse(predicate, iterable)
    Make an iterator that filters elements from iterable returning only those for which the predicate is False.
    If predicate is None, RETURN THE ITEMS THAT ARE FALSE.
    '''
    return [x for x in itertools.filterfalse(lambda x: len(x) < 5, lst)]

#Функция выдает на строку 'password' все возможные комбинации вида ([('p', 'a', 's', 's'), ('p', 'a', 's', 'w'), ('p', 'a', 's', 'o'), ...)
#Требуется написать код, который использует указанные входные данные и выводит на экран возвращаемое значение. 
def gen_exact_len_words_combination_from_string(line, out_len):
    '''
    itertools.combinations(iterable, r)
    Return r length subsequences of elements from the input iterable.
    The combination tuples are emitted in lexicographic ordering according to the order of the input iterable. 
    So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
    Elements are treated as unique based on their position, not on their value. So if the input elements are unique, 
    there will be no repeat values in each combination
    '''
    if out_len > len(line):
        raise Exception(f'Length for expected combinations is greater than length of input string')
    else:
        return [x for x in itertools.combinations(line, out_len)]


if __name__ == '__main__':
        
    print(merge_to_array([1, 2, 3], [4, 5], [6, 7]))
    print(filter_by_len(['hello', 'i', 'write', 'cool', 'code']))
    
    _LENGTH = 4
    print(gen_exact_len_words_combination_from_string('password', _LENGTH))