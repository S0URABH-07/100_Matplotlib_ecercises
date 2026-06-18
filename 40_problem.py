# Invert the Y-Axis and X-Axis values
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.scatter(x, y)

plt.gca().invert_yaxis()
plt.gca().invert_xaxis()

plt.show()