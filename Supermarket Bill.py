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

    # width settings
    name_width = max(len(f) for f in foods)
    price_width = 10
    table_width = name_width + price_width + 12   # total line width

    print("\n" + "🧾 SUPERMARKET BILL 🧾".center(table_width))
    print("-" * table_width)
    print(f"{'No.':<4} {'Item':<{name_width}} {'Price':>{price_width}}".center(table_width))
    print("-" * table_width)

    while idx < len(foods):
        line = f"{i:<4} {foods[idx]:<{name_width}} ₹{prices[idx]:>{price_width-1}.2f}"
        print(line.center(table_width))
        total += prices[idx]
        i += 1
        idx += 1

    print("-" * table_width)
    print(f"TOTAL: ₹{total:.2f}".center(table_width))
    print("-" * table_width)
