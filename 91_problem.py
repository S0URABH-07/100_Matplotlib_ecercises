# Box plot and change box,cap,whis color
import matplotlib.pyplot as plt
x = [10,20,30,40,50,60,70]

plt.boxplot(x ,labels=["python"] , patch_artist=True , showmeans=True ,boxprops={"color":"r"},capprops={"color":"b"} , whiskerprops={"color":"y"})
plt.show()