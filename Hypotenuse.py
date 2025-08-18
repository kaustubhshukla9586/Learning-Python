import math

a = float(input("Enter the length of a: "))
b = float(input("Enter the length of b: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"{round(c, 2)}cm^2")