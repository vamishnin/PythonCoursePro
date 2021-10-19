from datetime import datetime,timedelta


def count_of_weekdays(day1, day2, format):
    d1 = datetime.strptime(day1, format)
    d2 = datetime.strptime(day2, format)
    # return (d2 - d1).days
    daygenerator = (d1 + timedelta(d + 1) for d in range((d2 - d1).days))
    weekdays_count = 0
    for day in daygenerator:
        if day.weekday() < 5:
            weekdays_count += 1
    return weekdays_count
    
    
print(f'{count_of_weekdays("10/1/2021", "10/19/2021", "%m/%d/%Y")}')
