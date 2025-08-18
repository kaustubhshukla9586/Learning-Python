import math

r = float(input("Enter the radius of the circle: "))
calc = str(input("Enter what do you want to calculate ( area / circumference ): "))

area = math.pi * pow(r, 2)
circumference = 2 * math.pi * r
Circumference = round(circumference)

if calc == "area":
    print(f"{round(area, 2)}cm^2")
else:
    print(f"{round(circumference, 2)}cm")
