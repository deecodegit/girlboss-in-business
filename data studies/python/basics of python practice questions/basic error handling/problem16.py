"""
convert user input into an integer safely.
if conversion fails, print "invalid number".
"""

user_input = input("Enter a number: ")
try:
    number = int(user_input)
    print(f"You entered the number: {number}")
except ValueError:
    print("invalid number")
