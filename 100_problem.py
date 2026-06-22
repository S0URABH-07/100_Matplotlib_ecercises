# Fill_between plot 
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.plot(x,y,color="r")
plt.fill_between(x=[2,4],y1=2,y2=4 , color="y")

plt.title("Fill_between plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()