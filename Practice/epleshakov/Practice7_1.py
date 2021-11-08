#Написать функцию для подсчета количества рабочих дней между двумя датами (даты передаются в качестве параметров).
from datetime import date, timedelta


def work_dates(date_a, date_b):
    date_gen = (date_a + timedelta(x + 1) for x in range((date_b - date_a).days))
    num_wrk_days = sum(1 for day in date_gen if day.weekday() < 5)
    if date_a.weekday() < 5:  # Добавляем еще единицу если начальная дата тоже рабочий день
        num_wrk_days += 1     # можно конечно и не считать данный день ))
    return num_wrk_days


d1 = date(2021, 10, 29)
d2 = date(2021, 11, 7)
print(f'Между {d1} и {d2} {work_dates(d1, d2)} рабочих дней включительно')
