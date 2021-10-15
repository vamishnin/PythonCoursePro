class ReadParagraph:
    def __init__(self, filepath, sep='\n'):
        self._filepath = filepath
        self._sep = sep
        self._position = 0

    def __iter__(self):
        return self

    def __next__(self):
        paragraph = ''

        with open(self._filepath, 'r') as file:
            file.seek(self._position)
            char = file.read(1)

            if not char:
                raise StopIteration

            while char and (char != self._sep or char == self._sep and paragraph == ''):
                if char != self._sep:
                    paragraph = paragraph + char
                char = file.read(1)

            self._position = file.tell()
            return paragraph


num = 0
for each in ReadParagraph('for_tasks_1_2', '$'):
    num += 1
    print(f'paragraph {num}: {each}')
