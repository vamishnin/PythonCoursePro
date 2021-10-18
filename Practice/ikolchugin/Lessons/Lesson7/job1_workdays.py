import datetime as dt


# считаем рабочими дни с понедельника по пятницу включительно.
# начальная и конечная даты включаются в диапазон подсчёта рабочих дней.
def work_days_cnt(start_date, end_date):
    t_date = start_date
    res = 0
    while t_date <= end_date:
        if t_date.weekday() < 5:
            res += 1
        t_date += dt.timedelta(days=1)
    return res


# Если кому-то понадобятся даты рабочих дней, то генератор в помощь
def gen_work_days_cnt(start_date, end_date):
    t_date = start_date
    while t_date <= end_date:
        if t_date.weekday() < 5:
            yield t_date
        t_date += dt.timedelta(days=1)


# Начальные и конечные даты можно задать вот так
st_date = dt.datetime(2021, 10, 5, 0, 0)
end_date = dt.datetime(2021, 10, 10, 0, 0)

# или так:
# st_date = dt.datetime.strptime('2021-10-05', '%Y-%m-%d')
# end_date = dt.datetime.strptime('2021-10-10', '%Y-%m-%d')

# Печатаем количество рабочих дней.
print(f'Количество рабочих дней от {st_date} до {end_date} включительно - {work_days_cnt(st_date, end_date)}')

# если выбран вариант с  генератором, то вот так печатаем
# print(f'Количество рабочих дней между {st_date} и {end_date} - '
#      f'{len(tuple(gen_work_days_cnt(st_date, end_date)))}')

# даты печатаем, если есть необходимость
for i in gen_work_days_cnt(st_date, end_date):
    print(i.strftime('%Y-%m-%d'))
