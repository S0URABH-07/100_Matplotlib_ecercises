# Density Histogram
# save figure 
import matplotlib.pyplot as plt

scores = [55,60,62,65,68,70,72,75,78,80,82,85]

plt.hist(
    scores,
    bins=6,
    density=True,
    color="red"
)
plt.savefig("Histogram",facecolor="y",transparent=True)
plt.show()