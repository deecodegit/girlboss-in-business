"""
given a number:
1. print "positive" if > 0
2. "negative" if < 0
3. "zero" if exactly 0
"""

import random

number = random.randint(-100, 100)
print(f"number: {number}")

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

# printing numbers is not necessary, it's just to maintain clarity in the output.