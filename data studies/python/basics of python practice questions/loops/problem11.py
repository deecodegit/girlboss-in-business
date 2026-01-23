"""
using a while loop, print numbers from 10 down to 1.
"""
number = 10

# method 1 - simple while loop
while number >= 1:
    print(number)
    number -= 1

# method 2 - using cleaner code
number = 10
while number > 0:
    print(number)
    number -= 1

# method 3 - using boolean for python
number = 10
while number:
    print(number)
    number -= 1