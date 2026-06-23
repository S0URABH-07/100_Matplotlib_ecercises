# Multiple Marker Styles Together
# Save image
import matplotlib.pyplot as plt
plt.scatter([1, 2], [3, 4], marker="o", s=200, label="Circle")
plt.scatter([3, 4], [5, 6], marker="s", s=200, label="Square")
plt.scatter([5, 6], [7, 8], marker="^", s=200, label="Triangle")

plt.legend()
plt.savefig("Scatter_sym",dpi=300,facecolor="g")
plt.show()