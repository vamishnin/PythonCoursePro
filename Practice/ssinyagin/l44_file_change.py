def change_line(my_file, trig):
    with open(my_file) as f:
        if trig is "tab":
            dic = {"    ": "\t"}
        elif trig is "space":
            dic = {"\t": "    "}
        for line in f:
            for i, j in dic.items():
                print(f'before: {repr(line)}')
                line = line.replace(i, j)
                print(f'after: {repr(line)}')


fil = 'myfile.txt'
trig = "space"
fileop = change_line(fil, trig)


#  print(f'{str(t)}') - выведет табуляцию (как пользователю)
#  print(f'{repr(t)}') - выведет как служебный символ (как машине)
