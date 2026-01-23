"""
given:
marks = 72
print:
1. "fail" if < 40
2. "pass" if 40-59
3. "good" if 60-79
4. "excellent" if 80+
"""

marks = int(input("enter marks: ")) 
print(marks)

#method 1 - using proper comparisons
if marks < 40:
    print("fail")
elif 40 <= marks <= 59:
    print("pass")
elif 60 <= marks <= 79:
    print("good")
else:
    print("excellent")

# method 2 - cleaner comparisons
if marks < 40:
    print("fail")
elif marks < 60:
    print("pass")
elif marks < 80:
    print("good")
else:
    print("excellent")