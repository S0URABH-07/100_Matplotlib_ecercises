import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
travel = (
    df.groupby("BusinessTravel").agg(
          AttritionRate=(
              "Attrition",
              lambda x: (x == "Yes").mean() * 100
          )
      ).reset_index()
)
plt.figure(figsize=(8,5))

plt.bar(
    travel["BusinessTravel"],
    travel["AttritionRate"]
)

plt.title("Attrition Rate by Business Travel")
plt.xlabel("Business Travel")
plt.ylabel("Attrition Rate (%)")

plt.show()