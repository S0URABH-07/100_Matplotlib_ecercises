import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Analytics.csv")
analysis = df[
    [
        "TotalWorkingYears",
        "MonthlyIncome",
        "Attrition"
    ]
]
left = analysis[
    analysis["Attrition"] == "Yes"
]

stay = analysis[
    analysis["Attrition"] == "No"
]

plt.figure(figsize=(10,6))

plt.scatter(stay["TotalWorkingYears"],stay["MonthlyIncome"],label="Stayed")

plt.scatter(left["TotalWorkingYears"],left["MonthlyIncome"],label="Left")

plt.xlabel("Experience")

plt.ylabel("Monthly Income")

plt.title("Experience vs Salary")

plt.legend()

plt.show()