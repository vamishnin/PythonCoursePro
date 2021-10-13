
def temp_replace(temptext, change_dict: dict):
    for i in change_dict.keys():
        temptext = temptext.replace(i, str(change_dict[i]))
    return temptext


rep_list = {'<name>': 'СуперЮзер666', '<system>': 'МегаОС'}
text = 'Имя пользователя <name> не зарегистрировано в системе <system>'
print(f'Форматная строка: {text}')
print(f'После замены: {temp_replace(text, rep_list)}')
