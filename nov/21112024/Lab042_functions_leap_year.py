#check leap year
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = 2019

if check_leap_year(year):
    print("yes")
else:
    print("no")