def symbol_replase(data, sym: str = '\t', repsym: str = '    '):
    x = data
    return x.replace(sym, repsym)


source = 'qwe ert    yui\tasd\tfgh jkl    zxc'
print(f'{source=}')
print(f'Tab to 4*whitespaces: {repr(symbol_replase(source))}')
s2 = symbol_replase(source, "    ", "\t")
print(f'4*whitespaces to Tab : {repr(s2)}')


with open('Practice4_4_testfile.txt', 'r') as file2:
    text = file2.read()
    print(f'{text=}')
    print(repr(symbol_replase(text)))
    print(repr(symbol_replase(text, '    ', '\t')))
