def change_line(my_file):
    with open(my_file) as f:
        dic = {"    ": "\t", "\t": "    "}
        for line in f:
            for i, j in dic.items():
                print(f'before: {repr(line)}')
                line = line.replace(i, j)
                print(f'after: {repr(line)}')


fil = 'myfile.txt'
fileop = change_line(fil)


#  print(f'{str(t)}') - выведет табуляцию (как пользователю)
#  print(f'{repr(t)}') - выведет как служебный символ (как машине)
