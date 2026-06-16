# Draw Bar plot and write label
import matplotlib.pyplot as plt
x = ["a","b","c","d","e","f"]
y = [ 10,15,20,25,30,35]
plt.xlabel("Name")
plt.ylabel("No.")
plt.bar(x,y)
plt.show()