"""
given:
numbers = [1, 2, 3, 4, 5, 6]
create a new list with only even numbers.
"""

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)