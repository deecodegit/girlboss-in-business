"""
calculate the sum of numbers from 1 to 100 using a loop.
"""

# method 1 - simple for loop
total = 0 

for i in range(1, 101):
    total += i

print(total)

# method 2 - using range
print(sum(range(1, 101)))

# method 3 - using formula n(n+1)/2
n = 100
print(n * (n + 1) // 2)

