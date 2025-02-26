secondsInDay=24 * 60 * 60

print("How many seconds are in a year")
year = int(input("Enter the year "))

isLeapYear = year % 4 == 0
# ternary operator
daysInYear = 366 if isLeapYear else 365

secondsInYear = daysInYear * secondsInDay

print(f"Year {year} has {secondsInYear} seconds")