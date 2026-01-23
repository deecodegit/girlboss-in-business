"""
given:
names = ["apple", "banana", "cherry"]
create a dictionary where keys are names and values are their lengths.
"""
names = ["apple", "banana", "cherry"]

name_length_dict = {name: len(name) for name in names}
print(name_length_dict)
