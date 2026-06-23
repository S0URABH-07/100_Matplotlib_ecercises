# Ring pie chart 
import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]
z = [40,30,20,10]

plt.pie(x, labels=y , radius=1)
plt.pie([1] , colors="w",radius=0.6)

plt.savefig("RingPieChart",dpi=300,facecolor="m",bbox_inches="tight")
plt.show()