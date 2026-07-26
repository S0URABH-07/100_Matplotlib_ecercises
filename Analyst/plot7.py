import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("HR_Analytics.csv")
salary = df.groupby("Gender")["MonthlyIncome"].mean()

plt.bar(salary.index,salary.values)

plt.show()