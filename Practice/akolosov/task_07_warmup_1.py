class ReadParagraph:

    def __init__(self, text: str, paragraph: str):
        self.__text = text
        self.__paragraph = paragraph

    def __iter__(self):
        self.__current = 0
        return self

    def __next__(self):
        if self.__current >= len(self.__text):
            raise StopIteration
        else:
            res = self.__text.find(self.__paragraph, self.__current)
            cur = self.__current
            if res == -1:
                self.__current = len(self.__text)
            else:
                # The next paragraph begins with the next character after paragraph character
                # If the paragraph character is the last character then it is the last iteration
                # because res + 1 == len(text)
                self.__current = res + 1
            return self.__text[cur: self.__current]


if __name__ == "__main__":
    s = ReadParagraph("Abra abracadabra\nI wanna reach out and grab ya\nAbracadabra\nAbracadabra", "\n")
    for i, p in enumerate(s):
        print(f"Paragraph {i+1}: {p}")

    s = ReadParagraph("Abra abracadabra\nI wanna reach out and grab ya\nAbracadabra\nAbracadabra\n", "\n")
    for i, p in enumerate(s):
        print(f"Paragraph {i+1}: {p}")
