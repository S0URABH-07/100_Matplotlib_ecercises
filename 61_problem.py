# range – Ignore Values Outside a Range
import matplotlib.pyplot as plt

marks = [10, 20, 30, 40, 50, 60, 70, 80, 90]

plt.hist(
    marks,
    bins=4,
    range=(20, 80),
    edgecolor="black"
)

plt.show()