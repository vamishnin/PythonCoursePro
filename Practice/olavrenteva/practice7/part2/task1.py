import datetime as dt


def work_days_between(date1, date2):
    """
    The function takes two dates and returns a number of working days between them (including both date1 and date2).
    date2 is supposed to be not earlier than date1.
    """
    if date2 < date1:
        raise ValueError("Incorrect values passed: first passed date should not be later than second date")

    days = (date2 - date1).days
    date1_week = date1.isoweekday()
    date2_week = date2.isoweekday()
    work_days = 5 * (days // 7) + min(date2_week, 5) - min(date1_week, 5) + (1 if date1_week <= 5 else 0) + \
                (5 if date1_week > date2_week else 0)

    return work_days


date1 = dt.date(2021, 9, 30)
date2 = dt.date(2021, 10, 5)
print(f'{work_days_between(date1, date2)} working day(s) between {date1} and {date2}')

date1 = dt.date(2021, 9, 30)
date2 = dt.date(2021, 10, 8)
print(f'{work_days_between(date1, date2)} working day(s) between {date1} and {date2}')

date1 = dt.date(2021, 9, 30)
date2 = dt.date(2021, 10, 18)
print(f'{work_days_between(date1, date2)} working day(s) between {date1} and {date2}')

date1 = dt.date(2021, 10, 2)
date2 = dt.date(2021, 10, 11)
print(f'{work_days_between(date1, date2)} working day(s) between {date1} and {date2}')
