class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

obj = B()
obj.show()
obj.display()