# Fully Customized Scatter Plot
import matplotlib.pyplot as plt
x = [10, 20, 30, 40, 50]
y = [15, 25, 10, 35, 20]

plt.figure(figsize=(8, 6))

plt.scatter(x,y,c="red",s=300,marker="D",alpha=0.6,edgecolors="black",linewidths=3,label="Sales Data")

plt.title("Customized Scatter Plot", fontsize=18)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales", fontsize=12)
plt.grid(True, linestyle="--")
plt.legend()
plt.show()