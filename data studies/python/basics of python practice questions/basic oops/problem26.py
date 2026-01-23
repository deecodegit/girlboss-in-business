"""
build a tiny system that:
1. stores products in a list
2. prints only products above a certain price
3. uses a function for filtering
4. uses a loop to display results
5. handles invalid input gracefully
"""

class Product:
    shop = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.shop.append(self)

    def display_info(self):
        print(f"product name: {self.name}, price: {self.price}")

    @classmethod
    def filter_products_by_price(cls, min_price):
        return [product for product in cls.shop if product.price > min_price]
    
    @staticmethod
    def handle_filter():
        choice = input("do you want to filter products by price? (yes/no): ").strip().lower()

        if choice == "yes":
            try:
                min_price = float(input("enter minimum price: "))
                filtered_products = Product.filter_products_by_price(min_price)

                if not filtered_products:
                    print("no products found above that price.")
                else:
                    print("\nfiltered products:")
                    for product in filtered_products:
                        product.display_info()
            except ValueError:
                print("invalid price entered.")

# user input to add products
while True:
    name = input("enter product name (or type 'exit' to stop): ").strip()

    if name.lower() == "exit":
        break

    if not name:
        print("error: product name cannot be empty.")
        continue

    try:
        price = float(input("enter product price: "))
        if price <= 0:
            print("error: price must be greater than 0.")
            continue
    except ValueError:
        print("error: please enter a valid number for price.")
        continue

    Product(name, price)
    print("product added successfully.\n")

# user input to display
choice = input("do you want to see all products? (yes/no): ").strip().lower()

if choice == "yes":
    if not Product.shop:
        print("no products in the shop.")
    else:
        print("\nproducts in shop:")
        for product in Product.shop:
            product.display_info() 
    Product.handle_filter()
else:
    Product.handle_filter()