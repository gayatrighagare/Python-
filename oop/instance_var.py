class Student:
    college = "GCEK"   # class variable

    def __init__(self, name):
        self.name = name     # instance variable

s1 = Student("gayatri")
s2 = Student("priyanka")

print(s1.name, s1.college)
print(s2.name, s2.college)