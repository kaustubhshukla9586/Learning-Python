principal_amount = int(input("Enter your principal amount: "))

while principal_amount <= 0:
    print("Principal amount cannot be less than or equal to zero")
    principal_amount = int(input("Enter your principal amount: "))

interest_rate = float(input("Enter your interest rate: "))

while interest_rate <= 0:
    print("Interest rate cannot be less than or equal to zero")
    interest_rate = float(input("Enter your interest rate: "))

time = int(input("Enter your time of the loan period in years: "))

while time <= 0:
    print("Time cannot be less than or equal to zero")
    time = int(input("Enter your time in years: "))

type = (input("Are you calculating the interest rate? (Y/N): "))

total_amount = principal_amount * pow((1 + interest_rate / 100), time)
compound_interest = total_amount - principal_amount

if type == "Y":
    print(f"Total Amount after {time} years: {total_amount:.2f}")
    print("The compound interest is:", compound_interest)

