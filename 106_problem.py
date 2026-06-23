# Combine multiple parameter And Draw Scatter Chart
# Save figure in pdf format with high quality and padding
import matplotlib.pyplot as plt

x = [2, 3, 7, 2, 5, 9, 4, 6]
y = [8, 1, 3, 4, 6, 1, 0, 5]

plt.scatter(x,y,color="purple",s=150,marker="*",alpha=0.7,label="Data Points")

plt.title("Customized Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.legend()
plt.savefig("Scatterplot.pdf",dpi=400,facecolor="y")
plt.show()