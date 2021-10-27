import datetime as dt


def weekdays_counter(date1, date2):

    diff = abs(date1 - date2).days
    workdays = 0
    if date1 > date2:
        date1, date2 = date2, date1

    same_week = diff < 6 and date1.weekday() < date2.weekday()
    # учет рабочих дней первой недели из диапазона
    if 0 <= date1.weekday() < 5:
        diff -= 6 - date1.weekday()
        workdays += 5 - date1.weekday()
    # учет рабочих дней последней недели из диапазона

    if 0 <= date2.weekday() < 5 and not same_week:
        diff -= date2.weekday()
        workdays += date2.weekday() + 1 # + 1, так как включаем последнюю дату

    if diff >= 7:
        workdays += diff // 7 * 5
    print(f'between {date1.date()} and {date2.date()}  {workdays} workdays')


weekdays_counter(dt.datetime(2021, 9, 29), dt.datetime.now())

weekdays_counter(dt.datetime(2021, 9, 30), dt.datetime(2021, 10, 2))

weekdays_counter(dt.datetime(2021, 10, 2), dt.datetime(2021, 9, 30))

weekdays_counter(dt.datetime(2021, 10, 6), dt.datetime(2021, 9, 30))

weekdays_counter(dt.datetime(2021, 10, 1), dt.datetime(2021, 9, 30))
