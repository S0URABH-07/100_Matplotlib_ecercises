# Draw Bar plot and change color of bars with diffrent colors
import matplotlib.pyplot as plt
x = ["a","b","c","d","e","f"]
y = [ 10,15,20,25,30,35]
plt.xlabel("Name",fontsize=10)
plt.ylabel("No.",fontsize=15)
plt.title("Bar Plot")
c = ["y",'b','r',"g"]
plt.bar(x,y,width=0.5,color=c)
plt.show()