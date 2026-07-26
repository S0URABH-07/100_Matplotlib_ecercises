import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("HR_Analytics.csv")
salary = (df.groupby("JobRole")["MonthlyIncome"].mean().sort_values())

plt.figure(figsize=(12,5))

plt.barh(salary.index, salary.values)

plt.show()