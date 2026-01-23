"""
store your name, age, and favorite number in variables.
print a sentence using them.
"""

name = "dee"
age = 21
fav_num = 3

# method 1 - using f string
first_sentence = f"my name is {name} and i'm {age} years old. my favourite number is {fav_num}."
print(first_sentence)

# method 2 - using concatenation and str
second_sentence = "my name is "+ name + " and i'm " + str(age) + " years old. my favourite number is " + str(fav_num) + "."
print(second_sentence)

# method 3 - using format
third_sentence = "my name is {} and i'm {} years old. my favourite number is {}.".format(name, age, fav_num)
print(third_sentence)