# Annotate (Label) Each Point
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [4, 7, 5]

plt.scatter(x, y)

plt.text(1, 4, "A")
plt.text(2, 7, "B")
plt.text(3, 5, "C")

plt.title("Scatter with Labels")
plt.show()