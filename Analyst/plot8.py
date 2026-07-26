import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("HR_Analytics.csv")
departments = df["Department"].unique()

data = [df[df["Department"] == dept]["MonthlyIncome"] for dept in departments]

plt.boxplot(data, labels=departments)

plt.xticks(rotation=20)

plt.show()