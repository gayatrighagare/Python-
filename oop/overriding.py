class A:
    def show(self):
        print("Parent class")

class B(A):
    def show(self):
        print("Child class")

obj = B()
obj.show()