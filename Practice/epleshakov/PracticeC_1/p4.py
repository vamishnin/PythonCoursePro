# Написать функцию to_title: принимает строку, ищет пробелы,
# первые буквы после них и после начала строки делает заглавными.
def to_title2(txt):
    all_words = txt.split(' ')
    words = []
    for word in all_words:
        wrds_upper = word[0].upper() + word[1:]
        words.append(wrds_upper)
    return ' '.join(words)


# to_title2('orlov Ilya evgenyevich')
# print(to_title2(' orlov Ilya evgenyevich'))

# Вторая, поправленная версия
def to_title(txt: str):
    titled = ' '.join(word[0].upper() + word[1:] for word in txt.split())
    return titled


print(to_title('orlov Ilya evgenyevich'))
print(to_title(' orlov ilya evgenyevich'))