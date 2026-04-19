class Student:
    def __init__(self):
        self.__marks = 0   # private variable

    def set_marks(self, m):
        self.__marks = m

    def get_marks(self):
        return self.__marks

s = Student()
s.set_marks(90)
print("Marks:", s.get_marks())