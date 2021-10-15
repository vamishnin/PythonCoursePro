# Реализовать итератор, который бы "читал" заданный текст по параграфам. Символ параграфа задается отдельно

class ParagraphIter:

    def __init__(self, file, paragraph_symbol):
        self.__file = file
        self.__paragraph_symbol = paragraph_symbol

    def __iter__(self):
        return self

    def __next__(self):
        buffer = ''
        buffer_sent = False
        while True:
            sym = self.__file.read(1)

            if buffer_sent:
                buffer = ''
            # на случай, если символ параграфа состоит из нескольких символов,
            # находим конец предыдущего параграфа
            if buffer[len(buffer) - len(self.__paragraph_symbol):len(buffer)] == self.__paragraph_symbol:
                buffer_sent = True
                # возврашаем тект параграфа без символа параграфа
                if len(buffer[:len(buffer) - len(self.__paragraph_symbol)]) != 0:
                    return buffer[:len(buffer) - len(self.__paragraph_symbol)]
            else:
                buffer_sent = False
                buffer += sym

            if not sym:
                # вернем последний текст параграфа перед концом файла
                if len(buffer) != 0:
                    return buffer
                raise StopIteration


with open('text_P.txt', 'r') as f:
    p = ParagraphIter(f, 'Paragraph')
    try:
        print(next(p))
        print(next(p))
        print(next(p))
        print(next(p))
    except StopIteration:
        print('Too much "next" command')

