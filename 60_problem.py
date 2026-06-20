# histtype – Different Drawing Styles
import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 30, 40, 50]

plt.hist(
    data,
    bins=5,
    histtype="step",
    linewidth=2
)

plt.show()