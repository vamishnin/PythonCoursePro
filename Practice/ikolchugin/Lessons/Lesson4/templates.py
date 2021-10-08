animals = {
    'dog': 'собака',
    'cat': 'кошка',
    'fox': 'лиса'
}

# {{ tag }} в строке нужно заменить на animals[tag]
text = '{{ dog }} - друг человека, а вот {{ cat }} это вам не {{ dog }},' \
      ' хотя тоже вроде бы домашняя.\n{{ fox }} - что-то среднее,' \
       ' и ни {{ dog }}, и ни {{ cat }}.'


for tagname, animal in animals.items():
    text = text.replace(f'{{{{ {tagname} }}}}', animal)


print(text)
