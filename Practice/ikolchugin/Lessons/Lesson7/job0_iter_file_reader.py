

class ParagraphIter:

    def __init__(self, txt, eop='\t'):
        self._eop = eop
        self._txt = txt
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self._txt):
            res = []
            while self._i < len(self._txt) and self._txt[self._i] != self._eop:
                res.append(self._txt[self._i])
                self._i += 1
            self._i += 1
            return ''.join(res).strip('\n')
        else:
            raise StopIteration


example_txt = """Реализовать итератор,
\tкоторый бы "читал" заданный текст по параграфам. 
\tСимвол параграфа задается отдельно
"""

for p in ParagraphIter(example_txt):
    print(p)

#Генератор построкового чтения файла
def readfile_gen(filename):
    with open(filename, 'r') as f:
        while _line := f.readline():
            yield _line


for line in readfile_gen(__file__):
    print(line)
