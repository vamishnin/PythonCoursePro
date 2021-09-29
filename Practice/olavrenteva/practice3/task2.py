def if_palindrom(word: str):
    word = word.lower()
    len_word = len(word)
    if len_word >= 2:
        for i in range(len(word)//2):
            if word[i] != word[len(word) - 1 - i]:
                return False
    return True


print(f'" " is palindrom: {if_palindrom("")}')
print(f'"a" is palindrom: {if_palindrom("a")}')
print(f'"aa" is palindrom: {if_palindrom("aa")}')
print(f'"ab" is palindrom: {if_palindrom("ab")}')
print(f'"abA" is palindrom: {if_palindrom("abA")}')
print(f'"abc" is palindrom: {if_palindrom("abc")}')
print(f'"abba" is palindrom: {if_palindrom("abba")}')
print(f'"abab" is palindrom: {if_palindrom("abab")}')
print(f'"Топот" is palindrom: {if_palindrom("Топот")}')
print(f'"Довод" is palindrom: {if_palindrom("Довод")}')
print(f'"a b c c b a" is palindrom: {if_palindrom("a b c c b a")}')
