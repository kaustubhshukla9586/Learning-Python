low = int(input("Enter the lower range: "))
high = int(input("Enter the higher range: "))

for num in range(low, high + 1):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    armstrong_sum = sum(d ** power for d in digits)

    if num == armstrong_sum:
        print(num)