import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice = int(input("Enter 1 for HCF, 2 for LCM: "))

if choice == 1:
    print("HCF:", math.gcd(a, b))
elif choice == 2:
    print("LCM:", math.lcm(a, b))
else:
    print("Invalid choice")
