# Save the Plot as an Image
import matplotlib.pyplot as plt
x1 = [1, 2, 3]
y1 = [4, 5, 6]

x2 = [1, 2, 3]
y2 = [7, 3, 5]

plt.scatter(x1, y1, color="blue", label="Class A",s=200)
plt.scatter(x2, y2, color="green", label="Class B",s=200)

plt.savefig("scatter_plot.png")
plt.legend()
plt.show()