# Compare Two Histograms
# Two histograms are drawn together using transparency so that overlapping regions remain visible.
import matplotlib.pyplot as plt

class_a = [45,50,55,60,65,70,75,80]
class_b = [40,48,52,58,62,68,72,78]

plt.hist(
    class_a,
    bins=5,
    alpha=0.5,
    label="Class A"
)

plt.hist(
    class_b,
    bins=5,
    alpha=0.5,
    label="Class B"
)

plt.legend()
plt.show()