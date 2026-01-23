"""
write a function that takes a list of numbers and returns their average.
"""

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

nums = [10, 20, 30, 40, 50]
print(calculate_average(nums))