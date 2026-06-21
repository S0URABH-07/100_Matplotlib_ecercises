# Pie chart and change label font size using textprops
import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]
z = [0.1,0.0,0.0,0.0]
clr = ["b","y","g","r"]

plt.pie(x,labels=y, explode=z, colors=clr, autopct="%0d%%" , shadow=True , radius=1.1 , startangle=90 , textprops={"fontsize":15})
plt.show()