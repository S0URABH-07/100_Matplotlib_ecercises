# Highlight One Important Point
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.scatter(x, y)

plt.scatter([3], [6], s=300, color="red", marker="*")

plt.title("Highlight a Special Point")
plt.show()