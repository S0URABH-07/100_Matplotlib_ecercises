# Change Color and Border
import matplotlib.pyplot as plt

ages = [18,20,22,22,23,24,25,26,27,28,30,30,31]

plt.hist(
    ages,
    bins=6,
    color="skyblue",
    edgecolor="black"
)
plt.show()