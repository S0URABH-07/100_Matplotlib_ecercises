# Bubble Chart with Individual Colors and Sizes
import matplotlib.pyplot as plt
x = [5, 10, 15, 20, 25]
y = [20, 35, 15, 40, 30]

sizes = [100, 500, 800, 300, 700]
colors = ["red", "green", "blue", "orange", "purple"]

plt.figure(figsize=(9, 5))

plt.scatter(x,y,s=sizes,c=colors,alpha=0.7,edgecolors="black",linewidths=2)

plt.title("Bubble Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)

plt.show()