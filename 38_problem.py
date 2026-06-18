# Change X and Y Ticks
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.scatter(x, y)

plt.xticks([1, 2, 3, 4])
plt.yticks([10, 20, 30, 40])

plt.show()