# Data Science Style Histogram
import matplotlib.pyplot as plt

house_prices = [
    120,150,180,200,220,240,
    260,280,300,320,340,360,
    400,450,500
]

plt.figure(figsize=(8,5))

plt.hist(
    house_prices,
    bins=8,
    color="steelblue",
    edgecolor="black",
    linewidth=1.5,
    alpha=0.8,
    rwidth=0.9
)

plt.title("Distribution of House Prices")
plt.xlabel("Price (Thousands)")
plt.ylabel("Frequency")

plt.grid(axis="y", linestyle="--")

plt.show()