# align – Align Bins
import matplotlib.pyplot as plt

data = [2, 3, 4, 5, 6, 7]

plt.hist(
    data,
    bins=5,
    align="left",
    edgecolor="black"
)

plt.show()