# Different Color for Each Point
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 7, 3, 8, 4]

colors = ["red", "blue", "green", "orange", "purple"]

plt.scatter(x, y, c=colors)
plt.show()