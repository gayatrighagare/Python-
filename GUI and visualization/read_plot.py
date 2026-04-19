import matplotlib.pyplot as plt

x = []
y = []

f = open("data.txt", "r")

for line in f:
    a, b = map(int, line.split())
    x.append(a)
    y.append(b)

f.close()

plt.plot(x, y)
plt.show()