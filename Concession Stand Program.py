menu = {
    "Pizza": 249,
    "Burger": 149,
    "Pasta": 199,
    "Sandwich": 99,
    "Cold Coffee": 129
}

total = 0

print("Menu:")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

while True:
    item = input("\nEnter item (q to quit): ").title()
    if item == "Q":
        break
    if item not in menu:
        print("Not in menu, try again.")
        continue

    qty = int(input(f"Enter quantity of {item}: "))
    total += menu[item] * qty
    print(f"Added {qty} {item}(s), Subtotal = ₹{total}")

print("\nYour total bill = ₹", total)
