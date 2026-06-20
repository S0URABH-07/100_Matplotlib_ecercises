# log=True – Logarithmic Scale
# Helpful when frequencies span a very wide range.
import matplotlib.pyplot as plt
data = [1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]

plt.hist(
    data,
    bins=5,
    log=True
)

plt.show()