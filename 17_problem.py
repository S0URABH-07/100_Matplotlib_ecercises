# Draw two Bar plot without overlape and show Language names using xticks
import matplotlib.pyplot as plt
import numpy as np

x = ["python","c","c++","java"]
y = [10,20,30,40]
z = [80,25,48,12]

width = 0.3
p = np.arange(len(x))
p1 = [j+width for j in p]

plt.xlabel("language" , fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("Bar Plot",fontsize=20)

plt.bar(p,y,width,color='r',label="Chart 1")
plt.bar(p1,z,width,color='y',label="Chart 2")

plt.xticks(p+width/2, x)
plt.legend()

plt.show()