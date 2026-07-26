import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("HR_Analytics.csv")
plt.hist(df["Age"], bins=15)
plt.title("Age Distribution")
plt.show()