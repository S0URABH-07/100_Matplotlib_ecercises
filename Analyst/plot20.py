import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
analysis = (df.groupby("PerformanceRating").agg(AverageSalaryHike=("PercentSalaryHike", "mean")).reset_index())

plt.figure(figsize=(8,5))

plt.plot(
    analysis["PerformanceRating"],
    analysis["AverageSalaryHike"],
    marker="o",
    linewidth=3
)

plt.xlabel("Performance Rating")
plt.ylabel("Average Salary Hike (%)")
plt.title("Performance Rating vs Salary Hike")

plt.grid(True)

plt.show()