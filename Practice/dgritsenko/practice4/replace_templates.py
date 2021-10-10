data_text = "Времы работы с {time_from_hours} до {time_till_hours} часов, выходные дни {holiday_1} и {holiday_2}."

templates_set = {'time_from_hours': '9.00',
                 'time_till_hours': '18.00',
                 'holiday_1': 'воскресенье',
                 'holiday_2': 'понедельник'}

for t in templates_set:
    data_text = data_text.replace('{' + t + '}', templates_set[t])

print(data_text)


