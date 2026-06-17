# Different Size for Every Point
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 3, 8, 2, 7]

sizes = [50, 100, 200, 300, 500]

plt.scatter(x, y, s=sizes)
plt.title("Different Size for Each Point")
plt.show()