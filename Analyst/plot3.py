import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("HR_Analytics.csv")
plt.figure(figsize=(8,5))
plt.hist(df["MonthlyIncome"], bins=20)
plt.title("Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Employees")
plt.show()