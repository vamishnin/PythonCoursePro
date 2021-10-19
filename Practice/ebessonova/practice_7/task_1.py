import datetime as dt  # оптимальный способ импорта datetime


def weekdays_counter(date1, date2):

    diff = abs(date1 - date2).days
    workdays = 0
    # учет рабочих дней первой недели из диапазона
    if 0 <= date1.weekday() < 5:
        diff -= 6 - date1.weekday()
        workdays += 5 - date1.weekday()
    # учет рабочих дней последней недели из диапазона
    if 0 <= date2.weekday() < 5:
        diff -= date1.weekday()
        workdays += date2.weekday()

    workdays += diff // 7 * 5
    print(f'between {date1.date()} and {date2.date()}  {workdays} workdays')


weekdays_counter(dt.datetime(2021, 9, 29), dt.datetime.now())
