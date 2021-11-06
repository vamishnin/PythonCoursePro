import datetime as dt


def count_work_days(d1, d2):
    days = (d2 - d1).days
    data_1 = d1.isoweekday()
    data_2 = d2.isoweekday()
    work_days = 5 * (days // 7) + min(data_2, 5) - min(data_1, 5) + (5 if data_1 > data_2 else 0) + \
                (1 if data_1 <= 5 else 0)
    return work_days


start = dt.date(2021, 10, 24)
end = dt.date(2021, 10, 30)
res = count_work_days(start, end)
print(f'Между {start} и {end} - {res} рабочих дней.')



