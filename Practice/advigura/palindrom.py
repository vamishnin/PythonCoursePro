word = input('enter your word: ')

is_palindrom = True
for i in range(len(word) // 2):
    if not word[i] == word[len(word) - i - 1]:
         # print(f'ok')
         is_palindrom = False
         break
if is_palindrom:
    print('it is palindrom!')
else:
    print('it is not palindrom')