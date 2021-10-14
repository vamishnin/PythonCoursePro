# Написать генератор для построчного чтения файла
def gen_printline(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line


for file_str in gen_printline('text_P.txt'):
    print(file_str)
