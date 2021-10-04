user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_age = int(input('Введите возраст: '))
user_sex = input('Ваш пол (м/ж): ')
print(f'Неужели это {user_name} {user_surname}?!')
print(f'Не виделись со школы, лет {user_age - 17}!')

if user_sex == 'м':
    print('Ну ты и разжирел!')
elif user_sex == 'ж':
    print('Отлично выглядишь!')
else:
    print('Ну мне пора.')







