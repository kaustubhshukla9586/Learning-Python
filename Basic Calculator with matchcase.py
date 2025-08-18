num_1 = int(input("Enter Number 1:"))
num_2 = int(input("Enter Number 2:"))
operation = input("Put your operation you want to do (+, -, *, /):")

match operation:
    case "+":
        print(f"The addition of your numbers is {num_1} + {num_2} = {num_1 + num_2}")
    case "-":
        print(f"The Subtraction of your numbers is {num_1} - {num_2} = {num_1 - num_2}")
    case "*":
        print(f"The Multiplication of your numbers is {num_1} * {num_2} = {num_1 * num_2}")
    case "/":
        print(f"The Divison of your numbers is {num_1} / {num_2} = {num_1 / num_2}")
    case _:
        print("Invalid Operator")