import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")

salary_std = (
    df.groupby("Department").agg(
          AverageSalary=("MonthlyIncome", "mean"),
          SalaryVariation=("MonthlyIncome", "std")
      ).sort_values("SalaryVariation", ascending=False)
)
plt.figure(figsize=(8,5))

plt.bar(
    salary_std.index,
    salary_std["SalaryVariation"]
)

plt.title("Salary Variation by Department")
plt.xlabel("Department")
plt.ylabel("Standard Deviation")
plt.xticks(rotation=20)

plt.show()