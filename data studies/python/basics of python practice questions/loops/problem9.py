"""
given a list of prices:
prices = [499, 999, 1499, 1999]
print only the prices greater than 1000.
"""
prices = [499, 999, 1499, 1999]

# method 1 - simple for loop
for p in prices:
    if p > 1000:
        print(p)

# method 2 - list comprehension
prices_above_1000 = [p for p in prices if p > 1000]
print(prices_above_1000)

# method 3 - using filter()
print(list(filter(lambda x: x > 1000, prices)))

# method 4 - storing values in a new list
high_value_items = []

for p in prices:
    if p > 1000:
        high_value_items.append(p)

print(high_value_items)