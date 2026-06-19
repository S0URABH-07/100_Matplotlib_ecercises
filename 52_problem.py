# Histogram chart with more understanding
import matplotlib.pyplot as plt
marks = [45, 50, 100, 60, 60, 65, 70, 75, 80, 89, 90]

plt.hist(
    marks,
    bins=5,
    edgecolor="black",
    color="skyblue"
)

plt.show()