lst = list(map(int, input("Enter numbers: ").split()))
x = int(input("Enter element to search: "))

if x in lst:
    print("Found")
else:
    print("Not Found")
    