"""
create a list of 5 cities you like.
print:
1. the first city
2. the last city
3. the total number of cities
"""

cities = ["kolkata", "bengaluru", "mumbai", "delhi", "vasco"]

# method 1 - using -1 indexing and len function

print(cities[0])
print(cities[-1])
print(len(cities))

# method 2 - using exact indices and len function
print(cities[0])
print(cities[4])
print(len(cities))

# method 3 - using exact indices and len function with a new variable
count = len(cities)

print(cities[0])
print(cities[4])
print(count)
