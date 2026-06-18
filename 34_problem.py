# Bubble Chart (Different Color + Different Size)
import matplotlib.pyplot as plt
x = [10, 20, 30, 40]
y = [15, 35, 25, 45]

sizes = [100, 300, 500, 700]
colors = ["red", "green", "blue", "orange"]

plt.scatter(x, y, s=sizes, c=colors)

plt.title("Bubble Chart")
plt.show()