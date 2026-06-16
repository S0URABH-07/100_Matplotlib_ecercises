# Draw Bar plot and add bar boundry color and increse linewidth
import matplotlib.pyplot as plt
x = ["a","b","c","d","e","f"]
y = [ 10,15,20,25,30,35]
plt.xlabel("Name",fontsize=10)
plt.ylabel("No.",fontsize=15)
plt.title("Bar Plot")
c = ["y",'b','r',"g"]
plt.bar(x,y,width=0.5,color=c,align="edge",edgecolor="r",linewidth=5)
plt.show()