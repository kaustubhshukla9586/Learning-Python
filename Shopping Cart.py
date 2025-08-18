foods = []
prices = []

while True:
    food = input("What food do you want to buy? (q to quit): ")
    if food.lower() == "q":
        break
    price = float(input(f"Enter the price of {food}: "))
    foods.append(food)
    prices.append(price)

if not foods:
    print("\nYour cart is empty 🛒")
else:
    total = 0.0
    i = 1
    idx = 0
    print("\n-------- Y O U R   C A R T --------")


    while idx < len(foods):
        print(f"{i}. {foods[idx]:<15} ₹{prices[idx]:>9.2f}")
        total += prices[idx]
        i += 1
        idx += 1

    print(f"\nTotal price: ₹{total:.2f}")
