from sqlalchemy.sql.expression import false
word = input('enter your word: ')

is_palindrom = True
for i in range(0, word.__len__()):
    if not word[i] == word[word.__len__() - i - 1]:
         # print(f'ok')
         is_palindrom = False
         break
if is_palindrom:
    print('it is palindrom!')
else:
    print('it is not palindeom')