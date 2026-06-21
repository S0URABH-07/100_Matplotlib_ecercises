# Pie chart and add labels
import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]

plt.pie(x,labels=y)
plt.show()