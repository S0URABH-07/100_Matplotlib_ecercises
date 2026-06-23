# stack(area) plot and add grid ,axis label or title
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
area1 = [10,20,30,40,50]
area2 = [5,10,15,20,25]
area3 = [15,25,35,45,55]
l = ["area1" , "area2","area3"]

plt.stackplot(x,area1,area2 , area3 , labels=l , colors=["r","y","m"] ,baseline="wiggle")
plt.title("Stack(area)")
plt.xlabel("x-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.legend(loc=2)

plt.savefig("Stack_plot")
plt.show()