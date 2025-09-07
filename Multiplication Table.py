#multiplication table
#example output - 2 * 2 = 4
import time

num = int(input("Enter the number of which you want table of: "))

i = 1

for i in range(1,11):
    print(f"{num} * {i} = {num * i}")
    i += 1
    time.sleep(.5)
