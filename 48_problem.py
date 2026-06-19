#  Bar Graph and Add Borders and Transparency
import matplotlib.pyplot as plt

cities = ["Delhi", "Mumbai", "Pune", "Bhopal"]
population = [30, 22, 12, 8]

plt.bar(
    cities,
    population,
    color="skyblue",
    edgecolor="black",
    linewidth=2,
    alpha=0.7
)

plt.title("City Population")
plt.show()