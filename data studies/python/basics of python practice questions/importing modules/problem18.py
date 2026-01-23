"""
use the random module to:
1. pick a random number between 1 and 100
2. pick a random item from a list
"""

import random

random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

items = ['apple', 'banana', 'cherry', 'date', 'elderberry'] 
random_item = random.choice(items)
print(f"Random item from the list: {random_item}")
