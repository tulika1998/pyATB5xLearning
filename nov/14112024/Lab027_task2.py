#Checking for a Leap Year , 2024 → Yes
year = int(input("enter the year\n"))
if year % 4 == 0 and year % 100 != 0:
    print("year", "is a leap year")
elif year % 100 == 0:
    print ("year", "is not a leap year")
elif year % 400 == 0:
    print ("year", "is a leap year")
else:
    print("year", "not a leap year")

