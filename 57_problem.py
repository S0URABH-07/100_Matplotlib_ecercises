# Relative Bar Width in Histogram
import matplotlib.pyplot as plt

values = [1,2,2,3,3,4,4,5,6,7]

plt.hist(
    values,
    bins=6,
    rwidth=0.8,
    color="gold",
    edgecolor="black"
)

plt.show()