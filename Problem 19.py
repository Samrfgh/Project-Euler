def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def first_of_next_month(year, month):
    if month == 12:
        return (year + 1, 1, 1)
    else:
        return (year, month + 1, 1)

def is_last_day_of_month(year,month,day):
    return (month in [4,6,9,11] and day == 30) or (month in [1,3,5,7,8,10,12] and day == 31) or (month == 2 and ((is_leap_year(year) and day == 29) or (not is_leap_year(year) and day == 28)))

def next_day(current_day):
    (year, month, day) = current_day
    if is_last_day_of_month(year,month,day):
        return first_of_next_month(year,month)
    else:
        return (year, month, day + 1)

def day_list(start,finish):
    list1 = []
    current_day = start
    while current_day <= finish:
        list1.append(current_day)
        current_day = next_day(current_day)
    return list1

def daysoftheweek(x):
    days_of_the_week = []
    while len(days_of_the_week) < x:
        for i in range(1,8):
            days_of_the_week.append(i)
    return days_of_the_week

def sundays_on_first_of_month(start,finish):
    sundays = []
    x = day_list(start,finish)
    days = daysoftheweek(len(x))
    for i in range(len(x)):
        if x[i][2] == 1 and days[i - 1] == 7:
            sundays.append(i)
    return len(sundays)
print(sundays_on_first_of_month((1901,1,1),(2000,12,31)))
