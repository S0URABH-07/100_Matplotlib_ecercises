import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("HR_Analytics.csv")
plt.figure(figsize=(8,5))

plt.scatter(df["TotalWorkingYears"],df["MonthlyIncome"])

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()