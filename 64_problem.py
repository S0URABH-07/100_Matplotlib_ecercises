# weights – Weighted Histogram
# Instead of counting each value equally, each value contributes according to its weight.
import matplotlib.pyplot as plt

values = [1, 2, 3, 4]
weights = [10, 20, 5, 15]

plt.hist(
    values,
    bins=4,
    weights=weights,
    edgecolor="black"
)

plt.show()