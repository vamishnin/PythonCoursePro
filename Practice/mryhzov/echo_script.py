user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_age = int(input('Введите возраст: '))
sex = input('Ваш пол (м/ж): ')
print('Неужели это {} {}?!'.format(user_name, user_surname))
print('Не виделись лет {}, со школы! '.format(user_age - 17))

if sex == 'м':
    print('Ну ты и разжирел!')
elif sex == 'ж':
    print('Отлично выглядишь!')
else:
    print('Ну мне пора.')


