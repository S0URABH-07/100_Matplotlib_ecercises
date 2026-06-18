# Add Dashed Grid 
import matplotlib.pyplot as plt
x = [2, 4, 6, 8]
y = [1, 3, 5, 7]

plt.scatter(x, y)

plt.grid(linestyle="--")

plt.show()