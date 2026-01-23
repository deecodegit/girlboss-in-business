"""
create a dictionary for a product with:
1. name
2. category
3. price
4. in_stock (boolean)
print only the price and stock status.
"""

product = {"name": "soap", "category": "kitchen", "price": 50, "in_stock": True}

# method 1 - using .get method
print(f"Price: {product.get('price')}, Stock status: {product.get('in_stock')}")

# method 2 - direct access by key
print(f"Price: {product['price']}, Stock status: {product['in_stock']}")

# method 3 - using new variable to make boolean value more human-friendly
stock_status = "in stock" if product["in_stock"] else "out of stock"
print(f"price: {product['price']}, stock status: {stock_status}")
