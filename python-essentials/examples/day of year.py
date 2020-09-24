def IsYearLeap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def DaysInMonth(year,month):
    if month not in range(1, 13) or year < 0:
        return
        
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month != 2:
        days = 30
    elif IsYearLeap(year):
        days = 29
    else:
        days = 28
    
    return days

def DayOfYear(year,month,day):
    days = 0
    for i in range(month - 1):
        days += DaysInMonth(year, i + 1) + day
        
    return days

print(DayOfYear(2000,1,2))
