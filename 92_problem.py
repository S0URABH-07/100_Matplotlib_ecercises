# Draw two Box plot
import matplotlib.pyplot as plt
x = [10,20,30,40,50,60,70]
y = [20,40,60,80,100,120,140]

list = [x,y]
plt.boxplot(list ,labels=["python","C++"] , patch_artist=True)
plt.show()