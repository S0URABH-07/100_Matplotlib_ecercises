# Box plot and remove outlier and join whis to end point
import matplotlib.pyplot as plt
x = [10,20,30,40,50,60,70,125]

plt.boxplot(x ,labels=["python"] , patch_artist=True , showmeans=True , whis=2)
plt.show()