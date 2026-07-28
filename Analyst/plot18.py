import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
overtime = (
    df.groupby("JobRole").agg(OvertimeRate=("OverTime",lambda x: (x == "Yes").mean() * 100)).sort_values("OvertimeRate", ascending=False).reset_index())

plt.figure(figsize=(12,6))

plt.barh(
    overtime["JobRole"],
    overtime["OvertimeRate"]
)

plt.xlabel("Overtime Rate (%)")
plt.ylabel("Job Role")
plt.title("Overtime Rate by Job Role")

plt.show()