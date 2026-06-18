# Scatter Plot with Text Labels
import matplotlib.pyplot as plt
x = [2, 4, 6, 8, 10]
y = [10, 15, 7, 20, 13]

names = ["A", "B", "C", "D", "E"]

plt.figure(figsize=(7, 5))

plt.scatter(
    x,
    y,
    color="orange",
    s=250,
    edgecolors="black"
)

for i in range(len(x)):
    plt.text(x[i] + 0.2, y[i] + 0.2, names[i], fontsize=10)

plt.title("Students")
plt.grid(True)

plt.show()