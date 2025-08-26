num = int(input("Enter a number: "))

if num == 0:
    print("Number is neither odd nor even.")
elif num % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")
