# Set Bin Ranges Manually
import matplotlib.pyplot as plt

marks = [35,42,48,50,55,60,67,72,78,81,90,93]

plt.hist(
    marks,
    bins=[30,40,50,60,70,80,90,100],
    color="orange",
    edgecolor="black"
)

plt.show()