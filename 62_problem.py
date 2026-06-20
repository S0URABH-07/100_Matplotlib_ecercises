# stacked=True – Stack Multiple Histograms
# Useful when comparing multiple datasets in one chart.
import matplotlib.pyplot as plt

group1 = [10, 20, 30, 40]
group2 = [15, 25, 35, 45]

plt.hist(
    [group1, group2],
    bins=5,
    stacked=True,
    label=["Group 1", "Group 2"]
)

plt.legend()
plt.show()