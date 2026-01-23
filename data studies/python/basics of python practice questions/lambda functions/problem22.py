"""
write a lambda function that checks if a number is even.
"""

import random
number = random.randint(1, 100)
print(number)

is_even = lambda x: x % 2 == 0

print(is_even(number))  