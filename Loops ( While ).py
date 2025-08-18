age = int(input("Enter your age: "))
while age<=0 or age == "":
    print("Nigga type the correct age or you're gay or sum shit")
    age = int(input("Enter your age: "))
else:
    age = int(age)

name = str(input("Enter your name: "))
while name == "":
    print("Type your name or gay")
    name=input("Enter your name: ")
else:
    name = name

print(f"{name} is {age} years old")