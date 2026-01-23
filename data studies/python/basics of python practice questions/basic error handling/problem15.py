"""
ask the user for two numbers and divide them.
handle the case where the second number is 0.
"""

def divide_numbers():
    try:
        num1 = float(input("enter the first number: "))
        num2 = float(input("enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("error: cannot divide by zero.")
    except ValueError:
        print("error: please enter valid numbers.")
    else:
        print(f"the result is {result}")

divide_numbers()