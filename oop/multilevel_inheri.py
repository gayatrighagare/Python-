class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(B):
    def print_msg(self):
        print("Class C")

obj = C()
obj.show()
obj.display()
obj.print_msg()