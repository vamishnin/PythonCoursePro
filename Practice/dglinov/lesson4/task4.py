'''
Реализовать функциональность, которая бы “сворачивала” и “разворачивала” символы табуляции в файле или строке. 
То есть, передается на вход файл или строка, необходимо заменить все символы табуляции на четыре пробела, 
либо же заменить все комбинации из четырех символов пробела на символ табуляции.
'''
test_string = 'This is spaces:    :This is spaces\nThis is tab:\t:This is tab'

def tab_to_space(x):
    return x.replace('\t',' ' * 4)

def space_to_tab(x):
    return x.replace(' ' * 4,'\t')

print(tab_to_space(test_string))
print(space_to_tab(test_string))