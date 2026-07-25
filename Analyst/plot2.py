import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("HR_Analytics.csv")
salary = df.groupby("Department")["MonthlyIncome"].mean()

plt.figure(figsize=(8,5))
plt.bar(salary.index, salary.values)
plt.title("Average Salary by Department")
plt.xticks(rotation=20)
plt.show()