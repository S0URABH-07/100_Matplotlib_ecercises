# Draw Bar plot and write label
import matplotlib.pyplot as plt
x = ["a","b","c","d"]
y = [ 10,15,20,25]
plt.xlabel("Name")
plt.ylabel("No.")
plt.bar(x,y)
plt.show()