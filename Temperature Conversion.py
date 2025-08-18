temp = float(input("Enter the temperature in Celsius / Fahrenheit: "))
unit = str(input("Enter the unit of the temperature (C/F): ")).upper()

if unit == "C":
    result = (temp * 9 / 5 ) + 32
    print(f"Your converted temperature is {result} Fahrenheit" )
elif unit == "F":
    result = ( temp - 32 )* 5/9
    print(f"Your converted temperature is {result} Celsius" )
else:
    print("Invalid input.")
