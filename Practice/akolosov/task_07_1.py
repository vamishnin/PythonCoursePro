import datetime as dt


def calculate_working_days(begin, end):
    """
    Calculate days Monday-Friday and not calculate Saturday and Sunday
    Calculate working days between two dates (begin and end are not included):
      between yesterday and today is always 0
      between yesterday and tomorrow may be 1 working day - today
    """
    if isinstance(begin, str):
        try:
            begin = dt.date.fromisoformat(begin)
        except ValueError:
            return None
    elif not isinstance(begin, dt.date):
        return None

    if isinstance(end, str):
        try:
            end = dt.date.fromisoformat(end)
        except ValueError:
            return None
    elif not isinstance(end, dt.date):
        return None

    if begin > end:
        begin, end = end, begin

    days = (end - begin).days - 1 # because begin and end are not included in calculation
    week_day = (begin + dt.timedelta(days=1)).isoweekday() # the day of week of the first calculated day
    rest_days = days % 7 # = days - days_of_full_weeks
    rest_days_weekend = 0 # How many nonworking days in rest_days
    if week_day <= 6 < week_day + rest_days: # rest_days contain Saturday
        rest_days_weekend += 1
    if week_day <= 7 < week_day + rest_days: # rest_days contain Sunday
        rest_days_weekend += 1
    
    return (days // 7) * 5 + rest_days - rest_days_weekend


if __name__ == "__main__":
    begin = dt.date.today() - dt.timedelta(days=1)
    end = dt.date.today() + dt.timedelta(days=1)
    print(f"Working days between {begin} and {end} is : {calculate_working_days(begin, end)}")

    begin = "2020-01-01"
    end = "2021-01-01"
    print(f"Working days between {begin} and {end} is : {calculate_working_days(begin, end)}")

    begin = "2021-10-22"
    end = "2021-10-25"
    print(f"Working days between {begin} and {end} is : {calculate_working_days(begin, end)}")
    
    begin = "2021-10-17"
    end = "2021-10-23"
    print(f"Working days between {begin} and {end} is : {calculate_working_days(begin, end)}")
