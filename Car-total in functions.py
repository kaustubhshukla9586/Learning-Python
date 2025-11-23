def cart_total(discount, *args):
    total = sum(args)
    discount = (discount/100)*total
    final = total - discount
    print(f"Total before discount: ₹{total}")
    print(f"Discount ({discount}%): ₹{discount}:.2f")
    print(f"Final amount to pay: ₹{final:.2f}")


cart_total(20,1,2,2,3,3,4,3,3,4,5,6,9)
