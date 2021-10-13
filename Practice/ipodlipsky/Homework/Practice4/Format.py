my_dict = {'{name}': 'Петр', '{surname}': 'Первый', '{who}':  'самый', '{which}': "первый"}
my_str = '{name} {surname} {who} {which}'

print(my_str)

for key, value in my_dict.items():
     my_str = my_str.replace(key, value)

print(my_str)



