import datetime

def leap_year(year):
    if year % 400 == 0 and (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

def dayinprogrammer(year):
    day = datetime.date(year=year,month=1,day=1)
    result = day + datetime.timedelta(days = 256)
    return result

print(dayinprogrammer(2017))

