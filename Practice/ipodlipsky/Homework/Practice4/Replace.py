def tab_replace(val):
    new_str = str(val).replace('\t', '    ')
    return print(new_str)

def space_replace(val):
    new_str = str(val).replace('    ' , '\t')
    return print(new_str)


str1 = '''
    1tab  2tab    3tab    4tab
'''
str2 = '''
    1space  2space    3space    4space
'''

print(str1, str2)

tab_replace(str1)
space_replace(str2)