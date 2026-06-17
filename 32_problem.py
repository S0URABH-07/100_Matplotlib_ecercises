# Set Axis Limits 
import matplotlib.pyplot as plt
x = [2, 4, 6, 8]
y = [1, 5, 3, 7]

plt.scatter(x, y)

plt.xlim(0, 50)
plt.ylim(0, 8)

plt.title("Custom Axis Limits")
plt.show()