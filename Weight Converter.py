import math

weight = float(input("Enter your weight in kilograms or pounds : "))
output = str(input("Choose in which you want to convert( kg / lbs ) : "))

if output == "kg":   #converts lbs to kg
    result = round((weight / 2.205), 2)
    unit = "kilograms"
elif output == "lbs":    #converts kg to lbs
    result = round((weight * 2.205), 2)
    unit = "pounds"
else:
    print("Invalid input.")
    unit = "unknown"

if unit == "kilograms" or unit == "pounds":
    print(f"Your converted weight is {result} {unit}" )
