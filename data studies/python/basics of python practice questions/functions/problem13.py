"""
write a function that takes a price and discount percentage, and returns the final price.
"""

price = int(input("Enter the price: "))
discount = int(input("Enter the discount percentage: "))

# method 1 - direct function
def final_price_m1(p, d):
    return p - (p * (d / 100))

print(final_price_m1(price, discount))

# method 2 - using a new variable
def final_price_m2(p, d):
    discount_amount = p * (d / 100)
    return p - discount_amount

print(final_price_m2(price, discount))

# method 3 - defensive programming
price = float(input("Enter the price: "))
discount = float(input("Enter the discount percentage: "))

def final_price_m3(p, d):
    if p < 0:
        raise ValueError("Price cannot be negative")
    if 0 > d or d > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    return p - (p * (d / 100))