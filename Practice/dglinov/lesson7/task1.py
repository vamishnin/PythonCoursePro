'''
Написать функцию для подсчета количества рабочих дней между двумя датами (даты передаются в качестве параметров).
'''
import datetime

def gen_days(date_start, date_end):
    a = datetime.datetime.strptime(date_start, '%d.%m.%Y')
    b = datetime.datetime.strptime(date_end, '%d.%m.%Y')
    while a <= b:
        yield a
        a += datetime.timedelta(days = 1)

def bad_days_count(date_start, date_end):
    '''
    Подсчет кол-ва рабочих дней между указанными датами в формате %d.%m.%Y
    Не учитывает кол-во переносов праздничных дней на рабочую неделю
    '''
    bad_days = 0
    happy_days = [5,6]
    new_year_holydays = [each for each in range(1,11)]
    
    rf_holidays = [
        '23.02',
        '08.03',
        '01.05',
        '09.05',
        '12.06',
        '04.11',
    ]
    
    for i in gen_days(date_start, date_end):
        if i.weekday() in happy_days:
            continue
        elif i.month == 1 and i.day in new_year_holydays:
            continue
        elif i.strftime('%d.%m') in rf_holidays:
            continue
        else:
            bad_days += 1

    return bad_days


if __name__ == '__main__':
    #В 2021 году 365 календарных дней, при этом рабочих — 243, праздничных, выходных и нерабочих — 122.
    print(f'Рабочих дней с 01.01.2021 по 31.12.2021 - {bad_days_count("01.01.2021","31.12.2021")}')
    
    print(f'Рабочих дней с 01.10.2021 по 20.10.2021 - {bad_days_count("01.10.2021","20.10.2021")}')