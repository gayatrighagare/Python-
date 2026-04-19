lst = list(map(int, input("Enter numbers: ").split()))

lst = list(set(lst))  # remove duplicates
lst.sort()

print("Second Largest:", lst[-2])