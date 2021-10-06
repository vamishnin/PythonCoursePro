personal_data = {'{name}': 'Olga', '{surname}': 'Lavrenteva', '{city}': 'Saint-Petersburg'}
string = '{name} {surname} lives in {city}'

for key, value in personal_data.items():
    string = string.replace(key, value)

print(string)
