# Fill_between plot with numpy
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])

plt.plot(x,y,color="r")
plt.fill_between(x,y,color="y" , where=(x>=2) & (x<=4),alpha=0.4)

plt.title("Fill_between plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.savefig("Fill_between")
plt.show()