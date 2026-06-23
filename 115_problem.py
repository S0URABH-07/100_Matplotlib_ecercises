# Step plot and add label or change step color and add grid()
import matplotlib.pyplot as plt
x = [5,10,15,20,25,30]
y = [1,6,3,2,5,4]

plt.step(x , y ,color="r" , marker="o" , ms=10 , mfc="b" , label="Step")
plt.title("Step plot")
plt.xlabel("x-axis")
plt.ylabel("Y-axis")
plt.legend(loc=4)
plt.grid()
plt.savefig("Step_plot")
plt.show()