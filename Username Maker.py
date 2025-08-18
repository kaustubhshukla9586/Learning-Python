username = (input("Enter a valid username: "))

result_1 = len(username)
result_2 = username.isalpha()
result_3 = username.find(" ")

if result_1>12:
    print("Username cannot be more than 12 characters.")
elif not result_2:
    print("Username cannot contain digits or Spaces")
else:
    print(f"{username} is a valid username.")

