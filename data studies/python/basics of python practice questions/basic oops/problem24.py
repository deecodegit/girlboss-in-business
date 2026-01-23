"""
create a Student class with:
1. name
2. marks
3. add a method that returns "pass" or "fail".
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def result(self):
        if self.marks > 40:
            print("pass")
        else:
            print("fail")

s1 = Student("arya", 85)
s2 = Student("sansa", 35)

print(f"{s1.name} scored {s1.marks} marks.")
s1.result()

print(f"{s2.name} scored {s2.marks} marks.")
s2.result()
