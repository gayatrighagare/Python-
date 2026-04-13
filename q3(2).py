#swapping numbers without temp
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))

a,b=b,a
print("after swap:",a,b)