# Histogram ->A Realistic Data Science Example
import matplotlib.pyplot as plt

salary = [
    30000, 35000, 40000, 42000, 45000,
    50000, 55000, 60000, 65000, 70000,
    75000, 80000, 85000
]

plt.figure(figsize=(8, 5))

plt.hist(
    salary,
    bins=6,
    color="steelblue",
    edgecolor="black",
    linewidth=1.5,
    alpha=0.8,
    rwidth=0.9,
    label="Employees"
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.grid(axis="y", linestyle="--")
plt.legend()

plt.show()