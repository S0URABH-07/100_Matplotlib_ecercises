# Box plot and show mean point or outlier
import matplotlib.pyplot as plt
x = [10,20,30,40,50,60,70,125]

plt.boxplot(x ,labels=["python"] , patch_artist=True , showmeans=True)
plt.show()