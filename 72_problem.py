# Pie chart and increse pie chart size
import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]
z = [0.1,0.0,0.0,0.0]
clr = ["b","y","g","r"]

plt.pie(x,labels=y, explode=z, colors=clr, autopct="%0d%%" , shadow=True , radius=1.5)
plt.show()