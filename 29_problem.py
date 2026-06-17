# Add Black Borders Around Points
import matplotlib.pyplot as plt
x = [2, 4, 6, 8]
y = [1, 3, 5, 7]

plt.scatter(x,y,s=200,edgecolors="black",linewidths=2)

plt.title("Scatter with Borders")
plt.show()