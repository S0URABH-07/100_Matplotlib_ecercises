# Cumulative Histogram
import matplotlib.pyplot as plt

data = [10,20,20,30,30,30,40,40,50]

plt.hist(
    data,
    bins=5,
    cumulative=True,
    color="teal"
)
# Each bar includes all previous counts, creating a running total.cumulative=True
plt.show()