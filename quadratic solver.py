import math

print("The standard form of Quadratic Equation is - ax^2 + bx + c = 0")

# Ensure a != 0
while True:
    a = float(input("Enter the value of a: "))
    if a != 0:
        break
    print("The value of a cannot be 0, please re-enter.")

b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Discriminant
discriminant = (b ** 2) - (4 * a * c)

# Root calculation
if discriminant > 0:  # Two real & distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("The 1st root of the equation is", root1)
    print("The 2nd root of the equation is", root2)

elif discriminant == 0:  # One real root
    root = -b / (2 * a)
    print("The root of the equation is", root)

else:  # Complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
    print(f"Root 1 : {real_part} + {imaginary_part}i")
    print(f"Root 2 : {real_part} - {imaginary_part}i")
