# Multiple pie chart 
import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]
z = [40,30,20,10]
clr = ["r","y","g","b"]

plt.pie(x, labels=y , radius=1.5)
plt.pie(z, radius=1, colors=clr)

plt.show()