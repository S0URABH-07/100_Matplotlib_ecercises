# stack(area) plot with labels and colors
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
area1 = [10,20,30,40,50]
area2 = [5,10,15,20,25]
area3 = [15,25,35,45,55]
l = ["area1" , "area2","area3"]

plt.stackplot(x,area1,area2 , area3 , labels=l , colors=["r","y","m"] )
plt.legend(loc=2)
plt.show()