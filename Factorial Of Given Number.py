num = int(input("Enter a number: "))
if num == 0:
    print("0 doesnt have a factorial")
elif num<1:
    print("Factorial does not exist for Negative Numbers")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(factorial)




