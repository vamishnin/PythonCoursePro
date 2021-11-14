import datetime

def wdc(date1, date2):
    # В задании не указано, считаю, что рабочие дни между датами,
    # включая крайние значени
    # Определяем более раннюю дату
    if date1 > date2:
        date1, date2 = date2, date1
    # итого получим что date2 больше (позже) чем date1 (ранняя неделя)

    diff_date_count = date2 - date1
    diff_date = (date2 - date1).days
    wdate2 = date2.isoweekday()  # инд дня последней недели
    wdate1 = date1.isoweekday()  # инд дня ранней недели
    wday = 0
    if diff_date >= 7:
        wday = (diff_date // 7) * 5  # число рдней целых недель
        diff_date = diff_date % 7

    if 0 <= diff_date < 7:
         if wdate2 < wdate1:  # если дни попали на разные недели
             wday += max(6 - wdate1, 0) + min(wdate2, 5)
         else:  # дни попали на одну неделю
             wday += 6 - wdate1 + min(wdate2, 5) - 5

    print(f'allday different = {diff_date_count.days}, have {wday} workday')


# даты указываются в формате (ГГГГ, ММ, ДД)
wdc(datetime.datetime(2021, 11, 10), datetime.datetime(2021, 11, 3))
wdc(datetime.datetime(2020, 11, 17), datetime.datetime(2021, 11, 17))
# выходные
wdc(datetime.datetime(2021, 11, 27), datetime.datetime(2021, 11, 27))
wdc(datetime.datetime(1, 1, 1), datetime.datetime.now())
wdc(datetime.datetime(1, 1, 1), datetime.datetime(2022, 11, 14))
# рдень
wdc(datetime.datetime(2021, 11, 26), datetime.datetime(2021, 11, 26))
#wdc(datetime.datetime(2021, 11, 36), datetime.datetime(2021, 11, 26))
# исключения не будет, надо правильно писать даты:-)
