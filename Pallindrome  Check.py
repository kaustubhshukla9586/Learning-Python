user = int(input("Enter a number or sentence to check Pallindrome: "))

if user == user[::-1]:
    print("")
else:
    print("Not Pallindrome")