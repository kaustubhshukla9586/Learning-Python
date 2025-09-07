import calendar

month = int(input("Enter month: "))
year = int(input("Enter year: "))
cal = calendar.month(year, month)

print(cal)