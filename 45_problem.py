# Three Datasets with Different Styles
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))

plt.scatter(
    [1, 2, 3],
    [4, 5, 6],
    color="red",
    marker="o",
    s=200,
    label="Group A"
)

plt.scatter(
    [1, 2, 3],
    [7, 8, 5],
    color="blue",
    marker="^",
    s=250,
    label="Group B"
)

plt.scatter(
    [1, 2, 3],
    [2, 3, 1],
    color="green",
    marker="*",
    s=350,
    label="Group C"
)

plt.title("Multiple Scatter Groups")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)

plt.show()