class ReadParagraph:
    def __init__(self, filepath, sep='\n'):
        self._sep = sep
        self._position = 0
        self._file = open(filepath, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        paragraph = ''

        self._file.seek(self._position)
        char = self._file.read(1)

        if not char:
            raise StopIteration

        while char and (char != self._sep or char == self._sep and paragraph == ''):
            if char != self._sep:
                paragraph = paragraph + char
            char = self._file.read(1)

        self._position = self._file.tell()
        return paragraph

    def __del__(self):
        self._file.close()


num = 0
for each in ReadParagraph('for_tasks_1_2', '$'):
    num += 1
    print(f'paragraph {num}: {each}')
