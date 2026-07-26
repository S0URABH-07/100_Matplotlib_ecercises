import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("HR_Analytics.csv")
attrition = df["Attrition"].value_counts()

plt.pie(attrition.values,labels=attrition.index,autopct="%1.1f%%")

plt.show()