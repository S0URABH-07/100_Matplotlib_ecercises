import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")

salary = (df.groupby(["Department", "EducationField"])["MonthlyIncome"].mean().reset_index())

pivot = salary.pivot(
    index="Department",
    columns="EducationField",
    values="MonthlyIncome"
)

pivot.plot(
    kind="bar",
    figsize=(12,6)
)

plt.title("Average Salary by Department and Education Field")
plt.ylabel("Average Monthly Income")
plt.xticks(rotation=20)

plt.show()