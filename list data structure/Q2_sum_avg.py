lst = list(map(int, input("Enter numbers: ").split()))

total = sum(lst)
avg = total / len(lst)

print("Sum:", total)
print("Average:", avg)