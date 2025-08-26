p = int(input("Enter the principal amount: "))
r = float(input("Enter the interest rate: "))
t = int(input("Enter the time in years: "))

si = (p * r * t)/100
print(f"The simple interest is: {si}.")
print(f"You end balance would be {p + si}.")

