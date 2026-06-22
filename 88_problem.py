# Box plot with labels and fill color on the BOX
import matplotlib.pyplot as plt
x = [10,20,30,40,50,60,70]

plt.boxplot(x ,labels=["python"] , patch_artist=True)
plt.show()