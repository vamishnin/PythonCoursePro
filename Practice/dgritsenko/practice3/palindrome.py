def is_palidrome(word):
    if not(isinstance(word, str)):
        return False

    i = 0
    while i < len(word):
        if word[i] != word[-i - 1]:
            return False
        i += 1
    return True

word = 'topot'
print(f"{word} {'is' if is_palidrome(word) else 'is not'} palindrome")