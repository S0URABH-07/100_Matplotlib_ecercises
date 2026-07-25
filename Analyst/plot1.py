import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("HR_Analytics.csv")

dept = df["Department"].value_counts()

plt.figure(figsize=(8,5))
plt.bar(dept.index, dept.values)
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")
plt.xticks(rotation=20)
plt.show()