# Horizontal Histogram
import matplotlib.pyplot as plt

data = [2,4,5,5,6,7,8,8,9,10]

plt.hist(
    data,
    bins=5,
    orientation="horizontal",
    color="purple",
    edgecolor="red"
)

plt.show()