year = int(input("Enter year: "))

if (year % 400 == 0) and (year % 100 != 0):
    print("Leap Year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")