"""
given: price = 1499 and gst_rate = 0.18
calculate the final price including gst and store it in a new variable.
"""

price = 1499
gst_rate = 0.18

# method 1 - using a single expression
final_price_m1 = price + (price * gst_rate)
print(final_price_m1)

# method 2 - calculating gst_amount first as a new variable and then using expressions
gst_amount = price * gst_rate
final_price_m2 = price + gst_amount
print(final_price_m2)

# method 3 - usinf functions
def final_price_m3(price, gst_rate):
    return price + (price * gst_rate)
print(final_price_m3(1499, 0.18))