"""
convert a list of prices into a new list where each price is increased by 10%.
"""

prices = [100, 200, 300, 400, 500]

new_prices = [price + (price * 0.1) for price in prices]
print(new_prices)