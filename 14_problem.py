# Draw two Bar plot in one code
import matplotlib.pyplot as plt
x = ["a","b","c","d","e","f"]
y = [ 10,15,20,25,30,35]
z = [2,6,3,7,3,5]
plt.xlabel("Name",fontsize=10)
plt.ylabel("No.",fontsize=15)
plt.title("Bar Plot")
plt.bar(x,y,width=0.5,color="r",label="Popularity")
plt.bar(x,z,width=0.5,color="y",label="Popularity1")
plt.legend()
plt.show()