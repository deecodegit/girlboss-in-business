"""
sort a list of tuples based on the second value using lambda.
"""

products = [("shoe", 2000), ("tee", 800), ("jacket", 5000)]

sorted_products = sorted(products, key=lambda x: x[1])
print(sorted_products)