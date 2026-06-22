# Step plot add marker and change their size or color and change step color
import matplotlib.pyplot as plt
x = [5,10,15,20,25,30]
y = [1,6,3,2,5,4]

plt.step(x , y ,color="r" , marker="o" , ms=10 , mfc="b")
plt.title("Step plot")
plt.xlabel("x-axis")
plt.ylabel("Y-axis")
plt.show()