t = tuple(map(int, input("Enter elements: ").split()))

total = sum(t)
avg = total / len(t)

print("Sum:", total)
print("Average:", avg)