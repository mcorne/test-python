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

def DaysInMonth2(year,month):
    if month not in range(1, 13) or year < 0:
        return
        
    length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = length[month-1]
    
    if month == 2 and IsYearLeap(year):
        day += 1
        
    return day

testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
	yr = testyears[i]
	mo = testmonths[i]
	print(yr,mo,"->",end="")
	result = DaysInMonth2(yr,mo)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")