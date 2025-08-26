num = int(input("Enter a number: "))
number = []
for n in range(2, num+1):
    for m in range(2, n):
        if n % m == 0:
             break
    else:
        number.append(n)
print(number)








