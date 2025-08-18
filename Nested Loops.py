
rows = int(input("How many rows do you want? "))
columns = int(input("How many columns do you want? "))
symbol = input("Enter the symbol you want:  ")


for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()