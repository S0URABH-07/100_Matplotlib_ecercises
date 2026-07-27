import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
department = (
    df.groupby("Department")
      .agg(
          AttritionRate=(
              "Attrition",
              lambda x: (x == "Yes").mean() * 100
          ),
          OvertimeRate=(
              "OverTime",
              lambda x: (x == "Yes").mean() * 100
          )
      )
      .reset_index()
)

plt.figure(figsize=(10,6))

x = range(len(department))

plt.bar(
    x,
    department["AttritionRate"],
    width=0.4,
    label="Attrition"
)

plt.bar(
    [i + 0.4 for i in x],
    department["OvertimeRate"],
    width=0.4,
    label="Overtime"
)

plt.xticks([i + 0.2 for i in x],department["Department"])

plt.legend()

plt.title("Department-wise Attrition vs Overtime")

plt.show()