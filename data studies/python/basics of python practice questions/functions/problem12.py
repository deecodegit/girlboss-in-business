"""
write a function that takes a number and returns its square.
"""
# method 1 - simple function
number = int(input("Enter a number: "))

def square_m1(number):
    return number * number

print(square_m1(number))

# method 2 - cleaner global function
def square_m2(n):
    return n * n

num = int(input("Enter a number: "))
print(square_m2(num))

# method 2 - optimised mathematical function
def square_m3(n):
    return n ** 2

num = int(input("Enter a number: "))
print(square_m3(num))