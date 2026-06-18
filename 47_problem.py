# Advanced Scatter with Axis Limits and Tick Marks
import matplotlib.pyplot as plt
x = [5, 10, 15, 20, 25]
y = [30, 20, 35, 25, 40]

plt.figure(figsize=(8, 5))

plt.scatter(x,y,color="purple",marker="P",s=350,alpha=0.8,edgecolors="black",linewidths=2,label="Data")

plt.xlim(0, 30)
plt.ylim(10, 50)

plt.xticks([0, 5, 10, 15, 20, 25, 30])
plt.yticks([10, 20, 30, 40, 50])

plt.grid(True, linestyle=":")
plt.legend()

plt.title("Advanced Axis Control")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()