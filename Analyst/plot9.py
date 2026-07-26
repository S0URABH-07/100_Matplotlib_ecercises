import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("HR_Analytics.csv")
corr = df.corr(numeric_only=True)

plt.imshow(corr)

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)

plt.yticks(range(len(corr.columns)), corr.columns)

plt.show()