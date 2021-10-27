'''
Разминка Лекции №7 Q1
Реализовать итератор, который бы "читал" заданный текст по параграфам. Символ параграфа задается отдельно
'''

class Paragraph:

    def __init__(self, txt, separator):
        self.txt = str(txt)
        self.par = ''
        self.sep = separator
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        nextp = self.txt.find(self.sep)
        if nextp == -1 and len(self.txt):
            self.par = self.txt
            self.txt = ''
            return self.par
        elif nextp >= 0 and len(self.txt):
            self.par = self.txt[:nextp]
            z = nextp + len(self.sep)
            self.txt = self.txt[z:]
            return self.par
        else:
            raise StopIteration


with open('P7_0.txt','r', encoding='utf-8') as file:
    test_file = file.read()
    for pp in Paragraph(test_file, '\n\n'): # Через цикл
        print(pp)
    # # p = Paragraph(test_file, '\n\n') # вызовами next() что приведет к исключению
    # print(p.par)
    # next(p)
    # print(p.par)
    # next(p)
    # print(p.par)
    # next(p)
    # print(p.par)
    # next(p)
    # print(p.par)
    # next(p)
    # print(p.par)
    # next(p)
    # print(p.par)
    # next(p)
    # print(p.par)



# Разминка Лекции №7 Q2
# Написать генератор для построчного чтения файла


def Read1Line(source):
    while source.readline() != 0:
        yield source.readline()


in_file = 'P7_0.txt'
with open(in_file,'r', encoding='utf-8') as file_to_read:
    print(next(Read1Line(file_to_read)))
    print(next(Read1Line(file_to_read)))
    print(next(Read1Line(file_to_read)))
    # print(next(Read1Line(file_to_read)))
    # print(next(Read1Line(file_to_read)))
    # print(next(Read1Line(file_to_read)))
