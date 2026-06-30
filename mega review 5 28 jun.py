def calculate_discount(price, discount_percent=10):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price


print(calculate_discount(100))        # uses default 10%
print(calculate_discount(100, 20))    # uses 20% instead