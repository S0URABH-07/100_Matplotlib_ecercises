# Pie chart and explode the part of c
import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]
z = [0.1,0.0,0.0,0.0]

plt.pie(x,labels=y, explode=z)
plt.show()