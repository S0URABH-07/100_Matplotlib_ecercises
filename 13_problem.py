# Draw Bar plot and make a label using legend fnxn
import matplotlib.pyplot as plt
x = ["a","b","c","d","e","f"]
y = [ 10,15,20,25,30,35]
plt.xlabel("Name",fontsize=10)
plt.ylabel("No.",fontsize=15)
plt.title("Bar Plot")
c = ["y",'b','r',"g"]
plt.bar(x,y,width=0.5,color=c,edgecolor="r",label="Sourabh")
plt.legend()
plt.show()