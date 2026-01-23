"""
create a Product class with:
1. name
2. price
3. add a method that applies a discount and updates the price.
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def final_price(self):
        updated_price = self.price - (self.price * 0.1)
        print(updated_price)

p1 = Product("soap", 50)
p2 = Product("vegetable oil", 180)

print(f"discounted price of {p1.name} (originally {p1.price}) is: ")
p1.final_price()

print(f"discounted price of {p2.name} (originally {p2.price}) is: ")
p2.final_price()