# Draw Bar plot and change font size
import matplotlib.pyplot as plt
x = ["a","b","c","d","e","f"]
y = [ 10,15,20,25,30,35]
plt.xlabel("Name",fontsize=10)
plt.ylabel("No.",fontsize=15)
plt.title("Bar Plot")
plt.bar(x,y)
plt.show()