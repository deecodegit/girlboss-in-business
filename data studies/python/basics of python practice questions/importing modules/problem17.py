"""
use the math module to:
1. find the square root of 81
2. round a number up and down
"""

import math

squareRoot = math.sqrt(int(input("Enter a number to find its square root: ")))
number = float(input("Enter a number to round up and down: "))

rounded_up = math.ceil(number)
rounded_down = math.floor(number)

print("Square root:", squareRoot)
print("Rounded up:", rounded_up)
print("Rounded down:", rounded_down)
