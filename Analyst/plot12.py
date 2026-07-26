import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
plt.figure(figsize=(12,6))

departments = df["Department"].unique()

salary = [df[df["Department"] == d]["MonthlyIncome"] for d in departments]

plt.boxplot(salary,tick_labels=departments)

plt.xticks(rotation=20)

plt.title("Salary Distribution by Department")

plt.ylabel("Monthly Income")

plt.show()